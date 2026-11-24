# Cheatsheet 01 — Network Models

## Layers and PDUs

| # | OSI | TCP/IP | PDU | Address | Device |
|---|---|---|---|---|---|
| 7 | Application | Application | Data | URL / name | Proxy, L7 LB |
| 6 | Presentation | Application | Data | — | — |
| 5 | Session | Application | Data | — | — |
| 4 | Transport | Transport | Segment / Datagram | Port | Firewall, L4 LB |
| 3 | Network | Internet | Packet | IP | Router |
| 2 | Data link | Link | Frame | MAC | Switch, AP |
| 1 | Physical | Link | Bits | — | Cable, hub |

Mnemonic (7→1): **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing.

## "Next protocol" values

| Field | Value | Payload |
|---|---|---|
| EtherType | 0x0800 | IPv4 |
| EtherType | 0x86DD | IPv6 |
| EtherType | 0x0806 | ARP |
| EtherType | 0x8100 | 802.1Q tag |
| EtherType | 0x8847 | MPLS unicast |
| EtherType | 0x88CC | LLDP |
| IP protocol | 1 / 6 / 17 | ICMP / TCP / UDP |
| IP protocol | 47 / 50 / 51 | GRE / ESP / AH |
| IP protocol | 58 / 88 / 89 / 112 | ICMPv6 / EIGRP / OSPF / VRRP |

## Header sizes

| Header | Size |
|---|---|
| Ethernet II | 14 B + 4 B FCS (18 B with 802.1Q tag + FCS = 22 B) |
| IPv4 | 20 B (60 B max with options) |
| IPv6 | 40 B fixed |
| TCP | 20 B (60 B max) |
| UDP | 8 B |
| VXLAN overhead | 50 B (outer Eth 14 + IP 20 + UDP 8 + VXLAN 8) |

## Commands

| Task | Command |
|---|---|
| Capture with MACs | `sudo tcpdump -i eth0 -e -nn -vv` |
| Capture to a file | `sudo tcpdump -i eth0 -w out.pcap host 10.0.0.5` |
| Hex + ASCII | `sudo tcpdump -i eth0 -X -c 1 port 80` |
| Wireshark CLI | `tshark -r out.pcap -V -c 1` |
| Show interfaces | `ip -br link` / `ip -br addr` |
| Cisco interface status | `show ip interface brief` |

## Troubleshooting by layer

| Layer | Quick test |
|---|---|
| 1 | `ethtool eth0`, link LED, `show interfaces` (CRC, input errors) |
| 2 | `ip neigh`, `show mac address-table`, `show vlan brief` |
| 3 | `ping`, `ip route get <ip>`, `traceroute`, `show ip route` |
| 4 | `ss -tlnp`, `nc -vz host port`, SG/NACL rules |
| 7 | `curl -v`, `dig`, `openssl s_client -connect host:443` |
