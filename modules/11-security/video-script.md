# Video Script 11 — "Network Security Layers: ACLs, Firewalls, VPNs and Zero Trust"

**Length:** about 8 minutes.

| # | Time | Visual | Narration |
|---|---|---|---|
| 1 | 0:00-0:30 | Castle-and-moat image, then crossed out. | "The perimeter is not enough. Security is many layers, each doing one job." |
| 2 | 0:30-1:45 | Diagram: ACL processing flowchart. `show access-lists` counters. | "An ACL is checked top down. First match wins. Every ACL ends with an invisible deny. Standard ACLs near the destination, extended near the source." |
| 3 | 1:45-3:00 | Diagram: stateful vs stateless sequence. Lab A1 vs A2 terminal. | "A stateless filter judges each packet alone, so you must allow the return traffic. A stateful firewall remembers the connection. That is the NACL vs security group difference in AWS." |
| 4 | 3:00-4:15 | Diagram: IKEv2 sequence. Then WireGuard lab capture. | "IPsec: IKE on UDP 500 negotiates keys; ESP, protocol 50, carries encrypted packets. The internet sees only the gateways. WireGuard does the same with less code." |
| 5 | 4:15-5:15 | 802.1X roles diagram. RADIUS vs TACACS+ table. | "AAA: who are you, what can you do, what did you do. RADIUS for network access, TACACS+ for device admin. 802.1X keeps a port closed until the user proves who they are." |
| 6 | 5:15-6:30 | Animation: rogue DHCP server and ARP spoofing; then snooping and DAI blocking them. | "Layer 2 attacks are easy. DHCP snooping trusts only uplinks. Dynamic ARP Inspection checks ARP against the snooping table. Storm control and RA guard finish the job." |
| 7 | 6:30-7:30 | Zero trust diagram. | "Zero trust: never trust the network location. Verify identity, device and context on every request." |
| 8 | 7:30-8:00 | AWS mapping table. | "In AWS: NACLs, security groups, Network Firewall, Site-to-Site VPN, Client VPN and Verified Access map to the same ideas." |

## Diagrams to show

1. ACL processing flowchart.
2. Stateful vs stateless sequence.
3. IKEv2 sequence.
4. 802.1X roles.
5. Zero trust model.
