# Cheatsheet 10 — Wireless

## Standards

| IEEE | Name | Bands |
|---|---|---|
| 802.11b/g | — | 2.4 |
| 802.11a | — | 5 |
| 802.11n | Wi-Fi 4 | 2.4/5 |
| 802.11ac | Wi-Fi 5 | 5 |
| 802.11ax | Wi-Fi 6/6E | 2.4/5/6 |
| 802.11be | Wi-Fi 7 | 2.4/5/6 |

## RF numbers

| Item | Value |
|---|---|
| 2.4 GHz non-overlapping | 1, 6, 11 |
| Good RSSI for voice | −67 dBm or better |
| Good SNR | ≥ 25 dB |
| +3 dB / +10 dB | 2× / 10× power |
| Channel widths | 20, 40, 80, 160, 320 (Wi-Fi 7) MHz |

## Security

| | Personal | Enterprise | Cipher |
|---|---|---|---|
| WPA2 | PSK | 802.1X/EAP | AES-CCMP |
| WPA3 | SAE | 802.1X/EAP (192-bit option) | AES-CCMP/GCMP, PMF required |
| Enhanced Open | OWE | — | AES |

## Ports

| Protocol | Port |
|---|---|
| CAPWAP control / data | UDP 5246 / 5247 |
| RADIUS auth / acct | UDP 1812 / 1813 |
| TACACS+ | TCP 49 |

## AP modes

Local · FlexConnect · Monitor · Sniffer · SE-Connect · Bridge/Mesh

## WLC discovery

DHCP option 43 · DNS `CISCO-CAPWAP-CONTROLLER.<domain>` · L2/L3 broadcast · primed controller list

## Troubleshooting order

SSID visible → association/auth → DHCP → gateway/DNS → RF quality (RSSI, SNR, utilization, roaming)

## Client-side commands

| OS | Command |
|---|---|
| Windows | `netsh wlan show interfaces`, `netsh wlan show wlanreport` |
| macOS | Option-click Wi-Fi icon; `wdutil info` |
| Linux | `iw dev wlan0 link`, `nmcli dev wifi list` |
