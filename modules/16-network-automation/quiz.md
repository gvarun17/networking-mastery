# Quiz 16 — Network Automation

## Questions

### Q1. Which protocol carries YANG-modelled data as XML over SSH on TCP port 830?

- A) RESTCONF
- B) gNMI
- C) SNMP
- D) NETCONF

<details><summary>Answer</summary>

**Answer: D.** NETCONF uses XML RPCs over SSH (830). RESTCONF uses HTTPS; gNMI uses gRPC.

</details>

### Q2. Which HTTP method should you use in RESTCONF to replace a whole resource with the body you send?

- A) PATCH
- B) POST
- C) GET
- D) PUT

<details><summary>Answer</summary>

**Answer: D.** PUT replaces (create or replace). PATCH merges changes. POST creates a child resource.

</details>

### Q3. What is YANG?

- A) A Python library
- B) A transport protocol
- C) A data modelling language that describes configuration and state as a typed tree
- D) An encryption standard

<details><summary>Answer</summary>

**Answer: C.** YANG defines the schema; NETCONF/RESTCONF/gNMI carry data that conforms to it.

</details>

### Q4. Which gNMI RPC streams telemetry from a device?

- A) Get
- B) Subscribe
- C) Set
- D) Capabilities

<details><summary>Answer</summary>

**Answer: B.** Subscribe supports sample and on-change streaming.

</details>

### Q5. What does "idempotent" mean for a configuration tool?

- A) Running it many times gives the same end state and changes nothing when the state already matches
- B) It needs an agent on the device
- C) It always reboots the device
- D) It runs faster each time

<details><summary>Answer</summary>

**Answer: A.** An idempotent run reports no changes when the desired state is already present.

</details>

### Q6. Which statement about Ansible is correct?

- A) It works only with Linux servers
- B) It requires a database
- C) It is agentless and pushes changes over SSH or APIs
- D) It needs an agent installed on every network device

<details><summary>Answer</summary>

**Answer: C.** Ansible connects from a control node using network_cli (SSH), netconf or httpapi.

</details>

### Q7. Which Python library is a framework that runs tasks in parallel against an inventory and uses plugins such as Netmiko and NAPALM?

- A) Nornir
- B) Requests
- C) Paramiko
- D) Flask

<details><summary>Answer</summary>

**Answer: A.** Nornir provides inventory, filtering, threading and result handling in pure Python.

</details>

### Q8. Which NAPALM capability supports safe full-config deployment?

- A) `get_arp_table`
- B) `get_facts`
- C) `ping`
- D) `load_replace_candidate` followed by `compare_config` and `commit_config` (with rollback)

<details><summary>Answer</summary>

**Answer: D.** Replace + diff + commit (and `rollback`) makes the device config match the intended config exactly.

</details>

### Q9. In a controller-based architecture, what is the northbound interface?

- A) The physical uplink of the controller
- B) The console port
- C) The API between the controller and applications/scripts above it
- D) The interface between the controller and network devices

<details><summary>Answer</summary>

**Answer: C.** Northbound = apps to controller (usually REST). Southbound = controller to devices (NETCONF, RESTCONF, gNMI, SSH, OpenFlow).

</details>

### Q10. Which TWO items belong in a network GitOps pipeline before deployment? (Choose two.)

- A) Automated validation (linting, Batfish, lab deploy)
- B) Rendering configs from a source of truth with templates
- C) Manual CLI changes on production devices
- D) Emailing configs to the change board
- E) Disabling version control to move faster

<details><summary>Answer</summary>

**Answer: A, B.** Desired state is rendered from data and tested in CI before deploy.

</details>

### Q11. Which RESTCONF response status means a resource was created?

- A) 201
- B) 404
- C) 200
- D) 204

<details><summary>Answer</summary>

**Answer: A.** 201 Created. 204 means success with no body (common for PUT/PATCH/DELETE).

</details>

### Q12. Scenario: An Ansible playbook using `ios_config` with raw lines reports `changed` on every run, even when nothing changes. What is the best fix?

- A) Disable `gather_facts`
- B) Use a resource module (e.g. `cisco.ios.ios_vlans`) or match the exact running-config syntax
- C) Add `ignore_errors: true`
- D) Run with `--check` only

<details><summary>Answer</summary>

**Answer: B.** Resource modules compare structured state. Raw lines that differ in format from the running config always look "new".

</details>

### Q13. Scenario: You want to ask a public generative AI tool to review an ACL change. What is the correct first step according to safe prompting practice?

- A) Remove or mask sensitive data according to its data classification, then give a persona, clear instructions and an output format
- B) Paste the full running config with passwords
- C) Ask for a poem about ACLs
- D) Ask it to push the change directly to the router

<details><summary>Answer</summary>

**Answer: A.** Consider data classification, persona, instructions and output format (CCNA v2.0 topic 5.2).

</details>

### Q14. Which statement best describes agentic AI in network operations?

- A) An AI system that plans multi-step tasks and calls tools (such as show commands or ticket APIs) toward a goal, ideally with guardrails and human approval for changes
- B) A replacement for routing protocols
- C) A type of YANG model
- D) A static script that runs one command

<details><summary>Answer</summary>

**Answer: A.** Agents use tools to act. Least privilege, read-only defaults, approvals and audit logs keep them safe.

</details>

### Q15. Which data format uses indentation for structure and is common for Ansible playbooks and Nornir inventories?

- A) XML
- B) JSON
- C) YAML
- D) CSV

<details><summary>Answer</summary>

**Answer: C.** YAML is indentation-based and is a superset of JSON.

</details>
