# CCNA 200-301 v2.0 — Practice Exam 3

**Format:** 100 questions · 120 minutes · target score 85% (the real passing score is not published; aim high).
Original questions written for this repo, not exam dumps. Simulations are in [../labs/](../labs/README.md).

Run interactively: `python3 tools/quiz_runner.py cert/ccna-200-301/practice-exams/exam-3.md --shuffle`

| Domain | Questions |
|---|---|
| 1.0 Network Infrastructure and Connectivity | 25 |
| 2.0 Switching and Network Access | 25 |
| 3.0 IP Routing | 20 |
| 4.0 Network Services and Security | 20 |
| 5.0 AI, and Network Operations and Management | 10 |

Rules: no notes, one sitting, mark questions to revisit, never leave a question blank.

### Q1. The primary default route is learned by OSPF. Which administrative distance makes a backup static default route float (used only if the OSPF route is lost)?
- A) 110
- B) 109
- C) 1
- D) 130

<details><summary>Answer</summary>

**Answer: D.** The static route needs an AD higher than OSPF (110); equal AD would compete and a lower AD would win. *(Domain 3)*

</details>

### Q2. An IPv6 static route uses a link-local next hop fe80::2. What else must the command include?
- A) An administrative distance
- B) The outgoing interface
- C) A tag
- D) The keyword permanent

<details><summary>Answer</summary>

**Answer: B.** Link-local addresses are only unique per link: `ipv6 route ::/0 g0/1 fe80::2`. *(Domain 3)*

</details>

### Q3. A router has these routes: S* 0.0.0.0/0 via 203.0.113.1; O 10.120.0.0/16 via 10.0.12.2; O 10.120.208.0/20 via 10.0.13.3; D 10.120.217.0/24 via 10.0.14.4; S 10.120.217.0/26 via 10.0.15.5. Which next hop is used for a packet to 172.28.168.241?
- A) 10.0.12.2
- B) 10.0.14.4
- C) 10.0.13.3
- D) 203.0.113.1

<details><summary>Answer</summary>

**Answer: D.** Longest prefix match: the most specific route that contains 172.28.168.241 wins, regardless of AD. *(Domain 3)*

</details>

### Q4. Which TWO problems can cause DHCP clients to receive addresses from the wrong pool? (Choose 2.)
- A) The helper address is configured on the wrong interface
- B) The pool network statement does not match the giaddr subnet
- C) The client NIC speed
- D) The DNS server option
- E) Spanning-tree PortFast

<details><summary>Answer</summary>

**Answer: A, B.** The server matches the giaddr to a pool network; a wrong relay interface sends the wrong giaddr. *(Domain 1)*

</details>

### Q5. In SNMP, what is a MIB?
- A) A transport protocol
- B) A hierarchical database of manageable objects addressed by OIDs
- C) A type of trap
- D) An encryption key

<details><summary>Answer</summary>

**Answer: B.** For example IF-MIB ifHCInOctets = 1.3.6.1.2.1.31.1.1.1.6. *(Domain 5)*

</details>

### Q6. An ACL entry is `permit ip 10.37.40.0 0.0.0.15 any`. Which source address matches it?
- A) 10.37.40.10
- B) 10.37.40.34
- C) 10.37.40.128
- D) 10.37.39.222

<details><summary>Answer</summary>

**Answer: A.** 10.37.40.0 0.0.0.15 covers 10.37.40.0-10.37.40.15 (10.37.40.0/28). *(Domain 4)*

</details>

### Q7. Which TWO statements describe idempotent Ansible tasks? (Choose 2.)
- A) Running the playbook again makes no changes if the device already matches
- B) The task result reports `changed=0` on a second run
- C) They always reboot the device
- D) They cannot be run in check mode
- E) They require manual approval each time

<details><summary>Answer</summary>

**Answer: A, B.** Resource modules compare desired and current state. *(Domain 5)*

</details>

### Q8. Which feature prevents an alternate or root port from moving to forwarding when BPDUs stop arriving because of a unidirectional link?
- A) Loop guard
- B) Root guard
- C) BPDU guard
- D) PortFast

<details><summary>Answer</summary>

**Answer: A.** Loop guard moves the port to loop-inconsistent instead of forwarding. *(Domain 2)*

</details>

### Q9. Which wildcard mask matches the same addresses as subnet mask 255.255.255.248 in an ACL?
- A) 0.0.0.3
- B) 0.0.0.7
- C) 255.255.255.248
- D) 0.0.0.15

<details><summary>Answer</summary>

**Answer: B.** Wildcard = 255.255.255.255 − mask = 0.0.0.7. *(Domain 4)*

</details>

### Q10. An SVI for VLAN 30 shows `Vlan30 is down, line protocol is down`. VLAN 30 exists. What is a likely reason?
- A) No access or trunk port in VLAN 30 is up (or the SVI is shut down)
- B) OSPF is not configured
- C) The IP address is wrong
- D) DHCP is missing

<details><summary>Answer</summary>

**Answer: A.** An SVI comes up only if it is not shut and at least one port carrying that VLAN is up/forwarding. *(Domain 2)*

</details>

### Q11. Only one inside host at a time can reach the internet. NAT uses a pool with a single public address and no `overload`. What fixes it?
- A) Add `overload` to the NAT statement
- B) Remove `ip nat outside`
- C) Add a default route on the hosts
- D) Enable PortFast

<details><summary>Answer</summary>

**Answer: A.** Without overload, each inside host needs its own public address. *(Domain 4)*

</details>

### Q12. OSPF uses auto-cost reference-bandwidth 10000 (Mbps). What is the cost of a 1000 Mbps interface?
- A) 10
- B) 100
- C) 1
- D) 11

<details><summary>Answer</summary>

**Answer: A.** Cost = reference / interface bandwidth = 10000/1000 = 10 (minimum 1). *(Domain 3)*

</details>

### Q13. Which RADIUS ports are standard for authentication and accounting?
- A) UDP 1812 and 1813
- B) TCP 49 and 50
- C) UDP 161 and 162
- D) TCP 1645 and 1646

<details><summary>Answer</summary>

**Answer: A.** 1645/1646 are legacy RADIUS ports, still seen on older devices. *(Domain 4)*

</details>

### Q14. Which command copies the running configuration to an SFTP server?
- A) copy running-config sftp://admin@10.99.0.20/r1.cfg
- B) copy sftp running-config
- C) write sftp
- D) archive running-config

<details><summary>Answer</summary>

**Answer: A.** IOS `copy` supports sftp:// and scp:// URLs. *(Domain 4)*

</details>

### Q15. What is the network address of host 10.32.231.111/26?
- A) 10.32.231.64
- B) 10.32.231.127
- C) 10.32.231.128
- D) 10.32.231.0

<details><summary>Answer</summary>

**Answer: A.** /26 has 64 addresses per subnet; 10.32.231.111 falls in 10.32.231.64/26 (broadcast 10.32.231.127). *(Domain 1)*

</details>

### Q16. Which syslog severity is more critical: level 2 or level 6?
- A) Level 6
- B) Level 2
- C) They are equal
- D) It depends on the facility

<details><summary>Answer</summary>

**Answer: B.** Lower numbers are more severe (2 critical, 6 informational). *(Domain 5)*

</details>

### Q17. Host A is 10.137.207.234/26. Which host is in the same subnet as Host A (same mask)?
- A) 10.137.207.190
- B) 10.137.207.201
- C) 10.137.208.55
- D) 10.137.208.81

<details><summary>Answer</summary>

**Answer: B.** Host A is in 10.137.207.192/26; only 10.137.207.201 falls inside 10.137.207.192-10.137.207.255. *(Domain 1)*

</details>

### Q18. Which access port configuration is correct for a Cisco IP phone with a PC connected behind it?
- A) switchport mode trunk with all VLANs
- B) switchport mode access, switchport access vlan 10, switchport voice vlan 150
- C) switchport mode access with only voice vlan 150
- D) no switchport

<details><summary>Answer</summary>

**Answer: B.** Data VLAN untagged, voice VLAN tagged by the phone (learned via CDP/LLDP-MED). *(Domain 2)*

</details>

### Q19. Which DNS record type maps a hostname to an IPv6 address?
- A) A
- B) AAAA
- C) PTR
- D) MX

<details><summary>Answer</summary>

**Answer: B.** A = IPv4, AAAA = IPv6. *(Domain 4)*

</details>

### Q20. A non-root switch (short STP costs) has three uplinks. Port 1: FastEthernet (cost 19), neighbor advertises root path cost 0; Port 2: GigabitEthernet (cost 4), neighbor advertises root path cost 19; Port 3: FastEthernet (cost 19), neighbor advertises root path cost 2. Which port becomes the root port?
- A) Port 3
- B) None; all three forward
- C) Port 2
- D) Port 1

<details><summary>Answer</summary>

**Answer: D.** Root port = lowest total cost to the root (advertised cost + local port cost). Port 1 totals 19. *(Domain 2)*

</details>

### Q21. An ACL entry is `permit ip 10.78.205.0 0.0.0.15 any`. Which source address matches it?
- A) 10.78.205.3
- B) 10.78.204.155
- C) 10.78.205.34
- D) 10.78.205.171

<details><summary>Answer</summary>

**Answer: A.** 10.78.205.0 0.0.0.15 covers 10.78.205.0-10.78.205.15 (10.78.205.0/28). *(Domain 4)*

</details>

### Q22. Which RF characteristic describes signal loss as a wave passes through walls and furniture?
- A) Reflection
- B) Absorption / attenuation
- C) Diffraction
- D) Modulation

<details><summary>Answer</summary>

**Answer: B.** Materials absorb RF energy and weaken the signal; water and concrete absorb a lot. *(Domain 1)*

</details>

### Q23. Which subnet mask supports 900 hosts on one subnet while wasting the fewest addresses?
- A) 255.255.255.0
- B) 255.255.252.0
- C) 255.255.248.0
- D) 255.255.254.0

<details><summary>Answer</summary>

**Answer: B.** /22 (255.255.252.0) gives 1022 usable hosts; /23 gives only 510. *(Domain 1)*

</details>

### Q24. What is the broadcast address of the subnet that contains 10.171.33.122/24?
- A) 10.171.33.0
- B) 10.171.33.255
- C) 10.171.33.254
- D) 10.171.34.0

<details><summary>Answer</summary>

**Answer: B.** Network 10.171.33.0/24; the broadcast is the last address of the block, 10.171.33.255. *(Domain 1)*

</details>

### Q25. In the message `*Mar 3 10:41:07: %LINEPROTO-5-UPDOWN: Line protocol on Interface Gi0/1, changed state to down`, what is LINEPROTO?
- A) Severity
- B) Facility
- C) Mnemonic
- D) Hostname

<details><summary>Answer</summary>

**Answer: B.** Format: %FACILITY-SEVERITY-MNEMONIC. *(Domain 5)*

</details>

### Q26. A laptop connects to Wi-Fi and authenticates successfully but receives 169.254.x.x. Other WLANs work. What is the most likely cause?
- A) Wrong PSK
- B) The WLAN's VLAN is missing from the WLC/AP trunk or has no DHCP relay
- C) The AP is in monitor mode
- D) The SSID is hidden

<details><summary>Answer</summary>

**Answer: B.** Authentication succeeded, so the problem is in the wired path for DHCP. *(Domain 1)*

</details>

### Q27. A non-root switch (short STP costs) has three uplinks. Port 1: GigabitEthernet (cost 4), neighbor advertises root path cost 4; Port 2: GigabitEthernet (cost 4), neighbor advertises root path cost 8; Port 3: FastEthernet (cost 19), neighbor advertises root path cost 0. Which port becomes the root port?
- A) Port 1
- B) Port 3
- C) Port 2
- D) None; all three forward

<details><summary>Answer</summary>

**Answer: A.** Root port = lowest total cost to the root (advertised cost + local port cost). Port 1 totals 8. *(Domain 2)*

</details>

### Q28. In what order are DHCPv4 messages exchanged when a client gets a new lease?
- A) Request, Offer, Discover, Acknowledge
- B) Discover, Offer, Request, Acknowledge
- C) Discover, Request, Offer, Acknowledge
- D) Offer, Request, Acknowledge, Discover

<details><summary>Answer</summary>

**Answer: B.** DORA. *(Domain 1)*

</details>

### Q29. Which protocol is typically used between a switch (authenticator) and the authentication server in 802.1X?
- A) TACACS+
- B) RADIUS
- C) LDAP over UDP
- D) SNMP

<details><summary>Answer</summary>

**Answer: B.** RADIUS carries EAP between the authenticator and server. *(Domain 4)*

</details>

### Q30. A router has these routes: S* 0.0.0.0/0 via 203.0.113.1; O 10.52.0.0/16 via 10.0.12.2; O 10.52.176.0/20 via 10.0.13.3; D 10.52.178.0/24 via 10.0.14.4; S 10.52.178.64/26 via 10.0.15.5. Which next hop is used for a packet to 10.52.178.11?
- A) 10.0.12.2
- B) 10.0.13.3
- C) 10.0.14.4
- D) 203.0.113.1

<details><summary>Answer</summary>

**Answer: C.** Longest prefix match: the most specific route that contains 10.52.178.11 wins, regardless of AD. *(Domain 3)*

</details>

### Q31. Which command applies ACL MGMT to restrict SSH access to the router itself?
- A) ip access-group MGMT in on every interface
- B) access-class MGMT in under line vty 0 15
- C) ip ssh access-list MGMT
- D) login access MGMT

<details><summary>Answer</summary>

**Answer: B.** access-class filters VTY sessions. *(Domain 4)*

</details>

### Q32. Which fiber type has a core of about 9 microns and is used for links of 10 km or more?
- A) OM3 multimode
- B) OM4 multimode
- C) Single-mode (OS2)
- D) Cat6a

<details><summary>Answer</summary>

**Answer: C.** Single-mode fiber's small core allows one light path and long distances with laser optics. *(Domain 1)*

</details>

### Q33. Which DTP-related command stops a trunk port from sending DTP frames?
- A) switchport nonegotiate
- B) no cdp enable
- C) switchport mode dynamic auto
- D) spanning-tree bpdufilter enable

<details><summary>Answer</summary>

**Answer: A.** Use with a static `switchport mode trunk`. *(Domain 2)*

</details>

### Q34. Which cabling issue often causes intermittent errors that worsen when a cable is moved?
- A) A crossover cable
- B) A damaged or poorly terminated connector
- C) A plenum jacket
- D) Auto-MDIX

<details><summary>Answer</summary>

**Answer: B.** Bad terminations and bent cables produce intermittent physical errors. *(Domain 1)*

</details>

### Q35. Two switches are connected. SW1's port is `dynamic auto` and SW2's port is `dynamic auto`. What is the result?
- A) Trunk
- B) Access port
- C) Err-disabled
- D) EtherChannel

<details><summary>Answer</summary>

**Answer: B.** Both sides wait passively, so no trunk forms. Hard-code trunk mode in production. *(Domain 2)*

</details>

### Q36. An IoT sensor network must not reach the corporate user VLAN. What is the simplest design at the access layer?
- A) Put IoT devices in their own VLAN and filter between VLANs at the L3 boundary
- B) Put them in VLAN 1
- C) Use a trunk to each sensor
- D) Disable STP

<details><summary>Answer</summary>

**Answer: A.** Segmentation by VLAN plus ACLs/firewall rules at the gateway. *(Domain 2)*

</details>

### Q37. Which bridge becomes the STP root?
- A) The bridge with the highest priority
- B) The bridge with the lowest bridge ID (priority, then MAC)
- C) The bridge with the most ports
- D) The bridge with the highest MAC

<details><summary>Answer</summary>

**Answer: B.** Lowest bridge ID wins. *(Domain 2)*

</details>

### Q38. Two OSPF neighbors are stuck in EXSTART/EXCHANGE. What is the most common cause?
- A) Area mismatch
- B) MTU mismatch
- C) Hello timer mismatch
- D) Different process IDs

<details><summary>Answer</summary>

**Answer: B.** MTU is checked in DBD packets; area and timer mismatches stop neighbors before 2-Way. *(Domain 3)*

</details>

### Q39. A router shows `Gateway of last resort is not set`. What happens to packets for destinations not in the table?
- A) They are flooded
- B) They are dropped (ICMP unreachable may be sent)
- C) They go to the first route
- D) They are sent to the DHCP server

<details><summary>Answer</summary>

**Answer: B.** Without a default route, unmatched packets are dropped. *(Domain 3)*

</details>

### Q40. Which wildcard mask matches the same addresses as subnet mask 255.255.255.248 in an ACL?
- A) 0.0.0.15
- B) 255.255.255.248
- C) 0.0.0.7
- D) 0.0.0.3

<details><summary>Answer</summary>

**Answer: C.** Wildcard = 255.255.255.255 − mask = 0.0.0.7. *(Domain 4)*

</details>

### Q41. Which TWO routes would a router use for ECMP load sharing? (Choose 2.)
- A) Two OSPF routes to the same prefix with equal cost
- B) An OSPF and an EIGRP route to the same prefix
- C) Two routes with different prefix lengths
- D) Two static routes to the same prefix with the same AD
- E) A static and a connected route

<details><summary>Answer</summary>

**Answer: A, D.** Equal-cost paths from the same source with the same prefix and AD are installed together. *(Domain 3)*

</details>

### Q42. A router has these routes: S* 0.0.0.0/0 via 203.0.113.1; O 10.108.0.0/16 via 10.0.12.2; O 10.108.160.0/20 via 10.0.13.3; D 10.108.161.0/24 via 10.0.14.4; S 10.108.161.0/26 via 10.0.15.5. Which next hop is used for a packet to 10.108.161.139?
- A) 10.0.13.3
- B) 10.0.14.4
- C) 10.0.12.2
- D) 203.0.113.1

<details><summary>Answer</summary>

**Answer: B.** Longest prefix match: the most specific route that contains 10.108.161.139 wins, regardless of AD. *(Domain 3)*

</details>

### Q43. A router has these routes: S* 0.0.0.0/0 via 203.0.113.1; O 10.118.0.0/16 via 10.0.12.2; O 10.118.208.0/20 via 10.0.13.3; D 10.118.210.0/24 via 10.0.14.4; S 10.118.210.192/26 via 10.0.15.5. Which next hop is used for a packet to 172.28.253.103?
- A) 10.0.13.3
- B) 10.0.12.2
- C) 203.0.113.1
- D) 10.0.14.4

<details><summary>Answer</summary>

**Answer: C.** Longest prefix match: the most specific route that contains 172.28.253.103 wins, regardless of AD. *(Domain 3)*

</details>

### Q44. How many usable host addresses does a /23 IPv4 subnet provide?
- A) 512
- B) 510
- C) 1,022
- D) 254

<details><summary>Answer</summary>

**Answer: B.** 2^9 − 2 = 510 (network and broadcast are not usable). *(Domain 1)*

</details>

### Q45. What is the network address of host 192.168.184.57/25?
- A) 192.168.184.0
- B) 192.168.184.128
- C) 192.168.184.127
- D) 192.168.183.128

<details><summary>Answer</summary>

**Answer: A.** /25 has 128 addresses per subnet; 192.168.184.57 falls in 192.168.184.0/25 (broadcast 192.168.184.127). *(Domain 1)*

</details>

### Q46. What is the purpose of `default-information originate` under OSPF?
- A) Learns a default route from DHCP
- B) Advertises the router's default route into OSPF as an external route
- C) Sets the router ID
- D) Summarizes all routes

<details><summary>Answer</summary>

**Answer: B.** The ASBR must have a default route itself (or use `always`). *(Domain 3)*

</details>

### Q47. Which command shows the addresses a Cisco DHCP server has leased?
- A) show ip dhcp pool
- B) show ip dhcp binding
- C) show dhcp lease
- D) show ip interface brief

<details><summary>Answer</summary>

**Answer: B.** `show ip dhcp binding` lists IP, client ID/MAC and expiry. *(Domain 1)*

</details>

### Q48. Which pair of channel-group modes on two connected switches forms an EtherChannel?
- A) auto / auto
- B) active / passive
- C) on / active
- D) active / desirable

<details><summary>Answer</summary>

**Answer: B.** LACP: active-active or active-passive. PAgP: desirable-desirable or desirable-auto. Static: on-on. Modes from different protocols never bundle. *(Domain 2)*

</details>

### Q49. Which port security violation mode drops traffic from unknown MACs, increments the counter and sends a syslog message without shutting the port?
- A) protect
- B) restrict
- C) shutdown
- D) sticky

<details><summary>Answer</summary>

**Answer: B.** protect is silent; shutdown err-disables (default). *(Domain 4)*

</details>

### Q50. Which interface type gives a multilayer switch an IP address in a VLAN for inter-VLAN routing and management?
- A) Loopback
- B) SVI (interface vlan)
- C) Tunnel
- D) Null0

<details><summary>Answer</summary>

**Answer: B.** Switch virtual interfaces are the Layer 3 gateways for VLANs. *(Domain 2)*

</details>

### Q51. A router learns 10.95.165.0/24 from OSPF, RIP, iBGP. Which source is installed in the routing table (default ADs)?
- A) OSPF
- B) All three, load-balanced
- C) RIP
- D) iBGP

<details><summary>Answer</summary>

**Answer: A.** Same prefix from different sources: lowest administrative distance wins. OSPF = 110. *(Domain 3)*

</details>

### Q52. R1 (HSRP priority 100) is active. R2 has priority 120 and `standby 1 preempt`. What happens when R2 boots after R1?
- A) R1 stays active forever
- B) R2 takes over as active because it has a higher priority and preempt enabled
- C) Both become active
- D) R2 becomes listen only

<details><summary>Answer</summary>

**Answer: B.** Preemption lets the higher-priority router take the active role. *(Domain 3)*

</details>

### Q53. Which syslog severity level number is 'alerts'?
- A) 3
- B) 1
- C) 2
- D) 0

<details><summary>Answer</summary>

**Answer: B.** 0 emergencies, 1 alerts, 2 critical, 3 errors, 4 warnings, 5 notifications, 6 informational, 7 debugging. *(Domain 5)*

</details>

### Q54. Which command enables SSH version 2 only on a router that already has a hostname, domain name and RSA keys?
- A) ip ssh version 2
- B) ssh v2 enable
- C) transport ssh 2
- D) crypto ssh 2

<details><summary>Answer</summary>

**Answer: A.** Then restrict lines with `transport input ssh`. *(Domain 4)*

</details>

### Q55. Which security protocol replaces the WPA2 pre-shared key exchange in WPA3-Personal?
- A) TKIP
- B) SAE
- C) EAP-TLS
- D) WEP

<details><summary>Answer</summary>

**Answer: B.** Simultaneous Authentication of Equals resists offline dictionary attacks. *(Domain 1)*

</details>

### Q56. A router learns 10.208.165.0/24 from iBGP, OSPF, RIP. Which source is installed in the routing table (default ADs)?
- A) RIP
- B) All three, load-balanced
- C) OSPF
- D) iBGP

<details><summary>Answer</summary>

**Answer: C.** Same prefix from different sources: lowest administrative distance wins. OSPF = 110. *(Domain 3)*

</details>

### Q57. What are the RSTP port states?
- A) Blocking, listening, learning, forwarding
- B) Discarding, learning, forwarding
- C) Down, init, full
- D) Active, standby, listen

<details><summary>Answer</summary>

**Answer: B.** RSTP merged blocking, listening and disabled into discarding. *(Domain 2)*

</details>

### Q58. Which interface command removes the DR/BDR election on a link between exactly two OSPF routers?
- A) ip ospf priority 255
- B) ip ospf network point-to-point
- C) ip ospf cost 1
- D) passive-interface

<details><summary>Answer</summary>

**Answer: B.** The point-to-point network type also speeds up adjacency. *(Domain 3)*

</details>

### Q59. A router has `logging trap warnings`. Which messages are sent to the syslog server?
- A) All levels 0 through 7
- B) Level 4 only
- C) Levels 0 through 4
- D) Levels 4 through 7

<details><summary>Answer</summary>

**Answer: C.** The configured level (4) and every more severe (lower) level are sent. *(Domain 5)*

</details>

### Q60. Which symptom suggests a Layer 2 loop?
- A) Steady low CPU
- B) MAC address flapping log messages, very high CPU and link utilization
- C) One host with a wrong gateway
- D) DHCP leases expiring

<details><summary>Answer</summary>

**Answer: B.** %SW_MATM-4-MACFLAP_NOTIF and saturated links are classic loop signs. *(Domain 2)*

</details>

### Q61. Two non-root switches share a segment, and both report the same root path cost. Which port becomes designated for that segment?
- A) The one on the switch with the lower bridge ID
- B) The one on the switch with the higher MAC
- C) Both
- D) Neither

<details><summary>Answer</summary>

**Answer: A.** Tie-breaker after cost: lowest sender bridge ID. *(Domain 2)*

</details>

### Q62. Which protocol is the IEEE standard for EtherChannel negotiation?
- A) PAgP
- B) LACP
- C) DTP
- D) VTP

<details><summary>Answer</summary>

**Answer: B.** LACP (802.3ad/802.1AX). PAgP is Cisco proprietary. *(Domain 2)*

</details>

### Q63. Which VPN type lets a remote employee connect a laptop to the corporate network through a browser-compatible TLS session or a lightweight client?
- A) Site-to-site IPsec
- B) SSL/TLS remote access VPN
- C) GRE tunnel
- D) DMVPN hub

<details><summary>Answer</summary>

**Answer: B.** TLS VPNs (e.g. Cisco Secure Client) use 443 and traverse most firewalls. *(Domain 4)*

</details>

### Q64. What is the broadcast address of the subnet that contains 192.168.202.156/29?
- A) 192.168.202.160
- B) 192.168.202.159
- C) 192.168.202.158
- D) 192.168.202.152

<details><summary>Answer</summary>

**Answer: B.** Network 192.168.202.152/29; the broadcast is the last address of the block, 192.168.202.159. *(Domain 1)*

</details>

### Q65. What is the severity of the syslog message `%SPANTREE-2-BLOCK_BPDUGUARD: ...`?
- A) 4 (warnings)
- B) 2 (critical)
- C) 3 (errors)
- D) 0 (emergencies)

<details><summary>Answer</summary>

**Answer: B.** Cisco format is %FACILITY-SEVERITY-MNEMONIC; the number after the facility is the severity. *(Domain 5)*

</details>

### Q66. Rapid PVST+ for VLAN 10: SW1 priority 32778 MAC a662.825d.75e3; SW2 priority 4106 MAC a8b4.1fe9.1230; SW3 priority 16394 MAC 7dbb.f2be.ad87; SW4 priority 10 MAC 72c9.51a7.5e28. Which switch becomes the root bridge?
- A) SW1
- B) SW2
- C) SW3
- D) SW4

<details><summary>Answer</summary>

**Answer: D.** Lowest bridge ID wins: compare priority (including the VLAN ID) first, then the lowest MAC. *(Domain 2)*

</details>

### Q67. The network diagram says SW1 Gi1/0/24 connects to SW2 Gi1/0/1. `show cdp neighbors` on SW1 shows `SW2  Gig 1/0/23  ...  Gig 1/0/2`. What do you conclude?
- A) CDP is wrong
- B) The documentation is wrong: SW1 Gi1/0/23 connects to SW2 Gi1/0/2
- C) The link is down
- D) LLDP must be used instead

<details><summary>Answer</summary>

**Answer: B.** CDP output shows the local interface and the neighbor's port ID; use it to validate and fix diagrams. *(Domain 2)*

</details>

### Q68. An ACL entry is `permit ip 10.204.188.0 0.0.3.255 any`. Which source address matches it?
- A) 10.204.196.2
- B) 10.204.187.67
- C) 10.204.192.163
- D) 10.204.191.169

<details><summary>Answer</summary>

**Answer: D.** 10.204.188.0 0.0.3.255 covers 10.204.188.0-10.204.191.255 (10.204.188.0/22). *(Domain 4)*

</details>

### Q69. Which command configures OSPFv3 for IPv6 on an interface (process 1, area 0)?
- A) ipv6 ospf 1 area 0
- B) ospfv3 network area 0
- C) ip ospf 1 area 0 ipv6
- D) ipv6 router ospf area 0

<details><summary>Answer</summary>

**Answer: A.** OSPFv3 is enabled per interface; it also needs `ipv6 unicast-routing` and a 32-bit router ID. *(Domain 3)*

</details>

### Q70. OSPF uses auto-cost reference-bandwidth 100000 (Mbps). What is the cost of a 10 Mbps interface?
- A) 10000
- B) 1000
- C) 10001
- D) 100000

<details><summary>Answer</summary>

**Answer: A.** Cost = reference / interface bandwidth = 100000/10 = 10000 (minimum 1). *(Domain 3)*

</details>

### Q71. Which wildcard mask matches the same addresses as subnet mask 255.255.255.240 in an ACL?
- A) 0.0.0.31
- B) 255.255.255.240
- C) 0.0.0.7
- D) 0.0.0.15

<details><summary>Answer</summary>

**Answer: D.** Wildcard = 255.255.255.255 − mask = 0.0.0.15. *(Domain 4)*

</details>

### Q72. Rapid PVST+ for VLAN 30: SW1 priority 32798 MAC 237b.a932.a1e4; SW2 priority 32798 MAC 1dee.109b.ba66; SW3 priority 4126 MAC 0361.fbd9.1b00; SW4 priority 8222 MAC 368c.5fbc.55e9. Which switch becomes the root bridge?
- A) SW2
- B) SW4
- C) SW1
- D) SW3

<details><summary>Answer</summary>

**Answer: D.** Lowest bridge ID wins: compare priority (including the VLAN ID) first, then the lowest MAC. *(Domain 2)*

</details>

### Q73. What does a packet capture on a trunk show for frames in VLAN 20 (not native)?
- A) No tag
- B) An 802.1Q tag with VID 20 after the source MAC
- C) A VXLAN header
- D) An MPLS label

<details><summary>Answer</summary>

**Answer: B.** Non-native VLAN frames carry an 802.1Q tag (EtherType 0x8100). *(Domain 2)*

</details>

### Q74. A user's laptop gets a valid IP from Wi-Fi but cannot resolve names, while pinging 8.8.8.8 works. What is the most likely cause?
- A) Wrong gateway
- B) Missing or wrong DNS server configuration
- C) Wrong subnet mask
- D) Weak RSSI

<details><summary>Answer</summary>

**Answer: B.** IP connectivity works; name resolution does not. *(Domain 1)*

</details>

### Q75. A Windows host shows IP address 169.254.12.7. What does this mean?
- A) The host has a static private address
- B) The host failed to get a DHCP lease and self-assigned an APIPA address
- C) The host is using IPv6
- D) The host is behind NAT

<details><summary>Answer</summary>

**Answer: B.** 169.254.0.0/16 is link-local (APIPA), used when no DHCP server answers. *(Domain 1)*

</details>

### Q76. Host A is 172.28.245.138/23. Which host is in the same subnet as Host A (same mask)?
- A) 172.28.245.107
- B) 172.28.247.50
- C) 172.28.242.4
- D) 172.28.248.107

<details><summary>Answer</summary>

**Answer: A.** Host A is in 172.28.244.0/23; only 172.28.245.107 falls inside 172.28.244.0-172.28.245.255. *(Domain 1)*

</details>

### Q77. A VMware host runs VMs in VLANs 100 and 200 using a vSwitch with VLAN tagging. How should the physical switch port be configured?
- A) Access VLAN 100
- B) 802.1Q trunk allowing VLANs 100 and 200
- C) Routed port with two IPs
- D) Port security maximum 1

<details><summary>Answer</summary>

**Answer: B.** Virtualized hosts that tag VLANs need a trunk. *(Domain 2)*

</details>

### Q78. You must capture traffic from a server port to a laptop running Wireshark on the same switch. Which feature do you use?
- A) SPAN (monitor session)
- B) Port security
- C) BPDU filter
- D) DHCP snooping

<details><summary>Answer</summary>

**Answer: A.** `monitor session 1 source interface g1/0/5` and `destination interface g1/0/10` mirror traffic. *(Domain 2)*

</details>

### Q79. Which address can be assigned to a host in subnet 10.0.71.64/26?
- A) 10.0.71.64
- B) 10.0.71.128
- C) 10.0.71.127
- D) 10.0.71.86

<details><summary>Answer</summary>

**Answer: D.** 10.0.71.64/26 spans 10.0.71.64-10.0.71.127; usable hosts are 10.0.71.65-10.0.71.126. *(Domain 1)*

</details>

### Q80. What is the correct shortest form of 2001:0db8:c3b6:0000:0000:0023:be01:2e62?
- A) 2001:db8:c3b6::23:be01:2e62
- B) 2001:0db8:c3b6::0023:be01:2e62
- C) 2001:db8:c3b6:0:0:23:be01:2e62
- D) 2001:db8:c3b6:23:be01:2e62

<details><summary>Answer</summary>

**Answer: A.** Remove leading zeros in each hextet, then replace the longest run of all-zero hextets with :: (only once). *(Domain 1)*

</details>

### Q81. Which address can be assigned to a host in subnet 192.168.236.0/29?
- A) 192.168.236.0
- B) 192.168.236.1
- C) 192.168.236.8
- D) 192.168.236.7

<details><summary>Answer</summary>

**Answer: B.** 192.168.236.0/29 spans 192.168.236.0-192.168.236.7; usable hosts are 192.168.236.1-192.168.236.6. *(Domain 1)*

</details>

### Q82. In a controller-based architecture, what is the southbound interface?
- A) The REST API used by scripts to talk to the controller
- B) The interface/protocols the controller uses to program network devices (e.g. NETCONF, RESTCONF, SSH)
- C) The console port
- D) The management VLAN

<details><summary>Answer</summary>

**Answer: B.** Northbound = apps to controller; southbound = controller to devices. *(Domain 5)*

</details>

### Q83. Which component lets several virtual machines share one physical server's CPU, memory and NICs?
- A) A container runtime only
- B) A hypervisor
- C) A load balancer
- D) A virtual switch only

<details><summary>Answer</summary>

**Answer: B.** A hypervisor (Type 1 like ESXi/KVM, or Type 2) abstracts hardware and runs VMs, each with its own guest OS. *(Domain 1)*

</details>

### Q84. What is the main function of SNMP in network operations?
- A) Encrypting user traffic
- B) Monitoring and (optionally) managing devices by reading/writing MIB objects and receiving traps
- C) Routing between areas
- D) Assigning IP addresses

<details><summary>Answer</summary>

**Answer: B.** Managers poll agents (UDP 161); agents send traps/informs (UDP 162). *(Domain 5)*

</details>

### Q85. How does a Cisco router choose its OSPF router ID if `router-id` is not configured?
- A) Lowest physical interface IP
- B) Highest up loopback IP; if none, highest up physical interface IP
- C) The MAC address
- D) Random

<details><summary>Answer</summary>

**Answer: B.** Manual RID > highest loopback > highest active interface. *(Domain 3)*

</details>

### Q86. Which record delegates a subdomain to other name servers?
- A) NS
- B) SOA
- C) CNAME
- D) AAAA

<details><summary>Answer</summary>

**Answer: A.** NS records point to the authoritative servers for a zone or subdomain. *(Domain 4)*

</details>

### Q87. What does PortFast do on an access port?
- A) Disables STP entirely
- B) Moves the port to forwarding immediately, skipping the listening/learning delay
- C) Bundles ports
- D) Speeds up autonegotiation

<details><summary>Answer</summary>

**Answer: B.** PortFast (RSTP edge port) is for end hosts only. *(Domain 2)*

</details>

### Q88. An interface with MAC 4c:de:c6:31:65:1e uses EUI-64 with prefix 2001:db8:1:1::/64. What is its interface ID?
- A) 4ede:c6fe:ff31:651e
- B) 4cde:c6ff:fe31:651e
- C) 4ede:c6ff:fe31:651e
- D) 4cde:c631:651e:0

<details><summary>Answer</summary>

**Answer: C.** Insert ff:fe between the OUI and NIC parts, then flip the 7th bit (U/L) of the first byte. *(Domain 1)*

</details>

### Q89. Which subinterface command configures a router to handle VLAN 30 tagged frames?
- A) switchport access vlan 30
- B) encapsulation dot1Q 30
- C) vlan 30 encapsulation
- D) ip vlan 30

<details><summary>Answer</summary>

**Answer: B.** Router subinterfaces use `encapsulation dot1Q <vlan-id>` (add `native` for the native VLAN). *(Domain 2)*

</details>

### Q90. Which extended ACL entry permits HTTPS from 10.10.10.0/24 to server 10.50.0.80?
- A) permit tcp 10.10.10.0 0.0.0.255 host 10.50.0.80 eq 443
- B) permit udp 10.10.10.0 0.0.0.255 host 10.50.0.80 eq 443
- C) permit tcp host 10.50.0.80 10.10.10.0 0.0.0.255 eq 443
- D) permit ip 10.10.10.0 255.255.255.0 10.50.0.80 eq 443

<details><summary>Answer</summary>

**Answer: A.** Protocol TCP, source with wildcard, destination host, destination port. *(Domain 4)*

</details>

### Q91. What prefix length should an IPv6 LAN segment use so SLAAC works?
- A) /48
- B) /56
- C) /64
- D) /127

<details><summary>Answer</summary>

**Answer: C.** SLAAC builds a 64-bit interface ID, so the prefix must be /64. *(Domain 1)*

</details>

### Q92. What does DHCP snooping do on untrusted ports?
- A) Allows all DHCP messages
- B) Drops server messages (OFFER, ACK) and builds a binding table from client leases
- C) Encrypts DHCP
- D) Assigns static IPs

<details><summary>Answer</summary>

**Answer: B.** Only trusted ports (toward real servers) may send server messages. *(Domain 4)*

</details>

### Q93. Hosts in VLAN 20 on SW1 cannot reach VLAN 20 hosts on SW2. VLAN 10 works across the same trunk. Which command shows the likely cause?
- A) show vlan brief
- B) show interfaces trunk
- C) show ip route
- D) show cdp neighbors

<details><summary>Answer</summary>

**Answer: B.** Check the allowed and active VLAN lists on the trunk. *(Domain 2)*

</details>

### Q94. You want a public generative AI tool to explain an ACL change. The config includes SNMP communities and local user hashes. What should you do first?
- A) Paste the full config for best context
- B) Remove or mask sensitive data according to its classification, or use an approved enterprise tool
- C) Ask the AI to keep it secret
- D) Encode the config in Base64

<details><summary>Answer</summary>

**Answer: B.** Data classification decides what may be shared with which AI tool. *(Domain 5)*

</details>

### Q95. Which address is an IPv6 unique local address?
- A) 2001:db8::1
- B) fe80::1
- C) fd3a:91c2:7b00::10
- D) ff02::2

<details><summary>Answer</summary>

**Answer: C.** Unique local addresses use fc00::/7, in practice fd00::/8. *(Domain 1)*

</details>

### Q96. A floating static route never becomes active when the primary ISP fails because the primary route is also static and its next-hop interface stays up. What fixes this?
- A) Lower the floating route's AD to 1
- B) Use IP SLA tracking on the primary route (or a dynamic protocol/BFD)
- C) Remove the primary route
- D) Use a host route

<details><summary>Answer</summary>

**Answer: B.** Tracking removes the primary route when the remote test fails, so the floating route can install. *(Domain 3)*

</details>

### Q97. A server with a static IP loses connectivity after DAI is enabled on its VLAN. What is the cleanest fix?
- A) Disable DHCP snooping
- B) Add an ARP ACL (or static binding) for the server, or trust its port if appropriate
- C) Change the VLAN
- D) Enable PortFast

<details><summary>Answer</summary>

**Answer: B.** Static hosts have no DHCP binding, so DAI drops their ARP. *(Domain 4)*

</details>

### Q98. Which IPsec protocol provides encryption and is identified as IP protocol 50?
- A) AH
- B) ESP
- C) IKE
- D) GRE

<details><summary>Answer</summary>

**Answer: B.** AH (51) gives integrity only and breaks with NAT. *(Domain 4)*

</details>

### Q99. Which TWO statements describe HSRP? (Choose 2.)
- A) Cisco-proprietary first-hop redundancy protocol
- B) Active/standby routers share a virtual IP and virtual MAC
- C) Preemption is enabled by default
- D) It uses multicast 224.0.0.18
- E) It requires OSPF

<details><summary>Answer</summary>

**Answer: A, B.** HSRP preemption is off by default; VRRP uses 224.0.0.18. *(Domain 3)*

</details>

### Q100. Which command shows LLDP neighbors with their system name, port description and management address?
- A) show lldp neighbors detail
- B) show cdp interface
- C) show lldp traffic
- D) show interfaces counters

<details><summary>Answer</summary>

**Answer: A.** `show lldp neighbors detail` lists full neighbor TLVs; use it on multi-vendor links where CDP is unavailable. *(Domain 2)*

</details>
