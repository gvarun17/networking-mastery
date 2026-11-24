# Quiz 03 — IPv4 Addressing and Subnetting

## Questions

### Q1. What is the network address of 10.20.33.200/27?

- A) 10.20.33.160
- B) 10.20.33.192
- C) 10.20.33.200
- D) 10.20.33.224

<details><summary>Answer</summary>

**Answer: B.** /27 → block size 32 in the fourth octet. Multiples of 32: 160, 192, 224. 200 falls in 192-223, so the network is 10.20.33.192.

</details>

### Q2. What is the broadcast address of 172.16.45.130/21?

- A) 172.16.45.255
- B) 172.16.47.255
- C) 172.16.48.255
- D) 172.16.63.255

<details><summary>Answer</summary>

**Answer: B.** /21 → mask 255.255.248.0, block 8 in the third octet. 45 is in 40-47. Network 172.16.40.0, broadcast 172.16.47.255.

</details>

### Q3. How many usable host addresses does a /23 provide?

- A) 254
- B) 510
- C) 512
- D) 1022

<details><summary>Answer</summary>

**Answer: B.** 32 − 23 = 9 host bits. 2^9 − 2 = 510.

</details>

### Q4. Which subnet mask gives at least 25 usable hosts with the fewest wasted addresses?

- A) 255.255.255.192
- B) 255.255.255.224
- C) 255.255.255.240
- D) 255.255.255.248

<details><summary>Answer</summary>

**Answer: B.** /27 (255.255.255.224) gives 30 usable hosts. /28 gives only 14. /26 gives 62, which wastes more.

</details>

### Q5. Scenario: Host A is 192.168.5.33/27 and Host B is 192.168.5.65/27. They connect to the same switch and VLAN with no router. Can they ping each other?

- A) Yes, because they are in the same VLAN
- B) Yes, because they share the same first three octets
- C) No, because they are in different subnets and need a router
- D) No, because .65 is a broadcast address

<details><summary>Answer</summary>

**Answer: C.** A is in 192.168.5.32/27 (.32-.63). B is in 192.168.5.64/27 (.64-.95). Each host sends off-subnet traffic to a default gateway. Without a router, they cannot communicate. .65 is a valid host address.

</details>

### Q6. Which address is a valid host address in 10.0.77.16/28?

- A) 10.0.77.16
- B) 10.0.77.31
- C) 10.0.77.30
- D) 10.0.77.32

<details><summary>Answer</summary>

**Answer: C.** 10.0.77.16/28 covers .16-.31. .16 is the network, .31 is the broadcast and .32 is in the next subnet. .30 is the last usable host.

</details>

### Q7. What is the wildcard mask for 255.255.240.0?

- A) 0.0.15.255
- B) 0.0.16.255
- C) 0.0.240.255
- D) 255.255.15.0

<details><summary>Answer</summary>

**Answer: A.** Subtract each octet from 255: 255−255=0, 255−255=0, 255−240=15, 255−0=255 → 0.0.15.255.

</details>

### Q8. Which single route summarizes 172.16.32.0/24 through 172.16.39.0/24 exactly?

- A) 172.16.32.0/20
- B) 172.16.32.0/21
- C) 172.16.32.0/22
- D) 172.16.0.0/16

<details><summary>Answer</summary>

**Answer: B.** Eight /24s = one /21 (8 = 2^3, so 24 − 3 = 21). 32 is a multiple of 8, so the block is aligned: 172.16.32.0-172.16.39.255.

</details>

### Q9. Which range is reserved for carrier-grade NAT and often used for EKS secondary CIDRs?

- A) 169.254.0.0/16
- B) 100.64.0.0/10
- C) 192.0.2.0/24
- D) 240.0.0.0/4

<details><summary>Answer</summary>

**Answer: B.** RFC 6598 shared address space is 100.64.0.0/10. 169.254/16 is link-local, 192.0.2.0/24 is documentation and 240/4 is reserved.

</details>

### Q10. How many usable IP addresses does an AWS subnet of /28 have?

- A) 16
- B) 14
- C) 11
- D) 8

<details><summary>Answer</summary>

**Answer: C.** 16 addresses minus 5 reserved by AWS (network, VPC router, DNS, future use, broadcast) = 11. /28 is the smallest subnet AWS allows.

</details>

### Q11. You split 192.168.10.0/24 into /27 subnets. What is the fifth subnet?

- A) 192.168.10.96/27
- B) 192.168.10.128/27
- C) 192.168.10.160/27
- D) 192.168.10.192/27

<details><summary>Answer</summary>

**Answer: B.** /27 subnets start at .0, .32, .64, .96, .128. The fifth is .128.

</details>

### Q12. Which prefix should you use on a router-to-router point-to-point link to use only two addresses with no waste, as permitted by RFC 3021?

- A) /29
- B) /30
- C) /31
- D) /32

<details><summary>Answer</summary>

**Answer: C.** RFC 3021 allows /31 on point-to-point links, with both addresses usable and no network or broadcast. /30 is the classic CCNA answer but wastes two addresses.

</details>

### Q13. Scenario: An engineer configures `ip address 10.1.1.64 255.255.255.192` on a router interface. IOS rejects it. Why?

- A) 10.1.1.64 is the broadcast address of the /26
- B) 10.1.1.64 is the network address of the /26
- C) The mask is invalid
- D) 10.1.1.64 is a multicast address

<details><summary>Answer</summary>

**Answer: B.** /26 blocks are .0, .64, .128, .192. 10.1.1.64 is the network address of 10.1.1.64/26, so it cannot be assigned to an interface. IOS shows "Bad mask /26 for address 10.1.1.64".

</details>

### Q14. Which TWO addresses are RFC 1918 private addresses? (Choose two.)

- A) 172.32.1.1
- B) 172.20.5.5
- C) 192.169.1.1
- D) 10.255.255.254
- E) 100.64.0.1

<details><summary>Answer</summary>

**Answer: B, D.** RFC 1918: 10.0.0.0/8, 172.16.0.0/12 (172.16-172.31) and 192.168.0.0/16. 172.32 is public, 192.169 is public and 100.64 is shared CGNAT space, not RFC 1918.

</details>

### Q15. Scenario: You must allocate 10.10.0.0/22 for subnets of 500, 200 and 100 hosts, largest first. What is the network address of the 100-host subnet?

- A) 10.10.2.0/25
- B) 10.10.3.0/25
- C) 10.10.3.128/25
- D) 10.10.2.128/25

<details><summary>Answer</summary>

**Answer: B.** 500 hosts → /23 = 10.10.0.0-10.10.1.255. 200 hosts → /24 = 10.10.2.0. 100 hosts → /25 = 10.10.3.0. Check: `python3 tools/subnet_calc.py vlsm 10.10.0.0/22 --hosts 500 200 100`.

</details>
