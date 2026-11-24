# Video Script 14 — "AWS Networking as a Network Engineer Sees It"

**Length:** about 8 minutes.

| # | Time | Visual | Narration |
|---|---|---|---|
| 1 | 0:00-0:30 | AWS console VPC page. | "A VPC is a software-defined network. No switches, no broadcast. But every rule you learned still applies: subnets, routes, longest prefix match, stateful filters." |
| 2 | 0:30-1:45 | Diagram: VPC with tiers and endpoints. | "Public subnets route to the internet gateway. Private subnets route to a NAT gateway in the same AZ. Data subnets have no internet route. Gateway endpoints for S3 are free: use them everywhere." |
| 3 | 1:45-2:45 | Diagram: peering vs TGW. Comparison table. | "Peering is simple but not transitive. Transit Gateway is a router in the cloud with route tables. PrivateLink exposes one service, even with overlapping CIDRs." |
| 4 | 2:45-4:00 | Diagram: TGW segmentation. Lab step 3 terminal. | "Association decides which table handles traffic from an attachment. Propagation decides which tables learn its routes. Here app reaches shared, but not data, until I add one propagation." |
| 5 | 4:00-5:15 | Diagram: Direct Connect VIF types. | "Hybrid: VPN gives two IPsec tunnels over the internet. Direct Connect gives a private circuit with BGP per VLAN. Private VIF to VPCs, transit VIF to TGW, public VIF to AWS services. Not encrypted by default." |
| 6 | 5:15-6:15 | Diagram: hybrid DNS sequence. | "Hybrid DNS: outbound endpoints forward AWS queries to on-prem. Inbound endpoints let on-prem resolve private hosted zones." |
| 7 | 6:15-7:15 | Diagram: hub-and-spoke with inspection. | "The production pattern: spokes to TGW, TGW to an inspection VPC with appliance mode, then to egress or the destination. Capstone 3 builds it." |
| 8 | 7:15-8:00 | Reachability Analyzer result screen. | "When something fails, Reachability Analyzer names the blocking hop. Flow Logs show what the ENI accepted. Use both." |

## Diagrams to show

1. VPC tiers.
2. Peering vs TGW.
3. TGW segmentation.
4. DX VIF types.
5. Hybrid DNS sequence.
6. Hub-and-spoke reference.
