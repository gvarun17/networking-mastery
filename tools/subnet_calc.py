#!/usr/bin/env python3
"""Subnet calculator and practice-problem generator.

Examples:
    python3 tools/subnet_calc.py info 192.168.10.77/27
    python3 tools/subnet_calc.py split 10.0.0.0/22 --new-prefix 24
    python3 tools/subnet_calc.py vlsm 172.16.0.0/24 --hosts 100 50 25 2 2
    python3 tools/subnet_calc.py summarize 10.1.4.0/24 10.1.5.0/24 10.1.6.0/24 10.1.7.0/24
    python3 tools/subnet_calc.py wildcard 255.255.252.0
    python3 tools/subnet_calc.py practice --count 10 --seed 7
    python3 tools/subnet_calc.py info 2001:db8:acad::1/64
"""
from __future__ import annotations

import argparse
import ipaddress
import random
import sys
from dataclasses import dataclass
from typing import Iterable

IPNetwork = ipaddress.IPv4Network | ipaddress.IPv6Network


@dataclass(frozen=True)
class SubnetInfo:
    address: str
    network: str
    prefix: int
    netmask: str
    wildcard: str
    broadcast: str | None
    first_host: str | None
    last_host: str | None
    usable_hosts: int
    total_addresses: int
    ip_class: str | None
    is_private: bool


def ipv4_class(addr: ipaddress.IPv4Address) -> str:
    first = int(str(addr).split(".")[0])
    if first < 128:
        return "A"
    if first < 192:
        return "B"
    if first < 224:
        return "C"
    if first < 240:
        return "D (multicast)"
    return "E (reserved)"


def usable_hosts(net: IPNetwork) -> int:
    """Usable host count. /31 = 2 (RFC 3021 point-to-point), /32 = 1."""
    if net.version == 6:
        return net.num_addresses  # IPv6 has no broadcast; all addresses usable in practice
    if net.prefixlen == 32:
        return 1
    if net.prefixlen == 31:
        return 2
    return net.num_addresses - 2


def info(cidr: str) -> SubnetInfo:
    iface = ipaddress.ip_interface(cidr)
    net = iface.network
    if net.version == 4:
        if net.prefixlen >= 31:
            first, last, bcast = net[0], net[-1], None
        else:
            first, last, bcast = net[1], net[-2], net.broadcast_address
        return SubnetInfo(
            address=str(iface.ip),
            network=str(net.network_address),
            prefix=net.prefixlen,
            netmask=str(net.netmask),
            wildcard=str(net.hostmask),
            broadcast=str(bcast) if bcast else None,
            first_host=str(first),
            last_host=str(last),
            usable_hosts=usable_hosts(net),
            total_addresses=net.num_addresses,
            ip_class=ipv4_class(iface.ip),
            is_private=iface.ip.is_private,
        )
    return SubnetInfo(
        address=str(iface.ip),
        network=str(net.network_address),
        prefix=net.prefixlen,
        netmask=str(net.netmask),
        wildcard=str(net.hostmask),
        broadcast=None,
        first_host=str(net[0]),
        last_host=str(net[-1]),
        usable_hosts=usable_hosts(net),
        total_addresses=net.num_addresses,
        ip_class=None,
        is_private=iface.ip.is_private,
    )


def split(cidr: str, new_prefix: int) -> list[IPNetwork]:
    net = ipaddress.ip_network(cidr, strict=False)
    if new_prefix < net.prefixlen:
        raise ValueError("new prefix must be longer than the parent prefix")
    return list(net.subnets(new_prefix=new_prefix))


def prefix_for_hosts(hosts: int) -> int:
    """Smallest IPv4 prefix that holds `hosts` usable addresses."""
    if hosts < 1:
        raise ValueError("hosts must be >= 1")
    if hosts == 2:
        return 30  # classic CCNA answer; use /31 only when asked for point-to-point links
    bits = 0
    while (2**bits) - 2 < hosts:
        bits += 1
    return 32 - bits


def vlsm(cidr: str, host_counts: Iterable[int]) -> list[tuple[int, IPNetwork]]:
    """Allocate subnets largest-first. Returns (requested_hosts, subnet)."""
    parent = ipaddress.ip_network(cidr, strict=False)
    if parent.version != 4:
        raise ValueError("VLSM helper supports IPv4 only")
    requests = sorted(host_counts, reverse=True)
    cursor = int(parent.network_address)
    end = int(parent.broadcast_address)
    result: list[tuple[int, IPNetwork]] = []
    for hosts in requests:
        prefix = prefix_for_hosts(hosts)
        size = 2 ** (32 - prefix)
        if cursor % size:
            cursor += size - (cursor % size)
        if cursor + size - 1 > end:
            raise ValueError(f"not enough space for {hosts} hosts in {parent}")
        result.append((hosts, ipaddress.ip_network(f"{ipaddress.IPv4Address(cursor)}/{prefix}")))
        cursor += size
    return result


def summarize(cidrs: Iterable[str]) -> list[IPNetwork]:
    """Exact summary (no over-summarization)."""
    nets = [ipaddress.ip_network(c, strict=False) for c in cidrs]
    return list(ipaddress.collapse_addresses(nets))


def supernet(cidrs: Iterable[str]) -> IPNetwork:
    """Smallest single prefix that covers all inputs (may include extra space)."""
    nets = [ipaddress.ip_network(c, strict=False) for c in cidrs]
    candidate = nets[0]
    while not all(n.subnet_of(candidate) for n in nets):
        candidate = candidate.supernet()
    return candidate


def wildcard(mask: str) -> str:
    net = ipaddress.ip_network(f"0.0.0.0/{mask}")
    return str(net.hostmask)


def same_subnet(a: str, b: str) -> bool:
    return ipaddress.ip_interface(a).network == ipaddress.ip_interface(b).network


# ---------------------------------------------------------------- practice
def practice_problems(count: int, seed: int) -> list[tuple[str, str]]:
    rng = random.Random(seed)
    problems: list[tuple[str, str]] = []
    kinds = ["network", "broadcast", "hosts", "range", "mask", "fits"]
    for i in range(count):
        kind = kinds[i % len(kinds)]
        prefix = rng.randint(17, 30)
        octets = [rng.choice([10, 172, 192]), rng.randint(0, 255), rng.randint(0, 255), rng.randint(1, 254)]
        if octets[0] == 172:
            octets[1] = rng.randint(16, 31)
        if octets[0] == 192:
            octets[1] = 168
        addr = ".".join(map(str, octets))
        s = info(f"{addr}/{prefix}")
        if kind == "network":
            problems.append((f"What is the network address of {addr}/{prefix}?", s.network))
        elif kind == "broadcast":
            problems.append((f"What is the broadcast address of {addr}/{prefix}?", str(s.broadcast)))
        elif kind == "hosts":
            problems.append((f"How many usable hosts are in a /{prefix}?", str(s.usable_hosts)))
        elif kind == "range":
            problems.append((f"What is the usable host range of {addr}/{prefix}?", f"{s.first_host} - {s.last_host}"))
        elif kind == "mask":
            problems.append((f"Write /{prefix} as a dotted-decimal mask and as a wildcard.", f"{s.netmask} / {s.wildcard}"))
        else:
            hosts = rng.randint(3, 4000)
            problems.append((f"What is the longest prefix that holds {hosts} hosts?", f"/{prefix_for_hosts(hosts)}"))
    return problems


def _print_info(s: SubnetInfo) -> None:
    rows = [
        ("Address", s.address),
        ("Network", f"{s.network}/{s.prefix}"),
        ("Netmask", s.netmask),
        ("Wildcard", s.wildcard),
        ("Broadcast", s.broadcast or "n/a"),
        ("First host", s.first_host),
        ("Last host", s.last_host),
        ("Usable hosts", f"{s.usable_hosts:,}"),
        ("Total addresses", f"{s.total_addresses:,}"),
        ("Class", s.ip_class or "n/a (IPv6)"),
        ("Private", "yes" if s.is_private else "no"),
    ]
    width = max(len(k) for k, _ in rows)
    for k, v in rows:
        print(f"{k:<{width}} : {v}")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s_info = sub.add_parser("info", help="show subnet details")
    s_info.add_argument("cidr")
    s_split = sub.add_parser("split", help="split a network into smaller subnets")
    s_split.add_argument("cidr")
    s_split.add_argument("--new-prefix", type=int, required=True)
    s_vlsm = sub.add_parser("vlsm", help="allocate subnets for host counts, largest first")
    s_vlsm.add_argument("cidr")
    s_vlsm.add_argument("--hosts", type=int, nargs="+", required=True)
    s_sum = sub.add_parser("summarize", help="exact summary and smallest supernet")
    s_sum.add_argument("cidrs", nargs="+")
    s_wc = sub.add_parser("wildcard", help="convert a subnet mask to a wildcard mask")
    s_wc.add_argument("mask")
    s_pr = sub.add_parser("practice", help="generate practice problems")
    s_pr.add_argument("--count", type=int, default=10)
    s_pr.add_argument("--seed", type=int, default=None)
    s_pr.add_argument("--answers", action="store_true", help="print answers inline")
    args = p.parse_args(argv)

    try:
        if args.cmd == "info":
            _print_info(info(args.cidr))
        elif args.cmd == "split":
            for n in split(args.cidr, args.new_prefix):
                print(n)
        elif args.cmd == "vlsm":
            for hosts, n in vlsm(args.cidr, args.hosts):
                s = info(str(n))
                print(f"{hosts:>6} hosts -> {n!s:<18} hosts {s.first_host}-{s.last_host} bcast {s.broadcast}")
        elif args.cmd == "summarize":
            print("Exact summary :", ", ".join(map(str, summarize(args.cidrs))))
            print("Supernet      :", supernet(args.cidrs))
        elif args.cmd == "wildcard":
            print(wildcard(args.mask))
        elif args.cmd == "practice":
            seed = args.seed if args.seed is not None else random.randrange(1_000_000)
            print(f"# seed {seed}")
            probs = practice_problems(args.count, seed)
            for i, (q, a) in enumerate(probs, 1):
                print(f"{i:>2}. {q}" + (f"\n    -> {a}" if args.answers else ""))
            if not args.answers:
                print("\nAnswers:")
                for i, (_, a) in enumerate(probs, 1):
                    print(f"{i:>2}. {a}")
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
