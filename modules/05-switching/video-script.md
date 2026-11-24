# Video Script 05 — "VLANs, Trunks and Spanning Tree: Keeping Layer 2 Sane"

**Length:** about 8 minutes.

| # | Time | Visual | Narration |
|---|---|---|---|
| 1 | 0:00-0:40 | Animation: one broadcast reaches 500 PCs on a flat network. | "On a flat network, every broadcast reaches every host. VLANs fix that. Spanning tree keeps redundant links from destroying the network." |
| 2 | 0:40-1:40 | Diagram: two switches, access ports and a trunk. | "An access port carries one VLAN, untagged. A trunk carries many VLANs. Each frame gets a 4-byte tag with a 12-bit VLAN ID." |
| 3 | 1:40-2:20 | Diagram: 802.1Q tag fields. | "The tag sits after the source MAC. TPID 0x8100, three priority bits, and the VLAN ID. One VLAN, the native VLAN, stays untagged. Match it on both ends." |
| 4 | 2:20-3:00 | Animation: broadcast storm on a triangle of switches. MAC table flapping. | "Add a redundant link and you add a loop. Ethernet has no TTL. A broadcast loops forever. That is a broadcast storm." |
| 5 | 3:00-4:30 | Diagram: STP election triangle. Highlight root, root ports, designated, alternate. | "STP elects a root: lowest priority, then lowest MAC. Every other switch picks the cheapest path to the root: its root port. Each link gets one designated port. Everything else blocks." |
| 6 | 4:30-5:15 | Packet Tracer: `show spanning-tree vlan 10`. | "Here is the real output. The root says 'This bridge is the root'. On SW3, one port is Altn BLK. That is the blocked link." |
| 7 | 5:15-6:00 | Table: PortFast, BPDU guard, root guard, loop guard. | "Protect the tree. PortFast on host ports. BPDU guard to kill rogue switches. Root guard to keep the root where you put it. Loop guard for one-way links." |
| 8 | 6:00-7:00 | Diagram: two links bundled into Po1. `show etherchannel summary`. | "EtherChannel bundles links so STP sees one link and nothing blocks. Use LACP active on at least one side. All members must match." |
| 9 | 7:00-8:00 | Port security config; then AWS slide. | "Port security limits MACs per port. In AWS none of this exists: no broadcast, no loops. But Direct Connect still uses LACP for link aggregation." |

## Diagrams to show

1. VLAN/trunk topology.
2. 802.1Q tag.
3. STP election triangle.
