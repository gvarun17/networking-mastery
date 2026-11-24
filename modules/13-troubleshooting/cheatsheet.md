# Cheatsheet 13 — Troubleshooting

## Method

Define → Gather → Hypothesize → Test (one change) → Fix → Verify → Document. Ask: **what changed?**

## Tools by layer

| Layer | Linux | Cisco IOS |
|---|---|---|
| 1 | `ethtool eth0`, `ip -s link` | `show interfaces`, `show interfaces transceiver` |
| 2 | `ip neigh`, `bridge fdb`, `arping` | `show mac address-table`, `show arp`, `show cdp neighbors` |
| 3 | `ip route get`, `ping`, `traceroute`, `mtr`, `tracepath` | `show ip route`, `ping`, `traceroute`, `show ip ospf neighbor` |
| 4 | `ss -tlnp`, `ss -ti`, `nc -vz`, `nmap` | `show access-lists`, `show ip nat translations` |
| 7 | `curl -v`, `dig`, `openssl s_client` | `show logging` |

## ping / traceroute / mtr

```text
ping -c 5 -i 0.2 host               # quick
ping -M do -s 1472 host             # PMTU test (IPv4, 1500)
ping -I eth1 host                   # pick source interface
traceroute -n host                  # UDP probes
traceroute -n -T -p 443 host        # TCP SYN probes
traceroute -n -I host               # ICMP probes
mtr -rwbzc 100 host                 # report, wide, ASN, 100 cycles
tracepath host                      # PMTU per hop
```

## tcpdump

```text
tcpdump -i any -nn -s0 -w out.pcap host 10.0.0.5 and port 443
tcpdump -nn 'tcp[tcpflags] & (tcp-syn|tcp-rst) != 0'
tcpdump -nn -e arp or icmp
tcpdump -nn -r out.pcap -c 20
```

## Wireshark filters

| Filter | Shows |
|---|---|
| `tcp.analysis.retransmission` | Retransmits |
| `tcp.analysis.zero_window` | Receiver full |
| `tcp.flags.reset == 1` | RSTs |
| `dns.flags.rcode != 0` | DNS errors |
| `tls.handshake.type == 1` | ClientHello |
| `http.response.code >= 500` | Server errors |
| `icmp.type == 3 && icmp.code == 4` | Frag needed |

## nmap results

| State | Meaning |
|---|---|
| open | Listener answered |
| closed | RST: reachable, nothing listening |
| filtered | No answer: firewall drops |

## AWS

| Need | Tool |
|---|---|
| Config path check | VPC Reachability Analyzer |
| Exposure audit | Network Access Analyzer |
| Real traffic | VPC Flow Logs, TGW Flow Logs |
| Packets | Traffic Mirroring |
| Instance OS access without SSH | SSM Session Manager |
