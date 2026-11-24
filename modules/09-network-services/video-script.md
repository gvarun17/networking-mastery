# Video Script 09 — "The Invisible Services: DHCP, DNS, NAT, NTP, SNMP, Syslog"

**Length:** about 8 minutes.

| # | Time | Visual | Narration |
|---|---|---|---|
| 1 | 0:00-0:30 | Laptop joins Wi-Fi and opens a website. Six service icons appear. | "Six services run before your first web page loads. When they fail, everything fails." |
| 2 | 0:30-1:45 | Diagram: DORA through a relay. | "DHCP: discover, offer, request, acknowledge. Routers block broadcasts, so a relay turns them into unicast and stamps giaddr so the server picks the right pool." |
| 3 | 1:45-3:30 | Diagram: DNS resolution sequence. Terminal: `dig +trace`. | "DNS: your stub asks a recursive resolver. The resolver walks from the root to the TLD to the authoritative server, then caches the answer for the TTL." |
| 4 | 3:30-4:15 | Record type table. | "Know the records: A and AAAA for addresses, CNAME for aliases, MX for mail, NS for delegation, PTR for reverse." |
| 5 | 4:15-5:30 | Diagram: NAT inside/outside flow. `show ip nat translations`. | "NAT rewrites the source address on the way out and reverses it on the way back. PAT adds port numbers so thousands of hosts share one IP." |
| 6 | 5:30-6:15 | Stratum pyramid. | "NTP keeps clocks honest. Without it, logs lie, TLS breaks and Kerberos fails." |
| 7 | 6:15-7:00 | SNMP manager/agent arrows: 161 poll, 162 trap. | "SNMP: managers poll agents on 161, agents send traps to 162. Use version 3 for authentication and encryption." |
| 8 | 7:00-8:00 | Syslog line, colour-coded facility-severity-mnemonic. Severity table. | "Syslog: read %LINEPROTO-5-UPDOWN as facility, severity 5, mnemonic. Lower number means worse. 'logging trap 4' sends 0 through 4." |

## Diagrams to show

1. DHCP DORA with relay.
2. DNS resolution sequence.
3. NAT translation flow.
