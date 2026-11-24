# Video Script 03 — "Subnetting in 30 Seconds: The Magic Number Method"

**Length:** about 8 minutes.

| # | Time | Visual | Narration |
|---|---|---|---|
| 1 | 0:00-0:30 | Text on screen: `172.16.45.130/21`. A timer starts. | "By the end of this video you will solve this in under 30 seconds, in your head." |
| 2 | 0:30-1:30 | Diagram: network bits vs host bits (README first diagram). | "An IPv4 address has 32 bits. The prefix says how many bits are the network. The rest are hosts. All host bits zero is the network. All ones is broadcast." |
| 3 | 1:30-2:30 | Table: mask values 128 to 255 and block sizes. | "Learn one row: 128, 192, 224, 240, 248, 252, 254, 255. The block size is 256 minus the mask value." |
| 4 | 2:30-4:00 | Diagram: magic-number flowchart. Solve 172.16.45.130/21 step by step on a whiteboard. | "Find the interesting octet: /21 is the third octet, mask 248. Block size 8. Biggest multiple of 8 not above 45 is 40. Network 172.16.40.0. Next network 48, so broadcast 47.255." |
| 5 | 4:00-5:00 | Terminal: `python3 tools/subnet_calc.py info 172.16.45.130/21`. | "Check your work with the calculator in the repo. Then generate unlimited drills with the practice command." |
| 6 | 5:00-6:15 | Diagram: VLSM tree. | "VLSM means different sizes for different needs. Always allocate the largest subnet first, so every block lands on its own boundary." |
| 7 | 6:15-7:15 | Diagram: VPC IP plan tree. | "In AWS, this is not academic. Overlapping VPC CIDRs break peering and Transit Gateway. Plan a hierarchy: company, environment, Region, account. Remember AWS keeps 5 addresses per subnet." |
| 8 | 7:15-8:00 | Timer reappears. Solve a new problem: 10.20.33.200/27. | "Your turn. Pause the video. Network is .192, broadcast .223. Do 20 drills a day for two weeks and this becomes automatic." |

## Diagrams to show

1. Network/host bit split.
2. Magic-number flowchart.
3. VLSM allocation tree.
4. VPC IP plan.
