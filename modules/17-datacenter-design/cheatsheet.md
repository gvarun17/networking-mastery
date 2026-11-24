# Cheatsheet 17 — Data Center and Modern Design

## Spine-leaf rules

- Every leaf → every spine. No leaf-leaf, no spine-spine links (except MLAG peer links if used).
- Routed underlay, ECMP, BFD. No STP in the fabric.
- Oversubscription = downlink Gbps / uplink Gbps.

## Encapsulations

| | Port | Header | ID bits |
|---|---|---|---|
| VXLAN | UDP 4789 | 8 B | VNI 24 |
| Geneve | UDP 6081 | 8 B + options | VNI 24 |
| GRE | IP 47 | 4-16 B | key 32 |
| MPLS | EtherType 0x8847 | 4 B per label | label 20 |

VXLAN total overhead (IPv4) = 50 B (IPv6 outer: 70 B).

## EVPN route types

| Type | Name | Use |
|---|---|---|
| 1 | Ethernet A-D | Multihoming |
| 2 | MAC/IP | Hosts, ARP suppression |
| 3 | Inclusive multicast | BUM flood list |
| 4 | Ethernet segment | DF election |
| 5 | IP prefix | L3 routes in VRF |

## FRR commands

```text
show bgp summary
show bgp l2vpn evpn summary
show bgp l2vpn evpn route type macip | multicast | prefix
show evpn vni [detail]
show evpn mac vni 100
show evpn arp-cache vni 100
show ip route vrf all
```

## Linux VXLAN

```text
ip link add vxlan100 type vxlan id 100 dstport 4789 local 10.255.1.1 nolearning
ip link set vxlan100 master br100 up
bridge fdb show dev vxlan100
ip -d link show vxlan100
tcpdump -nn udp port 4789
```

## FRR leaf skeleton

```text
router bgp 65101
 neighbor FABRIC peer-group
 neighbor FABRIC remote-as external
 neighbor eth1 interface peer-group FABRIC
 address-family ipv4 unicast
  network 10.255.1.1/32
 address-family l2vpn evpn
  neighbor FABRIC activate
  advertise-all-vni
```

## SD-WAN components (Cisco Catalyst SD-WAN)

Manager (vManage) · Controller (vSmart, OMP) · Validator (vBond) · WAN Edge (cEdge/vEdge) · BFD probes per tunnel · app-aware routing · ZTP.

## SDN vocabulary

Control plane / data plane / management plane · northbound API / southbound API · OpenFlow · intent-based networking · Cisco ACI (APIC), SD-Access (Catalyst Center, LISP + VXLAN).
