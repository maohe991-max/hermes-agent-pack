# Hermes Agent Squad

[![Version](https://img.shields.io/badge/version-0.0.1-blue)](https://github.com/maohe991-max/hermes-agent-pack)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/maohe991-max/hermes-agent-pack)](https://github.com/maohe991-max/hermes-agent-pack/stargazers)
[![Sub-Agents](https://img.shields.io/badge/sub--agents-35+-orange)](skills/sub-agents)

Pre-built persona pack for Hermes Agent. Automatically matches task type and loads the corresponding sub-agent persona.

## Installation

### One-Click Install

```bash
curl -fsSL https://raw.githubusercontent.com/maohe991-max/hermes-agent-pack/main/install.sh | bash
```

### Manual Install

```bash
cd ~/.hermes/skills
git clone --depth 1 https://github.com/maohe991-max/hermes-agent-pack.git agent-squad
```

## Usage

Load the controller (~300 tokens):

```bash
skill_view(name='agent-squad')
```

Then just tell me what you need:

```
Review this code
→ Auto-matches "Code Reviewer" persona

Debug this error
→ Auto-matches "Bug Hunter" persona
```

## Sub-Agents

| Category | Agents |
|----------|--------|
| 🔧 Development | Code Reviewer, Bug Hunter, Security Auditor, Architect, Docs Writer, Code Mentor |
| 🚀 Dev Extended | Deploy Engineer, Test Engineer, Performance Optimizer, DBA, Mobile Engineer, API Designer, Refactoring Expert |
| ⚙️ DevOps | Operations Engineer, Container Expert, Observability Expert, CI/CD Expert, Cloud Architect |
| 🔐 Security | Network Security, Compliance Auditor, Pentesting |
| 📊 Data & AI | Data Analyst, ML Engineer, RAG Engineer, Business Intelligence |
| 📋 Management | Project Manager, Product Manager, UI/UX Reviewer, Tech Lead, Research Analyst |
| 🌐 General | i18n Expert, Knowledge Manager, Interviewer, Tech Writer, Accessibility Expert |

Each sub-agent is a separate file in `skills/sub-agents/`, loaded on demand.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT
