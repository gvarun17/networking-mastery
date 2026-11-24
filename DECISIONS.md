# Decisions

This file records the choices made where the brief was ambiguous or where facts changed the plan. Each entry has the decision, the reason and the date. Facts were checked on 24 Nov 2026.

| # | Decision | Reason |
|---|---|---|
| D1 | **Primary cert: Cisco CCNA 200-301 v2.0** (not v1.1). | Cisco retires v1.1 after 2 Feb 2027. v2.0 starts on 3 Feb 2027. The 12-week curriculum, started late Nov 2026, ends in mid-Feb 2027, so the learner sits v2.0. The v1.1 domains are also listed in `cert/ccna-200-301/blueprint.md` in case the learner wants to test early. |
| D2 | **Follow-up cert: Cisco CCNA Automation (200-901 v1.1)**, not AWS ANS-C01. | AWS retires ANS-C01. The last test day is 31 Dec 2026, and AWS has not named a successor. CCNA Automation covers Python, APIs, Ansible, Terraform and CI/CD. That fits a DevOps/Cloud role and extends Module 16. |
| D3 | Practice exams have **100 questions in 120 minutes**. | Cisco publishes the duration (120 min) but not the question count. Public candidate reports put it at roughly 100-120 items. 100 items give a domain split that matches the weights exactly (25/25/20/20/10). |
| D4 | Practice exams are **generated** from a hand-written question bank plus computed questions (subnetting, STP, LPM, wildcards). | Computed questions are correct by construction. A fixed random seed makes each exam stable between builds. Run `python3 tools/build_practice_exams.py`. |
| D5 | Simulations (drag-and-drop, testlets, CLI sims) are given as **Packet Tracer and Containerlab tasks** in `cert/ccna-200-301/labs/`. | Markdown cannot reproduce the exam simulator. A real CLI is better practice. |
| D6 | Default lab images: **FRRouting and Nokia SR Linux**. Arista cEOS is optional. | FRR and SR Linux pull freely from public registries. cEOS needs an Arista account and a manual image import. Every cEOS step has an FRR alternative. |
| D7 | Cisco IOS labs use **Packet Tracer 8.2+**. | The exam uses IOS syntax. Packet Tracer is free with a Cisco NetAcad account. Cisco IOL/CML are not free. |
| D8 | AWS labs use **real AWS free-tier resources with Terraform**, plus **LocalStack** where it works. | LocalStack Community does not emulate Transit Gateway routing, PrivateLink data paths, Direct Connect or Network Firewall. Every AWS lab lists its cost and has a `terraform destroy` step. |
| D9 | Kubernetes labs use **kind** with Cilium or Calico. | kind is free, starts in under a minute and lets you disable the default CNI. |
| D10 | 18 modules in 12 weeks: **about 1.5 modules per week**. Lighter modules share a week. | See the week column in `README.md`. |
| D11 | Mermaid is validated with the **mermaid parser** (Node, `tools/validate_mermaid.mjs`). | It runs in CI without a headless browser and catches all syntax errors. |
| D12 | The GitHub push was **not done** from the build environment. | Repo creation and push access were not granted in the build session. The repo is delivered as a git bundle with all per-module commits. Push it with the steps in the final report. |
| D13 | Commits are authored as `Varun <gvarun17@users.noreply.github.com>` with a Claude co-author trailer. | The repo belongs to the learner. The noreply address keeps the real email private. Change it with `git commit --amend --reset-author` if needed. |
| D14 | Prices are in USD, with INR estimated at about ₹88/USD before 18% GST. | Pearson VUE in India charges in USD. The bank sets the rate on the day you pay. |
| D15 | ASD-STE100 is applied to explanations and procedures. Code, command output, RFC titles and quoted exam topic names keep their original wording. | Changing technical output or official names would make them wrong. |
