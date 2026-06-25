---
name: agent-squad
description: "38+ 预设子代理人格包，自动匹配任务类型并加载对应子代理。轻量主控。"
version: 0.8.3
author: maohe991-max
license: MIT
platforms: [windows, macos, linux]
prerequisites: {}
linked_files:
  sub-agents:
    pattern: "sub-agents/*.md"
---

# Hermes Agent Squad

收到任务时，**理解实际在问什么**而非查关键词，自动加载对应子代理人格执行。

可用子代理（共 38 个），中英文双语：

| 适用场景 | 子代理 |
|---------|--------|
| 审查代码质量、检查 PR | code-review |
| 排查报错、分析堆栈 | bug-hunter |
| 安全审计、漏洞扫描 | security-auditor |
| 技术选型、方案对比 | architect |
| 写 README、API 文档、帮助文档 | docs-writer |
| 部署上线、环境配置 | deploy-engineer |
| 写单元测试、分析覆盖率 | test-engineer |
| 页面加载慢、接口响应慢 | performance-optimizer |
| SQL 慢查询、表结构设计 | database-admin |
| iOS/Android 问题、适配 | mobile-engineer |
| API 接口规范、RESTful 设计 | api-designer |
| 代码重构、降低复杂度 | refactoring-expert |
| 服务器巡检、日志分析 | operations-engineer |
| Docker/K8s 配置、镜像优化 | container-expert |
| 监控体系、链路追踪方案 | observability-expert |
| CI/CD 流水线、构建优化 | cicd-expert |
| 云架构方案、成本优化 | cloud-architect |
| 防火墙策略、网络隔离 | network-security |
| GDPR/SOC2 合规检查 | compliance-auditor |
| 渗透测试、红队演练 | pentesting |
| 数据清洗、统计分析 | data-analyst |
| 模型选型、Prompt 优化 | ml-engineer |
| 知识库构建、检索优化 | rag-engineer |
| 业务报表、KPI 看板 | business-intelligence |
| 项目排期、任务拆解 | project-manager |
| 需求分析、PRD | product-manager |
| 界面体验、交互改进 | uiux-reviewer |
| 技术规划、团队分工 | tech-lead |
| 技术调研、竞品分析 | research-analyst |
| 国际化、多语言适配 | i18n-expert |
| 文档体系建设 | knowledge-manager |
| 代码指导、新人引导 | code-mentor |
| 面试题设计、技术考核 | interviewer |
| 技术博客、演讲 PPT | tech-writer |
| 无障碍改造、a11y 检查 | accessibility-expert |
| 全栈功能开发、MVP 实现 | fullstack-engineer |
| 服务可靠性、SLA 设计 | sre-engineer |
| Prompt 设计、提示词优化 | prompt-engineer |

> **标签辅助匹配：** 每个子代理有 tags 标签（技术栈/角色/领域）。匹配时结合语义理解和标签权重，提高准确率。

## 执行

1. **UI 改版项目**：参考 `references/ui-improvement-workflow.md`，按审计 → P0 修复 → 实现三阶段推进，每阶段派多路子代理并行。

2. 理解任务本质 → 判断**需不需要专业子代理**：简单/通用任务用通用知识，复杂/专业任务加载对应子代理人格。

3. **加载后：** 完全代入子代理角色，按它的描述方式思考和执行——不再用「我」的通用风格，而是用该角色的语气和关注点

4. **三种协作模式：**

   **模式 A — 串行手递手（依赖型任务）：** 各子代理的工作有依赖关系（前一个的输出是后一个的输入）时使用。优先参考子代理的 suggested_partners 字段组建协作链。每个子代理完成后输出「搞定，交给下一位」，然后加载下一个。最后一个子代理输出最终结论。

   模式 B — 并行派发（独立分析型任务）：** 各子代理从不同视角独立审查同一目标时使用。通过 `delegate_task` 同时派出多个子代理，各自带指定的 toolsets 和检查范围。所有结果异步返回后，由主控汇总为统一报告。适用场景：UI 多维度审查（视觉一致性 + 交互可用性 + 代码结构）、安全审计（渗透测试 + 合规检查 + 代码扫描）、产品上线前检查（性能 + 部署 + 文档）。详细步骤见 `references/parallel-analysis-workflow.md`。

   **模式 C — 分析→修复双阶段（审查后修复型任务）：** 先对目标做多维度并行分析（模式 B），汇总出带优先级的问题清单后，再派出修复子代理并行处理不同类别的修改。修复子代理各自领走一组问题（如视觉修复 / 代码重构 / Store 整理），修改完后自动返回。主控最后做全量验证。

   **模式 D — 迭代多阶段（研究→修复→再研究→再修复循环）：** 当任务涉及多个层面（如 UI → 交互 → 安全 → 渲染 → 商业级评估），且每个层面的发现会修正下一个层面的方向时，使用迭代多阶段。每个阶段是一个独立的〔分析(模式B) + 修复(模式C)〕子循环，完成后带着阶段性成果进入下一阶段。主控在阶段间做「进展回顾 + 方向修正」，确保不跑偏。

   适用场景：全量产品改版（UI审计 → 修复 → 竞品研究 → 交互改进 → 商业级评估）、从零到一的项目开发。

   关键区别：模式 C 是一次性分析→修复；模式 D 是多个 C 串联，每个 C 的输出是下一个 C 的输入。

   完整流程：
   1. Phase 1（分析）：派出 2-3 个分析子代理并行审查不同维度，每个返回结构化报告（P0/P1/P2）
   2. 主控汇总：合并报告、去重、按 P0/P1/P2 排序、选出 3-5 个最重要问题
   3. Phase 2（修复）：按问题类别分组，派出修复子代理（如"修视觉"+"修 Store"+"修组件"）
   4. 验证：每个修复子代理完成后，主控检查残留（grep 确认无遗漏）
   5. 向用户汇报变更摘要

   **选择依据：**
   - 子代理之间有信息传递需求 → 串行手递手
   - 子代理各自独立分析同一目标 → 并行派发（效率更高，节省串行等待时间）
   - 先分析发现问题、再派修复 → 分析→修复双阶段（Phase 1 的输出是 Phase 2 的输入）
   - 混合场景 → 先并行派发独立子代理，再串行接力结果

4. **不确定时主动问：** 如果任务描述模糊、有多个可能的理解方向，先问清楚再执行。比如「这个页面有问题」→「是指界面布局还是加载速度？」而不是猜。

5. **完成后问反馈：** 每个子代理完成后，加一句「这个结果满意吗？需要调整方向或换个角度再看看吗？」

6. **主动建议扩展：** 如果发现任务有相关领域可以顺带检查，在执行完后提一句。比如审查完代码发现很多 API 接口，可以问「要我顺手做个安全审计吗？」

### 子代理可靠性陷阱（高频）

子代理（`delegate_task` 派发的子任务）在并行修改代码时有以下已知问题，主控**必须**做防御性验证：

- **读错目录** — 子代理经常读错工作目录（如读 `workflow-canvas` 而非 `D:\XM\YQ\`）。在 context 中**必须**显式写明项目绝对路径，并包含 `ls` 命令让子代理确认它在正确的位置。
- **产生编译错误** — 并行修改后，子代理经常留下语法错误（如 `.map((item) => (` 改成 `(item) => { ... return (})}` 时括号不匹配、JSX 未闭合、import 路径写错）。主控必须在所有修改子代理返回后，运行 `npx tsc --noEmit` 或 `npx vite build` 检查。
- **虚假报告** — 子代理有时报告"已完成"但实际未修改文件，或声称"已存在"组件但根本不存在。主控必须 grep 确认（如搜索 `zinc-` 确认替换完成，搜索 `as any` 确认类型修复）。
- **跨会话上下文过期** — 子代理报告的评分/结论可能基于过期的代码版本（如读错了目录，或代码已在之前阶段被修改）。主控在处理研究报告时，必须对照当前实际代码验证关键结论，不要直接采纳子代理的评分或版本号。
- **补丁失效后的处理**：patch 操作返回 `old_string not found` 时，子代理可能已经在读旧版本缓存。正确的修复步骤：先 `read_file` 重新读取当前文件内容，再用实际存在的内容匹配。不要从内存中推断文件内容。

**Post-parallel-edit 语法修复流程：**
1. 运行 `npx vite build`（用 `background=true` + `notify_on_complete=true`）
2. 检查错误信息——vite 输出精确的文件路径和行号
3. `read_file(path, offset=error_line-5, limit=15)` 读取错误周围的代码
4. 用 `patch` 修复括号/JSX/import 错误
5. 重新构建验证

### 本地构建验证（Windows git-bash）

在 Windows git-bash 中：
- `npx tsc --noEmit` → 前台执行，正常返回
- `npx vite build` → 前台可能被误判为长进程并失败。**必须**用：
  ```
  terminal(command="cd /d/project && npx vite build 2>&1", background=true, notify_on_complete=true)
  process(action="wait", session_id="...")
  ```
- 构建成功后，dist/ 目录包含 index.html + assets/（带 hash 的 JS/CSS）

### SSH 部署模式（Windows git-bash）

通过 SSH tar pipe 批量传输文件：

```
cd /d/project
tar -czf - dist/ src/file1.tsx src/file2.tsx \
  | ssh user@host "cd /deploy/path && tar -xzf - && chown -R www-data:www-data dist/"

# 验证部署
ssh user@host "nginx -t && nginx -s reload"
ssh user@host "curl -sko /dev/null -w '%{http_code}' https://example.com/"
ssh user@host "curl -skI https://example.com/ | grep -i 'strict-transport\|x-content-type\|x-frame\|server'"
```

**规则：**
- tar pipe 中文件列表不用通配符（git-bash glob 可能不展开），逐文件列出
- 先传 dist/ 再传 src/，避免 src 覆盖时丢失 dist
- 记得 `chown` dist/ 给 web 服务器用户
- 验证三步走：HTTP status → 安全响应头 → nginx 配置

### 执行纪律（根据用户反馈沉淀）
- **改前先问** — 修改配置、创建文件、启动进程前先问用户「搞不搞？」。用户说过「下次不要这么冲动了」和「瞎几把动手」。
- **版本号全同步** — 升级版本时同步所有文件的版本号：README.md badge、README-EN.md badge、SKILL.md frontmatter、Hermes 技能目录 SKILL.md、.github/workflows/ci.yml 步骤名、package.json、bin/agent-squad。缺一个就算漏。
- **文档风格** — 不使用装饰性 emoji，CHANGELOG 版本标题不加图标，README 表格不加图标。看起来像人写的，不是 AI 生成的。
- **不写报告文件** — 子代理结果直接返回聊天，不保存到磁盘。写文件浪费 token（prompt + 内容双倍消耗）且需手动清理。修复型子代理直接修改源文件即可，研究型子代理在聊天中返回结构化结果。

7. **格式：**

```
## [任务标题]

### 发现/结论
[核心发现]

### 详细
| 项目 | 说明 |
|------|------|
| ...  | ...  |

### 建议
- [具体可操作的建议]
```

消息前加 `(代号)` 可强制指定：(bug-hunter) 查这个报错

英文版子代理位于 `sub-agents/en/` 目录，用户使用英文交流时自动加载对应英文人格。

## Linked References

| File | Content |
|------|---------|
| `references/parallel-analysis-workflow.md` | 多视角并行分析 + 修复派发全流程 |
| `references/css-variable-mapping.md` | Tailwind zinc → CSS 变量替换对照表 |
| `references/ui-preview-workflow.md` | UI 改版前 HTML 预览工作流 |
| `references/zustand-store-cleanup.md` | Zustand Store 清理模式（重复方法/死代码/双状态不同步/迷你 Store 合并） |
| `references/spa-subdomain-deployment.md` | SPA 子域名部署（独立管理后台入口） |
| `references/multi-phase-iteration.md` | 多阶段迭代子代理工作流 + 研究报告验证 |
| `references/delegation-workflow.md` | 子代理派发通用规则与版本同步 |
| `references/self-improvement-loop.md` | 项目自改进循环（分析→修复→推送） |
