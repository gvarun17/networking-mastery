# Quiz 02 — Physical and Data Link

### Q1. What is the maximum segment length for 1000BASE-T over Cat6 copper?
- A) 55 m
- B) 100 m
- C) 185 m
- D) 550 m

<details><summary>Answer</summary>

**Answer: B.** Twisted-pair Ethernet (10BASE-T to 10GBASE-T on Cat6a) is limited to 100 m. 55 m is the 10GBASE-T limit on Cat6, and 550 m is a multimode fiber distance.

</details>

### Q2. Which fiber type uses a 9 µm core and lasers for long distances?
- A) Multimode OM3
- B) Multimode OM4
- C) Single-mode
- D) Plenum copper

<details><summary>Answer</summary>

**Answer: C.** Single-mode fiber has a small core (about 9 µm), so light takes one path. Dispersion is low, so it reaches kilometres. Multimode has 50/62.5 µm cores.

</details>

### Q3. Scenario: A switch port shows many late collisions. The PC is set to 100/full. What is the most likely cause?
- A) The switch port is autonegotiating and fell back to half duplex
- B) A bad VLAN assignment
- C) An ARP cache timeout
- D) A spanning-tree loop

<details><summary>Answer</summary>

**Answer: A.** When one side is hard-coded and the other side autonegotiates, the auto side detects speed but defaults to half duplex at 10/100 Mbps. The half-duplex side records late collisions. The full-duplex side records CRC/runt errors.

</details>

### Q4. A switch receives a frame for a destination MAC that is not in its MAC table. What does it do?
- A) Drops the frame
- B) Sends an ARP request
- C) Floods the frame out all ports in the VLAN except the ingress port
- D) Sends the frame to the default gateway

<details><summary>Answer</summary>

**Answer: C.** Unknown unicast frames are flooded within the VLAN. The switch learns the destination's port when the reply arrives.

</details>

### Q5. Which MAC address is an IPv4 multicast MAC?
- A) ff:ff:ff:ff:ff:ff
- B) 01:00:5e:00:00:05
- C) 33:33:00:00:00:01
- D) 00:1c:73:aa:bb:cc

<details><summary>Answer</summary>

**Answer: B.** IPv4 multicast maps to 01:00:5e plus the low 23 bits of the group (224.0.0.5 for OSPF → 01:00:5e:00:00:05). 33:33 is IPv6 multicast, ff…ff is broadcast, and 00:1c:73 is a unicast OUI.

</details>

### Q6. Host 10.1.1.10/24 sends a packet to 8.8.8.8. Which MAC address does it put in the destination field?
- A) The MAC of 8.8.8.8
- B) ff:ff:ff:ff:ff:ff
- C) The MAC of its default gateway
- D) Its own MAC

<details><summary>Answer</summary>

**Answer: C.** 8.8.8.8 is off-subnet, so the host ARPs for the default gateway and sends the frame to the gateway's MAC. The IP destination is still 8.8.8.8.

</details>

### Q7. Which message does a host send to announce its own IP-to-MAC mapping without being asked?
- A) Proxy ARP
- B) Reverse ARP
- C) Gratuitous ARP
- D) ICMP redirect

<details><summary>Answer</summary>

**Answer: C.** A gratuitous ARP announces (or tests) the sender's own mapping. VRRP/HSRP and keepalived use it after failover so switches and hosts update quickly.

</details>

### Q8. What is the minimum Ethernet frame size, including the FCS?
- A) 46 bytes
- B) 60 bytes
- C) 64 bytes
- D) 1518 bytes

<details><summary>Answer</summary>

**Answer: C.** 64 bytes: 14 header + 46 minimum payload + 4 FCS. Frames shorter than 64 bytes are "runts".

</details>

### Q9. A host uses `ping -M do -s 1472`. What total IPv4 packet size does this test?
- A) 1472 bytes
- B) 1480 bytes
- C) 1500 bytes
- D) 1518 bytes

<details><summary>Answer</summary>

**Answer: C.** 1472 bytes of ICMP data + 8-byte ICMP header + 20-byte IPv4 header = 1500 bytes.

</details>

### Q10. Scenario: SSH to a server works, but `cat` of a large log file freezes. Small HTTP requests work, but large downloads stall. A firewall in the path blocks all ICMP. What is the most likely cause?
- A) DNS failure
- B) A path MTU black hole
- C) A duplicate IP address
- D) An expired ARP entry

<details><summary>Answer</summary>

**Answer: B.** Large packets with DF set exceed a smaller link MTU. The router sends ICMP "fragmentation needed", but the firewall drops it, so the sender never lowers its packet size. Permit ICMP type 3 code 4 or clamp TCP MSS.

</details>

### Q11. What is the default MAC address table aging time on Cisco switches?
- A) 30 seconds
- B) 120 seconds
- C) 300 seconds
- D) 4 hours

<details><summary>Answer</summary>

**Answer: C.** 300 seconds. The 4-hour value is the Cisco default ARP timeout, a different table.

</details>

### Q12. Which TWO counters suggest a physical cable or optic problem? (Choose two.)
- A) CRC errors
- B) Input errors
- C) Output drops caused by congestion
- D) Spanning-tree topology changes
- E) ARP timeouts

<details><summary>Answer</summary>

**Answer: A, B.** CRC and input errors mean frames arrived damaged: bad cable, dirty or failing optic, EMI or duplex mismatch. Output drops usually mean congestion.

</details>

### Q13. In AWS, why does keepalived VIP failover with gratuitous ARP not work?
- A) AWS blocks UDP
- B) The VPC answers ARP itself and ignores guest GARP messages
- C) AWS uses IPv6 only
- D) Security groups block ARP replies

<details><summary>Answer</summary>

**Answer: B.** The VPC fabric owns IP-to-ENI mappings and answers ARP itself. Move the IP with the EC2 API (secondary private IP or Elastic IP), or use an NLB.

</details>

### Q14. What does the U/L bit in a MAC address indicate when it is set to 1?
- A) The address is multicast
- B) The address is locally administered (not assigned by the vendor)
- C) The address is a broadcast
- D) The frame has a VLAN tag

<details><summary>Answer</summary>

**Answer: B.** The second-lowest bit of the first byte is U/L. Value 1 means locally administered, as with Docker (02:42:...) and randomized phone MACs. The lowest bit (I/G) marks multicast.

</details>

### Q15. Which statement about full-duplex Ethernet is true?
- A) It uses CSMA/CD to detect collisions
- B) It can be used on hub ports
- C) It sends and receives at the same time, with no collisions
- D) It requires coaxial cable

<details><summary>Answer</summary>

**Answer: C.** Full duplex uses separate transmit and receive paths. Collisions cannot happen, so CSMA/CD is disabled. Hubs only support half duplex.

</details>
