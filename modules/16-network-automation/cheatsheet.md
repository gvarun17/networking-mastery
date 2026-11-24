# Cheatsheet 16 — Network Automation

## Protocols

| | Transport | Port | Encoding |
|---|---|---|---|
| SSH CLI | SSH | 22 | Text |
| NETCONF | SSH | 830 | XML |
| RESTCONF | HTTPS | 443 | JSON/XML |
| gNMI | gRPC/HTTP2 | 57400 (common), 9339 (IANA) | Protobuf/JSON |
| SNMP | UDP | 161/162 | BER |

## HTTP ↔ CRUD

| Method | Action | Typical success |
|---|---|---|
| POST | Create | 201 |
| GET | Read | 200 |
| PUT | Create/replace | 200/201/204 |
| PATCH | Update/merge | 200/204 |
| DELETE | Delete | 204 |

Errors: 400 bad request · 401 unauthenticated · 403 forbidden · 404 not found · 409 conflict · 500 server error.

## NETCONF operations

`<get>`, `<get-config>`, `<edit-config>` (merge/replace/create/delete/remove), `<commit>`, `<lock>`/`<unlock>`, `<discard-changes>`, `<validate>`. Datastores: running, candidate, startup.

## Python snippets

```python
# Netmiko
from netmiko import ConnectHandler
c = ConnectHandler(device_type="cisco_xe", host="10.0.0.1", username="u", password="p")
c.send_command("show ip route", use_textfsm=True); c.send_config_set(["..."]); c.save_config()

# NAPALM
from napalm import get_network_driver
d = get_network_driver("ios")("10.0.0.1", "u", "p"); d.open()
d.get_facts(); d.load_replace_candidate(filename="intended.cfg"); print(d.compare_config()); d.commit_config()

# ncclient
from ncclient import manager
with manager.connect(host=h, port=830, username=u, password=p, hostkey_verify=False) as m:
    m.get_config("running", filter=("subtree", xml_filter))

# requests + RESTCONF
requests.get(f"https://{h}/restconf/data/ietf-interfaces:interfaces", auth=(u, p),
             headers={"Accept": "application/yang-data+json"}, verify=False)
```

## Nornir

```text
nr = InitNornir(config_file="config.yaml")
nr.filter(role="leaf").run(task=netmiko_send_command, command_string="show version")
Tasks: netmiko_send_command, netmiko_send_config, netmiko_commit, napalm_get, napalm_configure, template_file
```

## Ansible

```text
ansible-playbook -i inventory.yml site.yml --check --diff --limit sw1
ansible-inventory -i inventory.yml --graph
ansible-vault encrypt_string 'S3cret' --name 'ansible_password'
Connections: ansible.netcommon.network_cli | netconf | httpapi
Resource module states: merged replaced overridden deleted gathered rendered parsed
```

## Testing tools

| Tool | Use |
|---|---|
| Batfish | Offline config analysis (reachability, ACLs, BGP) |
| pyATS / Genie | Parse state, snapshot and diff before/after |
| Containerlab | Real NOS containers in CI |
| yamllint / jsonschema | Validate source-of-truth data |
| NetBox | Source of truth (IPAM/DCIM) with API |

## CCNA v2.0 domain 5 reminders

Management approaches: device, cloud, controller, automation, IaC · SNMP polling vs traps · Ansible to execute commands · syslog severities · agentic AI with guardrails · prompts: data classification, persona, instructions, output format.
