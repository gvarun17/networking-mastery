output "instances" {
  description = "Instance IDs and private IPs."
  value = {
    app_client   = { id = aws_instance.app_client.id, ip = aws_instance.app_client.private_ip }
    data_server  = { id = aws_instance.data_server.id, ip = aws_instance.data_server.private_ip }
    shared_tools = { id = aws_instance.shared_tools.id, ip = aws_instance.shared_tools.private_ip }
  }
}

output "connect_app_client" {
  description = "SSH to the app client through the EC2 Instance Connect Endpoint."
  value       = "aws ec2-instance-connect ssh --instance-id ${aws_instance.app_client.id} --connection-type eice --region ${var.region}"
}

output "privatelink_endpoint_dns" {
  description = "Regional DNS name of the interface endpoint in the app VPC."
  value       = aws_vpc_endpoint.svc.dns_entry[0].dns_name
}

output "tgw_route_tables" {
  description = "TGW route table IDs."
  value = {
    spokes = aws_ec2_transit_gateway_route_table.spokes.id
    shared = aws_ec2_transit_gateway_route_table.shared.id
  }
}
