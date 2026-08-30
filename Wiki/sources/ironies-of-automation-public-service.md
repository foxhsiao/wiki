---
title: 自動化的反諷及其對公共服務自動化的意涵
type: source
aliases: [Ironies of automation, Lindgren 2024, 五個反諷]
tags: [自動化, 人因工程, 技能維持, 公共服務, 跨領域]
created: 2026-08-30
updated: 2026-08-30
status: active
confidence: high
source_type: paper
author: Ida Lindgren（Linköping University）
published: 2024-09-25
url: https://doi.org/10.1016/j.giq.2024.101974
raw: "[[2026-08-30--ironies-of-automation-public-service]]"
ingested: 2026-08-30
---

# 自動化的反諷及其對公共服務自動化的意涵

> **本庫第一份跨領域來源**，也是第一份不談軟體開發的來源。
> 它把 Lisanne Bainbridge 1983 年的《Ironies of Automation》做詮釋學分析，
> 拉出五個反諷並套到瑞典地方政府的 RPA 實務上。
>
> **對本庫的價值不在 RPA，在 Bainbridge**——那篇 1983 年的論文
> 早就回答了 [[open-questions]] Q6，而且答案不樂觀。

## 檔案來源（依 `[L6]`）

本檔由 LLM 代為取得，不是使用者剪存的。取得方式：WebFetch 抓 DiVA 的公開全文 PDF，
再放進 `Raw/`。**是出版商版本的完整 PDF，11 頁，沒有缺漏**——
論文為 CC BY 4.0 開放取用（Government Information Quarterly 41 (2024) 101974）。
**2026-08-30 更新：原文已補進本庫**（[[bainbridge-ironies-of-automation]]）。
本頁對 Bainbridge 的引用**全部是經由 Lindgren 的轉引**，
比對之後發現有數處失真（`in`／`with`、句尾遭截斷、方括號補字、逐代惡化被轉述得較弱）。
**要引 Bainbridge 請用原文頁，不要用本頁。** 差異清單見原文頁。

## Bainbridge 1983 是什麼

Automatica 19(6), 775–779。人因工程史上被引用最多的論文之一——
Lindgren 記的是 2024 年 9 月 Google Scholar 約 **3000 次引用**。

反諷的定義（Bainbridge 1983, p.775 原文，經 Lindgren 引用）：

> "a combination of circumstances, the result of which is the direct opposite of what might be expected"

自動化的經典目的是「以自動裝置與電腦取代人的手動控制、規劃與問題解決」。
但自動化不會消滅人在系統裡的位置，它**換掉人的工作內容**——換成兩件新的：
**監控**與**接手（take-over）**。

## 五個反諷

| # | 關於 | 內容 |
|---|---|---|
| 1 | **對人類能力的預設** | 所有涉入者都可能出錯，包括設計者。設計者的錯誤是操作問題的主因之一。自動化不是消除錯誤，**是換一個錯誤來源** |
| 2 | **工作的碎片化** | 設計者想用自動化消除操作員，結果留給操作員的是「電腦做不到」的那些任務——**一個任意的碎片集合**，造成新的錯誤來源、壓力上升、工作滿意度下降 |
| 3 | **監控** | 自動系統需要被監控，但即時監控超出人的認知限制。監控同時**無聊又高責任**。而且因為速度與黑箱性質，**沒有機會取得或維持**履行這個責任所需的能力 |
| 4 | **接手** | 系統失效需要人工接手時，操作員必須高度熟練——不只懂被自動化的流程，還要懂自動化系統本身。而需要接手時通常代表出了問題、需要非常規動作，所以**操作員需要比自動化之前更熟練，不是更不熟練** |
| 5 | **成本的分布** | 自動化為了省人力成本，卻在組織他處生成本（IT、更高技能人員），且分散在多個部門，**掩蓋了總成本**。結果自動化可能比人工更貴而組織不自知 |

Lindgren 標明反諷 #1–#4 直接源自 Bainbridge、相對穩健、可移轉到多種自動化場景；
**#5 是本文的產物，應視為待進一步檢驗的假說**。

## 直接回答 Q6 的三段

**監控學不到東西**（Bainbridge 1983, p.776，經 Lindgren 引用）：

> "one of the worst types [of tasks]; it is very boring but very responsible,
> yet **there is no opportunity to acquire or maintain the qualities required to
> handle the responsibility**."

**接手需要更高而非更低的技能**（Bainbridge 1983, p.775）：

> "… when manual take-over is needed there is likely to be something wrong in the process,
> so that unusual actions will be needed to control it, and one can argue that
> **the operator needs to be more rather than less skilled**"

**而且會逐代惡化。** Lindgren 的轉述：

> Already in 1983, Bainbridge forecasted that it would become increasingly difficult to
> recruit people who have the right skills – and interest – to work as supervisors of
> automated systems.

> it is difficult, and **potentially more difficult for each new generation** of human
> operators interacting with the system, to ensure that the human operator has the skills
> to monitor the automated system and compensate when it fails.

## 一個實證觀察到的對策

瑞典有些自治市理解了這個問題，做法是**刻意保留一小部分案件由人工處理**：

> handling a smaller subset of cases manually, to ensure that there are still people in the
> organization who can monitor the automated system and do a take-over when necessary.

這是本庫第一次看到針對 Q6 的**具體且被實際採用**的做法。

另一個被觀察到的路徑：參與 RPA 設計的承辦人員發展出關於流程與技術的新技能，
因而成為適合的監控者。但這造成**對少數個人的依賴**，是組織的脆弱點。

## 一句尖銳的引用

Lindgren 引 Hancock (2014, p.453) 在 Bainbridge 之上追問：
人被留在迴圈裡，是不是只是**「為了讓責任有個活體可歸」**
（"in order that blame can be attached to some living entity?"）。

## 方法與限制

| 項目 | 內容 |
|---|---|
| 方法 | 詮釋學分析，兩輪。先從 Bainbridge 原文抽反諷，再對照瑞典地方政府 RPA 的實證研究 |
| 實證基礎 | 2020–2023 的質性個案研究，訪談地方政府員工、RPA 廠商顧問、SALAR 代表 |
| 技術 | **只有 RPA**（規則式腳本，非機器學習）。Lindgren 明說 RPA 的「輕量」特性與其他自動化技術不同，論證的可移轉性需要進一步研究 |
| 範圍 | 單一國家、單一政府層級（瑞典地方政府）。Lindgren 自己列為限制 |
| 資助 | AFA Försäkring（AFA 保險），研究計畫「From Form to Robot?」 |

## 對 wiki 的影響

- 新增概念：[[monitoring-does-not-teach]]、[[automation-fragmentation]]
- 更新：[[judgment-supply]]（**Q6 的 H1 被 1983 年的論證直接反駁**）、
  [[judgment]]、[[can-judgment-be-outsourced]]、[[the-80-percent-problem]]（反諷 #4 是它的先驅）、
  [[harness-engineering]]（反諷 #1 與「多數失敗是設定失敗」隔 43 年同構）、
  [[ai-development-economics]]（反諷 #5 與 CapEx／OpEx 的對照）、
  [[control-group-collapse]]、[[open-questions]]、[[overview]]、[[index]]

## 我的判讀

（推論）這份的價值不平均：**Bainbridge 那半是原典級的，Lindgren 那半是應用**。
本庫需要的幾乎全在前者，而前者是**轉引**——這是本頁最大的弱點，
`confidence` 之所以還敢設 `high`，是因為引文都標了頁碼、而且 Lindgren 是同儕審查的期刊論文。
但若要在本庫的核心論證上用力壓，應該去補 Bainbridge 原文。

**最該注意的一件事**：本庫先前把「判斷力上移到閘門」當成一個**新問題**
（[[judgment-supply]] 是 2026-08-30 才寫的）。這份來源顯示它**1983 年就被完整描述過**，
包括逐代惡化的預測。（推論）本庫花了九份來源、四週，重新發現了一個四十三年前的結論。

盲點：

- **技術不同。** RPA 是規則式腳本，不是 LLM。Lindgren 自己說可移轉性待驗證。
  把它套到 agent 上是（推論）。
- **領域不同。** 公共服務的承辦流程與軟體開發的差異沒有被處理。
- **反諷 #5 是作者自己的產物**，不是 Bainbridge 的，作者也說它是假說。

## 相關頁面

- [[monitoring-does-not-teach]] —— 反諷 #3，Q6 的核心
- [[automation-fragmentation]] —— 反諷 #2，本庫原本沒有的概念
- [[judgment-supply]] —— 被這份來源大幅改寫的那一頁
- [[the-80-percent-problem]] —— 反諷 #4 是它的先驅
- [[harness-engineering]] —— 反諷 #1 與它隔 43 年同構
- [[bainbridge-ironies-of-automation]] —— 本頁轉引的原文；引用請以原文為準
