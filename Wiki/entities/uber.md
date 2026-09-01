---
title: Uber
type: entity
aliases: [Uber Engineering, UberEng]
tags: [組織, ai, agent, 成本]
created: 2026-09-01
updated: 2026-09-01
status: seed
confidence: medium
sources: ["[[running-a-software-factory-at-uber-scale]]"]
---

# Uber

> 本庫**第一個買方視角**的來源方——它不賣 agent 工具，它付錢買，
> 而且公開了自己怎麼把單位成本壓下來的方法與數字。

## 基本資料

| 項目 | 內容 |
|---|---|
| 類別 | 組織（採用方） |
| 本庫收錄 | [[running-a-software-factory-at-uber-scale]]（2026-08-29） |
| 規模訊號 | 70%+ 的 PR 由 agent 產出、3,600+ 個 agent skill、每日 30K+ 次 skill 執行 |

## 它為什麼在本庫裡重要

`[[overview]]` 的缺口清單長期掛著一句：**治理那一軸只有一份來源，而且是賣方的**，
`[[open-questions]]` Q6 的「還缺什麼」第 2 項也是「買方或監管方視角的組織來源」。
Uber 是第一個。

方向偏誤與賣方相反：賣方要證明 agent 有價值，Uber 要證明**同樣的價值可以更便宜**。
它公布的每一個槓桿都在減少 token 消耗，包括**把自家供應商的 MCP schema 趕出脈絡**
（[[context-tax]]）。

## 它的方法學自覺

原文有一句本庫先前沒有任何來源講過的話：

> "isolating our own optimization gains means **holding one model fixed**, since behavior shifts
> with every upgrade and model family."

（推論）這是 [[prompt-obsolescence]] 的營運版：不只規則檔會折舊，**量測基準也會**，
因為被量的那個東西每幾週就換一次。METR 在 [[control-group-collapse|對照組崩解]]
碰到的是同一類問題的另一面。

## 它的偏誤

（推論）這是工程部落格，目的包含展示能力與招募：

- **自陳、未經稽核**，通篇沒有一個失敗的槓桿。
- **成功的定義是成本，不是品質**。原文說「improving/maintaining output quality」，
  但沒有給任何全公司層級的品質數字。
- **規模極端**，很多槓桿在小團隊不成立。

## 相關頁面

- [[running-a-software-factory-at-uber-scale]] —— 本庫收錄的唯一一篇
- [[context-tax]] —— 它量出來的工具 schema 開銷
- [[managed-agents]] —— 它的結論方向
- [[metr]] —— 另一個沒有產品要賣的來源方，但立場不同：研究方 vs 採用方
- [[overview]] —— 本庫來源獨立性的分布
