# Sim 06 — L2/L3 Troubleshooting Ticket (15 min)

```mermaid
flowchart LR
  PCA["PC-A VLAN 20<br/>10.20.0.10/24"] --- ASW["ASW Fa0/3"]
  ASW == "Gi0/1 trunk" == DSW["DSW (SVIs 20, 30)"]
  DSW --- SRV["Server VLAN 30<br/>10.30.0.10/24"]
```

## Ticket

"PC-A cannot reach the server. It worked yesterday." Your trainer (or you, with a friend) injects **three** faults from this list before you start: VLAN 20 removed from the trunk allowed list; Fa0/3 in the wrong access VLAN; SVI 30 shut down; `ip routing` removed; server gateway wrong; PC-A port err-disabled by BPDU guard.

## Rules

- Start at PC-A. Use only `show`, `ping`, `traceroute` and Packet Tracer simulation mode until you know the cause.
- Fix one fault at a time and re-test after each fix.
- Write one line per fault: evidence → fix.

## Command checklist

```text
PC-A> ipconfig /all ; ping 10.20.0.1 ; tracert 10.30.0.10
ASW# show interfaces status ; show vlan brief ; show interfaces trunk ; show mac address-table interface fa0/3
DSW# show ip interface brief ; show interfaces trunk ; show ip route ; show running-config | include ip routing
DSW# show interfaces status err-disabled
```

## Verify

PC-A pings and traceroutes the server with two hops (gateway, server).

<details><summary>How each fault looks</summary>

| Fault | Evidence |
|---|---|
| VLAN missing on trunk | `show interfaces trunk` on ASW: 20 not in "allowed and active"; PC-A cannot ping its gateway |
| Wrong access VLAN | `show vlan brief`: Fa0/3 not in VLAN 20; MAC learned in another VLAN |
| SVI shut | `show ip interface brief`: Vlan30 administratively down |
| No `ip routing` | PC-A pings 10.20.0.1 but not 10.30.0.1; `show ip route` shows only "Default gateway" |
| Server gateway wrong | Packets reach the server (simulation mode) but replies are not sent to 10.30.0.1 |
| Err-disabled | `show interfaces status`: err-disabled; log `%SPANTREE-2-BLOCK_BPDUGUARD` |

</details>
