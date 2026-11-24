# Video Script 06 — "How a Router Decides: LPM, AD and Metric"

**Length:** about 6 minutes.

| # | Time | Visual | Narration |
|---|---|---|---|
| 1 | 0:00-0:30 | A packet icon arrives at a router icon with a question mark. | "A router asks one question per packet: where is the best match for this destination?" |
| 2 | 0:30-1:45 | Diagram: route selection flowchart. | "Step one: longest prefix match. The most specific route wins. Step two: if two sources offer the same prefix, the lower administrative distance wins. Step three: same source, lower metric wins." |
| 3 | 1:45-2:45 | Cisco `show ip route` output. Highlight codes and [AD/metric]. Walk through the 4-row lookup table. | "Read the brackets as AD slash metric. For 10.1.5.200, four routes match. The /25 is longest, so it wins." |
| 4 | 2:45-3:30 | AD table. | "Memorize this table: connected 0, static 1, eBGP 20, EIGRP 90, OSPF 110, RIP 120, iBGP 200." |
| 5 | 3:30-4:30 | Diagram: floating static sequence. Then lab terminal step 3. | "A floating static route has a high AD. It waits. When the primary route disappears, it takes over." |
| 6 | 4:30-5:15 | Lab step 5: ping fails, route still points to r2. | "But a floating route only reacts when the primary route leaves the table. Here the next hop is still up, so traffic goes into a black hole. Use dynamic routing, BFD or IP SLA." |
| 7 | 5:15-6:00 | Diagram: HSRP VIP. AWS route table screenshot. | "Hosts need a gateway that never dies: HSRP or VRRP share a virtual IP. In AWS, the VPC router is always there, and every route is static with longest prefix match." |

## Diagrams to show

1. Route selection flowchart.
2. Floating static sequence.
3. HSRP virtual IP.
