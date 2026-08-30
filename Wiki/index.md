---
title: 索引
type: synthesis
aliases: [index]
tags: [樞紐]
created: 2026-08-01
updated: 2026-08-30
status: active
confidence: high
sources: []
---

# 索引

> 全庫目錄。查詢時先讀這一頁找候選，再進去讀內文。每次 ingest 必須更新。
> 每筆格式：連結、破折號、一句話摘要，需要時在句末用「·」加附註。

## 樞紐

- [[overview]] — 全庫總覽與當前主軸
- [[log]] — 時序流水帳

## 來源（10）

- [[arm-yourself-with-specific-knowledge]] — Naval 2019：教不來但學得會的知識才有報酬
- [[read-what-you-love]] — Naval 2019：先讀你愛讀的，再往原典走；慾望比手段稀缺
- [[elephants-goldfish]] — Rensin 2026：Google 內部的 AI 開發實作報告，Design is the new code
- [[agent-skill-design-patterns]] — Google Cloud 2026：SKILL.md 的格式已解決，難的是內容設計的五種模式
- [[the-new-sdlc-with-vibe-coding]] — Google 白皮書 2026：51 頁，vibe coding 到 agentic engineering 的光譜 · **本庫唯一帶數據的來源**
- [[prompting-claude-opus-5]] — Anthropic 官方文件：哪些為前代調校的指令現在會反過來傷害你 · session 層級
- [[the-ai-native-sdlc-playbook]] — Anthropic 2026：六階段 13 個 play，把 SDLC 重建成迴圈 · **本庫唯一的組織治理來源**
- [[metr-early-2025-ai-developer-productivity]] — METR 2025：RCT 量到慢 19%（區間 +2% 到 +39%，顯著）· 本庫第一份實證研究，已被後續限定
- [[metr-2026-uplift-update]] — METR 2026：後續兩組區間都跨過 0，作者宣告自己的估計「很可能是糟糕的代理」· **一份宣告自己量不準的研究**
- [[ironies-of-automation-public-service]] — Lindgren 2024：把 Bainbridge 1983 的五個反諷套到公共服務自動化 · **本庫第一份跨領域來源；Q6 的答案 1983 年就寫好了**

## 實體（6）

- [[naval-ravikant]] — 提出「特定知識 + 責任 + 槓桿 + 判斷力」四件套
- [[dave-rensin]] — Google 工程主管，Elephant-Goldfish 模型的提出者 · seed
- [[addy-osmani]] — 工廠模型、指揮家與協調者、80% 問題的提出者 · seed
- [[shubham-saboo]] — 唯一橫跨兩份來源的作者 · seed
- [[claude-opus-5]] — 1M 脈絡、thinking 預設開；本庫第一個會自己做判斷的實體 · seed
- [[metr]] — 做 AI 評估的研究組織；本庫唯一沒有產品要賣的來源方 · seed

## 概念（31）

- [[specific-knowledge]] — 教不來但學得會；判準是「能被訓練的就能被量產」
- [[judgment]] — 兩份來源共同指認的、唯一不會貶值的能力
- [[leverage-and-compounding]] — 讓能力差距被放大的乘數 · seed，來源不足
- [[love-of-reading]] — 稀缺的是想學的慾望，不是學習的手段
- [[first-principles-foundation]] — 早期讀的東西會編程你的大腦，所以地基要打在原典
- [[elephant-goldfish-model]] — 餵大象、用金魚測試：AI 開發的四階段九步驟
- [[design-is-the-new-code]] — 程式碼將變得不透明，唯一還算數的產物是設計
- [[ai-as-interrogator]] — 別叫 AI 當研究員，叫它當拷問者：三段式提問法 · 即 Inversion 模式
- [[vibe-coding-spectrum]] — 不是二選一；判準只有一條：輸出怎麼被驗證
- [[context-engineering]] — 真正的技能：六種脈絡，以及靜態／動態的取捨
- [[harness-engineering]] — Agent = Model + Harness；多數 agent 失敗其實是設定失敗
- [[factory-model]] — 開發者的產出是產出程式碼的那套系統
- [[conductor-and-orchestrator]] — 與 AI 協作的兩種模式，一天內會流動
- [[the-80-percent-problem]] — 最後 20% 的錯誤是概念錯，因為看起來對所以更難抓
- [[ai-development-economics]] — vibe coding 低 CapEx 高 OpEx；脈絡工程是財務槓桿
- [[agent-skills]] — progressive disclosure：只為當下用到的能力付 token
- [[skill-design-patterns]] — Tool Wrapper / Generator / Reviewer / Inversion / Pipeline
- [[prompt-obsolescence]] — 規則檔會折舊：昨天的護欄是今天的成本
- [[agent-autonomy-cost]] — 失效模式從「做不到」變成「做太多」：過度驗證、範圍擴張、過度委派
- [[effort-and-thinking]] — effort 控制想多少，不是說多少；不要關 thinking
- [[ai-native-sdlc]] — 六階段從直線改成迴圈；瓶頸移到 build 左右兩側
- [[artifact-chain]] — intent→spec→plan→diff→PR→事故；commit chain 就是稽核軌跡
- [[intent-md]] — 用提案者自己的話寫的 proto-spec，非工程師也能寫
- [[advisory-vs-deterministic-control]] — skill 讓違規變罕見，hook 讓違規變幾乎不可能 · **本庫最有用的一刀**
- [[autonomy-tiering]] — 1σ 記錄／2σ 唯讀診斷／3σ 只能提議；偵測保持確定性
- [[agent-config-evals]] — 規則檔要像程式一樣被回歸測試 · Q11 的部分答案
- [[self-report-vs-measurement]] — 自認快 20%，實際慢 19%，差 39 個百分點 · **Q7 的解**
- [[evidence-types-for-ai-capability]] — benchmark 高估、自陳更高估、RCT 適用窄
- [[control-group-collapse]] — 工具好到受試者拒絕沒有它，RCT 就失效了 · **工具愈有價值愈難量測它的價值**
- [[monitoring-does-not-teach]] — 監控結構上不提供能力累積的條件，接手卻要求更高技能 · **Bainbridge 1983，直接反駁本庫的 H1**
- [[automation-fragmentation]] — 留給人的不是更高階的工作，可能只是機器做不到的碎片集合

## 綜合（4）

- [[can-judgment-be-outsourced]] — Naval 說判斷力教不來，Rensin 的方法卻在把它寫成文件 · 本庫核心矛盾
- [[what-the-19-percent-measures]] — METR 的結果對本庫既是支持也是削弱 · **更正了本庫對該數字四週的誤讀**
- [[two-sdlc-frameworks]] — Google 與 Anthropic 兩份 SDLC 框架的逐項比較 · 六階段幾乎逐格對應，但一份問「你怎麼工作」、一份問「一個變更怎麼走」
- [[judgment-supply]] — Q6：判斷力從哪長出來 · **場域不是被 agent 拿走的，是人自己不回去**；`confidence: low`，沒有來源直接談這題

## 問題（1）

- [[open-questions]] — 16 個開放問題 · **7 條已結案；Q6 的 H1 已被 1983 年的論證反駁，Q15（harness 能不能翻轉 19%）是剩下最大的缺口**
