# Quiz 08 — Transport

### Q1. Which flags are set in the second segment of a TCP 3-way handshake?
- A) SYN
- B) SYN and ACK
- C) ACK
- D) FIN and ACK

<details><summary>Answer</summary>

**Answer: B.** SYN → SYN-ACK → ACK.

</details>

### Q2. A client sends a SYN with seq=1000. What ack number does the server's SYN-ACK carry?
- A) 1000
- B) 1001
- C) 0
- D) The server's own ISN

<details><summary>Answer</summary>

**Answer: B.** The SYN consumes one sequence number, so the server acknowledges 1001 (the next byte expected).

</details>

### Q3. Which TWO protocols normally use UDP? (Choose two.)
- A) DNS queries
- B) SSH
- C) SNMP
- D) HTTPS over HTTP/2
- E) BGP

<details><summary>Answer</summary>

**Answer: A, C.** DNS (UDP 53, TCP for large responses and zone transfers) and SNMP (UDP 161/162). SSH, HTTP/2 and BGP use TCP.

</details>

### Q4. What does window scaling solve?
- A) Out-of-order delivery
- B) The 65,535-byte limit of the 16-bit window field on high bandwidth-delay paths
- C) Duplicate ACKs
- D) Port exhaustion

<details><summary>Answer</summary>

**Answer: B.** The window scale option shifts the 16-bit window left by up to 14 bits, allowing windows up to about 1 GB.

</details>

### Q5. Calculate the bandwidth-delay product of a 500 Mbps path with an RTT of 80 ms.
- A) 625 KB
- B) 5 MB
- C) 40 MB
- D) 6.25 MB

<details><summary>Answer</summary>

**Answer: B.** 500 × 10^6 bits/s × 0.08 s = 40 × 10^6 bits = 5 × 10^6 bytes = 5 MB.

</details>

### Q6. What triggers TCP fast retransmit?
- A) An RTO timeout
- B) Three duplicate ACKs
- C) A RST segment
- D) A zero window

<details><summary>Answer</summary>

**Answer: B.** Three duplicate ACKs mean a segment was probably lost while later segments arrived. The sender retransmits without waiting for the RTO.

</details>

### Q7. Scenario: A server shows thousands of sockets in CLOSE_WAIT. What is the most likely cause?
- A) A firewall drops FIN packets
- B) The application received FIN from the peer but never closed its own socket
- C) Ephemeral port exhaustion on the client
- D) MTU mismatch

<details><summary>Answer</summary>

**Answer: B.** CLOSE_WAIT means the peer closed and the local app has not called close(). It is an application bug (leaked connections).

</details>

### Q8. Which side of a TCP connection enters TIME_WAIT?
- A) The side that sends the first FIN (active close)
- B) The side that receives the first FIN
- C) Both sides
- D) The server only

<details><summary>Answer</summary>

**Answer: A.** The active closer enters TIME_WAIT for 2×MSL so delayed segments from the old connection are not accepted by a new one.

</details>

### Q9. A client gets `Connection refused` immediately. What did it receive?
- A) No reply
- B) An ICMP echo reply
- C) A TCP RST
- D) A SYN-ACK

<details><summary>Answer</summary>

**Answer: C.** A RST (no listener, or a firewall REJECT with tcp-reset) causes an immediate "refused". Silent drops cause timeouts.

</details>

### Q10. Which statement about QUIC is correct?
- A) It runs over TCP port 443
- B) It runs over UDP and includes TLS 1.3 in its handshake
- C) It has no congestion control
- D) It cannot multiplex streams

<details><summary>Answer</summary>

**Answer: B.** QUIC runs over UDP (usually 443), integrates TLS 1.3, has congestion control, and multiplexes independent streams.

</details>

### Q11. Why does HTTP/3 avoid head-of-line blocking that HTTP/2 over TCP suffers from?
- A) It uses larger packets
- B) Loss in one QUIC stream does not block other streams
- C) It disables retransmission
- D) It uses multiple TCP connections

<details><summary>Answer</summary>

**Answer: B.** TCP delivers one ordered byte stream, so one lost segment blocks all HTTP/2 streams. QUIC tracks ordering per stream.

</details>

### Q12. Scenario: An AWS NACL allows inbound TCP 443 from 0.0.0.0/0 and outbound TCP 443 to 0.0.0.0/0. Clients cannot load the website hosted in the subnet. What is missing?
- A) An inbound rule for ICMP
- B) An outbound rule for the ephemeral port range (1024-65535) to the clients
- C) A security group rule for port 80
- D) A route to the NAT gateway

<details><summary>Answer</summary>

**Answer: B.** NACLs are stateless. The server's replies go to the client's ephemeral source port, so outbound 1024-65535 must be allowed.

</details>

### Q13. Which Linux command shows per-socket RTT, cwnd and retransmissions?
- A) netstat -rn
- B) ss -ti
- C) ip neigh
- D) ethtool -S

<details><summary>Answer</summary>

**Answer: B.** `ss -ti` prints TCP internals for each socket.

</details>

### Q14. Which congestion control algorithm uses measured bottleneck bandwidth and RTT instead of loss as its main signal?
- A) Reno
- B) CUBIC
- C) BBR
- D) Vegas only in UDP

<details><summary>Answer</summary>

**Answer: C.** BBR models the path's bandwidth and minimum RTT. Reno and CUBIC react mainly to loss.

</details>

### Q15. Scenario: Long-lived database connections through an AWS NAT gateway drop after about 6 minutes of idle time. What is the best fix?
- A) Increase the MTU
- B) Enable TCP keepalives with an interval shorter than the 350-second idle timeout
- C) Switch to UDP
- D) Add a second route table

<details><summary>Answer</summary>

**Answer: B.** NAT gateways drop idle flows after 350 seconds. Keepalive packets keep the flow entry alive.

</details>
