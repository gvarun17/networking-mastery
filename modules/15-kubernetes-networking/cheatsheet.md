# Cheatsheet 15 — Kubernetes Networking

## kubectl

| Task | Command |
|---|---|
| Pod IPs and nodes | `kubectl get pods -o wide -A` |
| Services and endpoints | `kubectl get svc,endpointslices -n ns` |
| Debug pod | `kubectl run tmp --rm -it --image=nicolaka/netshoot -- bash` |
| Ephemeral debug container | `kubectl debug -it pod/web-x --image=nicolaka/netshoot --target=web` |
| DNS test | `kubectl exec client -- dig +search web` |
| NetworkPolicies | `kubectl get netpol -A`, `kubectl describe netpol x` |
| Gateway API | `kubectl get gatewayclass,gateway,httproute -A` |
| CoreDNS logs | `kubectl -n kube-system logs -l k8s-app=kube-dns` |

## Cilium

| Task | Command |
|---|---|
| Health | `cilium status` |
| Connectivity test | `cilium connectivity test` |
| Service table | `kubectl -n kube-system exec ds/cilium -- cilium-dbg service list` |
| Endpoints / identities | `cilium-dbg endpoint list`, `cilium-dbg identity list` |
| Flows | `hubble observe -n shop --verdict DROPPED` |
| DNS flows | `hubble observe --protocol dns` |

## kube-proxy (iptables mode)

```text
iptables -t nat -L KUBE-SERVICES -n | grep <clusterIP>
iptables -t nat -L KUBE-SVC-XXXX -n
ipvsadm -Ln            # IPVS mode
conntrack -L -d <clusterIP>
```

## Service types

ClusterIP · NodePort (30000-32767) · LoadBalancer · ExternalName · Headless (`clusterIP: None`)

## DNS names

| Object | Name |
|---|---|
| Service | `svc.ns.svc.cluster.local` |
| Headless pod | `pod-0.svc.ns.svc.cluster.local` |
| Pod by IP | `10-244-1-5.ns.pod.cluster.local` |
| kube-dns ClusterIP | usually `10.96.0.10` |

## NetworkPolicy rules of thumb

1. Start with default deny (ingress + egress).
2. Always allow DNS egress to kube-system/kube-dns on 53 UDP/TCP.
3. Same list item = AND; separate items = OR.
4. Policies are allow-only and additive.
5. Your CNI must enforce them.

## Ports

| Item | Port |
|---|---|
| kube-apiserver | 6443 |
| kubelet | 10250 |
| etcd | 2379-2380 |
| NodePort range | 30000-32767 |
| VXLAN (Cilium/Flannel) | UDP 8472 |
| VXLAN (IANA) | UDP 4789 |
| Geneve | UDP 6081 |
| Calico BGP | TCP 179 |
| Hubble relay | 4245 |

## EKS

VPC CNI (pod = VPC IP) · prefix delegation · custom networking (100.64/10) · Security Groups for Pods · AWS Load Balancer Controller (ALB/NLB, IP targets) · NodeLocal DNSCache.
