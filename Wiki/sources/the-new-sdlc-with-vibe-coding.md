---
title: The New SDLC With Vibe Coding
type: source
aliases: [新的軟體開發生命週期]
tags: [ai, 軟體工程, 工作方法, 白皮書]
created: 2026-08-01
updated: 2026-08-30
status: active
confidence: high
source_type: report
author: Addy Osmani、Shubham Saboo、Sokratis Kartakis（Google）
published: 2026-05-01
url: unknown
raw: "[[2026-08-01--the-new-sdlc-with-vibe-coding]]"
ingested: 2026-08-01
---

# The New SDLC With Vibe Coding

> Google 出的 51 頁白皮書，副標「From ad-hoc prompting to Agentic Engineering」。
> 主軸：vibe coding 與 agentic engineering 不是二元對立，是**光譜**，
> 而位置由「驗證」與「harness」決定，不是由用不用 AI 決定。

## 核心主張

### 1. 光譜，不是二選一（[[vibe-coding-spectrum]]）

分辨的關鍵不是有沒有用 AI，而是**AI 的輸出被多少結構、驗證與人類判斷包住**。
最大的單一差異項是**輸出怎麼被驗證**：測試驗證確定性的部分，evals 驗證非確定性的部分
（軌跡對不對、工具選得對不對、最終回應有沒有到品質線）。**兩者缺一，就還是 vibe coding。**

### 2. 真正的技能是 context engineering（[[context-engineering]]）

程式碼品質取決於**脈絡的品質**，不是 prompt 的巧妙。六種脈絡：
Instructions、Knowledge、Memory、Examples、Tools、Guardrails。
關鍵的架構決策是**靜態 vs 動態**：靜態脈絡（`AGENTS.md`／`CLAUDE.md`／`GEMINI.md`）每次都載入所以昂貴，
動態脈絡（[[agent-skills|skills]]、工具結果、RAG）只在需要時付費。

> 問題不是「怎麼騙 AI 寫出好程式」，是「一個新來的隊友需要知道什麼，我怎麼把它編碼成 AI 能用的形式」。

### 3. Agent = Model + Harness（[[harness-engineering]]）

把模型當成系統是錯的直覺，而且會導致錯誤的投資。開發者感受到的行為主要由 harness 決定。
**大多數 agent 失敗，誠實檢視之後，都是設定失敗。**

### 4. 工廠模型（[[factory-model]]）

開發者的主要產出不是程式碼，是**產出程式碼的那套系統**。
工廠經理不手工組裝每個零件，他設計產線並確保品質。

### 5. 指揮家與協調者（[[conductor-and-orchestrator]]）

conductor 是即時、貼身、在 IDE 裡導引；orchestrator 是非同步、多 agent、只定義目標與審查結果。
同一個開發者一天內會在兩種模式間流動。

### 6. 80% 問題（[[the-80-percent-problem]]）

AI 能快速生出約 80% 的程式碼，剩下 20%（邊界情況、錯誤處理、整合點、細微的正確性要求）
需要模型目前缺乏的深度脈絡。而且錯誤的性質變了：從語法錯變成**概念錯**，
因為程式碼「看起來對」而且可能通過基本測試，反而更難抓。

### 7. 經濟學（[[ai-development-economics]]）

Vibe coding 是低 CapEx、**高 OpEx**（token 燃燒、維護稅、資安補救）；
agentic engineering 是高 CapEx、低 OpEx。**Context engineering 是財務槓桿，不只是技術技能。**

## 關鍵數據

| 項目 | 數值 | 出處 |
|---|---|---|
| 專業開發者常態使用 AI coding agent | 85% | 2026 年初，尾註 1 |
| 每日使用 | 51% | 同上 |
| 新程式碼由 AI 生成的比例 | 估計 41% | 同上 |
| 產業調查的生產力提升 | 25–39% | 尾註 7 |
| **METR 研究：資深開發者在特定任務上反而慢了** | **19%** | 尾註 8/10 |
| Terminal Bench 2.0：只改 harness 不換模型 | 從 Top 30 外進到 Top 5 | — |
| LangChain：只調系統提示、工具、middleware | +13.7 分 | — |

## 值得引用的原文

> "Most agent failures, examined honestly, are configuration failures."

> "AI amplifies the engineering culture it lands in."

> "Structure scales, vibes don't."

> "Generation is solved. Verification, judgment, and direction are the new craft."

## 建議動作（可直接照做）

**個人**：建 `AGENTS.md`（從十行開始：技術棧、慣例、硬規則、工作流程，agent 每犯一次錯就加一條規則）；
挑一個重複的工作流程做成第一個 agent；**先寫測試與 evals 再生成程式碼**；要上線的每一行都審過；
保持自己的基本功。

**團隊**：把 `AGENTS.md`、系統提示、eval 套件、skill 庫當成程式碼——進 PR 審查、跟專案一起版控、有具名負責人。
**把標準設在 eval，不是 demo。** 明確區分原型工作與生產工作的界線，否則會「不小心把原型上線」。

**組織**：先建生產基座再談規模；採用開放標準（MCP、A2A）；
**依判斷力而非實作能力重新設計招募**。

## 對 wiki 的影響

- 新增：[[vibe-coding-spectrum]]、[[context-engineering]]、[[harness-engineering]]、[[factory-model]]、[[conductor-and-orchestrator]]、[[the-80-percent-problem]]、[[ai-development-economics]]、[[agent-skills]]、[[addy-osmani]]
- 更新：[[judgment]]（第三份來源，且是唯一帶數據的一份）、[[can-judgment-be-outsourced]]（提供了「層級移動說」的證據）、[[design-is-the-new-code]]、[[elephant-goldfish-model]]
- **矛盾**：本文同時引用「25–39% 生產力提升」與「METR：資深開發者慢 19%」，自己沒有調和

## 我的判讀

（推論）這是本庫**第一份帶數據的來源**（2026-08-30 更新：[[metr-early-2025-ai-developer-productivity]]
與 [[metr-2026-uplift-update]] 之後不再是唯一），也是唯一會自己引用反面證據的來源，這點加分。

**但它引用 METR 的方式有問題**：只取了「慢 19%」這個數字，沒有提時效限定，
也沒有提那份研究的作者已在頁首宣告結果過期。見 [[what-the-19-percent-measures]]。
但它是 Google 出的白皮書，結論指向 ADK、Agents CLI、Jules、Gemini——利益方向要打折。
最硬的是 harness 那兩個 benchmark 數字（只改 harness 就大幅移動排名），那是可驗證的。
最軟的是「85% 的專業開發者」——尾註指向兩個內容行銷型網站，不是調查機構。

## 相關頁面

- [[vibe-coding-spectrum]] —— 本文的核心框架
- [[context-engineering]] —— 本文認定的真正技能
- [[harness-engineering]] —— Agent = Model + Harness
- [[the-80-percent-problem]] —— 最誠實的一節
- [[addy-osmani]] —— 主要作者
- [[two-sdlc-frameworks]] —— 與 Anthropic 那份 SDLC 框架的逐項比較
