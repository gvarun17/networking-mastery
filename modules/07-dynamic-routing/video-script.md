# Video Script 07 — "OSPF and BGP: How Routers Learn the Map"

**Length:** about 8 minutes.

| # | Time | Visual | Narration |
|---|---|---|---|
| 1 | 0:00-0:30 | 50 routers with static routes; one link fails; red X's everywhere. | "Static routes cannot react when links fail. Dynamic routing protocols can." |
| 2 | 0:30-1:15 | Table: distance vector vs link state vs path vector. | "Three families. Distance vector shares distances. Link state shares the whole map. Path vector shares the path and applies policy." |
| 3 | 1:15-2:30 | Diagram: OSPF neighbor state machine. Lab output `show ip ospf neighbor`. | "OSPF routers say hello every 10 seconds. If timers, area, subnet and MTU match, they walk through these states to Full." |
| 4 | 2:30-3:15 | Animation: DR election on a LAN with 5 routers. | "On a LAN, OSPF elects a DR to cut down adjacencies. Highest priority, then highest router ID. On point-to-point links, skip the election." |
| 5 | 3:15-4:15 | Diagram: area 0 / area 1 with ABR and ASBR. LSA table. | "Areas keep the database small. The ABR summarizes with type 3 LSAs. The ASBR brings in external routes as type 5." |
| 6 | 4:15-4:45 | Cost formula, reference bandwidth problem. | "Cost is reference bandwidth over link bandwidth. The default reference is 100 megabits, so every fast link costs 1. Raise it everywhere." |
| 7 | 4:45-5:15 | EIGRP summary card. | "EIGRP: Cisco's advanced distance vector. Remember successor, feasible successor and the feasibility condition." |
| 8 | 5:15-6:45 | Diagram: BGP session state machine. Lab output: BGP table. Best-path table. | "BGP runs over TCP 179. Stuck in Active means TCP fails. Once Established, routes come with attributes. Local preference picks your exit. AS path length decides most internet paths." |
| 9 | 6:45-7:30 | Lab break #5: wrong remote-as. | "Here I set the wrong AS on the ISP. The OPEN message fails, and the session cycles. Always check AS numbers first." |
| 10 | 7:30-8:00 | AWS diagram: DX and VPN with BGP. | "In AWS, every dynamic hybrid connection is eBGP: Direct Connect, VPN and TGW Connect. Filter in both directions and summarize." |

## Diagrams to show

1. OSPF neighbor state machine.
2. Multi-area topology.
3. BGP session state machine.
