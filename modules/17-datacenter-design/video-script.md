# Video Script 17 — "Spine-Leaf and EVPN: How Modern Data Centers Work"

**Length:** about 7 minutes.

| # | Time | Visual | Narration |
|---|---|---|---|
| 1 | 0:00-0:30 | Old three-tier diagram with blocked links in red. | "Old data centers blocked half their links with spanning tree. Modern ones use every link." |
| 2 | 0:30-1:45 | Diagram: three-tier vs spine-leaf. | "Spine-leaf: every leaf to every spine. Two hops between any servers. All links routed, all active with ECMP. Add spines for bandwidth, leaves for ports." |
| 3 | 1:45-2:30 | Oversubscription calculation on screen. | "Oversubscription is downlink over uplink. 1200 gigabits down, 400 up: 3 to 1. AI fabrics want 1 to 1." |
| 4 | 2:30-3:30 | Diagram: VXLAN header stack. | "VXLAN wraps an Ethernet frame in UDP 4789 with a 24-bit VNI. 50 bytes of overhead, so use jumbo MTU in the fabric." |
| 5 | 3:30-5:00 | Diagram: EVPN learning sequence. Lab step 3 output. | "EVPN is BGP for MAC addresses. Type 3 says 'I am in VNI 100'. Type 2 says 'this MAC is behind me'. No flood and learn." |
| 6 | 5:00-5:45 | Lab step 4 tcpdump on spine. | "The spine sees only VTEP-to-VTEP UDP. It knows nothing about tenant networks." |
| 7 | 5:45-6:30 | SD-WAN diagram. | "SD-WAN builds an overlay over any transport and picks the path per application, based on measured loss, latency and jitter." |
| 8 | 6:30-7:00 | SDN planes diagram. | "SDN separates the control plane from forwarding. AWS VPC is the largest SDN you use every day." |

## Diagrams to show

1. Three-tier vs spine-leaf.
2. VXLAN header stack.
3. EVPN learning sequence.
4. SD-WAN components.
