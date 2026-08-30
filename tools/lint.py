#!/usr/bin/env python3
"""llm-wiki 健檢：機械性檢查。判斷性檢查（矛盾、過期、缺頁）由 LLM 依 .claude/skills/wiki-lint/SKILL.md 執行。

用法：python3 tools/lint.py [--quiet]
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "Wiki"
RAW = ROOT / "Raw"
TEMPLATES = WIKI / "_templates"
HUBS = {"index", "log", "overview"}

REQUIRED = ["title", "type", "created", "updated", "status", "confidence"]
VALID_TYPE = {"source", "entity", "concept", "synthesis", "question"}
VALID_STATUS = {"seed", "active", "stale"}
VALID_CONF = {"high", "medium", "low"}

LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)

problems, warnings = [], []


def rel(p):
    return str(p.relative_to(ROOT))


def parse_fm(text):
    m = FM_RE.match(text)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        if re.match(r"^\s", line) or ":" not in line:
            continue
        k, _, v = line.partition(":")
        fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm


pages = [p for p in WIKI.rglob("*.md") if TEMPLATES not in p.parents]
if not pages:
    print("Wiki/ 底下沒有頁面")
    sys.exit(1)

RAW_FILES = [p for p in RAW.rglob("*") if p.is_file() and not p.name.startswith(".")]
known = {p.stem for p in pages} | {p.stem for p in RAW_FILES}
inlinks = {p.stem: set() for p in pages}
outlinks = {}

for p in pages:
    text = p.read_text(encoding="utf-8")
    stem = p.stem

    fm = parse_fm(text)
    if fm is None:
        problems.append(f"[frontmatter] {rel(p)}：缺 frontmatter")
        fm = {}
    else:
        for k in REQUIRED:
            if not fm.get(k):
                problems.append(f"[frontmatter] {rel(p)}：缺欄位 {k}")
        if stem not in HUBS and fm.get("type") not in VALID_TYPE:
            problems.append(f"[frontmatter] {rel(p)}：type 值不合法 -> {fm.get('type')!r}")
        if fm.get("status") not in VALID_STATUS:
            problems.append(f"[frontmatter] {rel(p)}：status 值不合法 -> {fm.get('status')!r}")
        if fm.get("confidence") not in VALID_CONF:
            problems.append(f"[frontmatter] {rel(p)}：confidence 值不合法 -> {fm.get('confidence')!r}")
        if fm.get("type") in {"entity", "concept", "synthesis", "question"} \
                and stem not in HUBS and not fm.get("sources", "").strip("[] "):
            warnings.append(f"[來源] {rel(p)}：sources 為空，主張缺乏來源支撐")
        if fm.get("status") == "stale":
            warnings.append(f"[過期] {rel(p)}：標記為 stale，尚未整併新來源")

    body = FM_RE.sub("", text)
    targets = {t.strip() for t in LINK_RE.findall(body)}
    outlinks[stem] = targets
    for t in targets:
        if t not in known:
            problems.append(f"[斷鏈] {rel(p)} -> [[{t}]] 不存在")
        elif t in inlinks and t != stem:
            inlinks[t].add(stem)

# 孤兒：扣掉 index / log 的引用後沒有入鏈
for p in pages:
    stem = p.stem
    if stem in HUBS:
        continue
    real_in = inlinks[stem] - HUBS
    if not real_in:
        problems.append(f"[孤兒] {rel(p)}：除了 index/log 之外沒有任何頁面連進來")
    if len(outlinks[stem]) < 3:
        warnings.append(f"[少連結] {rel(p)}：只有 {len(outlinks[stem])} 條出鏈（規範至少 3 條）")

# index 漏登
index_targets = outlinks.get("index", set())
for p in pages:
    if p.stem in HUBS:
        continue
    if p.stem not in index_targets:
        problems.append(f"[未登錄] {rel(p)}：沒有出現在 Wiki/index.md")

# vault 裡的走失頁：Wiki/ 以外出現帶 frontmatter 的 wiki 頁
# （2026-08-29 加入：_to_delete/ 曾留下 7 個示範頁，圖表看得到但 lint 完全無感）
SKIP_DIRS = {".git", ".obsidian", "__pycache__", ".trash"}
wiki_stems = {p.stem for p in pages}
for stray in ROOT.rglob("*.md"):
    if WIKI in stray.parents or RAW in stray.parents:
        continue
    if any(part in SKIP_DIRS for part in stray.relative_to(ROOT).parts):
        continue
    fm = parse_fm(stray.read_text(encoding="utf-8"))
    if not fm or fm.get("type") not in VALID_TYPE:
        continue
    if stray.stem in wiki_stems:
        problems.append(
            f"[走失頁] {rel(stray)}：在 Wiki/ 之外，且與 Wiki/ 現行頁同名（{stray.stem}）"
        )
    else:
        warnings.append(f"[走失頁] {rel(stray)}：在 Wiki/ 之外的 wiki 頁，Obsidian 仍會算進 vault")

# Raw 未 ingest
ingested = set()
for p in WIKI.joinpath("sources").glob("*.md"):
    fm = parse_fm(p.read_text(encoding="utf-8")) or {}
    raw = fm.get("raw", "").strip("[]\"' ")
    if raw:
        ingested.add(raw)
for p in RAW_FILES:
    if p.stem not in ingested:
        warnings.append(f"[待處理] {rel(p)}：Raw 檔案尚未 ingest 成 sources/ 頁面")

# confidence 與來源數（N6）：high 需要兩份以上來源，否則要寫 confidence_note
# （2026-08-29 加入：規範建庫時就寫了，但沒有機制，一次健檢抓到 5 頁違規）
for p in pages:
    stem = p.stem
    if stem in HUBS:
        continue
    fm = parse_fm(p.read_text(encoding="utf-8")) or {}
    if fm.get("type") == "source" or fm.get("confidence") != "high":
        if fm.get("confidence_note") and fm.get("confidence") != "high":
            warnings.append(f"[confidence] {rel(p)}：有 confidence_note 但 confidence 不是 high")
        continue
    n_src = len(re.findall(r"\[\[", fm.get("sources", "")))
    note = fm.get("confidence_note", "").strip()
    if n_src < 2 and not note:
        problems.append(
            f"[confidence] {rel(p)}：confidence: high 但只有 {n_src} 個來源，"
            f"需要第二份來源，或加一行 confidence_note 說明理由"
        )
    elif n_src >= 2 and note:
        warnings.append(f"[confidence] {rel(p)}：已有 {n_src} 個來源，confidence_note 是多餘的")

# 殘留的合併衝突標記
# （2026-08-29 加入：PR #5 把一個 diff3 中段標記 ||||||| 帶進了 main，
#  當時的人工驗證只 grep 了 <<< === >>> 三種，漏掉第四種）
CONFLICT_RE = re.compile(r"^(<{7}|\|{7}|={7}|>{7})( |$)")
for f in ROOT.rglob("*"):
    if not f.is_file() or f.suffix not in {".md", ".py", ".json", ".yml", ".yaml"}:
        continue
    parts = f.relative_to(ROOT).parts
    if any(x in {".git", ".obsidian", "__pycache__", ".trash"} for x in parts):
        continue
    if RAW in f.parents:          # Raw/ 唯讀，不歸這裡管
        continue
    try:
        lines = f.read_text(encoding="utf-8").splitlines()
    except (UnicodeDecodeError, OSError):
        continue
    for i, line in enumerate(lines, 1):
        if CONFLICT_RE.match(line):
            problems.append(f"[衝突標記] {rel(f)}:{i}：殘留的合併衝突標記 {line[:7]!r}")
            break

# C1：type 與資料夾必須相符（2026-08-30 加入，把 C1 從建議變成閘門）
FOLDER_OF = {"source": "sources", "entity": "entities", "concept": "concepts",
             "synthesis": "syntheses", "question": "questions"}
for p in pages:
    if p.stem in HUBS:
        continue
    fm = parse_fm(p.read_text(encoding="utf-8")) or {}
    want = FOLDER_OF.get(fm.get("type"))
    if want and p.parent.name != want:
        problems.append(
            f"[分類] {rel(p)}：type 是 {fm.get('type')}，應該放在 {want}/ 而不是 {p.parent.name}/"
        )

# S5：空區塊——標題底下沒有內容，且下一個標題不是它的子標題
HEAD_RE = re.compile(r"^(#{2,6}) (.+)$", re.M)
for p in pages:
    body = FM_RE.sub("", p.read_text(encoding="utf-8"))
    heads = [(m.start(), len(m.group(1)), m.group(2)) for m in HEAD_RE.finditer(body)]
    for i, (pos, lvl, txt) in enumerate(heads):
        nxt = heads[i + 1] if i + 1 < len(heads) else None
        seg = body[pos:(nxt[0] if nxt else len(body))]
        if not HEAD_RE.sub("", seg).strip() and (nxt is None or nxt[1] <= lvl):
            warnings.append(f"[空區塊] {rel(p)}：「{txt}」底下沒有內容")

# 規則來由：CLAUDE.md 的每個編號都要在 rules-ledger 有一列，且證據等級要填
# （2026-08-29 加入：Q10 的教訓是「來由要在寫規則的當下記，事後補不回來」，
#  所以把這條紀律從自覺變成閘門）
RULES_FILE = ROOT / "CLAUDE.md"
LEDGER = ROOT / ".claude" / "rules-ledger.md"
VALID_EVIDENCE = {"有紀錄", "推論", "來由未知"}
RULE_ID_RE = re.compile(r"\[([A-Z]\d+)\]")

if RULES_FILE.exists():
    rule_ids = set(RULE_ID_RE.findall(RULES_FILE.read_text(encoding="utf-8")))
    if not LEDGER.exists():
        if rule_ids:
            problems.append(f"[來由] {rel(LEDGER)} 不存在，但 CLAUDE.md 有 {len(rule_ids)} 條編號規則")
    else:
        ledger_rows = {}
        for line in LEDGER.read_text(encoding="utf-8").splitlines():
            if not line.startswith("|"):
                continue
            cols = [c.strip().strip("*").strip() for c in line.strip().strip("|").split("|")]
            if len(cols) >= 5 and re.fullmatch(r"[A-Z]\d+", cols[0]):
                ledger_rows[cols[0]] = cols

        for rid in sorted(rule_ids - set(ledger_rows)):
            problems.append(
                f"[來由] 規則 {rid} 在 CLAUDE.md，但 {rel(LEDGER)} 沒有對應列"
            )
        for rid in sorted(set(ledger_rows) - rule_ids):
            warnings.append(
                f"[來由] {rel(LEDGER)} 有 {rid} 這一列，但 CLAUDE.md 已無此編號（規則被刪或編號改了？）"
            )
        # W8：2026-08-30 之後新增的規則，還要寫可否證的預期效果
        # （不回溯要求既有規則——來由補不回來，預期效果的基準線更補不回來）
        W8_FROM = "2026-08-30"
        for rid in sorted(rule_ids & set(ledger_rows)):
            cols = ledger_rows[rid]
            if not cols[3]:
                problems.append(f"[來由] 規則 {rid} 的「防什麼」欄是空的")
            dates = re.findall(r"\d{4}-\d{2}-\d{2}", cols[2])
            if dates and max(dates) >= W8_FROM and "預期效果" not in cols[3]:
                problems.append(
                    f"[來由] 規則 {rid} 於 {max(dates)} 加入，"
                    f"必須在「防什麼」欄寫一句「預期效果：…」（規則 W8）"
                )
            if cols[4] not in VALID_EVIDENCE:
                problems.append(
                    f"[來由] 規則 {rid} 的證據等級是 {cols[4]!r}，"
                    f"必須是 {'／'.join(sorted(VALID_EVIDENCE))} 之一"
                )

# N5：sources 與內文的雙向一致（2026-08-30 加入）
# （2026-08-30 健檢抓到 7 頁內文引用了某份來源卻沒列進 sources、4 頁列了卻從未提到。
#  這直接影響 N6——它的門檻就是數 sources 有幾份。index/log 是目錄，天生列全部，豁免。）
CATALOGS = {"index", "log"}
source_stems = {p.stem for p in pages if (parse_fm(p.read_text(encoding="utf-8")) or {}).get("type") == "source"}
for p in pages:
    stem = p.stem
    if stem in CATALOGS or stem in source_stems:
        continue
    text = p.read_text(encoding="utf-8")
    fm = parse_fm(text) or {}
    declared = set(LINK_RE.findall(fm.get("sources", "")))
    body = FM_RE.sub("", text, count=1)
    used = set(LINK_RE.findall(body)) & source_stems
    for miss in sorted(used - declared):
        problems.append(
            f"[來源一致] {rel(p)}：內文引用了 [[{miss}]] 但 frontmatter sources 沒列（規則 N5）"
        )
    for unused in sorted(declared - used):
        warnings.append(
            f"[來源一致] {rel(p)}：sources 列了 [[{unused}]] 但內文從未提到"
        )

# L5：維護型產物的計數要跟著現況（2026-08-30 加入）
# （2026-08-30 健檢時 README 停在四份來源之前的快照：7/43/14，實際是 11/56/16；
#  overview 的統計表也少算 6 頁、少算 3 條結案。這兩處都是 L5 說的維護型產物。）
n_sources = len(source_stems)
n_pages = len(pages)
n_questions = len(re.findall(r"^## Q\d", (WIKI / "questions" / "open-questions.md").read_text(encoding="utf-8"), re.M))

ov = (WIKI / "overview.md").read_text(encoding="utf-8")
for label, actual in (("來源", n_sources), ("Wiki 頁面", n_pages)):
    m = re.search(rf"^\|\s*{re.escape(label)}\s*\|\s*(\d+)", ov, re.M)
    if not m:
        problems.append(f"[計數] Wiki/overview.md 的統計表找不到「{label}」那一列，計數閘門失效")
    elif int(m.group(1)) != actual:
        problems.append(f"[計數] Wiki/overview.md 統計表：{label} 寫 {m.group(1)}，實際 {actual}")

readme = (ROOT / "README.md").read_text(encoding="utf-8")
m = re.search(r"(\d+) 份來源、(\d+) 個 wiki 頁面、(\d+) 個開放問題", readme)
if not m:
    problems.append("[計數] README.md 找不到「N 份來源、N 個 wiki 頁面、N 個開放問題」那一行，計數閘門失效")
else:
    got = tuple(int(x) for x in m.groups())
    if got != (n_sources, n_pages, n_questions):
        problems.append(
            f"[計數] README.md 目前狀態寫 {got}，實際 ({n_sources}, {n_pages}, {n_questions})"
        )

# K1：帶別名的 wikilink 不能放進表格（2026-08-30 加入）
# （規則 2026-08-29 寫進 CLAUDE.md，隔天在單一頁面違反 9 次，2026-08-30 健檢時
#  我自己又在改 overview 的當下踩了一次，另外還有兩處建庫時留下的。
#  跳脫與否都會出事：跳脫了 lint 的 LINK_RE 解不出 target，不跳脫 Obsidian 的表格會被切開。）
TABLE_ROW_RE = re.compile(r"^\|.*\|$")
ALIAS_IN_LINK_RE = re.compile(r"\[\[[^\]]*\|")
for f in sorted(ROOT.rglob("*.md")):
    if ".git" in f.parts:
        continue
    in_fence = False
    for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
        s = line.strip()
        if s.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if TABLE_ROW_RE.match(s) and ALIAS_IN_LINK_RE.search(s):
            problems.append(
                f"[表格別名] {rel(f)}:{i}：表格列裡有帶別名的 wikilink，"
                f"跳脫與否都會出事（規則 K1）"
            )

quiet = "--quiet" in sys.argv
print(f"檢查 {len(pages)} 頁 / {len(RAW_FILES)} 份原始檔\n")
if problems:
    print(f"問題 {len(problems)} 項：")
    for x in problems:
        print("  ✗ " + x)
else:
    print("問題：無 ✓")
if warnings and not quiet:
    print(f"\n提醒 {len(warnings)} 項：")
    for x in warnings:
        print("  · " + x)
print("\n機械性檢查到此為止。矛盾、過期主張、缺頁概念、證據薄弱請依 .claude/skills/wiki-lint/SKILL.md 人工判讀。")
sys.exit(1 if problems else 0)
