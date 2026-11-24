# Quiz 08 — Transport

## Questions

### Q1. Which flags are set in the second segment of a TCP 3-way handshake?

- A) FIN and ACK
- B) ACK
- C) SYN
- D) SYN and ACK

<details><summary>Answer</summary>

**Answer: D.** SYN → SYN-ACK → ACK.

</details>

### Q2. A client sends a SYN with seq=1000. What ack number does the server's SYN-ACK carry?

- A) 1000
- B) 0
- C) The server's own ISN
- D) 1001

<details><summary>Answer</summary>

**Answer: D.** The SYN consumes one sequence number, so the server acknowledges 1001 (the next byte expected).

</details>

### Q3. Which TWO protocols normally use UDP? (Choose two.)

- A) BGP
- B) HTTPS over HTTP/2
- C) SNMP
- D) SSH
- E) DNS queries

<details><summary>Answer</summary>

**Answer: C, E.** DNS (UDP 53, TCP for large responses and zone transfers) and SNMP (UDP 161/162). SSH, HTTP/2 and BGP use TCP.

</details>

### Q4. What does window scaling solve?

- A) Duplicate ACKs
- B) Port exhaustion
- C) Out-of-order delivery
- D) The 65,535-byte limit of the 16-bit window field on high bandwidth-delay paths

<details><summary>Answer</summary>

**Answer: D.** The window scale option shifts the 16-bit window left by up to 14 bits, allowing windows up to about 1 GB.

</details>

### Q5. What is the bandwidth-delay product of a 500 Mbps path with an RTT of 80 ms?

- A) 625 KB
- B) 5 MB
- C) 6.25 MB
- D) 40 MB

<details><summary>Answer</summary>

**Answer: B.** 500 × 10^6 bits/s × 0.08 s = 40 × 10^6 bits = 5 × 10^6 bytes = 5 MB.

</details>

### Q6. What triggers TCP fast retransmit?

- A) Three duplicate ACKs
- B) An RTO timeout
- C) A zero window
- D) A RST segment

<details><summary>Answer</summary>

**Answer: A.** Three duplicate ACKs mean a segment was probably lost while later segments arrived. The sender retransmits without waiting for the RTO.

</details>

### Q7. Scenario: A server shows thousands of sockets in CLOSE_WAIT. What is the most likely cause?

- A) The application received FIN from the peer but never closed its own socket
- B) A firewall drops FIN packets
- C) MTU mismatch
- D) Ephemeral port exhaustion on the client

<details><summary>Answer</summary>

**Answer: A.** CLOSE_WAIT means the peer closed and the local app has not called close(). It is an application bug (leaked connections).

</details>

### Q8. Which side of a TCP connection enters TIME_WAIT?

- A) The side that receives the first FIN
- B) Both sides
- C) The server only
- D) The side that sends the first FIN (active close)

<details><summary>Answer</summary>

**Answer: D.** The active closer enters TIME_WAIT for 2×MSL so delayed segments from the old connection are not accepted by a new one.

</details>

### Q9. A client gets `Connection refused` immediately. What did it receive?

- A) No reply
- B) A TCP RST
- C) An ICMP echo reply
- D) A SYN-ACK

<details><summary>Answer</summary>

**Answer: B.** A RST (no listener, or a firewall REJECT with tcp-reset) causes an immediate "refused". Silent drops cause timeouts.

</details>

### Q10. Which statement about QUIC is correct?

- A) It has no congestion control
- B) It runs over TCP port 443
- C) It runs over UDP and includes TLS 1.3 in its handshake
- D) It cannot multiplex streams

<details><summary>Answer</summary>

**Answer: C.** QUIC runs over UDP (usually 443), integrates TLS 1.3, has congestion control, and multiplexes independent streams.

</details>

### Q11. Why does HTTP/3 avoid head-of-line blocking that HTTP/2 over TCP suffers from?

- A) It disables retransmission
- B) It uses larger packets
- C) Loss in one QUIC stream does not block other streams
- D) It uses multiple TCP connections

<details><summary>Answer</summary>

**Answer: C.** TCP delivers one ordered byte stream, so one lost segment blocks all HTTP/2 streams. QUIC tracks ordering per stream.

</details>

### Q12. Scenario: An AWS NACL allows inbound TCP 443 from 0.0.0.0/0 and outbound TCP 443 to 0.0.0.0/0. Clients cannot load the website hosted in the subnet. What is missing?

- A) A route to the NAT gateway
- B) A security group rule for port 80
- C) An outbound rule for the ephemeral port range (1024-65535) to the clients
- D) An inbound rule for ICMP

<details><summary>Answer</summary>

**Answer: C.** NACLs are stateless. The server's replies go to the client's ephemeral source port, so outbound 1024-65535 must be allowed.

</details>

### Q13. Which Linux command shows per-socket RTT, cwnd and retransmissions?

- A) ss -ti
- B) netstat -rn
- C) ip neigh
- D) ethtool -S

<details><summary>Answer</summary>

**Answer: A.** `ss -ti` prints TCP internals for each socket.

</details>

### Q14. Which congestion control algorithm uses measured bottleneck bandwidth and RTT instead of loss as its main signal?

- A) Reno
- B) Vegas only in UDP
- C) CUBIC
- D) BBR

<details><summary>Answer</summary>

**Answer: D.** BBR models the path's bandwidth and minimum RTT. Reno and CUBIC react mainly to loss.

</details>

### Q15. Scenario: Long-lived database connections through an AWS NAT gateway drop after about 6 minutes of idle time. What is the best fix?

- A) Increase the MTU
- B) Switch to UDP
- C) Enable TCP keepalives with an interval shorter than the 350-second idle timeout
- D) Add a second route table

<details><summary>Answer</summary>

**Answer: C.** NAT gateways drop idle flows after 350 seconds. Keepalive packets keep the flow entry alive.

</details>
