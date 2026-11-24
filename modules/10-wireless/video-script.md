# Video Script 10 — "Wi-Fi for Engineers: Bands, Controllers and WPA3"

**Length:** about 6 minutes.

| # | Time | Visual | Narration |
|---|---|---|---|
| 1 | 0:00-0:30 | Office floor map with AP icons. | "Wi-Fi is Ethernet over a shared radio. Only one device per channel talks at a time. Design is about sharing airtime." |
| 2 | 0:30-1:30 | Band diagram: 2.4, 5, 6 GHz. | "2.4 gigahertz goes far but has only three clean channels: 1, 6, 11. 5 gigahertz has many more. 6 gigahertz is clean, short range, and requires WPA3." |
| 3 | 1:30-2:15 | dBm scale animation. Interference sources. | "Signal is in dBm. Closer to zero is better. Plus 3 dB doubles power. Interference comes from neighbours on the same channel, microwaves and walls." |
| 4 | 2:15-3:30 | Diagram: association + 4-way handshake sequence. | "A client hears beacons, associates, authenticates, then runs the 4-way handshake to create encryption keys. Enterprise networks add 802.1X with a RADIUS server." |
| 5 | 3:30-4:15 | Security comparison table. | "WEP and TKIP are broken. WPA2 uses AES but its PSK can be guessed offline. WPA3 uses SAE and makes management frame protection mandatory." |
| 6 | 4:15-5:15 | Diagram: CAPWAP architecture. Packet Tracer WLC screen. | "In enterprises, lightweight APs tunnel to a controller over CAPWAP UDP 5246 and 5247. FlexConnect keeps branch traffic local." |
| 7 | 5:15-6:00 | Troubleshooting flowchart. | "When Wi-Fi fails, go in order: SSID, authentication, DHCP, gateway, then RF quality." |

## Diagrams to show

1. Bands and channels.
2. Association + 4-way handshake.
3. CAPWAP architecture.
4. Troubleshooting flowchart.
