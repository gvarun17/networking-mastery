# Cheatsheet 02 — Physical and Data Link

## Media

| Standard | Medium | Distance |
|---|---|---|
| 1000BASE-T | Cat5e/6 | 100 m |
| 10GBASE-T | Cat6a (Cat6) | 100 m (55 m) |
| 1000BASE-SX / 10GBASE-SR | MMF | 550 m / 300-400 m |
| 1000BASE-LX / 10GBASE-LR | SMF | 5-10 km / 10 km |
| 10GBASE-ER | SMF | 40 km |

Straight-through: PC to switch. Crossover: like to like (switch-switch, PC-PC). Auto-MDIX makes the cable type irrelevant on modern ports.

## Frame sizes

| Item | Bytes |
|---|---|
| Min frame (with FCS) | 64 |
| Max frame, untagged | 1518 |
| Max frame, 802.1Q | 1522 |
| MTU (payload) | 1500 |
| Jumbo MTU | 9000 (AWS 9001) |
| Runt / giant | < 64 / > 1518 (no jumbo) |

## Special MACs

| MAC | Use |
|---|---|
| ff:ff:ff:ff:ff:ff | Broadcast |
| 01:00:5e:xx | IPv4 multicast |
| 33:33:xx | IPv6 multicast |
| 01:80:c2:00:00:00 | STP BPDUs |
| 01:00:0c:cc:cc:cc | CDP, VTP, DTP |
| 01:80:c2:00:00:0e | LLDP |
| 00:00:5e:00:01:xx | VRRP virtual MAC |
| 00:00:0c:07:ac:xx | HSRPv1 virtual MAC |

## Linux commands

| Task | Command |
|---|---|
| Link speed/duplex | `ethtool eth0` |
| NIC errors | `ip -s link show eth0`, `ethtool -S eth0` |
| ARP table | `ip neigh` |
| Flush ARP | `sudo ip neigh flush dev eth0` |
| Send GARP | `arping -U -I eth0 <ip>` |
| Duplicate IP check | `arping -D -I eth0 <ip>` |
| Bridge FDB | `bridge fdb show br br0` |
| Set MTU | `sudo ip link set eth0 mtu 9000` |
| PMTU test | `ping -M do -s 1472 <ip>` |
| PMTU discovery | `tracepath <ip>` |

## Cisco IOS commands

| Task | Command |
|---|---|
| Interface detail and counters | `show interfaces g0/1` |
| Status summary | `show interfaces status` |
| Optic levels | `show interfaces transceiver` |
| MAC table | `show mac address-table [dynamic]` |
| ARP table | `show ip arp` |
| Set speed/duplex | `speed auto` / `duplex auto` |
| Clear counters | `clear counters g0/1` |

## Counter meanings

| Counter | Usual cause |
|---|---|
| CRC / input errors | Cable, optic, EMI, duplex mismatch (full side) |
| Late collisions | Duplex mismatch (half side), cable too long |
| Runts | Collisions, duplex mismatch |
| Giants | MTU mismatch |
| Output drops | Congestion, QoS |
