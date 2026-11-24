"""Load, validate and render the capstone 5 network intent.

Used by validate.py, render.py and the tests. Pure Python + PyYAML + Jinja2 (no device access).
"""
from __future__ import annotations

import ipaddress
from pathlib import Path
from typing import Any

import yaml
from jinja2 import Environment, StrictUndefined

HERE = Path(__file__).resolve().parent
PRIVATE_ASN = range(64512, 65535)

TEMPLATE = """\
frr defaults traditional
hostname {{ name }}
!
interface lo
 ip address {{ loopback }}/32
{% for l in links %}
!
interface {{ l.interface }}
 description to-{{ l.peer }}
 ip address {{ l.ip }}/31
{% endfor %}
!
router bgp {{ asn }}
 bgp router-id {{ loopback }}
 no bgp ebgp-requires-policy
 timers bgp 3 9
{% for l in links %}
 neighbor {{ l.peer_ip }} remote-as {{ l.peer_asn }}
 neighbor {{ l.peer_ip }} description {{ l.peer }}
{% endfor %}
 !
 address-family ipv4 unicast
  network {{ loopback }}/32
 exit-address-family
!
line vty
!
"""


def load(path: str | Path = HERE / "intent" / "network.yaml") -> dict[str, Any]:
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))


def validate(intent: dict[str, Any]) -> list[str]:
    """Return a list of human-readable errors. Empty list = valid."""
    errors: list[str] = []
    routers = intent.get("routers") or {}
    links = intent.get("links") or []
    if not routers:
        return ["no routers defined"]

    seen_asn: dict[int, str] = {}
    seen_lo: dict[str, str] = {}
    for name, r in routers.items():
        asn = r.get("asn")
        if not isinstance(asn, int) or asn not in PRIVATE_ASN:
            errors.append(f"{name}: ASN {asn} is not a private 16-bit ASN (64512-65534)")
        elif asn in seen_asn:
            errors.append(f"{name}: ASN {asn} already used by {seen_asn[asn]}")
        else:
            seen_asn[asn] = name
        try:
            lo = ipaddress.ip_address(r.get("loopback", ""))
        except ValueError:
            errors.append(f"{name}: invalid loopback {r.get('loopback')!r}")
            continue
        if str(lo) in seen_lo:
            errors.append(f"{name}: loopback {lo} already used by {seen_lo[str(lo)]}")
        seen_lo[str(lo)] = name

    used_ports: set[tuple[str, str]] = set()
    used_ips: dict[str, str] = {}
    for i, link in enumerate(links, 1):
        a, b = link.get("a", {}), link.get("b", {})
        for end in (a, b):
            r = end.get("router")
            if r not in routers:
                errors.append(f"link {i}: unknown router {r!r}")
            port = (r, end.get("interface"))
            if port in used_ports:
                errors.append(f"link {i}: interface {port[1]} on {r} used twice")
            used_ports.add(port)
            ip = end.get("ip", "")
            if ip in used_ips:
                errors.append(f"link {i}: IP {ip} already used on {used_ips[ip]}")
            used_ips[ip] = f"{r}:{end.get('interface')}"
        if a.get("router") == b.get("router"):
            errors.append(f"link {i}: both ends on {a.get('router')}")
        try:
            na = ipaddress.ip_interface(f"{a.get('ip')}/31").network
            nb = ipaddress.ip_interface(f"{b.get('ip')}/31").network
            if na != nb:
                errors.append(f"link {i}: {a.get('ip')} and {b.get('ip')} are not in the same /31")
        except ValueError as exc:
            errors.append(f"link {i}: bad IP ({exc})")
    return errors


def per_router(intent: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """Build template variables for each router."""
    routers = intent["routers"]
    out = {name: {"name": name, "asn": r["asn"], "loopback": r["loopback"], "links": []} for name, r in routers.items()}
    for link in intent["links"]:
        for me, peer in ((link["a"], link["b"]), (link["b"], link["a"])):
            out[me["router"]]["links"].append({
                "interface": me["interface"],
                "ip": me["ip"],
                "peer": peer["router"],
                "peer_ip": peer["ip"],
                "peer_asn": routers[peer["router"]]["asn"],
            })
    return out


def render(intent: dict[str, Any]) -> dict[str, str]:
    env = Environment(undefined=StrictUndefined, trim_blocks=True, lstrip_blocks=True, keep_trailing_newline=True)
    tpl = env.from_string(TEMPLATE)
    return {name: tpl.render(**vars_) for name, vars_ in per_router(intent).items()}


def expected_peers(intent: dict[str, Any]) -> dict[str, set[str]]:
    return {name: {l["peer_ip"] for l in v["links"]} for name, v in per_router(intent).items()}
