---
title: Elephants, Goldfish and the New Golden Age of Software Engineering
type: source
aliases: [大象與金魚, Elephant-Goldfish]
tags: [ai, 軟體工程, 工作方法]
created: 2026-08-01
updated: 2026-08-01
status: active
confidence: high
source_type: article
author: Dave Rensin
published: 2026-04-28
url: https://drensin.medium.com/elephants-goldfish-and-the-new-golden-age-of-software-engineering-c33641a48874
raw: "[[2026-08-01--elephants-goldfish-golden-age]]"
ingested: 2026-08-01
---

# Elephants, Goldfish and the New Golden Age of Software Engineering

> [[dave-rensin|Rensin]] 在 Google 帶團隊用 AI 寫程式一年後的實作報告：
> 多數人把 AI 當研究員用（錯），該當**拷問者**用；程式碼會變得不透明，
> 唯一還讀得懂的產物是設計文件。

## 三個部分

### Part 1：三段式提問法（[[ai-as-interrogator]]）

1. **準備**：不要叫它「幫我研究」，要叫它「一直問我問題直到我喊停」。花 15–20 分鐘被拷問，
   一段話會長成 2–3 頁。跟它吵架，但**是為了學而吵，不是為了贏而吵**。
2. **驗收標準**：叫它扮演「懷疑論的事實查核者」，跟你討論一份好報告該長什麼樣。再 15–20 分鐘，
   得到 2–3 頁的評分標準。
3. **開新 session**跑深度研究，同時餵進問題描述與驗收標準。

破除諂媚迴圈的固定句：「你同意我的時候你沒在幫我。你最有用的時候是挑戰我的想法。」

### Part 2：Elephant-Goldfish 模型（[[elephant-goldfish-model]]）

三個 aha：
1. 模型 crash 之後重建脈絡極貴 → 早該維護一份寫清楚意圖與進度的文件。
2. 模型急於討好，沒有嚴格護欄就會衝下懸崖。
3. **sizeof(docs) << sizeof(code)** —— 餵設計文件比餵原始碼便宜、快、可靠。

以及 [[design-is-the-new-code|Design is the new code]]：人不再做那些微決策，
若不強迫決策「左移」進設計文件，系統對負責的人就是不可理解的。

**啟動既有 monolith 的方法**：從葉節點目錄開始讓 AI 產 README.md（葉節點約 50% 是錯的，
工程師花 5–10 分鐘修），再逐層往上 roll up。約一週可完成，之後開新 session 只餵 README 樹。

### Part 3：預測

- **我們都是管理者了**：IC 與 people manager 的界線今年就會模糊。建議 IC 現在就去上基礎管理課，
  並從同時管 3–5 個 agent 開始練。好管理的指標是「你能移開視線多久，回來時東西還是好的」。
- **持續專注是需要練的肌肉**：從每天 30–45 分鐘開始，每週加 5–10 分鐘。
- **Jevons 悖論**：工具讓工作變簡單，人不會工作變少，只會做更多。

## 值得引用的原文

> "If we aren't careful, we aren't just writing code faster. We are mass-producing our mistakes."

> "Do not make the mistake of outsourcing your judgment to the machine."

> "The job is intent. The job is architecture. The job is design judgment."

## 關鍵數據

| 項目 | 內容 |
|---|---|
| 起點 | 2025 年夏天為自己的問題寫的小工具 |
| 規模 | 數月內超過 100,000 名 Googler 常態使用 |
| 工具 | Google Antigravity + Gemini |
| Goldfish 批評者的命中率 | 約 30% 的建議「高度有價值」 |
| 非工程師寫的設計文件品質 | 初稿約 70–80% 正確，一兩輪後達標 |

## 對 wiki 的影響

- 新增：[[elephant-goldfish-model]]、[[design-is-the-new-code]]、[[ai-as-interrogator]]、[[dave-rensin]]
- 與 [[arm-yourself-with-specific-knowledge]] 在 [[judgment|判斷力]] 上正面交會 → [[can-judgment-be-outsourced]]

## 我的判讀

（推論）作者自己在開頭就要求讀者「帶著健康的懷疑」，並說一年後這些話可能就過時了——這點誠實。
最硬的部分是 Part 1 與 Part 2 的操作細節，都是可以今天照做的。
最弱的是「一週搞定 monolith」：他承認葉節點 50% 錯誤要人工修，卻沒算這在百萬行等級的人力總量。
Part 3 的預測價值低於它的框架價值。

## 相關頁面

- [[elephant-goldfish-model]] —— 本文的核心框架
- [[design-is-the-new-code]] —— 本文最強的一句主張
- [[ai-as-interrogator]] —— Part 1 的方法
- [[dave-rensin]] —— 作者
- [[can-judgment-be-outsourced]] —— 由本文延伸的對撞
