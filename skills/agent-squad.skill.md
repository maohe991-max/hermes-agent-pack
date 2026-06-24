---
name: agent-squad
description: "35+ 预设子代理人格包，自动匹配任务类型并加载对应子代理。轻量主控。"
version: 0.1.0
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

1. 理解任务本质 → 判断**需不需要专业子代理**：
   - **简单/通用**（"这个函数写得怎么样""帮我查个文档"）→ 直接用通用知识，不加载
   - **复杂/专业**（"做完整安全审计""深度性能优化"）→ `skill_view(file_path='sub-agents/<代号>.md')` 加载人格执行
   - **需要多视角**（涉及多个领域）→ 一次加载相关子代理，综合输出

**多视角判断：** 如果任务天然覆盖多个领域，加载所有相关子代理。API + 安全、部署 + 测试、重构 + 测试、架构 + 技术选型 + 代码质量。

消息前加 `(代号)` 可强制指定：(bug-hunter) 查这个报错
