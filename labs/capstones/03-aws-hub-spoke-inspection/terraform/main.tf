# Capstone 3: hub-and-spoke on Transit Gateway with a centralized inspection + egress VPC.
# Traffic flows:
#   spoke -> TGW (spoke RT: 0/0 -> inspection) -> inspection TGW subnet -> Network Firewall endpoint
#         -> (east-west) back to TGW (firewall RT: spoke routes) -> other spoke
#         -> (egress) NAT gateway -> internet gateway

terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.40, < 7.0"
    }
  }
}

provider "aws" {
  region = var.region
  default_tags {
    tags = { Project = "networking-mastery", Capstone = "03-hub-spoke-inspection" }
  }
}

data "aws_availability_zones" "this" {
  state = "available"
}

data "aws_ssm_parameter" "al2023_arm" {
  name = "/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-arm64"
}

locals {
  azs      = slice(data.aws_availability_zones.this.names, 0, var.az_count)
  supernet = "10.0.0.0/8"

  spoke_subnets = merge([
    for s, cidr in var.spokes : merge(
      { for i, az in local.azs : "${s}-workload-${az}" => { spoke = s, az = az, tier = "workload", cidr = cidrsubnet(cidr, 8, i) } },
      { for i, az in local.azs : "${s}-tgw-${az}" => { spoke = s, az = az, tier = "tgw", cidr = cidrsubnet(cidr, 12, 4080 + i) } }
    )
  ]...)

  insp_subnets = merge(
    { for i, az in local.azs : "tgw-${az}" => { az = az, tier = "tgw", cidr = cidrsubnet(var.inspection_cidr, 12, i) } },
    { for i, az in local.azs : "firewall-${az}" => { az = az, tier = "firewall", cidr = cidrsubnet(var.inspection_cidr, 12, 16 + i) } },
    { for i, az in local.azs : "public-${az}" => { az = az, tier = "public", cidr = cidrsubnet(var.inspection_cidr, 12, 32 + i) } }
  )

  # Map AZ -> Network Firewall endpoint ID (one endpoint per firewall subnet)
  fw_endpoint_by_az = {
    for ss in aws_networkfirewall_firewall.this.firewall_status[0].sync_states :
    ss.availability_zone => ss.attachment[0].endpoint_id
  }
}

# ================================================================ Spoke VPCs
resource "aws_vpc" "spoke" {
  for_each             = var.spokes
  cidr_block           = each.value
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags                 = { Name = "cap3-${each.key}" }
}

resource "aws_subnet" "spoke" {
  for_each          = local.spoke_subnets
  vpc_id            = aws_vpc.spoke[each.value.spoke].id
  availability_zone = each.value.az
  cidr_block        = each.value.cidr
  tags              = { Name = "cap3-${each.key}" }
}

resource "aws_route_table" "spoke" {
  for_each = var.spokes
  vpc_id   = aws_vpc.spoke[each.key].id
  tags     = { Name = "cap3-${each.key}-rt" }
}

resource "aws_route" "spoke_default" {
  for_each               = var.spokes
  route_table_id         = aws_route_table.spoke[each.key].id
  destination_cidr_block = "0.0.0.0/0"
  transit_gateway_id     = aws_ec2_transit_gateway.this.id
  depends_on             = [aws_ec2_transit_gateway_vpc_attachment.spoke]
}

resource "aws_route_table_association" "spoke" {
  for_each       = { for k, v in local.spoke_subnets : k => v if v.tier == "workload" }
  subnet_id      = aws_subnet.spoke[each.key].id
  route_table_id = aws_route_table.spoke[each.value.spoke].id
}

# ================================================================ Inspection VPC
resource "aws_vpc" "insp" {
  cidr_block           = var.inspection_cidr
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags                 = { Name = "cap3-inspection" }
}

resource "aws_subnet" "insp" {
  for_each          = local.insp_subnets
  vpc_id            = aws_vpc.insp.id
  availability_zone = each.value.az
  cidr_block        = each.value.cidr
  tags              = { Name = "cap3-insp-${each.key}" }
}

resource "aws_internet_gateway" "insp" {
  vpc_id = aws_vpc.insp.id
  tags   = { Name = "cap3-igw" }
}

resource "aws_eip" "nat" {
  for_each = toset(local.azs)
  domain   = "vpc"
  tags     = { Name = "cap3-nat-${each.key}" }
}

resource "aws_nat_gateway" "insp" {
  for_each      = toset(local.azs)
  allocation_id = aws_eip.nat[each.key].id
  subnet_id     = aws_subnet.insp["public-${each.key}"].id
  tags          = { Name = "cap3-nat-${each.key}" }
  depends_on    = [aws_internet_gateway.insp]
}

# Route tables per AZ, per tier (keeps traffic in the same AZ: symmetric through the firewall)
resource "aws_route_table" "insp_tgw" {
  for_each = toset(local.azs)
  vpc_id   = aws_vpc.insp.id
  tags     = { Name = "cap3-insp-tgw-${each.key}" }
}

resource "aws_route" "insp_tgw_to_fw" {
  for_each               = toset(local.azs)
  route_table_id         = aws_route_table.insp_tgw[each.key].id
  destination_cidr_block = "0.0.0.0/0"
  vpc_endpoint_id        = local.fw_endpoint_by_az[each.key]
}

resource "aws_route_table" "insp_fw" {
  for_each = toset(local.azs)
  vpc_id   = aws_vpc.insp.id
  tags     = { Name = "cap3-insp-firewall-${each.key}" }
}

resource "aws_route" "insp_fw_to_tgw" {
  for_each               = toset(local.azs)
  route_table_id         = aws_route_table.insp_fw[each.key].id
  destination_cidr_block = local.supernet
  transit_gateway_id     = aws_ec2_transit_gateway.this.id
  depends_on             = [aws_ec2_transit_gateway_vpc_attachment.insp]
}

resource "aws_route" "insp_fw_to_nat" {
  for_each               = toset(local.azs)
  route_table_id         = aws_route_table.insp_fw[each.key].id
  destination_cidr_block = "0.0.0.0/0"
  nat_gateway_id         = aws_nat_gateway.insp[each.key].id
}

resource "aws_route_table" "insp_public" {
  for_each = toset(local.azs)
  vpc_id   = aws_vpc.insp.id
  tags     = { Name = "cap3-insp-public-${each.key}" }
}

resource "aws_route" "insp_public_to_igw" {
  for_each               = toset(local.azs)
  route_table_id         = aws_route_table.insp_public[each.key].id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.insp.id
}

# Return traffic from the NAT gateway to spokes must pass the firewall again (same AZ endpoint)
resource "aws_route" "insp_public_to_fw" {
  for_each               = toset(local.azs)
  route_table_id         = aws_route_table.insp_public[each.key].id
  destination_cidr_block = local.supernet
  vpc_endpoint_id        = local.fw_endpoint_by_az[each.key]
}

resource "aws_route_table_association" "insp" {
  for_each  = local.insp_subnets
  subnet_id = aws_subnet.insp[each.key].id
  route_table_id = (
    each.value.tier == "tgw" ? aws_route_table.insp_tgw[each.value.az].id :
    each.value.tier == "firewall" ? aws_route_table.insp_fw[each.value.az].id :
    aws_route_table.insp_public[each.value.az].id
  )
}

# ================================================================ Transit Gateway
resource "aws_ec2_transit_gateway" "this" {
  description                     = "cap3 hub"
  default_route_table_association = "disable"
  default_route_table_propagation = "disable"
  tags                            = { Name = "cap3-tgw" }
}

resource "aws_ec2_transit_gateway_vpc_attachment" "spoke" {
  for_each                                        = var.spokes
  transit_gateway_id                              = aws_ec2_transit_gateway.this.id
  vpc_id                                          = aws_vpc.spoke[each.key].id
  subnet_ids                                      = [for k, v in local.spoke_subnets : aws_subnet.spoke[k].id if v.spoke == each.key && v.tier == "tgw"]
  transit_gateway_default_route_table_association = false
  transit_gateway_default_route_table_propagation = false
  tags                                            = { Name = "cap3-${each.key}-attach" }
}

resource "aws_ec2_transit_gateway_vpc_attachment" "insp" {
  transit_gateway_id                              = aws_ec2_transit_gateway.this.id
  vpc_id                                          = aws_vpc.insp.id
  subnet_ids                                      = [for k, v in local.insp_subnets : aws_subnet.insp[k].id if v.tier == "tgw"]
  appliance_mode_support                          = "enable"
  transit_gateway_default_route_table_association = false
  transit_gateway_default_route_table_propagation = false
  tags                                            = { Name = "cap3-inspection-attach" }
}

resource "aws_ec2_transit_gateway_route_table" "spoke" {
  transit_gateway_id = aws_ec2_transit_gateway.this.id
  tags               = { Name = "cap3-rt-spoke" }
}

resource "aws_ec2_transit_gateway_route_table" "firewall" {
  transit_gateway_id = aws_ec2_transit_gateway.this.id
  tags               = { Name = "cap3-rt-firewall" }
}

resource "aws_ec2_transit_gateway_route_table_association" "spoke" {
  for_each                       = var.spokes
  transit_gateway_attachment_id  = aws_ec2_transit_gateway_vpc_attachment.spoke[each.key].id
  transit_gateway_route_table_id = aws_ec2_transit_gateway_route_table.spoke.id
}

resource "aws_ec2_transit_gateway_route_table_association" "insp" {
  transit_gateway_attachment_id  = aws_ec2_transit_gateway_vpc_attachment.insp.id
  transit_gateway_route_table_id = aws_ec2_transit_gateway_route_table.firewall.id
}

# Spoke RT: everything goes to inspection
resource "aws_ec2_transit_gateway_route" "spoke_default" {
  destination_cidr_block         = "0.0.0.0/0"
  transit_gateway_attachment_id  = aws_ec2_transit_gateway_vpc_attachment.insp.id
  transit_gateway_route_table_id = aws_ec2_transit_gateway_route_table.spoke.id
}

# Firewall RT: learns the spoke CIDRs so inspected traffic can return to the right spoke
resource "aws_ec2_transit_gateway_route_table_propagation" "spokes_into_firewall" {
  for_each                       = var.spokes
  transit_gateway_attachment_id  = aws_ec2_transit_gateway_vpc_attachment.spoke[each.key].id
  transit_gateway_route_table_id = aws_ec2_transit_gateway_route_table.firewall.id
}

# ================================================================ AWS Network Firewall
resource "aws_networkfirewall_rule_group" "stateful" {
  name     = "cap3-stateful"
  type     = "STATEFUL"
  capacity = 100

  rule_group {
    stateful_rule_options {
      rule_order = "STRICT_ORDER" # evaluate rules top to bottom, first match wins
    }
    rules_source {
      rules_string = <<-EOT
        pass icmp 10.0.0.0/8 any -> 10.0.0.0/8 any (msg:"allow east-west ICMP"; sid:1000001; rev:1;)
        drop tcp ${var.spokes["a"]} any -> ${var.spokes["b"]} 22 (msg:"block SSH from spoke a to spoke b"; sid:1000002; rev:1;)
        pass tcp 10.0.0.0/8 any -> 10.0.0.0/8 any (msg:"allow other east-west TCP"; sid:1000003; rev:1;)
        pass tls 10.0.0.0/8 any -> any 443 (tls.sni; content:".amazonaws.com"; endswith; nocase; msg:"allow AWS APIs"; sid:1000010; rev:1;)
        pass tls 10.0.0.0/8 any -> any 443 (tls.sni; content:"github.com"; endswith; nocase; msg:"allow GitHub"; sid:1000011; rev:1;)
        drop tls 10.0.0.0/8 any -> any any (msg:"drop other TLS egress"; sid:1000020; rev:1;)
        drop http 10.0.0.0/8 any -> any any (msg:"drop plain HTTP egress"; sid:1000021; rev:1;)
      EOT
    }
  }
}

resource "aws_networkfirewall_firewall_policy" "this" {
  name = "cap3-policy"

  firewall_policy {
    stateless_default_actions          = ["aws:forward_to_sfe"]
    stateless_fragment_default_actions = ["aws:forward_to_sfe"]

    stateful_engine_options {
      rule_order = "STRICT_ORDER"
    }

    stateful_rule_group_reference {
      priority     = 10
      resource_arn = aws_networkfirewall_rule_group.stateful.arn
    }
  }
}

resource "aws_networkfirewall_firewall" "this" {
  name                = "cap3-firewall"
  firewall_policy_arn = aws_networkfirewall_firewall_policy.this.arn
  vpc_id              = aws_vpc.insp.id

  dynamic "subnet_mapping" {
    for_each = [for k, v in local.insp_subnets : aws_subnet.insp[k].id if v.tier == "firewall"]
    content {
      subnet_id = subnet_mapping.value
    }
  }
}

resource "aws_cloudwatch_log_group" "fw_alert" {
  name              = "/cap3/network-firewall/alert"
  retention_in_days = 3
}

resource "aws_networkfirewall_logging_configuration" "this" {
  firewall_arn = aws_networkfirewall_firewall.this.arn
  logging_configuration {
    log_destination_config {
      log_destination_type = "CloudWatchLogs"
      log_type             = "ALERT"
      log_destination      = { logGroup = aws_cloudwatch_log_group.fw_alert.name }
    }
  }
}

# ================================================================ Test instances
resource "aws_security_group" "test" {
  for_each    = var.spokes
  name        = "cap3-${each.key}-test"
  description = "Test instance: ICMP and SSH from 10/8"
  vpc_id      = aws_vpc.spoke[each.key].id

  ingress {
    protocol    = "icmp"
    from_port   = -1
    to_port     = -1
    cidr_blocks = [local.supernet]
  }

  ingress {
    protocol    = "tcp"
    from_port   = 22
    to_port     = 22
    cidr_blocks = [local.supernet]
  }

  egress {
    protocol    = "-1"
    from_port   = 0
    to_port     = 0
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "test" {
  for_each               = var.spokes
  ami                    = data.aws_ssm_parameter.al2023_arm.value
  instance_type          = "t4g.nano"
  subnet_id              = aws_subnet.spoke["${each.key}-workload-${local.azs[0]}"].id
  vpc_security_group_ids = [aws_security_group.test[each.key].id]
  metadata_options { http_tokens = "required" }
  tags = { Name = "cap3-${each.key}-test" }
}

resource "aws_ec2_instance_connect_endpoint" "spoke" {
  for_each           = var.spokes
  subnet_id          = aws_subnet.spoke["${each.key}-workload-${local.azs[0]}"].id
  security_group_ids = [aws_security_group.test[each.key].id]
  tags               = { Name = "cap3-${each.key}-eice" }
}
