# Video Script 12 — "From TLS Hello to 502: The Application Layer for Ops"

**Length:** about 7 minutes.

| # | Time | Visual | Narration |
|---|---|---|---|
| 1 | 0:00-0:30 | Browser error page "502 Bad Gateway". | "Most outages your users see are application-layer messages. Let's learn to read them." |
| 2 | 0:30-1:30 | `curl -v` output, annotated. | "curl -v shows everything: TCP connect, the TLS handshake, ALPN, request headers and the response." |
| 3 | 1:30-2:30 | Diagram: HTTP versions flow. | "HTTP/1.1: one request at a time per connection. HTTP/2: many streams on one TCP connection. HTTP/3: streams on QUIC, so one lost packet stalls only one stream." |
| 4 | 2:30-3:45 | Diagram: TLS 1.3 handshake. | "TLS 1.3 takes one round trip. The client sends its key share and SNI. The server answers with its key share, then everything is encrypted, including the certificate." |
| 5 | 3:45-5:00 | Diagram: L4 vs L7. Lab steps 2 and 3 side by side. | "An L4 balancer moves TCP connections. It cannot see paths. An L7 balancer terminates the connection, reads the request, routes by path, and adds X-Forwarded-For." |
| 6 | 5:00-5:45 | Status code table: 502, 503, 504 highlighted. | "502: the backend broke the conversation. 503: no healthy backend. 504: the backend was too slow." |
| 7 | 5:45-6:30 | CDN map with edge locations. Headers Age and X-Cache. | "A CDN caches near the user. Check Age and X-Cache to see hits. Version your file names to avoid stale content." |
| 8 | 6:30-7:00 | AWS LB comparison table. | "In AWS: ALB for HTTP, NLB for TCP and UDP with static IPs, CloudFront at the edge." |

## Diagrams to show

1. HTTP version evolution.
2. TLS 1.3 sequence.
3. L4 vs L7 diagram.
