#!/usr/bin/env bash
# Install the free lab toolchain on Ubuntu 22.04/24.04 (native or WSL2).
# Usage: bash labs/setup/install.sh [--no-docker] [--no-k8s] [--no-cloud]
# Safe to run more than once. Read it before you run it.
set -euo pipefail

WANT_DOCKER=1; WANT_K8S=1; WANT_CLOUD=1
for a in "$@"; do
  case "$a" in
    --no-docker) WANT_DOCKER=0 ;;
    --no-k8s) WANT_K8S=0 ;;
    --no-cloud) WANT_CLOUD=0 ;;
    *) echo "unknown option $a"; exit 1 ;;
  esac
done

ARCH=$(dpkg --print-architecture)          # amd64 or arm64
. /etc/os-release
echo "==> Ubuntu ${VERSION_ID} (${ARCH})"
if grep -qi microsoft /proc/version; then
  echo "==> WSL2 detected. Make sure systemd is enabled in /etc/wsl.conf ([boot] systemd=true)."
fi

echo "==> Base networking tools"
sudo apt-get update -y
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y \
  iproute2 iputils-ping iputils-arping traceroute tcptraceroute mtr-tiny iperf3 \
  tcpdump tshark nmap dnsutils netcat-openbsd ethtool bridge-utils conntrack nftables \
  wireguard-tools softflowd snmp snmpd chrony curl wget jq git unzip ca-certificates gnupg \
  python3 python3-venv python3-pip ipcalc whois openssl

if [[ $WANT_DOCKER == 1 ]]; then
  echo "==> Docker Engine"
  if ! command -v docker >/dev/null; then
    sudo install -m 0755 -d /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    echo "deb [arch=${ARCH} signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu ${VERSION_CODENAME} stable" \
      | sudo tee /etc/apt/sources.list.d/docker.list >/dev/null
    sudo apt-get update -y
    sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    sudo usermod -aG docker "$USER"
    echo "   Log out and in again (or run 'newgrp docker') to use docker without sudo."
  fi

  echo "==> Containerlab"
  if ! command -v containerlab >/dev/null; then
    bash -c "$(curl -sL https://get.containerlab.dev)"
  fi

  echo "==> Pre-pulling lab images (FRR, SR Linux, netshoot)"
  for img in quay.io/frrouting/frr:10.2.1 ghcr.io/nokia/srlinux:24.10 nicolaka/netshoot:latest; do
    sudo docker pull "$img" || echo "   could not pull $img (pull later)"
  done
fi

if [[ $WANT_K8S == 1 ]]; then
  echo "==> kubectl, kind, helm, cilium and hubble CLIs"
  KVER=$(curl -fsSL https://dl.k8s.io/release/stable.txt)
  curl -fsSLo /tmp/kubectl "https://dl.k8s.io/release/${KVER}/bin/linux/${ARCH}/kubectl"
  sudo install -m 0755 /tmp/kubectl /usr/local/bin/kubectl
  KIND_VER=$(curl -fsSL https://api.github.com/repos/kubernetes-sigs/kind/releases/latest | jq -r .tag_name)
  curl -fsSLo /tmp/kind "https://kind.sigs.k8s.io/dl/${KIND_VER}/kind-linux-${ARCH}"
  sudo install -m 0755 /tmp/kind /usr/local/bin/kind
  curl -fsSL https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
  CILIUM_CLI=$(curl -fsSL https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt)
  curl -fsSL "https://github.com/cilium/cilium-cli/releases/download/${CILIUM_CLI}/cilium-linux-${ARCH}.tar.gz" | sudo tar xz -C /usr/local/bin
  HUBBLE=$(curl -fsSL https://raw.githubusercontent.com/cilium/hubble/master/stable.txt)
  curl -fsSL "https://github.com/cilium/hubble/releases/download/${HUBBLE}/hubble-linux-${ARCH}.tar.gz" | sudo tar xz -C /usr/local/bin
fi

if [[ $WANT_CLOUD == 1 ]]; then
  echo "==> Terraform (HashiCorp apt repo)"
  if ! command -v terraform >/dev/null; then
    curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp.gpg
    echo "deb [signed-by=/usr/share/keyrings/hashicorp.gpg] https://apt.releases.hashicorp.com ${VERSION_CODENAME} main" \
      | sudo tee /etc/apt/sources.list.d/hashicorp.list >/dev/null
    sudo apt-get update -y && sudo apt-get install -y terraform
  fi
  echo "==> AWS CLI v2"
  if ! command -v aws >/dev/null; then
    AWSARCH=$([[ $ARCH == arm64 ]] && echo aarch64 || echo x86_64)
    curl -fsSLo /tmp/awscliv2.zip "https://awscli.amazonaws.com/awscli-exe-linux-${AWSARCH}.zip"
    unzip -qo /tmp/awscliv2.zip -d /tmp && sudo /tmp/aws/install --update
  fi
  echo "==> LocalStack CLI and tflocal (in a venv at ~/.venvs/localstack)"
  python3 -m venv ~/.venvs/localstack
  ~/.venvs/localstack/bin/pip install -q localstack terraform-local awscli-local
fi

echo "==> Python lab tools (venv at ~/.venvs/netlab)"
python3 -m venv ~/.venvs/netlab
~/.venvs/netlab/bin/pip install -q pyyaml pytest netmiko nornir nornir-netmiko nornir-utils ncclient pygnmi jinja2 ansible-core

echo
echo "Done. Next: run 'bash labs/setup/verify.sh'."
echo "Packet Tracer is a manual download: see labs/setup/packet-tracer.md."
