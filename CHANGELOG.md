# Changelog

## v0.7.0

### 🏷️ 角色边界
- 24 个子代理补齐「区别于」字段，消除相似角色混淆

### 📝 文档
- 重写 basic-usage.md，6 个场景覆盖全部 7 条执行规则
- 新增规则速查表
- TROUBLESHOOTING.md 路径修正

## v0.6.2

### 🐛 修复
- README 表格补充 fullstack-engineer、sre-engineer、prompt-engineer
- 修复 27 条缺失的 suggested_partners 反向引用
- 修复 code-reviewer.md 文件名笔误
- 统一 ML Engineer、UI/UX Reviewer 标题格式
- tech-writer tags 改为 writing

## v0.6.1

### 🐛 修复
- TROUBLESHOOTING.md 文件名示例错误（code-reviewer → code-review）
- README-EN.md 强制指定示例模糊
- fullstack-engineer.md 工作流重复
- 子代理标题大小写规范

## v0.6.0

### 📚 全员深度扩展
- 剩余 28 个子代理全部扩展，加上 v0.5.0 已扩展的 10 个，38 个子代理全部完整
- 每个新增：工作流步骤（3-4 步）、输出模板（带表格）、检查清单（5-6 项）
- 单文件从 ~12 行统一扩大到 ~35-40 行

### ⚙️ 工程化
- CI 校验脚本 `validate_sub_agents.py` 本地可运行
- CONTRIBUTING.md 新增本地校验说明
- 支持 `python3 .github/scripts/validate_sub_agents.py` 一键检查

### 🧠 匹配升级

## v0.5.0

### 🧠 匹配升级
- SKILL.md 新增标签辅助匹配，结合 tags 权重提高准确率
- 手递手机制升级：优先参考 suggested_partners 组建协作链

### 📚 深度扩展
- code-review、bug-hunter、security-auditor 等 10 个常用子代理扩展
- 每个新增：工作流步骤、输出模板、检查清单
- 平均从 12 行扩展到 38 行

## v0.4.0

### ✨ 新特性
- 38 个子代理新增 tags 标签体系（分类：技术栈/角色/领域）
- 每个子代理增加 suggested_partners 伙伴引用，支持跨代理协作

### ⚙️ 工程化
- CI 校验增强：自动检查 tags、suggested_partners 字段完整性
- 伙伴引用交叉验证：确保每个引用的子代理文件存在

## v0.3.0

### ✨ 新特性
- 新增 3 个子代理：fullstack-engineer（全栈）、sre-engineer（SRE）、prompt-engineer（提示词）
- 主文件增加适用场景匹配表，更直观
- 子代理总数 35 → 38

### 🎯 优化
- 修复 4 组角色边界重叠（安全/架构/文档/管理类），每个加「区别于」说明

## v0.2.1

### ✨ 优化
- 清理过时的引用文件和脚本
- 35 个子代理补充「适用场景」
- 补全英文 README 安装说明
- 新增 TROUBLESHOOTING.md 故障排查文档

## v0.2.0

### ✨ 新特性
- 不确定时主动问：任务模糊时先确认再执行
- 完成后问反馈：每个子代理干完活问是否满意
- 主动建议扩展：发现问题可顺带检查时主动提

## v0.1.3

### 📝 文档
- 更新 README：反映三层判断逻辑、准确 token 成本
- 清理过时的 `scripts/generate-table.py`（主文件已无匹配表）
- 添加故障排查指南

## v0.1.1

### 🐛 修复
- 明确多子代理加载机制
- 统一输出模板
- 明确加载后代入角色的行为

## v0.1.0 (重大更新)

### ✨ 新特性
- 多角度协作：跨领域任务自动加载多个子代理
- 双模式执行：简单任务不加载（0 成本），复杂任务才加载

### ⚡ 性能
- 主文件精简 56%
- 子代理文件精简 55%
- 总体 token 使用减少约 55%

## v0.0.1

### ✨ 新增
- 35 个预设子代理人格包
- 轻量主控文件（~300 tokens），子代理按需加载
- 自动任务匹配规则
- 强制指定子代理语法 `(code) xxx`

### 📦 结构
- `SKILL.md` — 主控文件，仅匹配规则
- `sub-agents/` — 35 个子代理人格文件
- MIT 协议
