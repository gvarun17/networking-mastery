# Quiz 01 — Network Models

15 questions. Target: 13 or more correct. Run interactively with `python3 tools/quiz_runner.py modules/01-osi-tcpip`.

### Q1. What is the PDU name at the OSI transport layer when TCP is used?
- A) Frame
- B) Packet
- C) Segment
- D) Bit

<details><summary>Answer</summary>

**Answer: C.** TCP data at Layer 4 is a segment. UDP data at Layer 4 is usually called a datagram. Packets are Layer 3, frames are Layer 2.

</details>

### Q2. Which OSI layers does the TCP/IP "Application" layer cover?
- A) Layer 7 only
- B) Layers 5, 6 and 7
- C) Layers 4 to 7
- D) Layers 6 and 7

<details><summary>Answer</summary>

**Answer: B.** The TCP/IP application layer combines OSI session, presentation and application layers.

</details>

### Q3. A frame arrives with EtherType 0x86DD. What does the receiver do with the payload?
- A) Gives it to the ARP process
- B) Gives it to IPv4
- C) Gives it to IPv6
- D) Drops it because it is a VLAN tag

<details><summary>Answer</summary>

**Answer: C.** 0x86DD is IPv6. 0x0800 is IPv4, 0x0806 is ARP and 0x8100 is an 802.1Q VLAN tag.

</details>

### Q4. A packet goes from a host through three routers to a server. Which field stays the same on every link (no NAT)?
- A) Source MAC address
- B) Destination MAC address
- C) Destination IP address
- D) IPv4 TTL

<details><summary>Answer</summary>

**Answer: C.** IP addresses are end to end. Each router builds a new Layer 2 header (new MACs) and decrements the TTL.

</details>

### Q5. Which device makes forwarding decisions using only Layer 2 information?
- A) Router
- B) Switch
- C) Stateful firewall
- D) L7 load balancer

<details><summary>Answer</summary>

**Answer: B.** A Layer 2 switch forwards frames by destination MAC address. Routers use Layer 3, firewalls use Layer 3/4 state, L7 load balancers read application data.

</details>

### Q6. Which IPv4 header field tells the receiver that the payload is UDP?
- A) Type of Service = 17
- B) Protocol = 17
- C) Protocol = 6
- D) Flags = 17

<details><summary>Answer</summary>

**Answer: B.** The IPv4 Protocol field is 17 for UDP, 6 for TCP and 1 for ICMP.

</details>

### Q7. Which component does the data link layer add at the end of a frame?
- A) TTL
- B) Sequence number
- C) Frame check sequence (FCS)
- D) Checksum of the TCP header

<details><summary>Answer</summary>

**Answer: C.** Ethernet adds a 4-byte FCS trailer (CRC-32). The receiver drops frames with a bad FCS and counts them as CRC errors.

</details>

### Q8. Scenario: A user can ping the default gateway but cannot reach any internet site. DNS works. At which layer do you start?
- A) Layer 1
- B) Layer 2
- C) Layer 3
- D) Layer 7

<details><summary>Answer</summary>

**Answer: C.** A ping to the gateway proves Layers 1-3 work on the local link. DNS working proves some remote reachability. Next, check routing beyond the gateway: default route, NAT and return route. "Divide and conquer" starts from the layer that the evidence points to.

</details>

### Q9. Why does TCP use port numbers?
- A) To find the next-hop router
- B) To identify the application process on a host
- C) To detect bit errors on the link
- D) To identify the network interface card

<details><summary>Answer</summary>

**Answer: B.** Ports multiplex many conversations onto one IP address and deliver data to the correct process (socket).

</details>

### Q10. A tcpdump line shows `length 74` for a TCP SYN with 20 bytes of TCP options. What makes up 74 bytes?
- A) 14 Ethernet + 20 IP + 40 TCP
- B) 18 Ethernet + 20 IP + 36 TCP
- C) 14 Ethernet + 40 IP + 20 TCP
- D) 20 Ethernet + 20 IP + 34 TCP

<details><summary>Answer</summary>

**Answer: A.** Ethernet header 14 bytes, IPv4 header 20 bytes, TCP header 20 base + 20 options = 40. tcpdump does not show the 4-byte FCS.

</details>

### Q11. Which statement about encapsulation is correct?
- A) Each layer reads all headers of the layers above it
- B) Each layer adds its own header and treats the upper-layer data as payload
- C) Only the transport layer adds a header
- D) Encapsulation happens at the receiver

<details><summary>Answer</summary>

**Answer: B.** Each layer treats everything from the layer above as opaque payload and adds its own header. The receiver decapsulates.

</details>

### Q12. Where do most books place TLS in the OSI model?
- A) Layer 2
- B) Layer 3
- C) Between Layers 4 and 7 (often called Layer 5/6)
- D) Layer 1

<details><summary>Answer</summary>

**Answer: C.** TLS runs on top of TCP and below the application protocol. Books place it at session or presentation. TCP/IP simply calls it part of the application layer.

</details>

### Q13. Scenario: A Cisco interface shows `GigabitEthernet0/1 is up, line protocol is down`. Which layers are involved?
- A) Layer 1 is up; Layer 2 has a problem
- B) Layer 1 is down
- C) Layer 3 has a problem
- D) The interface is administratively shut down

<details><summary>Answer</summary>

**Answer: A.** The first status is Layer 1 (physical signal). The line protocol is Layer 2 (keepalives, encapsulation, err-disable on some platforms). Administrative shutdown shows "administratively down".

</details>

### Q14. Which TWO are Layer 3 protocols? (Choose two.)
- A) ICMP
- B) ARP
- C) OSPF
- D) UDP
- E) Ethernet

<details><summary>Answer</summary>

**Answer: A, C.** ICMP and OSPF ride directly in IP (protocol 1 and 89) and are Layer 3. ARP is usually placed at Layer 2 (or "2.5"). UDP is Layer 4. Ethernet is Layer 2.

</details>

### Q15. Scenario: In AWS, an EC2 instance sends traffic to another subnet in the same VPC. Which AWS component performs the Layer 3 forwarding?
- A) The internet gateway
- B) The implicit VPC router, configured by the subnet route table
- C) The security group
- D) The Elastic Load Balancer

<details><summary>Answer</summary>

**Answer: B.** Every VPC has an implicit router (reachable at subnet base + 1). The route table attached to the subnet controls it. Security groups filter traffic but do not route it.

</details>
