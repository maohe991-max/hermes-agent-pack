# Hermes Agent Squad

<p align="center">
  <img src="https://img.shields.io/badge/version-0.2.0-blue" alt="Version" />
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License" />
  <img src="https://img.shields.io/github/stars/maohe991-max/hermes-agent-pack" alt="Stars" />
  <img src="https://img.shields.io/badge/sub--agents-35+-orange" alt="35+ Sub-Agents" />
</p>

<p align="center">
  <img src="https://api.star-history.com/svg?repos=maohe991-max/hermes-agent-pack&type=Date" width="600" alt="Star History" />
</p>

Hermes Agent 预设子代理人格包。加载后自动理解任务内容，智能判断是否需要加载专业子代理执行。

## 安装

### 一键安装

```bash
curl -fsSL https://raw.githubusercontent.com/maohe991-max/hermes-agent-pack/main/install.sh | bash
```

### 手动安装

```bash
cd ~/.hermes/skills
git clone --depth 1 https://github.com/maohe991-max/hermes-agent-pack.git agent-squad
```

## 使用

加载主控文件：

```
skill_view(name='agent-squad')
```

然后直接提需求，自动匹配：

```
你：审查一下项目代码
→ 自动匹配「代码审查官」执行

你：排查一下这个报错
→ 自动匹配「Bug 猎人」执行

你：评估这个 API 设计方案
→ 自动加载「API 设计师 + 安全审计员」综合输出
```

### 三层判断逻辑

| 任务类型 | 行为 | Token 成本 |
|---------|------|-----------|
| 简单/通用（"这个函数怎么样"） | 直接回答，不加载 | 0 |
| 复杂/专业（"做安全审计"） | 加载对应子代理执行 | ~150 |
| 多视角（"评估 API 方案"） | 加载多个子代理综合输出 | ~300 |

### 强制指定

消息前加 `(代号)` 可强制使用某个子代理：

```
(security-auditor) 检查一下这个配置
```

## 子代理列表

35 个，分布在 `skills/sub-agents/` 目录下。

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

**添加新子代理：** 在 `skills/sub-agents/` 下新建 `.md` 文件即可。主控文件自动通过语义理解匹配，无需修改。

## 许可

MIT
