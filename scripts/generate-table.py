#!/usr/bin/env python3
"""自动生成 sub-agents 目录下的匹配规则表，更新到 SKILL.md"""

import os, re

SKILL_FILE = "skills/agent-squad.skill.md"
SUB_AGENTS_DIR = "skills/sub-agents"

# 关键词映射
KEYWORDS = {
    "code-review": "审查、代码、质量、review",
    "bug-hunter": "bug、错误、报错、崩溃、调试",
    "security-auditor": "安全、漏洞、渗透、OWASP",
    "architect": "架构、设计、选型、技术决策",
    "docs-writer": "文档、README、写说明",
    "deploy-engineer": "部署、上线、Docker、服务器",
    "test-engineer": "测试、单元测试、覆盖率",
    "performance-optimizer": "性能、优化、加载慢、卡顿",
    "database-admin": "数据库、SQL、表设计、迁移",
    "mobile-engineer": "移动端、iOS、Android、小程序",
    "api-designer": "API、接口、REST、GraphQL",
    "refactoring-expert": "重构、迁移、技术债务",
    "operations-engineer": "运维、监控、告警、故障",
    "container-expert": "容器、K8s、编排",
    "observability-expert": "可观测性、日志、链路追踪",
    "cicd-expert": "CI/CD、流水线、自动构建",
    "cloud-architect": "云、AWS、Azure、GCP",
    "network-security": "网络安全、防火墙、VPN",
    "compliance-auditor": "合规、GDPR、SOC2",
    "pentesting": "渗透、红队、漏洞利用",
    "data-analyst": "数据分析、统计、可视化",
    "ml-engineer": "AI、模型、训练、Prompt",
    "rag-engineer": "RAG、知识库、向量搜索",
    "business-intelligence": "报表、看板、KPI",
    "project-manager": "项目、进度、排期、风险",
    "product-manager": "产品、需求、PRD、用户故事",
    "uiux-reviewer": "UI、UX、界面、体验",
    "tech-lead": "技术leader、roadmap",
    "research-analyst": "调研、竞品、POC",
    "i18n-expert": "国际化、i18n、翻译",
    "knowledge-manager": "知识库、wiki、教程",
    "code-mentor": "教学、指导、onboarding",
    "interviewer": "面试、面试题、考核",
    "tech-writer": "博客、演讲、白皮书",
    "accessibility-expert": "可访问性、a11y、WCAG",
}

def get_emoji(filename):
    emoji_map = {
        "code-review": "👨‍💻", "bug-hunter": "🐛", "security-auditor": "🛡️",
        "architect": "🏗️", "docs-writer": "📝", "deploy-engineer": "🚀",
        "test-engineer": "🧪", "performance-optimizer": "⚡",
        "database-admin": "🗄️", "mobile-engineer": "📱",
        "api-designer": "🔌", "refactoring-expert": "♻️",
        "operations-engineer": "🔧", "container-expert": "🐳",
        "observability-expert": "📡", "cicd-expert": "⚙️",
        "cloud-architect": "☁️", "network-security": "🔐",
        "compliance-auditor": "📜", "pentesting": "🕵️",
        "data-analyst": "📈", "ml-engineer": "🤖",
        "rag-engineer": "🔗", "business-intelligence": "📊",
        "project-manager": "📋", "product-manager": "📊",
        "uiux-reviewer": "🎨", "tech-lead": "🏗️",
        "research-analyst": "🔍", "i18n-expert": "🌐",
        "knowledge-manager": "📚", "code-mentor": "🧑‍🏫",
        "interviewer": "🎤", "tech-writer": "📝",
        "accessibility-expert": "📐",
    }
    name = filename.replace(".md", "")
    return emoji_map.get(name, "🔹")

def generate_table():
    files = sorted(f for f in os.listdir(SUB_AGENTS_DIR) if f.endswith(".md"))
    lines = ["| 关键词 | 加载文件 |", "|--------|---------|"]
    for f in files:
        name = f.replace(".md", "")
        keywords = KEYWORDS.get(name, name.replace("-", " "))
        lines.append(f"| {keywords} | sub-agents/{f} |")
    return "\n".join(lines) + "\n"

def update_skill_file():
    table = generate_table()
    with open(SKILL_FILE, encoding="utf-8") as f:
        content = f.read()
    start = content.index("| 关键词 | 加载文件 |")
    end = content.index("## 强制指定")
    new_content = content[:start] + table + content[end:]
    with open(SKILL_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"✅ 已更新 {SKILL_FILE} ({len([f for f in os.listdir(SUB_AGENTS_DIR) if f.endswith('.md')])} 个子代理)")

if __name__ == "__main__":
    update_skill_file()
