---
title: 總覽
type: synthesis
aliases: [overview]
tags: [樞紐]
created: 2026-08-01
updated: 2026-08-29
status: active
confidence: medium
sources: ["[[arm-yourself-with-specific-knowledge]]", "[[read-what-you-love]]", "[[elephants-goldfish]]", "[[agent-skill-design-patterns]]", "[[the-new-sdlc-with-vibe-coding]]", "[[prompting-claude-opus-5]]", "[[the-ai-native-sdlc-playbook]]"]
---

# 總覽

> 這個知識庫在累積什麼、目前的整體判斷是什麼。每次 ingest 後若有實質變動就更新這一頁。

## 這個庫在做什麼

累積多主題的個人知識。原始來源放 `Raw/`，由 LLM 讀完後寫成互相連結的 wiki 頁面放 `Wiki/`。
規則寫在根目錄的 `CLAUDE.md`。

**分工**：使用者負責找來源、提問、判斷方向；LLM 負責閱讀、萃取、歸檔、交叉引用、維持一致性。

## 目前的主軸

七份來源全部收斂到同一個問題：**在機器能做掉實作之後，人還剩下什麼，以及那個東西怎麼運作。**

### 1. 判斷力是共同答案（5 份來源，跨 7 年）—— 本庫收斂度最高的一條

[[naval-ravikant|Naval]]（2019）、[[dave-rensin|Rensin]]（2026-04）、
[[addy-osmani|Osmani]] 等（2026-05）從完全不同的方向出發，都指向 [[judgment|判斷力]]。
白皮書的收尾句最直接：**「Generation is solved. Verification, judgment, and direction
are the new craft.」**——並把它變成人事建議：依判斷力而非實作能力招募。

### 2. 但它能不能被寫下來交給機器（本庫核心矛盾，已有數據）

Rensin 說「不要把判斷力外包給機器」，可是他的整套方法就是把判斷寫進文件交給 agent 執行。
若判斷力寫得下來，它就通過了 Naval 的「可訓練即可量產」判準，於是會貶值。

白皮書沒有解決這個矛盾，但**畫出了界線**：架構是「最頑固的人類環節」，
AI 擅長的是決策做成之後的實作。並第一次提供了數據站在「無法外包」那側——
[[the-80-percent-problem|80% 問題]]與 METR 的「資深開發者反而慢 19%」。
三種解法與各自的證據見 [[can-judgment-be-outsourced]]。

**第四份來源換了說話的人**：[[prompting-claude-opus-5]] 是供應商在描述**模型的判斷**——
「模型會對任務應該是什麼行使自己的判斷」。它被寫進文件是因為它是要被約束的問題，
不是賣點，但這句話讓「判斷力是人類專屬」站不住了。
自我驗證、範圍判斷、自主委派這三層都在被吃掉（[[agent-autonomy-cost]]）。

**第五份來源給了它一個位置**：[[the-ai-native-sdlc-playbook]] 不辯論判斷力是什麼，
它直接**設計判斷力放在哪**——六個閘門（接受 `intent.md`、簽核 `spec.md`、核准 `plan.md`、
PR 核准、生產發布授權、事故分流），而且用 branch protection 與 hook 把人強制留在那些點上。
「寫程式的 agent 沒有辦法核准自己的程式碼。」

但它同時把政策本身寫成 skill 交出去了，
而且（推論）**閘門上的判斷是審查別人做完的東西，不是從頭做模式比對**——
這讓 Q6 更尖銳而不是更緩和。

**新的裂縫（兩條）**：

1. 如果判斷力持續上移，新的判斷力要從哪裡長出來？七份來源共同的盲點 → [[open-questions]] Q6。
2. **界線移動得比框架快**：談 AI 的六份來源只橫跨六個月，
   但 [[elephants-goldfish]]（4 月）建議的部分做法已被 8 月的官方文件列為該刪的東西。
   如果界線每幾個月移動一次，「哪些判斷屬於人」可能沒有穩定答案，只有適應速度。

### 3. 什麼東西教不來（2 份來源）

[[specific-knowledge|特定知識]]的判準是反向的：能被訓練的就能被量產。
辨識訊號是「對你像玩、對別人像工作」。它的燃料是好奇心，
而好奇心不是被培養的，是[[love-of-reading|沒被弄丟]]的；
地基要打在能自己推導的東西上（[[first-principles-foundation]]）。

### 4. 規則檔會折舊（2 份來源）

[[prompt-obsolescence]]：為某個模型版本寫的護欄，在下個版本可能變成成本來源。
[[prompting-claude-opus-5]] 整份文件都在叫你**刪東西**——過度驗證指令、
「再檢查一次」、為前代調的 workaround、沿用的 effort 預設值。

這條**直接挑戰**其他來源的一個共同假設：
[[harness-engineering]] 說 harness 是「建一次、精煉很多次」的共享資產、
[[ai-development-economics]] 把它算成一次性 CapEx、
[[elephant-goldfish-model]] 說設計文件「是你新的原始碼」——
**沒有一份處理版本升級時的折舊**。如果每次換代都要重驗整套規則檔，經濟模型要重算（Q11）。

**第二份來源給了做法**：[[the-ai-native-sdlc-playbook]] 說操控 agent 的設定檔
（`CLAUDE.md`、skills、hooks）值得程式碼享有的那種回歸測試——
20–50 個真實任務組成 eval suite，設定一改就在 CI 跑，通過率掉了擋 merge
（[[agent-config-evals]]）。這解決**偵測**，沒解決**定位**（哪一條在扣分），
所以 Q10 還在；而且它讓 harness 從一次性 CapEx 變成 **CapEx 加持續 OpEx**。

### 5. 治理是本庫原本完全空白的一軸（1 份來源，新主軸）

前六份來源談的都是**個人或小團隊**怎麼跟 AI 工作。
[[the-ai-native-sdlc-playbook]] 是第一份談**受監管的組織**怎麼做的，
它帶進三樣本庫原本沒有的東西：

1. **[[artifact-chain|產物鏈]]**：`intent.md` → `spec.md` → `plan.md` → diff 與測試 →
   PR 與審查發現 → 事故紀錄，每階段以 commit 收尾、下一階段讀它開始。
   **commit chain 本身就是稽核軌跡**，不必另建一套稽核系統。
2. **[[advisory-vs-deterministic-control|建議型控制 vs 確定型控制]]**：
   skill 讓違規變罕見，hook 讓違規變幾乎不可能。這是本庫收到過最有用的一刀，
   因為它修正了 [[agent-skills]]、[[skill-design-patterns]] 對 skill 的定位——
   **skill 是制度知識的散布機制，不是控制**。
3. **[[autonomy-tiering|自治分級]]**：偵測保持確定性（統計，不含模型），
   模型只在越界後被叫進來，而且訊號強度決定它拿得到哪些工具。
   最高等級也只是「開 PR 進審查閘門」。

原則一句話：**agent 可以做到 production gate 為止，過不了那道門。**

### 6. 已經可以直接照做的操作（5 份來源）

這是庫裡不需要再驗證就能今天動手的部分：

- [[vibe-coding-spectrum]] —— 先決定這個任務該落在光譜哪裡（判準只有一條：輸出怎麼被驗證）
- [[harness-engineering]] —— agent 出錯時先查設定不要先怪模型；規則檔、工具、沙箱、hooks、可觀測性
- [[context-engineering]] —— 靜態 vs 動態脈絡是一級架構決策，也是成本決策
- [[ai-as-interrogator]] / [[skill-design-patterns]] —— 三段式提問法；五種 skill 模式
- [[elephant-goldfish-model]] —— 四階段九步驟，含金魚測試
- [[agent-autonomy-cost]] —— 畫界線而不是禁止；那段範圍約束句可以直接抄
- [[effort-and-thinking]] —— 用低 effort 控成本，不要關 thinking
- [[advisory-vs-deterministic-control]] —— 分清楚哪些規則是建議、哪些需要確定性的東西墊底
- [[intent-md]] —— 讓非工程師也能提出可執行的提案
- [[agent-config-evals]] —— 規則檔改動要有回歸測試

### 7. 這個庫在照鏡子

四個概念直接指向本庫自己的設計：`CLAUDE.md` 是白皮書定義的**靜態脈絡**與
[[harness-engineering|harness 規則檔]]；`Wiki/index.md` 是 progressive disclosure 的手工版；
`tools/lint.py` 是確定性 guardrail；ingest 流程混用了
[[skill-design-patterns|Pipeline、Generator、Reviewer]] 三種模式，
原本認為缺的是 **Inversion** 硬閘門——[[prompting-claude-opus-5]] 給了相反方向的建議
（例行判斷讓模型自己做），Q9 一度因此擱置，後來被第七份來源改寫成「閘門該寫在哪裡」。
**現在 `tools/lint.py` 已有兩道確定性閘門**：規則來由缺漏、以及 `confidence` 與來源數不符。
反而 `CLAUDE.md` 沒有記錄**每條規則為什麼存在**，這在折舊問題下是實際的缺陷（Q10）。

**第七份來源給了三面新鏡子**：

- `CLAUDE.md` 建議控制在**一頁以內**（session 開頭全讀，過期內容白佔脈絡）。
  **已照做**（2026-08-29）：204 行壓到 76 行，細節搬進 `.claude/skills/`。
  代價是那些規則的執行力從常駐降成按需觸發（[[advisory-vs-deterministic-control]]）。
- Q9 被改寫了：問題不是「該不該加 Inversion 閘門」，是**閘門寫在哪裡**。
  寫在 `CLAUDE.md` 裡的是建議，`tools/lint.py` 才是確定性的閘門。
  已據此加了兩道：規則來由缺漏、`confidence` 與來源數不符。
  候選的下一條：ingest 完成前強制 lint 通過。
- Q13 是本庫自己的量測問題：**lint 全綠不代表 wiki 健康**，
  只代表機械性檢查沒抓到東西。「趨近於零」的指標，成功與停止量測長得一樣。

**Q10 已結案（2026-08-29）**：`CLAUDE.md` 每條規則加了穩定編號，來由記進 `.claude/rules-ledger.md`。
但證據狀況比預期差——**26 條規則裡只有 1 條的來由是有紀錄的**，其餘全是推論或未知，
因為建庫時沒記、而且這個 repo 不是 git repo。
教訓很直接：**來由要在寫規則的當下記，事後補不回來。**
改用「這條規則實際被觸發過嗎」當替代指標後跑出四個發現，最硬的一條是
**`query` 流程從未被執行過**（log 8 筆全是 ingest 與 lint），W3、W4 兩條規則從未被驗證。

## 目前的缺口

- **來源獨立性更差了**：七份裡三份出自 Google 或 Google 員工、**兩份出自 Anthropic**，
  全都在 2026 年、都有利益方向。談 AI 的五份來源只出自兩家公司。
- Naval 的兩篇都在 AI 普及之前（2019）。他 2026 年的說法是最大的缺口（Q1）。
- 除了白皮書，其餘五份來源都沒有資料，全是敘事與框架。
  最新這份 playbook 通篇沒有一個成效數字，所有指標都是「你自己去量」。
- [[leverage-and-compounding]] 仍是 seed，撐著主軸 3 的關鍵一步。
- **治理那一軸目前只有一份來源，而且是賣方的**。需要一份買方或監管方視角的來源來對撞。
- 十四個開放問題見 [[open-questions]]，Q10 已結案。
  **下一份最該找的來源仍是 METR 那份原始研究（Q7）。**
  另外 Q12、Q13、Q14 不需要新來源，動手就能推進。

## 統計

| 項目 | 數量 |
|---|---|
| 來源 | 7 |
| Wiki 頁面 | 43 |
| 開放問題 | 14（1 條 closed） |
| 已標記的矛盾 | 5（[[can-judgment-be-outsourced]]、[[the-80-percent-problem]] 的數據衝突、[[design-is-the-new-code]] 的判準 vs 清單、[[prompt-obsolescence]] 對 harness 是純資產的挑戰、[[design-is-the-new-code]] 的「唯一算數的產物是哪一個」） |
