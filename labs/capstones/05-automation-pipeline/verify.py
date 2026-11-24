#!/usr/bin/env python3
"""Post-deployment checks with Nornir: every expected BGP peer is Established and every loopback is reachable.

Retries for up to --wait seconds so it can run right after deploy in CI.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import time
from pathlib import Path

from nornir import InitNornir
from nornir.core.task import Result, Task
from nornir_utils.plugins.functions import print_result

import netintent

HERE = Path(__file__).resolve().parent
INTENT = netintent.load()
EXPECTED = netintent.expected_peers(INTENT)
LOOPBACKS = [r["loopback"] for r in INTENT["routers"].values()]


def vtysh_json(ctr: str, cmd: str) -> dict:
    out = subprocess.run(["docker", "exec", ctr, "vtysh", "-c", cmd], capture_output=True, text=True, check=False)
    return json.loads(out.stdout or "{}")


def check(task: Task) -> Result:
    ctr = task.host["container"]
    summary = vtysh_json(ctr, "show bgp ipv4 unicast summary json")
    peers = summary.get("peers", {})
    problems = [f"peer {ip} not Established ({peers.get(ip, {}).get('state', 'missing')})"
                for ip in sorted(EXPECTED[task.host.name]) if peers.get(ip, {}).get("state") != "Established"]
    my_lo = INTENT["routers"][task.host.name]["loopback"]
    for lo in LOOPBACKS:
        if lo == my_lo:
            continue
        ping = subprocess.run(["docker", "exec", ctr, "ping", "-c", "1", "-W", "1", "-I", my_lo, lo],
                              capture_output=True, text=True, check=False)
        if ping.returncode:
            problems.append(f"cannot reach loopback {lo}")
    return Result(host=task.host, failed=bool(problems), result="OK" if not problems else "\n".join(problems))


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--wait", type=int, default=60)
    args = p.parse_args()
    nr = InitNornir(
        runner={"plugin": "threaded", "options": {"num_workers": 5}},
        inventory={"plugin": "SimpleInventory", "options": {"host_file": str(HERE / "build" / "hosts.yaml")}},
        logging={"enabled": False},
    )
    deadline = time.time() + args.wait
    while True:
        result = nr.run(task=check)
        if not result.failed or time.time() > deadline:
            break
        time.sleep(5)
    print_result(result)
    return 1 if result.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
