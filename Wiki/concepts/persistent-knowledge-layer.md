---
title: 持久知識層
type: concept
aliases: [persistent knowledge layer, 三層知識架構, never reset]
tags: [ai, agent, skill, 知識庫, 架構]
created: 2026-09-01
updated: 2026-09-01
status: active
confidence: medium
sources: ["[[wikiskill]]"]
---

# 持久知識層

> 在**原始經驗**與**可執行程序**之間插一層會累積、永不重置的知識。
> 程序可以被回滾，知識不回滾——這個不對稱就是整個設計。

## 三層與它們的性質

[[wikiskill]] 把 agent 工作區切成三層，每層標了一個性質：

| 層 | 內容 | 性質 |
|---|---|---|
| `raw/` | 完整執行軌跡 | Permanent, Write Once |
| `wiki/` | 失效模式與成功策略的 pattern 頁、索引、演化日誌、提案影響紀錄 | **Compounding, Never Reset** |
| `skills/` | 現行程序知識 | Reversible, Conditional Update |

差別不在存什麼，在**改動規則不同**：軌跡寫完不動，知識只增不減，程序隨時可能被整包退回上一版。

## 為什麼知識不能跟著程序一起回滾

因為**一個提案被拒絕，本身就是知識**。

WikiSkill 的 gating 是硬的：候選 skill 在驗證集上分數沒有超過歷史最佳就整包回滾。
但無論接受或拒絕，harness 都以程式把提案內容、unified diff、驗證分數、
接受與否寫進 `skill-impact.md`。原文列了這份紀錄的三個用途，第一個最關鍵：

> "(1) observe the complete skill acceptance history so that **rejected interventions are not
> proposed again**"

（推論）如果知識跟著程序一起回滾，系統就會忘記自己試過什麼，
於是每一輪都可能重提同一個已經被否決的方案。
**回滾程序是為了保護當下的表現，保留知識是為了保護學習速度。** 兩者要分開。

## 它值多少：+15.0 分

這是本庫第一次看到有人把「知識層」當成單一變數隔離出來測。
其他條件不變，只看 Skill Proposer 有沒有讀得到持久 wiki
（Gemini-3.5-Flash，四個 benchmark 平均）：

- 沒有：**48.7%**
- 有：**63.7%**

差 **15.0 分**。原文的說法是，沒有跨輪累積的知識，Proposer「難以解決複雜的失效模式」。

界定它證明了什麼：這是 benchmark 答對率，不是真實工作的產出
（[[evidence-types-for-ai-capability]]）。它證明持久知識層在這五個 benchmark 上有效，
不證明它讓真實開發工作變快。

## 反直覺的一條：執行者不該讀知識層

WikiSkill 的預設設定是**禁止 Inference Agent 在訓練 rollout 期間讀 wiki**。
給它讀反而更差：63.7% → 60.9%，LiveMath 從 72.6 掉到 64.8。

原文的假說是：agent 同時拿得到 skill 與 wiki 時，
有些解題知識**直接從 wiki 拿走了而不是從 skill 拿**，
於是產生的軌跡對 skill 開發的資訊量下降。

（推論）這對 [[context-engineering]] 是一個新維度。
本庫原本只有「靜態 vs 動態」——什麼時候載入。這裡多了一條：**誰該載入**。
把知識塞給執行者，短期看起來像是幫忙，實際上污染了用來改進程序的訊號。

（推論）換到本庫的尺度就是：查詢時直接讀 `Wiki/` 是對的，
但如果 ingest 的判斷也總是先讀既有結論再看原文，
那些「原文讓我改變想法」的時刻就不會留下痕跡。

## 與本知識庫的關係

本庫的結構與這篇的三層是同一個形狀，而且比對之後看得出缺什麼：

| WikiSkill | 本庫 | 差異 |
|---|---|---|
| `raw/` 執行軌跡，不可變 | `Raw/` 原始來源，只有使用者能寫（`[L1]`） | 同構 |
| `wiki/patterns/` + `index.md` + `logs.md` | `Wiki/` + `index.md` + `log.md` | 同構 |
| `skills/` + `PURPOSE.md` | `.claude/skills/` + `CLAUDE.md` + `.claude/rules-ledger.md` | 同構 |
| `skill-impact.md`：被拒提案的 diff 與分數 | **沒有** | **本庫缺這一格** |

`PURPOSE.md` 把 skill 反指回啟發它的 pattern，這正是 `.claude/rules-ledger.md` 在做的事
（見 [[open-questions]] Q10）。差別在那份帳只記**被採用的**規則；
本庫沒有任何地方記錄「試過、被否決、為什麼」。

（推論）這是本庫可以直接照做的一條：`log.md` 記的是做了什麼，
缺的是**沒做什麼以及為什麼不做**。

## 作者自己指出的破口

`wiki/` 只增不減，而 WikiSkill **沒有自動 pruning 機制**。
原文承認演化跑久之後可能需要修剪。

（推論）這條直接撞上 [[prompt-obsolescence]]：只增不減的知識庫，
遲早會累積出已經不成立的 pattern，而「永不重置」的設計讓它們沒有出口。
本庫有同樣的問題，目前唯一的對策是 `[L5]` 的保留型／維護型之分與人工健檢。

## 相關頁面

- [[wikiskill]] —— 來源
- [[agent-skills]] —— 被這一層驅動的那一層
- [[context-engineering]] —— 「誰該載入」這個新維度
- [[agent-config-evals]] —— gating 與回滾的另一種形狀
- [[prompt-obsolescence]] —— 只增不減的知識庫必然遇到的問題
- [[harness-engineering]] —— 這一層是 harness 的一部分
- [[skill-transfer-across-models]] —— 同一份研究的另一個結果
- [[evidence-types-for-ai-capability]] —— 這個 +15.0 分能撐到哪裡
