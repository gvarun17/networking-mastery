# CCNA 200-301 v2.0 — Practice Exam 2

**Format:** 100 questions · 120 minutes · target score 85% (the real passing score is not published; aim high).
Original questions written for this repo, not exam dumps. Simulations are in [../labs/](../labs/README.md).

Run interactively: `python3 tools/quiz_runner.py cert/ccna-200-301/practice-exams/exam-2.md --shuffle`

| Domain | Questions |
|---|---|
| 1.0 Network Infrastructure and Connectivity | 25 |
| 2.0 Switching and Network Access | 25 |
| 3.0 IP Routing | 20 |
| 4.0 Network Services and Security | 20 |
| 5.0 AI, and Network Operations and Management | 10 |

Rules: no notes, one sitting, mark questions to revisit, never leave a question blank.

### Q1. Which Ansible file lists the devices to manage and their variables?
- A) Playbook
- B) Inventory
- C) Role
- D) ansible.cfg only

<details><summary>Answer</summary>

**Answer: B.** Playbooks define tasks; inventories define hosts and groups. *(Domain 5)*

</details>

### Q2. What is the main benefit of an EtherChannel compared with two separate trunk links between the same switches?
- A) STP sees one logical link, so both physical links forward and traffic is load-shared
- B) It removes the need for VLANs
- C) It encrypts traffic
- D) It doubles the speed of each flow

<details><summary>Answer</summary>

**Answer: A.** Load sharing is per flow; a single flow still uses one member link. *(Domain 2)*

</details>

### Q3. An IPv6 host has a global address but no default route. Which message did it probably not receive?
- A) Neighbor Advertisement
- B) Router Advertisement with a non-zero router lifetime
- C) DHCPv6 Reply
- D) ICMPv6 Echo Reply

<details><summary>Answer</summary>

**Answer: B.** The default route comes from RAs; DHCPv6 does not provide a gateway. *(Domain 1)*

</details>

### Q4. Which global command enables a Cisco router to act as an SCP server for file transfers?
- A) ip scp server enable
- B) scp enable
- C) ip ssh scp
- D) file scp server

<details><summary>Answer</summary>

**Answer: A.** SCP requires SSH and AAA authorization for the user. *(Domain 4)*

</details>

### Q5. Which management approach configures each device individually through its own CLI?
- A) Controller-based
- B) Device-based (traditional)
- C) Cloud-based
- D) Infrastructure as code

<details><summary>Answer</summary>

**Answer: B.** Traditional management is per device, usually SSH. *(Domain 5)*

</details>

### Q6. Which TWO practices make an AI agent safer in a production network? (Choose 2.)
- A) Least-privilege, read-only tool access by default
- B) Human approval before configuration changes, with audit logs
- C) Giving the agent enable-level access to all devices
- D) Disabling logging to save storage
- E) Allowing the agent to change its own permissions

<details><summary>Answer</summary>

**Answer: A, B.** Restrict tools, require approvals for changes, log everything. *(Domain 5)*

</details>

### Q7. Which TWO settings must match on all member ports for an EtherChannel to bundle? (Choose 2.)
- A) Speed and duplex
- B) Trunk/access mode and allowed VLANs
- C) Interface descriptions
- D) CDP neighbor names
- E) Port numbers

<details><summary>Answer</summary>

**Answer: A, B.** Members must share speed, duplex, mode, VLAN settings and native VLAN. *(Domain 2)*

</details>

### Q8. What is the network address of host 172.28.241.201/25?
- A) 172.28.242.0
- B) 172.28.241.128
- C) 172.28.241.0
- D) 172.28.241.255

<details><summary>Answer</summary>

**Answer: B.** /25 has 128 addresses per subnet; 172.28.241.201 falls in 172.28.241.128/25 (broadcast 172.28.241.255). *(Domain 1)*

</details>

### Q9. Which IPv6 address type is automatically configured on every IPv6-enabled interface and used for neighbor discovery and routing protocol next hops?
- A) Global unicast
- B) Unique local
- C) Link-local (fe80::/10)
- D) Anycast

<details><summary>Answer</summary>

**Answer: C.** Every interface creates a link-local address; NDP and IGP neighbors use it. *(Domain 1)*

</details>

### Q10. With the default reference bandwidth of 100 Mbps, why do Gigabit and 10-Gigabit links get the same OSPF cost?
- A) OSPF ignores bandwidth
- B) 100/1000 and 100/10000 round up to the minimum cost of 1
- C) They use different areas
- D) Cisco caps cost at 10

<details><summary>Answer</summary>

**Answer: B.** Set `auto-cost reference-bandwidth` higher on every router. *(Domain 3)*

</details>

### Q11. Host A is 172.29.43.109/21. Which host is in the same subnet as Host A (same mask)?
- A) 172.29.52.200
- B) 172.29.56.206
- C) 172.29.41.16
- D) 172.29.37.37

<details><summary>Answer</summary>

**Answer: C.** Host A is in 172.29.40.0/21; only 172.29.41.16 falls inside 172.29.40.0-172.29.47.255. *(Domain 1)*

</details>

### Q12. Which pair of channel-group modes on two connected switches forms an EtherChannel?
- A) auto / auto
- B) passive / passive
- C) auto / passive
- D) on / on

<details><summary>Answer</summary>

**Answer: D.** LACP: active-active or active-passive. PAgP: desirable-desirable or desirable-auto. Static: on-on. Modes from different protocols never bundle. *(Domain 2)*

</details>

### Q13. Which command enables LLDP globally on a Cisco switch?
- A) lldp enable
- B) lldp run
- C) cdp run lldp
- D) lldp transmit

<details><summary>Answer</summary>

**Answer: B.** `lldp run` (global). Per-interface `lldp transmit`/`lldp receive` can then be adjusted. *(Domain 2)*

</details>

### Q14. Which value is a valid STP bridge priority?
- A) 1000
- B) 20480
- C) 33000
- D) 65536

<details><summary>Answer</summary>

**Answer: B.** Priorities are multiples of 4096 from 0 to 61440 (20480 = 5 × 4096). *(Domain 2)*

</details>

### Q15. How do you configure a Layer 3 EtherChannel on a multilayer switch?
- A) Apply `no switchport` to the members and the port-channel, then put the IP address on the port-channel
- B) Put IP addresses on each member port
- C) Use `switchport mode trunk` on the port-channel
- D) Use PAgP only

<details><summary>Answer</summary>

**Answer: A.** Routed members bundle into a routed Port-channel interface that holds the IP. *(Domain 2)*

</details>

### Q16. A router has these routes: S* 0.0.0.0/0 via 203.0.113.1; O 10.70.0.0/16 via 10.0.12.2; O 10.70.144.0/20 via 10.0.13.3; D 10.70.145.0/24 via 10.0.14.4; S 10.70.145.192/26 via 10.0.15.5. Which next hop is used for a packet to 10.70.31.145?
- A) 10.0.14.4
- B) 10.0.12.2
- C) 10.0.13.3
- D) 203.0.113.1

<details><summary>Answer</summary>

**Answer: B.** Longest prefix match: the most specific route that contains 10.70.31.145 wins, regardless of AD. *(Domain 3)*

</details>

### Q17. A new router with OSPF priority 200 joins a LAN that already has a DR with priority 1. What happens?
- A) It becomes DR immediately
- B) Nothing until the current DR and BDR fail; OSPF DR election is not preemptive
- C) The current DR reloads
- D) The new router becomes BDR immediately regardless

<details><summary>Answer</summary>

**Answer: B.** DR/BDR election happens only when the roles are vacant. *(Domain 3)*

</details>

### Q18. Which TWO commands verify Layer 3 connectivity and the path to a remote host from a Cisco router? (Choose 2.)
- A) ping
- B) traceroute
- C) show vlan brief
- D) show mac address-table
- E) show spanning-tree

<details><summary>Answer</summary>

**Answer: A, B.** ping tests reachability; traceroute shows each hop. *(Domain 2)*

</details>

### Q19. What does PMF (802.11w), mandatory in WPA3, protect against?
- A) Co-channel interference
- B) Forged deauthentication/disassociation frames
- C) DHCP starvation
- D) Hidden nodes

<details><summary>Answer</summary>

**Answer: B.** Protected Management Frames authenticate management frames. *(Domain 1)*

</details>

### Q20. Which address can be assigned to a host in subnet 172.24.40.192/26?
- A) 172.24.40.247
- B) 172.24.40.192
- C) 172.24.40.255
- D) 172.24.41.0

<details><summary>Answer</summary>

**Answer: A.** 172.24.40.192/26 spans 172.24.40.192-172.24.40.255; usable hosts are 172.24.40.193-172.24.40.254. *(Domain 1)*

</details>

### Q21. What is the default OSPF hello/dead interval on broadcast and point-to-point networks?
- A) 5/15 seconds
- B) 10/40 seconds
- C) 30/120 seconds
- D) 60/180 seconds

<details><summary>Answer</summary>

**Answer: B.** NBMA uses 30/120. *(Domain 3)*

</details>

### Q22. The primary default route is learned by EIGRP. Which administrative distance makes a backup static default route float (used only if the EIGRP route is lost)?
- A) 1
- B) 89
- C) 90
- D) 121

<details><summary>Answer</summary>

**Answer: D.** The static route needs an AD higher than EIGRP (90); equal AD would compete and a lower AD would win. *(Domain 3)*

</details>

### Q23. Two OSPF routers on a point-to-point Ethernet link show `FULL/  -` in `show ip ospf neighbor`. What does the `-` mean?
- A) The neighbor is down
- B) No DR/BDR election (point-to-point network type)
- C) Authentication failed
- D) The neighbor is a DROTHER

<details><summary>Answer</summary>

**Answer: B.** Point-to-point links do not elect a DR. *(Domain 3)*

</details>

### Q24. Which wildcard mask matches the same addresses as subnet mask 255.255.255.224 in an ACL?
- A) 0.0.0.63
- B) 0.0.0.15
- C) 255.255.255.224
- D) 0.0.0.31

<details><summary>Answer</summary>

**Answer: D.** Wildcard = 255.255.255.255 − mask = 0.0.0.31. *(Domain 4)*

</details>

### Q25. Which command saves a switch's running configuration so VLAN-to-port settings survive a reload?
- A) copy running-config startup-config
- B) write erase
- C) reload
- D) show startup-config

<details><summary>Answer</summary>

**Answer: A.** VLAN definitions live in vlan.dat (VTP transparent/server) and port settings in the config. *(Domain 2)*

</details>

### Q26. Which TWO commands advertise interface G0/1 (10.1.12.1/30) into OSPF area 0? (Choose 2.)
- A) `network 10.1.12.0 0.0.0.3 area 0` under router ospf
- B) `ip ospf 1 area 0` under interface G0/1
- C) `network 10.1.12.0 255.255.255.252 area 0`
- D) `ospf area 0` globally
- E) `redistribute connected` only

<details><summary>Answer</summary>

**Answer: A, B.** OSPF network statements use wildcard masks; the interface command is an alternative. *(Domain 3)*

</details>

### Q27. Which TWO statements about TACACS+ are correct? (Choose 2.)
- A) Uses TCP port 49
- B) Encrypts the entire packet body
- C) Uses UDP 1812
- D) Combines authentication and authorization
- E) Is mainly used for 802.1X

<details><summary>Answer</summary>

**Answer: A, B.** TACACS+ separates AAA functions and suits device administration. *(Domain 4)*

</details>

### Q28. Which global command enables Rapid PVST+?
- A) spanning-tree mode rapid-pvst
- B) spanning-tree rstp enable
- C) spanning-tree mode mst
- D) spanning-tree portfast default

<details><summary>Answer</summary>

**Answer: A.** Rapid PVST+ runs one RSTP instance per VLAN. *(Domain 2)*

</details>

### Q29. A router has `logging trap informational`. Which messages are sent to the syslog server?
- A) Level 6 only
- B) Levels 0 through 6
- C) All levels 0 through 7
- D) Levels 6 through 7

<details><summary>Answer</summary>

**Answer: B.** The configured level (6) and every more severe (lower) level are sent. *(Domain 5)*

</details>

### Q30. Users report one-way traffic: R1 → R3 works, replies fail. R3 has no route to R1's LAN. Which fix is correct?
- A) Add a route on R3 back to R1's LAN (or advertise it in the IGP)
- B) Change R1's MTU
- C) Enable PortFast on R3
- D) Add a NAT rule on R1

<details><summary>Answer</summary>

**Answer: A.** Every path needs a return route. *(Domain 3)*

</details>

### Q31. What does the code `L` mean in `show ip route` output?
- A) Learned by LDP
- B) A local /32 route for an IP address configured on the router's own interface
- C) A floating static route
- D) A route learned by LLDP

<details><summary>Answer</summary>

**Answer: B.** Each interface IP creates a C (connected subnet) and an L (local host) route. *(Domain 3)*

</details>

### Q32. What is infrastructure as code for networks?
- A) Typing commands faster
- B) Declaring desired network state in version-controlled files that a pipeline validates and applies
- C) Using only GUI tools
- D) Storing configs on USB drives

<details><summary>Answer</summary>

**Answer: B.** Git, templates, CI checks and automated deployment. *(Domain 5)*

</details>

### Q33. Which interface counter usually points to frames larger than the configured MTU arriving on a port?
- A) Runts
- B) Giants
- C) CRC
- D) Output drops

<details><summary>Answer</summary>

**Answer: B.** Giants are frames above the maximum size (1518 bytes untagged without jumbo). *(Domain 1)*

</details>

### Q34. Which statement about the 802.1Q native VLAN is true?
- A) Frames in the native VLAN are tagged with VID 0
- B) Frames in the native VLAN are sent untagged on the trunk
- C) The native VLAN must be VLAN 1
- D) Native VLAN mismatches are harmless

<details><summary>Answer</summary>

**Answer: B.** Native VLAN traffic is untagged; mismatches leak traffic between VLANs and CDP logs a warning. *(Domain 2)*

</details>

### Q35. An ACL entry is `permit ip 10.31.240.0 0.0.15.255 any`. Which source address matches it?
- A) 10.32.0.10
- B) 10.31.247.77
- C) 10.32.16.2
- D) 10.31.239.218

<details><summary>Answer</summary>

**Answer: B.** 10.31.240.0 0.0.15.255 covers 10.31.240.0-10.31.255.255 (10.31.240.0/20). *(Domain 4)*

</details>

### Q36. A network printer must always use the same port and only its own MAC. Which feature enforces this?
- A) Port security with maximum 1 and a sticky or static MAC
- B) Root guard
- C) DTP
- D) LLDP

<details><summary>Answer</summary>

**Answer: A.** Port security limits learned MACs and reacts to violations. *(Domain 2)*

</details>

### Q37. Which wildcard mask matches the same addresses as subnet mask 255.255.255.248 in an ACL?
- A) 0.0.0.3
- B) 0.0.0.7
- C) 0.0.0.15
- D) 255.255.255.248

<details><summary>Answer</summary>

**Answer: B.** Wildcard = 255.255.255.255 − mask = 0.0.0.7. *(Domain 4)*

</details>

### Q38. An ACL entry is `permit ip 10.182.27.0 0.0.0.31 any`. Which source address matches it?
- A) 10.182.27.66
- B) 10.182.26.246
- C) 10.182.27.7
- D) 10.182.27.213

<details><summary>Answer</summary>

**Answer: C.** 10.182.27.0 0.0.0.31 covers 10.182.27.0-10.182.27.31 (10.182.27.0/27). *(Domain 4)*

</details>

### Q39. In VRRP, what role does the router forwarding traffic for the virtual IP hold?
- A) Active
- B) Master
- C) Primary
- D) Designated

<details><summary>Answer</summary>

**Answer: B.** VRRP uses master/backup; HSRP uses active/standby. *(Domain 3)*

</details>

### Q40. Which TWO are common sources of 2.4 GHz interference? (Choose 2.)
- A) Microwave ovens
- B) Bluetooth devices
- C) Weather radar
- D) Fiber optic cables
- E) 6 GHz APs

<details><summary>Answer</summary>

**Answer: A, B.** Microwave ovens and Bluetooth share 2.4 GHz. Radar affects 5 GHz DFS channels. *(Domain 1)*

</details>

### Q41. Host A is 10.219.45.166/21. Which host is in the same subnet as Host A (same mask)?
- A) 10.219.40.142
- B) 10.219.63.132
- C) 10.219.34.130
- D) 10.219.51.34

<details><summary>Answer</summary>

**Answer: A.** Host A is in 10.219.40.0/21; only 10.219.40.142 falls inside 10.219.40.0-10.219.47.255. *(Domain 1)*

</details>

### Q42. A trunk between SW1 and SW2 uses native VLAN 99 on SW1 and native VLAN 1 on SW2. Which TWO results are expected? (Choose 2.)
- A) CDP logs a native VLAN mismatch
- B) Untagged traffic crosses between VLAN 99 and VLAN 1
- C) The trunk becomes an EtherChannel
- D) All tagged VLANs stop working
- E) STP is disabled

<details><summary>Answer</summary>

**Answer: A, B.** Tagged VLANs still work; untagged frames land in the wrong VLAN. *(Domain 2)*

</details>

### Q43. A router learns 10.9.163.0/24 from RIP, EIGRP external, EIGRP (internal). Which source is installed in the routing table (default ADs)?
- A) All three, load-balanced
- B) RIP
- C) EIGRP (internal)
- D) EIGRP external

<details><summary>Answer</summary>

**Answer: C.** Same prefix from different sources: lowest administrative distance wins. EIGRP (internal) = 90. *(Domain 3)*

</details>

### Q44. Which wildcard mask matches the same addresses as subnet mask 255.255.248.0 in an ACL?
- A) 0.0.3.255
- B) 255.255.248.0
- C) 0.0.7.255
- D) 0.0.15.255

<details><summary>Answer</summary>

**Answer: C.** Wildcard = 255.255.255.255 − mask = 0.0.7.255. *(Domain 4)*

</details>

### Q45. What is the network address of host 192.168.215.231/26?
- A) 192.168.215.128
- B) 192.168.216.0
- C) 192.168.215.192
- D) 192.168.215.255

<details><summary>Answer</summary>

**Answer: C.** /26 has 64 addresses per subnet; 192.168.215.231 falls in 192.168.215.192/26 (broadcast 192.168.215.255). *(Domain 1)*

</details>

### Q46. What is the broadcast address of the subnet that contains 192.168.13.155/24?
- A) 192.168.13.0
- B) 192.168.13.254
- C) 192.168.13.255
- D) 192.168.14.0

<details><summary>Answer</summary>

**Answer: C.** Network 192.168.13.0/24; the broadcast is the last address of the block, 192.168.13.255. *(Domain 1)*

</details>

### Q47. Which UDP ports does IKE use with and without NAT traversal?
- A) 500 and 4500
- B) 1812 and 1813
- C) 161 and 162
- D) 1701 and 1723

<details><summary>Answer</summary>

**Answer: A.** IKE starts on 500 and moves to 4500 when NAT is detected (ESP is then UDP-encapsulated). *(Domain 4)*

</details>

### Q48. What is the difference between an SNMP trap and an inform?
- A) Traps are acknowledged; informs are not
- B) Informs are acknowledged by the manager; traps are not
- C) Traps use TCP
- D) There is no difference

<details><summary>Answer</summary>

**Answer: B.** Informs are retransmitted until acknowledged, so they are more reliable. *(Domain 5)*

</details>

### Q49. Why do dense 5 GHz deployments often use 20 MHz or 40 MHz channels instead of 80 MHz?
- A) Wider channels are not supported in 5 GHz
- B) Narrower channels give more non-overlapping channels and less co-channel interference
- C) Narrower channels increase range tenfold
- D) WPA3 requires 20 MHz

<details><summary>Answer</summary>

**Answer: B.** More channels means better reuse across many APs, which improves airtime efficiency. *(Domain 1)*

</details>

### Q50. Which device connects virtual machines on the same host to each other and to the physical network?
- A) A virtual switch (vSwitch)
- B) A WLC
- C) A firewall appliance only
- D) A DHCP relay

<details><summary>Answer</summary>

**Answer: A.** The hypervisor's virtual switch forwards frames between VM vNICs and uplinks, often with VLAN tagging. *(Domain 1)*

</details>

### Q51. `aaa authentication login default group tacacs+ local` is configured. When is the local database used?
- A) Always first
- B) Only when no TACACS+ server responds
- C) When TACACS+ rejects the password
- D) Never

<details><summary>Answer</summary>

**Answer: B.** Fallback happens on error (no response), not on a failed authentication. *(Domain 4)*

</details>

### Q52. Which subnet mask supports 5 hosts on one subnet while wasting the fewest addresses?
- A) 255.255.255.224
- B) 255.255.255.248
- C) 255.255.255.240
- D) 255.255.255.252

<details><summary>Answer</summary>

**Answer: B.** /29 (255.255.255.248) gives 6 usable hosts; /30 gives only 2. *(Domain 1)*

</details>

### Q53. How many usable host addresses does a /22 IPv4 subnet provide?
- A) 510
- B) 2,046
- C) 1,022
- D) 1,024

<details><summary>Answer</summary>

**Answer: C.** 2^10 − 2 = 1,022 (network and broadcast are not usable). *(Domain 1)*

</details>

### Q54. Rapid PVST+ for VLAN 10: SW1 priority 32778 MAC 8603.9b00.e9ed; SW2 priority 32778 MAC 7ed0.73d1.84f0; SW3 priority 8202 MAC 47a6.09c2.cd5a; SW4 priority 28682 MAC 85b1.2b2c.a04f. Which switch becomes the root bridge?
- A) SW3
- B) SW4
- C) SW1
- D) SW2

<details><summary>Answer</summary>

**Answer: A.** Lowest bridge ID wins: compare priority (including the VLAN ID) first, then the lowest MAC. *(Domain 2)*

</details>

### Q55. Which command creates an IPv6 default route through next hop 2001:db8:ffff::1?
- A) ipv6 route ::/0 2001:db8:ffff::1
- B) ipv6 route 0::0/128 2001:db8:ffff::1
- C) ipv6 default-gateway 2001:db8:ffff::1
- D) ip route ::/0 2001:db8:ffff::1

<details><summary>Answer</summary>

**Answer: A.** ::/0 is the IPv6 default route. *(Domain 3)*

</details>

### Q56. Which IPv6 prefix size is recommended for point-to-point router links?
- A) /64
- B) /96
- C) /127
- D) /128

<details><summary>Answer</summary>

**Answer: C.** RFC 6164 recommends /127 for inter-router links; /128 is a single host (loopback). *(Domain 1)*

</details>

### Q57. A non-root switch (short STP costs) has three uplinks. Port 1: TenGigabitEthernet (cost 2), neighbor advertises root path cost 0; Port 2: TenGigabitEthernet (cost 2), neighbor advertises root path cost 4; Port 3: GigabitEthernet (cost 4), neighbor advertises root path cost 2. Which port becomes the root port?
- A) Port 3
- B) Port 2
- C) Port 1
- D) None; all three forward

<details><summary>Answer</summary>

**Answer: C.** Root port = lowest total cost to the root (advertised cost + local port cost). Port 1 totals 2. *(Domain 2)*

</details>

### Q58. Which Windows command shows the IP address, mask, gateway, DNS servers and DHCP lease of all adapters?
- A) ipconfig /all
- B) netstat -r
- C) arp -a
- D) tracert

<details><summary>Answer</summary>

**Answer: A.** `ipconfig /all` (Linux: `ip addr`, `ip route`, `resolvectl status`). *(Domain 1)*

</details>

### Q59. Which command configures PAT using the outside interface address for hosts permitted by ACL 1?
- A) ip nat inside source list 1 interface g0/0 overload
- B) ip nat outside source list 1 interface g0/0
- C) ip nat inside source static 1 g0/0
- D) ip nat pool 1 overload

<details><summary>Answer</summary>

**Answer: A.** `overload` enables port address translation. *(Domain 4)*

</details>

### Q60. Which command shows on which switch port a given MAC address was learned?
- A) show arp
- B) show mac address-table address 0050.7966.6800
- C) show interfaces status
- D) show cdp neighbors

<details><summary>Answer</summary>

**Answer: B.** The MAC address table maps MAC, VLAN and port. *(Domain 2)*

</details>

### Q61. Which feature should you enable on distribution switch ports facing access switches to prevent a misconfigured access switch from becoming root?
- A) BPDU filter
- B) Root guard
- C) PortFast
- D) Loop guard

<details><summary>Answer</summary>

**Answer: B.** Root guard puts the port in root-inconsistent state when superior BPDUs arrive. *(Domain 2)*

</details>

### Q62. What does `permit tcp any any established` match?
- A) Only SYN packets
- B) TCP packets with the ACK or RST bit set (return traffic of sessions)
- C) All TCP
- D) Only port 179

<details><summary>Answer</summary>

**Answer: B.** A crude stateless way to allow return traffic; stateful firewalls do this properly. *(Domain 4)*

</details>

### Q63. OSPF uses auto-cost reference-bandwidth 100000 (Mbps). What is the cost of a 1000 Mbps interface?
- A) 10
- B) 1000
- C) 100
- D) 101

<details><summary>Answer</summary>

**Answer: C.** Cost = reference / interface bandwidth = 100000/1000 = 100 (minimum 1). *(Domain 3)*

</details>

### Q64. A static route `ip route 10.9.0.0 255.255.0.0 10.0.99.2` is missing from the routing table. 10.0.99.2 is not reachable through any other route. Why?
- A) Static routes need AD 0
- B) The recursive lookup for the next hop fails, so the route is not installed
- C) The mask is invalid
- D) Static routes appear only after a reload

<details><summary>Answer</summary>

**Answer: B.** A next hop must resolve to a connected or other route. *(Domain 3)*

</details>

### Q65. Which address can be assigned to a host in subnet 172.26.212.0/24?
- A) 172.26.212.255
- B) 172.26.212.142
- C) 172.26.212.0
- D) 172.26.213.0

<details><summary>Answer</summary>

**Answer: B.** 172.26.212.0/24 spans 172.26.212.0-172.26.212.255; usable hosts are 172.26.212.1-172.26.212.254. *(Domain 1)*

</details>

### Q66. Which command on a Cisco router enables DNS resolution of hostnames using server 10.99.0.53?
- A) ip name-server 10.99.0.53 (with ip domain lookup enabled)
- B) ip dns server 10.99.0.53
- C) dns client 10.99.0.53
- D) ip host dns 10.99.0.53

<details><summary>Answer</summary>

**Answer: A.** `ip domain lookup` is on by default on many platforms; `ip name-server` sets the resolver. *(Domain 4)*

</details>

### Q67. Which router interface command makes the router obtain its own IPv4 address from an ISP's DHCP server?
- A) ip address dhcp
- B) ip dhcp client enable
- C) ip helper-address dhcp
- D) dhcp client

<details><summary>Answer</summary>

**Answer: A.** `ip address dhcp` configures the interface as a DHCP client. *(Domain 1)*

</details>

### Q68. A switch port connects a router subinterface design (router on a stick). How must the switch port be configured?
- A) Access port
- B) 802.1Q trunk carrying the routed VLANs
- C) Routed port
- D) Port-channel only

<details><summary>Answer</summary>

**Answer: B.** The router uses `encapsulation dot1q <vlan>` subinterfaces; the switch side is a trunk. *(Domain 2)*

</details>

### Q69. Which TWO features work together to stop a man-in-the-middle attacker who sends forged ARP replies on an access VLAN? (Choose 2.)
- A) DHCP snooping
- B) Dynamic ARP Inspection
- C) Storm control
- D) BPDU guard
- E) LLDP

<details><summary>Answer</summary>

**Answer: A, B.** DAI uses the snooping bindings to reject forged ARP. *(Domain 4)*

</details>

### Q70. A router has these routes: S* 0.0.0.0/0 via 203.0.113.1; O 10.122.0.0/16 via 10.0.12.2; O 10.122.160.0/20 via 10.0.13.3; D 10.122.164.0/24 via 10.0.14.4; S 10.122.164.64/26 via 10.0.15.5. Which next hop is used for a packet to 10.122.23.109?
- A) 203.0.113.1
- B) 10.0.13.3
- C) 10.0.12.2
- D) 10.0.14.4

<details><summary>Answer</summary>

**Answer: C.** Longest prefix match: the most specific route that contains 10.122.23.109 wins, regardless of AD. *(Domain 3)*

</details>

### Q71. Which syslog severity level number is 'critical'?
- A) 3
- B) 4
- C) 1
- D) 2

<details><summary>Answer</summary>

**Answer: D.** 0 emergencies, 1 alerts, 2 critical, 3 errors, 4 warnings, 5 notifications, 6 informational, 7 debugging. *(Domain 5)*

</details>

### Q72. What is the correct shortest form of 2001:0db8:0000:00d0:0000:0000:0000:7b93?
- A) 2001:db8:0:d0:0:0:0:7b93
- B) 2001:db8:0:d0:7b93
- C) 2001:0db8:0000:00d0::0000:7b93
- D) 2001:db8:0:d0::7b93

<details><summary>Answer</summary>

**Answer: D.** Remove leading zeros in each hextet, then replace the longest run of all-zero hextets with :: (only once). *(Domain 1)*

</details>

### Q73. Rapid PVST+ for VLAN 30: SW1 priority 24606 MAC 0d08.df03.3c9c; SW2 priority 32798 MAC 96ce.6d2b.2c2e; SW3 priority 32798 MAC 1137.33c1.4248; SW4 priority 4126 MAC 79e6.a3be.ca7b. Which switch becomes the root bridge?
- A) SW3
- B) SW4
- C) SW1
- D) SW2

<details><summary>Answer</summary>

**Answer: B.** Lowest bridge ID wins: compare priority (including the VLAN ID) first, then the lowest MAC. *(Domain 2)*

</details>

### Q74. A reverse lookup of 203.0.113.25 returns NXDOMAIN. Which record is missing?
- A) A in the forward zone
- B) PTR in 25.113.0.203.in-addr.arpa
- C) MX
- D) TXT

<details><summary>Answer</summary>

**Answer: B.** Reverse DNS uses PTR records under in-addr.arpa. *(Domain 4)*

</details>

### Q75. A router learns 10.216.156.0/24 from static, EIGRP external, iBGP. Which source is installed in the routing table (default ADs)?
- A) EIGRP external
- B) All three, load-balanced
- C) iBGP
- D) static

<details><summary>Answer</summary>

**Answer: D.** Same prefix from different sources: lowest administrative distance wins. static = 1. *(Domain 3)*

</details>

### Q76. Which TWO actions harden unused switch ports? (Choose 2.)
- A) Shut them down
- B) Assign them to an unused 'black hole' VLAN
- C) Configure them as trunks
- D) Enable DTP desirable
- E) Set them as the native VLAN

<details><summary>Answer</summary>

**Answer: A, B.** Shutdown plus an unused VLAN limits accidental or malicious use. *(Domain 2)*

</details>

### Q77. What is the severity of the syslog message `%PM-4-ERR_DISABLE: ...`?
- A) 2 (critical)
- B) 6 (informational)
- C) 5 (notifications)
- D) 4 (warnings)

<details><summary>Answer</summary>

**Answer: D.** Cisco format is %FACILITY-SEVERITY-MNEMONIC; the number after the facility is the severity. *(Domain 5)*

</details>

### Q78. A packet arrives for 172.16.5.9. Routes: 172.16.0.0/16 via A (OSPF), 172.16.4.0/22 via B (static AD 200), 172.16.5.0/24 via C (RIP). Which next hop is used?
- A) A
- B) B
- C) C
- D) Load-balanced across all

<details><summary>Answer</summary>

**Answer: C.** Longest prefix (/24) wins before AD is considered. *(Domain 3)*

</details>

### Q79. A router has these routes: S* 0.0.0.0/0 via 203.0.113.1; O 10.98.0.0/16 via 10.0.12.2; O 10.98.96.0/20 via 10.0.13.3; D 10.98.104.0/24 via 10.0.14.4; S 10.98.104.0/26 via 10.0.15.5. Which next hop is used for a packet to 10.98.14.202?
- A) 10.0.14.4
- B) 10.0.13.3
- C) 10.0.12.2
- D) 203.0.113.1

<details><summary>Answer</summary>

**Answer: C.** Longest prefix match: the most specific route that contains 10.98.14.202 wins, regardless of AD. *(Domain 3)*

</details>

### Q80. What does Dynamic ARP Inspection validate?
- A) DNS replies
- B) ARP packets on untrusted ports against the DHCP snooping binding table or ARP ACLs
- C) STP BPDUs
- D) CDP messages

<details><summary>Answer</summary>

**Answer: B.** DAI stops ARP spoofing/poisoning. *(Domain 4)*

</details>

### Q81. Why might you disable CDP on an internet-facing interface?
- A) It uses too much bandwidth
- B) It reveals device model, software version and addresses to anyone connected
- C) It breaks OSPF
- D) It disables STP

<details><summary>Answer</summary>

**Answer: B.** Discovery protocols leak information; disable them on untrusted ports (`no cdp enable`). *(Domain 2)*

</details>

### Q82. An interface with MAC 5c:38:2f:2a:79:05 uses EUI-64 with prefix 2001:db8:1:1::/64. What is its interface ID?
- A) 5c38:2f2a:7905:0
- B) 5e38:2ffe:ff2a:7905
- C) 5e38:2fff:fe2a:7905
- D) 5c38:2fff:fe2a:7905

<details><summary>Answer</summary>

**Answer: C.** Insert ff:fe between the OUI and NIC parts, then flip the 7th bit (U/L) of the first byte. *(Domain 1)*

</details>

### Q83. What is the broadcast address of the subnet that contains 172.20.47.182/22?
- A) 172.20.44.0
- B) 172.20.47.255
- C) 172.20.47.254
- D) 172.20.48.0

<details><summary>Answer</summary>

**Answer: B.** Network 172.20.44.0/22; the broadcast is the last address of the block, 172.20.47.255. *(Domain 1)*

</details>

### Q84. Which IOS command prevents a DHCP pool from leasing addresses 10.1.1.1 to 10.1.1.20?
- A) ip dhcp pool exclude 10.1.1.1 10.1.1.20
- B) ip dhcp excluded-address 10.1.1.1 10.1.1.20
- C) no ip dhcp 10.1.1.1 10.1.1.20
- D) ip dhcp reserve 10.1.1.1 10.1.1.20

<details><summary>Answer</summary>

**Answer: B.** Excluded addresses are configured in global configuration mode. *(Domain 1)*

</details>

### Q85. Which TWO symptoms indicate a duplex mismatch on a 100 Mbps link? (Choose 2.)
- A) Late collisions on the half-duplex side
- B) CRC or runt errors on the full-duplex side
- C) Err-disabled port
- D) Giants on both sides
- E) Native VLAN mismatch messages

<details><summary>Answer</summary>

**Answer: A, B.** The half-duplex end sees late collisions; the full-duplex end sees damaged frames (CRC/runts). *(Domain 1)*

</details>

### Q86. Which global command must be enabled for a multilayer switch to route between SVIs?
- A) ip routing
- B) vlan routing
- C) ip cef only
- D) router svi

<details><summary>Answer</summary>

**Answer: A.** Without `ip routing`, the switch does not route between VLAN interfaces. *(Domain 2)*

</details>

### Q87. `show interfaces g0/1` displays `GigabitEthernet0/1 is down, line protocol is down (notconnect)`. What do you check first?
- A) The OSPF configuration
- B) The physical connection: cable, transceiver and the device at the other end
- C) The DHCP pool
- D) The NAT table

<details><summary>Answer</summary>

**Answer: B.** down/down with notconnect means no Layer 1 signal. *(Domain 1)*

</details>

### Q88. Which feature blocks rogue IPv6 Router Advertisements from host ports?
- A) RA guard
- B) DHCPv6 relay
- C) BPDU guard
- D) IPv6 ACL on SVI only

<details><summary>Answer</summary>

**Answer: A.** Attach an RA guard policy with device-role host. *(Domain 4)*

</details>

### Q89. How do you insert a new entry between sequence 10 and 20 in a named ACL?
- A) Delete and recreate the ACL
- B) Enter the ACL and add an entry with sequence number 15
- C) Use `ip access-list resequence` only
- D) It is not possible

<details><summary>Answer</summary>

**Answer: B.** Named (and numbered, in named-ACL mode) ACLs support sequence numbers. *(Domain 4)*

</details>

### Q90. A FlexConnect AP switches three SSIDs locally to VLANs 10, 20 and 30. How should its switch port be configured?
- A) Access VLAN 10
- B) Trunk with the management VLAN and VLANs 10, 20, 30 allowed
- C) Routed port
- D) Shut down

<details><summary>Answer</summary>

**Answer: B.** Locally switched client VLANs must reach the AP, so a trunk is needed. *(Domain 2)*

</details>

### Q91. A non-root switch (short STP costs) has three uplinks. Port 1: TenGigabitEthernet (cost 2), neighbor advertises root path cost 19; Port 2: GigabitEthernet (cost 4), neighbor advertises root path cost 0; Port 3: GigabitEthernet (cost 4), neighbor advertises root path cost 4. Which port becomes the root port?
- A) None; all three forward
- B) Port 2
- C) Port 1
- D) Port 3

<details><summary>Answer</summary>

**Answer: B.** Root port = lowest total cost to the root (advertised cost + local port cost). Port 2 totals 4. *(Domain 2)*

</details>

### Q92. Which module would you use to run `show version` on Cisco IOS devices with Ansible?
- A) cisco.ios.ios_command
- B) ansible.builtin.copy
- C) cisco.ios.ios_vlans
- D) community.general.ping

<details><summary>Answer</summary>

**Answer: A.** ios_command runs operational commands; resource modules (ios_vlans, ios_interfaces) manage config. *(Domain 5)*

</details>

### Q93. A router has these routes: S* 0.0.0.0/0 via 203.0.113.1; O 10.51.0.0/16 via 10.0.12.2; O 10.51.32.0/20 via 10.0.13.3; D 10.51.45.0/24 via 10.0.14.4; S 10.51.45.128/26 via 10.0.15.5. Which next hop is used for a packet to 10.51.46.18?
- A) 203.0.113.1
- B) 10.0.13.3
- C) 10.0.14.4
- D) 10.0.12.2

<details><summary>Answer</summary>

**Answer: B.** Longest prefix match: the most specific route that contains 10.51.46.18 wins, regardless of AD. *(Domain 3)*

</details>

### Q94. Why does a Layer 2 loop cause a broadcast storm?
- A) Frames have no TTL, so broadcasts circulate and multiply endlessly
- B) Switches drop broadcasts
- C) ARP is disabled
- D) VLANs are removed

<details><summary>Answer</summary>

**Answer: A.** Ethernet has no hop limit; STP exists to block loops. *(Domain 2)*

</details>

### Q95. Which command sends syslog messages of severity warning and more severe to server 10.99.0.14?
- A) logging host 10.99.0.14 and logging trap warnings
- B) logging buffered 4
- C) logging console 10.99.0.14
- D) snmp-server host 10.99.0.14 warnings

<details><summary>Answer</summary>

**Answer: A.** `logging trap` sets the level sent to remote hosts. *(Domain 5)*

</details>

### Q96. An ACL entry is `permit ip 10.93.128.0 0.0.7.255 any`. Which source address matches it?
- A) 10.93.136.108
- B) 10.93.144.2
- C) 10.93.127.109
- D) 10.93.134.180

<details><summary>Answer</summary>

**Answer: D.** 10.93.128.0 0.0.7.255 covers 10.93.128.0-10.93.135.255 (10.93.128.0/21). *(Domain 4)*

</details>

### Q97. Which port role is held by every active port on the root bridge?
- A) Root
- B) Designated
- C) Alternate
- D) Edge only

<details><summary>Answer</summary>

**Answer: B.** The root has no root port; all its ports are designated. *(Domain 2)*

</details>

### Q98. Which NAT type permanently maps one inside address to one outside address so external users can reach a server?
- A) Dynamic NAT
- B) PAT
- C) Static NAT
- D) NAT64

<details><summary>Answer</summary>

**Answer: C.** `ip nat inside source static 10.1.1.80 203.0.113.80`. *(Domain 4)*

</details>

### Q99. What is at the end of every IPv4 ACL?
- A) An implicit permit any
- B) An implicit deny any
- C) A log statement
- D) Nothing

<details><summary>Answer</summary>

**Answer: B.** Unmatched packets are dropped. *(Domain 4)*

</details>

### Q100. OSPF uses auto-cost reference-bandwidth 100000 (Mbps). What is the cost of a 100 Mbps interface?
- A) 1000
- B) 1001
- C) 100
- D) 10000

<details><summary>Answer</summary>

**Answer: A.** Cost = reference / interface bandwidth = 100000/100 = 1000 (minimum 1). *(Domain 3)*

</details>
