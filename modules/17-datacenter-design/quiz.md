# Quiz 17 — Data Center and Modern Design

## Questions

### Q1. In a spine-leaf fabric, how many hops does traffic take between servers on different leaves?

- A) Two switch hops (leaf → spine → leaf)
- B) It varies with STP
- C) Four
- D) One (leaf to leaf)

<details><summary>Answer</summary>

**Answer: A.** Every leaf connects to every spine, so the path is always leaf-spine-leaf.

</details>

### Q2. A leaf has 48 × 25 Gbps server ports and 4 × 100 Gbps uplinks. What is the oversubscription ratio?

- A) 3:1
- B) 4:1
- C) 2:1
- D) 1:1

<details><summary>Answer</summary>

**Answer: A.** 48 × 25 = 1200 Gbps down; 4 × 100 = 400 Gbps up; 1200 / 400 = 3:1.

</details>

### Q3. How many bits does the VXLAN Network Identifier have?

- A) 32
- B) 16
- C) 12
- D) 24

<details><summary>Answer</summary>

**Answer: D.** 24 bits, about 16 million segments, versus 4094 VLANs.

</details>

### Q4. Which UDP destination port does VXLAN use (IANA)?

- A) 6081
- B) 179
- C) 8472
- D) 4789

<details><summary>Answer</summary>

**Answer: D.** 4789 is the IANA port. Linux kernel default was 8472 (used by Flannel/Cilium). 6081 is Geneve.

</details>

### Q5. How many bytes of overhead does VXLAN add to an untagged inner frame over IPv4?

- A) 20
- B) 8
- C) 100
- D) 50

<details><summary>Answer</summary>

**Answer: D.** Outer Ethernet 14 + outer IPv4 20 + UDP 8 + VXLAN 8 = 50 bytes.

</details>

### Q6. Which EVPN route type advertises a host MAC (and optionally IP) behind a VTEP?

- A) Type 2
- B) Type 5
- C) Type 3
- D) Type 1

<details><summary>Answer</summary>

**Answer: A.** Type 2 MAC/IP advertisement. Type 3 builds the BUM flood list; type 5 carries IP prefixes.

</details>

### Q7. Why does the VXLAN UDP source port vary per flow?

- A) To give entropy so underlay ECMP hashing spreads traffic across paths
- B) To identify the VNI
- C) For encryption
- D) To avoid NAT

<details><summary>Answer</summary>

**Answer: A.** The source port is a hash of inner headers, so different flows take different ECMP paths.

</details>

### Q8. What is a distributed anycast gateway?

- A) One gateway router in the core
- B) A gateway that uses anycast DNS
- C) An internet gateway in AWS
- D) Every leaf hosts the same gateway IP and MAC for a subnet, so hosts route at their local leaf

<details><summary>Answer</summary>

**Answer: D.** It gives optimal first-hop routing and seamless VM mobility.

</details>

### Q9. Which TWO statements describe the RFC 7938 eBGP underlay design? (Choose two.)

- A) Spines typically share one ASN
- B) Each leaf (or leaf pair) uses its own private ASN
- C) Leaves connect directly to other leaves
- D) iBGP full mesh is required between all leaves
- E) STP is required between spines

<details><summary>Answer</summary>

**Answer: A, B.** Unique leaf ASNs and a shared spine ASN give loop prevention through AS_PATH and simple policy.

</details>

### Q10. What does BGP unnumbered (RFC 5549) allow?

- A) Peering over IPv6 link-local addresses and advertising IPv4 routes with IPv6 next hops, so no /31 plan is needed
- B) BGP without ASNs
- C) Running OSPF inside BGP
- D) BGP without TCP

<details><summary>Answer</summary>

**Answer: A.** Peers are interfaces; next hops are link-local IPv6 addresses.

</details>

### Q11. Scenario: Hosts on different leaves can ping with default sizes, but file transfers between them stall. What do you check first?

- A) Underlay MTU (must be at least 1550 for 1500-byte host frames)
- B) The anycast gateway MAC
- C) EVPN route type 5
- D) STP root placement

<details><summary>Answer</summary>

**Answer: A.** VXLAN adds 50 bytes. A 1500-byte underlay drops full-size encapsulated frames.

</details>

### Q12. In SD-WAN, what does application-aware routing do?

- A) Chooses the WAN path per application based on measured latency, loss and jitter against an SLA
- B) Routes only by destination IP
- C) Blocks all applications except web
- D) Replaces DNS

<details><summary>Answer</summary>

**Answer: A.** Probes measure each tunnel, and policies steer apps to paths that meet their SLA.

</details>

### Q13. Which Cisco Catalyst SD-WAN component handles onboarding and NAT traversal for new edges?

- A) SD-WAN Validator
- B) SD-WAN Manager
- C) WAN Edge
- D) SD-WAN Controller

<details><summary>Answer</summary>

**Answer: A.** The Validator (vBond) authenticates and orchestrates edges and helps with NAT traversal. The Controller (vSmart) distributes routing policy; the Manager (vManage) is the management GUI/API.

</details>

### Q14. What is the core idea of SDN?

- A) Use only static routes
- B) Separate the control plane from the data plane and centralize control in software with programmable APIs
- C) Replace switches with hubs
- D) Every device runs its own independent control plane only

<details><summary>Answer</summary>

**Answer: B.** Controllers program the forwarding behaviour of devices through southbound APIs.

</details>

### Q15. Which EVPN route type builds the list of VTEPs that receive broadcast, unknown unicast and multicast (BUM) traffic for a VNI?

- A) Type 5
- B) Type 4
- C) Type 3
- D) Type 2

<details><summary>Answer</summary>

**Answer: C.** Type 3 inclusive multicast Ethernet tag routes announce VTEP membership per VNI for head-end replication.

</details>
