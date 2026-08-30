---
title: 監控學不到東西
type: concept
aliases: [monitoring does not teach, 監控的反諷, irony of monitoring]
tags: [自動化, 能力, 技能維持, 人因工程]
created: 2026-08-30
updated: 2026-08-30
status: active
confidence: medium
sources: ["[[ironies-of-automation-public-service]]"]
---

# 監控學不到東西

> 自動化把人的工作換成**監控**與**接手**。
> 但監控**沒有機會取得或維持**履行那個責任所需的能力——
> 而接手需要的技能比自動化之前**更高**。
> 這是 Bainbridge 1983 年寫下的，不是 AI 時代的新發現。

## 兩句原文

監控（Bainbridge 1983, p.776，經 [[ironies-of-automation-public-service|Lindgren]] 轉引）：

> "one of the worst types [of tasks]; it is very boring but very responsible,
> yet **there is no opportunity to acquire or maintain the qualities required to
> handle the responsibility**."

接手（同上，p.775）：

> "… when manual take-over is needed there is likely to be something wrong in the process,
> so that unusual actions will be needed to control it, and one can argue that
> **the operator needs to be more rather than less skilled**"

兩句合起來是一個夾擊：**日常工作不再產生能力，而偶爾需要的那次要求更高的能力。**

## 為什麼監控學不到

原文給的機制有兩個：

- **速度**——即時監控超出人的認知限制。所以實務上常再裝一套自動警報系統來監控自動系統。
- **黑箱**——看得到輸出，看不到過程。

（推論）能力來自「做出決定 → 看到後果 → 修正」的迴圈。
監控只提供後果，不提供決定。看一百次別人做對，不等於自己做過一次。

## 它直接反駁本庫的一個假說

[[judgment-supply]] 列的 **H1 場域轉移說**主張：實作被接手之後，
審查與規格也是複雜環境裡的模式比對，所以判斷力仍有累積場域。

Bainbridge 的論證是這條的**直接反面**，而且早了四十三年：
監控**不是**一個能累積能力的位置，它結構上就不提供累積的條件。

這也讓 [[the-ai-native-sdlc-playbook]] 那句「人的注意力集中到閘門上」
變得比原文聽起來更沉重——閘門就是監控位置。

## 逐代惡化

> Already in 1983, Bainbridge forecasted that it would become increasingly difficult to
> recruit people who have the right skills – and interest – to work as supervisors of
> automated systems.

> it is difficult, and **potentially more difficult for each new generation** of human
> operators interacting with the system, to ensure that the human operator has the skills
> to monitor the automated system and compensate when it fails.

第一代監控者是自動化之前就累積好能力的人。（推論）他們能監控，
是因為他們的能力來自**自動化之前的實作**——那個場域對下一代已經不存在。

## 已被實際採用的對策

瑞典有些自治市的做法是**刻意保留一小部分案件由人工處理**，
確保組織裡還有人有能力監控與接手。

（推論）這是把訓練場域當成一項**要編列預算的成本**，
而不是指望它作為工作的副產品自然出現。代價是明擺著的：那部分工作刻意不自動化。

另一條被觀察到的路徑是**參與設計**——參與 RPA 建置的承辦人員因此發展出流程與技術的新技能。
但那造成對少數個人的依賴，是組織脆弱點，而且**不可規模化**：
不可能讓每一代人都參與同一套系統的初次設計。

## 相關頁面

- [[ironies-of-automation-public-service]] —— 來源
- [[judgment-supply]] —— 被這一頁反駁的 H1 所在
- [[automation-fragmentation]] —— 同一份來源的反諷 #2
- [[the-ai-native-sdlc-playbook]] —— 把人的判斷力放在閘門上的那份
- [[the-80-percent-problem]] —— 接手那半的現代版
