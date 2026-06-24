#!/bin/sh
# Hermes Agent Squad — 一键安装脚本
# 用法: curl -fsSL https://raw.githubusercontent.com/maohe991-max/hermes-agent-pack/main/install.sh | bash

set -e

HERMES_SKILLS_DIR="${HERMES_SKILLS_DIR:-$HOME/.hermes/skills}"
REPO_URL="https://github.com/maohe991-max/hermes-agent-pack.git"

echo "📦 Installing Hermes Agent Squad..."

if [ ! -d "$HERMES_SKILLS_DIR" ]; then
  echo "📁 Creating skills directory: $HERMES_SKILLS_DIR"
  mkdir -p "$HERMES_SKILLS_DIR"
fi

cd "$HERMES_SKILLS_DIR"

if [ -d "agent-squad" ]; then
  echo "🔄 Updating existing installation..."
  cd agent-squad
  git pull
else
  echo "⬇️  Cloning from $REPO_URL"
  git clone --depth 1 "$REPO_URL" agent-squad
fi

echo ""
echo "✅ 安装完成！在对话中加载："
echo "   skill_view(name='agent-squad')"
echo ""
echo "📖 使用说明: https://github.com/maohe991-max/hermes-agent-pack"
