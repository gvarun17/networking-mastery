# Quiz 10 — Wireless

### Q1. Which 2.4 GHz channels do not overlap in North America and India?
- A) 1, 5, 9
- B) 1, 6, 11
- C) 2, 7, 12
- D) 1, 4, 8, 11

<details><summary>Answer</summary>

**Answer: B.** With 20-22 MHz wide channels spaced 5 MHz apart, only 1, 6 and 11 avoid overlap.

</details>

### Q2. Which media access method does 802.11 use?
- A) CSMA/CD
- B) CSMA/CA
- C) Token passing
- D) TDMA only

<details><summary>Answer</summary>

**Answer: B.** Wireless stations cannot detect collisions while transmitting, so they avoid them with carrier sense, random backoff and ACKs (CSMA/CA).

</details>

### Q3. What does WPA3-Personal use instead of the WPA2 pre-shared key handshake?
- A) TKIP
- B) SAE (Simultaneous Authentication of Equals)
- C) WEP
- D) EAP-TLS

<details><summary>Answer</summary>

**Answer: B.** SAE resists offline dictionary attacks and provides forward secrecy.

</details>

### Q4. Which statement about 6 GHz Wi-Fi (Wi-Fi 6E) is correct?
- A) It allows WEP
- B) It requires WPA3 (or OWE) security
- C) It has only three channels
- D) It has longer range than 2.4 GHz

<details><summary>Answer</summary>

**Answer: B.** 6 GHz operation requires WPA3 or Enhanced Open (OWE) with PMF. It has many channels but the shortest range.

</details>

### Q5. Which ports does CAPWAP use between a lightweight AP and a WLC?
- A) TCP 5246 and 5247
- B) UDP 5246 (control) and UDP 5247 (data)
- C) UDP 1812 and 1813
- D) TCP 22 and 443

<details><summary>Answer</summary>

**Answer: B.** CAPWAP control is UDP 5246 (DTLS encrypted) and data is UDP 5247. 1812/1813 are RADIUS.

</details>

### Q6. Which AP mode switches client traffic locally at a branch and can keep working if the WAN link to the WLC fails?
- A) Local
- B) Monitor
- C) FlexConnect
- D) Sniffer

<details><summary>Answer</summary>

**Answer: C.** FlexConnect APs switch data locally and can continue serving clients when the WLC is unreachable.

</details>

### Q7. Scenario: A local-mode AP connects to an access switch. How should the switch port be configured?
- A) Trunk with all client VLANs
- B) Access port in the AP management VLAN
- C) Routed port
- D) Shutdown until the AP joins

<details><summary>Answer</summary>

**Answer: B.** In local mode, all client traffic is tunnelled in CAPWAP to the WLC. The AP needs only its management VLAN. The WLC uplink is the trunk.

</details>

### Q8. Which RSSI value indicates the best signal?
- A) −85 dBm
- B) −72 dBm
- C) −60 dBm
- D) −45 dBm

<details><summary>Answer</summary>

**Answer: D.** RSSI is negative dBm. Closer to zero is stronger, so −45 dBm is best.

</details>

### Q9. An AP increases transmit power by 3 dB. What happens to its power?
- A) It increases by 3%
- B) It doubles
- C) It increases tenfold
- D) It halves

<details><summary>Answer</summary>

**Answer: B.** +3 dB ≈ 2× power. +10 dB = 10× power.

</details>

### Q10. Which TWO are ways a lightweight AP can discover a WLC? (Choose two.)
- A) DHCP option 43
- B) DNS lookup of CISCO-CAPWAP-CONTROLLER.<domain>
- C) OSPF LSA type 5
- D) SNMP trap
- E) BGP community

<details><summary>Answer</summary>

**Answer: A, B.** APs use DHCP option 43, DNS, broadcast on the local subnet, previously known controllers, or a static configuration.

</details>

### Q11. Scenario: Clients connect to the SSID and authenticate, but get 169.254.x.x addresses. Other WLANs work. What is the most likely cause?
- A) Wrong PSK
- B) The WLAN's VLAN is not allowed on the WLC uplink trunk or has no DHCP relay
- C) The AP is in monitor mode
- D) WPA3 is not supported

<details><summary>Answer</summary>

**Answer: B.** Authentication worked, so security is fine. The client's DHCP traffic is dropped in the wired network: missing VLAN on the trunk or no helper address on the SVI.

</details>

### Q12. Which security combination is recommended for corporate laptops today?
- A) WPA2-Personal with TKIP
- B) WEP 128-bit
- C) WPA3-Enterprise with 802.1X EAP-TLS
- D) Open network with MAC filtering

<details><summary>Answer</summary>

**Answer: C.** Certificate-based 802.1X with WPA3-Enterprise gives per-user/device authentication and strong encryption.

</details>

### Q13. What does management frame protection (802.11w/PMF) prevent?
- A) Co-channel interference
- B) Spoofed deauthentication and disassociation attacks
- C) DHCP starvation
- D) Hidden node problems

<details><summary>Answer</summary>

**Answer: B.** PMF authenticates management frames, so attackers cannot easily forge deauth frames to kick clients off. It is mandatory in WPA3.

</details>

### Q14. Which source commonly interferes with the 2.4 GHz band?
- A) Radar
- B) Microwave ovens
- C) Fiber optic cables
- D) 6 GHz APs

<details><summary>Answer</summary>

**Answer: B.** Microwave ovens operate around 2.45 GHz. Radar affects 5 GHz DFS channels.

</details>

### Q15. Which Wi-Fi generation is 802.11ax?
- A) Wi-Fi 4
- B) Wi-Fi 5
- C) Wi-Fi 6
- D) Wi-Fi 7

<details><summary>Answer</summary>

**Answer: C.** 802.11n = Wi-Fi 4, 802.11ac = Wi-Fi 5, 802.11ax = Wi-Fi 6/6E, 802.11be = Wi-Fi 7.

</details>
