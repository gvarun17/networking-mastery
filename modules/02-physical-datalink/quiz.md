# Quiz 02 — Physical and Data Link

## Questions

### Q1. What is the maximum segment length for 1000BASE-T over Cat6 copper?

- A) 100 m
- B) 55 m
- C) 185 m
- D) 550 m

<details><summary>Answer</summary>

**Answer: A.** Twisted-pair Ethernet (10BASE-T to 10GBASE-T on Cat6a) is limited to 100 m. 55 m is the 10GBASE-T limit on Cat6, and 550 m is a multimode fiber distance.

</details>

### Q2. Which fiber type uses a 9 µm core and lasers for long distances?

- A) Single-mode
- B) Plenum copper
- C) Multimode OM4
- D) Multimode OM3

<details><summary>Answer</summary>

**Answer: A.** Single-mode fiber has a small core (about 9 µm), so light takes one path. Dispersion is low, so it reaches kilometres. Multimode has 50/62.5 µm cores.

</details>

### Q3. Scenario: A switch port shows many late collisions. The PC is set to 100/full. What is the most likely cause?

- A) A spanning-tree loop
- B) A bad VLAN assignment
- C) The switch port is autonegotiating and fell back to half duplex
- D) An ARP cache timeout

<details><summary>Answer</summary>

**Answer: C.** When one side is hard-coded and the other side autonegotiates, the auto side detects speed but defaults to half duplex at 10/100 Mbps. The half-duplex side records late collisions. The full-duplex side records CRC/runt errors.

</details>

### Q4. A switch receives a frame for a destination MAC that is not in its MAC table. What does it do?

- A) Sends the frame to the default gateway
- B) Drops the frame
- C) Floods the frame out all ports in the VLAN except the ingress port
- D) Sends an ARP request

<details><summary>Answer</summary>

**Answer: C.** Unknown unicast frames are flooded within the VLAN. The switch learns the destination's port when the reply arrives.

</details>

### Q5. Which MAC address is an IPv4 multicast MAC?

- A) 33:33:00:00:00:01
- B) ff:ff:ff:ff:ff:ff
- C) 01:00:5e:00:00:05
- D) 00:1c:73:aa:bb:cc

<details><summary>Answer</summary>

**Answer: C.** IPv4 multicast maps to 01:00:5e plus the low 23 bits of the group (224.0.0.5 for OSPF → 01:00:5e:00:00:05). 33:33 is IPv6 multicast, ff…ff is broadcast, and 00:1c:73 is a unicast OUI.

</details>

### Q6. Host 10.1.1.10/24 sends a packet to 8.8.8.8. Which MAC address does it put in the destination field?

- A) Its own MAC
- B) ff:ff:ff:ff:ff:ff
- C) The MAC of its default gateway
- D) The MAC of 8.8.8.8

<details><summary>Answer</summary>

**Answer: C.** 8.8.8.8 is off-subnet, so the host ARPs for the default gateway and sends the frame to the gateway's MAC. The IP destination is still 8.8.8.8.

</details>

### Q7. Which message does a host send to announce its own IP-to-MAC mapping without being asked?

- A) Gratuitous ARP
- B) Reverse ARP
- C) ICMP redirect
- D) Proxy ARP

<details><summary>Answer</summary>

**Answer: A.** A gratuitous ARP announces (or tests) the sender's own mapping. VRRP/HSRP and keepalived use it after failover so switches and hosts update quickly.

</details>

### Q8. What is the minimum Ethernet frame size, including the FCS?

- A) 46 bytes
- B) 60 bytes
- C) 1518 bytes
- D) 64 bytes

<details><summary>Answer</summary>

**Answer: D.** 64 bytes: 14 header + 46 minimum payload + 4 FCS. Frames shorter than 64 bytes are "runts".

</details>

### Q9. A host uses `ping -M do -s 1472`. What total IPv4 packet size does this test?

- A) 1500 bytes
- B) 1472 bytes
- C) 1518 bytes
- D) 1480 bytes

<details><summary>Answer</summary>

**Answer: A.** 1472 bytes of ICMP data + 8-byte ICMP header + 20-byte IPv4 header = 1500 bytes.

</details>

### Q10. Scenario: SSH to a server works, but `cat` of a large log file freezes. Small HTTP requests work, but large downloads stall. A firewall in the path blocks all ICMP. What is the most likely cause?

- A) A duplicate IP address
- B) An expired ARP entry
- C) A path MTU black hole
- D) DNS failure

<details><summary>Answer</summary>

**Answer: C.** Large packets with DF set exceed a smaller link MTU. The router sends ICMP "fragmentation needed", but the firewall drops it, so the sender never lowers its packet size. Permit ICMP type 3 code 4 or clamp TCP MSS.

</details>

### Q11. What is the default MAC address table aging time on Cisco switches?

- A) 4 hours
- B) 120 seconds
- C) 300 seconds
- D) 30 seconds

<details><summary>Answer</summary>

**Answer: C.** 300 seconds. The 4-hour value is the Cisco default ARP timeout, a different table.

</details>

### Q12. Which TWO counters suggest a physical cable or optic problem? (Choose two.)

- A) Spanning-tree topology changes
- B) Input errors
- C) ARP timeouts
- D) Output drops caused by congestion
- E) CRC errors

<details><summary>Answer</summary>

**Answer: B, E.** CRC and input errors mean frames arrived damaged: bad cable, dirty or failing optic, EMI or duplex mismatch. Output drops usually mean congestion.

</details>

### Q13. In AWS, why does keepalived VIP failover with gratuitous ARP not work?

- A) Security groups block ARP replies
- B) AWS uses IPv6 only
- C) The VPC answers ARP itself and ignores guest GARP messages
- D) AWS blocks UDP

<details><summary>Answer</summary>

**Answer: C.** The VPC fabric owns IP-to-ENI mappings and answers ARP itself. Move the IP with the EC2 API (secondary private IP or Elastic IP), or use an NLB.

</details>

### Q14. What does the U/L bit in a MAC address indicate when it is set to 1?

- A) The address is a broadcast
- B) The frame has a VLAN tag
- C) The address is multicast
- D) The address is locally administered (not assigned by the vendor)

<details><summary>Answer</summary>

**Answer: D.** The second-lowest bit of the first byte is U/L. Value 1 means locally administered, as with Docker (02:42:...) and randomized phone MACs. The lowest bit (I/G) marks multicast.

</details>

### Q15. Which statement about full-duplex Ethernet is true?

- A) It sends and receives at the same time, with no collisions
- B) It uses CSMA/CD to detect collisions
- C) It requires coaxial cable
- D) It can be used on hub ports

<details><summary>Answer</summary>

**Answer: A.** Full duplex uses separate transmit and receive paths. Collisions cannot happen, so CSMA/CD is disabled. Hubs only support half duplex.

</details>
