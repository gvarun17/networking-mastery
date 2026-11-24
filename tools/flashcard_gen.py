#!/usr/bin/env python3
"""Generate cert/ccna-200-301/flashcards.csv (Anki-importable: front, back, tags).

Sources:
  1. reference/glossary.md        (Term | Definition | Module)   -> "What is X?" cards
  2. reference/ports-protocols.md (first table: Service | Protocol | Port | Notes)
  3. EXTRA_CARDS below            (hand-written CCNA v2.0 facts)

Import into Anki: File → Import → select the CSV → fields separated by comma,
map field 1 = Front, 2 = Back, 3 = Tags; tick "Allow HTML in fields" off.
Run: python3 tools/flashcard_gen.py
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "cert" / "ccna-200-301" / "flashcards.csv"

# (front, back, tags)
EXTRA_CARDS: list[tuple[str, str, str]] = [
    ("CCNA v2.0 domain weights?", "D1 Infrastructure 25%, D2 Switching/Access 25%, D3 IP Routing 20%, D4 Services/Security 20%, D5 AI/Ops/Mgmt 10%", "exam blueprint"),
    ("First test date of CCNA 200-301 v2.0?", "3 February 2027 (v1.1 last day: 2 February 2027)", "exam blueprint"),
    ("CCNA exam duration and price?", "120 minutes; US$300 plus local tax", "exam"),
    ("AD: connected, static, eBGP, EIGRP, OSPF, IS-IS, RIP, EIGRP ext, iBGP?", "0, 1, 20, 90, 110, 115, 120, 170, 200", "d3 routing"),
    ("Route selection order?", "Longest prefix match → lowest AD → lowest metric → ECMP", "d3 routing"),
    ("OSPF neighbor states in order?", "Down, Init, 2-Way, ExStart, Exchange, Loading, Full", "d3 ospf"),
    ("OSPF stuck in ExStart/Exchange: usual cause?", "MTU mismatch (or duplicate router ID)", "d3 ospf"),
    ("OSPF router ID selection order?", "router-id command → highest up loopback IP → highest up physical interface IP", "d3 ospf"),
    ("OSPF DR election?", "Highest interface priority (0 = never), then highest RID; non-preemptive", "d3 ospf"),
    ("OSPF hello/dead on broadcast and P2P?", "10 / 40 seconds", "d3 ospf"),
    ("OSPF cost formula and default reference bandwidth?", "Reference BW / interface BW; default reference 100 Mbps", "d3 ospf"),
    ("OSPF multicast addresses?", "224.0.0.5 all OSPF routers; 224.0.0.6 DR/BDR (IPv6 ff02::5 / ff02::6)", "d3 ospf"),
    ("HSRP vs VRRP preemption default?", "HSRP: off. VRRP: on", "d3 fhrp"),
    ("HSRPv2 virtual MAC for group 1?", "0000.0c9f.f001", "d3 fhrp"),
    ("VRRP virtual MAC format?", "0000.5e00.01XX (XX = group in hex)", "d3 fhrp"),
    ("Floating static route?", "Static route with an AD higher than the primary route's AD", "d3 routing"),
    ("IPv6 static route with link-local next hop needs…?", "The exit interface: ipv6 route ::/0 g0/1 fe80::2", "d3 routing"),
    ("STP root bridge election?", "Lowest bridge ID: priority (+ VLAN ID) then MAC", "d2 stp"),
    ("STP priority increments?", "Multiples of 4096 (0-61440)", "d2 stp"),
    ("Short STP costs for 10M/100M/1G/10G?", "100 / 19 / 4 / 2", "d2 stp"),
    ("RSTP port states?", "Discarding, learning, forwarding", "d2 stp"),
    ("RSTP port roles?", "Root, designated, alternate, backup, disabled", "d2 stp"),
    ("BPDU guard action?", "Err-disables the port when a BPDU is received", "d2 stp"),
    ("Root guard action?", "Root-inconsistent (blocks) when a superior BPDU arrives", "d2 stp"),
    ("Loop guard action?", "Loop-inconsistent when BPDUs stop arriving on a root/alternate port", "d2 stp"),
    ("LACP mode pairs that form a bundle?", "active/active, active/passive", "d2 etherchannel"),
    ("PAgP mode pairs that form a bundle?", "desirable/desirable, desirable/auto", "d2 etherchannel"),
    ("Command to add a VLAN to a trunk without replacing the list?", "switchport trunk allowed vlan add <id>", "d2 trunk"),
    ("What does show vlan brief NOT show?", "Trunk ports", "d2 trunk"),
    ("Native VLAN mismatch symptom?", "CDP %NATIVE_VLAN_MISMATCH log; untagged traffic leaks between VLANs", "d2 trunk"),
    ("CDP vs LLDP default timers?", "CDP 60/180 s; LLDP 30/120 s", "d2 discovery"),
    ("Enable LLDP globally?", "lldp run", "d2 discovery"),
    ("Port for a local-mode AP?", "Access port in the AP management VLAN", "d2 edge"),
    ("Port for a FlexConnect AP with local switching?", "802.1Q trunk (native = mgmt VLAN)", "d2 edge"),
    ("IP phone + PC port config?", "switchport access vlan <data> + switchport voice vlan <voice>", "d2 edge"),
    ("Port security violation modes?", "protect (drop), restrict (drop+log), shutdown (err-disable, default)", "d4 l2sec"),
    ("DHCP snooping: which ports are trusted?", "Only ports toward legitimate DHCP servers (uplinks); all others untrusted by default", "d4 l2sec"),
    ("DAI validates ARP against…?", "The DHCP snooping binding table (or ARP ACLs)", "d4 l2sec"),
    ("RA guard purpose?", "Drop rogue IPv6 Router Advertisements on host ports", "d4 l2sec"),
    ("Storm control purpose?", "Limit broadcast/multicast/unknown unicast traffic on a port", "d4 l2sec"),
    ("Standard ACL placement?", "Near the destination", "d4 acl"),
    ("Extended ACL placement?", "Near the source", "d4 acl"),
    ("ACL processing rules?", "Top-down, first match wins, implicit deny any at the end", "d4 acl"),
    ("Standard / extended ACL number ranges?", "1-99, 1300-1999 / 100-199, 2000-2699", "d4 acl"),
    ("Apply an ACL to VTY lines?", "access-class <acl> in", "d4 acl"),
    ("NAT terms: inside local vs inside global?", "Inside local = real private IP; inside global = translated public IP", "d4 nat"),
    ("PAT keyword in IOS?", "overload", "d4 nat"),
    ("Show NAT entries?", "show ip nat translations", "d4 nat"),
    ("RADIUS vs TACACS+ transport?", "RADIUS UDP 1812/1813; TACACS+ TCP 49", "d4 aaa"),
    ("When is 'local' used in 'group tacacs+ local'?", "Only if no TACACS+ server responds (not on a rejected password)", "d4 aaa"),
    ("Strongest local password hash in IOS XE?", "algorithm-type scrypt secret (type 9)", "d4 aaa"),
    ("Enable SCP server on IOS?", "ip scp server enable (requires SSH + AAA authorization)", "d4 files"),
    ("IPsec ESP vs AH protocol numbers?", "ESP 50 (encrypts), AH 51 (integrity only)", "d4 vpn"),
    ("IKE ports?", "UDP 500; UDP 4500 with NAT traversal", "d4 vpn"),
    ("DNS record for mail?", "MX", "d4 dns"),
    ("DNS record for reverse lookup?", "PTR", "d4 dns"),
    ("DHCP ports?", "Server UDP 67, client UDP 68", "d1 dhcp"),
    ("DHCP relay command?", "ip helper-address <server> on the client-facing interface", "d1 dhcp"),
    ("Exclude addresses from a Cisco DHCP pool?", "ip dhcp excluded-address <first> <last> (global config)", "d1 dhcp"),
    ("APIPA range?", "169.254.0.0/16", "d1 ipv4"),
    ("IPv6 LAN prefix length?", "/64", "d1 ipv6"),
    ("IPv6 P2P link prefix (RFC 6164)?", "/127", "d1 ipv6"),
    ("EUI-64 steps?", "Split MAC, insert FFFE, flip bit 7 (U/L) of the first byte", "d1 ipv6"),
    ("Enable IPv6 routing and RAs on IOS?", "ipv6 unicast-routing", "d1 ipv6"),
    ("2.4 GHz non-overlapping channels?", "1, 6, 11", "d1 wireless"),
    ("WPA3-Personal key exchange?", "SAE (Simultaneous Authentication of Equals)", "d1 wireless"),
    ("Which Wi-Fi band requires WPA3?", "6 GHz (Wi-Fi 6E/7)", "d1 wireless"),
    ("Good RSSI and SNR targets for voice?", "RSSI ≥ −67 dBm; SNR ≥ 25 dB", "d1 wireless"),
    ("Late collisions usually mean…?", "Duplex mismatch (half-duplex side) or cable too long", "d1 cabling"),
    ("CRC/input errors usually mean…?", "Bad cable/optic/EMI or the full-duplex side of a mismatch", "d1 cabling"),
    ("Max copper Ethernet segment?", "100 m", "d1 cabling"),
    ("Type 1 vs Type 2 hypervisor?", "Type 1 runs on hardware (ESXi, KVM); Type 2 runs on a host OS (VirtualBox)", "d1 virtualization"),
    ("Container vs VM?", "Containers share the host kernel; VMs run a full guest OS", "d1 virtualization"),
    ("Syslog severities 0-7?", "Emergency, Alert, Critical, Error, Warning, Notification, Informational, Debugging", "d5 syslog"),
    ("logging trap warnings sends which levels?", "0 through 4", "d5 syslog"),
    ("Cisco syslog message format?", "%FACILITY-SEVERITY-MNEMONIC: description", "d5 syslog"),
    ("SNMP trap vs inform?", "Trap: unacknowledged. Inform: acknowledged by the manager", "d5 snmp"),
    ("SNMPv3 security level with auth and encryption?", "authPriv", "d5 snmp"),
    ("Ansible connection plugin for IOS CLI?", "ansible.netcommon.network_cli", "d5 ansible"),
    ("Ansible dry run flags?", "--check --diff", "d5 ansible"),
    ("Is Ansible agent-based?", "No: agentless, pushes over SSH/APIs", "d5 ansible"),
    ("Northbound vs southbound API?", "Northbound: apps ↔ controller. Southbound: controller ↔ devices", "d5 mgmt"),
    ("Four elements of a good generative AI prompt (CCNA)?", "Data classification, persona, instructions, output format", "d5 ai"),
    ("Agentic AI safety basics?", "Least privilege, read-only default, human approval for changes, audit logs", "d5 ai"),
]


def parse_table(path: Path, min_cols: int) -> list[list[str]]:
    rows: list[list[str]] = []
    in_first_table = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if set("".join(cells)) <= set("-: "):
                in_first_table = True
                continue
            if in_first_table and len(cells) >= min_cols:
                rows.append(cells)
        elif in_first_table and rows:
            break  # only the first table
    return rows


def clean(text: str) -> str:
    return re.sub(r"`([^`]*)`", r"\1", text).strip()


def main() -> int:
    cards: list[tuple[str, str, str]] = []
    for term, definition, module in parse_table(ROOT / "reference" / "glossary.md", 3):
        cards.append((f"What is {clean(term)}?", clean(definition), f"glossary module-{module}"))
    for service, proto, port, notes in parse_table(ROOT / "reference" / "ports-protocols.md", 4):
        back = f"{proto} {port}" + (f" — {clean(notes)}" if notes else "")
        cards.append((f"Port/protocol for {clean(service)}?", back, "ports"))
    cards.extend((f, b, f"ccna {t}") for f, b, t in EXTRA_CARDS)

    seen: set[str] = set()
    unique = []
    for c in cards:
        if c[0] not in seen:
            seen.add(c[0])
            unique.append(c)
    with OUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["front", "back", "tags"])
        w.writerows(unique)
    print(f"wrote {OUT.relative_to(ROOT)} with {len(unique)} cards")
    return 0 if len(unique) >= 300 else 1


if __name__ == "__main__":
    raise SystemExit(main())
