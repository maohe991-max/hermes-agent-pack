#!/usr/bin/env node

/**
 * Hermes Agent Pack — 一键安装脚本
 * 
 * 检测 Hermes 环境，复制 skills/ 目录到目标位置。
 */

const fs = require('fs');
const path = require('path');

function getTargetDir() {
  // 优先使用环境变量
  if (process.env.HERMES_SKILLS_DIR) {
    return process.env.HERMES_SKILLS_DIR;
  }

  // 默认 ~/.hermes/skills
  const home = process.env.HOME ||
    process.env.USERPROFILE ||
    (process.platform === 'win32' && process.env.HOMEDRIVE + process.env.HOMEPATH) ||
    os.homedir();
  return path.join(home, '.hermes', 'skills');
}

function main() {
  const sourceDir = path.resolve(__dirname, '..', 'skills');
  const targetDir = getTargetDir();

  console.log('=== Hermes Agent Pack Installer ===\n');

  // 检查源目录
  if (!fs.existsSync(sourceDir)) {
    console.error(`[ERROR] 未找到 skills/ 目录: ${sourceDir}`);
    console.error('[ERROR] 请确保在 hermes-agent-pack 项目根目录下运行此脚本。');
    process.exit(1);
  }

  console.log(`[INFO]  源目录: ${sourceDir}`);
  console.log(`[INFO]  目标目录: ${targetDir}`);

  // 创建目标目录（如果不存在）
  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
    console.log('[INFO]  已创建目标目录');
  }

  // 复制 skills/
  try {
    const items = fs.readdirSync(sourceDir);
    let count = 0;

    for (const item of items) {
      const srcPath = path.join(sourceDir, item);
      const dstPath = path.join(targetDir, item);

      if (fs.statSync(srcPath).isDirectory()) {
        // 递归复制目录
        fs.cpSync(srcPath, dstPath, { recursive: true });
        console.log(`  ✓ 已复制目录: ${item}`);
      } else {
        fs.copyFileSync(srcPath, dstPath);
        console.log(`  ✓ 已复制文件: ${item}`);
      }
      count++;
    }

    console.log(`\n[SUCCESS] 安装完成！已复制 ${count} 项到:`);
    console.log(`          ${targetDir}`);
    console.log('\n[INFO]   重启 Hermes Agent 后即可生效。');
  } catch (err) {
    console.error(`[ERROR] 复制过程中出错: ${err.message}`);
    process.exit(1);
  }
}

main();
