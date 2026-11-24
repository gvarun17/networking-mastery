# Cheatsheet 11 — Security

## ACLs (IOS)

| Type | Range | Place |
|---|---|---|
| Standard | 1-99, 1300-1999 | Near destination |
| Extended | 100-199, 2000-2699 | Near source |

```text
access-list 10 permit 10.99.0.0 0.0.0.255
ip access-list extended WEB
 10 permit tcp 10.10.10.0 0.0.0.255 host 10.50.0.80 eq 443
 20 deny ip any any log
 15 permit udp any host 10.50.0.53 eq 53       ! insert between 10 and 20
interface g0/1
 ip access-group WEB in
line vty 0 15
 access-class 10 in
show access-lists
show ip interface g0/1 | include access list
```

Keywords: `host x` = `x 0.0.0.0`; `any` = `0.0.0.0 255.255.255.255`; `eq lt gt neq range`; `established` (TCP ACK/RST set).

## Firewalls

| | Stateless | Stateful |
|---|---|---|
| Return traffic | Explicit rule | Automatic |
| AWS | NACL | Security group |
| Linux | nft without `ct` | `ct state established,related accept` |

## VPN

| Item | Value |
|---|---|
| IKE | UDP 500, NAT-T UDP 4500 |
| ESP / AH | IP 50 / IP 51 |
| WireGuard | UDP 51820 (default) |
| OpenVPN | UDP/TCP 1194 or 443 |
| L2TP | UDP 1701 (with IPsec) |
| GRE | IP 47 |

## AAA

| | RADIUS | TACACS+ |
|---|---|---|
| Port | UDP 1812/1813 (legacy 1645/1646) | TCP 49 |
| Encrypts | Password | Whole body |
| Use | Network access | Device admin |

```text
username admin privilege 15 algorithm-type scrypt secret <pw>
enable algorithm-type scrypt secret <pw>
service password-encryption
aaa new-model
aaa authentication login default group tacacs+ local
ip ssh version 2
crypto key generate rsa modulus 2048
login block-for 120 attempts 5 within 60
```

## Layer 2 security

```text
ip dhcp snooping
ip dhcp snooping vlan 10
interface g1/0/48
 ip dhcp snooping trust
 ip arp inspection trust
interface range g1/0/1-24
 ip dhcp snooping limit rate 15
 storm-control broadcast level 5.00
 storm-control action shutdown
ip arp inspection vlan 10
ipv6 nd raguard policy HOSTS
 device-role host
show ip dhcp snooping binding
show ip arp inspection statistics
show storm-control
```

## Linux

| Task | Command |
|---|---|
| List rules | `sudo nft list ruleset` |
| Conntrack | `sudo conntrack -L` |
| WireGuard status | `sudo wg show` |
| IPsec (strongSwan) | `sudo swanctl --list-sas` |
| Port scan your own host | `nmap -sS -p- 10.0.0.5` |
