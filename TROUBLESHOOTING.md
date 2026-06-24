# 故障排查 / Troubleshooting

## 技能加载后不生效 / Skill loaded but not working

- **确认路径**：技能文件应在 `~/.hermes/skills/agent-squad/SKILL.md`
  **Verify path**: The skill file should be at `~/.hermes/skills/agent-squad/SKILL.md`
- **重新加载**：在对话中执行 `skill_view(name='agent-squad')` 重新加载技能
  **Reload**: Run `skill_view(name='agent-squad')` in conversation to reload the skill
- **检查版本**：打开 `SKILL.md` 确认 `version` 字段存在且格式正确
  **Check version**: Open `SKILL.md` and verify the `version` field exists and is correctly formatted

## 子代理不匹配 / Sub-agent not matching

- **确保子代理文件存在**：确认子代理 `.md` 文件位于 `skills/sub-agents/` 目录下
  **Ensure sub-agent files exist**: Verify the sub-agent `.md` files are under `skills/sub-agents/`
- **尝试强制指定**：在消息前加子代理标签，例如 `(code-review)`：
  **Try force-specify**: Prefix your message with a sub-agent tag, e.g. `(code-review)`:
  ```
  (code-review) Review this pull request
  ```
- **检查文件名规范**：子代理文件名应使用英文小写 + 连字符，如 `code-review.md`
  **Check naming convention**: Sub-agent filenames should use lowercase + hyphens, e.g. `code-review.md`

## 手递手不触发 / Handoff not working

- **确保任务涉及多个领域**：手递手需要任务跨多个领域才能触发（如 API 设计 + 安全审计）
  **Ensure task spans multiple domains**: Handoff requires a task that spans multiple domains (e.g. API design + security audit)
- **或强制指定多个子代理**：
  **Or force-specify multiple sub-agents**:
  ```
  (api-designer,security-auditor) Evaluate this API design
  ```
- **检查 handoff 配置**：确保 `SKILL.md` 中 `handoff` 相关配置已启用
  **Check handoff config**: Ensure handoff-related settings in `SKILL.md` are enabled

## Git 克隆失败 / Git clone failed

- **检查网络连接**：确认可以访问 `github.com`
  **Check network**: Verify you can reach `github.com`
- **使用代理**：如需要，配置 Git 代理：
  **Use proxy**: If needed, configure Git proxy:
  ```bash
  git config --global http.proxy http://proxy:port
  ```
- **尝试浅克隆**：已使用 `--depth 1` 减少下载量，如仍然失败请检查磁盘空间
  **Try shallow clone**: `--depth 1` is already used to reduce download size; if still failing, check disk space

## 安装脚本运行失败 / Install script failed

- **检查 curl 是否可用**：Windows 用户可用 `curl.exe` 替代 `curl`
  **Check curl availability**: Windows users can use `curl.exe` instead of `curl`
- **手动安装**：按照 README 中的手动安装步骤操作
  **Manual install**: Follow the manual install steps in README

---

**仍有问题？** 请提交 Issue：https://github.com/maohe991-max/hermes-agent-pack/issues

**Still having issues?** Please submit an Issue: https://github.com/maohe991-max/hermes-agent-pack/issues
