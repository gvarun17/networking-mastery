# Quiz 15 — Kubernetes Networking

## Questions

### Q1. Which statement is part of the Kubernetes network model?

- A) Pods share the node's IP address
- B) Only pods in the same namespace can communicate
- C) Every pod gets its own IP and can reach every other pod without NAT
- D) Pods on different nodes must use NAT to communicate

<details><summary>Answer</summary>

**Answer: C.** Unique pod IPs and flat, NAT-free pod-to-pod connectivity. Namespaces do not isolate traffic without NetworkPolicy.

</details>

### Q2. What does a CNI plugin do when a pod starts?

- A) Creates the pod's network interface, assigns an IP and programs routes
- B) Schedules the pod to a node
- C) Pulls the container image
- D) Creates the Service

<details><summary>Answer</summary>

**Answer: A.** The kubelet (through the container runtime) calls the CNI plugin to wire the pod's network namespace.

</details>

### Q3. A Service of type ClusterIP has no endpoints. What is the most common cause?

- A) The Service selector does not match the pod labels, or the pods are not Ready
- B) The Service port is above 1024
- C) The node has no public IP
- D) CoreDNS is down

<details><summary>Answer</summary>

**Answer: A.** EndpointSlices list only Ready pods that match the selector.

</details>

### Q4. In iptables mode, how does kube-proxy implement a ClusterIP?

- A) It assigns the ClusterIP to a network interface
- B) It runs a userspace proxy process per Service
- C) It writes NAT rules that DNAT the ClusterIP to a randomly chosen backend pod IP
- D) It creates a cloud load balancer

<details><summary>Answer</summary>

**Answer: C.** `KUBE-SERVICES` → `KUBE-SVC-*` → `KUBE-SEP-*` chains with random probability DNAT.

</details>

### Q5. Which Service type exposes a port in the range 30000-32767 on every node?

- A) ExternalName
- B) Headless
- C) NodePort
- D) ClusterIP

<details><summary>Answer</summary>

**Answer: C.** NodePort (and LoadBalancer, which builds on it unless the LB uses IP targets).

</details>

### Q6. A namespace has a NetworkPolicy with `podSelector: {}` and `policyTypes: [Ingress, Egress]` and no rules. What happens?

- A) Only egress is denied
- B) All ingress and egress for every pod in the namespace is denied
- C) All traffic is allowed
- D) Only DNS is allowed

<details><summary>Answer</summary>

**Answer: B.** That is a default-deny policy for both directions. You must add allow policies, including DNS egress.

</details>

### Q7. In a NetworkPolicy `from:` list, a single item contains both `namespaceSelector` and `podSelector`. How is it evaluated?

- A) It is invalid
- B) As AND: pods matching the podSelector inside namespaces matching the namespaceSelector
- C) As OR
- D) The podSelector is ignored

<details><summary>Answer</summary>

**Answer: B.** Same item = AND. Separate items = OR.

</details>

### Q8. Scenario: After applying a default-deny policy, pods can reach other pods by IP but not by Service name. What is missing?

- A) An egress allow to CoreDNS (kube-dns) on UDP/TCP 53
- B) An Ingress
- C) A LoadBalancer Service
- D) kube-proxy

<details><summary>Answer</summary>

**Answer: A.** Name resolution needs egress to the DNS pods.

</details>

### Q9. With `ndots:5`, how is the name `api.github.com` resolved?

- A) With each search domain appended first, then as an absolute name
- B) Only through /etc/hosts
- C) Directly as an absolute name first
- D) Through the node's resolver only

<details><summary>Answer</summary>

**Answer: A.** Names with fewer dots than ndots are tried with search domains first, which causes extra NXDOMAIN queries.

</details>

### Q10. Which TWO are advantages of Gateway API over Ingress? (Choose two.)

- A) Native traffic splitting and header matching without vendor annotations
- B) It works only with NodePort
- C) It requires no controller
- D) Role-oriented resources (GatewayClass, Gateway, Routes) for infra, platform and app teams
- E) It replaces NetworkPolicy

<details><summary>Answer</summary>

**Answer: A, D.** Gateway API is expressive and portable. It still needs a controller and does not replace NetworkPolicy.

</details>

### Q11. What does Cilium's kube-proxy replacement use instead of iptables rules for Services?

- A) Userspace proxies
- B) IPVS only
- C) Static routes
- D) eBPF maps and programs

<details><summary>Answer</summary>

**Answer: D.** Cilium does service lookup and load balancing in eBPF at the socket or tc layer.

</details>

### Q12. On EKS with the AWS VPC CNI, what IP does a pod get?

- A) A real VPC IP from the node's ENIs (secondary IP or prefix)
- B) An overlay IP from 10.244.0.0/16
- C) A public IP
- D) The node's IP

<details><summary>Answer</summary>

**Answer: A.** Pods are first-class VPC citizens, which is why subnet sizing matters.

</details>

### Q13. Scenario: Same-node pod traffic works, but cross-node pod traffic fails in an overlay cluster. What do you check first?

- A) That the overlay port (e.g. VXLAN UDP 8472 or 4789) is allowed between nodes and the MTU leaves room for encapsulation
- B) Ingress controller logs
- C) CoreDNS replicas
- D) The kubelet version

<details><summary>Answer</summary>

**Answer: A.** Overlay traffic is encapsulated in UDP between node IPs. Firewalls/SGs and MTU are the usual culprits.

</details>

### Q14. What does `externalTrafficPolicy: Local` do on a LoadBalancer Service?

- A) Sends traffic only to pods on the node that received it, preserving the client source IP
- B) Uses only the control-plane node
- C) Blocks external traffic
- D) Enables mTLS

<details><summary>Answer</summary>

**Answer: A.** It avoids SNAT and the extra hop; nodes without local endpoints fail health checks so the LB skips them.

</details>

### Q15. Which feature is the main reason to adopt a service mesh?

- A) Automatic mTLS and L7 traffic policy (retries, timeouts, splits) with per-service telemetry
- B) Replacing CoreDNS
- C) Assigning pod IPs
- D) Creating VPCs

<details><summary>Answer</summary>

**Answer: A.** Meshes add identity-based encryption and L7 control. CNI and DNS remain separate.

</details>
