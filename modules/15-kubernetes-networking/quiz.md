# Quiz 15 — Kubernetes Networking

## Questions

### Q1. Which statement is part of the Kubernetes network model?

- A) Pods on different nodes must use NAT to communicate
- B) Every pod gets its own IP and can reach every other pod without NAT
- C) Pods share the node's IP address
- D) Only pods in the same namespace can communicate

<details><summary>Answer</summary>

**Answer: B.** Unique pod IPs and flat, NAT-free pod-to-pod connectivity. Namespaces do not isolate traffic without NetworkPolicy.

</details>

### Q2. What does a CNI plugin do when a pod starts?

- A) Pulls the container image
- B) Creates the pod's network interface, assigns an IP and programs routes
- C) Schedules the pod to a node
- D) Creates the Service

<details><summary>Answer</summary>

**Answer: B.** The kubelet (through the container runtime) calls the CNI plugin to wire the pod's network namespace.

</details>

### Q3. A Service of type ClusterIP has no endpoints. What is the most common cause?

- A) The Service port is above 1024
- B) The Service selector does not match the pod labels, or the pods are not Ready
- C) CoreDNS is down
- D) The node has no public IP

<details><summary>Answer</summary>

**Answer: B.** EndpointSlices list only Ready pods that match the selector.

</details>

### Q4. In iptables mode, how does kube-proxy implement a ClusterIP?

- A) It runs a userspace proxy process per Service
- B) It writes NAT rules that DNAT the ClusterIP to a randomly chosen backend pod IP
- C) It assigns the ClusterIP to a network interface
- D) It creates a cloud load balancer

<details><summary>Answer</summary>

**Answer: B.** `KUBE-SERVICES` → `KUBE-SVC-*` → `KUBE-SEP-*` chains with random probability DNAT.

</details>

### Q5. Which Service type exposes a port in the range 30000-32767 on every node?

- A) ClusterIP
- B) NodePort
- C) ExternalName
- D) Headless

<details><summary>Answer</summary>

**Answer: B.** NodePort (and LoadBalancer, which builds on it unless the LB uses IP targets).

</details>

### Q6. A namespace has a NetworkPolicy with `podSelector: {}` and `policyTypes: [Ingress, Egress]` and no rules. What happens?

- A) All traffic is allowed
- B) All ingress and egress for every pod in the namespace is denied
- C) Only DNS is allowed
- D) Only egress is denied

<details><summary>Answer</summary>

**Answer: B.** That is a default-deny policy for both directions. You must add allow policies, including DNS egress.

</details>

### Q7. In a NetworkPolicy `from:` list, a single item contains both `namespaceSelector` and `podSelector`. How is it evaluated?

- A) As OR
- B) As AND: pods matching the podSelector inside namespaces matching the namespaceSelector
- C) The podSelector is ignored
- D) It is invalid

<details><summary>Answer</summary>

**Answer: B.** Same item = AND. Separate items = OR.

</details>

### Q8. Scenario: After applying a default-deny policy, pods can reach other pods by IP but not by Service name. What is missing?

- A) A LoadBalancer Service
- B) An egress allow to CoreDNS (kube-dns) on UDP/TCP 53
- C) kube-proxy
- D) An Ingress

<details><summary>Answer</summary>

**Answer: B.** Name resolution needs egress to the DNS pods.

</details>

### Q9. With `ndots:5`, how is the name `api.github.com` resolved?

- A) Directly as an absolute name first
- B) With each search domain appended first, then as an absolute name
- C) Only through /etc/hosts
- D) Through the node's resolver only

<details><summary>Answer</summary>

**Answer: B.** Names with fewer dots than ndots are tried with search domains first, which causes extra NXDOMAIN queries.

</details>

### Q10. Which TWO are advantages of Gateway API over Ingress? (Choose two.)

- A) Role-oriented resources (GatewayClass, Gateway, Routes) for infra, platform and app teams
- B) Native traffic splitting and header matching without vendor annotations
- C) It requires no controller
- D) It works only with NodePort
- E) It replaces NetworkPolicy

<details><summary>Answer</summary>

**Answer: A, B.** Gateway API is expressive and portable. It still needs a controller and does not replace NetworkPolicy.

</details>

### Q11. What does Cilium's kube-proxy replacement use instead of iptables rules for Services?

- A) IPVS only
- B) eBPF maps and programs
- C) Userspace proxies
- D) Static routes

<details><summary>Answer</summary>

**Answer: B.** Cilium does service lookup and load balancing in eBPF at the socket or tc layer.

</details>

### Q12. On EKS with the AWS VPC CNI, what IP does a pod get?

- A) An overlay IP from 10.244.0.0/16
- B) A real VPC IP from the node's ENIs (secondary IP or prefix)
- C) The node's IP
- D) A public IP

<details><summary>Answer</summary>

**Answer: B.** Pods are first-class VPC citizens, which is why subnet sizing matters.

</details>

### Q13. Scenario: Same-node pod traffic works, but cross-node pod traffic fails in an overlay cluster. What do you check first?

- A) Ingress controller logs
- B) That the overlay port (e.g. VXLAN UDP 8472 or 4789) is allowed between nodes and the MTU leaves room for encapsulation
- C) CoreDNS replicas
- D) The kubelet version

<details><summary>Answer</summary>

**Answer: B.** Overlay traffic is encapsulated in UDP between node IPs. Firewalls/SGs and MTU are the usual culprits.

</details>

### Q14. What does `externalTrafficPolicy: Local` do on a LoadBalancer Service?

- A) Sends traffic only to pods on the node that received it, preserving the client source IP
- B) Blocks external traffic
- C) Enables mTLS
- D) Uses only the control-plane node

<details><summary>Answer</summary>

**Answer: A.** It avoids SNAT and the extra hop; nodes without local endpoints fail health checks so the LB skips them.

</details>

### Q15. Which feature is the main reason to adopt a service mesh?

- A) Assigning pod IPs
- B) Automatic mTLS and L7 traffic policy (retries, timeouts, splits) with per-service telemetry
- C) Replacing CoreDNS
- D) Creating VPCs

<details><summary>Answer</summary>

**Answer: B.** Meshes add identity-based encryption and L7 control. CNI and DNS remain separate.

</details>
