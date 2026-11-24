# Quiz 11 — Security

## Questions

### Q1. Where should you place a standard ACL?

- A) As close to the destination as possible
- B) On every interface
- C) Only on VTY lines
- D) As close to the source as possible

<details><summary>Answer</summary>

**Answer: A.** Standard ACLs match only the source address. Placed near the source, they would block that source from every destination.

</details>

### Q2. What does the wildcard mask 0.0.0.255 match with 10.10.10.0?

- A) 10.10.0.0 through 10.10.255.255
- B) Every address
- C) 10.10.10.0 through 10.10.10.255
- D) Only 10.10.10.0

<details><summary>Answer</summary>

**Answer: C.** Wildcard 0 bits must match; 1 bits are "don't care". The last octet can be anything.

</details>

### Q3. An extended ACL contains only `deny tcp any host 10.50.0.80 eq 23`. It is applied inbound on the LAN interface. What happens to HTTPS traffic to 10.50.0.80?

- A) It is permitted
- B) It is denied by the implicit deny
- C) It is permitted only from the LAN
- D) It is logged and permitted

<details><summary>Answer</summary>

**Answer: B.** Every ACL ends with an implicit `deny ip any any`. Without a permit entry, all traffic is dropped.

</details>

### Q4. Which statement about AWS security groups and NACLs is correct?

- A) Security groups are stateless; NACLs are stateful
- B) Both are stateful
- C) Security groups are stateful; NACLs are stateless
- D) Both are stateless

<details><summary>Answer</summary>

**Answer: C.** SGs track connections and allow return traffic. NACLs evaluate each packet and need explicit return rules (ephemeral ports).

</details>

### Q5. Which IPsec component encrypts the payload and is IP protocol 50?

- A) IKE
- B) GRE
- C) AH
- D) ESP

<details><summary>Answer</summary>

**Answer: D.** ESP (protocol 50) gives confidentiality and integrity. AH (51) gives integrity only. IKE uses UDP 500/4500.

</details>

### Q6. Which UDP ports does IKEv2 use when a NAT device is between the peers?

- A) 443 only
- B) 500 then 4500
- C) 1701
- D) 1812 and 1813

<details><summary>Answer</summary>

**Answer: B.** IKE starts on UDP 500. When NAT is detected, IKE and ESP move to UDP 4500 (NAT traversal).

</details>

### Q7. Which TWO statements about TACACS+ compared with RADIUS are true? (Choose two.)

- A) TACACS+ encrypts the entire payload
- B) TACACS+ uses TCP port 49
- C) TACACS+ is the IETF standard for 802.1X
- D) TACACS+ uses UDP 1812
- E) TACACS+ combines authentication and authorization

<details><summary>Answer</summary>

**Answer: A, B.** TACACS+ uses TCP 49, encrypts the whole body and separates A, A and A. RADIUS (UDP 1812/1813) is used for 802.1X and encrypts only the password.

</details>

### Q8. In 802.1X, which device is the authenticator?

- A) The switch or WLC
- B) The DHCP server
- C) The laptop
- D) The RADIUS server

<details><summary>Answer</summary>

**Answer: A.** Supplicant = client, authenticator = switch/WLC, authentication server = RADIUS.

</details>

### Q9. Scenario: After you enable DHCP snooping on an access switch, no client gets an IP address. The DHCP server is reached through the uplink G1/0/48. What did you forget?

- A) Port security on G1/0/48
- B) `spanning-tree portfast` on G1/0/48
- C) `ip arp inspection` on all ports
- D) `ip dhcp snooping trust` on G1/0/48

<details><summary>Answer</summary>

**Answer: D.** All ports are untrusted by default, so server replies on the uplink are dropped. Trust the uplink. (Option 82 insertion can also cause servers to reject requests; `no ip dhcp snooping information option` fixes that.)

</details>

### Q10. What does Dynamic ARP Inspection use to validate ARP packets?

- A) The MAC address table
- B) The DHCP snooping binding table (or ARP ACLs)
- C) The routing table
- D) CDP neighbor data

<details><summary>Answer</summary>

**Answer: B.** DAI compares the sender IP/MAC in ARP packets with the DHCP snooping bindings on untrusted ports.

</details>

### Q11. Which feature drops rogue IPv6 Router Advertisements on host-facing ports?

- A) BPDU guard
- B) Storm control
- C) DHCP snooping
- D) RA guard

<details><summary>Answer</summary>

**Answer: D.** RA guard blocks RAs from ports configured with a host role.

</details>

### Q12. Scenario: `aaa authentication login default group tacacs+ local` is configured. The TACACS+ server is reachable but rejects the admin's password. What happens?

- A) Login fails; local is used only if the server does not respond
- B) The router allows login without a password
- C) The router tries the local user database
- D) The router uses RADIUS

<details><summary>Answer</summary>

**Answer: A.** The next method is tried only on an error (no response), not on a rejection.

</details>

### Q13. Which VPN type usually works through restrictive firewalls because it uses TCP or UDP 443?

- A) GRE
- B) SSL/TLS VPN
- C) IPsec with AH
- D) L2TP without IPsec

<details><summary>Answer</summary>

**Answer: B.** TLS-based VPNs (AnyConnect/Secure Client, OpenVPN, AWS Client VPN) run over 443, which is almost always open.

</details>

### Q14. Which principle best describes zero trust?

- A) Disable encryption internally for performance
- B) Trust everything inside the corporate network
- C) Use only one large firewall at the perimeter
- D) Authenticate and authorize every request based on identity, device and context, regardless of network location

<details><summary>Answer</summary>

**Answer: D.** Zero trust removes implicit trust based on location (NIST SP 800-207).

</details>

### Q15. Scenario: A named extended ACL has entry 10 `permit ip any any` and entry 20 `deny tcp any any eq 23`. Telnet traffic still passes. Why?

- A) Telnet uses UDP
- B) Named ACLs process from the bottom up
- C) The ACL must be numbered to deny Telnet
- D) The first matching entry (10) permits it, so entry 20 is never checked

<details><summary>Answer</summary>

**Answer: D.** ACLs are processed top down and stop at the first match. Put specific denies before broad permits.

</details>
