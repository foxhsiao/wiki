---
title: 兩份 SDLC 框架：Google 與 Anthropic
type: synthesis
aliases: [two SDLC frameworks, Google vs Anthropic SDLC]
tags: [ai, 軟體工程, 流程, 比較, 論點]
created: 2026-08-30
updated: 2026-08-30
status: active
confidence: medium
sources: ["[[the-new-sdlc-with-vibe-coding]]", "[[the-ai-native-sdlc-playbook]]"]
---

# 兩份 SDLC 框架：Google 與 Anthropic

> 觀念上高度相近，但問的問題不同。
> （推論）Google 那份的單位是**開發者**——你這個人該怎麼工作；
> Anthropic 那份的單位是**一個變更**——它怎麼從想法走到生產。
> 幾乎所有差異都能從這一點推導出來。

## 兩份是什麼

| | [[the-new-sdlc-with-vibe-coding]] | [[the-ai-native-sdlc-playbook]] |
|---|---|---|
| 出處 | Google（[[addy-osmani]]、[[shubham-saboo]]、Kartakis） | Anthropic Applied AI team |
| 日期 | 2026-05 | 2026（原檔日期不可信，取得日 2026-08-29） |
| 形式 | 51 頁白皮書 | 部落格長文，13 個 play |
| 副標／主軸 | From ad-hoc prompting to Agentic Engineering | 把 SDLC 從直線改成迴圈 |

## 相同的部分

| 主題 | Google | Anthropic |
|---|---|---|
| 核心診斷 | Generation is solved. Verification, judgment, and direction are the new craft. | Code is no longer the bottleneck. |
| 六階段 | 需求／架構／實作／測試／審查／維護 | Plan／Design／Build／Test／Deploy／Maintain |
| 制度知識檔案化 | `AGENTS.md`／`CLAUDE.md`／`GEMINI.md` ＋ skills | `CLAUDE.md` ＋ skills |
| 規則檔的維護法則 | agent 每犯一次錯就加一條規則 | 同一個錯**犯第二次**才寫進去 |
| 規則檔的地位 | 當成程式碼：進 PR 審查、版控、有具名負責人 | 同上，另加回歸測試 |
| 品質基準 | 「把標準設在 eval，不是 demo」 | CI 裡的 continuous evals，pass rate 掉了擋 merge |
| 人的位置 | 驗證、判斷、指揮 | [[judgment]]集中在**閘門**上 |

**六階段幾乎可以逐格對應**，這不是巧合——兩份都在改造同一個傳統 SDLC。
差別只在 Google 的「審查」被 Anthropic 併進 Deploy，而 Anthropic 把 Plan 獨立成
一個有專屬產物（[[intent-md|`intent.md`]]）的階段。

## 差異的部分

| 面向 | Google | Anthropic |
|---|---|---|
| **框架性質** | **描述性**——給你一把尺量自己落在[[vibe-coding-spectrum]]哪裡 | **規範性**——13 個 play，照著裝 |
| **位置由什麼決定** | **風險**（週末原型 vs 金流 API） | **環境**（dev 自由部署／staging／prod 要授權） |
| **控制的分層** | 沒有切開，`AGENTS.md`、skills、guardrails 並列在 [[harness-engineering]] 底下 | **明確切開**：skill 是建議、hook 才是控制 |
| **產物的意義** | 脈絡的載體（[[context-engineering]]的角度） | **稽核軌跡**——commit chain 就是誰要什麼、agent 產出什麼、誰核准 |
| **自治怎麼管** | [[conductor-and-orchestrator]]，人自己在兩種模式間流動 | [[autonomy-tiering]]：1σ 記錄／2σ 唯讀／3σ 只能提議 |
| **治理與法規** | 幾乎沒談 | 每個 play 都有治理考量、managed settings、職責分離 |
| **個人技能與人事** | 有：保持基本功、依判斷力招募 | 幾乎沒談 |
| **經濟學** | 有：CapEx／OpEx、[[ai-development-economics]] | 沒有成本模型 |
| **證據** | 帶數據，且會引用反面證據 | **零成效數字**，但每個 play 給兩個可否證的指標 |

**兩份的空白區幾乎不重疊**——Google 缺治理，Anthropic 缺經濟學與個人技能。
（推論）這讓它們比較像互補而不是競爭，也解釋了為什麼兩份放在一起讀比單讀任何一份有用。

## 觀念上最深的一條差異

（推論）同一個 harness，在兩份裡的**權屬**不同。

Google 說「多數 agent 失敗其實是設定失敗」，重點是**你要會調**——
harness 是一個開發者的工具箱，調得好是能力。

Anthropic 說 managed settings 由平台團隊經 MDM 派送，`allowManagedHooksOnly`、
`disableSideloadFlags`、`allowManagedPermissionRulesOnly`，重點是**你不准調**——
harness 是組織的產線設定，個別工程師關不掉。

這條差異不是矛盾，是同一件事在不同尺度上的樣子。
展開見 [[harness-engineering]] 的「harness 的作用範圍會擴到組織」。

## 兩條實質衝突（都已在本庫記錄）

### 1. 給判準還是給清單（[[open-questions]] Q8）

Google 的[[factory-model|工廠模型]]說「成功來自給 agent 成功判準，而不是逐步指令」；
Anthropic 的 `plan.md` 要求列出**每一個**會改動的檔案、工作順序、證明用的測試。

調和方式不是折衷，是**拆成兩份分別被核准的文件**：
`spec.md` 是判準層、`plan.md` 是清單層。見 [[artifact-chain]]。

### 2. skill 是不是控制

Google 把 skill 當制度知識的載體，與 guardrails 並列。
Anthropic 明說「nothing forces a session to comply with it」，
必須永遠成立的政策要有 hook 墊底。

**這條修正了本庫原本對 skill 的定位**——skill 是散布機制，不是控制。
見 [[advisory-vs-deterministic-control]] 與 [[agent-skills]]。

## 一個要打的折扣

兩份都是廠商文件，而且各自指向自家產品線：
Google 那份指向 ADK、Agents CLI、Jules、Gemini；
Anthropic 那份指向 Claude Code、Cowork、Claude Design、Claude Security、Claude Tag。

[[overview]] 的缺口那節記著同一件事：本庫談 AI 的六份來源只出自兩家公司，
**治理這一軸目前只有賣方視角**。所以上面那些「相同之處」要小心解讀——
兩家在同一個時間點賣同一類產品，框架趨同本來就有一部分是市場趨同，
不必然是因為它們各自獨立發現了同一個真相。

（推論）真正能檢驗這件事的，是一份買方或監管方視角的來源，本庫還沒有。

## 相關頁面

- [[the-new-sdlc-with-vibe-coding]] —— Google 那份
- [[the-ai-native-sdlc-playbook]] —— Anthropic 那份
- [[ai-native-sdlc]] —— Anthropic 那份的框架本體
- [[vibe-coding-spectrum]] —— Google 那份的核心框架
- [[advisory-vs-deterministic-control]] —— 兩份最實質的一條分歧
- [[harness-engineering]] —— 兩份對 harness 權屬的不同假設
