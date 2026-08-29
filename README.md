# llm-wiki

由 LLM 維護的個人知識庫。你負責找來源、提問、判斷方向；LLM 負責閱讀、萃取、歸檔、交叉引用。

## 怎麼用

只有四種動作：`ingest` / `query` / `lint` / `publish`。下面的 prompt 可以直接照抄。

### 1. 加來源 — ingest

把檔案丟進 `Raw/inbox/`（用 Obsidian Web Clipper 最快），然後：

```
ingest 這份
```

Agent 會**先完整讀完，口頭回報 3–5 個關鍵重點等你確認方向，才動筆**。
這一步是刻意的：一份來源的擴散更新通常會動到 5–15 頁，方向錯了代價很高。

想指定角度，就在後面接一句：

```
ingest 這份，重點放在方法學
ingest 這份，特別注意它跟現有主張的衝突
```

預設一次只處理一份。要批次得明說：

```
這三份一起 ingest
```

### 2. 提問 — query

直接問。Agent 會先讀 `Wiki/index.md` 找候選頁，再讀內文。

```
wiki 裡對「判斷力」的說法是什麼？
```

回答**一定附 wikilink 引用**。wiki 裡沒有的會明說「wiki 內查無」；
要用模型知識或網路搜尋補洞，會**先聲明**再說。

想指定輸出形式：

```
比較 A 和 B         →  表格
X 這條線怎麼演變的   →  時間軸
做成簡報            →  Marp
畫個圖              →  matplotlib，圖存進 Raw/assets/
```

回答有價值就留下來：

```
存進 wiki
```

### 3. 健檢 — lint

```
跑一次 lint            →  只跑機械性檢查（`tools/lint.py`）
跑一次完整的 lint 健檢  →  再加六項判斷性檢查
```

六項是：矛盾、過期、孤兒、缺頁、證據薄弱、缺口。
結果會是一份清單，**逐項問你要不要修**，不會擅自大改。

### 4. 發布 — publish

```
推上去
```

走 GitHub flow：開分支 → 開 PR → 你 review → 合併。不直接 commit 到 `main`。
`Raw/` 永遠不入版控。

### 改規則

`CLAUDE.md` 每條規則有編號（`[L1]`、`[K3]`、`[W2]`…）。

```
加一條規則：ingest 完成前一定要跑 lint
這條規則為什麼存在？
[W2] 還有用嗎？
```

加規則時 agent 會要你一起講清楚**防什麼**，並記進 `.claude/rules-ledger.md`。
`tools/lint.py` 會擋掉沒有來由的規則——**來由要在寫規則的當下記，事後補不回來**。

### Agent 會拒絕的事

| 你說 | 會發生什麼 |
|---|---|
| 「幫我下載這篇存進 `Raw/`」 | 拒絕。`Raw/` 只有你能寫，agent 只讀。它會把網址給你，由你剪存 |
| 「把這個矛盾改掉」 | 不會覆寫。矛盾要並列雙方、各標來源與日期，並降低 `confidence` |
| 「這頁還沒來源，先寫上去」 | 不會。沒有來源支撐的主張不寫；純推論一定標「（推論）」 |
| 「直接推 main」 | 不會。改動一律走分支與 PR |

### 想跳過確認

ingest 預設會停下來等你確認方向。趕時間可以：

```
直接做，不用先回報重點
```

代價是你失去在擴散更新前介入的機會。第一次處理陌生領域的來源不建議這樣做。

```bash
python3 tools/lint.py          # 斷鏈 / 孤兒頁 / frontmatter 缺漏 / index 漏登 / Raw 未 ingest / 走失頁 / 規則來由缺漏
grep "^## \[" Wiki/log.md | tail -5   # 最近 5 筆動作
```

## 結構

| 路徑 | 內容 | 誰寫 |
|---|---|---|
| `Raw/` | 原始來源，不可變 | 只有你 |
| `Raw/inbox/` | 待 ingest 的新檔案 | 只有你 |
| `Raw/assets/` | 圖片附件（設為 Obsidian 附件資料夾） | Obsidian |
| `Wiki/` | LLM 生成的頁面 | 只有 LLM |
| `CLAUDE.md` | 規則書（一頁），每條規則有編號 | 兩邊共同演化 |
| `.claude/rules-ledger.md` | 每條規則的來由、證據等級、觸發紀錄 | 只有 LLM |
| `.claude/skills/` | ingest 與 lint 的流程細節，按需載入 | 只有 LLM |
| `tools/lint.py` | 健檢腳本 | — |

`Wiki/` 底下：`sources/` 來源摘要、`entities/` 人事物、`concepts/` 概念、
`syntheses/` 跨來源論點、`questions/` 開放問題、`_templates/` 模板。
`index.md` 是目錄、`log.md` 是流水帳、`overview.md` 是當前綜合判斷。

## Obsidian 建議設定

- **附件資料夾**：設定 → 檔案與連結 → 附件資料夾路徑 → `Raw/assets`
- **下載附件**：設定 → 快速鍵 → 搜尋「Download」→ 綁定「Download attachments for current file」
- **Web Clipper**：瀏覽器擴充，把網頁存成 markdown 丟進 `Raw/inbox/`
- **關係圖檢視**：看孤兒頁與樞紐頁最快的方式
- **Dataview**（選用）：可對 frontmatter 的 `type` / `status` / `confidence` 跑動態表格

## 目前狀態

7 份來源、43 個 wiki 頁面、14 個開放問題（最後更新 2026-08-29）。
主題集中在「機器能做掉實作之後，人還剩下什麼」——判斷力、脈絡工程、
agent harness、AI-native SDLC 的治理。從 `Wiki/overview.md` 進去最快。

## 版本控制

`Raw/` **不入版控**（見 `.gitignore`）。那裡放的是第三方文章的原始副本，
只留在本機；`Wiki/` 底下的摘要與交叉引用才是這個 repo 的內容。
所以 source 頁 frontmatter 的 `raw:` 欄位在 clone 之後會指向不存在的檔案，這是預期行為。
