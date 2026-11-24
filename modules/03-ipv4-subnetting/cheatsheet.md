# Cheatsheet 03 — IPv4 Subnetting

## Prefix table

| Prefix | Mask | Wildcard | Block | Usable |
|---|---|---|---|---|
| /8 | 255.0.0.0 | 0.255.255.255 | 1st octet 1 | 16,777,214 |
| /16 | 255.255.0.0 | 0.0.255.255 | 2nd octet 1 | 65,534 |
| /17 | 255.255.128.0 | 0.0.127.255 | 128 | 32,766 |
| /18 | 255.255.192.0 | 0.0.63.255 | 64 | 16,382 |
| /19 | 255.255.224.0 | 0.0.31.255 | 32 | 8,190 |
| /20 | 255.255.240.0 | 0.0.15.255 | 16 | 4,094 |
| /21 | 255.255.248.0 | 0.0.7.255 | 8 | 2,046 |
| /22 | 255.255.252.0 | 0.0.3.255 | 4 | 1,022 |
| /23 | 255.255.254.0 | 0.0.1.255 | 2 | 510 |
| /24 | 255.255.255.0 | 0.0.0.255 | 1 (3rd) / 256 | 254 |
| /25 | 255.255.255.128 | 0.0.0.127 | 128 | 126 |
| /26 | 255.255.255.192 | 0.0.0.63 | 64 | 62 |
| /27 | 255.255.255.224 | 0.0.0.31 | 32 | 30 |
| /28 | 255.255.255.240 | 0.0.0.15 | 16 | 14 |
| /29 | 255.255.255.248 | 0.0.0.7 | 8 | 6 |
| /30 | 255.255.255.252 | 0.0.0.3 | 4 | 2 |
| /31 | 255.255.255.254 | 0.0.0.1 | 2 | 2 (P2P, RFC 3021) |
| /32 | 255.255.255.255 | 0.0.0.0 | 1 | 1 (host route) |

## Magic number steps

1. Interesting octet = first octet where mask ≠ 255.
2. Block = 256 − mask octet.
3. Network = biggest multiple of block ≤ address octet.
4. Broadcast = next network − 1.

## Binary place values

`128 64 32 16 8 4 2 1`

## Special ranges

| Range | Use |
|---|---|
| 10/8, 172.16/12, 192.168/16 | RFC 1918 private |
| 100.64/10 | CGNAT shared space |
| 127/8 | Loopback |
| 169.254/16 | Link-local / APIPA / AWS IMDS |
| 192.0.2/24, 198.51.100/24, 203.0.113/24 | Documentation |
| 224/4 | Multicast |
| 240/4 | Reserved |

## Tools

| Task | Command |
|---|---|
| Subnet info | `python3 tools/subnet_calc.py info 10.1.2.3/20` |
| VLSM | `python3 tools/subnet_calc.py vlsm 10.0.0.0/22 --hosts 500 200 2` |
| Split | `python3 tools/subnet_calc.py split 10.0.0.0/16 --new-prefix 20` |
| Summarize | `python3 tools/subnet_calc.py summarize 10.1.4.0/24 10.1.5.0/24` |
| Drill | `python3 tools/subnet_calc.py practice --count 20` |
| Linux | `ipcalc 10.1.2.3/20` (package `ipcalc`) |
| Route to a host | `ip route get 10.1.2.3` |

## AWS

- 5 reserved IPs per subnet → /24 = 251, /28 = 11.
- VPC size /16 to /28.
- Plan with IPAM; never overlap if you will use peering or TGW.
