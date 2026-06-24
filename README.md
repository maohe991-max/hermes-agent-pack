# Hermes Agent Squad

<p align="center">
  <img src="https://img.shields.io/badge/version-0.0.1-blue" alt="Version" />
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License" />
  <img src="https://img.shields.io/github/stars/maohe991-max/hermes-agent-pack" alt="Stars" />
  <img src="https://img.shields.io/badge/sub--agents-35+-orange" alt="35+ Sub-Agents" />
</p>

Hermes Agent 预设子代理人格包。加载后自动根据任务类型匹配对应人格执行。

## 安装

### 一键安装（推荐）

```bash
curl -fsSL https://raw.githubusercontent.com/maohe991-max/hermes-agent-pack/main/install.sh | bash
```

### 手动安装

```bash
cd ~/.hermes/skills
git clone --depth 1 https://github.com/maohe991-max/hermes-agent-pack.git agent-squad
```

## 使用

```bash
# 加载主控文件（~300 tokens）
skill_view(name='agent-squad')

# 直接发任务，自动匹配子代理
```

```
你：审查一下项目代码
→ 自动匹配并加载「代码审查官」人格执行

你：这个 bug 查一下
→ 自动匹配并加载「Bug 猎人」人格执行
```

## 子代理列表

子代理定义在 `skills/sub-agents/` 目录下，每个文件对应一个子代理。当前共 **35 个**：

| 方向 | 子代理 |
|------|--------|
| 🔧 开发 | 代码审查官、Bug 猎人、安全审计员、架构师、文档工匠、代码导师 |
| 🚀 开发扩展 | 部署工程师、测试工程师、性能优化师、数据库管理员、移动端工程师、API 设计师、重构专家 |
| ⚙️ DevOps | 运维工程师、容器化专家、可观测性专家、CI/CD 专家、云架构师 |
| 🔐 安全 | 网络安全、合规审计、渗透测试 |
| 📊 数据 & AI | 数据分析师、AI/ML 工程师、RAG 工程师、商业智能 |
| 📋 管理 | 项目经理、产品经理、UI/UX 审阅、技术 Leader、调研研究员 |
| 🌐 通用 | 国际化专家、知识管理、面试官、技术写手、可访问性专家 |

## 维护

**添加新子代理：** 在 `skills/sub-agents/` 下新建 `.md` 文件，然后在主 `SKILL.md` 的匹配规则表加一行即可。

## 许可

MIT
