output "test_instances" {
  description = "Test instance IDs and private IPs per spoke."
  value       = { for k, i in aws_instance.test : k => { id = i.id, ip = i.private_ip } }
}

output "connect_commands" {
  description = "SSH to each test instance through its EC2 Instance Connect Endpoint."
  value       = { for k, i in aws_instance.test : k => "aws ec2-instance-connect ssh --instance-id ${i.id} --connection-type eice --region ${var.region}" }
}

output "firewall_endpoints" {
  description = "Network Firewall endpoint per AZ."
  value       = local.fw_endpoint_by_az
}

output "nat_public_ips" {
  description = "Public egress IPs (allow-list these at partners)."
  value       = { for az, e in aws_eip.nat : az => e.public_ip }
}
