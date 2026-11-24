# Video Script 18 — "Seeing the Network: Metrics, Flows and Probes"

**Length:** about 6 minutes.

| # | Time | Visual | Narration |
|---|---|---|---|
| 1 | 0:00-0:30 | A dashboard full of green panels, and a user saying "it's slow". | "Green dashboards and unhappy users mean you are measuring the wrong things." |
| 2 | 0:30-1:30 | Five-signal table. | "Five signals: metrics say how much, flows say who talks to whom, logs say what happened, packets say exactly what was sent, and probes say what users feel." |
| 3 | 1:30-2:30 | Pipeline diagram. | "SNMP and gNMI feed metrics. NetFlow, IPFIX and sFlow feed flow collectors. Syslog feeds logs. Prometheus stores metrics; Grafana shows everything." |
| 4 | 2:30-3:30 | Raw counter graph vs rate graph. | "Interface counters only go up. Always graph the rate. Use 64-bit counters, or a gigabit link wraps in 34 seconds." |
| 5 | 3:30-4:15 | Lab: softflowd → goflow2 JSON → jq top talkers. | "Flows answer the money question: who is sending what, where. Here are my top talkers from NetFlow v9." |
| 6 | 4:15-5:00 | Blackbox probe panels and an alert firing. | "Synthetic probes measure the user path: ICMP, DNS and HTTP timing. Alert on symptoms that last, with a for duration." |
| 7 | 5:00-6:00 | Datadog NPM service map; VPC Flow Logs Insights query. | "In the cloud: VPC Flow Logs for ENI-level flows, and Datadog NPM uses eBPF to show service-to-service traffic, retransmits and cross-AZ cost." |

## Diagrams to show

1. Five-signal table.
2. Observability pipeline.
