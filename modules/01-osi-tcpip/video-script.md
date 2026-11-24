# Video Script 01 — "Layers: How One Web Request Crosses the Network"

**Length:** about 7 minutes. **Audience:** DevOps engineers. **Tone:** direct, practical.

## Scene list

| # | Time | Visual | Narration |
|---|---|---|---|
| 1 | 0:00-0:30 | You at the terminal. Type `curl https://example.com`. Freeze frame. | "This one command crosses seven layers and many devices. In seven minutes, you will see every header it adds." |
| 2 | 0:30-1:30 | Diagram A: OSI vs TCP/IP side by side. Highlight each layer as you name it. | "Engineers split networking into layers. Each layer solves one problem. Layer 1 sends bits. Layer 2 moves frames to the next device. Layer 3 moves packets across the world. Layer 4 picks the program and makes delivery reliable. The top layers give meaning to the data." |
| 3 | 1:30-2:30 | Diagram B: encapsulation animation. Boxes stack: HTTP, then TCP, then IP, then Ethernet. | "Encapsulation means each layer puts its own header in front of the data. TCP adds ports. IP adds addresses. Ethernet adds MAC addresses and a checksum at the end." |
| 4 | 2:30-3:45 | Screen recording: `tcpdump -e -nn -vv -c 1`. Zoom on each field. Colour-code by layer. | "Here is a real SYN. These are the MAC addresses: Layer 2. Note that the destination MAC is the router, not the server. This is TTL and the IP addresses: Layer 3. These are the ports and flags: Layer 4." |
| 5 | 3:45-4:45 | Diagram C: sequence diagram, host → router → server. Show MACs changing per hop. | "At each router, the Layer 2 header is removed and a new one is built. The IP addresses stay the same. The TTL goes down by one. Remember this rule: MACs are per hop, IPs are end to end." |
| 6 | 4:45-5:45 | Split screen: two captures from the lab, r-eth0 and r-eth1. | "This is the proof from the lab. Same IPs and ports on both sides. Different MACs. TTL 64 becomes 63. The IP checksum changes because the TTL changed." |
| 7 | 5:45-6:30 | Table: symptoms mapped to layers. | "Use the layers as a troubleshooting checklist. Link down: Layer 1. ARP incomplete: Layer 2. No route: Layer 3. Port blocked: Layer 4. HTTP 502: Layer 7." |
| 8 | 6:30-7:00 | AWS console: VPC route table, security group. | "In AWS, the provider runs Layers 1 and 2. You still own Layer 3 routing, Layer 4 security groups and Layer 7 load balancers. Next video: Ethernet, MAC and ARP." |

## Diagrams to show

1. OSI vs TCP/IP mapping (README section 1).
2. Encapsulation flow (README section 2).
3. Host → router → server sequence diagram (README section 2).

## Recording notes

- Record the terminal at 1920x1080 with a 20 pt font.
- Use the same three colours for layers in every video: L2 blue, L3 green, L4 orange.
- Put the lab commands in the video description.
