# Cheatsheet 12 — Application Layer

## curl

| Task | Command |
|---|---|
| Verbose with TLS info | `curl -v https://host/` |
| Headers only | `curl -sI https://host/` |
| Force HTTP version | `--http1.1`, `--http2`, `--http3` |
| Resolve to a specific IP | `curl --resolve host:443:1.2.3.4 https://host/` |
| Send Host header | `curl -H "Host: api.example.com" http://10.0.0.5/` |
| Timing breakdown | `curl -o /dev/null -s -w "dns:%{time_namelookup} tcp:%{time_connect} tls:%{time_appconnect} ttfb:%{time_starttransfer} total:%{time_total}\n" https://host/` |
| Through a proxy | `curl -x http://proxy:3128 https://host/` |

## openssl

```text
openssl s_client -connect host:443 -servername host -alpn h2 -showcerts </dev/null
echo | openssl s_client -connect host:443 -servername host 2>/dev/null | openssl x509 -noout -subject -issuer -dates -ext subjectAltName
openssl s_client -connect host:443 -tls1_2      # test a specific version
openssl x509 -in cert.pem -noout -text
openssl verify -CAfile chain.pem cert.pem
```

## Status codes

| Code | Meaning |
|---|---|
| 301/308 | Permanent redirect |
| 302/307 | Temporary redirect |
| 304 | Not modified |
| 401 / 403 | Unauthenticated / forbidden |
| 429 | Rate limited |
| 502 | Bad gateway (upstream error/reset) |
| 503 | No healthy upstream / overloaded |
| 504 | Upstream timeout |

## Headers to know

| Header | Purpose |
|---|---|
| Host | Virtual host (HTTP/2: `:authority`) |
| X-Forwarded-For / -Proto | Original client IP / scheme behind a proxy |
| Cache-Control, Age, ETag, Vary | Caching |
| Strict-Transport-Security | Force HTTPS (HSTS) |
| Alt-Svc | Advertises HTTP/3 |
| Connection: keep-alive | Reuse TCP (HTTP/1.1) |

## Versions

| | Transport | Multiplexing | HOL blocking |
|---|---|---|---|
| HTTP/1.1 | TCP | No (one request at a time per connection) | Yes |
| HTTP/2 | TCP + TLS (h2) | Yes | Yes (TCP level) |
| HTTP/3 | QUIC (UDP) | Yes | No (per stream) |

## TLS 1.3

1-RTT handshake · ECDHE only · AEAD ciphers only (AES-GCM, ChaCha20-Poly1305) · encrypted certificate · 0-RTT on resumption.

## AWS load balancers

| | ALB | NLB | GWLB |
|---|---|---|---|
| Layer | 7 | 4 | 3 (GENEVE 6081) |
| Protocols | HTTP, HTTPS, gRPC, WebSocket | TCP, UDP, TLS, QUIC | IP |
| Client IP | X-Forwarded-For | Preserved | Preserved |
| Static IP | No (use GA) | Yes (EIP per AZ) | — |
