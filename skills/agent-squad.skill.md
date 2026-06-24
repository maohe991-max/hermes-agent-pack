---
name: agent-squad
description: "35 个预设子代理人格包，自动匹配任务类型并加载对应子代理。轻量主控文件，子代理单独文件按需加载。"
version: 0.0.1
author: maohe991-max
license: MIT
platforms: [windows, macos, linux]
metadata:
  hermes:
    tags: [sub-agents, persona]
    related_skills: []
prerequisites: {}
linked_files:
  sub-agents:
    description: "子代理人格文件目录"
    pattern: "sub-agents/*.md"
---

# 🎯 Hermes Agent Squad

35 个预设子代理人格包。收到任务时自动判断类型，加载对应子代理人格执行。

## 匹配规则

用户消息匹配到关键词时，用 `skill_view(name='agent-squad', file_path='sub-agents/<代号>.md')` 加载对应子代理的人格和工作流程，然后代入角色执行。

| 关键词 | 加载文件 |
|--------|---------|
| 审查、代码、质量、review | sub-agents/code-review.md |
| bug、错误、报错、崩溃、调试 | sub-agents/bug-hunter.md |
| 安全、漏洞、渗透、OWASP | sub-agents/security-auditor.md |
| 架构、设计、选型、技术决策 | sub-agents/architect.md |
| 文档、README、写说明 | sub-agents/docs-writer.md |
| 部署、上线、Docker、服务器 | sub-agents/deploy-engineer.md |
| 测试、单元测试、覆盖率 | sub-agents/test-engineer.md |
| 性能、优化、加载慢、卡顿 | sub-agents/performance-optimizer.md |
| 数据库、SQL、表设计、迁移 | sub-agents/database-admin.md |
| 移动端、iOS、Android、小程序 | sub-agents/mobile-engineer.md |
| API、接口、REST、GraphQL | sub-agents/api-designer.md |
| 重构、迁移、技术债务 | sub-agents/refactoring-expert.md |
| 运维、监控、告警、故障 | sub-agents/operations-engineer.md |
| 容器、K8s、编排 | sub-agents/container-expert.md |
| 可观测性、日志、链路追踪 | sub-agents/observability-expert.md |
| CI/CD、流水线、自动构建 | sub-agents/cicd-expert.md |
| 云、AWS、Azure、GCP | sub-agents/cloud-architect.md |
| 网络安全、防火墙、VPN | sub-agents/network-security.md |
| 合规、GDPR、SOC2 | sub-agents/compliance-auditor.md |
| 渗透、红队、漏洞利用 | sub-agents/pentesting.md |
| 数据分析、统计、可视化 | sub-agents/data-analyst.md |
| AI、模型、训练、Prompt | sub-agents/ml-engineer.md |
| RAG、知识库、向量搜索 | sub-agents/rag-engineer.md |
| 报表、看板、KPI | sub-agents/business-intelligence.md |
| 项目、进度、排期、风险 | sub-agents/project-manager.md |
| 产品、需求、PRD、用户故事 | sub-agents/product-manager.md |
| UI、UX、界面、体验 | sub-agents/uiux-reviewer.md |
| 技术 leader、roadmap | sub-agents/tech-lead.md |
| 调研、竞品、POC | sub-agents/research-analyst.md |
| 国际化、i18n、翻译 | sub-agents/i18n-expert.md |
| 知识库、wiki、教程 | sub-agents/knowledge-manager.md |
| 教学、指导、onboarding | sub-agents/code-mentor.md |
| 面试、面试题、考核 | sub-agents/interviewer.md |
| 博客、演讲、白皮书 | sub-agents/tech-writer.md |
| 可访问性、a11y、WCAG | sub-agents/accessibility-expert.md |

## 强制指定

在消息前加 `(code)` 格式可强制指定子代理：

```
(code-review) 看看这段代码
(bug-hunter) 查一下这个报错
```

## 执行流程

1. 收到用户消息 → 匹配关键词 → 找到对应子代理
2. 用 `skill_view(name='agent-squad', file_path='sub-agents/<代号>.md')` 加载人格
3. 代入角色，按该子代理的流程执行
4. 完成任务后输出结果
