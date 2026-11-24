#!/usr/bin/env python3
"""Render one FRR config per router into build/, plus a Nornir inventory (build/hosts.yaml)."""
from __future__ import annotations

from pathlib import Path

import yaml

import netintent

LAB = "cap5"


def main() -> int:
    intent = netintent.load()
    errors = netintent.validate(intent)
    if errors:
        print("intent is invalid; run validate.py")
        return 1
    build = netintent.HERE / "build"
    build.mkdir(exist_ok=True)
    hosts = {}
    for name, text in netintent.render(intent).items():
        (build / f"{name}.conf").write_text(text, encoding="utf-8")
        hosts[name] = {"hostname": f"clab-{LAB}-{name}", "data": {"container": f"clab-{LAB}-{name}"}}
        print(f"rendered build/{name}.conf ({len(text.splitlines())} lines)")
    (build / "hosts.yaml").write_text(yaml.safe_dump(hosts, sort_keys=True), encoding="utf-8")
    print("wrote build/hosts.yaml")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
