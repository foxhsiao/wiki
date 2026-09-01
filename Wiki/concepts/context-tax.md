---
title: 脈絡稅
type: concept
aliases: [context tax, schema overhead, 工具 schema 開銷]
tags: [ai, agent, 成本, 脈絡]
created: 2026-09-01
updated: 2026-09-01
status: active
confidence: medium
sources: ["[[running-a-software-factory-at-uber-scale]]"]
---

# 脈絡稅

> 工具的 schema 是**預付**的：不管這次用不用得到，開場就在脈絡裡，
> 而且每一輪對話都重送一次。
> 它跟 [[context-engineering]] 談的「載入什麼知識」不同——這是**還沒開始工作就已經付掉的成本**。

## 量出來的數字

[[running-a-software-factory-at-uber-scale|Uber]] 是第一個把它量出來的：

| 情境 | schema 開銷 |
|---|---|
| 裝了 100+ 工具 | **約 50K–70K tokens**，每一輪重送 |
| 某 workspace 套件（單一 server） | 49 個工具、約 **22K tokens** |
| 某訊息軟體／某專案追蹤軟體 | 34 個／46 個工具 |

原文那句最刺的話：

> "Loading two or three vendor servers makes the agent **carry more schema overhead than the file
> being edited** before a user even enters a prompt."

## 為什麼這是結構性的，不是設定錯誤

> "Vendors design MCP servers to expose full product capabilities because they **can't anticipate
> specific customer usage**."

供應商沒有辦法知道你會用哪三個工具，所以理性的做法是把全部功能都暴露出來。
（推論）**成本落在使用方，決定權在供應商**——這是一個典型的外部性，
不會因為某一家廠商比較體貼就消失。

## 三種解法

Uber 用的三個機制，由淺到深：

1. **CLI tool resolution**——把工具改成 shell 指令，模型在需要時才執行，
   由 CLI 動態解析並呼叫。**schema 完全離開 session 脈絡**。
   1,000+ 個內部 MCP 工具全部投影成 CLI。
2. **Tool search**——讓模型搜尋工具目錄、按需載入。原文說它在工具庫變大時
   仍維持高選擇準確度，避免大型工具集造成的退化。
3. **Code-mode**——工具既然是 shell 指令，模型就能在**一個腳本裡批次多個動作**。
   收益不只來自省下資料傳輸：省掉的是 schema 初始化、多輪輪詢、以及逐步推理的重複。

   實測（5 個相同的 SQL 查詢）：**即使結果集遠低於回應大小上限也省超過 50% token**；
   批次工作因為「N 個模型回合變成一個腳本」，**省超過 90%**。
   一次 SQL 查詢原本要送出請求、輪詢狀態 2 到 5 次、再取回輸出，
   code-mode 把整個迴圈丟進子行程，只有摘要回到脈絡。

## 它和 progressive disclosure 是同一件事

[[agent-skills]] 的三層揭露解的是**知識**的預付問題：
啟動時只看到 metadata，任務匹配才載入本體。

脈絡稅是**工具**的同一個問題，而且更難處理——
skill 的 metadata 是自己寫的，可以壓到很短；
工具 schema 是供應商定義的，你只能選擇不載入它。

（推論）所以三種解法的本質都是**把「有哪些工具」從常駐脈絡改成一次查詢**。
tool search 與 progressive disclosure 是同一個模式，只是作用在不同的東西上。

## 對本庫的意義

（推論）本庫的 `Wiki/index.md` 是這個模式的手工版：先讀索引，再決定載入哪幾頁
（`[W3]`）。差別是本庫的索引是自己寫的、可以控制長度，
而工具 schema 不是——這正是脈絡稅比索引難處理的原因。

## 相關頁面

- [[running-a-software-factory-at-uber-scale]] —— 來源，唯一量出數字的
- [[context-engineering]] —— 脈絡的另外兩個維度：什麼時候載入、誰該載入
- [[agent-skills]] —— progressive disclosure 是同一個模式的知識版
- [[ai-development-economics]] —— 這筆稅落在哪一格
- [[managed-agents]] —— 受管 agent 能把這筆稅一次砍掉的原因
