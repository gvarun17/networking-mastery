# Certification Recommendation and CCNA 200-301 Prep Track

Facts below were checked on the issuers' sites on **24 November 2026**. Exam details change, so check the source links again before you book.

## 1. Comparison

| | Cisco CCNA (200-301) | CompTIA Network+ (N10-009) | Juniper JNCIA-Junos | AWS Advanced Networking – Specialty (ANS-C01) | Free: Cisco NetAcad courses / Fortinet FCF |
|---|---|---|---|---|---|
| **Issuer** | Cisco | CompTIA | Juniper | AWS | Cisco Networking Academy / Fortinet |
| **Current version** | v1.1 until **2 Feb 2027**; **v2.0 from 3 Feb 2027** | V9 (N10-009, launched June 2024) | **JN0-106** (replaced JN0-105 in April 2026) | ANS-C01, **last exam date 31 Dec 2026**; no successor announced | NetAcad: Networking Basics, CCNA 1-3; Fortinet Certified Fundamentals (NSE 1 + NSE 2) |
| **Cost (USD)** | $300 | About $390-400 list (CompTIA raised prices on 1 June 2026; resellers vary) | About $200-250 (varies by region) | $300 | Free |
| **Cost (INR, est.)** | ≈ ₹26,400 + 18% GST | ≈ ₹34,000-35,000 | ≈ ₹17,500-22,000 | ≈ ₹26,400 + GST | ₹0 |
| **Format** | 120 min; multiple choice, drag-and-drop, simulations (question count not published) | Max 90 questions, MCQ + performance-based, 90 min | 65 MCQ, 90 min | 65 questions (50 scored), MCQ/multi-response/matching, 170 min | Online quizzes/exams |
| **Validity** | 3 years | 3 years (CE program) | 3 years | 3 years | FCF: 2 years; NetAcad course badges do not expire |
| **Industry recognition** | Very high; the reference associate cert | High, vendor-neutral, common in HR filters | Medium (strong in SP and Juniper shops) | High for AWS network specialists | Low–medium (good starter) |
| **Relevance to DevOps/Cloud** | High: fundamentals + v2.0 adds Ansible and AI ops | Medium: broad but shallow | Low–medium | Very high, but retiring | Low |
| **Prep time (1.5 h/day, your profile)** | 14-16 weeks | 8-10 weeks | 5-6 weeks | 6-8 weeks (if you had time before retirement) | 2-4 weeks |
| **Lab requirements** | Packet Tracer (free) + optional CML/real gear | Any lab; simulations are generic | vLabs / vSRX trial | AWS account (paid usage) | None |

## 2. Recommendation

**Primary: Cisco CCNA 200-301 v2.0.**

1. It fixes exactly the gaps in your profile: OSI, subnetting, switching, routing protocols and packet-level troubleshooting.
2. It is the most recognized associate networking certification, so it carries weight in interviews for cloud network, platform and SRE roles.
3. Timing: your 12-week curriculum plus a 4-week sprint ends in March 2027. v1.1 cannot be taken after 2 Feb 2027, so plan for **v2.0** from day one. Cisco itself advises new learners who cannot test before the cutoff to plan for v2.0.
4. v2.0 rewards hands-on skill (troubleshooting, Ansible, operations), which suits a DevOps engineer.

**Follow-up: Cisco CCNA Automation (200-901 CCNAAUTO v1.1).** $300, 120 minutes. It covers software development and design, APIs, Cisco platforms, application deployment and security, and infrastructure and automation (Ansible, Terraform, NSO). It builds directly on Module 16 and your Python/CI/CD background.

**Not recommended now:** AWS ANS-C01, because AWS retires it after 31 Dec 2026, which is too soon to prepare well. Network+ overlaps heavily with CCNA and adds less. JNCIA-Junos is valuable only if your employer uses Juniper.

## 3. CCNA v2.0 at a glance

| Domain | Weight |
|---|---|
| 1.0 Network Infrastructure and Connectivity | 25% |
| 2.0 Switching and Network Access | 25% |
| 3.0 IP Routing | 20% |
| 4.0 Network Services and Security | 20% |
| 5.0 AI, and Network Operations and Management | 10% |

Full mapping to the modules: [blueprint.md](blueprint.md).

## 4. This prep track

| File | Purpose |
|---|---|
| [blueprint.md](blueprint.md) | Every v2.0 exam topic mapped to modules, with weights (v1.1 included for reference) |
| [study-plan.md](study-plan.md) | 16-week plan: 12 curriculum weeks with daily cert tasks, then a 4-week sprint |
| [domain-notes/](domain-notes/README.md) | One condensed notes file per domain |
| [practice-exams/](practice-exams/exam-1.md) | 3 full practice exams × 100 original questions |
| [labs/](labs/README.md) | Exam-style CLI simulations |
| [flashcards.csv](flashcards.csv) | 300+ Anki cards (front, back, tags) |
| [exam-day.md](exam-day.md) | Registration, cost, policies, time management, last-7-days plan |
| [resources.md](resources.md) | Official and free resources only |

## Sources

- Cisco CCNA v2.0 exam topics (PDF): <https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301_CCNA_v2.0_Exam_Topics_PDF.pdf>
- Cisco Learning Network, CCNA exam topics: <https://learningnetwork.cisco.com/s/ccna-exam-topics>
- Cisco blog, CCNA v2.0 dates and v1.1 last day: <https://blogs.cisco.com/learning/ai-updates-ccna-ccie-automation> and <https://blogs.cisco.com/learning/stay-on-track-get-certified-before-the-ccna-refresh>
- Cisco exam pricing: <https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/faq.html>
- Cisco CCNA Automation exam and price: <https://www.cisco.com/site/us/en/learn/training-certifications/certifications/automation/ccna-automation/exams-and-training.html> and exam topics <https://learningcontent.cisco.com/documents/marketing/exam-topics/200-901-CCNAAUTO_v.1.1.pdf>
- CompTIA Network+ (V9, N10-009): <https://www.comptia.org/en-us/certifications/network/>
- Juniper JNCIA-Junos: <https://www.juniper.net/us/en/training/certification/tracks/junos/jncia-junos.html>
- AWS Advanced Networking – Specialty: <https://aws.amazon.com/certification/certified-advanced-networking-specialty/> and exam guide <https://docs.aws.amazon.com/aws-certification/latest/advanced-networking-specialty-01/advanced-networking-specialty-01.html>
- Fortinet NSE certification program: <https://www.fortinet.com/training-certification>
- Cisco Networking Academy: <https://www.netacad.com/>
