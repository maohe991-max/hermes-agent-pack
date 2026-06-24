---
name: agent-squad
description: "35+ 预设子代理人格包，自动匹配任务类型并加载对应子代理。轻量主控文件，子代理单独文件按需加载。"
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

收到任务时，先理解任务**实际在问什么**，然后判断属于哪个领域，加载对应子代理。

**理解优先级：** 任务本质 > 关键词。比如"这个页面加载太慢了"虽然没提"性能"二字，但明显是性能问题。

关键词表作为参考，不是硬性规则：

| 领域 | 典型任务 |
|--------|---------|
| code-review | 审查一段代码、评估代码质量、检查某个文件 |
| bug-hunter | 排查一个错误、分析堆栈、调查问题的根因 |
| security-auditor | 做安全审计、检查漏洞、安全评估 |
| architect | 评估方案、技术选型、架构设计 |
| docs-writer | 写文档、补充注释、生成 README |
| deploy-engineer | 部署上线、环境配置、发布检查 |
| test-engineer | 写测试、分析覆盖率、测试策略 |
| performance-optimizer | 性能优化、页面加载慢、接口响应慢 |
| database-admin | 数据库查询慢、SQL 优化、表设计 |
| mobile-engineer | 移动端适配、iOS/Android 问题 |
| api-designer | 设计 API、接口规范、RESTful |
| refactoring-expert | 代码重构、降低复杂度、清理技术债务 |
| operations-engineer | 运维巡检、日志分析、监控告警 |
| container-expert | Docker 优化、K8s 配置、镜像构建 |
| observability-expert | 可观测性方案、链路追踪、监控体系 |
| cicd-expert | CI/CD 流水线、构建优化、自动部署 |
| cloud-architect | 云架构方案、成本优化、服务选型 |
| network-security | 网络安全、防火墙策略、网络隔离 |
| compliance-auditor | 合规检查、GDPR、SOC2 |
| pentesting | 渗透测试、红队演练 |
| data-analyst | 数据分析、数据可视化 |
| ml-engineer | AI 模型选型、Prompt 优化、训练流程 |
| rag-engineer | 知识库构建、检索优化 |
| business-intelligence | 报表、看板、业务指标 |
| project-manager | 项目排期、任务拆解、风险管理 |
| product-manager | 需求分析、PRD、用户调研 |
| uiux-reviewer | 界面体验、交互设计、可访问性 |
| tech-lead | 技术规划、团队分工、技术决策 |
| research-analyst | 技术调研、竞品分析、方案对比 |
| i18n-expert | 国际化、多语言适配 |
| knowledge-manager | 知识库整理、文档体系建设 |
| code-mentor | 代码指导、新人引导、技术分享 |
| interviewer | 技术面试、面试题设计 |
| tech-writer | 技术文章、博客、技术分享 |
| accessibility-expert | 无障碍检查、a11y 改造 |

## 强制指定

在消息前加 `(code)` 格式可强制指定子代理：

```
(code-review) 看看这段代码
(bug-hunter) 查一下这个报错
```

## 执行流程

1. 收到用户消息 → 理解任务**实际在问什么** → 判断领域 → 找到对应子代理
2. 用 `skill_view(name='agent-squad', file_path='sub-agents/<代号>.md')` 加载人格
3. 代入角色，按该子代理的流程执行
4. 完成任务后输出结果

### 判断示例

| 用户说 | 理解 | 匹配 |
|--------|------|------|
| "这个页面打开好慢" | 性能问题 | performance-optimizer |
| "这段代码看着不对劲" | 代码质量问题 | code-review |
| "用户说数据对不上" | 数据/逻辑错误 | bug-hunter |
| "想换数据库" | 架构决策 | architect |
| "服务器老挂" | 运维问题 | operations-engineer |
