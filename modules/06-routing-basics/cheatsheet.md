# Cheatsheet 06 — Routing Basics

## Route selection

1. Longest prefix match.
2. Lowest administrative distance (same prefix, different sources).
3. Lowest metric (same source).
4. Equal → ECMP.

## Administrative distance

| Source | AD |
|---|---|
| Connected | 0 |
| Static | 1 |
| eBGP | 20 |
| EIGRP internal | 90 |
| OSPF | 110 |
| IS-IS | 115 |
| RIP | 120 |
| EIGRP external | 170 |
| iBGP | 200 |
| Unknown | 255 |

## Cisco static routes

```text
ip route 10.2.0.0 255.255.0.0 10.0.12.2              ! next hop
ip route 10.2.0.0 255.255.0.0 g0/1 10.0.12.2         ! fully specified
ip route 0.0.0.0 0.0.0.0 203.0.113.1                 ! default
ip route 10.9.9.9 255.255.255.255 10.0.12.2          ! host
ip route 0.0.0.0 0.0.0.0 198.51.100.1 250            ! floating
ip route 10.2.0.0 255.255.0.0 Null0                  ! discard (summary black hole)
ipv6 route ::/0 2001:db8:ffff::2
ipv6 route 2001:db8:2::/64 g0/1 fe80::2
show ip route [static|connected|10.2.0.0]
show ip route 10.2.3.4                               ! LPM lookup
show ipv6 route
```

## IP SLA tracked static (reference)

```text
ip sla 1
 icmp-echo 8.8.8.8 source-interface g0/0
 frequency 5
ip sla schedule 1 life forever start-time now
track 1 ip sla 1 reachability
ip route 0.0.0.0 0.0.0.0 203.0.113.1 track 1
ip route 0.0.0.0 0.0.0.0 198.51.100.1 250
```

## HSRP / VRRP

```text
interface g0/0
 standby version 2
 standby 10 ip 10.10.10.1
 standby 10 priority 110
 standby 10 preempt
 vrrp 20 ip 10.10.20.1          ! IOS classic; IOS XE uses "vrrp 20 address-family ipv4"
show standby brief
show vrrp brief
```

| | HSRP | VRRP |
|---|---|---|
| Default priority | 100 | 100 (owner 255) |
| Preempt default | Off | On |
| Hello / hold | 3 s / 10 s | 1 s / ~3 s |
| Group MAC | 0000.0c07.acXX (v1) / 0000.0c9f.fXXX (v2) | 0000.5e00.01XX |

## Linux

| Task | Command |
|---|---|
| Show routes | `ip route` / `ip -6 route` |
| Lookup | `ip route get 10.1.2.3` |
| Add | `sudo ip route add 10.2.0.0/16 via 10.0.12.2` |
| Default | `sudo ip route replace default via 203.0.113.1` |
| Metric (lower wins) | `sudo ip route add default via 198.51.100.1 metric 500` |
| Forwarding | `sysctl -w net.ipv4.ip_forward=1` |
| FRR | `vtysh -c "show ip route"` |
