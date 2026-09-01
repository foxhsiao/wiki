#!/usr/bin/env python3
"""lint 的反向對照：對 tools/lint.py 做突變測試。

lint 全綠只代表「lint 沒抓到東西」，不代表庫是健康的
（見 Wiki/questions/open-questions.md Q13）。這支腳本回答另一半：
**lint 到底抓不抓得到它宣稱會抓的東西。**

做法：在暫存目錄建一個乾淨的最小 fixture（基準線必須全綠），
逐一注入一種已知缺陷，斷言 lint 回報對應的標記。

用法：python3 tools/test_lint.py
"""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REAL_LINT = Path(__file__).resolve().parent / "lint.py"

PAGE = """---
title: {title}
type: {type}
aliases: []
tags: [t]
created: 2026-01-01
updated: 2026-01-01
status: active
confidence: medium
sources: [{sources}]
---

# {title}

一句話。

## 相關頁面

{links}
"""


def build(root: Path):
    """建立一個基準線全綠的最小 fixture。"""
    (root / "tools").mkdir(parents=True)
    shutil.copy(REAL_LINT, root / "tools" / "lint.py")
    (root / ".claude").mkdir()
    (root / "Raw").mkdir()
    (root / "Wiki" / "sources").mkdir(parents=True)
    (root / "Wiki" / "concepts").mkdir()
    (root / "Wiki" / "questions").mkdir()
    (root / "Wiki" / "_templates").mkdir()

    (root / "CLAUDE.md").write_text(
        "# 規則\n\n- `[T1]` 測試用規則。\n"
        "- `[T2]` 否決的提案記進 `.claude/rejected-proposals.md`。\n",
        encoding="utf-8")
    (root / ".claude" / "rules-ledger.md").write_text(
        "# 帳\n\n| 編號 | 規則 | 加入 | 防什麼 | 證據 | 觸發紀錄 |\n"
        "|---|---|---|---|---|---|\n"
        "| T1 | 測試用規則 | 建庫 | 防手滑 | 推論 | 無 |\n"
        "| T2 | 否決的提案要記帳 | 建庫 | 防重複論證 | 推論 | 無 |\n"
        "| T3 | skill 裡的規則 | 建庫 | 防搬家時掉了來由 | 推論 | 無 |\n",
        encoding="utf-8",
    )
    (root / ".claude" / "skills" / "demo").mkdir(parents=True)
    (root / ".claude" / "skills" / "demo" / "SKILL.md").write_text(
        "# demo\n\n`[T3]` skill 裡也有規則。\n", encoding="utf-8")
    (root / ".claude" / "rejected-proposals.md").write_text(
        "# 被否決的提案\n\n| 日期 | 提案 | 決定 | 為什麼 | 什麼會讓它重新成立 | 出處 |\n"
        "|---|---|---|---|---|---|\n"
        "| 2026-01-01 | 一個提案 | 不做 | 因為某個理由 | 某個條件成立時 | Q1 |\n",
        encoding="utf-8")
    (root / "Raw" / "2026-01-01--src.md").write_text("原始來源。\n", encoding="utf-8")

    others = {"alpha": ["beta", "gamma", "src", "open-questions"],
              "beta": ["alpha", "gamma", "src"],
              "gamma": ["alpha", "beta", "src"]}
    for name, outs in others.items():
        (root / "Wiki" / "concepts" / f"{name}.md").write_text(
            PAGE.format(title=name, type="concept", sources='"[[src]]"',
                        links="\n".join(f"- [[{o}]] —— 說明" for o in outs)),
            encoding="utf-8")

    src = PAGE.format(title="src", type="source", sources="",
                      links="\n".join(f"- [[{o}]] —— 說明" for o in ("alpha", "beta", "gamma")))
    src = src.replace("confidence: medium\n",
                      'confidence: medium\nsource_type: article\nauthor: a\n'
                      'published: 2026-01-01\nurl: u\nraw: "[[2026-01-01--src]]"\n'
                      "ingested: 2026-01-01\n")
    (root / "Wiki" / "sources" / "src.md").write_text(src, encoding="utf-8")

    hub = "---\ntitle: {t}\ntype: synthesis\ncreated: 2026-01-01\nupdated: 2026-01-01\n" \
          "status: active\nconfidence: high\nsources: []\n---\n\n# {t}\n\n{body}\n"
    (root / "Wiki" / "index.md").write_text(
        hub.format(t="index", body="\n".join(f"- [[{n}]] — 摘要"
                                             for n in ("src", "alpha", "beta", "gamma", "open-questions"))),
        encoding="utf-8")
    (root / "Wiki" / "log.md").write_text(hub.format(t="log", body="## [2026-01-01] lint | x"),
                                          encoding="utf-8")
    q = PAGE.format(title="open-questions", type="question", sources='"[[src]]"',
                    links="\n".join(f"- [[{o}]] —— 說明" for o in ("alpha", "beta", "src")))
    q = q.replace("一句話。", "## Q1. 一個問題？\n\n- **狀態**：open")
    (root / "Wiki" / "questions" / "open-questions.md").write_text(q, encoding="utf-8")

    n_pages, n_src, n_q = 8, 1, 1
    (root / "Wiki" / "overview.md").write_text(
        hub.format(t="overview",
                   body="總覽。見 [[open-questions]]。\n\n## 統計\n\n| 項目 | 數量 |\n|---|---|\n"
                        f"| 來源 | {n_src} |\n| Wiki 頁面 | {n_pages} |\n"),
        encoding="utf-8")
    (root / "README.md").write_text(
        f"# fixture\n\n## 目前狀態\n\n{n_src} 份來源、{n_pages} 個 wiki 頁面、{n_q} 個開放問題。\n",
        encoding="utf-8")


def run(root: Path):
    r = subprocess.run([sys.executable, str(root / "tools" / "lint.py")],
                       capture_output=True, text=True)
    return r.returncode, r.stdout


# 每個突變：(名稱, 期待的標記, 期待 exit 1?, 動作)
def m_missing_field(root):
    p = root / "Wiki" / "concepts" / "alpha.md"
    p.write_text(re.sub(r"^status: .*$", "", p.read_text(encoding="utf-8"),
                        count=1, flags=re.M), encoding="utf-8")


def m_bad_type(root):
    p = root / "Wiki" / "concepts" / "alpha.md"
    p.write_text(p.read_text(encoding="utf-8").replace("type: concept", "type: 亂寫", 1),
                 encoding="utf-8")


def m_broken_link(root):
    p = root / "Wiki" / "concepts" / "alpha.md"
    p.write_text(p.read_text(encoding="utf-8") + "\n- [[不存在的頁]] —— 說明\n", encoding="utf-8")


def m_orphan(root):
    for n in ("beta", "gamma", "src", "open-questions"):
        p = next(root.glob(f"Wiki/*/{n}.md"))
        p.write_text(p.read_text(encoding="utf-8").replace("[[alpha]]", "[[beta]]"),
                     encoding="utf-8")


def m_few_links(root):
    p = root / "Wiki" / "concepts" / "alpha.md"
    t = p.read_text(encoding="utf-8")
    p.write_text(t.replace("- [[gamma]] —— 說明\n", "").replace("- [[src]] —— 說明\n", ""),
                 encoding="utf-8")


def m_unindexed(root):
    p = root / "Wiki" / "index.md"
    p.write_text(p.read_text(encoding="utf-8").replace("- [[alpha]] — 摘要\n", ""),
                 encoding="utf-8")


def m_stray_page(root):
    (root / "stray.md").write_text(
        "---\ntitle: s\ntype: concept\ncreated: 2026-01-01\nupdated: 2026-01-01\n"
        "status: active\nconfidence: low\nsources: []\n---\n\nx\n", encoding="utf-8")


def m_conflict_marker(root):
    p = root / "Wiki" / "concepts" / "alpha.md"
    p.write_text(p.read_text(encoding="utf-8") + "\n<<<<<<< HEAD\nx\n", encoding="utf-8")


def m_rule_without_ledger(root):
    p = root / "CLAUDE.md"
    p.write_text(p.read_text(encoding="utf-8") + "- `[T9]` 新規則沒補來由。\n", encoding="utf-8")


def m_rule_without_effect(root):
    (root / "CLAUDE.md").write_text(
        (root / "CLAUDE.md").read_text(encoding="utf-8") + "- `[T8]` 今天加的規則。\n",
        encoding="utf-8")
    p = root / ".claude" / "rules-ledger.md"
    p.write_text(p.read_text(encoding="utf-8") +
                 "| T8 | 今天加的 | **2026-08-30** | 防手滑 | 推論 | 無 |\n", encoding="utf-8")


def m_bad_evidence(root):
    p = root / ".claude" / "rules-ledger.md"
    p.write_text(p.read_text(encoding="utf-8").replace("| 推論 |", "| 大概吧 |", 1),
                 encoding="utf-8")


def m_high_confidence(root):
    p = root / "Wiki" / "concepts" / "alpha.md"
    p.write_text(p.read_text(encoding="utf-8").replace("confidence: medium",
                                                       "confidence: high", 1), encoding="utf-8")


def m_wrong_folder(root):
    src = root / "Wiki" / "sources" / "src.md"
    shutil.move(str(src), str(root / "Wiki" / "concepts" / "src.md"))


def m_empty_section(root):
    p = root / "Wiki" / "concepts" / "alpha.md"
    p.write_text(p.read_text(encoding="utf-8") + "\n## 空的\n\n## 也是空的\n", encoding="utf-8")


def m_raw_not_ingested(root):
    (root / "Raw" / "2026-01-02--another.md").write_text("x\n", encoding="utf-8")


def m_source_undeclared(root):
    p = root / "Wiki" / "concepts" / "beta.md"
    p.write_text(p.read_text(encoding="utf-8").replace('sources: ["[[src]]"]', "sources: []"),
                 encoding="utf-8")


def m_source_unused(root):
    p = root / "Wiki" / "concepts" / "gamma.md"
    p.write_text(p.read_text(encoding="utf-8").replace("- [[src]] —— 說明\n", ""),
                 encoding="utf-8")


def m_count_mismatch(root):
    p = root / "README.md"
    p.write_text(p.read_text(encoding="utf-8").replace("8 個 wiki 頁面", "43 個 wiki 頁面"),
                 encoding="utf-8")


def m_count_anchor_gone(root):
    p = root / "Wiki" / "overview.md"
    p.write_text(p.read_text(encoding="utf-8").replace("| Wiki 頁面 | 8 |", "頁面數：很多"),
                 encoding="utf-8")


def m_alias_in_table(root):
    p = root / "Wiki" / "concepts" / "alpha.md"
    p.write_text(p.read_text(encoding="utf-8").replace(
        "一句話。", "| 欄 | 值 |\n|---|---|\n| a | [[beta|貝他]] |"), encoding="utf-8")


def m_empty_sources(root):
    # 只留非 source 頁的出鏈，否則 sources 清空會連帶觸發 [來源一致]（problem），
    # 讓這個 warning 級的斷言收到錯誤的 exit code。
    (root / "Wiki" / "concepts" / "alpha.md").write_text(
        PAGE.format(title="alpha", type="concept", sources="",
                    links="\n".join(f"- [[{o}]] —— 說明"
                                    for o in ("beta", "gamma", "open-questions"))),
        encoding="utf-8")


def m_stale_status(root):
    p = root / "Wiki" / "concepts" / "alpha.md"
    p.write_text(p.read_text(encoding="utf-8").replace("status: active", "status: stale", 1),
                 encoding="utf-8")


def m_skill_rule_without_ledger(root):
    p = root / ".claude" / "skills" / "demo" / "SKILL.md"
    p.write_text(p.read_text(encoding="utf-8") + "`[T7]` skill 新規則沒補來由。\n",
                 encoding="utf-8")


def m_rejected_ledger_missing(root):
    (root / ".claude" / "rejected-proposals.md").unlink()


def m_rejected_row_incomplete(root):
    p = root / ".claude" / "rejected-proposals.md"
    p.write_text(p.read_text(encoding="utf-8").replace("| 某個條件成立時 |", "|  |", 1),
                 encoding="utf-8")


MUTATIONS = [
    ("frontmatter 缺欄位", "[frontmatter]", True, m_missing_field),
    ("type 值不合法", "[frontmatter]", True, m_bad_type),
    ("斷鏈", "[斷鏈]", True, m_broken_link),
    ("孤兒頁", "[孤兒]", True, m_orphan),
    ("出鏈不足 3 條", "[少連結]", False, m_few_links),
    ("index 漏登", "[未登錄]", True, m_unindexed),
    ("Wiki/ 以外的走失頁", "[走失頁]", False, m_stray_page),
    ("殘留的衝突標記", "[衝突標記]", True, m_conflict_marker),
    ("規則沒補來由", "[來由]", True, m_rule_without_ledger),
    ("新規則沒寫預期效果（W8）", "[來由]", True, m_rule_without_effect),
    ("證據等級不合法", "[來由]", True, m_bad_evidence),
    ("high 但來源不足", "[confidence]", True, m_high_confidence),
    ("type 與資料夾不符", "[分類]", True, m_wrong_folder),
    ("空區塊", "[空區塊]", False, m_empty_section),
    ("Raw 未 ingest", "[待處理]", False, m_raw_not_ingested),
    ("內文引用但 sources 沒列", "[來源一致]", True, m_source_undeclared),
    ("sources 列了但內文沒用", "[來源一致]", False, m_source_unused),
    ("README 計數與實際不符", "[計數]", True, m_count_mismatch),
    ("overview 統計表的錨點不見了", "[計數]", True, m_count_anchor_gone),
    ("表格裡的別名 wikilink", "[表格別名]", True, m_alias_in_table),
    ("sources 為空", "[來源]", False, m_empty_sources),
    ("status: stale 沒人處理", "[過期]", False, m_stale_status),
    ("SKILL.md 裡的規則沒補來由", "[來由]", True, m_skill_rule_without_ledger),
    ("否決帳不存在（W9）", "[否決帳]", True, m_rejected_ledger_missing),
    ("否決帳少了「什麼會讓它重新成立」（W9）", "[否決帳]", True, m_rejected_row_incomplete),
]


def main():
    with tempfile.TemporaryDirectory() as td:
        base = Path(td) / "base"
        build(base)
        code, out = run(base)
        if code != 0 or "問題：無" not in out:
            print("基準線 fixture 不是全綠，測試無效：\n" + out)
            return 1
        print(f"基準線：全綠 ✓\n\n逐一注入 {len(MUTATIONS)} 種缺陷：\n")

        failed = []
        for name, marker, should_fail, mutate in MUTATIONS:
            work = Path(td) / "work"
            shutil.rmtree(work, ignore_errors=True)
            shutil.copytree(base, work)
            mutate(work)
            code, out = run(work)
            caught = marker in out
            exit_ok = (code == 1) if should_fail else True
            ok = caught and exit_ok
            lvl = "問題" if should_fail else "提醒"
            print(f"  {'✓' if ok else '✗'}  {name:<24s} → 期待 {marker}（{lvl}）"
                  + ("" if ok else f"  實際 exit={code}"))
            if not ok:
                failed.append(name)

        print()
        if failed:
            print(f"有 {len(failed)} 種缺陷 lint 抓不到：{failed}")
            return 1
        print(f"全部 {len(MUTATIONS)} 種都被抓到 ✓")
        print("\n注意：這只證明 lint 抓得到它有檢查的東西。")
        print("lint 不涵蓋的部分見 .claude/skills/wiki-lint/SKILL.md 的「lint 不涵蓋什麼」。")
        return 0


if __name__ == "__main__":
    sys.exit(main())
