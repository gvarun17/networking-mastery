#!/usr/bin/env python3
"""Run show commands on every device in the inventory, in parallel, with Nornir + Netmiko.

Usage:
    python3 nornir_show.py "show version"
    python3 nornir_show.py "show interface brief" --role leaf
"""
from __future__ import annotations

import argparse

from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command")
    parser.add_argument("--role", default=None, help="filter hosts by data.role")
    args = parser.parse_args()

    nr = InitNornir(config_file="config.yaml")
    if args.role:
        nr = nr.filter(role=args.role)
    result = nr.run(task=netmiko_send_command, command_string=args.command)
    print_result(result)
    return 1 if result.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
