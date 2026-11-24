# Cheatsheet 07 — Dynamic Routing

## Protocol facts

| | OSPF | EIGRP | BGP |
|---|---|---|---|
| Type | Link state | Advanced DV | Path vector |
| Transport | IP 89 | IP 88 | TCP 179 |
| Multicast | 224.0.0.5 / .6, ff02::5 / ::6 | 224.0.0.10, ff02::a | none (unicast) |
| AD | 110 | 90 / 170 | 20 eBGP / 200 iBGP |
| Metric | Cost = ref BW / BW | BW + delay | Attributes |
| Hello/dead | 10/40 (broadcast, P2P), 30/120 (NBMA) | 5/15 | Keepalive 60 / hold 180 |

## OSPF config (IOS)

```text
router ospf 1
 router-id 1.1.1.1
 auto-cost reference-bandwidth 100000
 passive-interface default
 no passive-interface g0/0
 network 10.0.12.0 0.0.0.3 area 0
 default-information originate [always]
 area 1 range 10.1.0.0 255.255.0.0      ! summarize on ABR
interface g0/0
 ip ospf 1 area 0
 ip ospf network point-to-point
 ip ospf priority 0                     ! never DR
 ip ospf cost 10
 ip ospf hello-interval 10
```

## OSPF show commands

| Command | Shows |
|---|---|
| `show ip ospf neighbor` | State, DR/BDR, dead time |
| `show ip ospf interface [brief]` | Area, cost, network type, timers, DR |
| `show ip ospf database` | LSDB by LSA type |
| `show ip route ospf` | O, O IA, O E1/E2, O N1/N2 |
| `show ip protocols` | RID, networks, passive interfaces |
| `clear ip ospf process` | Restart (applies new RID) |

## OSPF states

Down → Init → 2-Way → ExStart → Exchange → Loading → Full

| Stuck in | Usual cause |
|---|---|
| Init | One-way hellos (ACL, multicast blocked) |
| 2-Way | Normal for DROTHERs |
| ExStart/Exchange | MTU mismatch, duplicate RID |

## LSA types

1 Router · 2 Network (DR) · 3 Summary (ABR) · 4 ASBR summary · 5 External (ASBR) · 7 NSSA external

## BGP config (IOS)

```text
router bgp 65001
 bgp router-id 1.1.1.1
 neighbor 203.0.113.2 remote-as 65002
 neighbor 203.0.113.2 password S3cret
 address-family ipv4 unicast
  network 198.51.100.0 mask 255.255.255.0
  neighbor 203.0.113.2 activate
  neighbor 203.0.113.2 prefix-list IN in
  neighbor 203.0.113.2 route-map PREPEND out
  neighbor 203.0.113.2 maximum-prefix 1000
route-map PREPEND permit 10
 set as-path prepend 65001 65001
```

| Command | Shows |
|---|---|
| `show ip bgp summary` | Peers, state, prefixes received |
| `show ip bgp` | BGP table (`*` valid, `>` best, `i` iBGP) |
| `show ip bgp neighbors X advertised-routes` | What you send |
| `show ip bgp neighbors X routes` | What you accept |
| `clear ip bgp X soft` | Re-apply policy without reset |

## BGP best path (Cisco)

Weight ↑ → Local pref ↑ → Locally originated → AS path ↓ → Origin (i < e < ?) → MED ↓ → eBGP > iBGP → IGP metric to next hop ↓ → oldest → router ID ↓ → neighbor IP ↓

## FRR equivalents

| IOS | FRR (vtysh) |
|---|---|
| `show ip ospf neighbor` | same |
| `show ip bgp summary` | `show bgp ipv4 unicast summary` |
| `ip ospf 1 area 0` | `ip ospf area 0` |
| — | `no bgp ebgp-requires-policy` (RFC 8212 default) |
