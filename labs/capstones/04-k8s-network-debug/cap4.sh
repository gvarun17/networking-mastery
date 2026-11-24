#!/usr/bin/env bash
# Capstone 4 helper.
#   ./cap4.sh up            create kind cluster, install Calico, deploy the app
#   ./cap4.sh break <1-7>   inject a fault (or "random")
#   ./cap4.sh reset         remove all faults and redeploy the app
#   ./cap4.sh down          delete the cluster
set -euo pipefail
cd "$(dirname "$0")"
CALICO_VERSION=${CALICO_VERSION:-v3.29.1}

up() {
  kind create cluster --config kind-config.yaml
  kubectl apply -f "https://raw.githubusercontent.com/projectcalico/calico/${CALICO_VERSION}/manifests/calico.yaml"
  kubectl -n kube-system set env daemonset/calico-node FELIX_IGNORELOOSERPF=true   # needed on kind
  kubectl -n kube-system rollout status ds/calico-node --timeout=300s
  kubectl wait --for=condition=Ready nodes --all --timeout=300s
  kubectl apply -f app.yaml
  kubectl -n shop rollout status deploy/backend --timeout=180s
  kubectl -n shop rollout status deploy/frontend --timeout=180s
  echo "Healthy baseline: kubectl -n shop logs deploy/frontend -f"
}

reset() {
  kubectl -n shop delete networkpolicy --all --ignore-not-found
  kubectl -n kube-system patch ds calico-node --type json \
    -p '[{"op":"remove","path":"/spec/template/spec/nodeSelector/broken"}]' 2>/dev/null || true
  kubectl -n kube-system scale deploy coredns --replicas=2
  kubectl -n kube-system get cm coredns -o yaml | sed 's#forward . 192.0.2.53#forward . /etc/resolv.conf#' | kubectl apply -f -
  kubectl -n kube-system rollout restart deploy coredns
  kubectl apply -f app.yaml
  kubectl -n shop rollout restart deploy frontend
  echo "Reset done."
}

brk() {
  local n="$1"
  [[ "$n" == "random" ]] && n=$(( (RANDOM % 7) + 1 ))
  case "$n" in
    1) # upstream DNS broken: cluster names work, external names fail
       kubectl -n kube-system get cm coredns -o yaml | sed 's#forward . /etc/resolv.conf#forward . 192.0.2.53#' | kubectl apply -f -
       kubectl -n kube-system rollout restart deploy coredns ;;
    2) # no DNS at all
       kubectl -n kube-system scale deploy coredns --replicas=0 ;;
    3) # default deny without a DNS exception
       kubectl apply -f - <<'EOF'
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata: { name: default-deny, namespace: shop }
spec:
  podSelector: {}
  policyTypes: [Ingress, Egress]
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata: { name: allow-frontend-to-backend, namespace: shop }
spec:
  podSelector: { matchLabels: { app: frontend } }
  policyTypes: [Egress]
  egress:
    - to: [{ podSelector: { matchLabels: { app: backend } } }]
      ports: [{ port: 8080, protocol: TCP }]
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata: { name: backend-ingress, namespace: shop }
spec:
  podSelector: { matchLabels: { app: backend } }
  policyTypes: [Ingress]
  ingress:
    - from: [{ podSelector: { matchLabels: { app: frontend } } }]
      ports: [{ port: 8080, protocol: TCP }]
EOF
       ;;
    4) # selector typo
       kubectl -n shop patch svc backend -p '{"spec":{"selector":{"app":"backnd"}}}' ;;
    5) # wrong targetPort
       kubectl -n shop patch svc backend --type json -p '[{"op":"replace","path":"/spec/ports/0/targetPort","value":8081}]' ;;
    6) # CNI agent gone from all nodes; new pods cannot get IPs
       kubectl -n kube-system patch ds calico-node -p '{"spec":{"template":{"spec":{"nodeSelector":{"broken":"true"}}}}}'
       sleep 20
       kubectl -n shop rollout restart deploy backend ;;
    7) # policy written against the Service port instead of the pod port
       kubectl apply -f - <<'EOF'
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata: { name: backend-ingress, namespace: shop }
spec:
  podSelector: { matchLabels: { app: backend } }
  policyTypes: [Ingress]
  ingress:
    - from: [{ podSelector: { matchLabels: { app: frontend } } }]
      ports: [{ port: 80, protocol: TCP }]
EOF
       ;;
    *) echo "fault must be 1-7 or random"; exit 1 ;;
  esac
  echo "Fault injected. Ticket: 'shop frontend reports failures. Find the cause.'"
}

case "${1:-}" in
  up) up ;;
  break) brk "${2:?fault number}" ;;
  reset) reset ;;
  down) kind delete cluster --name cap4 ;;
  *) sed -n '2,7p' "$0"; exit 1 ;;
esac
