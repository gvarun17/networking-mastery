# Video Script 15 — "Kubernetes Networking, Packet by Packet"

**Length:** about 8 minutes.

| # | Time | Visual | Narration |
|---|---|---|---|
| 1 | 0:00-0:30 | `kubectl get pods -o wide` output. | "Every pod has an IP. How does a packet get from this pod to that one, on another node? Let's follow it." |
| 2 | 0:30-1:30 | Diagram: node/pod topology with veth pairs. | "Kubernetes sets three rules: unique pod IPs, no NAT between pods, nodes can reach their pods. A CNI plugin builds this with veth pairs, routes and either native routing or an overlay." |
| 3 | 1:30-2:15 | CNI comparison table. | "Cilium uses eBPF. Calico uses BGP or eBPF. On EKS, the VPC CNI gives pods real VPC IPs." |
| 4 | 2:15-3:45 | Diagram: Service DNAT sequence. iptables chain output. | "A Service is a virtual IP. kube-proxy writes NAT rules that pick a backend at random and DNAT to it. Conntrack reverses it on the way back. Cilium does the same in eBPF, with no iptables at all." |
| 5 | 3:45-4:45 | Diagram: Gateway API roles. | "Ingress is frozen. Gateway API splits ownership: the platform team owns the Gateway, app teams own their routes, with traffic splitting built in." |
| 6 | 4:45-6:00 | NetworkPolicy YAML. Hubble showing DROPPED flows. | "By default every pod can talk to every pod. Start with default deny. Then allow DNS, or nothing resolves. Then allow exactly what each tier needs." |
| 7 | 6:00-6:45 | resolv.conf with ndots:5; Hubble DNS flows counting queries. | "ndots 5 means short names try every search domain first. External names cost extra queries. Use a trailing dot or lower ndots." |
| 8 | 6:45-7:30 | Mesh diagram: sidecars with mTLS. | "A service mesh adds mTLS and L7 policy between services. Add it when you need it, not by default." |
| 9 | 7:30-8:00 | EKS mapping table. | "On EKS: size subnets for pods, use prefix delegation, Security Groups for Pods for AWS resources, and the Load Balancer Controller for NLB and ALB." |

## Diagrams to show

1. Pod network model.
2. Service DNAT sequence.
3. Gateway API roles.
