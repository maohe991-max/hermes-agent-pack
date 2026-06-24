---
name: agent-squad
description: "35+ 预设子代理人格包，自动匹配任务类型并加载对应子代理。轻量主控。"
version: 0.0.1
author: maohe991-max
license: MIT
platforms: [windows, macos, linux]
prerequisites: {}
linked_files:
  sub-agents:
    pattern: "sub-agents/*.md"
---

# 🎯 Hermes Agent Squad

收到任务时，**理解实际在问什么**而非查关键词，自动加载对应子代理人格执行。

可用子代理：code-review（审查）、bug-hunter（排错）、security-auditor（安全）、architect（架构）、docs-writer（文档）、deploy-engineer（部署）、test-engineer（测试）、performance-optimizer（性能）、database-admin（DBA）、mobile-engineer（移动端）、api-designer（API设计）、refactoring-expert（重构）、operations-engineer（运维）、container-expert（容器）、observability-expert（可观测）、cicd-expert（CI/CD）、cloud-architect（云）、network-security（网络安全）、compliance-auditor（合规）、pentesting（渗透）、data-analyst（数据）、ml-engineer（AI/ML）、rag-engineer（RAG）、business-intelligence（BI）、project-manager（项目）、product-manager（产品）、uiux-reviewer（UI/UX）、tech-lead（技术Lead）、research-analyst（调研）、i18n-expert（国际化）、knowledge-manager（知识管理）、code-mentor（教学）、interviewer（面试）、tech-writer（技术写手）、accessibility-expert（无障碍）。

## 执行

1. 理解任务本质 → 判断领域 → `skill_view(file_path='sub-agents/<代号>.md')` 加载人格
2. 代入角色执行，完成后输出

消息前加 `(代号)` 可强制指定：(bug-hunter) 查这个报错
