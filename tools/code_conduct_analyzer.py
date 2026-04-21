# Code Conduct Analyzer

> 用途：批量扫描代码仓库，对照八荣八耻检查潜在违反行为

```python
"""
code_conduct_analyzer.py

分析代码库中的潜在"八耻"行为：
1. 猜接口 → 未引用文档的 API 调用
2. 模糊执行 → TODO/FIXME/HACK 注释
3. 重复造轮子 → 相似度高的函数
4. 跳过验证 → 缺乏测试覆盖的变更
5. 破坏架构 → 跨层依赖、循环导入
6. 盲目修改 → 大规模 diff、混变更
"""

import os
import re
import ast
from pathlib import Path
from collections import defaultdict


def scan_todo_hacks(filepath: str) -> list:
    """扫描 TODO/FIXME/HACK 注释 —— 原则 2（模糊执行）"""
    issues = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            if re.search(r'//\s*(TODO|FIXME|HACK|XXX|TEMP)', line):
                issues.append({
                    'line': i,
                    'type': '模糊执行',
                    'content': line.strip(),
                    'severity': 'warning'
                })
    return issues


def scan_ts_ignore(filepath: str) -> list:
    """扫描 as any / @ts-ignore —— 原则 1、7（瞎猜接口、假装理解）"""
    issues = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            if '@ts-ignore' in line or '@ts-expect-error' in line or 'as any' in line:
                issues.append({
                    'line': i,
                    'type': '假装理解',
                    'content': line.strip(),
                    'severity': 'error'
                })
    return issues


def scan_empty_catch(filepath: str) -> list:
    """扫描空 catch 块 —— 原则 5（跳过验证）"""
    issues = []
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    # Simple pattern: catch(e) {} or catch(err) {\n}
    pattern = r'catch\s*\([^)]*\)\s*\{\s*\}'
    for match in re.finditer(pattern, content):
        line_num = content[:match.start()].count('\n') + 1
        issues.append({
            'line': line_num,
            'type': '跳过验证',
            'content': match.group().strip(),
            'severity': 'error'
        })
    return issues


def analyze_repo(repo_path: str) -> dict:
    """分析整个代码库"""
    results = defaultdict(list)
    extensions = {'.py', '.ts', '.tsx', '.js', '.jsx', '.go', '.java'}

    for root, dirs, files in os.walk(repo_path):
        # Skip node_modules, .git, dist, build
        dirs[:] = [d for d in dirs if d not in (
            'node_modules', '.git', 'dist', 'build', '__pycache__', '.next'
        )]

        for f in files:
            ext = os.path.splitext(f)[1]
            if ext in extensions:
                filepath = os.path.join(root, f)
                results['todo_hacks'].extend(scan_todo_hacks(filepath))
                results['ts_ignore'].extend(scan_ts_ignore(filepath))
                results['empty_catch'].extend(scan_empty_catch(filepath))

    return dict(results)


def print_report(results: dict):
    """打印分析报告"""
    total = sum(len(v) for v in results.values())
    print(f"\n{'='*60}")
    print(f"  程序员八荣八耻 — 代码规范扫描报告")
    print(f"  共发现 {total} 处潜在问题")
    print(f"{'='*60}\n")

    for category, issues in results.items():
        if not issues:
            continue
        print(f"## {category}")
        for issue in issues[:20]:  # Limit output
            severity = "🔴" if issue['severity'] == 'error' else "🟡"
            print(f"  {severity} L{issue['line']}: {issue['type']}")
            print(f"     {issue['content']}")
        if len(issues) > 20:
            print(f"  ... 还有 {len(issues) - 20} 处未显示")
        print()


if __name__ == '__main__':
    import sys
    repo_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    results = analyze_repo(repo_path)
    print_report(results)
