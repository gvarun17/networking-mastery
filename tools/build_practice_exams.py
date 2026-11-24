#!/usr/bin/env python3
"""Build three 100-question CCNA 200-301 v2.0 practice exams.

Each exam = hand-written questions from cert/ccna-200-301/practice-exams/bank/d*.yaml
            + computed questions (subnetting, IPv6, STP, LPM, AD, wildcards, syslog) whose
              answers are calculated here, so they are correct by construction.

Domain split per exam matches the v2.0 weights: D1 25, D2 25, D3 20, D4 20, D5 10.
Output: cert/ccna-200-301/practice-exams/exam-{1,2,3}.md (quiz_runner.py compatible).
Run:    python3 tools/build_practice_exams.py
"""
from __future__ import annotations

import ipaddress
import random
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import subnet_calc as sc  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CERT = ROOT / "cert" / "ccna-200-301" / "practice-exams"
BANK = CERT / "bank"

DOMAINS = {
    1: ("Network Infrastructure and Connectivity", 25),
    2: ("Switching and Network Access", 25),
    3: ("IP Routing", 20),
    4: ("Network Services and Security", 20),
    5: ("AI, and Network Operations and Management", 10),
}
COMPUTED_PER_EXAM = {1: 12, 2: 5, 3: 9, 4: 6, 5: 3}
LETTERS = "ABCDEF"


# ------------------------------------------------------------------ helpers
def mcq(rng: random.Random, question: str, correct: str, wrong: list[str], explanation: str, domain: int) -> dict:
    opts = [correct] + [w for w in dict.fromkeys(wrong) if w != correct][:3]
    while len(opts) < 4:
        opts.append(f"None of the above ({len(opts)})")
    rng.shuffle(opts)
    return {"q": question, "o": opts, "a": LETTERS[opts.index(correct)], "e": explanation, "d": domain}


def rand_private(rng: random.Random) -> str:
    first = rng.choice([10, 172, 192])
    if first == 10:
        return f"10.{rng.randint(0, 255)}.{rng.randint(0, 255)}.{rng.randint(1, 254)}"
    if first == 172:
        return f"172.{rng.randint(16, 31)}.{rng.randint(0, 255)}.{rng.randint(1, 254)}"
    return f"192.168.{rng.randint(0, 255)}.{rng.randint(1, 254)}"


# ------------------------------------------------------------------ domain 1 generators
def q_network(rng):
    p = rng.randint(18, 29)
    addr = rand_private(rng)
    s = sc.info(f"{addr}/{p}")
    net = ipaddress.ip_network(f"{s.network}/{p}")
    block = net.num_addresses
    wrong = [s.broadcast, str(net.network_address + block) if int(net.network_address) + block < 2**32 else s.first_host,
             str(ipaddress.ip_address(int(net.network_address) - block)) if int(net.network_address) >= block else s.last_host,
             s.first_host]
    return mcq(rng, f"What is the network address of host {addr}/{p}?", s.network, wrong,
               f"/{p} has {block} addresses per subnet; {addr} falls in {s.network}/{p} (broadcast {s.broadcast}).", 1)


def q_broadcast(rng):
    p = rng.randint(18, 29)
    addr = rand_private(rng)
    s = sc.info(f"{addr}/{p}")
    net = ipaddress.ip_network(f"{s.network}/{p}")
    wrong = [s.network, s.last_host, str(net.broadcast_address + 1) if str(net.broadcast_address) != "255.255.255.255" else s.first_host,
             str(ipaddress.ip_address(int(net.broadcast_address) - net.num_addresses))]
    return mcq(rng, f"What is the broadcast address of the subnet that contains {addr}/{p}?", s.broadcast, wrong,
               f"Network {s.network}/{p}; the broadcast is the last address of the block, {s.broadcast}.", 1)


def q_hosts(rng):
    p = rng.randint(19, 30)
    n = 2 ** (32 - p) - 2
    return mcq(rng, f"How many usable host addresses does a /{p} IPv4 subnet provide?", f"{n:,}",
               [f"{n + 2:,}", f"{n // 2 - 1:,}" if n > 2 else "1", f"{(n + 2) * 2 - 2:,}"],
               f"2^{32 - p} − 2 = {n:,} (network and broadcast are not usable).", 1)


def q_mask_for_hosts(rng):
    h = rng.choice([5, 12, 25, 50, 60, 100, 120, 200, 300, 500, 900, 1500])
    p = sc.prefix_for_hosts(h)
    mask = str(ipaddress.ip_network(f"0.0.0.0/{p}").netmask)
    wrong = [str(ipaddress.ip_network(f"0.0.0.0/{x}").netmask) for x in (p + 1, p - 1, p + 2, p - 2) if 8 <= x <= 30][:3]
    return mcq(rng, f"Which subnet mask supports {h} hosts on one subnet while wasting the fewest addresses?", mask, wrong,
               f"/{p} ({mask}) gives {2 ** (32 - p) - 2} usable hosts; /{p + 1} gives only {2 ** (31 - p) - 2}.", 1)


def q_valid_host(rng):
    p = rng.randint(24, 29)
    addr = rand_private(rng)
    s = sc.info(f"{addr}/{p}")
    net = ipaddress.ip_network(f"{s.network}/{p}")
    good = str(net[rng.randint(1, net.num_addresses - 2)])
    nxt = str(net.broadcast_address + 1)
    return mcq(rng, f"Which address can be assigned to a host in subnet {s.network}/{p}?", good,
               [s.network, s.broadcast, nxt],
               f"{s.network}/{p} spans {s.network}-{s.broadcast}; usable hosts are {s.first_host}-{s.last_host}.", 1)


def q_same_subnet(rng):
    p = rng.randint(20, 28)
    addr = rand_private(rng)
    net = ipaddress.ip_interface(f"{addr}/{p}").network
    same = str(net[rng.randint(1, net.num_addresses - 2)])
    others = []
    for delta in (1, -1, 2):
        k = int(net.network_address) + delta * net.num_addresses + rng.randint(1, net.num_addresses - 2)
        if 0 < k < 2**32:
            others.append(str(ipaddress.ip_address(k)))
    return mcq(rng, f"Host A is {addr}/{p}. Which host is in the same subnet as Host A (same mask)?", same, others,
               f"Host A is in {net}; only {same} falls inside {net.network_address}-{net.broadcast_address}.", 1)


def q_ipv6_compress(rng):
    groups = [rng.choice(["2001", "2001", "fd12"]), "0db8"]
    for _ in range(6):
        groups.append(rng.choice(["0000", f"{rng.randint(1, 0xffff):04x}", f"00{rng.randint(1, 255):02x}"]))
    run_at = rng.randint(2, 6)               # force a run of at least two zero hextets
    groups[run_at] = groups[run_at + 1] = "0000"
    full = ":".join(groups)
    correct = ipaddress.IPv6Address(full).compressed
    no_lead = ":".join(g.lstrip("0") or "0" for g in groups)
    head, tail = correct.split("::")
    wrong = [no_lead,                                   # forgot to compress the zero run
             correct.replace("::", ":", 1),            # dropped the zeros without ::
             full.replace("0000:0000", "", 1).replace("::", "::").rstrip(":") + ("" if tail else ""),
             f"{head}::{tail.replace(':0:', '::', 1)}" if ":0:" in tail else no_lead.replace(":0:", "::", 2)]
    return mcq(rng, f"What is the correct shortest form of {full}?", correct, wrong,
               "Remove leading zeros in each hextet, then replace the longest run of all-zero hextets with :: (only once).", 1)


def q_eui64(rng):
    mac = [rng.randint(0, 255) & 0xFC for _ in range(1)] + [rng.randint(0, 255) for _ in range(5)]
    flipped = mac[0] ^ 0x02
    iid = f"{flipped:02x}{mac[1]:02x}:{mac[2]:02x}ff:fe{mac[3]:02x}:{mac[4]:02x}{mac[5]:02x}"
    iid_noflip = f"{mac[0]:02x}{mac[1]:02x}:{mac[2]:02x}ff:fe{mac[3]:02x}:{mac[4]:02x}{mac[5]:02x}"
    iid_wrongpad = f"{flipped:02x}{mac[1]:02x}:{mac[2]:02x}fe:ff{mac[3]:02x}:{mac[4]:02x}{mac[5]:02x}"
    macs = ":".join(f"{b:02x}" for b in mac)
    norm = lambda s: str(ipaddress.IPv6Address("2001:db8:1:1:" + s)).split("2001:db8:1:1:")[-1]  # noqa: E731
    correct = norm(iid)
    return mcq(rng, f"An interface with MAC {macs} uses EUI-64 with prefix 2001:db8:1:1::/64. What is its interface ID?",
               correct, [norm(iid_noflip), norm(iid_wrongpad), norm(f"{mac[0]:02x}{mac[1]:02x}:{mac[2]:02x}{mac[3]:02x}:{mac[4]:02x}{mac[5]:02x}:0")],
               "Insert ff:fe between the OUI and NIC parts, then flip the 7th bit (U/L) of the first byte.", 1)


D1_GENS = [q_network, q_broadcast, q_hosts, q_mask_for_hosts, q_valid_host, q_same_subnet, q_ipv6_compress, q_eui64,
           q_network, q_broadcast, q_valid_host, q_same_subnet]


# ------------------------------------------------------------------ domain 2 generators
def rand_mac(rng):
    return ".".join(f"{rng.randint(0, 0xffff):04x}" for _ in range(3))


def q_stp_root(rng):
    vlan = rng.choice([1, 10, 20, 30])
    bases = rng.sample([0, 4096, 8192, 16384, 24576, 28672, 32768, 32768, 32768], 4)
    sws = [(f"SW{i + 1}", b + vlan, rand_mac(rng)) for i, b in enumerate(bases)]
    # force a tie on priority sometimes so MAC decides
    if rng.random() < 0.5:
        sws[1] = (sws[1][0], sws[0][1], sws[1][2])
    root = min(sws, key=lambda t: (t[1], int(t[2].replace(".", ""), 16)))
    listing = "; ".join(f"{n} priority {p} MAC {m}" for n, p, m in sws)
    return mcq(rng, f"Rapid PVST+ for VLAN {vlan}: {listing}. Which switch becomes the root bridge?", root[0],
               [n for n, _, _ in sws if n != root[0]],
               "Lowest bridge ID wins: compare priority (including the VLAN ID) first, then the lowest MAC.", 2)


def q_root_port(rng):
    speeds = {"FastEthernet (cost 19)": 19, "GigabitEthernet (cost 4)": 4, "TenGigabitEthernet (cost 2)": 2}
    ports = []
    for i in range(3):
        name, local = rng.choice(list(speeds.items()))
        upstream = rng.choice([0, 2, 4, 19])
        ports.append((f"Port {i + 1}", name, upstream, local + upstream))
    ports.sort(key=lambda t: t[3])
    low = ports[0][3]
    ports = [ports[0]] + [(n, s, u + 4, c + 4) if c == low else (n, s, u, c) for n, s, u, c in ports[1:]]
    best = ports[0]
    desc = "; ".join(f"{n}: {s}, neighbor advertises root path cost {u}" for n, s, u, _ in sorted(ports))
    return mcq(rng, f"A non-root switch (short STP costs) has three uplinks. {desc}. Which port becomes the root port?",
               best[0], [p[0] for p in ports[1:]] + ["None; all three forward"],
               f"Root port = lowest total cost to the root (advertised cost + local port cost). {best[0]} totals {best[3]}.", 2)


def q_etherchannel(rng):
    good = [("active", "active"), ("active", "passive"), ("desirable", "auto"), ("desirable", "desirable"), ("on", "on")]
    bad = [("passive", "passive"), ("auto", "auto"), ("active", "desirable"), ("on", "active"), ("auto", "passive")]
    g = rng.choice(good)
    wrong = rng.sample(bad, 3)
    fmt = lambda t: f"{t[0]} / {t[1]}"  # noqa: E731
    return mcq(rng, "Which pair of channel-group modes on two connected switches forms an EtherChannel?", fmt(g),
               [fmt(w) for w in wrong],
               "LACP: active-active or active-passive. PAgP: desirable-desirable or desirable-auto. Static: on-on. Modes from different protocols never bundle.", 2)


D2_GENS = [q_stp_root, q_root_port, q_etherchannel, q_stp_root, q_root_port]


# ------------------------------------------------------------------ domain 3 generators
def q_lpm(rng):
    base = ipaddress.ip_network(f"10.{rng.randint(0, 200)}.0.0/16")
    sub20 = list(base.subnets(new_prefix=20))[rng.randint(0, 15)]
    sub24 = list(sub20.subnets(new_prefix=24))[rng.randint(0, 15)]
    sub26 = list(sub24.subnets(new_prefix=26))[rng.randint(0, 3)]
    routes = [("0.0.0.0/0", "203.0.113.1", "S*"), (str(base), "10.0.12.2", "O"), (str(sub20), "10.0.13.3", "O"),
              (str(sub24), "10.0.14.4", "D"), (str(sub26), "10.0.15.5", "S")]
    pick = rng.choice(["26", "24", "20", "16", "0"])
    if pick == "26":
        dst, ans = sub26[rng.randint(1, 60)], "10.0.15.5"
    elif pick == "24":
        others = [n for n in sub24.subnets(new_prefix=26) if n != sub26]
        dst, ans = rng.choice(others)[rng.randint(1, 60)], "10.0.14.4"
    elif pick == "20":
        others = [n for n in sub20.subnets(new_prefix=24) if n != sub24]
        dst, ans = rng.choice(others)[rng.randint(1, 250)], "10.0.13.3"
    elif pick == "16":
        others = [n for n in base.subnets(new_prefix=20) if n != sub20]
        dst, ans = rng.choice(others)[rng.randint(1, 4000)], "10.0.12.2"
    else:
        dst, ans = ipaddress.ip_address(f"172.{rng.randint(16, 31)}.{rng.randint(0, 255)}.{rng.randint(1, 254)}"), "203.0.113.1"
    table = "; ".join(f"{c} {n} via {h}" for n, h, c in routes)
    return mcq(rng, f"A router has these routes: {table}. Which next hop is used for a packet to {dst}?", ans,
               [h for _, h, _ in routes if h != ans],
               f"Longest prefix match: the most specific route that contains {dst} wins, regardless of AD.", 3)


def q_ad(rng):
    srcs = {"eBGP": 20, "EIGRP (internal)": 90, "OSPF": 110, "RIP": 120, "static": 1, "iBGP": 200, "EIGRP external": 170}
    chosen = rng.sample(list(srcs.items()), 3)
    pfx = f"10.{rng.randint(0, 255)}.{rng.randint(0, 255)}.0/24"
    best = min(chosen, key=lambda t: t[1])
    names = ", ".join(n for n, _ in chosen)
    return mcq(rng, f"A router learns {pfx} from {names}. Which source is installed in the routing table (default ADs)?",
               best[0], [n for n, _ in chosen if n != best[0]] + ["All three, load-balanced"],
               f"Same prefix from different sources: lowest administrative distance wins. {best[0]} = {best[1]}.", 3)


def q_floating(rng):
    proto, ad = rng.choice([("OSPF", 110), ("EIGRP", 90), ("eBGP", 20), ("RIP", 120)])
    good = rng.choice([v for v in (121, 130, 150, 200, 250) if v > ad])
    return mcq(rng, f"The primary default route is learned by {proto}. Which administrative distance makes a backup static default route float (used only if the {proto} route is lost)?",
               str(good), [str(ad - 1) if ad > 1 else "0", "1", str(ad)],
               f"The static route needs an AD higher than {proto} ({ad}); equal AD would compete and a lower AD would win.", 3)


def q_ospf_cost(rng):
    ref = rng.choice([100, 1000, 10000, 100000])
    bw = rng.choice([10, 100, 1000, 10000])
    cost = max(1, ref // bw)
    wrong = [str(x) for x in dict.fromkeys([cost * 10, max(1, cost // 10), cost + 1, 1, 10, 100]) if x != cost][:3]
    return mcq(rng, f"OSPF uses auto-cost reference-bandwidth {ref} (Mbps). What is the cost of a {bw} Mbps interface?",
               str(cost), wrong,
               f"Cost = reference / interface bandwidth = {ref}/{bw} = {cost} (minimum 1).", 3)


D3_GENS = [q_lpm, q_ad, q_floating, q_ospf_cost, q_lpm, q_ad, q_lpm, q_ospf_cost, q_lpm]


# ------------------------------------------------------------------ domain 4 generators
def q_wildcard(rng):
    p = rng.randint(16, 30)
    mask = str(ipaddress.ip_network(f"0.0.0.0/{p}").netmask)
    wc = sc.wildcard(mask)
    wrong = [sc.wildcard(str(ipaddress.ip_network(f"0.0.0.0/{x}").netmask)) for x in (p + 1, p - 1, p - 2) if 8 <= x <= 32][:2] + [mask]
    return mcq(rng, f"Which wildcard mask matches the same addresses as subnet mask {mask} in an ACL?", wc, wrong,
               f"Wildcard = 255.255.255.255 − mask = {wc}.", 4)


def q_ace_match(rng):
    p = rng.choice([20, 21, 22, 27, 28, 29])
    net = ipaddress.ip_network(f"10.{rng.randint(0, 255)}.{rng.randint(0, 255)}.0/{p}", strict=False)
    wc = net.hostmask
    inside = net[rng.randint(1, net.num_addresses - 2)]
    outs = [net.broadcast_address + rng.randint(1, 200), net.network_address - rng.randint(1, 200),
            net.broadcast_address + net.num_addresses + 3, net.network_address - net.num_addresses - 7,
            net.broadcast_address + 2 * net.num_addresses + 11]
    return mcq(rng, f"An ACL entry is `permit ip {net.network_address} {wc} any`. Which source address matches it?",
               str(inside), [str(o) for o in outs],
               f"{net.network_address} {wc} covers {net.network_address}-{net.broadcast_address} ({net}).", 4)


D4_GENS = [q_wildcard, q_ace_match, q_wildcard, q_ace_match, q_ace_match, q_wildcard]


# ------------------------------------------------------------------ domain 5 generators
SEVERITY = ["emergencies", "alerts", "critical", "errors", "warnings", "notifications", "informational", "debugging"]


def q_syslog_level(rng):
    lvl = rng.randint(0, 7)
    return mcq(rng, f"Which syslog severity level number is '{SEVERITY[lvl]}'?", str(lvl),
               [str((lvl + d) % 8) for d in (1, 2, 7)],
               "0 emergencies, 1 alerts, 2 critical, 3 errors, 4 warnings, 5 notifications, 6 informational, 7 debugging.", 5)


def q_logging_trap(rng):
    lvl = rng.randint(1, 6)
    correct = f"Levels 0 through {lvl}"
    return mcq(rng, f"A router has `logging trap {SEVERITY[lvl]}`. Which messages are sent to the syslog server?", correct,
               [f"Level {lvl} only", f"Levels {lvl} through 7", "All levels 0 through 7"],
               f"The configured level ({lvl}) and every more severe (lower) level are sent.", 5)


def q_syslog_msg(rng):
    msgs = [("%LINEPROTO-5-UPDOWN", 5), ("%OSPF-5-ADJCHG", 5), ("%SYS-5-CONFIG_I", 5), ("%LINK-3-UPDOWN", 3),
            ("%SEC_LOGIN-4-LOGIN_FAILED", 4), ("%SPANTREE-2-BLOCK_BPDUGUARD", 2), ("%DUAL-5-NBRCHANGE", 5),
            ("%PM-4-ERR_DISABLE", 4), ("%SYS-6-LOGGINGHOST_STARTSTOP", 6)]
    m, lvl = rng.choice(msgs)
    return mcq(rng, f"What is the severity of the syslog message `{m}: ...`?", f"{lvl} ({SEVERITY[lvl]})",
               [f"{(lvl + d) % 8} ({SEVERITY[(lvl + d) % 8]})" for d in (1, 2, 6)],
               "Cisco format is %FACILITY-SEVERITY-MNEMONIC; the number after the facility is the severity.", 5)


D5_GENS = [q_syslog_level, q_logging_trap, q_syslog_msg]

GENERATORS = {1: D1_GENS, 2: D2_GENS, 3: D3_GENS, 4: D4_GENS, 5: D5_GENS}


# ------------------------------------------------------------------ build
def load_bank() -> dict[int, list[dict]]:
    bank: dict[int, list[dict]] = {}
    for d in DOMAINS:
        items = yaml.safe_load((BANK / f"d{d}.yaml").read_text(encoding="utf-8")) or []
        for it in items:
            it["d"] = d
            assert len(it["o"]) >= 4, it["q"]
            for a in str(it["a"]).replace(" ", "").split(","):
                assert a in LETTERS[: len(it["o"])], it["q"]
        bank[d] = items
    return bank


POSITIONAL = ("of the above", "Both A and B", "A and B", "None of these")


def shuffled(item: dict) -> dict:
    """Return a copy of a bank item with options shuffled (seeded by question text) and answers remapped."""
    if any(p in o for o in item["o"] for p in POSITIONAL):
        return item
    import hashlib

    order = list(range(len(item["o"])))
    random.Random(int(hashlib.sha256(item["q"].encode()).hexdigest(), 16) % 2**32).shuffle(order)
    mapping = {LETTERS[o]: LETTERS[k] for k, o in enumerate(order)}
    answers = sorted(mapping[a.strip()] for a in str(item["a"]).split(","))
    return {**item, "o": [item["o"][o] for o in order], "a": ",".join(answers)}


def build_exam(n: int, bank: dict[int, list[dict]]) -> list[dict]:
    rng = random.Random(1000 + n)
    questions: list[dict] = []
    for d, (_, total) in DOMAINS.items():
        hand = [q for i, q in enumerate(bank[d]) if i % 3 == n - 1]
        need_hand = total - COMPUTED_PER_EXAM[d]
        if len(hand) < need_hand:
            raise SystemExit(f"domain {d}: need {need_hand} hand-written questions for exam {n}, have {len(hand)}")
        questions += [shuffled(q) for q in hand[:need_hand]]
        gens = GENERATORS[d]
        for i in range(COMPUTED_PER_EXAM[d]):
            questions.append(gens[i % len(gens)](rng))
    rng.shuffle(questions)
    return questions


def to_markdown(n: int, questions: list[dict]) -> str:
    lines = [
        f"# CCNA 200-301 v2.0 — Practice Exam {n}",
        "",
        "**Format:** 100 questions · 120 minutes · target score 85% (the real passing score is not published; aim high).",
        "Original questions written for this repo, not exam dumps. Simulations are in [../labs/](../labs/README.md).",
        "",
        "Run interactively: `python3 tools/quiz_runner.py cert/ccna-200-301/practice-exams/exam-%d.md --shuffle`" % n,
        "",
        "| Domain | Questions |",
        "|---|---|",
    ]
    for d, (name, total) in DOMAINS.items():
        lines.append(f"| {d}.0 {name} | {total} |")
    lines += ["", "Rules: no notes, one sitting, mark questions to revisit, never leave a question blank.", "", "## Questions", ""]
    for i, q in enumerate(questions, 1):
        answers = [a.strip() for a in str(q["a"]).split(",")]
        multi = len(answers) > 1
        text = q["q"].strip().replace("\n", " ")
        if multi and "Choose" not in text:
            text += f" (Choose {len(answers)}.)"
        lines += [f"### Q{i}. {text}", ""]
        for k, opt in enumerate(q["o"]):
            lines.append(f"- {LETTERS[k]}) {opt}")
        lines += ["", "<details><summary>Answer</summary>", "",
                  f"**Answer: {', '.join(answers)}.** {q['e'].strip()} *(Domain {q['d']})*", "", "</details>", ""]
    return "\n".join(lines)


def main() -> int:
    bank = load_bank()
    for d in DOMAINS:
        print(f"domain {d}: {len(bank[d])} hand-written questions in bank")
    for n in (1, 2, 3):
        qs = build_exam(n, bank)
        assert len(qs) == 100, len(qs)
        out = CERT / f"exam-{n}.md"
        out.write_text(to_markdown(n, qs), encoding="utf-8")
        print(f"wrote {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
