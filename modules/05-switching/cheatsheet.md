# Cheatsheet 05 — Switching

## VLANs and trunks

```text
vlan 10
 name USERS
interface g0/1
 switchport mode access
 switchport access vlan 10
 switchport voice vlan 150
interface g0/24
 switchport trunk encapsulation dot1q     ! only on platforms that support ISL
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 10,20,99
 switchport trunk allowed vlan add 30
 switchport nonegotiate                   ! disable DTP
```

| Show command | Purpose |
|---|---|
| `show vlan brief` | VLANs and access ports |
| `show interfaces trunk` | Trunks, native, allowed, active VLANs |
| `show interfaces g0/1 switchport` | Mode, access/native VLAN, DTP |
| `show mac address-table vlan 10` | MACs per VLAN |

## DTP modes

| Local \ Remote | dynamic auto | dynamic desirable | trunk | access |
|---|---|---|---|---|
| dynamic auto | access | trunk | trunk | access |
| dynamic desirable | trunk | trunk | trunk | access |
| trunk | trunk | trunk | trunk | limited/mismatch |

Best practice: hard-code `switchport mode trunk` + `switchport nonegotiate`, or `switchport mode access`.

## STP

```text
spanning-tree mode rapid-pvst
spanning-tree vlan 10 root primary          ! priority 24576
spanning-tree vlan 10 priority 4096         ! multiples of 4096
spanning-tree portfast default
spanning-tree portfast bpduguard default
interface g0/1
 spanning-tree portfast
 spanning-tree bpduguard enable
 spanning-tree guard root
 spanning-tree guard loop
 spanning-tree vlan 10 cost 10
show spanning-tree vlan 10
show spanning-tree root
show spanning-tree summary
show spanning-tree inconsistentports
```

| Item | Value |
|---|---|
| Default priority | 32768 (+ VLAN ID) |
| Priority steps | 4096 |
| Hello / Max age / Fwd delay | 2 s / 20 s / 15 s |
| BPDU MAC | 01:80:c2:00:00:00 (PVST+ uses 01:00:0c:cc:cc:cd) |

Election order: lowest bridge ID → lowest root path cost → lowest sender bridge ID → lowest sender port ID.

## EtherChannel

```text
interface range g0/1-2
 channel-group 1 mode active        ! LACP
interface port-channel 1
 switchport mode trunk
port-channel load-balance src-dst-ip
show etherchannel summary
show lacp neighbor
```

Flags: `P` bundled, `I` stand-alone, `s` suspended, `D` down, `S` Layer 2, `R` Layer 3, `U` in use.

## Port security

```text
switchport port-security
switchport port-security maximum 2
switchport port-security mac-address sticky
switchport port-security violation {protect|restrict|shutdown}
show port-security interface g0/5
show interfaces status err-disabled
errdisable recovery cause psecure-violation
errdisable recovery interval 300
```

## CDP / LLDP

```text
show cdp neighbors [detail]
no cdp enable            ! per interface
lldp run
show lldp neighbors [detail]
```
