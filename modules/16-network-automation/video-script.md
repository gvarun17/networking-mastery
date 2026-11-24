# Video Script 16 — "Network as Code: From SSH Scripts to GitOps"

**Length:** about 8 minutes.

| # | Time | Visual | Narration |
|---|---|---|---|
| 1 | 0:00-0:30 | 200 terminal windows with `conf t`. | "Typing the same change on 200 switches is slow and risky. You already know how to treat infrastructure as code. Networks work the same way." |
| 2 | 0:30-1:30 | Management approaches table; controller diagram. | "Five approaches: device by device, cloud dashboards, controllers with northbound APIs, automation tools, and full infrastructure as code." |
| 3 | 1:30-3:00 | Netmiko and Nornir code; lab step 2 output. | "Netmiko speaks SSH to almost anything. Nornir runs tasks across your whole inventory in parallel. Same Python you use every day." |
| 4 | 3:00-4:30 | Diagram: YANG → NETCONF/RESTCONF/gNMI. Lab step 4 XML vs JSON. | "Screen scraping is fragile. YANG models give structured data. NETCONF carries it as XML over SSH, RESTCONF as JSON over HTTPS, gNMI as protobuf over gRPC, with streaming telemetry." |
| 5 | 4:30-5:30 | Ansible playbook; two runs: changed=1 then changed=0. | "Ansible is agentless and, with resource modules, idempotent. The second run changes nothing." |
| 6 | 5:30-6:45 | Diagram: GitOps pipeline. | "GitOps for networks: intent in Git, configs rendered by templates, tested in CI with Batfish and Containerlab, deployed with replace and confirmed commit, then verified and watched for drift." |
| 7 | 6:45-7:30 | Prompt table; agent diagram with approval gate. | "AI is now on the CCNA. Agents call tools to investigate. Keep them read-only by default. When you prompt, respect data classification, set a persona, give instructions and an output format." |
| 8 | 7:30-8:00 | Capstone 5 preview. | "In Capstone 5 you build the full pipeline: Nornir, GitHub Actions and config validation." |

## Diagrams to show

1. Controller architecture.
2. YANG and the three protocols.
3. GitOps pipeline.
