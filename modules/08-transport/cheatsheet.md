# Cheatsheet 08 — Transport

## TCP header flags

| Flag | Meaning |
|---|---|
| SYN | Start, sync sequence numbers |
| ACK | Acknowledgment field valid |
| FIN | Sender is done |
| RST | Abort |
| PSH | Push data to app now |
| URG | Urgent pointer valid |
| ECE / CWR | ECN congestion signalling |

tcpdump filters: `'tcp[tcpflags] & tcp-syn != 0'`, `'tcp[tcpflags] & tcp-rst != 0'`.

## Port ranges

| Range | Use |
|---|---|
| 0-1023 | Well known |
| 1024-49151 | Registered |
| 49152-65535 | IANA ephemeral |
| 32768-60999 | Linux default ephemeral |

## Key numbers

| Item | Value |
|---|---|
| TCP header | 20-60 B |
| UDP header | 8 B |
| MSS on 1500 MTU | 1460 (1448 with timestamps) |
| Initial cwnd (Linux) | 10 MSS |
| Linux min RTO | 200 ms |
| TIME_WAIT (Linux) | 60 s |
| SYN retries (Linux) | 6 (~127 s) |
| Max window with scaling | ~1 GB (shift 14) |
| BDP | bandwidth × RTT |

## Linux commands

| Task | Command |
|---|---|
| Listening sockets | `ss -tulnp` |
| TCP internals | `ss -tin` |
| States | `ss -tan state time-wait` |
| Count by state | `ss -tan \| awk '{print $1}' \| sort \| uniq -c` |
| Congestion algorithm | `sysctl net.ipv4.tcp_congestion_control` |
| Enable BBR | `sysctl -w net.core.default_qdisc=fq net.ipv4.tcp_congestion_control=bbr` |
| Buffers | `sysctl net.ipv4.tcp_rmem net.ipv4.tcp_wmem` |
| Add delay/loss | `tc qdisc add dev eth0 root netem delay 100ms loss 1%` |
| Remove netem | `tc qdisc del dev eth0 root` |
| Throughput test | `iperf3 -c host -t 10 [-R] [-u -b 100M] [-P 4]` |
| Port check | `nc -vz host 443` |
| Keepalive | `sysctl net.ipv4.tcp_keepalive_time` (default 7200 s) |

## AWS timeouts

| Component | Idle timeout |
|---|---|
| NAT gateway | 350 s |
| NLB TCP | 350 s default (60-6000 s) |
| NLB UDP | 120 s |
| ALB | 60 s default (1-4000 s) |
| Gateway Load Balancer | 350 s |
