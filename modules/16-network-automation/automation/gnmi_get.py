#!/usr/bin/env python3
"""Read interface counters from SR Linux over gNMI (TCP 57400) with pygnmi, then stream them.

Usage:
    python3 gnmi_get.py 172.20.16.11 ethernet-1/1
    python3 gnmi_get.py 172.20.16.11 ethernet-1/1 --subscribe
"""
from __future__ import annotations

import json
import sys

from pygnmi.client import gNMIclient


def main() -> int:
    host = sys.argv[1] if len(sys.argv) > 1 else "172.20.16.11"
    ifname = sys.argv[2] if len(sys.argv) > 2 else "ethernet-1/1"
    path = f"/interface[name={ifname}]/statistics"
    with gNMIclient(target=(host, 57400), username="admin", password="NokiaSrl1!", skip_verify=True) as gc:
        print(json.dumps(gc.get(path=[path], encoding="json_ietf"), indent=2)[:2000])
        if "--subscribe" in sys.argv:
            sub = {
                "subscription": [{"path": f"{path}/in-octets", "mode": "sample", "sample_interval": 5_000_000_000}],
                "mode": "stream",
                "encoding": "json_ietf",
            }
            for i, update in enumerate(gc.subscribe2(subscribe=sub)):
                print(update)
                if i >= 5:
                    break
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
