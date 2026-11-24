#!/usr/bin/env bash
# Module 13 fault-injection lab.
# Usage:
#   sudo ./faults.sh build          # create the topology
#   sudo ./faults.sh inject <1-10>  # inject one fault (or "random")
#   sudo ./faults.sh reset          # rebuild a clean topology
#   sudo ./faults.sh destroy
# Topology: client (10.13.1.10) - router (10.13.1.1 | 10.13.2.1) - server (10.13.2.20)
# Server runs: HTTP on 8080, a DNS-like UDP echo on 5353, SSH-like TCP listener on 2222.
set -euo pipefail

NS=(client router server)

destroy() {
  for n in "${NS[@]}"; do ip netns del "$n" 2>/dev/null || true; done
}

build() {
  destroy
  for n in "${NS[@]}"; do ip netns add "$n"; ip -n "$n" link set lo up; done
  ip link add c-eth0 type veth peer name r-eth0
  ip link add s-eth0 type veth peer name r-eth1
  ip link set c-eth0 netns client; ip link set r-eth0 netns router
  ip link set r-eth1 netns router; ip link set s-eth0 netns server
  ip -n client addr add 10.13.1.10/24 dev c-eth0
  ip -n router addr add 10.13.1.1/24 dev r-eth0
  ip -n router addr add 10.13.2.1/24 dev r-eth1
  ip -n server addr add 10.13.2.20/24 dev s-eth0
  for pair in client:c-eth0 router:r-eth0 router:r-eth1 server:s-eth0; do
    ip -n "${pair%%:*}" link set "${pair##*:}" up
  done
  ip -n client route add default via 10.13.1.1
  ip -n server route add default via 10.13.2.1
  ip netns exec router sysctl -qw net.ipv4.ip_forward=1
  mkdir -p /tmp/m13www && echo "hello" > /tmp/m13www/index.html
  head -c 200000 /dev/urandom > /tmp/m13www/big.bin
  ip netns exec server sh -c 'cd /tmp/m13www && python3 -m http.server 8080 --bind 10.13.2.20 >/dev/null 2>&1 &'
  ip netns exec server sh -c 'nc -lk 10.13.2.20 2222 >/dev/null 2>&1 &' || true
  echo "nameserver 10.13.2.20" > /tmp/m13-resolv.conf
  echo "Built. Test: sudo ip netns exec client curl -s -o /dev/null -w '%{http_code}\n' http://10.13.2.20:8080/"
}

inject() {
  local n="$1"
  if [[ "$n" == "random" ]]; then n=$(( (RANDOM % 10) + 1 )); fi
  case "$n" in
    1) ip -n client link set c-eth0 down ;;                                         # L1/L2 link down
    2) ip -n client route del default ;;                                             # missing default route
    3) ip -n server route del default ;;                                             # missing return route
    4) ip netns exec router sysctl -qw net.ipv4.ip_forward=0 ;;                      # router not forwarding
    5) ip -n client addr del 10.13.1.10/24 dev c-eth0
       ip -n client addr add 10.13.1.10/30 dev c-eth0
       ip -n client route add default via 10.13.1.1 2>/dev/null || true ;;           # wrong mask
    6) ip netns exec router nft 'add table inet f; add chain inet f fwd { type filter hook forward priority 0; }; add rule inet f fwd tcp dport 8080 drop' ;;   # silent drop
    7) ip netns exec server nft 'add table inet f; add chain inet f in { type filter hook input priority 0; }; add rule inet f in tcp dport 8080 reject with tcp reset' ;;  # reject
    8) pkill -f "http.server 8080" || true ;;                                        # service down
    9) ip -n router link set r-eth0 mtu 1200
       ip netns exec router nft 'add table inet f; add chain inet f out { type filter hook output priority 0; }; add rule inet f out icmp type destination-unreachable drop' ;;  # MTU black hole (router cannot send frag-needed)
    10) ip netns exec router tc qdisc add dev r-eth1 root netem delay 150ms loss 5% ;; # latency + loss
    *) echo "fault must be 1-10 or random"; exit 1 ;;
  esac
  echo "Fault injected. Ticket: 'The client cannot use the web app on 10.13.2.20:8080, or it is slow, or big downloads (/big.bin) hang.'"
  echo "Diagnose, then run: sudo $0 reset"
}

case "${1:-}" in
  build) build ;;
  inject) inject "${2:?fault number}" ;;
  reset) build ;;
  destroy) destroy ;;
  *) sed -n '2,9p' "$0"; exit 1 ;;
esac
