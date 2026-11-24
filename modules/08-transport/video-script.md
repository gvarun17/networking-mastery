# Video Script 08 — "TCP Under the Microscope (and Why QUIC Exists)"

**Length:** about 8 minutes.

| # | Time | Visual | Narration |
|---|---|---|---|
| 1 | 0:00-0:30 | A slow file copy progress bar. | "Your link is 1 gigabit but the copy runs at 40 megabits. The answer is in TCP." |
| 2 | 0:30-1:30 | Table: TCP vs UDP vs QUIC. | "IP is best effort. TCP adds reliability, order, flow control and congestion control. UDP adds only ports. QUIC rebuilds TCP's features on UDP, with encryption built in." |
| 3 | 1:30-2:45 | Diagram: handshake/close sequence. Lab tcpdump with sequence numbers. | "Three-way handshake: SYN, SYN-ACK, ACK. Each side picks a random starting sequence number. The SYN-ACK acknowledges ISN plus one." |
| 4 | 2:45-3:30 | Diagram: TCP state machine; highlight TIME_WAIT and CLOSE_WAIT. | "TIME_WAIT is normal on the side that closes first. CLOSE_WAIT piling up is an application bug." |
| 5 | 3:30-4:45 | BDP calculation on a whiteboard. | "To fill a pipe, the window must be bandwidth times RTT. One gigabit at 100 milliseconds needs 12.5 megabytes in flight." |
| 6 | 4:45-6:00 | Diagram: congestion control flow. Lab step 5 results table. | "Congestion control starts slow, doubles every RTT, and backs off on loss. CUBIC treats loss as congestion. BBR measures the path. With 1% loss, BBR wins by a lot." |
| 7 | 6:00-7:00 | Diagram: TCP+TLS vs QUIC handshake. | "QUIC merges the transport and TLS handshakes: one round trip instead of two. Streams are independent, so one lost packet does not stall the page." |
| 8 | 7:00-8:00 | AWS slide: NACL ephemeral ports, idle timeouts. | "In AWS: NACLs are stateless, so allow ephemeral ports. NAT gateways drop idle flows after 350 seconds, so turn on keepalives." |

## Diagrams to show

1. Handshake/close sequence.
2. TCP state machine.
3. Congestion control flow.
4. TCP+TLS vs QUIC sequence.
