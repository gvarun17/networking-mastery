# Cheatsheet 04 — IPv6

## Address types

| Prefix | Type |
|---|---|
| ::/128 | Unspecified |
| ::1/128 | Loopback |
| 2000::/3 | Global unicast |
| 2001:db8::/32 | Documentation |
| fc00::/7 (fd00::/8) | Unique local |
| fe80::/10 | Link-local |
| ff00::/8 | Multicast |
| 64:ff9b::/96 | NAT64 well-known prefix |
| ::ffff:0:0/96 | IPv4-mapped |

## Multicast groups

| Address | Group |
|---|---|
| ff02::1 | All nodes |
| ff02::2 | All routers |
| ff02::5 / ff02::6 | OSPFv3 routers / DRs |
| ff02::a | EIGRP routers |
| ff02::1:2 | DHCPv6 servers and relays |
| ff02::1:ffXX:XXXX | Solicited-node |
| ff02::fb | mDNS |

## ICMPv6 types

| Type | Name |
|---|---|
| 1 | Destination unreachable |
| 2 | Packet too big |
| 3 | Time exceeded |
| 128 / 129 | Echo request / reply |
| 133 / 134 | RS / RA |
| 135 / 136 | NS / NA |
| 137 | Redirect |

## Prefix sizes

| Prefix | Use |
|---|---|
| /32 | ISP allocation |
| /48 | Site |
| /56 | Small site, AWS VPC |
| /64 | LAN subnet (SLAAC), AWS subnet |
| /127 | Point-to-point link |
| /128 | Loopback / host route |

## Cisco IOS

```text
ipv6 unicast-routing
interface g0/0
 ipv6 address 2001:db8:1::1/64
 ipv6 address 2001:db8:1::/64 eui-64
 ipv6 address fe80::1 link-local
 ipv6 address autoconfig          ! act as SLAAC client
 ipv6 address dhcp                ! act as DHCPv6 client
 ipv6 nd other-config-flag        ! O flag
 ipv6 nd managed-config-flag      ! M flag
ipv6 route ::/0 2001:db8:ffff::2
ipv6 route ::/0 g0/1 fe80::2      ! link-local next hop needs the interface
show ipv6 interface brief
show ipv6 route
show ipv6 neighbors
```

## Linux

| Task | Command |
|---|---|
| Addresses | `ip -6 addr` |
| Routes | `ip -6 route` |
| Neighbors | `ip -6 neigh` |
| Ping link-local | `ping -6 fe80::1%eth0` |
| Accept RA when forwarding | `sysctl net.ipv6.conf.eth0.accept_ra=2` |
| Capture RAs | `tcpdump -i eth0 'icmp6 and ip6[40] == 134'` |
| Force IPv6 | `curl -6 -v https://example.com` |
