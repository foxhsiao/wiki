---
title: METR
type: entity
aliases: [Model Evaluation and Threat Research]
tags: [ai, 組織, 評估, 研究]
created: 2026-08-29
updated: 2026-08-30
status: seed
confidence: medium
sources: ["[[metr-early-2025-ai-developer-productivity]]", "[[metr-2026-uplift-update]]"]
---

# METR

> 做 AI 能力評估的研究組織。本庫唯一一個**產出實證資料**而非框架的來源方。

## 基本資料

| 項目 | 內容 |
|---|---|
| 類別 | 研究組織 |
| 本庫收錄 | [[metr-early-2025-ai-developer-productivity]]（2025-07-10）、[[metr-2026-uplift-update]]（2026-02-24） |
| 已知後續 | [[metr-2026-uplift-update]]（2026-02-24），**已 ingest** |

## 它為什麼做這個研究

原文寫得很直接：關心 **AI 對 AI 研發本身的影響**，因為極快的 AI 進展可能導致監督與防護機制失效。
量測 AI 對開發者生產力的影響，是用來補 benchmark 不足的旁證。

也就是說，這份研究的動機不是「AI 對工程師好不好用」，是**AI 安全**。
（推論）這解釋了它的方法學為什麼這麼保守——低估比高估安全。

## 它對自己的研究有多不客氣

兩份研究連起來看，METR 的行為模式很一致：

- 2025 那份主動列出 20 個替代解釋、公布其中 6 個被自己的資料排除、用整張表寫「我們不提供證據支持什麼」
- 結果過期後在原文**頁首掛橫幅**，而不是靜靜留著
- 2026 那份直接說自己的中央估計值「**很可能是真實生產力影響的糟糕代理**」，
  並公開六個方法學問題與三段對自己不利的受訪者引言
- 兩份研究的**完整資料集都公開在 GitHub**

（推論）本庫收錄的八份來源裡，沒有第二份會這樣對待自己的結論。
這是把它的 `confidence` 撐起來的主要理由——不是因為它結論可靠，
是因為**它對自己結論的不可靠說得最清楚**。

## 與本庫的關聯

本庫的其他七份來源全部出自供應商或從業者，而且都有利益方向：
三份來自 Google 或其員工、兩份來自 Anthropic、兩篇來自 [[naval-ravikant|Naval]]。
METR 是第一個**沒有產品要賣**的來源方，這讓它在
[[what-the-19-percent-measures]] 那條對撞裡份量不同。

但它也不是沒有立場：它的組織動機是 AI 風險評估，
（推論）這個方向會讓它對「AI 能力被高估」的證據更敏感。

## 它現在的處境

[[control-group-collapse|對照組崩解]]讓 METR 的招牌方法在這個題目上快走不動了。
它列出的六條替代路徑裡，有一條是回頭用**問卷**——
也就是它自己在 2025 年證明「可能相當不可靠」的那種證據。

## 相關頁面

- [[metr-early-2025-ai-developer-productivity]] —— 本庫收錄的研究
- [[evidence-types-for-ai-capability]] —— 它主張的證據層級
- [[what-the-19-percent-measures]] —— 它的結果在本庫引發的對撞
- [[open-questions]] —— Q7 待補的 2026 更新
- [[metr-2026-uplift-update]] —— 第二份收錄的研究
- [[control-group-collapse]] —— 它現在面對的方法學困境
