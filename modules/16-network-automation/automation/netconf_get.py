#!/usr/bin/env python3
"""Read an interface from SR Linux over NETCONF (TCP 830) with ncclient.

Usage:
    python3 netconf_get.py 172.20.16.11 ethernet-1/1
"""
from __future__ import annotations

import sys

from ncclient import manager

FILTER = """
<interface xmlns="urn:nokia.com:srlinux:chassis:interfaces">
  <name>{name}</name>
</interface>
"""


def main() -> int:
    host = sys.argv[1] if len(sys.argv) > 1 else "172.20.16.11"
    ifname = sys.argv[2] if len(sys.argv) > 2 else "ethernet-1/1"
    with manager.connect(
        host=host,
        port=830,
        username="admin",
        password="NokiaSrl1!",
        hostkey_verify=False,
        device_params={"name": "default"},
        timeout=30,
    ) as m:
        print("Server capabilities (first 5):")
        for cap in list(m.server_capabilities)[:5]:
            print("  ", cap)
        reply = m.get_config(source="running", filter=("subtree", FILTER.format(name=ifname)))
        print(reply.xml)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
