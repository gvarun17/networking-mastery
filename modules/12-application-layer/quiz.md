# Quiz 12 — Application Layer

## Questions

### Q1. Which HTTP status code does a load balancer return when the backend sends an invalid response or resets the connection?

- A) 404
- B) 503
- C) 502
- D) 504

<details><summary>Answer</summary>

**Answer: C.** 502 Bad Gateway. 503 = no healthy backend/overloaded, 504 = backend timeout.

</details>

### Q2. What problem did HTTP/2 solve compared with HTTP/1.1?

- A) It multiplexes many requests as streams over one connection, with header compression
- B) It made HTTP stateful
- C) It removed TLS
- D) It removed TCP

<details><summary>Answer</summary>

**Answer: A.** HTTP/2 uses binary framing, many concurrent streams per connection and HPACK. It still runs on TCP, so packet loss blocks all streams.

</details>

### Q3. Which transport does HTTP/3 use?

- A) SCTP
- B) Raw IP
- C) TCP
- D) QUIC over UDP

<details><summary>Answer</summary>

**Answer: D.** HTTP/3 maps HTTP semantics onto QUIC streams over UDP.

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

- A) It tells the server which hostname the client wants, so the server can present the right certificate
- B) It negotiates HTTP/2
- C) It chooses the cipher suite
- D) It encrypts the certificate

<details><summary>Answer</summary>

**Answer: A.** SNI allows many HTTPS sites on one IP. ALPN negotiates the application protocol.

</details>

### Q6. Scenario: `curl` reports `unable to get local issuer certificate` for your site, but browsers work. What is the most likely cause?

- A) DNS is wrong
- B) HTTP/2 is disabled
- C) The certificate expired
- D) The server does not send the intermediate certificate; browsers fetch it themselves but curl does not

<details><summary>Answer</summary>

**Answer: D.** Always serve the full chain (leaf + intermediates). Browsers can use AIA fetching or caches and hide the problem.

</details>

### Q7. Which TWO features require an L7 load balancer? (Choose two.)

- A) Preserving the client source IP at the packet level
- B) Load balancing UDP DNS traffic
- C) Distributing TCP connections by 5-tuple hash
- D) Inserting an X-Forwarded-For header
- E) Routing by URL path

<details><summary>Answer</summary>

**Answer: D, E.** Path routing and HTTP header changes need HTTP awareness. 5-tuple hashing, UDP and source IP preservation are L4 features (NLB).

</details>

### Q8. Which AWS load balancer preserves the client IP and supports UDP?

- A) CloudFront
- B) Application Load Balancer
- C) Classic Load Balancer
- D) Network Load Balancer

<details><summary>Answer</summary>

**Answer: D.** NLB is L4, supports TCP/UDP/TLS and preserves the source IP (with instance or IP targets, depending on settings).

</details>

### Q9. Scenario: Behind an ALB, a Node.js service shows random 502 errors under low traffic. Its keep-alive timeout is 5 seconds; the ALB idle timeout is 60 seconds. What is the fix?

- A) Use HTTP/1.0
- B) Disable health checks
- C) Set the backend keep-alive timeout higher than the ALB idle timeout
- D) Lower the ALB idle timeout to 1 second

<details><summary>Answer</summary>

**Answer: C.** The ALB reuses idle connections that the backend has already closed. The backend's keep-alive must outlive the ALB's idle timeout.

</details>

### Q10. Which header shows how many seconds a response has been stored in a cache?

- A) Cache-Control
- B) Vary
- C) ETag
- D) Age

<details><summary>Answer</summary>

**Answer: D.** `Age` shows time in cache. `Cache-Control` sets policy, `ETag` identifies a version, `Vary` adds headers to the cache key.

</details>

### Q11. What is a reverse proxy?

- A) A proxy that clients configure to reach the internet
- B) A proxy that only handles DNS
- C) A NAT gateway
- D) A proxy in front of servers that receives client requests on their behalf

<details><summary>Answer</summary>

**Answer: D.** Reverse proxies (NGINX, Envoy, ALB) front servers. Forward proxies (Squid) act for clients.

</details>

### Q12. Which mechanism lets a client and server agree on HTTP/2 during the TLS handshake?

- A) HSTS
- B) SNI
- C) ALPN
- D) OCSP stapling

<details><summary>Answer</summary>

**Answer: C.** Application-Layer Protocol Negotiation.

</details>

### Q13. Why does TLS 1.3 always provide forward secrecy?

- A) It uses static RSA key exchange
- B) It uses 4096-bit keys
- C) It disables encryption after the handshake
- D) It allows only ephemeral (EC)DHE key exchange

<details><summary>Answer</summary>

**Answer: D.** Static RSA key exchange was removed. Session keys come from ephemeral Diffie-Hellman, so a stolen private key cannot decrypt recorded traffic.

</details>

### Q14. Scenario: Users still see an old version of a JavaScript file after a deployment. The file is served through CloudFront with `Cache-Control: max-age=86400`. What are the TWO best fixes? (Choose two.)

- A) Restart the origin server
- B) Change the DNS TTL
- C) Use versioned file names (e.g. app.3f9a.js) in future deployments
- D) Disable HTTPS
- E) Create a CloudFront invalidation for the path

<details><summary>Answer</summary>

**Answer: C, E.** An invalidation removes the cached object now; content-hashed file names avoid the problem permanently.

</details>

### Q15. Which command shows the TLS version, cipher and negotiated ALPN for a server?

- A) `ss -tlnp`
- B) `dig example.com`
- C) `traceroute example.com`
- D) `openssl s_client -connect example.com:443 -servername example.com -alpn h2`

<details><summary>Answer</summary>

**Answer: D.** `openssl s_client` performs a real handshake and prints protocol, cipher, certificate chain and ALPN.

</details>
