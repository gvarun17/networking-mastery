import ipaddress
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import subnet_calc as sc  # noqa: E402


def test_info_slash27():
    s = sc.info("192.168.10.77/27")
    assert s.network == "192.168.10.64"
    assert s.broadcast == "192.168.10.95"
    assert (s.first_host, s.last_host) == ("192.168.10.65", "192.168.10.94")
    assert s.usable_hosts == 30
    assert s.wildcard == "0.0.0.31"


def test_info_slash21():
    s = sc.info("172.16.45.130/21")
    assert s.network == "172.16.40.0"
    assert s.broadcast == "172.16.47.255"
    assert s.usable_hosts == 2046


def test_slash31_and_32():
    assert sc.info("10.1.1.0/31").usable_hosts == 2
    assert sc.info("10.1.1.0/31").broadcast is None
    assert sc.info("10.1.1.1/32").usable_hosts == 1


def test_ipv6_info():
    s = sc.info("2001:db8:acad::1/64")
    assert s.network == "2001:db8:acad::"
    assert s.broadcast is None


def test_prefix_for_hosts():
    assert sc.prefix_for_hosts(2) == 30
    assert sc.prefix_for_hosts(30) == 27
    assert sc.prefix_for_hosts(31) == 26
    assert sc.prefix_for_hosts(500) == 23


def test_vlsm_no_overlap():
    alloc = sc.vlsm("172.16.0.0/24", [100, 50, 25, 2, 2])
    nets = [n for _, n in alloc]
    assert str(nets[0]) == "172.16.0.0/25"
    for i, a in enumerate(nets):
        for b in nets[i + 1:]:
            assert not a.overlaps(b)


def test_summarize_and_supernet():
    nets = ["10.1.4.0/24", "10.1.5.0/24", "10.1.6.0/24", "10.1.7.0/24"]
    assert [str(n) for n in sc.summarize(nets)] == ["10.1.4.0/22"]
    assert str(sc.supernet(["10.0.1.0/24", "10.0.2.0/24"])) == "10.0.0.0/22"


def test_wildcard():
    assert sc.wildcard("255.255.240.0") == "0.0.15.255"


def test_same_subnet():
    assert sc.same_subnet("10.0.0.5/30", "10.0.0.6/30")
    assert not sc.same_subnet("10.0.0.6/30", "10.0.0.9/30")


def test_practice_is_deterministic():
    assert sc.practice_problems(6, 1) == sc.practice_problems(6, 1)


def test_split_count():
    assert len(sc.split("10.0.0.0/22", 24)) == 4
    assert sc.split("10.0.0.0/22", 24)[3] == ipaddress.ip_network("10.0.3.0/24")


def test_cli_runs(capsys):
    assert sc.main(["info", "10.0.0.1/24"]) == 0
    assert "10.0.0.0/24" in capsys.readouterr().out
