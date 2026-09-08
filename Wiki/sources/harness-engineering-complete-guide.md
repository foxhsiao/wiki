---
title: "Harness Engineering: The Complete Guide to Building AI Agents That Don't Fall Apart"
type: source
aliases: [Harness Engineering Complete Guide, LunarResearcher 2026, harness 完整指南]
tags: [ai, agent, harness, 工作方法]
created: 2026-09-08
updated: 2026-09-08
status: active
confidence: low
source_type: article
author: "@LunarResearcher"
published: 2026-09-06
url: https://x.com/LunarResearcher/status/2096570562625655088
raw: "[[2026-09-08--harness-engineering-complete-guide]]"
ingested: 2026-09-08
---

# Harness Engineering: The Complete Guide to Building AI Agents That Don't Fall Apart

> 19 節的 X 長文，把 [[harness-engineering]] 從一個名詞寫成一份**可照著建的規格**：
> 八個欄位、六個層級、一條量測比值。零數據。

## 核心主張

- **多數 agent 失敗是環境失敗，不是推理失敗。** 開頭列的六種失敗全部沒有一個是模型答錯：
  不知道哪些檔案重要、在錯的地方用對的工具、丟失上一個 session 的決定、
  沒跑檢查就宣稱成功、部分失敗後重複同一個動作、有權限做本該需要核准的事。
- **提示改變一次嘗試，harness 改變每一次嘗試。**
- **完成必須由環境證明，不能由模型宣稱。**
- **政策要放在推理迴圈外面**，因為有些規則不該取決於模型記不記得。
- **harness 本身也會折舊，而且要主動刪。** 見 [[harness-decay]]。

## 八欄位規格（§17）

原文稱 `AGENT HARNESS SPEC`，並說欄位沒定義完就不叫自主：

| 欄位 | 內容 | 本庫對應頁 |
|---|---|---|
| 1. CONTRACT | objective、scope、constraints、acceptance evidence | [[task-contract]] |
| 2. CONTEXT | 常駐地圖、檢索來源、局部指令、新鮮度規則 | [[context-engineering]] |
| 3. TOOLS | 允許的工具、前置條件、副作用、成功證據、逾時與重試策略 | [[context-tax]] |
| 4. STATE | facts、decisions、progress、lessons、checkpoint 格式 | [[persistent-knowledge-layer]] |
| 5. POLICY | 自動動作、需核准動作、禁止動作、預算上限 | [[advisory-vs-deterministic-control]] |
| 6. VERIFICATION | 確定性檢查、對抗性檢查、驗收規則 | [[completion-evidence]] |
| 7. RECOVERY | 失效類別、重試上限、升級條件、安全回滾 | [[completion-evidence]] |
| 8. OBSERVABILITY | trace 事件、指標、最終 change receipt | [[harness-engineering]] |

## 六層漸進建法（§16）

1. 有邊界的任務（目標、範圍、限制、驗收檢查）
2. 可讀的環境（專案地圖、指令、局部說明、已知相依）
3. 受控的動作（型別化工具、參數驗證、路徑與權限邊界、結構化結果）
4. 持久的執行（明確 run state、checkpoint、決定、教訓）
5. 證據（確定性檢查、對抗性驗證、change receipt）
6. 恢復與學習（失效分類、有界重試、升級、由重複失敗驅動的 harness 更新）

判準只有一條，而且是本篇最該記住的一句：

> "Build the smallest layer that eliminates the failure you actually have. …
> **Complexity should be earned by observed failure.**"

## 關鍵事實與數據

| 項目 | 數值 | 出處位置 |
|---|---|---|
| 實驗、benchmark、田野數據 | **零** | 全文 |
| 節數 | 19 節 | 全文 |
| 提出的量測比值 | `accepted outputs ÷ (human review minutes + run cost)` | §18 |

**這一格是空的，而且必須被寫出來。** 全文沒有任何一個數字、實驗或案例，
所有主張都是形狀論證。詳見〈我的判讀〉。

## 值得引用的原文

> "**Harness Engineering is the practice of building the environment that turns model intelligence
> into reliable work.** A prompt changes one attempt. A harness changes every attempt."（§前言）

> "A powerful model inside a weak harness is still a weak agent."（§1）

> "Without a contract, the agent optimizes for **plausible activity**.
> With a contract, it can optimize for **verified completion**."（§2）

> "The objective is not maximum context. It is **maximum signal per token**."（§3）

> "Giving an agent twenty tools does not make it capable.
> It gives the agent twenty ways to make a mistake."（§4）

> "**Do not use another model where a compiler, schema, checksum, query, or test can answer the
> question.** Use models for ambiguity. Use code for plumbing."（§7）

> "A model can propose that the task is complete. **Only the environment can prove it.**"（§7）

> "If you ask the same agent, in the same context, to 'double-check its work,'
> it often **preserves the assumptions that created the mistake**. …
> Verification is not a second opinion. **It is an attempted disproof.**"（§8）

> "**Autonomy is not the absence of control.**
> It is the ability to operate freely inside a clearly enforced boundary."（§9）

> "**A retry should change at least one relevant condition.**
> Otherwise the system is paying to reproduce the same failure."（§10）

> "The prompt should explain judgment. The harness should enforce invariants."（§11）

> "The receipt is not a summary of what the model said.
> It is a summary of **what the system can prove**."（§13）

> "A corrected answer helps one run. **A corrected harness helps every future run.**"（§14）

> "The best harness is not the largest one. It is **the smallest system that reliably closes the
> gap between intent and evidence**. **Build to delete.**"（§15）

> "If these fields are undefined, the agent is not autonomous. **It is improvising.**"（§17）

> "An agent can look highly productive while creating expensive review work.
> The objective is not more agent activity.
> It is **more trusted outcomes per unit of human attention**."（§18）

## 對 wiki 的影響

- 新增：[[task-contract]]、[[harness-decay]]、[[completion-evidence]]
- 更新：[[harness-engineering]] —— 補上「怎麼建」那一半，以及 §18 的量測比值
- 更新：[[prompt-obsolescence]] —— 折舊的對象從規則檔擴到整個 harness
- 更新：[[advisory-vs-deterministic-control]] —— 兩格的區分被撐成五格的指令階梯
- 更新：[[autonomy-tiering]] —— §9 的分級軸線與 `bands.yaml` 不同，並列
- 更新：[[context-engineering]] —— 「給地圖不給手冊」與 context flooding
- 更新：[[persistent-knowledge-layer]] —— 記憶四類與本庫三層的對應
- 更新：[[agent-config-evals]] —— verifier 的職責不對稱
- 更新：[[open-questions]] —— Q15 拿到一個候選的量測形式
- 衝突：原文 §14（每次失敗都該讓 harness 長出新基礎設施）與 §15（harness 會肥、要 build to delete）
  彼此拉扯，原文並置卻沒調和。記在 [[harness-decay]]。

## 我的判讀

（推論）**這是本庫證據等級最低的一份，比 [[ai-engineering-skills-map-software-fundamentals]] 還低**——
那份至少掛著可查證的作者。理由要列清楚，因為這一頁的內容很好用，
好用到容易忘記它沒有證據：

| 折扣項 | 內容 |
|---|---|
| 零數據 | 沒有實驗、沒有 benchmark、沒有案例、沒有客戶名 |
| 匿名 | `@LunarResearcher` 沒有可查證的身分、機構或作品紀錄，本庫因此**不為它開實體頁** |
| 有導流動機 | 文中三處導向作者的 Substack 訂閱 |
| 論證方式 | 全篇是形狀論證與 ASCII 圖，沒有一句「我們量到」 |

（推論）它的價值不在證據，在**詞彙與結構**——本庫先前談 harness 一直是列元件清單
（[[harness-engineering]] 的六個元件），沒有「照什麼順序建、建到哪裡可以停」。
這份補上了那個維度，而且 §15、§16 兩節的自我約束（build to delete、
complexity should be earned by observed failure）罕見地反著賣方誘因寫。

**一個獨立的旁證。** §15 的五個汰除問題——「這防哪一種失敗？那種失敗現在還多常發生？
它加了多少延遲與複雜度？移掉會怎樣？」——與本庫 `.claude/rules-ledger.md` 的
`[W8]`（新規則要寫可否證的預期效果）是同一個主意，而兩邊互不知道對方。
（推論）這不提高本庫規則的正確性，但它把「規則帳」從一個本地習慣變成
**有第二個人獨立想到的做法**。

**最該小心的一點**：本篇讀起來像經驗總結，但它可能只是把已公開的 agent 框架
（工具閘門、verifier 子 agent、trace、風險分級）重新整理成一份清單。
本庫收錄它的方式應該是**當詞彙表用，不當證據引**——
任何一句要拿來支撐主張的，都要去找有數據的來源交叉。

## 相關頁面

- [[harness-engineering]] —— 被這份補完的主頁
- [[task-contract]] —— §2、§17 的第一欄
- [[harness-decay]] —— §15，本篇最反直覺的一節
- [[completion-evidence]] —— §7、§8、§10
- [[advisory-vs-deterministic-control]] —— §11 把它從兩格撐成五格
- [[autonomy-tiering]] —— §9 提供另一條分級軸線
- [[context-engineering]] —— §3 的 context flooding 與專案地圖
- [[persistent-knowledge-layer]] —— §6 的記憶四類
- [[agent-config-evals]] —— §8 的 verifier 不對稱是它的前提
- [[open-questions]] —— §18 的比值是 Q15 的候選形式
- [[ai-engineering-skills-map-software-fundamentals]] —— 先前證據等級最低的一份，現在被這份取代
- [[how-to-fix-your-entire-life-in-1-day]] —— 同一週進來、同樣零數據的另一份 `confidence: low` 來源
- [[control-loops-human-and-agent]] —— 同一週進來的另一份來源與它同形
