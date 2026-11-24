# Cheatsheet 14 — AWS Cloud Networking

## Key limits and numbers (check current quotas)

| Item | Value |
|---|---|
| VPC CIDR size | /16 to /28 |
| Reserved IPs per subnet | 5 |
| IPv4 CIDRs per VPC | 5 (adjustable) |
| VPC DNS resolver | base + 2, 169.254.169.253 |
| Time sync | 169.254.169.123 |
| Metadata (IMDS) | 169.254.169.254 (use IMDSv2) |
| MTU in VPC / via IGW / via TGW | 9001 / 1500 / 8500 |
| VPN tunnel bandwidth | up to 1.25 Gbps per tunnel |
| DX private VIF prefixes from you | 100 |
| NAT GW connections | 55,000 per destination per IP |
| NAT GW idle timeout | 350 s |

## Choosing connectivity

| Need | Use |
|---|---|
| Few VPCs, high throughput | VPC peering |
| Many VPCs + on-prem, segmentation | Transit Gateway |
| Global multi-Region policy network | Cloud WAN |
| Expose one service, overlap OK | PrivateLink |
| Service-to-service L7 with IAM auth | VPC Lattice |
| On-prem, quick, encrypted | Site-to-Site VPN |
| On-prem, consistent, high bandwidth | Direct Connect (+ VPN backup) |

## AWS CLI

```bash
aws ec2 describe-route-tables --filters Name=vpc-id,Values=vpc-123 --query 'RouteTables[].Routes[]'
aws ec2 search-transit-gateway-routes --transit-gateway-route-table-id tgw-rtb-123 --filters Name=state,Values=active
aws ec2 describe-transit-gateway-attachments
aws ec2 describe-vpc-endpoints --query 'VpcEndpoints[].[VpcEndpointId,ServiceName,State]'
aws ec2 describe-network-interfaces --filters Name=addresses.private-ip-address,Values=10.1.0.25
aws ec2 create-network-insights-path --source eni-a --destination eni-b --protocol tcp --destination-port 443
aws route53 list-hosted-zones-by-vpc --vpc-id vpc-123 --vpc-region ap-south-1
aws ec2-instance-connect ssh --instance-id i-123 --connection-type eice
```

## Terraform resource names

| Concept | Resource |
|---|---|
| VPC / subnet | `aws_vpc`, `aws_subnet` |
| Routes | `aws_route_table`, `aws_route`, `aws_route_table_association` |
| IGW / NAT / EIGW | `aws_internet_gateway`, `aws_nat_gateway`, `aws_egress_only_internet_gateway` |
| TGW | `aws_ec2_transit_gateway`, `..._vpc_attachment`, `..._route_table`, `..._route_table_association`, `..._route_table_propagation`, `..._route` |
| Endpoints | `aws_vpc_endpoint`, `aws_vpc_endpoint_service` |
| DNS | `aws_route53_zone`, `aws_route53_record`, `aws_route53_resolver_endpoint`, `aws_route53_resolver_rule` |
| Hybrid | `aws_customer_gateway`, `aws_vpn_connection`, `aws_dx_gateway` |
| Firewall | `aws_networkfirewall_firewall`, `aws_networkfirewall_rule_group` |
| Logs | `aws_flow_log` |

## Flow log fields worth adding

`pkt-srcaddr`, `pkt-dstaddr` (real source behind NAT/TGW), `tcp-flags`, `flow-direction`, `traffic-path`, `vpc-id`, `subnet-id`, `az-id`.

## DX BGP communities (AWS → you / you → AWS)

| Community | Meaning |
|---|---|
| 7224:7100 / 7200 / 7300 | Local preference low / medium / high (you set, for AWS outbound) |
| 7224:9100 / 9200 / 9300 | Scope: local Region / continent / global (public VIF) |
