# Quiz 14 — Cloud Networking (AWS)

## Questions

### Q1. VPC A peers with VPC B, and VPC B peers with VPC C. Can instances in A reach C through B?

- A) Yes, peering is transitive
- B) No, VPC peering is not transitive
- C) Yes, if all three are in the same Region
- D) Yes, if B has an internet gateway

<details><summary>Answer</summary>

**Answer: B.** Peering connections are point to point. Use a direct peering A-C, a Transit Gateway or Cloud WAN.

</details>

### Q2. In Transit Gateway, what does associating an attachment with a TGW route table control?

- A) The VPC route table entries
- B) Which routes the attachment advertises
- C) Which TGW route table is used to forward traffic that arrives from that attachment
- D) The attachment's bandwidth

<details><summary>Answer</summary>

**Answer: C.** Association = which table looks up traffic from that attachment. Propagation = which tables learn the attachment's routes. One association, many propagations.

</details>

### Q3. Which VPC endpoint type for S3 is free and works as a route table target?

- A) Resolver endpoint
- B) Gateway Load Balancer endpoint
- C) Gateway endpoint
- D) Interface endpoint

<details><summary>Answer</summary>

**Answer: C.** Gateway endpoints (S3, DynamoDB) add a prefix-list route in the route table and have no hourly or data charge.

</details>

### Q4. Scenario: A SaaS provider must expose an API to 200 customer VPCs, some with overlapping CIDRs. No customer should get network-level access to the provider's VPC. What do you use?

- A) VPC peering to each customer
- B) PrivateLink: an endpoint service behind an NLB, consumed through interface endpoints
- C) Transit Gateway shared with RAM
- D) Public internet with IP allow lists

<details><summary>Answer</summary>

**Answer: B.** PrivateLink gives one-way, service-level access and works with overlapping CIDRs because consumers use local ENI IPs.

</details>

### Q5. How many IPsec tunnels does an AWS Site-to-Site VPN connection provide?

- A) 2
- B) 1
- C) 4
- D) 8

<details><summary>Answer</summary>

**Answer: A.** Two tunnels, each terminating on a different AWS endpoint, for redundancy. Each tunnel supports up to 1.25 Gbps.

</details>

### Q6. Which Direct Connect virtual interface type connects to a Transit Gateway through a Direct Connect gateway?

- A) Transit VIF
- B) Public VIF
- C) Private VIF
- D) Hosted VIF only

<details><summary>Answer</summary>

**Answer: A.** Transit VIF → DX gateway → TGW. Private VIF connects to a VGW (directly or through a DX gateway). Public VIF reaches AWS public endpoints.

</details>

### Q7. Is Direct Connect traffic encrypted by default?

- A) Yes, with IPsec
- B) No, and encryption is impossible
- C) Yes, with TLS
- D) No; use MACsec on supported dedicated connections or run IPsec VPN over DX

<details><summary>Answer</summary>

**Answer: D.** DX is a private circuit but not encrypted. MACsec (Layer 2) or an IPsec VPN over a public/transit VIF adds encryption.

</details>

### Q8. Scenario: Private subnets in two AZs both route 0.0.0.0/0 to one NAT gateway in AZ-a. What are TWO problems? (Choose two.)

- A) Cross-AZ data transfer charges for AZ-b traffic
- B) Security groups stop working
- C) IPv6 stops working
- D) NAT gateways cannot be shared by two subnets
- E) AZ-a failure breaks internet access for both AZs

<details><summary>Answer</summary>

**Answer: A, E.** Deploy one NAT gateway per AZ and route each private subnet to its local NAT gateway.

</details>

### Q9. Which Route 53 component lets on-premises DNS servers resolve names in a private hosted zone?

- A) Inbound endpoint
- B) Outbound endpoint
- C) Alias record
- D) Health check

<details><summary>Answer</summary>

**Answer: A.** On-prem DNS conditionally forwards to the inbound endpoint IPs in the VPC. Outbound endpoints + rules forward VPC queries to on-prem DNS.

</details>

### Q10. Why should you enable appliance mode on the TGW attachment of an inspection VPC?

- A) To increase bandwidth
- B) To keep both directions of a flow on the same AZ's appliance, so stateful inspection sees the whole flow
- C) To enable IPv6
- D) To allow overlapping CIDRs

<details><summary>Answer</summary>

**Answer: B.** Without appliance mode, TGW may send return traffic to an appliance in another AZ, which drops it as an unknown flow.

</details>

### Q11. How many IP addresses does AWS reserve in each subnet?

- A) 5
- B) 3
- C) 8
- D) 2

<details><summary>Answer</summary>

**Answer: A.** Network, VPC router (+1), DNS (+2), future use (+3) and broadcast (last).

</details>

### Q12. Scenario: An interface endpoint for SSM exists, but `dig ssm.ap-south-1.amazonaws.com` on an instance returns public IPs. What is the most likely cause?

- A) SSM does not support PrivateLink
- B) The security group blocks UDP 53
- C) The endpoint is in the wrong AZ
- D) Private DNS is disabled on the endpoint, or the VPC's DNS hostnames/support attributes are off

<details><summary>Answer</summary>

**Answer: D.** Private DNS creates a hidden private hosted zone that overrides the public name. It needs `enableDnsSupport` and `enableDnsHostnames` on the VPC.

</details>

### Q13. Which tool tells you, without sending traffic, which component blocks a path between two ENIs?

- A) AWS Config
- B) VPC Reachability Analyzer
- C) CloudTrail
- D) VPC Flow Logs

<details><summary>Answer</summary>

**Answer: B.** Reachability Analyzer analyses route tables, SGs, NACLs, TGW and more, and names the blocking hop.

</details>

### Q14. Your on-prem network learns the same prefix from AWS over Direct Connect and Site-to-Site VPN. Which path does AWS prefer to send traffic to on-prem for an identical prefix?

- A) Random
- B) Direct Connect
- C) VPN
- D) The path with the lowest MTU

<details><summary>Answer</summary>

**Answer: B.** For identical prefixes, AWS prefers Direct Connect BGP routes over VPN routes. More specific prefixes always win first.

</details>

### Q15. Scenario: EKS pods get "no IP addresses available" errors although nodes are healthy. The VPC CNI is in use with /24 subnets. What are good fixes?

- A) Use larger subnets or add a secondary CIDR (e.g. from 100.64.0.0/10) with custom networking, or enable prefix delegation
- B) Use a NAT gateway
- C) Disable security groups
- D) Increase the node instance size only

<details><summary>Answer</summary>

**Answer: A.** Each pod takes a VPC IP. Size pod subnets for pods, use secondary CIDRs with custom networking, or use prefix delegation (/28 per ENI slot) to improve density.

</details>
