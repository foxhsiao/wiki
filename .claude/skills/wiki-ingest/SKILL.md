---
name: wiki-ingest
description: llm-wiki 的 ingest 流程細節——完整 frontmatter 規範、十個步驟、擴散更新的做法、index.md 與 log.md 的格式。使用者丟新來源進 Raw/ 或 Raw/inbox/、要求 ingest、或需要新建／修改 Wiki/ 頁面的 frontmatter 時載入。
---

# llm-wiki ingest 流程

根目錄 `CLAUDE.md` 是常駐規則，這份是 ingest 當下才需要的細節。兩者衝突時以 `CLAUDE.md` 為準。

## 目錄

```
Wiki/
├── index.md      # 內容目錄，依分類列出所有頁面
├── log.md        # 時序流水帳（append-only，新的加在最下面）
├── overview.md   # 全庫總覽與當前綜合論點
├── sources/ entities/ concepts/ syntheses/ questions/
└── _templates/   # 頁面模板（不列入 index，lint 略過）
```

## Frontmatter 規範

每一頁都必須有，欄位順序固定（`[N4]`）。共用欄位：

```yaml
---
title: 頁面中文標題
type: source | entity | concept | synthesis | question
aliases: [同義詞, 英文原名]
tags: [主題標籤]
created: 2026-08-01
updated: 2026-08-01
status: seed | active | stale
confidence: high | medium | low
sources: ["[[as-we-may-think]]"]
---
```

- `status`：`seed` = 只有骨架待補；`active` = 內容完整；`stale` = 已知有更新的來源尚未整併。
- `confidence`：這頁的主張有多穩。單一來源支撐 → `medium` 以下；多來源交叉驗證 → `high`。
  單一來源仍要 `high` 的，必須在 `confidence` 下一行加 `confidence_note:` 說明理由
  （典型的合格理由：供應商描述自家產品的定義性事實）。`tools/lint.py` 會擋，見 `CLAUDE.md` `[N6]`。
- `sources`：除了 `type: source` 的頁面外，每頁都必須列出支撐它的來源頁。
- `[I1]` `updated` 每次改動都要更新。需要今天的日期時用 bash `date`，不要憑印象寫。

`[I2]` `type: source` 的頁面另加：

```yaml
source_type: article | paper | book | podcast | video | report | note | dataset
author: 作者
published: 1945-07-01     # 未知寫 unknown
url: https://...
raw: "[[2026-08-01--as-we-may-think]]"   # 指向 Raw/ 的原檔
ingested: 2026-08-01
```

## 十個步驟

`[I3]` 順序固定，不要跳步。

1. 讀 `Raw/inbox/` 或使用者指定的檔案。**先完整讀完再動筆。**
   `[I4]` 含圖的 markdown 先讀文字，再單獨檢視 `Raw/assets/` 內被引用的圖。
2. 口頭回報 3–5 個關鍵重點，**等使用者確認方向或加註強調點**。
3. 把檔案移到 `Raw/`，重新命名為 `YYYY-MM-DD--slug.ext`（日期是取得日）。只改檔名，不動內容。
4. 在 `Wiki/sources/` 建立摘要頁（用 `_templates/source.md`）。
5. **擴散更新** `[I5]`：找出這份來源牽動的所有既有頁面並更新。一份來源通常會動到 5–15 頁。
   - 新事實 → 補進對應的 entity / concept 頁。
   - 與既有主張**衝突** → 不要偷偷覆蓋。在該頁的「## 爭議與矛盾」區塊並列兩種說法、
     各自標來源與日期，並降低 `confidence`。
   - 出現值得追的新實體或概念 → 開 `status: seed` 骨架頁。
6. 更新 `Wiki/overview.md` 的綜合論點（若有實質變動）。
7. 更新 `Wiki/index.md`（新增條目、修改一行摘要、更新各分類的數量）。
8. 追加 `Wiki/log.md` 一筆。
9. 跑 `python3 tools/lint.py`，修掉它報的問題。
10. 回報：新增哪些頁、更新哪些頁、發現哪些矛盾、產生哪些新問題。

## index.md 的一行格式

`[I6]` 內容導向的目錄，依分類分節，每頁一行。摘要要寫得夠有辨識度，因為它是查詢時的第一入口：

```markdown
- [[as-we-may-think]] — Bush 1945 年提出 Memex 的原始論文 · 3 個引用頁
```

## log.md 的一筆格式

`[I7]` append-only，新的加在最下面。格式固定，方便 grep：

```markdown
## [2026-08-01] ingest | As We May Think
- 新增：[[as-we-may-think]]、[[memex]]、[[vannevar-bush]]
- 更新：[[overview]]（加入「維護成本」這條軸線）
- 矛盾：無
- 新問題：[[open-questions]] #3
```

動作只有 `ingest` / `query` / `lint` / `publish` 四種。

`[I8]` **注意**：log 裡提到不存在的頁面時不要寫成 `[[...]]`，會被 lint 判成斷鏈。用反引號或純文字。
