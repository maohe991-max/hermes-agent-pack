# Hermes Agent Pack

Hermes Agent 预设子代理人格包。加载后自动根据任务类型匹配对应人格执行。

## 子代理列表

| 角色 | 代号 | 专长 |
|------|------|------|
| 👨‍💻 代码审查官 | `code-review` | 代码质量、架构评估、最佳实践 |
| 🐛 Bug 猎人 | `bug-hunter` | 问题排查、根因分析、修复方案 |
| 🛡️ 安全审计员 | `security-auditor` | 漏洞扫描、安全审查、OWASP |
| 🏗️ 架构师 | `architect` | 技术选型、系统设计、方案评审 |
| 📝 文档工匠 | `docs-writer` | 技术文档、API 文档、README |
| 🚀 部署工程师 | `deploy-engineer` | Docker、CI/CD、环境配置 |

## 安装

将 `skills/agent-squad.skill.md` 复制到 Hermes 的 skills 目录：

```bash
# Hermes 默认技能目录
cp skills/agent-squad.skill.md ~/.hermes/skills/
```

## 使用

在对话中自动生效：

```
你：审查一下项目代码
→ 自动匹配「代码审查官」执行

你：这个 bug 查一下
→ 自动匹配「Bug 猎人」执行
```

## 贡献

欢迎 PR！想加新子代理人格，直接在 `SKILL.md` 的 `personas:` 段加一个 entry 即可。

## 许可

MIT
