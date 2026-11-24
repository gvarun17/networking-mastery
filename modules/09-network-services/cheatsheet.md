# Cheatsheet 09 — Network Services

## Ports

| Service | Port |
|---|---|
| DHCP | UDP 67 (server), 68 (client) |
| DHCPv6 | UDP 547 (server), 546 (client) |
| DNS | UDP/TCP 53, DoT 853, DoH 443 |
| NTP | UDP 123 |
| SNMP | UDP 161 (poll), 162 (trap/inform) |
| Syslog | UDP 514, TCP 6514 (TLS) |
| TFTP | UDP 69 |

## DHCP (IOS)

```text
ip dhcp excluded-address 10.10.10.1 10.10.10.20
ip dhcp pool USERS
 network 10.10.10.0 255.255.255.0
 default-router 10.10.10.1
 dns-server 10.99.0.53
 domain-name corp.example
 lease 0 8
interface vlan 10
 ip helper-address 10.99.0.10
interface g0/0
 ip address dhcp                 ! DHCP client
show ip dhcp binding | pool | conflict | server statistics
debug ip dhcp server packet
```

## DNS

| Type | Use |
|---|---|
| A / AAAA | IPv4 / IPv6 |
| CNAME | Alias (not at apex) |
| MX | Mail (lower preference first) |
| NS | Delegation |
| PTR | Reverse |
| SOA | Zone metadata, negative TTL |
| TXT | SPF, DKIM, verification |
| SRV | Service + port |
| CAA | Allowed CAs |

```text
dig name [type] [@server] +short | +trace | +norecurse | +tcp | +dnssec | -x IP
resolvectl status ; resolvectl query name
nslookup -type=mx example.com
```

Status codes: NOERROR · NXDOMAIN · SERVFAIL · REFUSED.

## NAT (IOS)

```text
interface g0/1
 ip nat inside
interface g0/0
 ip nat outside
ip nat inside source static 10.10.10.80 203.0.113.80
ip nat inside source static tcp 10.10.10.80 443 203.0.113.80 443
ip nat pool PUB 203.0.113.10 203.0.113.20 netmask 255.255.255.0
ip nat inside source list 1 pool PUB [overload]
ip nat inside source list 1 interface g0/0 overload
show ip nat translations [verbose]
show ip nat statistics
clear ip nat translation *
```

## NTP / SNMP / Syslog (IOS)

```text
ntp server 10.99.0.123 prefer
clock timezone IST 5 30
show ntp status | associations
snmp-server group MON v3 priv
snmp-server user monitor MON v3 auth sha AUTHPASS priv aes 128 PRIVPASS
snmp-server host 10.99.0.20 version 3 priv monitor
service timestamps log datetime msec localtime
logging host 10.99.0.14
logging trap warnings
logging buffered 64000 informational
show logging
```

## Syslog severity

0 Emergency · 1 Alert · 2 Critical · 3 Error · 4 Warning · 5 Notification · 6 Informational · 7 Debugging
("Every Awesome Cisco Engineer Will Need Ice cream Daily")

## AWS

| Need | Service |
|---|---|
| DNS resolver | VPC+2, 169.254.169.253 |
| Hybrid DNS | Resolver inbound/outbound endpoints |
| NTP | 169.254.169.123 |
| NAT | NAT gateway (per AZ) |
| DHCP options | DHCP option sets |
