# Quiz 05 — Switching

## Questions

### Q1. How many bits identify the VLAN in an 802.1Q tag?

- A) 12
- B) 10
- C) 16
- D) 8

<details><summary>Answer</summary>

**Answer: A.** The VID field is 12 bits, so VLANs 1-4094 are usable (0 and 4095 are reserved).

</details>

### Q2. Which frames does a trunk send without a tag?

- A) Frames in the voice VLAN
- B) Frames in the native VLAN
- C) Frames in VLAN 1 always
- D) No frames; all frames are tagged

<details><summary>Answer</summary>

**Answer: B.** The native VLAN is untagged (VLAN 1 by default, but you can change it). Both trunk ends must use the same native VLAN.

</details>

### Q3. Three switches have these bridge IDs for VLAN 10: SW1 32778.0011.1111.1111, SW2 32778.0011.0000.0001, SW3 28682.00aa.ffff.ffff. Which switch is the root bridge?

- A) SW2
- B) SW3
- C) The one with the most ports
- D) SW1

<details><summary>Answer</summary>

**Answer: B.** The lowest bridge ID wins. Priority is compared first: 28682 (28672 + 10) is lower than 32778, so SW3 wins even with the highest MAC.

</details>

### Q4. Scenario: A non-root switch has two paths to the root: via Gi0/1 with cost 4 + 4 and via Gi0/2 with cost 19. Which port becomes the root port?

- A) The port with the lowest port number regardless of cost
- B) Both, load balanced
- C) Gi0/1 with total cost 8
- D) Gi0/2 with total cost 19

<details><summary>Answer</summary>

**Answer: C.** The root port has the lowest total path cost to the root. 8 is less than 19.

</details>

### Q5. Which RSTP port role is a backup path to the root bridge through a different switch?

- A) Backup
- B) Designated
- C) Edge
- D) Alternate

<details><summary>Answer</summary>

**Answer: D.** Alternate = an alternative path to the root via another switch. Backup = a redundant port to the same segment (rare, needs a shared medium). Designated forwards toward a segment.

</details>

### Q6. What does BPDU guard do when a BPDU arrives on an enabled port?

- A) Moves the port to the native VLAN
- B) Makes the port the root port
- C) Places the port in err-disabled state
- D) Ignores the BPDU

<details><summary>Answer</summary>

**Answer: C.** BPDU guard err-disables the port. It is used with PortFast on access ports to stop rogue switches and loops.

</details>

### Q7. Which feature puts a port in a root-inconsistent state if a superior BPDU arrives?

- A) Root guard
- B) BPDU filter
- C) UplinkFast
- D) Loop guard

<details><summary>Answer</summary>

**Answer: A.** Root guard protects the location of the root bridge. When a superior BPDU arrives, the port blocks (root-inconsistent) until the superior BPDUs stop.

</details>

### Q8. Which pair of LACP modes forms an EtherChannel?

- A) active / passive
- B) passive / passive
- C) on / active
- D) auto / auto

<details><summary>Answer</summary>

**Answer: A.** LACP forms with active-active or active-passive. Passive-passive never starts negotiation. auto/desirable are PAgP modes. "on" does not negotiate and does not work with an LACP peer.

</details>

### Q9. Scenario: `show etherchannel summary` shows `Po1(SD)` and both members show `(s)` (suspended). What is a likely cause?

- A) STP is disabled
- B) Member ports have mismatched settings, such as different allowed VLANs or speed
- C) CDP is disabled
- D) The port-channel has an IP address

<details><summary>Answer</summary>

**Answer: B.** Suspended members usually have a configuration mismatch with the bundle (speed, duplex, trunk/access mode, allowed VLANs, native VLAN) or the peer is not in a matching channel group.

</details>

### Q10. Which port security violation mode drops offending traffic, increments the violation counter and sends a log, but keeps the port up?

- A) protect
- B) shutdown
- C) sticky
- D) restrict

<details><summary>Answer</summary>

**Answer: D.** restrict drops, counts and logs. protect drops silently. shutdown err-disables the port (default). sticky is a way to learn MACs, not a violation mode.

</details>

### Q11. Which command shows which VLANs are allowed and active on each trunk?

- A) show interfaces trunk
- B) show spanning-tree summary
- C) show mac address-table
- D) show vlan brief

<details><summary>Answer</summary>

**Answer: A.** `show interfaces trunk` lists trunk ports, the native VLAN, allowed VLANs, active VLANs and VLANs in STP forwarding state. `show vlan brief` lists access ports only.

</details>

### Q12. Scenario: Users in VLAN 10 on SW1 can reach VLAN 10 users on SW2, but VLAN 30 users on SW1 cannot reach VLAN 30 users on SW2. VLAN 30 exists on both switches. What do you check first?

- A) The default gateway on the PCs
- B) The OSPF configuration
- C) The DNS server
- D) The allowed VLAN list on the trunk between SW1 and SW2

<details><summary>Answer</summary>

**Answer: D.** Same-VLAN traffic across switches needs the VLAN to be allowed on the trunk. VLAN 10 works, so the trunk is up; VLAN 30 is probably missing from the allowed list.

</details>

### Q13. Which TWO statements about LLDP are correct? (Choose two.)

- A) It is enabled by default on all Cisco IOS switches
- B) It works with multi-vendor devices
- C) It is a Layer 3 routing protocol
- D) It is an IEEE standard (802.1AB)
- E) It requires an IP address on the interface

<details><summary>Answer</summary>

**Answer: B, D.** LLDP is the IEEE 802.1AB vendor-neutral discovery protocol at Layer 2. On many Cisco IOS devices it is off by default (`lldp run` enables it). CDP is Cisco proprietary and on by default.

</details>

### Q14. What is the purpose of the command `spanning-tree vlan 10 root primary`?

- A) It makes all ports designated
- B) It disables STP on VLAN 10
- C) It enables root guard
- D) It sets the priority low enough for the switch to become root for VLAN 10

<details><summary>Answer</summary>

**Answer: D.** It sets the priority to 24576, or lower than the current root if needed, so the switch becomes the root for VLAN 10. `root secondary` sets 28672 for a backup root.

</details>

### Q15. Scenario: A Layer 3 switch has SVIs for VLAN 10 and VLAN 20, but hosts in different VLANs cannot ping each other. Both SVIs are up/up. What global command is probably missing?

- A) `ip routing`
- B) `vlan routing`
- C) `spanning-tree mode rapid-pvst`
- D) `ip default-gateway`

<details><summary>Answer</summary>

**Answer: A.** A Layer 3 switch routes between SVIs only after `ip routing` is enabled. Without it, it acts like a Layer 2 switch with management IPs.

</details>
