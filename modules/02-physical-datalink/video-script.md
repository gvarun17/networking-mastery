# Video Script 02 — "Ethernet, MAC and ARP: The Local Delivery Service"

**Length:** about 7 minutes.

| # | Time | Visual | Narration |
|---|---|---|---|
| 1 | 0:00-0:30 | Photo of a switch with blinking LEDs. | "Before a packet crosses the internet, it must reach the next device. That is the job of Layers 1 and 2." |
| 2 | 0:30-1:30 | Table of media: copper, multimode, single-mode. | "Copper Ethernet stops at 100 metres. Multimode fiber is for short runs inside a building. Single-mode fiber uses lasers and goes for kilometres." |
| 3 | 1:30-2:30 | Diagram: Ethernet frame fields (README). | "This is the Ethernet frame. Destination MAC first, so the switch can decide fast. Then the source MAC, EtherType, payload, and a 4-byte checksum at the end." |
| 4 | 2:30-3:30 | Diagram: switch learn/flood/forward flowchart. | "A switch learns from the source MAC. It forwards using the destination MAC. If it does not know the destination, it floods. Broadcasts always flood." |
| 5 | 3:30-4:45 | Diagram: ARP sequence. Then the lab terminal with tcpdump. | "Your host knows the IP but needs a MAC. It broadcasts an ARP request. The owner replies with a unicast. For off-subnet destinations, your host ARPs for the gateway." |
| 6 | 4:45-5:45 | Diagram: MTU/PMTUD sequence. Show `ping -M do -s 1472`. | "MTU is the largest packet a link carries. If a smaller link is in the path and ICMP is blocked, big packets vanish. Small ones work. That is an MTU black hole." |
| 7 | 5:45-6:30 | `show interfaces` output with CRC and late collisions highlighted. | "Duplex mismatch: one side hard-coded, one side auto. Look for late collisions on one end and CRC errors on the other. Fix: auto on both ends." |
| 8 | 6:30-7:00 | AWS slide: "No broadcast, VPC answers ARP, MTU 9001". | "In AWS, the VPC answers ARP for you and broadcast does not exist. So GARP failover does not work. Use the API instead." |

## Diagrams to show

1. MAC address structure.
2. Ethernet frame.
3. Switch forwarding flowchart.
4. ARP sequence.
5. PMTUD sequence.
