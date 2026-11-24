# Lab Topologies

| Folder | Type | Used by | Nodes |
|---|---|---|---|
| [common/](common/daemons) | FRR `daemons` file shared by all FRR labs | — | — |
| [m04-ipv6/](m04-ipv6/m04-ipv6.clab.yml) | Containerlab | Module 04 | 2 FRR, 2 hosts |
| [m06-static/](m06-static/m06-static.clab.yml) | Containerlab | Module 06 | 3 FRR, 2 hosts |
| [m07-ospf-bgp/](m07-ospf-bgp/m07-ospf-bgp.clab.yml) | Containerlab | Module 07 | 4 FRR, 1 host |
| [m12-lb/](m12-lb/docker-compose.yml) | Docker Compose | Module 12 | HAProxy + 3 backends |
| [m13-faults/](m13-faults/faults.sh) | Bash + namespaces | Module 13 | 3 namespaces |
| [m16-automation/](m16-automation/m16-automation.clab.yml) | Containerlab | Module 16 | 2 SR Linux |
| [m17-evpn/](m17-evpn/m17-evpn.clab.yml) | Containerlab | Module 17 | 2 spines, 2 leaves, 2 hosts |
| [m18-observability/](m18-observability/docker-compose.yml) | Docker Compose | Module 18 | Prometheus, Grafana, exporters, goflow2 |
| [../capstones/02-bgp-multihomed-edge/](../capstones/02-bgp-multihomed-edge/capstone2.clab.yml) | Containerlab | Capstone 2 | 4 FRR, 1 host |
| [../capstones/05-automation-pipeline/](../capstones/05-automation-pipeline/capstone5.clab.yml) | Containerlab | Capstone 5 | 3 FRR |

## Common commands

```bash
sudo containerlab deploy  -t <file>.clab.yml
sudo containerlab inspect -t <file>.clab.yml
sudo containerlab graph   -t <file>.clab.yml      # topology view in a browser (served locally)
sudo containerlab destroy -t <file>.clab.yml --cleanup
docker exec -it clab-<lab>-<node> vtysh            # FRR shell
docker exec -it clab-<lab>-<node> sr_cli           # SR Linux CLI
docker exec -it clab-<lab>-<node> bash             # Linux shell
```

## Conventions

- Lab names: `m<module>-<topic>`; node names: `r1`, `spine1`, `leaf1`, `h1`.
- FRR configs are bound into `/etc/frr/frr.conf`. Edit live with `vtysh`, then `write memory` if you want to keep changes inside the container (they are lost on destroy; copy them back to the repo).
- Containerlab gives every veth link MTU 9500 by default.
- Every lab has a `Clean up` step. Run it before you start another lab to free memory.
