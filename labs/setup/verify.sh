#!/usr/bin/env bash
# Check that the lab toolchain is installed. Prints OK/MISSING per tool and a summary.
set -uo pipefail

missing=0
check() {
  local name=$1; shift
  if "$@" >/dev/null 2>&1; then
    printf "  %-14s OK\n" "$name"
  else
    printf "  %-14s MISSING\n" "$name"; missing=$((missing + 1))
  fi
}

echo "Core tools"
for t in ip tcpdump tshark mtr iperf3 nmap dig nc ethtool conntrack nft wg jq python3; do
  check "$t" command -v "$t"
done
echo "Containers"
check docker docker version
check compose docker compose version
check containerlab containerlab version
echo "Kubernetes"
for t in kubectl kind helm cilium hubble; do check "$t" command -v "$t"; done
echo "Cloud"
check terraform terraform version
check aws aws --version
check localstack test -x "$HOME/.venvs/localstack/bin/localstack"
echo "Python lab venv"
check netlab-venv "$HOME/.venvs/netlab/bin/python" -c "import nornir, netmiko, ncclient"
echo "Kernel features"
check netns sudo ip netns add verify-ns-test
sudo ip netns del verify-ns-test 2>/dev/null || true
check vxlan sudo modprobe vxlan

echo
if [[ $missing -eq 0 ]]; then
  echo "All tools present. Start with modules/01-osi-tcpip/README.md."
else
  echo "$missing item(s) missing. Re-run labs/setup/install.sh or install them by hand."
fi
exit "$missing"
