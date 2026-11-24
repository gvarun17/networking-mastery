# Module 14 lab: three VPCs on a Transit Gateway, a PrivateLink service,
# a Route 53 private hosted zone and an EC2 Instance Connect Endpoint.
# No internet access is created on purpose: all access is private.

data "aws_availability_zones" "this" {
  state = "available"
}

data "aws_ssm_parameter" "al2023_arm" {
  name = "/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-arm64"
}

locals {
  azs = slice(data.aws_availability_zones.this.names, 0, var.az_count)

  # One private /24 per AZ per VPC (netnum 0, 1, ...) and one /28 per AZ for TGW ENIs.
  private_subnets = merge([
    for vpc, cidr in var.vpcs : {
      for i, az in local.azs : "${vpc}-${az}" => {
        vpc  = vpc
        az   = az
        cidr = cidrsubnet(cidr, 8, i)
      }
    }
  ]...)

  tgw_subnets = merge([
    for vpc, cidr in var.vpcs : {
      for i, az in local.azs : "${vpc}-${az}" => {
        vpc  = vpc
        az   = az
        cidr = cidrsubnet(cidr, 12, 4080 + i) # x.x.255.0/28, x.x.255.16/28
      }
    }
  ]...)

  supernet = "10.0.0.0/8"
}

# ---------------------------------------------------------------- VPCs
resource "aws_vpc" "this" {
  for_each             = var.vpcs
  cidr_block           = each.value
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags                 = { Name = "${var.name}-${each.key}" }
}

resource "aws_subnet" "private" {
  for_each          = local.private_subnets
  vpc_id            = aws_vpc.this[each.value.vpc].id
  availability_zone = each.value.az
  cidr_block        = each.value.cidr
  tags              = { Name = "${var.name}-${each.key}-private", Tier = "private" }
}

resource "aws_subnet" "tgw" {
  for_each          = local.tgw_subnets
  vpc_id            = aws_vpc.this[each.value.vpc].id
  availability_zone = each.value.az
  cidr_block        = each.value.cidr
  tags              = { Name = "${var.name}-${each.key}-tgw", Tier = "tgw" }
}

resource "aws_route_table" "private" {
  for_each = var.vpcs
  vpc_id   = aws_vpc.this[each.key].id
  tags     = { Name = "${var.name}-${each.key}-private-rt" }
}

resource "aws_route_table_association" "private" {
  for_each       = local.private_subnets
  subnet_id      = aws_subnet.private[each.key].id
  route_table_id = aws_route_table.private[each.value.vpc].id
}

# Send all RFC 1918 10/8 traffic that is not local to the Transit Gateway.
resource "aws_route" "to_tgw" {
  for_each               = var.vpcs
  route_table_id         = aws_route_table.private[each.key].id
  destination_cidr_block = local.supernet
  transit_gateway_id     = aws_ec2_transit_gateway.this.id
  depends_on             = [aws_ec2_transit_gateway_vpc_attachment.this]
}

# ---------------------------------------------------------------- Transit Gateway
resource "aws_ec2_transit_gateway" "this" {
  description                     = "${var.name} hub"
  amazon_side_asn                 = 64512
  default_route_table_association = "disable"
  default_route_table_propagation = "disable"
  dns_support                     = "enable"
  tags                            = { Name = "${var.name}-tgw" }
}

resource "aws_ec2_transit_gateway_vpc_attachment" "this" {
  for_each           = var.vpcs
  transit_gateway_id = aws_ec2_transit_gateway.this.id
  vpc_id             = aws_vpc.this[each.key].id
  subnet_ids         = [for k, s in aws_subnet.tgw : s.id if local.tgw_subnets[k].vpc == each.key]
  dns_support        = "enable"

  transit_gateway_default_route_table_association = false
  transit_gateway_default_route_table_propagation = false

  tags = { Name = "${var.name}-${each.key}-attach" }
}

# Two TGW route tables: "spokes" (app, data) and "shared".
# app and data can reach shared, shared can reach both, but app and data cannot reach each other
# directly. Lab step 6 asks you to change this.
resource "aws_ec2_transit_gateway_route_table" "spokes" {
  transit_gateway_id = aws_ec2_transit_gateway.this.id
  tags               = { Name = "${var.name}-rt-spokes" }
}

resource "aws_ec2_transit_gateway_route_table" "shared" {
  transit_gateway_id = aws_ec2_transit_gateway.this.id
  tags               = { Name = "${var.name}-rt-shared" }
}

resource "aws_ec2_transit_gateway_route_table_association" "this" {
  for_each                       = var.vpcs
  transit_gateway_attachment_id  = aws_ec2_transit_gateway_vpc_attachment.this[each.key].id
  transit_gateway_route_table_id = each.key == "shared" ? aws_ec2_transit_gateway_route_table.shared.id : aws_ec2_transit_gateway_route_table.spokes.id
}

# shared propagates into spokes; spokes propagate into shared.
resource "aws_ec2_transit_gateway_route_table_propagation" "shared_into_spokes" {
  transit_gateway_attachment_id  = aws_ec2_transit_gateway_vpc_attachment.this["shared"].id
  transit_gateway_route_table_id = aws_ec2_transit_gateway_route_table.spokes.id
}

resource "aws_ec2_transit_gateway_route_table_propagation" "spokes_into_shared" {
  for_each                       = { for k, v in var.vpcs : k => v if k != "shared" }
  transit_gateway_attachment_id  = aws_ec2_transit_gateway_vpc_attachment.this[each.key].id
  transit_gateway_route_table_id = aws_ec2_transit_gateway_route_table.shared.id
}

# ---------------------------------------------------------------- Security groups
resource "aws_security_group" "lab" {
  for_each    = var.vpcs
  name        = "${var.name}-${each.key}-lab"
  description = "Lab instances: ICMP and 8080 from 10/8, SSH from the EIC endpoint"
  vpc_id      = aws_vpc.this[each.key].id

  ingress {
    description = "ICMP from internal networks"
    protocol    = "icmp"
    from_port   = -1
    to_port     = -1
    cidr_blocks = [local.supernet]
  }

  ingress {
    description = "Demo web service"
    protocol    = "tcp"
    from_port   = 8080
    to_port     = 8080
    cidr_blocks = [local.supernet]
  }

  ingress {
    description = "SSH from within the VPC (EC2 Instance Connect Endpoint)"
    protocol    = "tcp"
    from_port   = 22
    to_port     = 22
    cidr_blocks = [each.value]
  }

  egress {
    description = "All outbound"
    protocol    = "-1"
    from_port   = 0
    to_port     = 0
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# ---------------------------------------------------------------- Instances
locals {
  web_user_data = <<-EOT
    #!/bin/bash
    mkdir -p /srv/www && echo "hello from $(hostname) in the data VPC" > /srv/www/index.html
    cd /srv/www && nohup python3 -m http.server 8080 >/var/log/web.log 2>&1 &
  EOT
}

resource "aws_instance" "app_client" {
  ami                    = data.aws_ssm_parameter.al2023_arm.value
  instance_type          = var.instance_type
  subnet_id              = aws_subnet.private["app-${local.azs[0]}"].id
  vpc_security_group_ids = [aws_security_group.lab["app"].id]
  metadata_options { http_tokens = "required" }
  tags = { Name = "${var.name}-app-client" }
}

resource "aws_instance" "data_server" {
  ami                    = data.aws_ssm_parameter.al2023_arm.value
  instance_type          = var.instance_type
  subnet_id              = aws_subnet.private["data-${local.azs[0]}"].id
  vpc_security_group_ids = [aws_security_group.lab["data"].id]
  user_data              = local.web_user_data
  metadata_options { http_tokens = "required" }
  tags = { Name = "${var.name}-data-server" }
}

resource "aws_instance" "shared_tools" {
  ami                    = data.aws_ssm_parameter.al2023_arm.value
  instance_type          = var.instance_type
  subnet_id              = aws_subnet.private["shared-${local.azs[0]}"].id
  vpc_security_group_ids = [aws_security_group.lab["shared"].id]
  metadata_options { http_tokens = "required" }
  tags = { Name = "${var.name}-shared-tools" }
}

# EC2 Instance Connect Endpoints: SSH to private instances with no bastion and no internet (free).
resource "aws_ec2_instance_connect_endpoint" "this" {
  for_each           = var.vpcs
  subnet_id          = aws_subnet.private["${each.key}-${local.azs[0]}"].id
  security_group_ids = [aws_security_group.lab[each.key].id]
  preserve_client_ip = false
  tags               = { Name = "${var.name}-${each.key}-eice" }
}

# ---------------------------------------------------------------- PrivateLink (provider = data VPC)
resource "aws_lb" "svc" {
  name               = "${var.name}-svc-nlb"
  internal           = true
  load_balancer_type = "network"
  subnets            = [for k, s in aws_subnet.private : s.id if local.private_subnets[k].vpc == "data"]
}

resource "aws_lb_target_group" "svc" {
  name        = "${var.name}-svc-tg"
  port        = 8080
  protocol    = "TCP"
  vpc_id      = aws_vpc.this["data"].id
  target_type = "instance"

  health_check {
    protocol = "TCP"
    port     = "8080"
  }
}

resource "aws_lb_target_group_attachment" "svc" {
  target_group_arn = aws_lb_target_group.svc.arn
  target_id        = aws_instance.data_server.id
  port             = 8080
}

resource "aws_lb_listener" "svc" {
  load_balancer_arn = aws_lb.svc.arn
  port              = 80
  protocol          = "TCP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.svc.arn
  }
}

resource "aws_vpc_endpoint_service" "svc" {
  acceptance_required        = false
  network_load_balancer_arns = [aws_lb.svc.arn]
  tags                       = { Name = "${var.name}-svc" }
}

# Consumer = app VPC
resource "aws_vpc_endpoint" "svc" {
  vpc_id              = aws_vpc.this["app"].id
  service_name        = aws_vpc_endpoint_service.svc.service_name
  vpc_endpoint_type   = "Interface"
  subnet_ids          = [for k, s in aws_subnet.private : s.id if local.private_subnets[k].vpc == "app"]
  security_group_ids  = [aws_security_group.endpoint.id]
  private_dns_enabled = false
  tags                = { Name = "${var.name}-svc-endpoint" }
}

resource "aws_security_group" "endpoint" {
  name        = "${var.name}-app-endpoint"
  description = "Interface endpoint: TCP 80 from the app VPC"
  vpc_id      = aws_vpc.this["app"].id

  ingress {
    protocol    = "tcp"
    from_port   = 80
    to_port     = 80
    cidr_blocks = [var.vpcs["app"]]
  }
}

# ---------------------------------------------------------------- Route 53 private zone
resource "aws_route53_zone" "lab" {
  name = "lab.internal"

  dynamic "vpc" {
    for_each = var.vpcs
    content {
      vpc_id = aws_vpc.this[vpc.key].id
    }
  }
}

resource "aws_route53_record" "data" {
  zone_id = aws_route53_zone.lab.zone_id
  name    = "data.lab.internal"
  type    = "A"
  ttl     = 60
  records = [aws_instance.data_server.private_ip]
}

resource "aws_route53_record" "svc" {
  zone_id = aws_route53_zone.lab.zone_id
  name    = "svc.lab.internal"
  type    = "CNAME"
  ttl     = 60
  records = [aws_vpc_endpoint.svc.dns_entry[0].dns_name]
}

resource "aws_route53_record" "tools" {
  zone_id = aws_route53_zone.lab.zone_id
  name    = "tools.lab.internal"
  type    = "A"
  ttl     = 60
  records = [aws_instance.shared_tools.private_ip]
}

# ---------------------------------------------------------------- Flow logs
resource "aws_cloudwatch_log_group" "flow" {
  count             = var.enable_flow_logs ? 1 : 0
  name              = "/${var.name}/flowlogs/app"
  retention_in_days = 3
}

resource "aws_iam_role" "flow" {
  count = var.enable_flow_logs ? 1 : 0
  name  = "${var.name}-flowlogs"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "vpc-flow-logs.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy" "flow" {
  count = var.enable_flow_logs ? 1 : 0
  role  = aws_iam_role.flow[0].id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = ["logs:CreateLogStream", "logs:PutLogEvents", "logs:DescribeLogStreams"]
      Resource = "${aws_cloudwatch_log_group.flow[0].arn}:*"
    }]
  })
}

resource "aws_flow_log" "app" {
  count                    = var.enable_flow_logs ? 1 : 0
  vpc_id                   = aws_vpc.this["app"].id
  traffic_type             = "ALL"
  log_destination_type     = "cloud-watch-logs"
  log_destination          = aws_cloudwatch_log_group.flow[0].arn
  iam_role_arn             = aws_iam_role.flow[0].arn
  max_aggregation_interval = 60
  log_format               = "$${version} $${interface-id} $${srcaddr} $${dstaddr} $${srcport} $${dstport} $${protocol} $${packets} $${bytes} $${action} $${tcp-flags} $${flow-direction}"
}
