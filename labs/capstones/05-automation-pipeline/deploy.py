#!/usr/bin/env python3
"""Deploy rendered configs to the Containerlab FRR routers with Nornir.

Each router gets a full config **replace** with FRR's frr-reload.py:
  --test shows the diff (like NAPALM compare_config), --reload applies only the differences.

Usage:
    python3 deploy.py --diff      # show what would change
    python3 deploy.py             # apply
"""
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

from nornir import InitNornir
from nornir.core.task import Result, Task
from nornir_utils.plugins.functions import print_result

HERE = Path(__file__).resolve().parent
RELOAD = "/usr/lib/frr/frr-reload.py"


def sh(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, check=False)


def frr_replace(task: Task, diff_only: bool) -> Result:
    ctr = task.host["container"]
    src = HERE / "build" / f"{task.host.name}.conf"
    cp = sh(["docker", "cp", str(src), f"{ctr}:/tmp/candidate.conf"])
    if cp.returncode:
        return Result(host=task.host, failed=True, result=cp.stderr)
    test = sh(["docker", "exec", ctr, "python3", RELOAD, "--test", "/tmp/candidate.conf"])
    if diff_only or test.returncode:
        return Result(host=task.host, failed=bool(test.returncode), result=test.stdout + test.stderr)
    apply = sh(["docker", "exec", ctr, "python3", RELOAD, "--reload", "/tmp/candidate.conf"])
    sh(["docker", "exec", ctr, "cp", "/tmp/candidate.conf", "/etc/frr/frr.conf"])
    return Result(host=task.host, failed=bool(apply.returncode), changed=True, result=test.stdout + apply.stderr)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--diff", action="store_true", help="show the diff only")
    args = p.parse_args()
    nr = InitNornir(
        runner={"plugin": "threaded", "options": {"num_workers": 5}},
        inventory={"plugin": "SimpleInventory", "options": {"host_file": str(HERE / "build" / "hosts.yaml")}},
        logging={"enabled": False},
    )
    result = nr.run(task=frr_replace, diff_only=args.diff)
    print_result(result)
    return 1 if result.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
