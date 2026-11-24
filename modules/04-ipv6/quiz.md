# Quiz 04 — IPv6

### Q1. Which is the correct compressed form of 2001:0db8:0000:0000:00a0:0000:0000:0001?
- A) 2001:db8::a0::1
- B) 2001:db8::a0:0:0:1
- C) 2001:db8:0:0:a0::1
- D) 2001:db8::a:1

<details><summary>Answer</summary>

**Answer: B.** You can use `::` only once. Both zero runs are two groups long; RFC 5952 compresses the first. Leading zeros are removed (00a0 → a0). C is a valid address but not the RFC 5952 canonical form. A uses `::` twice. D changes the value.

</details>

### Q2. Which prefix identifies IPv6 link-local addresses?
- A) fc00::/7
- B) fe80::/10
- C) ff00::/8
- D) 2000::/3

<details><summary>Answer</summary>

**Answer: B.** fe80::/10 is link-local. fc00::/7 is unique local, ff00::/8 is multicast and 2000::/3 is global unicast.

</details>

### Q3. What replaces ARP in IPv6?
- A) DHCPv6
- B) Neighbor Discovery Protocol using ICMPv6 NS and NA
- C) Inverse ARP
- D) IGMP

<details><summary>Answer</summary>

**Answer: B.** NDP uses ICMPv6 Neighbor Solicitation (135) and Neighbor Advertisement (136) to resolve addresses.

</details>

### Q4. A router interface has MAC 00:1c:73:aa:bb:cc. What is its EUI-64 interface ID?
- A) 001c:73ff:feaa:bbcc
- B) 021c:73ff:feaa:bbcc
- C) 021c:73fe:ffaa:bbcc
- D) 001c:73fe:ffaa:bbcc

<details><summary>Answer</summary>

**Answer: B.** Insert ff:fe in the middle → 00:1c:73:ff:fe:aa:bb:cc. Flip the U/L bit (7th bit) of the first byte: 00 → 02.

</details>

### Q5. Which multicast address does a host use to reach all routers on the local link?
- A) ff02::1
- B) ff02::2
- C) ff02::5
- D) ff02::1:2

<details><summary>Answer</summary>

**Answer: B.** ff02::2 is all routers. ff02::1 is all nodes, ff02::5 is OSPFv3 routers, ff02::1:2 is DHCPv6 relay agents and servers.

</details>

### Q6. Scenario: A host receives an RA with M=0, O=1 and the A flag set in the prefix option. How does it configure itself?
- A) Stateful DHCPv6 for address and DNS
- B) SLAAC for the address and stateless DHCPv6 for options such as DNS
- C) SLAAC only, with no DHCPv6
- D) Manual configuration only

<details><summary>Answer</summary>

**Answer: B.** A=1 → build an address with SLAAC. O=1 → get other configuration (DNS, domain) from a stateless DHCPv6 server. M=1 would mean stateful DHCPv6 addresses.

</details>

### Q7. Where does an IPv6 host learn its default gateway?
- A) From the DHCPv6 server
- B) From the source address of Router Advertisements (a link-local address)
- C) From the DNS server
- D) From the solicited-node multicast group

<details><summary>Answer</summary>

**Answer: B.** The RA's source link-local address becomes the default gateway. DHCPv6 has no default-gateway option.

</details>

### Q8. Which command enables IPv6 routing and Router Advertisements on a Cisco router?
- A) ipv6 enable
- B) ipv6 unicast-routing
- C) ipv6 address autoconfig
- D) ipv6 nd ra

<details><summary>Answer</summary>

**Answer: B.** `ipv6 unicast-routing` (global config) enables IPv6 forwarding and RAs. `ipv6 enable` only creates a link-local address on an interface.

</details>

### Q9. What is the solicited-node multicast address for 2001:db8:1::a:1234:5678?
- A) ff02::1:ff34:5678
- B) ff02::1:ff12:3456
- C) ff02::1:ffa:1234
- D) ff02::2:ff34:5678

<details><summary>Answer</summary>

**Answer: A.** Solicited-node = ff02::1:ff + the last 24 bits of the address. The last 24 bits of ...:1234:5678 are 34:5678.

</details>

### Q10. Which device is allowed to fragment an IPv6 packet?
- A) Any router in the path
- B) Only the source host
- C) Only the destination host
- D) Only the first-hop router

<details><summary>Answer</summary>

**Answer: B.** IPv6 routers never fragment. They drop oversized packets and send ICMPv6 type 2 "Packet Too Big". The source uses PMTUD and fragments if needed.

</details>

### Q11. Scenario: In an AWS IPv6-enabled VPC, private instances must reach the IPv6 internet for updates but must not accept inbound connections from it. What do you use?
- A) NAT gateway
- B) Internet gateway with a public route
- C) Egress-only internet gateway
- D) VPC endpoint

<details><summary>Answer</summary>

**Answer: C.** An egress-only internet gateway allows outbound IPv6 and return traffic only. IPv6 has no NAT, so a NAT gateway is the IPv4 tool (it is used for NAT64 only).

</details>

### Q12. What is the recommended prefix length for an IPv6 LAN subnet?
- A) /48
- B) /56
- C) /64
- D) /127

<details><summary>Answer</summary>

**Answer: C.** /64 is required for SLAAC and is standard for LANs. /127 is recommended for point-to-point router links (RFC 6164). /48 and /56 are site allocations.

</details>

### Q13. Which TWO ICMPv6 message types must a firewall permit for basic IPv6 operation on a LAN? (Choose two.)
- A) Type 128 Echo Request only
- B) Type 135/136 Neighbor Solicitation/Advertisement
- C) Type 2 Packet Too Big
- D) Type 255 Reserved
- E) Type 200 Private experimentation

<details><summary>Answer</summary>

**Answer: B, C.** NS/NA are needed for address resolution. Packet Too Big is needed for path MTU discovery. Echo is useful but not required.

</details>

### Q14. Scenario: A host has only an fe80:: address on its interface. Other hosts on the same VLAN have global addresses. What is the most likely cause?
- A) The host's DNS is wrong
- B) The host does not receive Router Advertisements (for example, accept_ra is disabled or RAs are filtered)
- C) The host's MTU is 1500
- D) The router has too many routes

<details><summary>Answer</summary>

**Answer: B.** Link-local addresses are always created. A global SLAAC address needs an RA with a prefix. Check `accept_ra` (Linux turns it off when forwarding is on) and RA Guard settings.

</details>

### Q15. Which address type do you use for internal-only IPv6 addressing, like RFC 1918 in IPv4?
- A) Global unicast 2001:db8::/32
- B) Unique local fd00::/8
- C) Link-local fe80::/10
- D) Multicast ff05::/16

<details><summary>Answer</summary>

**Answer: B.** Unique local addresses (fc00::/7, with fd00::/8 used in practice and a random 40-bit global ID) are routable inside an organization but not on the internet. 2001:db8::/32 is for documentation only.

</details>
