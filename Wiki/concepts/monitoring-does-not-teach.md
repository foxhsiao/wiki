---
title: 監控學不到東西
type: concept
aliases: [monitoring does not teach, 監控的反諷, irony of monitoring]
tags: [自動化, 能力, 技能維持, 人因工程]
created: 2026-08-30
updated: 2026-08-30
status: active
confidence: medium
sources: ["[[bainbridge-ironies-of-automation]]", "[[ironies-of-automation-public-service]]", "[[the-ai-native-sdlc-playbook]]"]
---

# 監控學不到東西

> 自動化把人的工作換成**監控**與**接手**。
> 但監控**沒有機會取得或維持**履行那個責任所需的能力——
> 而接手需要的技能比自動化之前**更高**。
> 這是 Bainbridge 1983 年寫下的，不是 AI 時代的新發現。

## 兩句原文

**2026-08-30 更正**：本頁原本引的是轉引版，補進 [[bainbridge-ironies-of-automation|原文]]
後發現有失真，以下為原文。

監控（Bainbridge 1983, p.776）：

> "Otherwise the job is one of the worst types, it is very boring but very responsible, yet
> **there is no opportunity to aquire or maintain the qualities required to handle the
> responsibility**."

（`aquire` 是原文的拼字。）

接手（同上，p.775）：

> "When manual take-over is needed there is likely to be something wrong **with** the process,
> so that unusual actions will be needed to control it, and one can argue that the operator
> needs to be **more rather than less skilled, and less rather than more loaded, than average**."

轉引版少了句尾的「**負載要比平均更低而不是更高**」——那半句其實是本庫最該注意的：
需要接手的時候，人不只要更熟練，**還要更有餘裕**。而閘門位置通常是相反的。

兩句合起來是一個夾擊：**日常工作不再產生能力，而偶爾需要的那次要求更高的能力。**

## 為什麼監控學不到

原文給的機制有兩個，而且第一個有具體數字：

- **注意力的生理上限**——引 Mackworth (1950) 的 vigilance 研究：
  > "it is impossible for even a highly motivated human being to maintain effective visual
  > attention towards a source of information on which very little happens,
  > **for more than about half an hour**."

  所以監控不尋常狀況「必須由自動警報系統來做」——**要再裝一套自動系統來監控自動系統**。
- **黑箱**——看得到輸出，看不到過程。

技能退化那一段講得更直接：

> "**physical skills deteriorate when they are not used** … This means that a **formerly
> experienced operator who has been monitoring an automated process may now be an
> inexperienced one**."

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

原文的說法比轉引精確得多：

> "There is some concern that the present generation of automated systems, which are monitored
> by former manual operators, are **riding on their skills**, which **later generations of
> operators cannot be expected to have**."

「**riding on their skills**」——現在這代自動系統之所以能運作，
是因為它們騎在一批**在自動化之前就練成**的人身上。那批人退場之後沒有補充機制。

## 對策：原文 1983 年就寫了

> "it can be important to **maintain manual skills**. One possibility is to allow the operator
> to use **hands-on control for a short period in each shift**. If this suggestion is laughable
> then **simulator practice** must be provided."

（推論）[[ironies-of-automation-public-service|Lindgren 2024]] 記的瑞典自治市
「刻意保留一小部分案件由人工處理」，就是這句話**四十一年後的實作**。
本庫先前把它當成新發現。

值得注意「if this suggestion is laughable」這個轉折——
Bainbridge 自己預期會有人覺得「留一段時間手動操作」很可笑，
所以先備好了退路（模擬器）。（推論）四十年後在軟體開發脈絡下，
第一個選項聽起來一樣可笑，而第二個選項（給 agent 時代的模擬器）沒有人做過。

## 最後的反諷

全文最有力的一句：

> "Perhaps the final irony is that it is **the most successful automated systems, with rare
> need for manual intervention, which may need the greatest investment in human operator
> training**."

（推論）這條把 [[ai-development-economics|經濟學]]那一頁的算法整個翻過來：
自動化愈成功，訓練成本愈高，而不是愈低。

## 已被實際採用的版本

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
- [[bainbridge-ironies-of-automation]] —— 原文，本頁的引文已據它更正
