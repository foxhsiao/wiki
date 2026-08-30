---
title: Ironies of Automation（Bainbridge 1983 原文）
type: source
aliases: [Bainbridge 1983, 自動化的反諷, Ironies of Automation]
tags: [自動化, 人因工程, 技能維持, 原典, 跨領域]
created: 2026-08-30
updated: 2026-08-30
status: active
confidence: high
source_type: paper
author: Lisanne Bainbridge（University College London 心理系）
published: 1983-11-01
url: https://doi.org/10.1016/0005-1098(83)90046-8
raw: "[[2026-08-30--bainbridge-ironies-of-automation-1983]]"
ingested: 2026-08-30
---

# Ironies of Automation（Bainbridge 1983 原文）

> **本庫最舊的一份來源，也是唯一的原典。** Automatica 19(6), 775–779。
> 五頁的 Brief Paper，1982 年 9 月發表於 Baden-Baden 的 IFAC 人機系統會議，
> 1983 年 11 月刊出。
>
> 它是 [[ironies-of-automation-public-service|Lindgren 2024]] 那份的來源。
> **補進原文之後發現轉引有數處失真**，本頁一併更正。

## 檔案來源（依 `[L6]`）

由 LLM 代為取得：WebFetch 抓公開鏡像的 PDF（出版商排版完整掃描，5 頁，無缺漏）。
**本文非開放取用**——© 1983 IFAC / Pergamon Press。
`Raw/` 不入版控（`.gitignore`），僅供本機閱讀。
先前嘗試失敗的路徑：原站 `ise.ncsu.edu` 已 404、`web.archive.org` 本環境擋、ScienceDirect 付費牆。

## 兩個定義（原文開頭）

> **Irony**: combination of circumstances, the result of which is the direct opposite of
> what might be expected.

> **Paradox**: seemingly absurd though perhaps really well-founded statement.

摘要一句話講完全文：

> "This paper discusses the ways in which automation of industrial processes may
> **expand rather than eliminate** problems with the human operator."

## 設計者態度的兩個反諷

Bainbridge 說重要的反諷來自兩處：系統設計者的**期待**，以及留給操作員的**任務性質**。

1. **設計者自己會出錯。** "designer errors can be a major source of operating problems"。
   而且他補了一句本庫該記住的：蒐集到這類資料的人**不願意發表**，因為實際數字難以解讀。
2. **想消除操作員的設計者，反而留給操作員一堆他自己想不出怎麼自動化的事。**
   > "the operator can be left with an **arbitrary collection of tasks**, and little thought
   > may have been given to providing support for them."

## 自動化之後留下的兩類任務

> "There are two general categories of task left for an operator in an automated system.
> He may be expected to **monitor** that the automatic system is operating correctly,
> and if it is not he may be expected to call a more experienced operator or to
> **take-over** himself."

### 手動控制技能會退化

> "Unfortunately, **physical skills deteriorate when they are not used**, particularly the
> refinements of gain and timing. This means that a **formerly experienced operator who has
> been monitoring an automated process may now be an inexperienced one**."

接手那一句的原文（本庫先前引的是轉引版，有兩處失真，見下）：

> "When manual take-over is needed there is likely to be something wrong **with** the process,
> so that unusual actions will be needed to control it, and one can argue that the operator
> needs to be **more rather than less skilled, and less rather than more loaded, than average**."

### 認知技能同樣依賴使用

> "efficient retrieval of knowledge from long-term memory depends on **frequency of use**"

> "this type of knowledge develops **only through use and feedback** about its effectiveness.
> People given this knowledge in theoretical classroom instruction without appropriate
> practical exercises will probably not understand much of it"

**逐代惡化那一句，原文比轉引精確得多**：

> "There is some concern that the present generation of automated systems, which are monitored
> by former manual operators, are **riding on their skills**, which **later generations of
> operators cannot be expected to have**."

### 監控本身是不可能的任務

> "We know from many 'vigilance' studies (Mackworth, 1950) that it is impossible for even a
> highly motivated human being to maintain effective visual attention towards a source of
> information on which very little happens, **for more than about half an hour**."

所以監控不尋常狀況這件事「必須由自動警報系統來做」。而如果沒有那樣的協助：

> "Otherwise the job is one of the worst types, it is very boring but very responsible, yet
> **there is no opportunity to aquire or maintain the qualities required to handle the
> responsibility**."

（`aquire` 是原文的拼字，照抄不改。）

### 一個本庫完全沒有的社會面向

> "The job is **'deskilled'** by being reduced to monitoring, this is difficult for the
> individuals involved to come to terms with. It also leads to the ironies of incongruous
> pay differentials, when the deskilled workers insist on a high pay level as the
> **remaining symbol of a status which is no longer justified by the job content**."

## 對策：原文自己給的

在 §2.3 談長期知識時，Bainbridge 直接給了維持技能的做法：

> "it can be important to **maintain manual skills**. One possibility is to allow the operator
> to use **hands-on control for a short period in each shift**. If this suggestion is laughable
> then **simulator practice** must be provided."

（推論）[[ironies-of-automation-public-service|Lindgren 2024]] 記的瑞典自治市
「刻意保留一小部分案件由人工處理」，就是這句話**四十一年後的實作**。
本庫先前把它當成新發現，其實原文就寫了。

原文也提到操作員自己知道這件事：

> "I know of one automated plant where the management had to be present during the night
> shift, or the operators switched the process to 'manual'."

## 最後的反諷

全文最有力的一句，本庫先前完全沒有：

> "Perhaps the final irony is that it is **the most successful automated systems, with rare
> need for manual intervention, which may need the greatest investment in human operator
> training**."

配套的另一句：

> "It is ironic to train operators in following instructions and then put them in the system
> to provide intelligence."

結論段：

> "I hope this paper has made clear both the irony that it is not by automating necessarily
> removing the difficulties, and also the possibility that resolving them will require even
> greater technological ingenuity than does classic automation."

## 轉引與原文的三處差異（更正紀錄）

[[ironies-of-automation-public-service]] 是本庫先前唯一的管道，補進原文後發現：

| 項目 | 轉引版 | 原文 |
|---|---|---|
| 接手那句 | "something wrong **in** the process" | "something wrong **with** the process" |
| 同上，句尾 | 到 "more rather than less skilled" 為止 | 還有 "**and less rather than more loaded, than average**" |
| 監控那句 | "one of the worst types **[of tasks]**" | "the job is one of the worst types"，**沒有方括號補字** |
| 逐代惡化 | 轉述為「對每個新世代更困難」 | 原文是 "**riding on their skills**, which later generations of operators cannot be expected to have" |
| irony 定義 | "**a** combination of circumstances" | "combination of circumstances"（無冠詞） |

差異不大但方向一致：**轉引版本都比原文弱一點、鬆一點**。
（推論）這是本庫第一次有機會比對原典與轉引，結論支持 `[S2]`「引文照抄」那條規則。

## 對 wiki 的影響

- 更新：[[monitoring-does-not-teach]]（引文更正、補上原文對策與「最後的反諷」）、
  [[ironies-of-automation-public-service]]（標明它是轉引來源，並指向本頁）、
  [[judgment-supply]]（Q6 的對策原文就有）、[[automation-fragmentation]]（原文用語是
  "arbitrary collection of tasks"）、[[harness-engineering]]、[[the-80-percent-problem]]、
  [[open-questions]]、[[overview]]、[[index]]

## 我的判讀

（推論）這份的份量與本庫其他九份不同，理由有三：

1. **它是 1983 年寫的，而本庫其餘九份全在 2019–2026 年之間。** 它預測的東西已經被四十年驗證過。
2. **它談的是通用的人機系統，不是某個產品。** 本庫其餘來源有九份出自賣方。
3. **它自己就給了對策**，而且對策具體到可以編預算（每班保留一段手動時間，做不到就用模擬器）。

弱點：

- **領域是工業製程控制**，不是軟體開發。套到 agent 上是（推論）。
  但比 RPA 那份更容易外推，因為它談的是人機分工的一般結構。
- **1983 年沒有 LLM。** 原文的「自動系統」是確定性的；agent 不是。
  這個差異對反諷 #1（設計者的錯誤）影響最大——LLM 的行為連設計者都無法完全預期。
- 五頁的 Brief Paper，論證密但沒有實證資料。它引用的 vigilance 研究是 1950 年的。

## 相關頁面

- [[monitoring-does-not-teach]] —— 本文最核心的一條
- [[ironies-of-automation-public-service]] —— 本庫先前唯一的管道，本頁更正了它的轉引
- [[judgment-supply]] —— Q6，本文直接回答的問題
- [[automation-fragmentation]] —— 本文的第二個反諷
- [[the-80-percent-problem]] —— 接手那半的現代版
