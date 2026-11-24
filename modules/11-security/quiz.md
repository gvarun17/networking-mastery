# Quiz 11 — Security

## Questions

### Q1. Where should you place a standard ACL?

- A) As close to the source as possible
- B) As close to the destination as possible
- C) On every interface
- D) Only on VTY lines

<details><summary>Answer</summary>

**Answer: B.** Standard ACLs match only the source address. Placed near the source, they would block that source from every destination.

</details>

### Q2. What does the wildcard mask 0.0.0.255 match with 10.10.10.0?

- A) Only 10.10.10.0
- B) 10.10.10.0 through 10.10.10.255
- C) 10.10.0.0 through 10.10.255.255
- D) Every address

<details><summary>Answer</summary>

**Answer: B.** Wildcard 0 bits must match; 1 bits are "don't care". The last octet can be anything.

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

- A) Both are stateless
- B) Security groups are stateful; NACLs are stateless
- C) Security groups are stateless; NACLs are stateful
- D) Both are stateful

<details><summary>Answer</summary>

**Answer: B.** SGs track connections and allow return traffic. NACLs evaluate each packet and need explicit return rules (ephemeral ports).

</details>

### Q5. Which IPsec component encrypts the payload and is IP protocol 50?

- A) AH
- B) ESP
- C) IKE
- D) GRE

<details><summary>Answer</summary>

**Answer: B.** ESP (protocol 50) gives confidentiality and integrity. AH (51) gives integrity only. IKE uses UDP 500/4500.

</details>

### Q6. Which UDP ports does IKEv2 use when a NAT device is between the peers?

- A) 500 then 4500
- B) 1812 and 1813
- C) 1701
- D) 443 only

<details><summary>Answer</summary>

**Answer: A.** IKE starts on UDP 500. When NAT is detected, IKE and ESP move to UDP 4500 (NAT traversal).

</details>

### Q7. Which TWO statements about TACACS+ compared with RADIUS are true? (Choose two.)

- A) TACACS+ uses TCP port 49
- B) TACACS+ encrypts the entire payload
- C) TACACS+ combines authentication and authorization
- D) TACACS+ is the IETF standard for 802.1X
- E) TACACS+ uses UDP 1812

<details><summary>Answer</summary>

**Answer: A, B.** TACACS+ uses TCP 49, encrypts the whole body and separates A, A and A. RADIUS (UDP 1812/1813) is used for 802.1X and encrypts only the password.

</details>

### Q8. In 802.1X, which device is the authenticator?

- A) The laptop
- B) The switch or WLC
- C) The RADIUS server
- D) The DHCP server

<details><summary>Answer</summary>

**Answer: B.** Supplicant = client, authenticator = switch/WLC, authentication server = RADIUS.

</details>

### Q9. Scenario: After you enable DHCP snooping on an access switch, no client gets an IP address. The DHCP server is reached through the uplink G1/0/48. What did you forget?

- A) `ip dhcp snooping trust` on G1/0/48
- B) Port security on G1/0/48
- C) `ip arp inspection` on all ports
- D) `spanning-tree portfast` on G1/0/48

<details><summary>Answer</summary>

**Answer: A.** All ports are untrusted by default, so server replies on the uplink are dropped. Trust the uplink. (Option 82 insertion can also cause servers to reject requests; `no ip dhcp snooping information option` fixes that.)

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

- A) DHCP snooping
- B) RA guard
- C) Storm control
- D) BPDU guard

<details><summary>Answer</summary>

**Answer: B.** RA guard blocks RAs from ports configured with a host role.

</details>

### Q12. Scenario: `aaa authentication login default group tacacs+ local` is configured. The TACACS+ server is reachable but rejects the admin's password. What happens?

- A) The router tries the local user database
- B) Login fails; local is used only if the server does not respond
- C) The router allows login without a password
- D) The router uses RADIUS

<details><summary>Answer</summary>

**Answer: B.** The next method is tried only on an error (no response), not on a rejection.

</details>

### Q13. Which VPN type usually works through restrictive firewalls because it uses TCP or UDP 443?

- A) IPsec with AH
- B) SSL/TLS VPN
- C) GRE
- D) L2TP without IPsec

<details><summary>Answer</summary>

**Answer: B.** TLS-based VPNs (AnyConnect/Secure Client, OpenVPN, AWS Client VPN) run over 443, which is almost always open.

</details>

### Q14. Which principle best describes zero trust?

- A) Trust everything inside the corporate network
- B) Authenticate and authorize every request based on identity, device and context, regardless of network location
- C) Use only one large firewall at the perimeter
- D) Disable encryption internally for performance

<details><summary>Answer</summary>

**Answer: B.** Zero trust removes implicit trust based on location (NIST SP 800-207).

</details>

### Q15. Scenario: A named extended ACL has entry 10 `permit ip any any` and entry 20 `deny tcp any any eq 23`. Telnet traffic still passes. Why?

- A) Telnet uses UDP
- B) The first matching entry (10) permits it, so entry 20 is never checked
- C) Named ACLs process from the bottom up
- D) The ACL must be numbered to deny Telnet

<details><summary>Answer</summary>

**Answer: B.** ACLs are processed top down and stop at the first match. Put specific denies before broad permits.

</details>
