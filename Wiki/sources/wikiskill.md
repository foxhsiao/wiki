---
title: "WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution"
type: source
aliases: [WikiSkill, 三層知識架構]
tags: [ai, agent, skill, 評估, 知識庫]
created: 2026-09-01
updated: 2026-09-01
status: active
confidence: high
source_type: paper
author: Liyan Tang, Cyrus Rashtchian, Chun-Sung Ferng, Andrew Tomkins, Da-Cheng Juan, Tu Vu（Google Research、Virginia Tech）
published: 2026-08-27
url: https://arxiv.org/abs/2608.27454
raw: "[[2026-09-01--wikiskill-persistent-knowledge-skill-evolution]]"
ingested: 2026-09-01
---

# WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution

> 把 agent 的執行經驗編譯成一個**持續累積、永不重置**的 wiki，再由 wiki 驅動 skill 演化。
> 本庫第一份**用實驗隔離出「知識層本身值多少」**的來源——
> 而且它的三層架構與這個知識庫的結構是同一個形狀。

## 核心主張

- 現有的 skill 演化方法把「學到了什麼」散在最佳化歷史裡，**沒有維護成一個獨立的、會演化的知識表徵**。
- WikiSkill 在原始經驗與可執行程序之間插入一個**結構化知識層**，
  讓每一輪的 skill 更新建立在愈來愈完整的知識上。
- 靈感明說來自 Karpathy (2026) 的「LLM Wiki」觀點——把經驗編譯成持久、會複利的知識。
- **skill 可回滾，wiki 不回滾。** 這是整個設計的核心不對稱。

## 三層架構

| 層 | 內容 | 論文標的性質 |
|---|---|---|
| `raw/` | 完整執行軌跡（推理、工具呼叫、輸出、最終答案） | Permanent, Write Once |
| `wiki/` | `patterns/` 失效模式與成功策略、`index.md`、`logs.md`、`skill-impact.md` | **Compounding, Never Reset** |
| `skills/` | 現行 skill 集合，每個含 `SKILL.md` 與 `PURPOSE.md` | Reversible, Conditional Update |

`PURPOSE.md` 把每個 skill 反指回**啟發它的 wiki pattern**——也就是這條 skill 為什麼存在。

## 四步迴圈

1. **Inference Agent** —— 用現行 skill 跑 rollout，產生不可變軌跡。**訓練時被禁止讀 wiki**（理由見下）。
2. **Wiki Maintainer** —— 對失敗軌跡做**根因分析**、從成功軌跡萃取策略，
   以增量 patch 方式更新 pattern 頁，改動時同步修 `index.md`，並把本輪發現追加進 `logs.md`。
3. **Skill Proposer** —— 以 ReAct 方式運作。**不預先餵軌跡**，只給 wiki 索引、
   `skill-impact.md` 與任務結果摘要，讓它自己用 `read_file` 按需去讀 pattern 與軌跡。
   每輪只產出一個**原子提案**（新增一個 skill，或對單一 skill 做增量修補）。
4. **Gating & Rollback** —— 在驗證集上跑；分數超過歷史最佳才接受，否則整個提案回滾。
   接受與否，harness 都以程式把提案 metadata、目標 skill、unified diff、驗證分數、
   接受結果寫進 `skill-impact.md`。

## 關鍵事實與數據

實驗規模：5 個 benchmark（LiveMath、SealQA、SpreadsheetBench、OfficeQA、ALFWorld）
× 5 個模型（Qwen-3.5-4B/9B、Qwen-3.6-27B、Gemma-4-31B、Gemini-3.5-Flash），
**每個設定完整重跑三次獨立演化**，顯著性用 paired bootstrap（1,000 次，`p < 0.05`）。

**本庫最關心的一張表——ablation（Gemini-3.5-Flash，四個 benchmark 平均）：**

| Inference Agent 讀 wiki | Skill Proposer 讀 wiki | 平均 |
|---|---|---|
| （no skill 基線） | | 40.4 |
| 是 | 否 | 45.3 |
| 否 | 否 | 48.7 |
| 是 | 是 | 60.9 |
| **否** | **是** | **63.7**（預設設定） |

- **持久 wiki 值 +15.0 分**：其他條件不變，Skill Proposer 有無 wiki 是 48.7% → 63.7%
  （LiveMath 51.3 → 72.6、SpreadSheet 49.9 → 76.6）。
  Proposer 沒有 wiki 時，**無法解決複雜的失效模式**。
- **讓執行任務的 agent 讀 wiki 反而變差**：63.7% → 60.9%，LiveMath 72.6 → 64.8。

其他數字：

- 相對各模型最強的競爭方法，WikiSkill 平均高 **3.3 / 5.1 / 10.0 / 5.8 / 12.0** 分
  （Qwen-3.5-4B、Qwen-3.5-9B、Qwen-3.6-27B、Gemma-4-31B、Gemini-3.5-Flash）。
- **增益隨模型變強而變大**：Qwen 家族相對 no-skill 是 **+12.3 / +17.5 / +23.9** 分（4B / 9B / 27B）。
- **skill 可以補模型規模**：Qwen-3.5-9B + WikiSkill 平均 **47.4%**，
  勝過 Qwen-3.6-27B 無 skill 的 **39.4%**。
- **跨模型移轉可以勝過自己演化的**：Qwen-3.5-9B 在 ALFWorld 用自己的 skill 是 63.4%，
  用 Qwen-3.6-27B 演化的 skill 是 **70.2%**；SpreadSheet 是 24.3%（無）／33.6%（自己）／**50.5%**（27B 的）。
- **小模型演化的 skill 也能幫到大模型**：Qwen-3.5-4B 的 skill 讓 Gemma-4-31B
  在 LiveMath 拿 73.1%、ALFWorld 拿 66.9%。
- **但也有負移轉**：Qwen-3.5-4B 的 skill 讓 Gemini-3.5-Flash 在 SpreadSheet
  從 50.5% **掉到 18.1%**；同一個 benchmark 換成 Qwen-3.6-27B 的 skill 則升到 63.4%。
- **提案接受率很低**：以 Qwen-3.5-4B 為例，平均每輪提案新增 3.1 個 skill、接受 1.6 個；
  提案修改 4.9 次、接受 1.3 次。**wiki 那側則是「All wiki pattern creations and edits are retained」。**
- skill 長度隨模型不同：Qwen 家族 118.9–128.6 行，Gemma-4-31B 45.1 行，Gemini-3.5-Flash 81.2 行。

## 值得引用的原文

wiki 為什麼不重置（§3.1）：

> "The wiki is not reset between iterations, but rather accumulates and compiles knowledge
> continuously throughout the evolution process."

gating 的不對稱（§3.2.4）：

> "Notably, the wiki 𝑊𝑘 is never rolled back regardless of the acceptance decision; accumulated
> patterns and logs persist across all iterations to ensure long-term knowledge retention."

`skill-impact.md` 的用途（§3.1）——這是本庫 `log.md` 沒有做到的事：

> "These records allow the Wiki Maintainer and Skill Proposer to (1) observe the complete skill
> acceptance history so that **rejected interventions are not proposed again**, (2) track what was
> proposed in prior iterations and whether those proposals succeeded, and (3) identify which
> errors recur across iterations."

執行者不該讀 wiki（§5.1）：

> "We hypothesize that when the Inference Agent has access to both skills and the wiki during
> training rollouts, **some task-solving knowledge may be obtained directly from the wiki rather
> than the skills**, which can make the resulting trajectories less informative for skill development."

移轉結果最反直覺的一句（§4.2.2）：

> "Our results indicate that **stronger source models do not necessarily produce better skills**
> and that procedural knowledge developed by one model’s experience can transfer across model
> scales and families."

負移轉的機制（§4.2.2）：

> "First, Qwen-3.5-4B skills encode **low-level workarounds**, such as single-line Python commands
> and string-conversion rules, which help the smaller model avoid execution failures but
> **constrain stronger models** such as Gemini-3.5-Flash from using comprehensive end-to-end scripts."

發現能力與執行能力是兩回事（§1）：

> "These results suggest that **skill discovery and skill execution are distinct capabilities**."

## 作者自陳的限制

1. skill 是**直接注入提示**，不測 retrieval 與觸發——skill 一多，這會變成問題。
2. gating 要求每個被接受的提案**必須提高驗證分數**，因此排除了
   「當下持平、但為後續鋪路」的中性提案。作者說這是為了與既有框架公平比較。
3. **wiki 沒有自動 pruning 機制**。pattern 頁、演化日誌、提案 diff 一直累積，
   演化跑久了可能需要修剪。
4. benchmark 不含**很長 horizon** 的任務（數百個動作或數小時）。

另有一則 AI Disclosure：寫作潤飾與部分表格圖表由 LLM 與 coding agent 協助產生。

## 對 wiki 的影響

- 新增：[[persistent-knowledge-layer]]、[[skill-transfer-across-models]]
- 更新：[[harness-engineering]] —— 本庫第一個把 harness 效果單獨隔離出來的數字
- 更新：[[context-engineering]] —— 靜態／動態之外的第三個維度：**誰該讀到**
- 更新：[[agent-skills]] —— skill 與知識該分層，且 skill 可移轉
- 更新：[[agent-config-evals]] —— gating／rollback 的具體形狀，含被拒提案要留下 diff
- 更新：[[prompt-obsolescence]] —— 負移轉是「規則綁在特定模型上」的實驗證據
- 更新：[[can-judgment-be-outsourced]] —— 解法 1（有損壓縮說）第一次遇到反向證據
- 更新：[[open-questions]] Q2、Q15、Q13（突變測試從 15 種增為 22 種）
- 照做：規則 `[W9]` 與 `.claude/rejected-proposals.md`，見 [[two-wiki-architectures]]
- 衝突：與本庫既有主張沒有正面衝突，但**削弱了解法 1**，見該頁。

## 我的判讀

（推論）這是本庫收錄過**方法最紮實**的一份 AI 工程來源，理由：三次獨立重跑、
paired bootstrap 顯著性檢定、四格 ablation 隔離變數、負面結果照登（負移轉、
執行者讀 wiki 反而更差）、限制自己列了四條。

要打的折也很明確：

1. **這是 arXiv 預印本，不是同儕審查後的版本。**
2. **提出方法的人測自己的方法**，且對照組（Trace2Skill、EvoSkill、SkillOpt）由他們自己實作。
3. **全部是 benchmark**。[[evidence-types-for-ai-capability]] 說 benchmark 傾向高估，
   而且這裡量的是「答對率」，不是真實工作裡的價值。
4. 五個模型裡 Gemini-3.5-Flash 是 Google 自家的，而作者主要在 Google Research。

**所以它能撐什麼、不能撐什麼要分清楚**：它能撐「在這五個 benchmark 上，
持久知識層讓 skill 演化明顯變好」；它撐不起「持久知識層讓真實開發工作變快」——
那是 [[open-questions]] Q15 問的問題，而這份來源沒有回答（見 [[what-the-19-percent-measures]]
對 benchmark 與真實工作差距的討論）。

## 產業上有人在做同一件事

[[running-a-software-factory-at-uber-scale|Uber]]（2026-08-29）的「進行中工作」有一條：

> "**Continuous Skill Improvement**: We are working on an automated way to record papercuts from
> agent skill executions and **auto-generate skill updates from the collected traces**."

那正是本篇的迴圈——從執行軌跡回頭改進 skill。Uber 已經有超過 3,600 個 skill、
每天超過 30K 次執行，也就是本篇需要的那種軌跡量它天然就有。

（推論）兩者的落差在 gating：本篇花最多篇幅在
「驗證分數沒超過歷史最佳就整包回滾、被拒的提案留 diff」，
Uber 那條還是「working on」，沒有說怎麼判斷一次自動更新是不是改善。
本篇的 ablation（知識層值 15.0 分）與接受率數字（每輪提 3.1 個只收 1.6 個）
正好是那個問題的答案形狀。

## 相關頁面

- [[persistent-knowledge-layer]] —— 本篇的核心設計
- [[skill-transfer-across-models]] —— 本篇對 Q2 最有份量的結果
- [[harness-engineering]] —— 第一個被隔離出來的 harness 效果數字
- [[context-engineering]] —— 「誰該讀到」這個維度的來源
- [[agent-skills]] —— skill 與知識分層的實驗依據
- [[agent-config-evals]] —— gating 與 rollback 的具體形狀
- [[prompt-obsolescence]] —— 負移轉是折舊第一層的實驗證據
- [[can-judgment-be-outsourced]] —— 被本篇削弱的解法 1
- [[evidence-types-for-ai-capability]] —— 判定本篇份量的尺
- [[two-wiki-architectures]] —— 本篇與本庫架構的逐格比對
- [[running-a-software-factory-at-uber-scale]] —— 產業上在做同一件事的一方
