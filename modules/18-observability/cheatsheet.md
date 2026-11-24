# Cheatsheet 18 — Network Observability

## Ports

| Protocol | Port |
|---|---|
| SNMP poll / trap | UDP 161 / 162 |
| NetFlow (common) | UDP 2055, 9995, 9996 |
| IPFIX | UDP 4739 |
| sFlow | UDP 6343 |
| Syslog | UDP 514, TCP 6514 |
| gNMI | TCP 57400 (common), 9339 |
| Prometheus / Grafana | 9090 / 3000 |
| node_exporter / blackbox | 9100 / 9115 |
| snmp_exporter | 9116 |

## PromQL

```text
rate(counter[5m])                                  # per-second rate
rate(node_network_receive_bytes_total[5m]) * 8     # bps
100 * rate(ifHCInOctets[5m]) * 8 / (ifHighSpeed * 1e6)   # % utilisation
increase(ifInErrors[1h])                           # errors in the last hour
topk(5, rate(...[5m]))                             # top N
histogram_quantile(0.95, sum by (le) (rate(x_bucket[5m])))
avg_over_time(probe_success[30d])                  # availability SLI
```

Window ≥ 4 × scrape interval. In Grafana use `$__rate_interval`.

## IF-MIB OIDs

| Name | OID |
|---|---|
| ifDescr | 1.3.6.1.2.1.2.2.1.2 |
| ifOperStatus | 1.3.6.1.2.1.2.2.1.8 |
| ifInErrors | 1.3.6.1.2.1.2.2.1.14 |
| ifHCInOctets | 1.3.6.1.2.1.31.1.1.1.6 |
| ifHCOutOctets | 1.3.6.1.2.1.31.1.1.1.10 |
| ifHighSpeed (Mbps) | 1.3.6.1.2.1.31.1.1.1.15 |
| sysUpTime | 1.3.6.1.2.1.1.3.0 |

## Flow export on devices

```text
! Cisco Flexible NetFlow (IOS XE)
flow record REC
 match ipv4 source address
 match ipv4 destination address
 match transport source-port
 match transport destination-port
 match ipv4 protocol
 collect counter bytes long
 collect counter packets long
flow exporter EXP
 destination 10.99.0.50
 transport udp 2055
 export-protocol ipfix
flow monitor MON
 record REC
 exporter EXP
interface g0/0
 ip flow monitor MON input
```

Linux: `softflowd -i eth0 -n collector:2055 -v 9` · `pmacct` · `hsflowd` (sFlow).

## AWS

| Need | Tool |
|---|---|
| Flow metadata | VPC Flow Logs, TGW Flow Logs |
| Packets | Traffic Mirroring |
| DNS names | Route 53 Resolver query logs |
| Synthetic | CloudWatch Synthetics, Network Monitor, Internet Monitor |
| Query | CloudWatch Logs Insights, Athena |

## Datadog

| Product | What |
|---|---|
| NPM | eBPF flow metrics between services/pods/hosts/cloud |
| Network Device Monitoring | SNMP profiles, NetFlow, topology |
| Network Path | Hop-by-hop path views |
| Synthetics | API/browser/ICMP/TCP/DNS tests |
