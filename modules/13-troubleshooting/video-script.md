# Video Script 13 — "Troubleshoot Like a Network Engineer"

**Length:** about 7 minutes.

| # | Time | Visual | Narration |
|---|---|---|---|
| 1 | 0:00-0:30 | Pager alert: "API timeouts". | "An alert fires. Do not start changing things. Start with a method." |
| 2 | 0:30-1:30 | Diagram: method flowchart. | "Define the problem. Gather facts. Form one hypothesis. Test it. Fix with the smallest change. Verify as the user. Write it down. And ask: what changed?" |
| 3 | 1:30-2:15 | Approach table. | "Pick the approach: bottom-up for physical changes, top-down when one app fails, divide and conquer when you have one clue in the middle." |
| 4 | 2:15-3:15 | Tools-by-layer diagram. Quick terminal demos: ping, ip route get. | "Each layer has its tools. ping and ip route get for Layer 3. ss and nc for Layer 4. curl, dig and openssl for Layer 7." |
| 5 | 3:15-4:15 | mtr output; highlight a false-loss hop. | "Read mtr correctly. Loss at one hop that disappears later is just ICMP rate limiting. Real loss continues to the destination." |
| 6 | 4:15-5:30 | Diagram: two-point capture decision sequence. | "Capture at both ends. SYN not arriving? Forward path. SYN-ACK leaving but not arriving? Return path. RST? Nothing listening or a host firewall." |
| 7 | 5:30-6:15 | nmap open/closed/filtered table. | "Closed means the host answered with a reset. Filtered means silence. That tells you where to look." |
| 8 | 6:15-7:00 | Lab: inject random fault; solve ticket 9 on screen. | "Practise with the ten fault tickets. Here, small pages work and big downloads hang. The answer is an MTU black hole." |

## Diagrams to show

1. Method flowchart.
2. Tools by layer.
3. Two-point capture sequence.
