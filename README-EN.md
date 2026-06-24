# Hermes Agent Squad

[![Version](https://img.shields.io/badge/version-0.8.2-blue)](https://github.com/maohe991-max/hermes-agent-pack)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/maohe991-max/hermes-agent-pack)](https://github.com/maohe991-max/hermes-agent-pack/stargazers)
[![Sub-Agents](https://img.shields.io/badge/sub--agents-38+-orange)](skills/sub-agents)
[![npm](https://img.shields.io/npm/v/hermes-agent-pack)](https://www.npmjs.com/package/hermes-agent-pack)

Pre-built persona pack for Hermes Agent. Understands task intent, judges complexity, and loads the right sub-agent automatically.

## Installation
### One-Click Install

```bash
curl -fsSL https://raw.githubusercontent.com/maohe991-max/hermes-agent-pack/main/install.sh | bash
```

### npm Install

```bash
npx hermes-agent-pack install
```

### Manual Install
```bash
cd ~/.hermes/skills
git clone --depth 1 https://github.com/maohe991-max/hermes-agent-pack.git agent-squad
```

Then load in conversation:
```
skill_view(name='agent-squad')
```

## Usage

```
skill_view(name='agent-squad')
```

Then just describe your task — matching is automatic:

```
Review this project
→ Auto-loads "Code Reviewer"

Debug this error
→ Auto-loads "Bug Hunter"

Evaluate this API design
→ Loads "API Designer + Security Auditor"
```

### Three-Level Judgment

| Task Type | Behavior | Token Cost |
|-----------|----------|-----------|
| Simple ("how's this function") | Direct answer, no load | 0 |
| Complex ("full security audit") | Load sub-agent | ~150 |
| Multi-angle ("evaluate API design") | Load multiple agents | ~300 |

### Force Specify

Prefix your message with `(code)` — e.g. `(security-auditor)`:

```
(security-auditor) check this config
```

## Sub-Agents

38+ agents under `skills/sub-agents/`.

| Category | Agents |
|----------|--------|
| Development | Code Reviewer, Bug Hunter, Security Auditor, Architect, Docs Writer, Code Mentor, Fullstack Engineer |
| Dev Extended | Deploy Engineer, Test Engineer, Performance Optimizer, DBA, Mobile Engineer, API Designer, Refactoring Expert |
| DevOps | Operations Engineer, Container Expert, Observability Expert, CI/CD Expert, Cloud Architect, SRE Engineer |
| Security | Network Security, Compliance Auditor, Pentesting |
| Data & AI | Data Analyst, ML Engineer, RAG Engineer, Business Intelligence, Prompt Engineer |
| Management | Project Manager, Product Manager, UI/UX Reviewer, Tech Lead, Research Analyst |
| General | i18n Expert, Knowledge Manager, Interviewer, Tech Writer, Accessibility Expert |

## Contributing

Add new sub-agents by creating a `.md` file in `skills/sub-agents/`. No main file changes needed — matching is semantic.

## License

MIT
