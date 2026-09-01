---
title: 工廠模型
type: concept
aliases: [factory model]
tags: [ai, 軟體工程]
created: 2026-08-01
updated: 2026-09-01
status: active
confidence: medium
sources: ["[[the-new-sdlc-with-vibe-coding]]", "[[the-ai-native-sdlc-playbook]]", "[[running-a-software-factory-at-uber-scale]]"]
---

# 工廠模型

> 開發者的主要產出不是程式碼，是**產出程式碼的那套系統**。

## 系統包含什麼

- 定義要建什麼的規格與脈絡
- 把規格翻譯成實作的 agent
- 驗證正確性的測試與品質閘門
- 把失敗路由回 agent 修正的回饋迴圈
- 把 agent 限制在安全可預期行為裡的 guardrails

工廠經理不手工組裝每個零件，他設計產線並確保品質控制。
**成功來自給 agent 成功判準，而不是逐步指令**，然後讓它自己迭代。

## 它怎麼改變 SDLC 各階段

| 階段 | 變化 |
|---|---|
| 需求 | 不再是團隊之間交接的文件，變成人與 AI 的對話，**同時**產出規格與初步實作 |
| 架構 | **最頑固的人類環節**。架構是取捨（一致性 vs 可用性、複雜度 vs 彈性、自建 vs 採購），依賴 AI 抓不到的商業脈絡與長期考量 |
| 實作 | 從「寫」變成「審查、引導、驗證」 |
| 測試 | 不只評估產出，還要評估**軌跡**——流暢但跳過驗證步驟的輸出，比帶著明顯錯誤的輸出更危險 |
| 審查 | AI 當第一輪審查者，人保留設計、可維護性、策略對齊的判斷 |
| 維護 | 最被低估的變化。「只有原作者看得懂、風險太高不敢動」的程式碼現在可以被安全重構 |

## 邊界

（推論）「給成功判準而非逐步指令」與 [[elephant-goldfish-model]] 的 Phase 2
（要求列出**每一個**會被改動的檔案）表面上衝突。
比較可能的調和是層級不同：架構層給判準，實作層給清單。這兩份來源都沒有處理這個張力。

## Q8 的新證據：兩個層級都要，而且是分開的檔案

本頁的「邊界」一節懸著一個張力：本頁說給成功判準，
[[elephant-goldfish-model]] 要求列出每一個會被改動的檔案。

[[the-ai-native-sdlc-playbook]] 提供了第三個資料點，而且站在**兩者都對**那側——
因為它把兩層放進**不同的產物**：

- `spec.md`（Design 階段）是判準層：解決什麼問題、受什麼政策約束、哪裡有疑慮要升級。
- `plan.md`（Build 階段）是清單層：**哪些檔案會改**、工作順序、風險、什麼測試能證明它成立。

原文對 `plan.md` 的驗收標準寫得比 Rensin 還嚴：
**「迭代到一個從沒看過這段對話的工程師，只靠這份計畫就能實作出來為止。」**
而且實作偏離計畫時，`plan.md` 要在同一個 commit 裡被更新，可以用 hook 強制同步。

這支持了 [[open-questions]] Q8 原本那個「層級不同」的推論，
並且指出調和的方式不是折衷，是**拆成兩份被分別核准的文件**。

## 這個模型有一個組織版

本頁說開發者的產出是**產出程式碼的那套系統**。
[[managed-agents]] 是同一件事推到組織層級——
[[running-a-software-factory-at-uber-scale|Uber]] 不再優化幾千個工程師各自的終端機 session，
改成經營一支受管 agent 艦隊，每個配自己的 benchmark 與 Pareto 最優模型。

（推論）差別在**誰擁有那套系統**。本頁的工廠是個人的：你自己的規則檔、提示、工具。
受管 agent 把工廠收成組織資產——模型路由、執行 harness、花費全部變成可設定的東西，
而不是散在每個人的習慣裡。

代價原文也講了：這條路線要求任務**夠標準化到能建 benchmark**，
而且要有規模才攤得平固定成本。本頁的個人版沒有這兩個門檻。

## 相關頁面

- [[the-new-sdlc-with-vibe-coding]] —— 來源
- [[managed-agents]] —— 同一個模型的組織版
- [[running-a-software-factory-at-uber-scale]] —— 那個組織版的實例
- [[harness-engineering]] —— 工廠裡的機器周邊設施
- [[conductor-and-orchestrator]] —— 工廠經理的兩種工作模式
- [[design-is-the-new-code]] —— 同一主張的另一種說法
- [[addy-osmani]] —— 提出者
- [[the-ai-native-sdlc-playbook]] —— Q8 的新證據
- [[artifact-chain]] —— 判準層與清單層被拆進不同產物
