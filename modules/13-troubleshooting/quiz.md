# Quiz 13 — Troubleshooting

## Questions

### Q1. Which troubleshooting approach fits best when one application fails but all others work for the same user?

- A) Bottom-up
- B) Top-down
- C) Replace the cable first
- D) Reboot all routers

<details><summary>Answer</summary>

**Answer: B.** Other applications working proves Layers 1-3 (and likely 4) are fine. Start at the application.

</details>

### Q2. A ping reply shows `ttl=61` from a Linux server. How many routers are between you and the server, assuming the server starts at TTL 64?

- A) 1
- B) 3
- C) 61
- D) 64

<details><summary>Answer</summary>

**Answer: B.** 64 − 61 = 3 decrements, so 3 router hops.

</details>

### Q3. mtr shows 70% loss at hop 4 and 0% loss at hops 5-12, including the destination. What is the most likely explanation?

- A) Hop 4 is dropping 70% of your traffic
- B) Hop 4 rate-limits ICMP replies to its own control plane; transit traffic is fine
- C) The destination is down
- D) DNS failure

<details><summary>Answer</summary>

**Answer: B.** Loss that does not continue to later hops is not real forwarding loss.

</details>

### Q4. nmap shows port 5432 as `filtered`. What does this mean?

- A) The host replied with RST: nothing is listening
- B) No reply was received: a firewall probably drops the probes
- C) The port is open
- D) The host is down

<details><summary>Answer</summary>

**Answer: B.** `closed` = RST received (reachable, no listener). `filtered` = no answer or ICMP unreachable (filtering).

</details>

### Q5. Scenario: A capture on the server shows SYNs arriving from the client and SYN-ACKs leaving. A capture on the client shows SYNs leaving but no SYN-ACKs. Where is the problem?

- A) The server application
- B) The return path (routing, NAT or a stateful firewall dropping replies)
- C) The client's DNS
- D) The client's NIC

<details><summary>Answer</summary>

**Answer: B.** The forward path works and the server answers. The reply is lost on the way back.

</details>

### Q6. Which command shows which process listens on TCP port 8080 on Linux?

- A) `ip route`
- B) `ss -tlnp`
- C) `dig`
- D) `traceroute`

<details><summary>Answer</summary>

**Answer: B.** `-t` TCP, `-l` listening, `-n` numeric, `-p` process.

</details>

### Q7. What is the "golden question" to ask at the start of most incidents?

- A) "Which vendor is it?"
- B) "What changed?"
- C) "How old is the hardware?"
- D) "Who is on call?"

<details><summary>Answer</summary>

**Answer: B.** Most incidents follow a change: deployment, config, certificate expiry, route or rule edits.

</details>

### Q8. Which TWO tools can prove whether a TCP port is reachable when ICMP is blocked? (Choose two.)

- A) `nc -vz host 443`
- B) `ping host`
- C) `traceroute -T -p 443 host`
- D) `arp -a`
- E) `ip link`

<details><summary>Answer</summary>

**Answer: A, C.** Both use TCP to the real port. ping and traceroute (default UDP/ICMP) can be filtered while the service works.

</details>

### Q9. Which Wireshark display filter shows TCP retransmissions?

- A) `tcp.port == 80`
- B) `tcp.analysis.retransmission`
- C) `ip.ttl < 5`
- D) `dns.qry.name`

<details><summary>Answer</summary>

**Answer: B.** Wireshark's TCP analysis flags retransmissions, duplicate ACKs, zero windows and more.

</details>

### Q10. Scenario: Small web pages load, but large file downloads hang forever. SSH logins work, but `cat` of a big file stalls. What do you test next?

- A) DNS resolution
- B) Path MTU, with `ping -M do -s 1472` and `tracepath`
- C) The ARP cache
- D) NTP sync

<details><summary>Answer</summary>

**Answer: B.** Classic MTU black hole symptoms.

</details>

### Q11. Which AWS tool checks, without sending packets, whether security groups, NACLs and route tables allow a path between two resources?

- A) VPC Flow Logs
- B) VPC Reachability Analyzer
- C) Traffic Mirroring
- D) CloudTrail

<details><summary>Answer</summary>

**Answer: B.** Reachability Analyzer does static configuration analysis and names the blocking component. Flow Logs record real traffic.

</details>

### Q12. `ping` from a host returns `From 10.13.1.10 icmp_seq=1 Destination Host Unreachable`, where 10.13.1.10 is the host's own IP. What does this indicate?

- A) A remote router has no route
- B) The host cannot resolve the next hop's MAC address with ARP on the local link
- C) The destination service is down
- D) TTL expired

<details><summary>Answer</summary>

**Answer: B.** When the error comes from your own IP, ARP for the destination (or gateway) failed locally.

</details>

### Q13. Which Linux command performs a route lookup and shows the outgoing interface and source IP for a destination?

- A) `ip route get <ip>`
- B) `ip neigh`
- C) `ss -s`
- D) `ethtool eth0`

<details><summary>Answer</summary>

**Answer: A.** `ip route get` applies longest prefix match and policy rules.

</details>

### Q14. Scenario: One EC2 instance can reach the database and a similar instance in the same subnet cannot. What is the most efficient first step?

- A) Rebuild the VPC
- B) Compare the two instances: security groups, IAM, routes, DNS, application config
- C) Restart the database
- D) Open all ports

<details><summary>Answer</summary>

**Answer: B.** "Compare working vs broken" quickly isolates the difference (often a different security group).

</details>

### Q15. In which order does the structured troubleshooting method proceed?

- A) Fix, test, define, document
- B) Define the problem, gather facts, hypothesize, test, fix, verify, document
- C) Gather, fix, define, verify
- D) Document, fix, test

<details><summary>Answer</summary>

**Answer: B.** Define → gather → hypothesize → test → fix → verify → document.

</details>
