---
title: "AI Engineering Skills Map: Software engineering fundamentals"
type: source
aliases: [AI Engineering Skills Map, Ng 技能地圖, 軟體工程基本功]
tags: [ai, 軟體工程, 能力]
created: 2026-09-01
updated: 2026-09-01
status: active
confidence: medium
source_type: article
author: Andrew Ng
published: unknown
url: https://x.com/andrewyng/status/2093388974194872781
raw: "[[2026-09-01--ai-engineering-skills-map-software-fundamentals]]"
ingested: 2026-09-01
---

# AI Engineering Skills Map: Software engineering fundamentals

> [[andrew-ng|Ng]] 的技能地圖系列之一：agentic coding 之後，軟體工程基本功不但沒過時，
> 反而變成**能不能操縱 agent** 的前提——因為不知道有哪些取捨存在的人，無從指定要哪一種。

## 核心主張

- 就算所有程式碼都由 coding agent 寫，懂軟體基本功仍然重要，
  因為那決定你**能不能把 agent 導向你要的取捨**。
- 不懂基本功的新手 vibe code 出來的東西，agent 會在
  latency、availability、consistency、reliability、maintainability、simplicity、cost
  上做出壞的取捨。**失敗的原因不是指令下得差，是不知道有這些取捨可下。**
- 最重要的五塊技能：全端、資料管理、系統架構、安全與可靠、規模化與維運。
- 資料值得特別對待，因為它是軟體蓋在上面的地基，而且**相對難改**（即使 agent 能幫忙做遷移）。
- 架構是**移動的標的**：做原型的簡單架構不會是第一版生產系統的正確架構，
  那一版也不會是規模化之後的正確架構。
- 「shift left」——安全工作往生命週期前段移，**很多開發者現在也部分是資安工程師**。
- 背語法這類知識正在過時，但深懂軟體如何運作的人「vastly outperform」不懂就 vibe code 的人。

## 五塊技能各自包含什麼

| 技能塊 | 原文列舉的內容 |
|---|---|
| Building full-stack applications | UI 元件、快取、頁面渲染、API 選型與設計、認證、狀態與 session 管理、非同步處理、資料持久化、測試、安全、無障礙 |
| Managing data | 存取模式、資料模型、儲存型別（relational / document / key-value / graph）、交易、並行、乾淨一致新鮮、隱私與治理與法遵、資料生命週期 |
| Designing system architectures | 應用平台、前後端界線、系統分解、應用狀態放哪、架構粒度（monolith vs microservices）、技術棧選型（有時先做實驗再定案） |
| Making systems secure and reliable | 單元測試與整合測試的比例、框架、覆蓋率、失敗處理（如 API 撞到 rate limit）、graceful degradation、縮小 blast radius、shift left |
| Scaling and operating in production | 部署環境設定、發布策略、CI/CD、IaaS、可觀測性、告警、事故管理、擴容與負載平衡、sharding／indexing／replication、版控、程式碼審查、相依維護、技術債 |

## 關鍵事實與數據

**沒有。全篇零數字、零日期、零外部引用。**唯一提到的依據是一句
"our study of AI Engineering Skills shows"——那份研究沒有連結、沒有方法、沒有樣本數。
這件事對本庫很重要，見下方〈我的判讀〉與 [[evidence-types-for-ai-capability]]。

## 值得引用的原文

主張的核心（第二段）：

> "A novice who vibe codes without understanding software fundamentals can create simple
> applications, but this often leads to the coding agent making bad tradeoffs in latency,
> availability, consistency, reliability, maintainability, simplicity, and/or cost. In such
> cases, **the developer didn’t know such tradeoffs even existed and therefore did not steer
> the agent to make the right decisions for their application context**."

資料架構那段（Managing data）——本篇對本庫最有價值的一句：

> "Deciding how to manage data requires significant human-provided context. **Your AI systems
> will get their own input context from your data source, so if data architecture is chosen
> poorly, the AI doesn’t know what it doesn’t know.**"

同段還有一句把「best practice 本身會移動」講明：

> "How to build data infrastructure for agents — rather than only traditional software or
> humans — is also a rapidly evolving area, and you should continue to adjust your best
> practices as the field evolves."

角色擴張：

> "Agentic coding enables many developers who previously played more specialized roles
> (like front-end developer or mobile developer) to play a broader, full-stack role."

收尾（最後第三段）：

> "Some parts of coding knowledge — like **memorizing coding syntax** — are becoming obsolete.
> But developers who **deeply understand how software works vastly outperform** those who vibe
> code without understanding."

## 對 wiki 的影響

- 新增：[[andrew-ng]]（seed）、[[tradeoff-literacy]]
- 更新：[[context-engineering]] —— 把脈絡的上限往上游推到**資料模型層**，本庫原本只談到提示與檔案層
- 更新：[[the-80-percent-problem]] —— 補上它的上游版本：錯誤不只出在 AI 的輸出，也出在人給的方向
- 更新：[[vibe-coding-spectrum]] —— 光譜講「怎麼做」，這份補上「該懂什麼」這個先決條件
- 更新：[[specific-knowledge]] —— 「背語法過時」是可訓練邊界外移的一個具體事例
- 更新：[[judgment-supply]]、[[open-questions]] Q6 —— 它**要求**這種理解卻不談它從哪來
- 衝突：無直接矛盾。與 [[monitoring-does-not-teach]] 之間是**張力**而不是矛盾，見下。

## 它和 Bainbridge 的張力

本篇要求開發者「deeply understand how software works」，才有資格 steer agent。
[[monitoring-does-not-teach]]（Bainbridge 1983）主張的是：
自動化之後留給人的監控位置**結構上不提供**取得或維持那種理解的條件。

兩邊沒有互相否認，因為 Ng 通篇**沒有談這種理解從哪裡累積**。
（推論）他預設了供給。這正是 [[open-questions]] Q6 的形狀，
所以這份來源讓 Q6 更尖銳，而不是回答它。

## 我的判讀

（推論）這是本庫收錄過**證據等級最低**的來源，理由有三：

1. **零證據**。唯一的依據是「our study of AI Engineering Skills shows」，
   那份研究沒公開、沒方法、沒數字。按 [[evidence-types-for-ai-capability]] 的尺，
   這連「敘事與框架」都算保守——它是**敘事加上一份不可查證的內部研究的權威背書**。
2. **賣方立場**。這是技能地圖系列的一篇，而技能地圖的商業形式是課程。
   本篇的結論（「你需要學這五塊」）與作者的產品方向完全一致。
3. **不可否證**。「懂基本功的人表現遠勝不懂的人」沒有給出任何會讓它為假的觀察。

所以 `confidence` 設 `medium` 而不是本庫其他來源頁慣用的 `high`：
摘要本身忠於原文，但這份來源的主張沒有任何東西撐著。
**它的價值在於提出了一個本庫沒有的軸線（該懂什麼），不在於證明了什麼。**

## 原檔的缺漏

原檔開頭引用了一張技能地圖圖片（`pbs.twimg.com` 的外部連結），
**該圖沒有被抓下來，本庫沒有它的內容**。所以上表的五塊技能是依內文段落標題整理的，
圖裡若還有內文沒提到的結構，本庫看不到。

原檔的 frontmatter 也沒有 `published`，X 貼文本身的日期未取得，故記為 `unknown`。

## 相關頁面

- [[andrew-ng]] —— 作者
- [[tradeoff-literacy]] —— 本篇的核心概念
- [[the-80-percent-problem]] —— 同一個失敗的另一端
- [[context-engineering]] —— 被本篇往資料層推的那條
- [[vibe-coding-spectrum]] —— 本篇補上的是它的先決條件
- [[evidence-types-for-ai-capability]] —— 判定本篇證據等級的那把尺
- [[monitoring-does-not-teach]] —— 與本篇的張力所在
- [[open-questions]] —— Q6 因這份來源更尖銳
