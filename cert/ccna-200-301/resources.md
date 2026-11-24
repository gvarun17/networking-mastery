# Official and Free Resources

Only issuer documentation, standards and free courses. No brain dumps.

## Cisco (official)

| Resource | Link | Use |
|---|---|---|
| CCNA v2.0 exam topics (PDF) | <https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301_CCNA_v2.0_Exam_Topics_PDF.pdf> | The source of truth |
| Cisco Learning Network – CCNA exam topics | <https://learningnetwork.cisco.com/s/ccna-exam-topics> | Topic pages, community |
| Exam pricing and policies FAQ | <https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/faq.html> | Price, recertification, policies |
| Pearson VUE for Cisco | <https://home.pearsonvue.com/cisco> | Booking, OnVUE requirements |
| Cisco U. (free tier, tutorials, exam topic videos) | <https://u.cisco.com/> | Free tutorials and some free paths |
| Cisco Networking Academy (free courses, Packet Tracer) | <https://www.netacad.com/> | Packet Tracer download, free courses |
| Cisco DevNet sandboxes (free IOS XE/NX-OS labs) | <https://developer.cisco.com/site/sandbox/> | Real IOS XE for sims and Ansible |
| CCNA Automation (follow-up) exam topics | <https://learningcontent.cisco.com/documents/marketing/exam-topics/200-901-CCNAAUTO_v.1.1.pdf> | Next certification |

## Standards (RFCs)

| Topic | RFC |
|---|---|
| IPv4 / ICMP / TCP / UDP | [791](https://www.rfc-editor.org/rfc/rfc791), [792](https://www.rfc-editor.org/rfc/rfc792), [9293](https://www.rfc-editor.org/rfc/rfc9293), [768](https://www.rfc-editor.org/rfc/rfc768) |
| ARP / private addressing / CIDR | [826](https://www.rfc-editor.org/rfc/rfc826), [1918](https://www.rfc-editor.org/rfc/rfc1918), [4632](https://www.rfc-editor.org/rfc/rfc4632) |
| IPv6 / addressing / NDP / SLAAC | [8200](https://www.rfc-editor.org/rfc/rfc8200), [4291](https://www.rfc-editor.org/rfc/rfc4291), [4861](https://www.rfc-editor.org/rfc/rfc4861), [4862](https://www.rfc-editor.org/rfc/rfc4862), [5952](https://www.rfc-editor.org/rfc/rfc5952) |
| OSPFv2 / OSPFv3 / BGP-4 | [2328](https://www.rfc-editor.org/rfc/rfc2328), [5340](https://www.rfc-editor.org/rfc/rfc5340), [4271](https://www.rfc-editor.org/rfc/rfc4271) |
| DHCP / DNS / NTP | [2131](https://www.rfc-editor.org/rfc/rfc2131), [1034](https://www.rfc-editor.org/rfc/rfc1034), [1035](https://www.rfc-editor.org/rfc/rfc1035), [5905](https://www.rfc-editor.org/rfc/rfc5905) |
| VRRPv3 / syslog / SNMPv3 | [5798](https://www.rfc-editor.org/rfc/rfc5798), [5424](https://www.rfc-editor.org/rfc/rfc5424), [3414](https://www.rfc-editor.org/rfc/rfc3414) |

The full annotated list is in [reference/rfc-reading-list.md](../../reference/rfc-reading-list.md).

## Free courses and labs

| Resource | Link | Notes |
|---|---|---|
| Cisco NetAcad "Networking Basics", "CCNA: Introduction to Networks" (where offered free) | <https://www.netacad.com/> | Structured, with Packet Tracer activities |
| Jeremy's IT Lab – free CCNA course (YouTube + Packet Tracer labs) | <https://www.youtube.com/@JeremysITLab> | Popular free video course; check it covers v2.0 topics |
| Containerlab documentation and lab examples | <https://containerlab.dev/> | For the FRR/SR Linux labs |
| FRRouting documentation | <https://docs.frrouting.org/> | OSPF, BGP, EVPN configuration |
| Nokia SR Linux learn portal | <https://learn.srlinux.dev/> | Free tutorials, gNMI, automation |
| Ansible network automation docs | <https://docs.ansible.com/ansible/latest/network/> | Network modules and connection types |
| Wireshark user guide | <https://www.wireshark.org/docs/wsug_html_chunked/> | Capture and display filters |

## Practice in this repo

- 18 module quizzes (270 questions): `python3 tools/quiz_runner.py modules --all --limit 50`
- 3 practice exams (300 questions): `cert/ccna-200-301/practice-exams/`
- 9 sims: `cert/ccna-200-301/labs/`
- 300+ flashcards: `cert/ccna-200-301/flashcards.csv`

**Avoid:** "actual exam questions", "dumps" and "latest leaked" products. They violate the Cisco candidate agreement and can get your certification revoked.
