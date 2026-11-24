# Cisco Packet Tracer Setup (for the IOS CLI labs)

Packet Tracer is free with a Cisco Networking Academy account. Use it for the Cisco IOS labs (Modules 05, 09, 10, 11 and the CCNA sims), because the exam uses IOS syntax.

## Install

1. Create a free account at [Cisco Networking Academy](https://www.netacad.com/).
2. Enrol in the free "Getting Started with Cisco Packet Tracer" course. The download link is in the course resources (or the "Resources → Download Packet Tracer" page).
3. Download version **8.2.2 or later** for your OS:
   - **Windows:** run the `.exe` installer. This is the easiest option if you use WSL2 for the Linux labs.
   - **Ubuntu (native):** `sudo apt install ./CiscoPacketTracer_822_Ubuntu_64bit.deb`. If it fails with missing libraries, run `sudo apt -f install`.
4. Start Packet Tracer and log in with your NetAcad account (needed once, then it works offline for a period).

## Which labs use Packet Tracer

| Lab | Devices |
|---|---|
| Module 05 switching | 2960 switches, 3650 multilayer switch |
| Module 09 DHCP relay and PAT | ISR 4331 routers, server |
| Module 10 wireless | WLC-2504, 3702i LAP, laptops |
| Module 11 ACL and DHCP snooping | ISR routers, 2960 switch |
| CCNA sims (`cert/ccna-200-301/labs/`) | Mixed |
| Capstone 1 (3-site enterprise) | ISR routers, 3650, 2960 |

## Tips

- Use **Simulation mode** to watch packets hop by hop and open each PDU's OSI view. It is a good way to review Module 01 encapsulation.
- Save often. Name files `lab05-switching-<date>.pkt`.
- Packet Tracer simulates IOS. A few commands from real IOS XE are missing. If a command is rejected, try the IOS 15 equivalent or skip it and note it.
- Packet Tracer does not support some v2.0 topics well (for example WPA3, RA guard, Ansible). Practise those with the Linux/Containerlab labs and the reference configs.

## Free alternatives for IOS practice

| Tool | Notes |
|---|---|
| GNS3 + your own IOS images | Free software; you need legal images (not included) |
| EVE-NG Community | Free; same image requirement |
| Cisco Modeling Labs Free tier | Free tier with a node limit; requires a Cisco account |
| Cisco DevNet Sandboxes | Free reservable IOS XE / NX-OS devices in the cloud |
