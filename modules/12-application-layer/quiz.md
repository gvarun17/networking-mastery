# Quiz 12 — Application Layer

## Questions

### Q1. Which HTTP status code does a load balancer return when the backend sends an invalid response or resets the connection?

- A) 404
- B) 502
- C) 503
- D) 504

<details><summary>Answer</summary>

**Answer: B.** 502 Bad Gateway. 503 = no healthy backend/overloaded, 504 = backend timeout.

</details>

### Q2. What problem did HTTP/2 solve compared with HTTP/1.1?

- A) It removed TCP
- B) It multiplexes many requests as streams over one connection, with header compression
- C) It removed TLS
- D) It made HTTP stateful

<details><summary>Answer</summary>

**Answer: B.** HTTP/2 uses binary framing, many concurrent streams per connection and HPACK. It still runs on TCP, so packet loss blocks all streams.

</details>

### Q3. Which transport does HTTP/3 use?

- A) TCP
- B) SCTP
- C) QUIC over UDP
- D) Raw IP

<details><summary>Answer</summary>

**Answer: C.** HTTP/3 maps HTTP semantics onto QUIC streams over UDP.

</details>

### Q4. How many round trips does a full TLS 1.3 handshake add before application data (without 0-RTT)?

- A) 0
- B) 1
- C) 2
- D) 3

<details><summary>Answer</summary>

**Answer: B.** TLS 1.3 needs 1 RTT (TLS 1.2 needed 2). Resumption can offer 0-RTT early data.

</details>

### Q5. What is the purpose of SNI in the TLS ClientHello?

- A) It chooses the cipher suite
- B) It tells the server which hostname the client wants, so the server can present the right certificate
- C) It encrypts the certificate
- D) It negotiates HTTP/2

<details><summary>Answer</summary>

**Answer: B.** SNI allows many HTTPS sites on one IP. ALPN negotiates the application protocol.

</details>

### Q6. Scenario: `curl` reports `unable to get local issuer certificate` for your site, but browsers work. What is the most likely cause?

- A) The certificate expired
- B) The server does not send the intermediate certificate; browsers fetch it themselves but curl does not
- C) DNS is wrong
- D) HTTP/2 is disabled

<details><summary>Answer</summary>

**Answer: B.** Always serve the full chain (leaf + intermediates). Browsers can use AIA fetching or caches and hide the problem.

</details>

### Q7. Which TWO features require an L7 load balancer? (Choose two.)

- A) Routing by URL path
- B) Distributing TCP connections by 5-tuple hash
- C) Inserting an X-Forwarded-For header
- D) Load balancing UDP DNS traffic
- E) Preserving the client source IP at the packet level

<details><summary>Answer</summary>

**Answer: A, C.** Path routing and HTTP header changes need HTTP awareness. 5-tuple hashing, UDP and source IP preservation are L4 features (NLB).

</details>

### Q8. Which AWS load balancer preserves the client IP and supports UDP?

- A) Application Load Balancer
- B) Network Load Balancer
- C) Classic Load Balancer
- D) CloudFront

<details><summary>Answer</summary>

**Answer: B.** NLB is L4, supports TCP/UDP/TLS and preserves the source IP (with instance or IP targets, depending on settings).

</details>

### Q9. Scenario: Behind an ALB, a Node.js service shows random 502 errors under low traffic. Its keep-alive timeout is 5 seconds; the ALB idle timeout is 60 seconds. What is the fix?

- A) Lower the ALB idle timeout to 1 second
- B) Set the backend keep-alive timeout higher than the ALB idle timeout
- C) Disable health checks
- D) Use HTTP/1.0

<details><summary>Answer</summary>

**Answer: B.** The ALB reuses idle connections that the backend has already closed. The backend's keep-alive must outlive the ALB's idle timeout.

</details>

### Q10. Which header shows how many seconds a response has been stored in a cache?

- A) Cache-Control
- B) ETag
- C) Age
- D) Vary

<details><summary>Answer</summary>

**Answer: C.** `Age` shows time in cache. `Cache-Control` sets policy, `ETag` identifies a version, `Vary` adds headers to the cache key.

</details>

### Q11. What is a reverse proxy?

- A) A proxy that clients configure to reach the internet
- B) A proxy in front of servers that receives client requests on their behalf
- C) A proxy that only handles DNS
- D) A NAT gateway

<details><summary>Answer</summary>

**Answer: B.** Reverse proxies (NGINX, Envoy, ALB) front servers. Forward proxies (Squid) act for clients.

</details>

### Q12. Which mechanism lets a client and server agree on HTTP/2 during the TLS handshake?

- A) SNI
- B) ALPN
- C) OCSP stapling
- D) HSTS

<details><summary>Answer</summary>

**Answer: B.** Application-Layer Protocol Negotiation.

</details>

### Q13. Why does TLS 1.3 always provide forward secrecy?

- A) It uses static RSA key exchange
- B) It allows only ephemeral (EC)DHE key exchange
- C) It disables encryption after the handshake
- D) It uses 4096-bit keys

<details><summary>Answer</summary>

**Answer: B.** Static RSA key exchange was removed. Session keys come from ephemeral Diffie-Hellman, so a stolen private key cannot decrypt recorded traffic.

</details>

### Q14. Scenario: Users still see an old version of a JavaScript file after a deployment. The file is served through CloudFront with `Cache-Control: max-age=86400`. What are the TWO best fixes? (Choose two.)

- A) Create a CloudFront invalidation for the path
- B) Use versioned file names (e.g. app.3f9a.js) in future deployments
- C) Restart the origin server
- D) Change the DNS TTL
- E) Disable HTTPS

<details><summary>Answer</summary>

**Answer: A, B.** An invalidation removes the cached object now; content-hashed file names avoid the problem permanently.

</details>

### Q15. Which command shows the TLS version, cipher and negotiated ALPN for a server?

- A) `dig example.com`
- B) `openssl s_client -connect example.com:443 -servername example.com -alpn h2`
- C) `traceroute example.com`
- D) `ss -tlnp`

<details><summary>Answer</summary>

**Answer: B.** `openssl s_client` performs a real handshake and prints protocol, cipher, certificate chain and ALPN.

</details>
