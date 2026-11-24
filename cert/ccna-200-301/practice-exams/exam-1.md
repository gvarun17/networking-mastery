# CCNA 200-301 v2.0 — Practice Exam 1

**Format:** 100 questions · 120 minutes · target score 85% (the real passing score is not published; aim high).
Original questions written for this repo, not exam dumps. Simulations are in [../labs/](../labs/README.md).

Run interactively: `python3 tools/quiz_runner.py cert/ccna-200-301/practice-exams/exam-1.md --shuffle`

| Domain | Questions |
|---|---|
| 1.0 Network Infrastructure and Connectivity | 25 |
| 2.0 Switching and Network Access | 25 |
| 3.0 IP Routing | 20 |
| 4.0 Network Services and Security | 20 |
| 5.0 AI, and Network Operations and Management | 10 |

Rules: no notes, one sitting, mark questions to revisit, never leave a question blank.

### Q1. Which command converts a Layer 3 switch port into a routed port?
- A) switchport mode access
- B) no switchport
- C) ip routing
- D) switchport nonegotiate

<details><summary>Answer</summary>

**Answer: B.** `no switchport` makes the port a Layer 3 interface that can take an IP address. *(Domain 2)*

</details>

### Q2. Which RSTP port role provides an alternate path to the root through a different switch and is discarding?
- A) Root
- B) Designated
- C) Alternate
- D) Backup

<details><summary>Answer</summary>

**Answer: C.** Alternate ports are pre-computed backups for the root port. *(Domain 2)*

</details>

### Q3. A wired PC can ping its gateway but not hosts on other subnets. Other PCs in the same VLAN work. What do you check first on the PC?
- A) The DNS suffix
- B) The configured default gateway and subnet mask
- C) The NIC duplex
- D) The browser proxy

<details><summary>Answer</summary>

**Answer: B.** Wrong gateway or mask on one host is the usual cause when neighbours work. *(Domain 1)*

</details>

### Q4. A user reports no connectivity. `show interfaces status` shows the port as `err-disabled`. What is the next step?
- A) Reload the switch
- B) Find the cause (e.g. `show interfaces status err-disabled`, logs), fix it, then shut/no shut
- C) Change the VLAN
- D) Enable DTP

<details><summary>Answer</summary>

**Answer: B.** Fix the cause first (BPDU guard, port security, etc.) before re-enabling. *(Domain 2)*

</details>

### Q5. Where should a standard IPv4 ACL normally be placed?
- A) Close to the source
- B) Close to the destination
- C) On every interface
- D) Only outbound on WAN links

<details><summary>Answer</summary>

**Answer: B.** It matches only the source, so placing it near the source over-blocks. *(Domain 4)*

</details>

### Q6. A non-root switch (short STP costs) has three uplinks. Port 1: FastEthernet (cost 19), neighbor advertises root path cost 19; Port 2: FastEthernet (cost 19), neighbor advertises root path cost 2; Port 3: TenGigabitEthernet (cost 2), neighbor advertises root path cost 23. Which port becomes the root port?
- A) None; all three forward
- B) Port 1
- C) Port 2
- D) Port 3

<details><summary>Answer</summary>

**Answer: C.** Root port = lowest total cost to the root (advertised cost + local port cost). Port 2 totals 21. *(Domain 2)*

</details>

### Q7. Rapid PVST+ for VLAN 20: SW1 priority 24596 MAC 0f34.5640.df6e; SW2 priority 32788 MAC 4043.f1fd.899b; SW3 priority 28692 MAC 6d33.31e3.bb81; SW4 priority 16404 MAC f714.f007.5595. Which switch becomes the root bridge?
- A) SW3
- B) SW4
- C) SW2
- D) SW1

<details><summary>Answer</summary>

**Answer: B.** Lowest bridge ID wins: compare priority (including the VLAN ID) first, then the lowest MAC. *(Domain 2)*

</details>

### Q8. What is the default port cost for a 1 Gbps link in short-mode STP?
- A) 1
- B) 2
- C) 4
- D) 19

<details><summary>Answer</summary>

**Answer: C.** Short costs: 10 Mbps 100, 100 Mbps 19, 1 Gbps 4, 10 Gbps 2. *(Domain 2)*

</details>

### Q9. An interface with MAC 14:2d:77:b8:f0:0a uses EUI-64 with prefix 2001:db8:1:1::/64. What is its interface ID?
- A) 142d:77ff:feb8:f00a
- B) 162d:77fe:ffb8:f00a
- C) 162d:77ff:feb8:f00a
- D) 142d:77b8:f00a:0

<details><summary>Answer</summary>

**Answer: C.** Insert ff:fe between the OUI and NIC parts, then flip the 7th bit (U/L) of the first byte. *(Domain 1)*

</details>

### Q10. A router has these routes: S* 0.0.0.0/0 via 203.0.113.1; O 10.191.0.0/16 via 10.0.12.2; O 10.191.224.0/20 via 10.0.13.3; D 10.191.227.0/24 via 10.0.14.4; S 10.191.227.64/26 via 10.0.15.5. Which next hop is used for a packet to 10.191.139.38?
- A) 203.0.113.1
- B) 10.0.13.3
- C) 10.0.12.2
- D) 10.0.14.4

<details><summary>Answer</summary>

**Answer: C.** Longest prefix match: the most specific route that contains 10.191.139.38 wins, regardless of AD. *(Domain 3)*

</details>

### Q11. What is the correct shortest form of fd12:0db8:0000:0000:0000:0000:0000:0000?
- A) fd12:db8:0:0:0:0:0:0
- B) fd12:db8::
- C) fd12:0db8::0000:0000:0000:0000
- D) fd12:db8:

<details><summary>Answer</summary>

**Answer: B.** Remove leading zeros in each hextet, then replace the longest run of all-zero hextets with :: (only once). *(Domain 1)*

</details>

### Q12. A named extended ACL has `10 permit ip any any` and `20 deny tcp any any eq 23`. Telnet still works. Why?
- A) Named ACLs are processed bottom-up
- B) The first match (entry 10) permits all traffic
- C) Telnet uses UDP
- D) The ACL needs `log`

<details><summary>Answer</summary>

**Answer: B.** Put specific entries before general ones; you can insert with a lower sequence number. *(Domain 4)*

</details>

### Q13. What does `switchport port-security mac-address sticky` do?
- A) Disables MAC learning
- B) Dynamically learns MACs and adds them to the running configuration
- C) Shuts the port
- D) Sets the maximum to 1

<details><summary>Answer</summary>

**Answer: B.** Save the config to keep sticky addresses after reload. *(Domain 4)*

</details>

### Q14. Which command shows each switch port's status, VLAN, duplex, speed and type in one table?
- A) show interfaces status
- B) show ip interface brief
- C) show running-config
- D) show version

<details><summary>Answer</summary>

**Answer: A.** `show interfaces status` is the quick access-layer overview. *(Domain 2)*

</details>

### Q15. An ACL entry is `permit ip 10.163.211.0 0.0.0.31 any`. Which source address matches it?
- A) 10.163.210.200
- B) 10.163.211.66
- C) 10.163.211.29
- D) 10.163.211.35

<details><summary>Answer</summary>

**Answer: C.** 10.163.211.0 0.0.0.31 covers 10.163.211.0-10.163.211.31 (10.163.211.0/27). *(Domain 4)*

</details>

### Q16. In `show cdp neighbors`, what does the `Port ID` column show?
- A) The local interface
- B) The neighbor's interface that connects to you
- C) The VLAN ID
- D) The TCP port

<details><summary>Answer</summary>

**Answer: B.** Local Intrfce = your port; Port ID = the remote device's port. *(Domain 2)*

</details>

### Q17. What is the severity of the syslog message `%SYS-5-CONFIG_I: ...`?
- A) 5 (notifications)
- B) 3 (errors)
- C) 6 (informational)
- D) 7 (debugging)

<details><summary>Answer</summary>

**Answer: A.** Cisco format is %FACILITY-SEVERITY-MNEMONIC; the number after the facility is the severity. *(Domain 5)*

</details>

### Q18. `show standby brief` on R1 shows `Gi0/0 10 110 P Active local 10.1.1.3 10.1.1.1`. What is the virtual IP?
- A) 10.1.1.3
- B) 10.1.1.1
- C) 10.1.1.110
- D) The IP of Gi0/0

<details><summary>Answer</summary>

**Answer: B.** Columns: interface, group, priority, preempt flag, state, active, standby, virtual IP. *(Domain 3)*

</details>

### Q19. OSPF uses auto-cost reference-bandwidth 100000 (Mbps). What is the cost of a 100 Mbps interface?
- A) 100
- B) 10000
- C) 1000
- D) 1001

<details><summary>Answer</summary>

**Answer: C.** Cost = reference / interface bandwidth = 100000/100 = 1000 (minimum 1). *(Domain 3)*

</details>

### Q20. Which LACP mode pair fails to form an EtherChannel?
- A) active / active
- B) active / passive
- C) passive / passive
- D) Both A and B

<details><summary>Answer</summary>

**Answer: C.** Two passive ports never send LACPDUs. *(Domain 2)*

</details>

### Q21. Which component is required for WPA2-Enterprise or WPA3-Enterprise authentication?
- A) A TACACS+ server
- B) An 802.1X authentication server such as RADIUS
- C) A DHCP server
- D) A syslog server

<details><summary>Answer</summary>

**Answer: B.** Enterprise mode uses 802.1X/EAP with a RADIUS server. *(Domain 1)*

</details>

### Q22. A router has these routes: S* 0.0.0.0/0 via 203.0.113.1; O 10.90.0.0/16 via 10.0.12.2; O 10.90.16.0/20 via 10.0.13.3; D 10.90.21.0/24 via 10.0.14.4; S 10.90.21.128/26 via 10.0.15.5. Which next hop is used for a packet to 10.90.21.243?
- A) 10.0.13.3
- B) 203.0.113.1
- C) 10.0.12.2
- D) 10.0.14.4

<details><summary>Answer</summary>

**Answer: D.** Longest prefix match: the most specific route that contains 10.90.21.243 wins, regardless of AD. *(Domain 3)*

</details>

### Q23. Rapid PVST+ for VLAN 20: SW1 priority 32788 MAC 3a9d.30d5.2b7d; SW2 priority 24596 MAC 7ef4.20ea.66ef; SW3 priority 20 MAC ef15.cec3.3ea3; SW4 priority 32788 MAC ebdc.1e9f.6b82. Which switch becomes the root bridge?
- A) SW1
- B) SW4
- C) SW2
- D) SW3

<details><summary>Answer</summary>

**Answer: D.** Lowest bridge ID wins: compare priority (including the VLAN ID) first, then the lowest MAC. *(Domain 2)*

</details>

### Q24. Host A is 192.168.10.30/27 with gateway 192.168.10.33. A cannot reach other subnets. What is wrong?
- A) The mask is invalid
- B) The gateway is outside Host A's subnet (192.168.10.0/27 ends at .31)
- C) The gateway must be .1
- D) Host A needs a /24

<details><summary>Answer</summary>

**Answer: B.** 192.168.10.0/27 covers .0-.31; .33 is in the next subnet, so A cannot ARP for it. *(Domain 1)*

</details>

### Q25. In the routing table entry `O 10.20.0.0/16 [110/30] via 10.0.12.2`, what is 110?
- A) The metric
- B) The administrative distance
- C) The hop count
- D) The route age

<details><summary>Answer</summary>

**Answer: B.** [AD/metric]: 110 is OSPF's administrative distance; 30 is the cost. *(Domain 3)*

</details>

### Q26. What is the size of the 802.1Q tag inserted into an Ethernet frame?
- A) 2 bytes
- B) 4 bytes
- C) 8 bytes
- D) 12 bytes

<details><summary>Answer</summary>

**Answer: B.** TPID (2 B) + TCI (2 B: PCP, DEI, 12-bit VID). *(Domain 2)*

</details>

### Q27. An ACL entry is `permit ip 10.39.32.0 0.0.7.255 any`. Which source address matches it?
- A) 10.39.40.21
- B) 10.39.34.182
- C) 10.39.31.203
- D) 10.39.48.2

<details><summary>Answer</summary>

**Answer: B.** 10.39.32.0 0.0.7.255 covers 10.39.32.0-10.39.39.255 (10.39.32.0/21). *(Domain 4)*

</details>

### Q28. What is the maximum standard segment length for 1000BASE-T?
- A) 55 m
- B) 100 m
- C) 185 m
- D) 550 m

<details><summary>Answer</summary>

**Answer: B.** All twisted-pair Ethernet standards up to 10GBASE-T on Cat6a are limited to 100 m. *(Domain 1)*

</details>

### Q29. Host A is 192.168.200.23/28. Which host is in the same subnet as Host A (same mask)?
- A) 192.168.200.38
- B) 192.168.200.3
- C) 192.168.200.55
- D) 192.168.200.21

<details><summary>Answer</summary>

**Answer: D.** Host A is in 192.168.200.16/28; only 192.168.200.21 falls inside 192.168.200.16-192.168.200.31. *(Domain 1)*

</details>

### Q30. Which feature limits broadcast traffic on an access port to 5% of bandwidth?
- A) storm-control broadcast level 5.00
- B) switchport port-security maximum 5
- C) ip dhcp snooping limit rate 5
- D) spanning-tree bpduguard

<details><summary>Answer</summary>

**Answer: A.** Storm control can drop, trap or shut down when the threshold is exceeded. *(Domain 4)*

</details>

### Q31. Which address can be assigned to a host in subnet 172.31.14.192/28?
- A) 172.31.14.200
- B) 172.31.14.208
- C) 172.31.14.192
- D) 172.31.14.207

<details><summary>Answer</summary>

**Answer: A.** 172.31.14.192/28 spans 172.31.14.192-172.31.14.207; usable hosts are 172.31.14.193-172.31.14.206. *(Domain 1)*

</details>

### Q32. Which syslog severity level number is 'debugging'?
- A) 7
- B) 6
- C) 1
- D) 0

<details><summary>Answer</summary>

**Answer: A.** 0 emergencies, 1 alerts, 2 critical, 3 errors, 4 warnings, 5 notifications, 6 informational, 7 debugging. *(Domain 5)*

</details>

### Q33. Host A is 172.26.111.210/26. Which host is in the same subnet as Host A (same mask)?
- A) 172.26.112.73
- B) 172.26.111.148
- C) 172.26.111.199
- D) 172.26.112.59

<details><summary>Answer</summary>

**Answer: C.** Host A is in 172.26.111.192/26; only 172.26.111.199 falls inside 172.26.111.192-172.26.111.255. *(Domain 1)*

</details>

### Q34. `show spanning-tree vlan 10` on SW3 shows `Gi0/2 Altn BLK 4 128.26 P2p`. What does this mean?
- A) Gi0/2 is the root port
- B) Gi0/2 is an alternate port in the discarding/blocking state
- C) Gi0/2 is err-disabled
- D) Gi0/2 is an edge port

<details><summary>Answer</summary>

**Answer: B.** Altn BLK = alternate role, blocking/discarding state. *(Domain 2)*

</details>

### Q35. A router has `logging trap critical`. Which messages are sent to the syslog server?
- A) All levels 0 through 7
- B) Levels 2 through 7
- C) Level 2 only
- D) Levels 0 through 2

<details><summary>Answer</summary>

**Answer: D.** The configured level (2) and every more severe (lower) level are sent. *(Domain 5)*

</details>

### Q36. You changed `router-id` under OSPF, but `show ip ospf` still shows the old ID. What must you do?
- A) Nothing; it updates in 30 seconds
- B) Run `clear ip ospf process` (or reload)
- C) Change the area
- D) Remove all network statements

<details><summary>Answer</summary>

**Answer: B.** The RID is chosen when the process starts. *(Domain 3)*

</details>

### Q37. www.example.com is a CNAME to web.example.net. What must exist for the name to resolve to an address?
- A) A PTR for www.example.com
- B) An A or AAAA record for web.example.net
- C) An MX for web.example.net
- D) Nothing else

<details><summary>Answer</summary>

**Answer: B.** A CNAME is an alias; the canonical name must resolve to A/AAAA. *(Domain 4)*

</details>

### Q38. Which TWO features are best practice on a port connected to a desktop PC? (Choose 2.)
- A) spanning-tree portfast
- B) spanning-tree bpduguard enable
- C) switchport mode trunk
- D) channel-group 1 mode active
- E) spanning-tree guard root

<details><summary>Answer</summary>

**Answer: A, B.** Edge ports go forwarding immediately and err-disable if a switch is connected. *(Domain 2)*

</details>

### Q39. What is the role of a transceiver such as an SFP+ module?
- A) It routes packets between VLANs
- B) It converts electrical signals to optical (or copper) signals for a specific media type and distance
- C) It stores the startup configuration
- D) It provides PoE

<details><summary>Answer</summary>

**Answer: B.** Pluggable optics define the physical media, wavelength and reach. *(Domain 1)*

</details>

### Q40. Which Ansible characteristic is true?
- A) It needs an agent on every network device
- B) It is agentless and connects over SSH or APIs from a control node
- C) It only works on Windows
- D) It requires a database server

<details><summary>Answer</summary>

**Answer: B.** Network modules use network_cli, netconf or httpapi connections. *(Domain 5)*

</details>

### Q41. Which TWO statements describe a site-to-site IPsec VPN? (Choose 2.)
- A) Gateways at each site build the tunnel; end hosts need no VPN software
- B) Tunnel mode protects the entire original packet with a new outer IP header
- C) Each user installs a VPN client
- D) It uses only TCP 443
- E) It cannot carry routing protocols

<details><summary>Answer</summary>

**Answer: A, B.** Remote-access VPNs use clients; site-to-site VPNs connect networks. *(Domain 4)*

</details>

### Q42. Which SNMP version supports authentication and encryption?
- A) v1
- B) v2c
- C) v3
- D) All versions

<details><summary>Answer</summary>

**Answer: C.** SNMPv3 authPriv uses e.g. SHA and AES. *(Domain 5)*

</details>

### Q43. NAT is configured, but `show ip nat translations` is empty and users have no internet. Which TWO items do you check first? (Choose 2.)
- A) `ip nat inside` and `ip nat outside` on the correct interfaces
- B) The ACL matches the inside source addresses
- C) The VTP domain
- D) The CDP timers
- E) The HSRP group

<details><summary>Answer</summary>

**Answer: A, B.** Traffic must enter an inside interface, match the ACL and exit an outside interface. *(Domain 4)*

</details>

### Q44. A router learns 10.112.9.0/24 from OSPF, static, EIGRP (internal). Which source is installed in the routing table (default ADs)?
- A) static
- B) OSPF
- C) All three, load-balanced
- D) EIGRP (internal)

<details><summary>Answer</summary>

**Answer: A.** Same prefix from different sources: lowest administrative distance wins. static = 1. *(Domain 3)*

</details>

### Q45. What is the broadcast address of the subnet that contains 192.168.205.200/27?
- A) 192.168.205.224
- B) 192.168.205.223
- C) 192.168.205.222
- D) 192.168.205.192

<details><summary>Answer</summary>

**Answer: B.** Network 192.168.205.192/27; the broadcast is the last address of the block, 192.168.205.223. *(Domain 1)*

</details>

### Q46. Which prompt is best for getting a usable review of a routing change from a generative AI assistant?
- A) 'Is this OK?'
- B) 'You are a senior network engineer. Review this OSPF change for risks. Do not invent commands. Answer as a table: line, risk, fix.'
- C) 'Write me a poem about OSPF.'
- D) 'Fix my network.'

<details><summary>Answer</summary>

**Answer: B.** Good prompts set a persona, give clear instructions and define the output format. *(Domain 5)*

</details>

### Q47. Which command shows the root bridge ID, root port and root cost for every VLAN on a switch?
- A) show spanning-tree root
- B) show spanning-tree blockedports
- C) show vlan brief
- D) show interfaces trunk

<details><summary>Answer</summary>

**Answer: A.** `show spanning-tree root` summarizes root information per VLAN. *(Domain 2)*

</details>

### Q48. A Cisco router must act as a SLAAC client on G0/0. Which interface command does this?
- A) ipv6 address dhcp
- B) ipv6 address autoconfig
- C) ipv6 enable
- D) ipv6 unicast-routing

<details><summary>Answer</summary>

**Answer: B.** `ipv6 address autoconfig` builds an address from received RAs. `ipv6 address dhcp` uses DHCPv6. *(Domain 1)*

</details>

### Q49. Which statement describes cloud-based network management (for example Meraki)?
- A) Devices are managed from a cloud dashboard while user traffic stays local
- B) All user traffic must traverse the cloud
- C) It needs no internet connection
- D) It requires OSPF to the cloud

<details><summary>Answer</summary>

**Answer: A.** The management plane is in the cloud; the data plane stays on site. *(Domain 5)*

</details>

### Q50. Which field in a relayed DHCP DISCOVER tells the server which subnet the client is on?
- A) ciaddr
- B) giaddr
- C) yiaddr
- D) siaddr

<details><summary>Answer</summary>

**Answer: B.** giaddr is set by the relay to its interface address in the client subnet. *(Domain 1)*

</details>

### Q51. Which pair of channel-group modes on two connected switches forms an EtherChannel?
- A) auto / passive
- B) auto / auto
- C) active / desirable
- D) desirable / auto

<details><summary>Answer</summary>

**Answer: D.** LACP: active-active or active-passive. PAgP: desirable-desirable or desirable-auto. Static: on-on. Modes from different protocols never bundle. *(Domain 2)*

</details>

### Q52. A router learns 10.241.47.0/24 from RIP, iBGP, eBGP. Which source is installed in the routing table (default ADs)?
- A) All three, load-balanced
- B) iBGP
- C) eBGP
- D) RIP

<details><summary>Answer</summary>

**Answer: C.** Same prefix from different sources: lowest administrative distance wins. eBGP = 20. *(Domain 3)*

</details>

### Q53. After enabling DHCP snooping, no client gets an address. The DHCP server is reached through uplink G1/0/48. What is missing?
- A) `ip dhcp snooping trust` on G1/0/48
- B) `spanning-tree portfast` on G1/0/48
- C) Port security on G1/0/48
- D) A static ARP entry

<details><summary>Answer</summary>

**Answer: A.** All ports are untrusted by default; also check option 82 behaviour. *(Domain 4)*

</details>

### Q54. Which command makes a switch the root bridge for VLAN 10 by lowering its priority automatically?
- A) spanning-tree vlan 10 root primary
- B) spanning-tree vlan 10 priority 65535
- C) spanning-tree root 10
- D) spanning-tree mode root

<details><summary>Answer</summary>

**Answer: A.** root primary sets 24576 or lower than the current root. *(Domain 2)*

</details>

### Q55. Which subnet mask supports 300 hosts on one subnet while wasting the fewest addresses?
- A) 255.255.255.128
- B) 255.255.252.0
- C) 255.255.254.0
- D) 255.255.255.0

<details><summary>Answer</summary>

**Answer: C.** /23 (255.255.254.0) gives 510 usable hosts; /24 gives only 254. *(Domain 1)*

</details>

### Q56. What is the network address of host 10.243.135.67/20?
- A) 10.243.143.255
- B) 10.243.144.0
- C) 10.243.112.0
- D) 10.243.128.0

<details><summary>Answer</summary>

**Answer: D.** /20 has 4096 addresses per subnet; 10.243.135.67 falls in 10.243.128.0/20 (broadcast 10.243.143.255). *(Domain 1)*

</details>

### Q57. Which TWO statements about RSTP are correct? (Choose 2.)
- A) It converges in about a second on point-to-point links using proposal/agreement
- B) It defines edge ports as part of the standard
- C) It uses five port states
- D) It requires PAgP
- E) It works only on VLAN 1

<details><summary>Answer</summary>

**Answer: A, B.** RSTP adds a handshake for fast convergence and standardizes edge ports. *(Domain 2)*

</details>

### Q58. `show etherchannel summary` shows `Po1(SU)` and both members `(P)`. What does this mean?
- A) The bundle is down
- B) Layer 2 port-channel in use, both members bundled
- C) Layer 3 port-channel, members suspended
- D) Members are stand-alone

<details><summary>Answer</summary>

**Answer: B.** S = Layer 2, U = in use, P = bundled in port-channel. *(Domain 2)*

</details>

### Q59. Which protocol is enabled by default on Cisco devices and shows the neighbor's device ID, platform, IP address and connected port?
- A) LLDP
- B) CDP
- C) SNMP
- D) DTP

<details><summary>Answer</summary>

**Answer: B.** CDP is on by default; LLDP must be enabled with `lldp run` on many IOS platforms. *(Domain 2)*

</details>

### Q60. An ACL entry is `permit ip 10.103.15.0 0.0.0.7 any`. Which source address matches it?
- A) 10.103.14.221
- B) 10.103.15.129
- C) 10.103.15.18
- D) 10.103.15.2

<details><summary>Answer</summary>

**Answer: D.** 10.103.15.0 0.0.0.7 covers 10.103.15.0-10.103.15.7 (10.103.15.0/29). *(Domain 4)*

</details>

### Q61. A switch uplink is configured `switchport mode trunk`, and the neighbor is `switchport mode access`. What happens?
- A) A trunk forms
- B) The link is inconsistent: one side tags frames, the other does not, so traffic is misdelivered or dropped
- C) EtherChannel forms
- D) Both ports err-disable immediately

<details><summary>Answer</summary>

**Answer: B.** Mode mismatches cause partial or broken connectivity; configure both ends the same. *(Domain 2)*

</details>

### Q62. Which command must be entered before AAA method lists can be configured on IOS?
- A) aaa enable
- B) aaa new-model
- C) aaa authentication enable
- D) tacacs enable

<details><summary>Answer</summary>

**Answer: B.** `aaa new-model` activates AAA. *(Domain 4)*

</details>

### Q63. Why should every device have NTP configured before you rely on syslog?
- A) NTP encrypts logs
- B) Accurate, consistent timestamps let you correlate events across devices
- C) Syslog requires NTP to start
- D) NTP increases buffer size

<details><summary>Answer</summary>

**Answer: B.** Also enable `service timestamps log datetime msec`. *(Domain 5)*

</details>

### Q64. You must copy a new IOS XE image to a router securely. Which TWO protocols are appropriate? (Choose 2.)
- A) SCP
- B) SFTP
- C) TFTP
- D) FTP
- E) Telnet

<details><summary>Answer</summary>

**Answer: A, B.** SCP and SFTP run over SSH and encrypt the transfer; TFTP and FTP do not. *(Domain 4)*

</details>

### Q65. A non-root switch (short STP costs) has three uplinks. Port 1: GigabitEthernet (cost 4), neighbor advertises root path cost 0; Port 2: GigabitEthernet (cost 4), neighbor advertises root path cost 19; Port 3: TenGigabitEthernet (cost 2), neighbor advertises root path cost 0. Which port becomes the root port?
- A) None; all three forward
- B) Port 1
- C) Port 2
- D) Port 3

<details><summary>Answer</summary>

**Answer: D.** Root port = lowest total cost to the root (advertised cost + local port cost). Port 3 totals 2. *(Domain 2)*

</details>

### Q66. How many IPv4 ACLs can be applied to one interface?
- A) One per interface
- B) One per direction (in and out) per interface
- C) Unlimited
- D) Two per VLAN

<details><summary>Answer</summary>

**Answer: B.** One ACL per interface, per direction, per protocol. *(Domain 4)*

</details>

### Q67. What happens when a port with BPDU guard enabled receives a BPDU?
- A) The BPDU is ignored
- B) The port goes to err-disabled
- C) The port becomes root
- D) The port moves to VLAN 1

<details><summary>Answer</summary>

**Answer: B.** BPDU guard shuts the port to stop rogue switches and loops. *(Domain 2)*

</details>

### Q68. The primary default route is learned by eBGP. Which administrative distance makes a backup static default route float (used only if the eBGP route is lost)?
- A) 19
- B) 20
- C) 1
- D) 200

<details><summary>Answer</summary>

**Answer: D.** The static route needs an AD higher than eBGP (20); equal AD would compete and a lower AD would win. *(Domain 3)*

</details>

### Q69. Which command creates a local user with the strongest password hashing available on modern IOS XE?
- A) username admin password Cisco123
- B) username admin secret 5 Cisco123
- C) username admin privilege 15 algorithm-type scrypt secret Str0ng!Pass
- D) enable password Cisco123

<details><summary>Answer</summary>

**Answer: C.** scrypt (type 9) is a strong hash; `password` stores reversible or clear text. *(Domain 4)*

</details>

### Q70. Which wildcard mask matches the same addresses as subnet mask 255.255.255.0 in an ACL?
- A) 0.0.0.127
- B) 0.0.0.255
- C) 0.0.1.255
- D) 255.255.255.0

<details><summary>Answer</summary>

**Answer: B.** Wildcard = 255.255.255.255 − mask = 0.0.0.255. *(Domain 4)*

</details>

### Q71. Which TWO conditions must be true for two routers to form an OSPFv2 adjacency on an Ethernet link? (Choose 2.)
- A) Same area ID
- B) Same hello and dead intervals
- C) Same process ID
- D) Same router ID
- E) Same interface bandwidth

<details><summary>Answer</summary>

**Answer: A, B.** Area, timers, subnet, authentication and stub flags must match; process IDs are local. *(Domain 3)*

</details>

### Q72. On a broadcast segment, router A has priority 1 and RID 3.3.3.3, router B priority 1 and RID 1.1.1.1, router C priority 0 and RID 9.9.9.9. All start at the same time. Which is DR?
- A) Router A
- B) Router B
- C) Router C
- D) None

<details><summary>Answer</summary>

**Answer: A.** Priority 0 never becomes DR. Among priority-1 routers, the highest RID (3.3.3.3) wins. *(Domain 3)*

</details>

### Q73. In the 2.4 GHz band, which channel set avoids overlap between neighbouring APs?
- A) 1, 4, 8
- B) 1, 6, 11
- C) 2, 7, 12
- D) 3, 6, 9

<details><summary>Answer</summary>

**Answer: B.** Only channels 1, 6 and 11 do not overlap (in most regulatory domains). *(Domain 1)*

</details>

### Q74. Which static route is a host route?
- A) ip route 10.1.1.0 255.255.255.0 10.0.0.2
- B) ip route 10.1.1.10 255.255.255.255 10.0.0.2
- C) ip route 0.0.0.0 0.0.0.0 10.0.0.2
- D) ip route 10.0.0.0 255.0.0.0 Null0

<details><summary>Answer</summary>

**Answer: B.** A /32 mask matches one host. *(Domain 3)*

</details>

### Q75. A router has these routes: S* 0.0.0.0/0 via 203.0.113.1; O 10.77.0.0/16 via 10.0.12.2; O 10.77.128.0/20 via 10.0.13.3; D 10.77.139.0/24 via 10.0.14.4; S 10.77.139.0/26 via 10.0.15.5. Which next hop is used for a packet to 172.16.159.130?
- A) 10.0.13.3
- B) 10.0.12.2
- C) 203.0.113.1
- D) 10.0.14.4

<details><summary>Answer</summary>

**Answer: C.** Longest prefix match: the most specific route that contains 172.16.159.130 wins, regardless of AD. *(Domain 3)*

</details>

### Q76. A lightweight AP in local mode connects to an access switch. How should the port be configured?
- A) Trunk carrying all client VLANs
- B) Access port in the AP management VLAN
- C) Routed port
- D) EtherChannel

<details><summary>Answer</summary>

**Answer: B.** Local-mode APs tunnel client data to the WLC over CAPWAP, so they need only one VLAN. *(Domain 2)*

</details>

### Q77. A router has these routes: S* 0.0.0.0/0 via 203.0.113.1; O 10.124.0.0/16 via 10.0.12.2; O 10.124.176.0/20 via 10.0.13.3; D 10.124.181.0/24 via 10.0.14.4; S 10.124.181.128/26 via 10.0.15.5. Which next hop is used for a packet to 10.124.186.28?
- A) 10.0.13.3
- B) 203.0.113.1
- C) 10.0.12.2
- D) 10.0.14.4

<details><summary>Answer</summary>

**Answer: A.** Longest prefix match: the most specific route that contains 10.124.186.28 wins, regardless of AD. *(Domain 3)*

</details>

### Q78. Which Ansible option shows what would change without applying it?
- A) --check (with --diff)
- B) --force
- C) --verbose only
- D) --limit

<details><summary>Answer</summary>

**Answer: A.** Check mode is a dry run; --diff prints the differences. *(Domain 5)*

</details>

### Q79. What best describes agentic AI in network operations?
- A) A static script that runs one show command
- B) An AI system that plans multi-step tasks and calls tools (show commands, telemetry queries, ticket APIs) to reach a goal
- C) A replacement for routing protocols
- D) A new YANG model

<details><summary>Answer</summary>

**Answer: B.** Agents reason and act through tools; guardrails and approvals keep them safe. *(Domain 5)*

</details>

### Q80. What does `passive-interface g0/2` under OSPF do?
- A) Removes the network from OSPF
- B) Advertises the interface's network but stops sending hellos on it, so no neighbors form there
- C) Makes the router DR
- D) Disables the interface

<details><summary>Answer</summary>

**Answer: B.** Use it on LAN and loopback interfaces with no routers. *(Domain 3)*

</details>

### Q81. Mail to example.com is delivered to the wrong server. Which record do you check?
- A) CNAME
- B) MX
- C) NS
- D) PTR

<details><summary>Answer</summary>

**Answer: B.** MX records list mail servers and preferences. *(Domain 4)*

</details>

### Q82. Which statement correctly compares containers and virtual machines?
- A) Containers each include a full guest operating system
- B) Containers share the host kernel and package only the app and its dependencies; VMs include a full guest OS
- C) VMs start faster than containers
- D) Containers require a Type 2 hypervisor

<details><summary>Answer</summary>

**Answer: B.** Containers isolate processes on a shared kernel, so they are lighter and start faster than VMs. *(Domain 1)*

</details>

### Q83. Which address can be assigned to a host in subnet 172.20.51.216/29?
- A) 172.20.51.216
- B) 172.20.51.219
- C) 172.20.51.223
- D) 172.20.51.224

<details><summary>Answer</summary>

**Answer: B.** 172.20.51.216/29 spans 172.20.51.216-172.20.51.223; usable hosts are 172.20.51.217-172.20.51.222. *(Domain 1)*

</details>

### Q84. How many usable host addresses does a /19 IPv4 subnet provide?
- A) 8,192
- B) 8,190
- C) 4,094
- D) 16,382

<details><summary>Answer</summary>

**Answer: B.** 2^13 − 2 = 8,190 (network and broadcast are not usable). *(Domain 1)*

</details>

### Q85. What is the network address of host 10.46.193.202/18?
- A) 10.46.192.0
- B) 10.47.0.0
- C) 10.46.128.0
- D) 10.46.255.255

<details><summary>Answer</summary>

**Answer: A.** /18 has 16384 addresses per subnet; 10.46.193.202 falls in 10.46.192.0/18 (broadcast 10.46.255.255). *(Domain 1)*

</details>

### Q86. Which virtual MAC format does VRRP use?
- A) 0000.0c07.acXX
- B) 0000.0c9f.fXXX
- C) 0000.5e00.01XX
- D) 0100.5e00.00XX

<details><summary>Answer</summary>

**Answer: C.** XX is the VRRP group number in hex. *(Domain 3)*

</details>

### Q87. Which tool on a Cisco router confirms the exact route used for a specific destination?
- A) show ip route 10.2.3.4
- B) show ip interface brief
- C) show arp
- D) show cdp neighbors

<details><summary>Answer</summary>

**Answer: A.** `show ip route <address>` performs the lookup and prints the matching entry. *(Domain 3)*

</details>

### Q88. In Cisco NAT terminology, what is the inside local address?
- A) The public address representing the inside host
- B) The private address actually configured on the inside host
- C) The outside server address
- D) The NAT pool's first address

<details><summary>Answer</summary>

**Answer: B.** Inside local = real private address; inside global = translated address. *(Domain 4)*

</details>

### Q89. Which command adds VLAN 50 to an existing trunk without removing the other allowed VLANs?
- A) switchport trunk allowed vlan 50
- B) switchport trunk allowed vlan add 50
- C) switchport trunk vlan 50
- D) switchport access vlan 50

<details><summary>Answer</summary>

**Answer: B.** Without `add`, the command replaces the whole list and can cut off other VLANs. *(Domain 2)*

</details>

### Q90. Clients in VLAN 40 on a Layer 3 switch receive no DHCP address. The server is 10.99.0.10 in another VLAN. Which command fixes this?
- A) `ip helper-address 10.99.0.10` under interface vlan 40
- B) `ip dhcp relay` globally
- C) `ip default-gateway 10.99.0.10`
- D) `ip dhcp snooping trust` on the SVI

<details><summary>Answer</summary>

**Answer: A.** The relay must be on the SVI that receives the client broadcasts. *(Domain 1)*

</details>

### Q91. Which command configures an IPv4 default static route to next hop 203.0.113.1?
- A) ip route 0.0.0.0 255.255.255.255 203.0.113.1
- B) ip route 0.0.0.0 0.0.0.0 203.0.113.1
- C) ip default-network 203.0.113.1
- D) ip route default 203.0.113.1

<details><summary>Answer</summary>

**Answer: B.** Network 0.0.0.0 with mask 0.0.0.0 matches everything. *(Domain 3)*

</details>

### Q92. Which wildcard mask matches the same addresses as subnet mask 255.255.255.240 in an ACL?
- A) 255.255.255.240
- B) 0.0.0.7
- C) 0.0.0.31
- D) 0.0.0.15

<details><summary>Answer</summary>

**Answer: D.** Wildcard = 255.255.255.255 − mask = 0.0.0.15. *(Domain 4)*

</details>

### Q93. What is the main advantage of a Type 1 (bare-metal) hypervisor over a Type 2 hypervisor?
- A) It runs as an app on a desktop OS
- B) It runs directly on the hardware with less overhead, suitable for data centers
- C) It cannot run Linux guests
- D) It needs no CPU virtualization support

<details><summary>Answer</summary>

**Answer: B.** Type 1 hypervisors (ESXi, KVM, Hyper-V) run on the hardware; Type 2 (VirtualBox) runs on a host OS. *(Domain 1)*

</details>

### Q94. A switch port shows a steadily rising CRC error count and input errors, but no late collisions. Both ends are set to auto. What is the most likely cause?
- A) A duplex mismatch
- B) A damaged cable, dirty fiber connector or failing transceiver
- C) An STP loop
- D) A wrong access VLAN

<details><summary>Answer</summary>

**Answer: B.** CRC/input errors with matching autonegotiation point to the physical layer: cabling, connectors, optics or EMI. *(Domain 1)*

</details>

### Q95. OSPF uses auto-cost reference-bandwidth 100 (Mbps). What is the cost of a 10 Mbps interface?
- A) 11
- B) 1
- C) 10
- D) 100

<details><summary>Answer</summary>

**Answer: C.** Cost = reference / interface bandwidth = 100/10 = 10 (minimum 1). *(Domain 3)*

</details>

### Q96. OSPFv3 on an IPv6-only router fails to start. No IPv4 addresses exist. What is missing?
- A) An IPv6 global address
- B) A manually configured 32-bit router ID
- C) A DR
- D) Area 1

<details><summary>Answer</summary>

**Answer: B.** OSPFv3 still needs an IPv4-format router ID. *(Domain 3)*

</details>

### Q97. A host can ping its default gateway but traceroute to a remote server stops at the gateway. What does this indicate?
- A) A Layer 1 problem on the host
- B) A routing or filtering problem at or beyond the gateway
- C) A duplex mismatch
- D) A wrong host VLAN

<details><summary>Answer</summary>

**Answer: B.** Layer 2/3 to the gateway works; the next hop or return path fails. *(Domain 2)*

</details>

### Q98. What is the broadcast address of the subnet that contains 172.22.190.28/19?
- A) 172.22.192.0
- B) 172.22.160.0
- C) 172.22.191.254
- D) 172.22.191.255

<details><summary>Answer</summary>

**Answer: D.** Network 172.22.160.0/19; the broadcast is the last address of the block, 172.22.191.255. *(Domain 1)*

</details>

### Q99. A client reports an RSSI of −82 dBm and an SNR of 8 dB. What is the likely user experience?
- A) Excellent
- B) Good enough for voice
- C) Poor: low data rates, retries and disconnects
- D) No effect

<details><summary>Answer</summary>

**Answer: C.** Good service usually needs RSSI ≥ −67 dBm and SNR ≥ 25 dB. *(Domain 1)*

</details>

### Q100. Which wildcard mask matches the same addresses as subnet mask 255.255.255.252 in an ACL?
- A) 0.0.0.3
- B) 0.0.0.7
- C) 0.0.0.1
- D) 255.255.255.252

<details><summary>Answer</summary>

**Answer: A.** Wildcard = 255.255.255.255 − mask = 0.0.0.3. *(Domain 4)*

</details>
