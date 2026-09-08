---
title: 自主性的成本
type: concept
aliases: [agent autonomy cost, 範圍擴張]
tags: [ai, agent, 工作方法]
created: 2026-08-02
updated: 2026-09-08
status: active
confidence: high
sources: ["[[prompting-claude-opus-5]]", "[[the-ai-native-sdlc-playbook]]", "[[running-a-software-factory-at-uber-scale]]", "[[harness-engineering-complete-guide]]"]
---

# 自主性的成本

> 模型變得更主動之後，失效模式從「做不到」變成「做太多」。
> 控制方式不是禁止，是**明確畫出界線**。

## 三種做太多

### 1. 過度驗證

模型不需要被叫就會自我驗證與自我修錯。
既有提示裡的「加入最終驗證步驟」「用子 agent 驗證」會與它自身行為疊加，
**只增成本不改善結果**。（[[prompt-obsolescence]]）

### 2. 範圍擴張

> "Claude Opus 5 can also expand the scope of a task, adding steps that weren't requested
> or applying its own judgment about what the task should be."

[[prompting-claude-opus-5]] 給的約束句值得整段記下來，因為它示範了怎麼**畫界線而不是禁止**：

> 交付被要求的東西，照被要求的範圍。例行判斷自己做，只有在不同解讀會導致實質不同的工作時才確認。
> 如果覺得請求有誤或有更好的做法，用一句話說出來然後照原樣繼續，
> 而不是安靜地把任務縮小、放大或改造。做完整件事，但停在明顯超出要求的動作之前。

三個機制值得注意：**例行判斷授權給模型**、**異議要說出來但不要單方面執行**、
**兩端都設限**（不准縮小也不准放大）。

### 3. 過度委派

比前代更主動生成子 agent。真正獨立的大工作上划算，
小任務上是成本與時間的**乘法**。對策是明講哪些情境值得委派，或設確定性的數量上限。

## 一般化

（推論）這三者是同一件事的三種表現：**模型的自主性上升，harness 的工作從「補能力」變成「設邊界」。**
[[harness-engineering]] 描述的 harness 元件沒變，但每個元件裡該寫什麼反過來了——
從「教它怎麼做」變成「告訴它做到哪裡為止」。

## 邊界怎麼真的被畫出來

這一頁到此為止只有原則（畫界線而不是禁止），沒有機制。
[[the-ai-native-sdlc-playbook]] 補上了機制：**邊界不是提示裡的一句話，
是版控設定裡的路由與工具清單。**

[[autonomy-tiering|自治分級]]用訊號強度決定 agent 拿得到哪些工具：
2σ 只給唯讀工具，3σ 才可行動，而且行動只能走 PR 或事先核准的 runbook。
差別在於**提示裡的邊界靠模型願意遵守，分級的邊界靠它沒有工具可用**。

同一個道理套在部署上是一句話：
「agent 可以做到 production gate 為止，過不了那道門。」

## 與判斷力那條線的關係

「對任務應該是什麼行使自己的判斷」——這是供應商用自己的話承認模型在做
[[judgment|判斷]]，而且把它列為需要被約束的行為。
這對 [[can-judgment-be-outsourced]] 是直接的新證據。

## 委派成本有了定價方案

本頁把「自主委派」列為三種做太多之一：模型自己決定要不要生成子 agent，
而每個子 agent 都要付一次完整的脈絡建置成本。

[[running-a-software-factory-at-uber-scale|Uber]] 的做法不是禁止委派，是**替委派定價**：

> "Because subagents perform well-defined tasks with specified inputs that often do not require
> frontier-level reasoning, we **default them to a weaker, more cost-effective model** while still
> allowing manual overrides. The primary model handles task decomposition and evaluation while
> subagents execute the work."

原文說這是最有效的槓桿之一，而且重要性還在上升，因為**會生成子 agent 的 session 比例持續增加**——
模型能力變強讓多 agent 編排更可行。

配套：subagent 的 prompt cache TTL 維持 5 分鐘（互動式 session 改成 1 小時），
理由是子任務短命。

（推論）這把本頁的立場往前推了一格。本頁原本說「畫界線而不是禁止」，
Uber 示範的是第三條路：**讓那個行為變便宜，而不是讓它變難**。
主模型拆解與評估、子 agent 執行——這正好也是 [[conductor-and-orchestrator|協調者]]那條分工，
只是把它變成了模型路由設定。

## 每一種做太多，對應契約缺的一欄

[[task-contract]] 給了本頁一個更精確的診斷語言。
本頁列的失效模式全部可以重述成「契約少寫了哪一欄」：

| 失效模式 | 契約缺的欄位 |
|---|---|
| 範圍擴張 | `scope`（什麼在裡面）與 `constraints`（什麼不准動） |
| 過度驗證 | `acceptance`（什麼證據算完成，也就是**什麼時候可以停**） |
| 過度委派 | `approval_required` 與工具清單沒有界定 |

> "Without a contract, the agent optimizes for **plausible activity**.
> With a contract, it can optimize for **verified completion**."

（推論）這改了本頁的因果說法。本頁原本把這些歸因於「模型自主性提高」，
像是模型的性質變化；契約的語言指出另一半：**自主性高的模型不是不受控，
是在沒有終止條件時自己補一個**。少了 `acceptance`，「做完了嗎」這個判斷
就從 harness 掉回模型身上，而模型補出來的終止條件通常比需要的嚴格。

這不推翻本頁的結論（harness 的工作從補能力變成設邊界），
而是指出邊界的**最小形式**是什麼：五個欄位，寫在動手之前。

## 相關頁面

- [[task-contract]] —— 邊界的最小形式，每一欄對應一種做太多
- [[harness-engineering-complete-guide]] —— 契約語言的來源

- [[prompting-claude-opus-5]] —— 來源
- [[prompt-obsolescence]] —— 過度驗證來自過期的指令
- [[can-judgment-be-outsourced]] —— 模型行使判斷的證據
- [[harness-engineering]] —— harness 的工作性質改變了
- [[autonomy-tiering]] —— 畫界線的具體機制
- [[the-ai-native-sdlc-playbook]] —— 分級的來源
- [[running-a-software-factory-at-uber-scale]] —— 替委派定價而不是禁止委派
- [[managed-agents]] —— 把這些設定收到可控位置
