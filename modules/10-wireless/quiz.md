# Quiz 10 — Wireless

## Questions

### Q1. Which 2.4 GHz channels do not overlap in North America and India?

- A) 1, 5, 9
- B) 1, 4, 8, 11
- C) 1, 6, 11
- D) 2, 7, 12

<details><summary>Answer</summary>

**Answer: C.** With 20-22 MHz wide channels spaced 5 MHz apart, only 1, 6 and 11 avoid overlap.

</details>

### Q2. Which media access method does 802.11 use?

- A) CSMA/CA
- B) CSMA/CD
- C) TDMA only
- D) Token passing

<details><summary>Answer</summary>

**Answer: A.** Wireless stations cannot detect collisions while transmitting, so they avoid them with carrier sense, random backoff and ACKs (CSMA/CA).

</details>

### Q3. What does WPA3-Personal use instead of the WPA2 pre-shared key handshake?

- A) WEP
- B) TKIP
- C) EAP-TLS
- D) SAE (Simultaneous Authentication of Equals)

<details><summary>Answer</summary>

**Answer: D.** SAE resists offline dictionary attacks and provides forward secrecy.

</details>

### Q4. Which statement about 6 GHz Wi-Fi (Wi-Fi 6E) is correct?

- A) It allows WEP
- B) It has longer range than 2.4 GHz
- C) It has only three channels
- D) It requires WPA3 (or OWE) security

<details><summary>Answer</summary>

**Answer: D.** 6 GHz operation requires WPA3 or Enhanced Open (OWE) with PMF. It has many channels but the shortest range.

</details>

### Q5. Which ports does CAPWAP use between a lightweight AP and a WLC?

- A) TCP 5246 and 5247
- B) UDP 5246 (control) and UDP 5247 (data)
- C) TCP 22 and 443
- D) UDP 1812 and 1813

<details><summary>Answer</summary>

**Answer: B.** CAPWAP control is UDP 5246 (DTLS encrypted) and data is UDP 5247. 1812/1813 are RADIUS.

</details>

### Q6. Which AP mode switches client traffic locally at a branch and can keep working if the WAN link to the WLC fails?

- A) FlexConnect
- B) Monitor
- C) Sniffer
- D) Local

<details><summary>Answer</summary>

**Answer: A.** FlexConnect APs switch data locally and can continue serving clients when the WLC is unreachable.

</details>

### Q7. Scenario: A local-mode AP connects to an access switch. How should the switch port be configured?

- A) Shutdown until the AP joins
- B) Access port in the AP management VLAN
- C) Trunk with all client VLANs
- D) Routed port

<details><summary>Answer</summary>

**Answer: B.** In local mode, all client traffic is tunnelled in CAPWAP to the WLC. The AP needs only its management VLAN. The WLC uplink is the trunk.

</details>

### Q8. Which RSSI value indicates the best signal?

- A) −72 dBm
- B) −85 dBm
- C) −60 dBm
- D) −45 dBm

<details><summary>Answer</summary>

**Answer: D.** RSSI is negative dBm. Closer to zero is stronger, so −45 dBm is best.

</details>

### Q9. An AP increases transmit power by 3 dB. What happens to its power?

- A) It increases tenfold
- B) It doubles
- C) It halves
- D) It increases by 3%

<details><summary>Answer</summary>

**Answer: B.** +3 dB ≈ 2× power. +10 dB = 10× power.

</details>

### Q10. Which TWO are ways a lightweight AP can discover a WLC? (Choose two.)

- A) DNS lookup of `CISCO-CAPWAP-CONTROLLER.<domain>`
- B) DHCP option 43
- C) SNMP trap
- D) BGP community
- E) OSPF LSA type 5

<details><summary>Answer</summary>

**Answer: A, B.** APs use DHCP option 43, DNS, broadcast on the local subnet, previously known controllers, or a static configuration.

</details>

### Q11. Scenario: Clients connect to the SSID and authenticate, but get 169.254.x.x addresses. Other WLANs work. What is the most likely cause?

- A) The AP is in monitor mode
- B) Wrong PSK
- C) WPA3 is not supported
- D) The WLAN's VLAN is not allowed on the WLC uplink trunk or has no DHCP relay

<details><summary>Answer</summary>

**Answer: D.** Authentication worked, so security is fine. The client's DHCP traffic is dropped in the wired network: missing VLAN on the trunk or no helper address on the SVI.

</details>

### Q12. Which security combination is recommended for corporate laptops today?

- A) WPA3-Enterprise with 802.1X EAP-TLS
- B) Open network with MAC filtering
- C) WEP 128-bit
- D) WPA2-Personal with TKIP

<details><summary>Answer</summary>

**Answer: A.** Certificate-based 802.1X with WPA3-Enterprise gives per-user/device authentication and strong encryption.

</details>

### Q13. What does management frame protection (802.11w/PMF) prevent?

- A) Hidden node problems
- B) DHCP starvation
- C) Spoofed deauthentication and disassociation attacks
- D) Co-channel interference

<details><summary>Answer</summary>

**Answer: C.** PMF authenticates management frames, so attackers cannot easily forge deauth frames to kick clients off. It is mandatory in WPA3.

</details>

### Q14. Which source commonly interferes with the 2.4 GHz band?

- A) Fiber optic cables
- B) Microwave ovens
- C) Radar
- D) 6 GHz APs

<details><summary>Answer</summary>

**Answer: B.** Microwave ovens operate around 2.45 GHz. Radar affects 5 GHz DFS channels.

</details>

### Q15. Which Wi-Fi generation is 802.11ax?

- A) Wi-Fi 5
- B) Wi-Fi 6
- C) Wi-Fi 4
- D) Wi-Fi 7

<details><summary>Answer</summary>

**Answer: B.** 802.11n = Wi-Fi 4, 802.11ac = Wi-Fi 5, 802.11ax = Wi-Fi 6/6E, 802.11be = Wi-Fi 7.

</details>
