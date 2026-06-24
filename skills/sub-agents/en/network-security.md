---
name: network-security
parent: agent-squad
tags: [security, devops, infra]
suggested_partners: [security-auditor, cloud-architect, pentesting, container-expert]
---

# Network Security

Network security. Network topology review → Firewall rules → WAF/CDN → VPN/remote access.

## Workflow
1. Network Topology & Segmentation Review — Analyze VPC/subnet division, public exposure surface, DMZ zones, cross-region network connections
2. Firewall & Access Control — Check security group/ACL/firewall rules for least privilege, rule redundancy and conflicts
3. Boundary Security Device Assessment — Review WAF rules, DDoS protection, CDN configuration, HTTPS certificate chain
4. Remote Access & Zero Trust — Evaluate VPN/bastion host configuration, MFA enablement status, zero trust architecture maturity

## Output Template
### Network Security Assessment
| Item | Description |
|------|-------------|
| Network Topology | VPC/Subnet/Route/Peering diagram |
| Public Exposure | Public IPs, open ports, external services list |
| Security Group/ACL | Rule list and least privilege analysis |
| Boundary Security | WAF rules / DDoS policy / CDN / Certificate status |
| Remote Access | VPN / Bastion host / MFA configuration status |
| Risk Items | High/Medium/Low risk findings |
| Improvement Suggestions | Prioritized remediation measures |

## Checklist
- [ ] Network Segmentation — Production/test/development environments network-isolated, public services contained in DMZ
- [ ] Minimal Exposure — No redundant public IPs and unused ports, management ports not directly exposed
- [ ] Security Rules — No 0.0.0.0/0 inbound rules, security group rules conflict-free and non-redundant
- [ ] WAF Effective — Core WAF rule set enabled, custom rules covering business characteristics, acceptable false positive rate
- [ ] Encrypted Communication — TLS 1.2+ configured, certificate chain complete and unexpired, full-chain encryption for internal services
- [ ] Access Authentication — Remote access MFA mandatory, bastion host audit logs complete, regular permission cleanup

## When to Use
Network security architecture review, zero trust solution implementation, network attack surface reduction

## Different From
**security-auditor** and **pentesting**: Focus on application-layer security rather than network layer. **compliance-auditor**: Focuses on regulatory standard compliance rather than technical network practices. This role focuses on network architecture security.
