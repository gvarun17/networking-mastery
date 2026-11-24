import copy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import netintent  # noqa: E402

GOOD = netintent.load()


def test_repo_intent_is_valid():
    assert netintent.validate(GOOD) == []


def test_link_ends_must_share_a_slash31():
    bad = copy.deepcopy(GOOD)
    bad["links"][0]["b"]["ip"] = "10.0.12.3"
    assert any("same /31" in e for e in netintent.validate(bad))


def test_duplicate_asn_detected():
    bad = copy.deepcopy(GOOD)
    bad["routers"]["r2"]["asn"] = 65001
    assert any("already used" in e for e in netintent.validate(bad))


def test_public_asn_rejected():
    bad = copy.deepcopy(GOOD)
    bad["routers"]["r3"]["asn"] = 16509
    assert any("private" in e for e in netintent.validate(bad))


def test_interface_reuse_detected():
    bad = copy.deepcopy(GOOD)
    bad["links"][1]["a"]["interface"] = "eth1"
    assert any("used twice" in e for e in netintent.validate(bad))


def test_render_contains_every_neighbor():
    configs = netintent.render(GOOD)
    assert set(configs) == {"r1", "r2", "r3"}
    assert "neighbor 10.0.12.1 remote-as 65002" in configs["r1"]
    assert "neighbor 10.0.13.1 remote-as 65003" in configs["r1"]
    assert "network 10.255.0.2/32" in configs["r2"]


def test_expected_peers():
    assert netintent.expected_peers(GOOD)["r3"] == {"10.0.13.0", "10.0.23.0"}
