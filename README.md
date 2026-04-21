# 程序员八荣八耻 · Code Honor Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![AgentSkill](https://img.shields.io/badge/AgentSkill-Standard-green)](SKILL.md) [![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code) [![OpenCode](https://img.shields.io/badge/OpenCode-Skill-blue)](https://github.com/opencode-ai/opencode)

> **写好代码，从尊重开始。做有原则的技术人。**

将「程序员八荣八耻」蒸馏为 **AI Agent 可执行的编码行为准则**。

不是道德说教，是每一行代码落笔前的 **检查清单** 和 **决策过滤器**。

![程序员八荣八耻](assets/WechatIMG147083.jpg)

---

## 八荣八耻一览

| # | ❌ 耻 | ✅ 荣 |
|---|------|------|
| 1 | 瞎猜接口 | 认真查询 |
| 2 | 模糊执行 | 寻求确认 |
| 3 | 臆想业务 | 人类确认 |
| 4 | 创造接口 | 复用现有 |
| 5 | 跳过验证 | 主动测试 |
| 6 | 破坏架构 | 谨慎规范 |
| 7 | 假装理解 | 诚实无知 |
| 8 | 盲目修改 | 谨慎重构 |

---

## 安装

### Claude Code

```bash
# 项目级别安装（在 git 仓库根目录执行）
mkdir -p .claude/skills
git clone https://github.com/your-org/code-honor-skill .claude/skills/code-honor

# 全局安装（所有项目可用）
git clone https://github.com/your-org/code-honor-skill ~/.claude/skills/code-honor
```

### OpenCode

```bash
git clone https://github.com/your-org/code-honor-skill ~/.opencode/workspace/skills/code-honor
```

---

## 使用

在 Claude Code / OpenCode 中输入：

```
/code-honor
```

或直接触发——当你描述任何编码任务时，Skill 自动激活。

### 使用场景

| 场景 | 触发方式 | 效果 |
|------|---------|------|
| **日常编码** | 描述写代码需求 | AI 自动按八荣耻执行 |
| **Code Review** | 说「review 这段代码」 | 逐条对照八荣耻审查 |
| **代码扫描** | 运行分析工具 | 批量发现潜在违反行为 |
| **新人培训** | 展示八荣耻原文图 | 团队编码规范对齐 |

---

## 功能特性

### 荣耻检查协议

AI Agent 在执行任何编码操作前，自动通过 **8 道检查**：

```
[1] 接口  → 查了文档还是凭感觉？
[2] 需求  → 确认了细节还是模糊执行？
[3] 业务  → 跟产品对齐了还是脑补？
[4] 复用  → 搜了现有实现还是造轮子？
[5] 验证  → 跑了测试还是"应该没问题"？
[6] 架构  → 遵循规范还是破坏分层？
[7] 理解  → 真的懂了还是假装懂？
[8] 重构  → 理清逻辑还是盲目改？
```

**任何一道不通过，必须停下来解决。**

### 反模式拦截

本 Skill 主动拦截以下行为：

| 反模式 | 对应原则 |
|--------|---------|
| `// TODO: 应该查一下` | 原则 1 - 不查接口 |
| `should work` / `大概是这样` | 原则 2 - 模糊执行 |
| `as any` / `@ts-ignore` | 原则 1,7 - 类型压制 |
| `catch(e) {}` | 原则 5 - 跳过验证 |
| 删除失败测试 | 原则 5 - 跳过验证 |
| 大规模重构混功能修改 | 原则 8 - 盲目修改 |

### Code Review 检查清单

内置完整的 Code Review checklist，逐条对照八荣耻，任何项标记为 ❌ 必须给出具体修改建议。

### 代码扫描工具

提供 `code_conduct_analyzer.py` 工具，批量扫描代码库中的潜在违反行为：

```bash
python3 tools/code_conduct_analyzer.py ./src

# 输出示例：
# ============================================================
#   程序员八荣八耻 — 代码规范扫描报告
#   共发现 23 处潜在问题
# ============================================================
#
# ## todo_hacks
#   🟡 L42: 模糊执行
#      // TODO: should probably check the API
#
# ## ts_ignore
#   🔴 L15: 假装理解
#      const data = response as any;
```

---

## 项目结构

```
code-honor-skill/
├── SKILL.md                  # Skill 入口，含完整 Agentic Protocol
├── assets/
│   └── WechatIMG147083.jpg   # 八荣八耻原版图片
├── prompts/
│   ├── intake.md             # 激活与信息录入模板
│   └── review.md             # Code Review Prompt
└── tools/
    └── code_conduct_analyzer.py  # 批量代码扫描工具
```

---

## 蒸馏方法论

本 Skill 通过 [女娲 · Skill造人术](https://github.com/alchaincyf/nuwa-skill) 蒸馏完成，
并经 [Darwin Skill](https://github.com/alchaincyf/darwin-skill) 进化验证。

蒸馏过程将原始的八条原则提炼为：
- **4 个心智模型**：信息先核实、不确定就对齐、你不是用户、代码没有新的
- **8 条决策启发式**：每条原则对应一个可操作的判断规则
- **6 种反模式**：明确标注绝不做的事情
- **Code Review 检查清单**：可直接用于审查流程

---

## License

MIT License
