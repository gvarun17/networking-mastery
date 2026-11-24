# Quiz 06 — Routing Basics

### Q1. A router has routes 10.0.0.0/8 (static, AD 1), 10.1.0.0/16 (OSPF, AD 110) and 10.1.1.0/24 (EIGRP, AD 90). Which route forwards a packet to 10.1.1.50?
- A) 10.0.0.0/8 because static has the lowest AD
- B) 10.1.0.0/16 because OSPF is preferred
- C) 10.1.1.0/24 because it is the longest prefix match
- D) The packet is load-balanced over all three

<details><summary>Answer</summary>

**Answer: C.** Longest prefix match comes first. AD only compares routes for the same prefix.

</details>

### Q2. What is the default administrative distance of an OSPF route?
- A) 90
- B) 100
- C) 110
- D) 120

<details><summary>Answer</summary>

**Answer: C.** OSPF is 110. EIGRP internal is 90, RIP is 120 and eBGP is 20.

</details>

### Q3. In the output `O 10.1.5.0/24 [110/30] via 10.0.13.3`, what does 30 mean?
- A) The administrative distance
- B) The OSPF cost (metric) to the destination
- C) The number of hops
- D) The age of the route in seconds

<details><summary>Answer</summary>

**Answer: B.** The brackets show [AD/metric]. 110 is the AD; 30 is the OSPF cost.

</details>

### Q4. Which command creates a floating static default route that is used only when a route with AD 110 is gone?
- A) ip route 0.0.0.0 0.0.0.0 198.51.100.1
- B) ip route 0.0.0.0 0.0.0.0 198.51.100.1 1
- C) ip route 0.0.0.0 0.0.0.0 198.51.100.1 120
- D) ip route 0.0.0.0 255.255.255.255 198.51.100.1 120

<details><summary>Answer</summary>

**Answer: C.** The AD must be higher than 110. Option A and B have AD 1 and would win. Option D uses the wrong mask (host route to 0.0.0.0).

</details>

### Q5. Which route source has an administrative distance of 0?
- A) Static route to an exit interface
- B) Connected interface
- C) eBGP
- D) Host route

<details><summary>Answer</summary>

**Answer: B.** Connected routes have AD 0. Static routes have AD 1, even when they point to an exit interface.

</details>

### Q6. Scenario: Users behind R1 can send traffic to a server behind R3, but get no replies. R1 has a route to the server subnet. What do you check on R3 first?
- A) The duplex on R1's interface
- B) R3's route back to the users' subnet
- C) The DNS server
- D) The STP root bridge

<details><summary>Answer</summary>

**Answer: B.** One-way traffic is almost always a missing return route. Check `show ip route <user-subnet>` on the far-end router.

</details>

### Q7. Which TWO statements about floating static routes are true? (Choose two.)
- A) They have a higher AD than the primary route
- B) They are installed in the routing table when the primary route disappears
- C) They always fail over when the remote network is unreachable
- D) They must use AD 255
- E) They replace the primary route permanently

<details><summary>Answer</summary>

**Answer: A, B.** A floating static has a higher AD and is used only when the primary route leaves the table. If the primary route stays (for example, its next hop is still reachable), no failover happens. AD 255 means "never use".

</details>

### Q8. What is a host route in IPv4?
- A) A route with a /0 mask
- B) A route with a /32 mask
- C) A route to the router's own loopback only
- D) A route learned from a host by ARP

<details><summary>Answer</summary>

**Answer: B.** A host route matches exactly one address (/32 in IPv4, /128 in IPv6).

</details>

### Q9. Why is `ip route 10.2.0.0 255.255.0.0 GigabitEthernet0/1` (no next hop) a poor choice on Ethernet?
- A) It has AD 0
- B) The router must ARP for every destination address, which depends on proxy ARP
- C) Static routes cannot use Ethernet interfaces
- D) The route is never installed

<details><summary>Answer</summary>

**Answer: B.** With only an exit interface, the router treats every destination as directly connected and ARPs for each one. It works only if the next router answers with proxy ARP, and it fills the ARP cache.

</details>

### Q10. Scenario: `show standby brief` on R1 shows `Gi0/0 10 100 Active local 10.10.10.3 10.10.10.1`. R2 has priority 110 but is Standby. What is the most likely reason?
- A) R2 has a lower IP address
- B) Preemption is not enabled on R2
- C) HSRP version mismatch
- D) R1 has a higher MAC address

<details><summary>Answer</summary>

**Answer: B.** HSRP preemption is off by default. R1 became active first and stays active even though R2 has a higher priority. Configure `standby 10 preempt` on R2.

</details>

### Q11. What virtual MAC address does VRRP group 5 use?
- A) 0000.0c07.ac05
- B) 0000.0c9f.f005
- C) 0000.5e00.0105
- D) 0100.5e00.0005

<details><summary>Answer</summary>

**Answer: C.** VRRP uses 0000.5e00.01XX where XX is the group in hex. HSRPv1 uses 0000.0c07.acXX and HSRPv2 uses 0000.0c9f.fXXX.

</details>

### Q12. Which Linux command shows the route the kernel will use for a destination?
- A) ip route show table all
- B) ip route get 10.1.5.200
- C) ip neigh show
- D) ss -tnp

<details><summary>Answer</summary>

**Answer: B.** `ip route get` performs the longest prefix match and shows the next hop, egress interface and source IP.

</details>

### Q13. Scenario: R1 has two OSPF routes to 10.5.0.0/24 with equal cost via two neighbors. What does R1 do?
- A) Uses the first route learned
- B) Uses the route with the lower next-hop IP
- C) Installs both and load-shares (ECMP)
- D) Drops the traffic

<details><summary>Answer</summary>

**Answer: C.** Equal-cost routes from the same protocol are installed together (up to `maximum-paths`, default 4 for OSPF on IOS) and traffic is load-shared, usually per flow.

</details>

### Q14. A router has routes 0.0.0.0/0 via 203.0.113.1, 172.16.0.0/12 via 10.0.0.2 and 172.16.4.0/22 via 10.0.0.3. Where does a packet to 172.16.7.9 go?
- A) 203.0.113.1
- B) 10.0.0.2
- C) 10.0.0.3
- D) It is dropped

<details><summary>Answer</summary>

**Answer: C.** 172.16.4.0/22 covers 172.16.4.0-172.16.7.255, so 172.16.7.9 matches the /22, which is longer than the /12 and the /0.

</details>

### Q15. In an AWS VPC route table, which route always exists for the VPC CIDR and cannot be deleted?
- A) The IGW route
- B) The local route
- C) The NAT gateway route
- D) The TGW route

<details><summary>Answer</summary>

**Answer: B.** The `local` route covers the VPC CIDR. You can add more specific routes for subnets to send traffic through an appliance, but you cannot delete the local route.

</details>
