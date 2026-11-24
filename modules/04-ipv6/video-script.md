# Video Script 04 — "IPv6 Without Fear: Addresses, SLAAC and NDP"

**Length:** about 7 minutes.

| # | Time | Visual | Narration |
|---|---|---|---|
| 1 | 0:00-0:30 | Long IPv6 address appears and shrinks to compressed form. | "IPv6 addresses look scary. They are not. Two rules make them short, and one protocol makes them automatic." |
| 2 | 0:30-1:30 | Animation: remove leading zeros, then replace one zero run with `::`. | "Rule one: drop leading zeros in each group. Rule two: replace one run of zero groups with a double colon. Only once." |
| 3 | 1:30-2:30 | Diagram: address types tree. | "Global unicast starts with 2 or 3. Unique local starts with fd. Every interface also has a link-local address starting with fe80. There is no broadcast. Multicast does that job." |
| 4 | 2:30-3:30 | Diagram: 48/16/64 structure. EUI-64 animation from a MAC. | "Your ISP gives you a /48. You have 16 bits for subnets. The last 64 bits identify the interface. EUI-64 builds them from the MAC: insert ff-fe, flip one bit." |
| 5 | 3:30-5:00 | Diagram: SLAAC sequence. Then the lab capture showing RS, RA, NS. | "Watch a host configure itself. It makes a link-local address and checks it is unique. It asks for routers. The router advertises the prefix. The host builds its address and uses the router's link-local as the gateway." |
| 6 | 5:00-5:45 | Table: M and O flags. | "Two flags in the RA decide the method. M means use DHCPv6 for addresses. O means use DHCPv6 for other things like DNS. DHCPv6 never gives a gateway." |
| 7 | 5:45-6:30 | Diagram: dual stack with DNS A and AAAA. | "Dual stack runs both protocols. Clients try both and use the fastest. That hides IPv6 breakage, so test with curl -6." |
| 8 | 6:30-7:00 | AWS console: VPC IPv6 CIDR, egress-only IGW. | "In AWS: /56 per VPC, /64 per subnet, egress-only internet gateway for outbound-only. And never block all ICMPv6." |

## Diagrams to show

1. Address types tree.
2. 48/16/64 structure.
3. SLAAC sequence.
4. Dual stack flow.
