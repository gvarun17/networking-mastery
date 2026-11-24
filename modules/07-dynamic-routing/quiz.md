# Quiz 07 — Dynamic Routing

## Questions

### Q1. Which IP protocol number does OSPF use?

- A) 88
- B) 6
- C) 17
- D) 89

<details><summary>Answer</summary>

**Answer: D.** OSPF runs directly over IP with protocol 89. EIGRP is 88. BGP uses TCP (6) port 179.

</details>

### Q2. A router has no `router-id` command. Its interfaces are Loopback0 10.255.0.1, Loopback1 10.255.0.9, G0/0 192.168.1.1 (all up). What is its OSPF router ID?

- A) 10.255.0.9
- B) 192.168.1.1
- C) 0.0.0.0
- D) 10.255.0.1

<details><summary>Answer</summary>

**Answer: A.** Without a manual router ID, the highest IP on an up loopback wins, even if a physical interface has a higher IP.

</details>

### Q3. Two OSPF routers on a point-to-point link are stuck in ExStart. Hellos are fine. What is the most likely cause?

- A) Duplicate network statement
- B) Different hello timers
- C) Mismatched interface MTU
- D) Different area IDs

<details><summary>Answer</summary>

**Answer: C.** An MTU mismatch is detected during the DBD exchange, so neighbors stall in ExStart/Exchange. Area or timer mismatches stop the neighbor before 2-Way.

</details>

### Q4. On a broadcast segment, which router becomes DR if all priorities are default?

- A) The router that boots last
- B) The router with the highest interface IP
- C) The router with the highest router ID
- D) The router with the lowest router ID

<details><summary>Answer</summary>

**Answer: C.** Highest priority wins (default 1 for all); the tie-breaker is the highest router ID. The election is non-preemptive.

</details>

### Q5. Scenario: `show ip ospf neighbor` shows two neighbors in `2WAY/DROTHER` on a broadcast LAN. What does this mean?

- A) Normal: DROTHERs form full adjacencies only with the DR and BDR
- B) An error: the neighbors are misconfigured
- C) The MTU is wrong
- D) Authentication failed

<details><summary>Answer</summary>

**Answer: A.** Two DROTHERs stop at 2-Way by design. Full adjacencies form only with the DR and BDR.

</details>

### Q6. With the default reference bandwidth, what OSPF cost do a 1 Gbps and a 10 Gbps interface get?

- A) 1 and 1
- B) 100 and 10
- C) 10 and 1
- D) 4 and 2

<details><summary>Answer</summary>

**Answer: A.** Default reference is 100 Mbps. 100/1000 and 100/10000 round up to the minimum cost of 1. Use `auto-cost reference-bandwidth` to fix it on all routers.

</details>

### Q7. Which LSA type does an ABR create to advertise prefixes from one area into another?

- A) Type 3
- B) Type 5
- C) Type 1
- D) Type 2

<details><summary>Answer</summary>

**Answer: A.** Type 3 summary LSAs carry inter-area prefixes (`O IA`). Type 5 carries external routes from an ASBR.

</details>

### Q8. Which TWO parameters must match for OSPF neighbors to form an adjacency on an Ethernet link? (Choose two.)

- A) Hello and dead intervals
- B) Process ID
- C) Router ID
- D) Interface bandwidth
- E) Area ID

<details><summary>Answer</summary>

**Answer: A, E.** Timers, area, subnet/mask, authentication and stub flags must match. The process ID is local only, and router IDs must be different.

</details>

### Q9. What is the EIGRP feasibility condition?

- A) The path must have the lowest hop count
- B) The neighbor's feasible distance must be equal to the reported distance
- C) The neighbor must have the highest router ID
- D) The neighbor's reported distance must be less than the current feasible distance

<details><summary>Answer</summary>

**Answer: D.** A neighbor is a feasible successor (loop-free backup) when its reported (advertised) distance is lower than the current best path's feasible distance.

</details>

### Q10. Which TCP port does BGP use?

- A) 179
- B) 89
- C) 520
- D) 443

<details><summary>Answer</summary>

**Answer: A.** BGP uses TCP port 179. 520 is RIP (UDP).

</details>

### Q11. Scenario: `show ip bgp summary` shows a neighbor in the `Active` state for a long time. What is the most likely cause?

- A) The TCP connection cannot be made: wrong peer IP, no route, or port 179 blocked
- B) The session is established and passing routes
- C) The routes are filtered by a prefix list
- D) The neighbor sent too many prefixes

<details><summary>Answer</summary>

**Answer: A.** Active means the router is trying to open the TCP session and failing. An established session shows a prefix count in the State/PfxRcd column.

</details>

### Q12. Which BGP attribute do you raise to prefer one exit point for outbound traffic for your whole AS?

- A) MED
- B) LOCAL_PREF
- C) AS_PATH length
- D) ORIGIN

<details><summary>Answer</summary>

**Answer: B.** LOCAL_PREF is shared inside the AS through iBGP; the highest value wins. MED and AS_PATH prepending influence how other ASes send traffic to you.

</details>

### Q13. What is the administrative distance of eBGP and iBGP routes on Cisco IOS?

- A) 90 and 170
- B) 20 and 200
- C) 200 and 20
- D) 110 and 115

<details><summary>Answer</summary>

**Answer: B.** eBGP is 20 and iBGP is 200.

</details>

### Q14. Scenario: R1 has `network 198.51.100.0 mask 255.255.255.0` under BGP, but the prefix is not advertised. The routing table has only 198.51.100.1/32 on a loopback. What is wrong?

- A) The `network` command needs an exact match (198.51.100.0/24) in the routing table
- B) BGP cannot advertise loopbacks
- C) BGP needs a route-map
- D) The prefix is private

<details><summary>Answer</summary>

**Answer: A.** The BGP `network` statement advertises a prefix only if an exact matching route exists in the RIB. Add `ip route 198.51.100.0 255.255.255.0 Null0` as an anchor.

</details>

### Q15. Which statement about OSPF areas is correct?

- A) Every area must connect to area 0 (the backbone)
- B) Areas reduce the number of routers in the domain
- C) Area 0 must be configured only on ABRs
- D) Type 5 LSAs are blocked in area 0

<details><summary>Answer</summary>

**Answer: A.** All non-backbone areas must attach to area 0 (directly or through a virtual link). Areas reduce LSDB size and SPF runs, not router count.

</details>
