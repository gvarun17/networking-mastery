# Quiz 18 — Network Observability

## Questions

### Q1. Which signal best answers "which hosts are sending the most traffic to the database subnet?"

- A) Syslog
- B) CPU metrics
- C) Flow records (NetFlow/IPFIX/sFlow or VPC Flow Logs)
- D) Interface counters

<details><summary>Answer</summary>

**Answer: C.** Flows record source, destination, ports and volume. Interface counters show totals only.

</details>

### Q2. What is the main difference between sFlow and NetFlow v9?

- A) NetFlow cannot carry IPv6
- B) sFlow uses TCP
- C) sFlow is Cisco proprietary
- D) sFlow samples packets (1 in N) and counters; NetFlow builds flow records from a flow cache

<details><summary>Answer</summary>

**Answer: D.** sFlow is packet sampling plus counter samples. NetFlow v9/IPFIX aggregate packets into template-based flow records.

</details>

### Q3. Which UDP port is the IANA default for IPFIX?

- A) 161
- B) 2055
- C) 6343
- D) 4739

<details><summary>Answer</summary>

**Answer: D.** IPFIX 4739. sFlow 6343. NetFlow commonly 2055/9995 (not IANA-assigned). SNMP 161.

</details>

### Q4. Why must you use `rate()` when graphing `node_network_receive_bytes_total`?

- A) The metric is a cumulative counter; utilisation is its per-second rate of change
- B) Prometheus requires it for all metrics
- C) The metric is a gauge
- D) To convert bits to bytes

<details><summary>Answer</summary>

**Answer: A.** Counters only increase (and reset). `rate()` computes per-second change and handles resets.

</details>

### Q5. A 1 Gbps interface is monitored with the 32-bit `ifInOctets` counter every 5 minutes. What problem occurs?

- A) None
- B) The counter wraps in about 34 seconds at line rate, so polling every 5 minutes gives wrong results; use 64-bit `ifHCInOctets`
- C) SNMP cannot read it
- D) It only counts errors

<details><summary>Answer</summary>

**Answer: B.** 2^32 bytes ≈ 4.29 GB; at 125 MB/s it wraps in ~34 s.

</details>

### Q6. Which TWO are advantages of gNMI streaming telemetry over SNMP polling? (Choose two.)

- A) Higher-frequency data with lower device CPU cost
- B) It needs no authentication
- C) It uses UDP 161
- D) Structured data based on YANG models
- E) It works on every legacy device

<details><summary>Answer</summary>

**Answer: A, D.** Telemetry pushes YANG-modelled data efficiently. SNMP still wins on universal legacy support.

</details>

### Q7. What does a VPC Flow Log record contain?

- A) Full packet payloads
- B) Per-ENI flow metadata: addresses, ports, protocol, packets, bytes, action (ACCEPT/REJECT) and optional fields
- C) HTTP URLs
- D) DNS query names

<details><summary>Answer</summary>

**Answer: B.** Flow Logs are metadata, not packets. Use Traffic Mirroring for packets and Route 53 Resolver query logs for DNS names.

</details>

### Q8. How does Datadog Network Performance Monitoring collect flow data on hosts and Kubernetes nodes?

- A) Syslog parsing
- B) SNMP polling of switches only
- C) An eBPF-based system-probe in the Datadog Agent that observes connections in the kernel
- D) Packet capture to disk

<details><summary>Answer</summary>

**Answer: C.** The system-probe uses eBPF to collect connection-level metrics (volume, retransmits, RTT) tagged by service.

</details>

### Q9. Which Prometheus exporter runs synthetic ICMP, HTTP, DNS and TCP probes?

- A) blackbox_exporter
- B) node_exporter
- C) snmp_exporter
- D) pushgateway

<details><summary>Answer</summary>

**Answer: A.** blackbox_exporter probes targets and exposes `probe_success` and timing metrics.

</details>

### Q10. Scenario: Users report slowness, but 5-minute average link utilisation is only 40%. What could hide the problem?

- A) Too many dashboards
- B) DNS caching
- C) Microbursts that fill buffers for milliseconds; check queue drops and use finer-grained telemetry
- D) IPv6

<details><summary>Answer</summary>

**Answer: C.** Averages smooth out short bursts. Look at output drops/discards and high-resolution telemetry.

</details>

### Q11. Why is `for: 5m` important in a Prometheus alert rule?

- A) It delays scrapes
- B) It sets the rate window
- C) The condition must stay true for 5 minutes before the alert fires, which reduces flapping and noise
- D) It sets the retention period

<details><summary>Answer</summary>

**Answer: C.** Durations prevent alerts on brief blips.

</details>

### Q12. Flow totals from a sampled sFlow collector are 1000× lower than interface counters. What is the most likely cause?

- A) Flows are encrypted
- B) The collector did not multiply by the sampling rate (1:1000)
- C) MTU mismatch
- D) The link is down

<details><summary>Answer</summary>

**Answer: B.** Sampled counts must be scaled by the sampling rate.

</details>

### Q13. Which is a good network SLI?

- A) Percentage of successful synthetic probes from user locations to the service
- B) Number of routers
- C) Number of VLANs
- D) Size of the config file

<details><summary>Answer</summary>

**Answer: A.** SLIs measure the user experience: availability, latency, loss.

</details>

### Q14. Which signal type is best for proving exactly why a TLS handshake fails between two hosts?

- A) Packet capture
- B) Interface metrics
- C) SNMP traps
- D) Flow records

<details><summary>Answer</summary>

**Answer: A.** Only packets show the handshake messages and alerts. Capture on demand because of volume and privacy.

</details>

### Q15. Scenario: Your AWS bill shows high NAT gateway data processing charges. Which observability data helps you find the cause fastest?

- A) Syslog from routers
- B) VPC Flow Logs (or Datadog NPM) grouped by destination, to find large flows to S3/ECR that could use VPC endpoints
- C) CloudTrail only
- D) EC2 CPU metrics

<details><summary>Answer</summary>

**Answer: B.** Flow data shows which sources send most bytes through the NAT gateway and where. Gateway endpoints for S3/DynamoDB and interface endpoints for ECR usually cut the cost.

</details>
