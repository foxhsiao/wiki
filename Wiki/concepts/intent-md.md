---
title: intent.md
type: concept
aliases: [intent, proto-spec, 意圖檔]
tags: [ai, 軟體工程, 流程]
created: 2026-08-29
updated: 2026-08-29
status: active
confidence: medium
sources: ["[[the-ai-native-sdlc-playbook]]"]
---

# intent.md

> 用**提案者自己的話**寫下的 proto-spec，版控、人可讀、下一階段可直接執行。
> 它是 [[artifact-chain|產物鏈]]的第一份產物，也是迴圈閉合時最後一份。

## 它是什麼

一份 markdown，內容是：想要什麼、為什麼、在什麼限制下。原文的模板欄位：

- Problem（今天做不到什麼、誰受影響）
- Proposed outcome
- Affected users and systems
- Constraints
- Open questions

寫法不要求任何正式語言。提案者對 Claude 描述問題，Claude **當分析師來問**——
範圍、使用者、限制、成功長什麼樣——問到具體為止，再照組織模板寫出來，提案者改掉誤解的地方。

## 誰寫它

**不必是工程師。** 這是這個 play 的重點。原文特別安排：
非工程師用 claude.ai 或 Cowork，透過版控系統的 connector 讓 Claude 代為 commit，
所以貢獻者不需要碰 git。技術團隊只做一次性的事——把 intent 的家立起來、決定誰能寫。

單一產品最簡單的家是 repo 裡的 `intent/` 資料夾。專用的 intent repo 只有在意圖橫跨多個
repository 時才划算。

## 三種進入路徑

| 來源 | 誰觸發 |
|---|---|
| 有人有想法 | 人，跟 Claude 腦力激盪 |
| ticket 被開 | 既有工作流 |
| 事故告警 | Stage 6 的監控 agent，無人在觸發路徑上 |

第三種是迴圈閉合的關鍵（[[autonomy-tiering]]）：控制帶被突破後，
agent 把診斷寫成 `intent.md`，用的是**跟人寫的完全一樣的格式**，
所以它從那裡開始就走跟其他工作一樣的流程與閘門。

超出單一 PR 範圍的資安掃描發現，同樣被寫成 `intent.md` 回到 Stage 1。

## 怎麼知道它有效

原文給的兩個指標值得記下來，因為它們示範了怎麼量測流程而不量測產出：

- **領先指標**：從第一次對話到 `intent.md` 被 commit 的時間，直接讀 git 歷史。
  期待從數週的需求訪談與細化週期掉到**數小時**。
- **落後指標**：存活率——產品負責人接受進入 Design 而非關掉的比例；
  以及同一個變更的第一份 `spec.md` commit 之後，`intent.md` 還被改幾次。

## 判讀

（推論）這個 play 真正拆掉的不是文件工作，是**准入門檻**。
傳統流程裡有想法的人必須先說服產品團隊有人願意幫他寫，
所以想法在被評估之前先被「有沒有人有空」過濾一次。
`intent.md` 把那道過濾器換成產品負責人對成品的接受或退回——
過濾還在，但發生在後面，而且留下紀錄。

代價原文沒談：進來的量會變大，而分流的人還是那幾個。存活率這個指標大概會掉。

## 相關頁面

- [[artifact-chain]] —— 它在鏈上的位置
- [[the-ai-native-sdlc-playbook]] —— 來源
- [[autonomy-tiering]] —— agent 自己寫 `intent.md` 的那條路徑
- [[ai-as-interrogator]] —— Claude 當分析師提問，與這個模式同構
- [[ai-native-sdlc]] —— 它所屬的流程框架
