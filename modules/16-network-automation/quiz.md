# Quiz 16 — Network Automation

## Questions

### Q1. Which protocol carries YANG-modelled data as XML over SSH on TCP port 830?

- A) RESTCONF
- B) NETCONF
- C) gNMI
- D) SNMP

<details><summary>Answer</summary>

**Answer: B.** NETCONF uses XML RPCs over SSH (830). RESTCONF uses HTTPS; gNMI uses gRPC.

</details>

### Q2. Which HTTP method should you use in RESTCONF to replace a whole resource with the body you send?

- A) GET
- B) POST
- C) PUT
- D) PATCH

<details><summary>Answer</summary>

**Answer: C.** PUT replaces (create or replace). PATCH merges changes. POST creates a child resource.

</details>

### Q3. What is YANG?

- A) A transport protocol
- B) A data modelling language that describes configuration and state as a typed tree
- C) A Python library
- D) An encryption standard

<details><summary>Answer</summary>

**Answer: B.** YANG defines the schema; NETCONF/RESTCONF/gNMI carry data that conforms to it.

</details>

### Q4. Which gNMI RPC streams telemetry from a device?

- A) Get
- B) Set
- C) Subscribe
- D) Capabilities

<details><summary>Answer</summary>

**Answer: C.** Subscribe supports sample and on-change streaming.

</details>

### Q5. What does "idempotent" mean for a configuration tool?

- A) It runs faster each time
- B) Running it many times gives the same end state and changes nothing when the state already matches
- C) It always reboots the device
- D) It needs an agent on the device

<details><summary>Answer</summary>

**Answer: B.** An idempotent run reports no changes when the desired state is already present.

</details>

### Q6. Which statement about Ansible is correct?

- A) It needs an agent installed on every network device
- B) It is agentless and pushes changes over SSH or APIs
- C) It works only with Linux servers
- D) It requires a database

<details><summary>Answer</summary>

**Answer: B.** Ansible connects from a control node using network_cli (SSH), netconf or httpapi.

</details>

### Q7. Which Python library is a framework that runs tasks in parallel against an inventory and uses plugins such as Netmiko and NAPALM?

- A) Requests
- B) Nornir
- C) Paramiko
- D) Flask

<details><summary>Answer</summary>

**Answer: B.** Nornir provides inventory, filtering, threading and result handling in pure Python.

</details>

### Q8. Which NAPALM capability supports safe full-config deployment?

- A) `get_facts`
- B) `load_replace_candidate` followed by `compare_config` and `commit_config` (with rollback)
- C) `ping`
- D) `get_arp_table`

<details><summary>Answer</summary>

**Answer: B.** Replace + diff + commit (and `rollback`) makes the device config match the intended config exactly.

</details>

### Q9. In a controller-based architecture, what is the northbound interface?

- A) The interface between the controller and network devices
- B) The API between the controller and applications/scripts above it
- C) The physical uplink of the controller
- D) The console port

<details><summary>Answer</summary>

**Answer: B.** Northbound = apps to controller (usually REST). Southbound = controller to devices (NETCONF, RESTCONF, gNMI, SSH, OpenFlow).

</details>

### Q10. Which TWO items belong in a network GitOps pipeline before deployment? (Choose two.)

- A) Rendering configs from a source of truth with templates
- B) Automated validation (linting, Batfish, lab deploy)
- C) Manual CLI changes on production devices
- D) Disabling version control to move faster
- E) Emailing configs to the change board

<details><summary>Answer</summary>

**Answer: A, B.** Desired state is rendered from data and tested in CI before deploy.

</details>

### Q11. Which RESTCONF response status means a resource was created?

- A) 200
- B) 201
- C) 204
- D) 404

<details><summary>Answer</summary>

**Answer: B.** 201 Created. 204 means success with no body (common for PUT/PATCH/DELETE).

</details>

### Q12. Scenario: An Ansible playbook using `ios_config` with raw lines reports `changed` on every run, even when nothing changes. What is the best fix?

- A) Add `ignore_errors: true`
- B) Use a resource module (e.g. `cisco.ios.ios_vlans`) or match the exact running-config syntax
- C) Run with `--check` only
- D) Disable `gather_facts`

<details><summary>Answer</summary>

**Answer: B.** Resource modules compare structured state. Raw lines that differ in format from the running config always look "new".

</details>

### Q13. Scenario: You want to ask a public generative AI tool to review an ACL change. What is the correct first step according to safe prompting practice?

- A) Paste the full running config with passwords
- B) Remove or mask sensitive data according to its data classification, then give a persona, clear instructions and an output format
- C) Ask it to push the change directly to the router
- D) Ask for a poem about ACLs

<details><summary>Answer</summary>

**Answer: B.** Consider data classification, persona, instructions and output format (CCNA v2.0 topic 5.2).

</details>

### Q14. Which statement best describes agentic AI in network operations?

- A) A static script that runs one command
- B) An AI system that plans multi-step tasks and calls tools (such as show commands or ticket APIs) toward a goal, ideally with guardrails and human approval for changes
- C) A replacement for routing protocols
- D) A type of YANG model

<details><summary>Answer</summary>

**Answer: B.** Agents use tools to act. Least privilege, read-only defaults, approvals and audit logs keep them safe.

</details>

### Q15. Which data format uses indentation for structure and is common for Ansible playbooks and Nornir inventories?

- A) XML
- B) JSON
- C) YAML
- D) CSV

<details><summary>Answer</summary>

**Answer: C.** YAML is indentation-based and is a superset of JSON.

</details>
