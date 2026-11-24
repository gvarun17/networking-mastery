# Quiz 09 — Network Services

## Questions

### Q1. In what order are DHCP messages exchanged when a client joins a network?

- A) Discover, Offer, Request, Ack
- B) Offer, Discover, Ack, Request
- C) Discover, Request, Offer, Ack
- D) Request, Offer, Discover, Ack

<details><summary>Answer</summary>

**Answer: A.** DORA: Discover, Offer, Request, Acknowledge.

</details>

### Q2. Scenario: Clients in VLAN 30 get 169.254.x.x addresses. The DHCP server is on another subnet. The router's VLAN 30 SVI has no special DHCP configuration. What is missing?

- A) `ip helper-address <server>` on the VLAN 30 SVI
- B) `ip dhcp excluded-address` on the router
- C) A DNS server option
- D) `ip nat inside` on the SVI

<details><summary>Answer</summary>

**Answer: A.** Routers do not forward broadcasts. The relay must be configured on the interface that receives client broadcasts.

</details>

### Q3. Which field does a DHCP relay agent set so the server can select the correct pool?

- A) giaddr
- B) ciaddr
- C) yiaddr
- D) chaddr

<details><summary>Answer</summary>

**Answer: A.** giaddr (gateway IP address) holds the relay's interface IP in the client subnet.

</details>

### Q4. Which DNS record type maps an IP address back to a name?

- A) PTR
- B) A
- C) NS
- D) CNAME

<details><summary>Answer</summary>

**Answer: A.** PTR records live under in-addr.arpa (IPv4) or ip6.arpa (IPv6).

</details>

### Q5. Scenario: Email for example.com bounces, but the website works. Which record do you check first?

- A) A
- B) PTR
- C) AAAA
- D) MX

<details><summary>Answer</summary>

**Answer: D.** Mail delivery uses MX records to find mail servers. The website uses A/AAAA.

</details>

### Q6. Why can you not put a CNAME record at the zone apex (example.com)?

- A) A CNAME cannot coexist with other records, and the apex must have SOA and NS records
- B) CNAMEs require TCP
- C) The apex must be a PTR record
- D) CNAMEs only work for IPv6

<details><summary>Answer</summary>

**Answer: A.** A name with a CNAME may have no other data, but the apex needs SOA and NS. Route 53 Alias records solve this for AWS targets.

</details>

### Q7. What does `status: SERVFAIL` in dig output usually mean?

- A) The resolver could not complete the query, for example due to a DNSSEC failure or unreachable authoritative servers
- B) The query was refused by policy
- C) The answer is authoritative
- D) The name does not exist

<details><summary>Answer</summary>

**Answer: A.** NXDOMAIN = name does not exist; REFUSED = policy; SERVFAIL = resolver failure.

</details>

### Q8. In Cisco NAT terminology, what is the "inside global" address?

- A) The private address of the inside host
- B) The public address that represents the inside host to the outside
- C) The address of the outside server
- D) The address of the NAT router's inside interface

<details><summary>Answer</summary>

**Answer: B.** Inside local = private host IP. Inside global = translated public IP for that host.

</details>

### Q9. Scenario: PAT is configured with `ip nat inside source list 1 interface g0/0 overload`. No translations appear. Users have no internet. `ip nat outside` is on G0/0. What is the most likely cause?

- A) The LAN interface lacks `ip nat inside`, or ACL 1 does not match the inside subnet
- B) `overload` should be removed
- C) The ISP blocks port 443
- D) NAT requires OSPF

<details><summary>Answer</summary>

**Answer: A.** Translation needs traffic to enter an `ip nat inside` interface, match the ACL, and leave an `ip nat outside` interface.

</details>

### Q10. Which TWO statements about SNMPv3 are true? (Choose two.)

- A) The authPriv level provides both authentication and privacy
- B) It supports authentication and encryption
- C) It cannot send traps
- D) It uses TCP 179
- E) It uses community strings only

<details><summary>Answer</summary>

**Answer: A, B.** SNMPv3 uses users with authentication (e.g. SHA) and privacy (e.g. AES). v1/v2c use community strings. SNMP uses UDP 161/162.

</details>

### Q11. A router has `logging trap warnings`. Which messages go to the syslog server?

- A) Severity 0 through 4
- B) All severities
- C) Severity 4 through 7
- D) Severity 4 only

<details><summary>Answer</summary>

**Answer: A.** The configured level and all more severe (lower-numbered) levels are sent: 0 emergency to 4 warning.

</details>

### Q12. In the message `%OSPF-5-ADJCHG: Process 1, Nbr 2.2.2.2 ... from FULL to DOWN`, what is the severity?

- A) 4 Warning
- B) 2 Critical
- C) 5 Notification
- D) 6 Informational

<details><summary>Answer</summary>

**Answer: C.** The format is %FACILITY-SEVERITY-MNEMONIC. 5 = notification.

</details>

### Q13. What is an NTP stratum 1 server?

- A) A server that is one hop from a stratum 2 server
- B) A server with no time source
- C) The NTP client
- D) A server directly connected to a reference clock (stratum 0)

<details><summary>Answer</summary>

**Answer: D.** Stratum 0 is the reference clock (GPS, atomic). Stratum 1 servers attach to it. Stratum 16 means unsynchronized.

</details>

### Q14. Which ports do DHCP server and client use?

- A) TCP 67 and TCP 68
- B) UDP 546 and 547
- C) UDP 68 server, UDP 67 client
- D) UDP 67 server, UDP 68 client

<details><summary>Answer</summary>

**Answer: D.** DHCPv4 server 67, client 68. DHCPv6 uses UDP 547 (server) and 546 (client).

</details>

### Q15. Scenario: Pods in Kubernetes see random 5-second delays on DNS lookups for external names. What is a well-known cause?

- A) Pods use DHCP
- B) CoreDNS does not support TCP
- C) Parallel A/AAAA queries over one UDP socket hit a conntrack race, so one reply is lost and the resolver retries after 5 seconds
- D) MTU 9001

<details><summary>Answer</summary>

**Answer: C.** The conntrack race plus the default 5-second resolver timeout causes the delay. Mitigations: NodeLocal DNSCache, `single-request-reopen`, lower `ndots`.

</details>
