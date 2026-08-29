# llm-wiki

由 LLM 維護的個人知識庫。你負責找來源、提問、判斷方向；LLM 負責閱讀、萃取、歸檔、交叉引用。

## 怎麼用

**加來源**：把檔案丟進 `Raw/inbox/`，然後跟 agent 說「ingest 這份」。
Agent 會讀完、跟你討論重點、寫摘要頁、更新所有相關頁面、更新 index 與 log。一次一份效果最好。

**提問**：直接問。Agent 會先讀 `Wiki/index.md` 找候選頁，再讀內文回答，並附上引用。
好的回答可以說一句「存進 wiki」，它就會變成 `Wiki/syntheses/` 底下的新頁面。

**健檢**：說「跑一次 lint」。機械性問題由 `tools/lint.py` 抓，判斷性問題（矛盾、過期、缺頁）由 agent 判讀。

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
