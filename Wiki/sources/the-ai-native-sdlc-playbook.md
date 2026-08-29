---
title: The AI-Native SDLC Playbook
type: source
aliases: [AI-native SDLC, agentic SDLC, SDLC playbook]
tags: [ai, 軟體工程, agent, 流程, 治理, 官方文件]
created: 2026-08-29
updated: 2026-08-29
status: active
confidence: high
source_type: article
author: Anthropic Applied AI team（致謝 Jim Blackhurst、Will Steuk、Jamal Arif）
published: unknown
url: https://claude.com/blog/the-ai-native-sdlc-playbook
raw: "[[2026-08-29--the-ai-native-sdlc-playbook]]"
ingested: 2026-08-29
---

# The AI-Native SDLC Playbook

> 本庫第一份**組織層級的操作手冊**。前六份談的是個人怎麼跟 AI 工作，
> 這份談的是一間受監管的公司怎麼把整條軟體生命週期重建成迴圈，
> 而且每一個 play 都附上治理證據與兩個可量測指標。

## 核心主張

### 1. 瓶頸位移：code 不再是瓶頸，左右兩側才是

> "Code is no longer the bottleneck."

傳統 SDLC 六階段的控制手段，是為「寫程式是最貴最慢的那一段」而設計的。
當 build 塌縮成幾小時，三件事同時成立：

- 瓶頸移到 build **左右兩側**——plan、review/test、deploy 仍在人的速度；
- **控制手段失真**：逐行人工審查在人寫程式時合理，agent 寫掉大部分 diff 之後跟不上；
- **治理成本上升**：例外仍然要走每週或每月才開一次的會議與委員會。

原文給的例子是資安：資安團隊的編制是照人的產出量設計的，
agent 一放大產出，結果只有兩種——審查佇列塞爆，或程式碼在審查不足的情況下上線。
受監管的組織兩種都不能接受。

### 2. 貫穿線是 committed artifact，commit chain 就是稽核軌跡

這是全文最重要的結構性主張（[[artifact-chain]]）。每個階段以**寫一份產物進版控**收尾，
下一個階段以**讀它**開始：

`intent.md` → `spec.md` → `plan.md` → diff 與它的測試 → PR 與審查發現 → 事故紀錄 → 回到 `intent.md`

> "The chain of commits is also the audit trail: who asked for what, what the agent produced,
> and who approved it."

早期階段用 `.md` 是因為**產品負責人與 agent 讀的是同一個檔案**；build 之後產物變成程式碼與它的紀錄。

### 3. skill 是建議，hook 才是控制

原文對自家機制講得罕見地保守（[[advisory-vs-deterministic-control]]）：

> "A skill is a control, though an advisory one. It makes Claude likely to apply the policy
> while the code is written, and **nothing forces a session to comply with it**."

> "The skill makes violations rare and the hook makes them close to impossible."

必須永遠成立的政策，後面要墊一個確定性的東西：擋掉動作的 hook，或在 PR 再檢一次的審查回合。

### 4. 操控 agent 的設定檔要像程式一樣被回歸測試

`CLAUDE.md`、skills、hooks 一改就在 CI 跑 eval suite，pass rate 掉了就擋 merge
（[[agent-config-evals]]）。suite 由 20 到 50 個**近期真實任務**構成，
每次生產事故都要變成一條永久 eval 留在裡面。

> "...since that configuration steers the agent and deserves the regression testing that code gets."

### 5. 自治要分級，而且偵測必須保持確定性

`bands.yaml` 把回應分三層（[[autonomy-tiering]]）：1σ 只記錄、2σ 唯讀診斷、
3σ 才可行動——而且行動只能是「開一個 PR 進審查閘門」或「觸發預先核准的 runbook」。

> "Detection stays deterministic. Claude is invoked once a band is breached, and the tier sets
> what it may do."

部署面的原則一句話：

> "The governing principle is that the agent may act up to the production gate and cannot pass it."

### 6. 迴圈閉合：沒有人在觸發路徑上

Stage 6 讓監控腳本、ticket、Slack 訊息或排程直接叫起 Claude，
它診斷完把結果寫成 `intent.md`（[[intent-md]]）丟回 Stage 1，整條流程重跑一次。
人**分流與審查**這些工作，不再需要**啟動**它們。

## 六階段的位移

| 階段 | 傳統 | AI-native |
|---|---|---|
| Plan | 委員會蒐集需求、工作坊提煉、簽核後手寫 | Claude 直接從來源萃取痛點，寫成人可讀、機器可執行的 `intent.md` |
| Design | 分析師寫規格、設計師再解析一次 | 需求與設計壓縮進**同一個** session，用 skill 編碼的標準約束，版控在 git |
| Build | 手寫測試與程式碼，文件事後補 | 測試與程式碼由 AI 生成，制度知識維護成版控的 `CLAUDE.md` 與 skills |
| Test | 階段邊界上的 QA 閘門 | 連續 eval 織進實作過程 |
| Deploy | 人審每一行，治理發生在審查週期、常不一致 | 多層 agent 審查，人審保留給受監管與關鍵程式碼；治理在 agent 動作當下強制，hook 當核准閘門 |
| Maintain | 人盯生產環境找 bug | agent 盯線上部署，任何越界的控制帶被診斷後寫回成新的 `intent.md` |

## 關鍵事實與數據

| 項目 | 內容 | 出處位置 |
|---|---|---|
| 階段數 | 6 個階段、13 個 play，**非線性**，各 play 標明 prerequisites | Plays 開頭 |
| 每個 play 的結構 | 改變什麼／如何開始／執行步驟／治理考量／怎麼量測（leading + lagging 各一） | Plays 開頭 |
| eval suite 規模 | **20 到 50** 個近期真實任務 | Continuous evals 步驟 1 |
| 平行 session | **2 到 3 個是合理起點**；實務上限是一個人審得完幾條流 | Parallel sessions 步驟 3 |
| 審查回合 | 三個 pass：Bugs、Security、Compliance（對 `spec.md`、`plan.md`、設計原則） | REVIEW.md 範例 |
| nit 上限 | 每次審查最多回報 **5 條** nit，其餘只給計數 | REVIEW.md 範例 |
| `CLAUDE.md` 長度 | **控制在一頁以內**，因為每個 session 開頭全讀，過期內容白佔脈絡 | CLAUDE.md 步驟 5 |
| `CLAUDE.md` 更新規則 | **同一個錯誤犯第二次，修正就寫進去** | CLAUDE.md 步驟 4 |
| 控制帶 | `rolling_30d` 基線，Western Electric 規則，1σ log／2σ diagnose／3σ propose | bands.yaml |
| 掃描頻率 | 積極開發中的服務**每週**掃一次是合理預設 | Recurring codebase scans 步驟 3 |
| Claude Security | 跑在 **Mythos 5** 上，每個發現先驗證再回報並附信心評分，按用量計費 | Recurring codebase scans |
| Claude Tag | Slack 公開測試中，Claude 以自己的身分成為頻道成員 | Claude on call |
| 全文數據 | **零**——沒有任何成效數字、對照組或案例量測 | 全文 |

## 三種 source of truth 的配置

既有的 Jira、需求工具、Figma、變更委員會不可能被取代，因為稽核與法規已經接受它們。
原文要求**每一種產物指定唯一一個系統當權威來源**，其餘只放副本或連結：

| 配置 | 誰是權威 | 適用 |
|---|---|---|
| repo 為準 | markdown 產物；舊系統引用 commit 內的檔案 | 工程主導的組織最乾淨，單一工具單一時間戳權威 |
| 舊系統為準 | Jira／ServiceNow／需求工具；markdown 是工作副本 | Claude 在同一個 session 裡透過 MCP 讀取與寫回 |
| 只做連結 | 兩個都是權威 | **轉型起步點**，接受雙來源 |

## 值得引用的原文

> "A skill is a control, though an advisory one. ... nothing forces a session to comply with it.
> A policy that must always hold needs something deterministic behind the skill."
>（Skills as institutional knowledge／Governance considerations）

> "Separation of duties is preserved, because **the agent that wrote the code has no way to
> approve it**."（AI in the PR review loop／Governance considerations）

> "...an agent fixing code must not be able to weaken the check on that code."
>（Give Claude a feedback loop 步驟 7）

> "Human attention concentrates at the gates, reviewing what the agent flagged rather than
> starting each stage from scratch."（Plays 開頭）

> "The loop keeps running. Human judgement stays above it."（Closing thoughts，全文最後一句）

## 兩個容易混掉的區分

**回饋迴圈 ≠ verifier 子 agent。** 回饋迴圈跑遍整個任務，跑幾次由工作量決定；
verifier 子 agent 是把最終檢查包起來，在 session 自認做完之後**開一個新的脈絡視窗**跑一次，
好讓判定不被產生程式碼的那組假設污染。

**build 期 hook ≠ deploy 期 hook。** 前者無人介入地允許或阻擋，必須快且只掃改動的那個檔案；
後者會**問人**、暫停動作等特定人核准。原文特別指出：把「要人核准」的 hook 放在 build 期，
等於把一個人放回**所有平行 session 的關鍵路徑**上。

## 對 wiki 的影響

- 新增概念：[[ai-native-sdlc]]、[[artifact-chain]]、[[intent-md]]、
  [[advisory-vs-deterministic-control]]、[[autonomy-tiering]]、[[agent-config-evals]]
- 更新：[[agent-skills]]（skill 不是控制，只是建議——這是對該頁的實質修正）、
  [[skill-design-patterns]]（Inversion 的「不可協商閘門」要由 hook 實現才成立）、
  [[agent-autonomy-cost]]（分級是「畫界線」的具體機制）、
  [[prompt-obsolescence]]（**Q11 的直接答案**：用 eval suite 回歸測試設定檔）、
  [[harness-engineering]]（harness 的作用範圍從 session 擴到組織；managed settings）、
  [[context-engineering]]（`CLAUDE.md` 一頁以內；產物鏈是刻意的動態脈絡）、
  [[design-is-the-new-code]]（產物鏈 vs 單一設計文件）、
  [[factory-model]]（**Q8 的新證據**：`plan.md` 要求列出每一個會改動的檔案）、
  [[can-judgment-be-outsourced]]（第五份來源：判斷力被搬到閘門上）、
  [[judgment]]、[[ai-development-economics]]（eval 與掃描是**經常性**成本）、
  [[vibe-coding-spectrum]]（原文的產物鏈是光譜紀律端的組織版）
- **矛盾**：與 [[design-is-the-new-code]] 對「唯一算數的產物」說法不同，見該頁

## 我的判讀

（推論）這是 Anthropic 自家 blog，賣點藏得不深——Claude Code、Cowork、Claude Design、
Claude Security、Claude Tag、Code Review、claude-code-action 全部在文內被點名，
而且 Claude Security 明講按用量計費、要開 Extra Usage 與付費席位。

但有兩點讓它比行銷文件可信：

1. **每個 play 的量測都綁在組織既有系統上**——git log 時間戳、PR metadata、CI check、
   OpenTelemetry export、incident tracker。全部可被否證，而且不需要買新工具才能量。
2. **它對自家機制講壞話**：skill 不強制、hook 才強制；managed settings 那段還特別寫
   「把上面當成起點來調整，不是照抄的建議，每一條 deny 都在拿能力去換」。

盲點也清楚：

- **全文沒有一個成效數字**。相較 [[the-new-sdlc-with-vibe-coding]] 至少並列了互斥的數據，
  這份是純框架，所有指標都是「你自己去量」。
- **預設組織已經有 git、CI、branch protection、metrics store、MDM**。
  沒有這些的團隊，這份 playbook 的起步成本被完全略過。
- **`published` 日期不可信**：原檔 frontmatter 寫 `2001-08-21`，是網頁擷取工具抓錯，
  `author` 欄空白。正文署名 Anthropic Applied AI team。內文提到 Claude Mythos 5 與
  Claude Tag 公開測試，本頁一律照抄不改。取得日 2026-08-29。
- **三張圖是 CDN 外連**，`Raw/assets/` 沒有存檔，本頁的摘要只根據圖說文字。

## 相關頁面

- [[ai-native-sdlc]] —— 全文的框架
- [[artifact-chain]] —— 貫穿六階段的那條線
- [[advisory-vs-deterministic-control]] —— 本文最有價值的一刀
- [[autonomy-tiering]] —— 自治的具體機制
- [[agent-config-evals]] —— 對 [[open-questions]] Q11 的直接回答
- [[the-new-sdlc-with-vibe-coding]] —— 同主題的另一份白皮書，帶數據但不談治理
- [[prompting-claude-opus-5]] —— 同一供應商，session 層級；這份是組織層級
