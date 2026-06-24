# 贡献指南

感谢你愿意为 Hermes Agent Squad 贡献！

## 添加新的子代理

1. 在 `skills/sub-agents/` 下创建 `.md` 文件
2. 文件必须包含以下 frontmatter：

```markdown
---
name: your-agent-name
parent: agent-squad
---

# 你的子代理名
```

3. 可包含的内容：本质、说话风格、工作流程、红线
4. 在 `SKILL.md` 的匹配规则表加一行

## 完善现有子代理

直接修改 `skills/sub-agents/` 下对应的 `.md` 文件，补充：

- **本质** — 角色定位和经验背景
- **说话风格** — 语气、用词习惯
- **工作流程** — 接到任务后的执行步骤
- **红线** — 什么情况下停下来问用户

## 提交 PR

1. Fork 本仓库
2. 创建你的特性分支：`git checkout -b feat/my-agent`
3. 提交改动：`git commit -m "feat: add my-agent"`
4. 推送到你的仓库：`git push origin feat/my-agent`
5. 发起 Pull Request

## 规范

> **本地校验：** 在项目根目录运行 `python3 .github/scripts/validate_sub_agents.py` 检查子代理文件格式。

- 文件名使用 `kebab-case`（如 `code-review.md`）
- frontmatter 必须包含 `name` 和 `parent: agent-squad`
- 中文内容为主，英文为辅
- 每个文件尽量独立，不依赖其他文件
