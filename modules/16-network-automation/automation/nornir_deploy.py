#!/usr/bin/env python3
"""Render SR Linux config from inventory data with Jinja2 and deploy it with Nornir + Netmiko.

Usage:
    python3 nornir_deploy.py --dry-run     # render and print only
    python3 nornir_deploy.py               # render, push, commit, verify
"""
from __future__ import annotations

import argparse

from jinja2 import Environment, StrictUndefined
from nornir import InitNornir
from nornir.core.task import Result, Task
from nornir_netmiko.tasks import netmiko_commit, netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result

TEMPLATE = """\
set / interface {{ p2p.interface }} admin-state enable
set / interface {{ p2p.interface }} subinterface 0 ipv4 admin-state enable
set / interface {{ p2p.interface }} subinterface 0 ipv4 address {{ p2p.ip }}
set / interface lo0 subinterface 0 ipv4 admin-state enable
set / interface lo0 subinterface 0 ipv4 address {{ loopback }}
set / network-instance default interface {{ p2p.interface }}.0
set / network-instance default interface lo0.0
set / interface {{ p2p.interface }} description "managed-by-nornir"
"""

ENV = Environment(undefined=StrictUndefined, trim_blocks=True, lstrip_blocks=True)


def render(task: Task) -> Result:
    text = ENV.from_string(TEMPLATE).render(**task.host.data)
    task.host["rendered"] = text.strip().splitlines()
    return Result(host=task.host, result=text)


def deploy(task: Task, dry_run: bool) -> Result:
    task.run(task=render)
    if dry_run:
        return Result(host=task.host, result="dry run: nothing pushed")
    task.run(task=netmiko_send_config, config_commands=task.host["rendered"])
    task.run(task=netmiko_commit)
    verify = task.run(task=netmiko_send_command, command_string="show interface brief")
    ok = "managed" in task.run(
        task=netmiko_send_command,
        command_string=f"info from running / interface {task.host['p2p']['interface']} description",
    ).result
    return Result(host=task.host, result=verify.result, failed=not ok)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    nr = InitNornir(config_file="config.yaml")
    result = nr.run(task=deploy, dry_run=args.dry_run)
    print_result(result)
    return 1 if result.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
