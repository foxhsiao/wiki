---
title: AI 能力的三種證據
type: concept
aliases: [evidence types, benchmark vs RCT, 證據層級]
tags: [ai, 方法學, 評估]
created: 2026-08-29
updated: 2026-08-30
status: active
confidence: medium
sources: ["[[metr-early-2025-ai-developer-productivity]]", "[[metr-2026-uplift-update]]"]
---

# AI 能力的三種證據

> benchmark、RCT、軼事自陳三者對「AI 有多強」給出**部分互相矛盾**的答案。
> 重點不是哪個對，是**每一種的偏誤方向不同**。

## 三種各自怎麼錯

[[metr-early-2025-ai-developer-productivity]] 的討論段整理出這組對照：

| 證據 | 偏誤方向 | 原文理由 |
|---|---|---|
| **Benchmark** | 傾向**高估** | 只量「範圍界定良好、可用演算法評分」的任務 |
| Benchmark | 也可能**低估** | 沒有真人互動，模型可能因為人類隨手會修的小卡點而失敗 |
| **軼事自陳** | 傾向**高估** | 「已有強證據顯示自陳的加速估計可能非常不準」（見 [[self-report-vs-measurement]]） |
| **RCT** | 適用範圍窄 | 只涵蓋受試者實際的用法；不涵蓋「對每個問題抽樣數百上千條軌跡」的用法 |

## 它們可能在問不同的問題

原文明說調和困難，而且**部分差異是合理的**，不全是誤差：

> 我們同時關心兩件事——**最大化引出**（對每個問題抽樣上百萬 token、數十上百次嘗試）
> 的模型能力，以及**標準／常見用法**下的模型能力。

也就是說 benchmark 測的是能力上限，RCT 測的是**當前實務下的實際交付**。
兩者都對，只是別互相冒充。

## RCT 那一格的限制，從「適用範圍窄」變成「可能跑不動」

本頁原本記 RCT 的問題是**適用範圍窄**——只涵蓋受試者實際的用法。
[[metr-2026-uplift-update]] 加上了更嚴重的一條：**這種設計可能招不到人、收不到代表性的任務**。

當工具好用到受試者拒絕在沒有它的條件下工作，隨機化就失去意義。
30–50% 的開發者承認會避開「AI 增益高」的任務，有一位在被禁止用 AI 的組別裡一個任務都沒完成。
展開見 [[control-group-collapse]]。

這讓三種證據的處境變成：

| 證據 | 狀態 |
|---|---|
| Benchmark | 傾向高估，但**還跑得動** |
| 自陳 | 已知不可靠，但**還跑得動**，而且正在被迫重新啟用 |
| **RCT** | 偏誤最小，但**在這個題目上正在失去可行性** |

（推論）最不偏誤的方法最先失效，這個順序很糟：
剩下的兩種都偏向高估，而且沒有第三方可以校準它們。

## 對本庫的意義

（推論）本庫收錄的八份來源裡，**七份的證據等級是軼事或框架**，
而這一頁指出軼事自陳是三種裡最不可靠的一種。

這不代表那七份沒有價值——框架的用途是組織思考，不是證明因果。
但它確實意味著：本庫任何「AI 讓 X 提升 Y%」形式的主張，
只要出處是自陳調查，都該標記出來而不是當成事實。

它同時對 [[harness-engineering]] 造成麻煩：那一頁最硬的兩個證據
（Terminal Bench 只改 harness 進 Top 5、LangChain +13.7 分）**都是 benchmark**，
而這一頁說 benchmark 傾向高估、且難以直接翻譯成真實世界的影響。
展開見 [[what-the-19-percent-measures]]。

## 相關頁面

- [[metr-early-2025-ai-developer-productivity]] —— 來源
- [[self-report-vs-measurement]] —— 自陳那一格的具體資料
- [[harness-engineering]] —— 證據基礎被這一頁削弱的對象
- [[what-the-19-percent-measures]] —— 三種證據在本庫的實際對撞
- [[metr-2026-uplift-update]] —— RCT 失去可行性的紀錄
- [[control-group-collapse]] —— 失效的機制
