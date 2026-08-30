---
title: METR：Early-2025 AI 對資深開源開發者生產力的影響
type: source
aliases: [METR study, METR RCT, 19% slowdown, downlift]
tags: [ai, 軟體工程, 實證研究, RCT, 生產力]
created: 2026-08-29
updated: 2026-08-30
status: active
confidence: high
source_type: paper
author: Joel Becker、Nate Rush、Beth Barnes、David Rein（剪存檔的 author 欄空白，此為 blog 署名與 arXiv 作者列，非取自 Raw 原檔）
published: 2025-07-10
url: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
raw: "[[2026-08-29--metr-early-2025-ai-developer-productivity]]"
ingested: 2026-08-29
---

# METR：Early-2025 AI 對資深開源開發者生產力的影響

> **本庫第一份實證研究**，也是第一份隨機對照試驗。
> 來源在頁首自宣結果已過期；後續研究 [[metr-2026-uplift-update]] 已於 2026-08-30 整併，
> `status` 從 `stale` 解除。**但「已整併」不等於「已被推翻」——見下方那一節。**

## 後續研究說了什麼（2026-08-30 整併）

[[metr-2026-uplift-update]] 帶來兩件事，一件補洞、一件限定。

**補洞：這份研究的信賴區間終於有了。** 本頁原本記著「原文未給信賴區間」，
後續報告揭露 2025 這一輪是 **19% 拖慢，信賴區間 `+2% 到 +39%`**——
**不含 0，所以當年這個結果在統計上是顯著的**。

**限定：後續兩組的區間都跨過 0。** 原班參與者中的 10 位估到 −18%（區間 `−38% 到 +9%`）、
新招募的 47 位估到 −4%（區間 `−15% 到 +9%`），
**兩組都與「沒有差別」在統計上無法區分**。而 METR 說那些新數字
「很可能是真實生產力影響的糟糕代理」，原因是 [[control-group-collapse|對照組崩解]]。

所以現在的狀態很尷尬也很誠實：
**這一份是顯著的但已過期；下一份是當期的但不可解讀。**
本庫兩個數字都不能直接當事實引用，見 [[what-the-19-percent-measures]]。

另注：後續報告首句把這份研究寫成「20% 的拖慢」，與本頁與論文的 **19%** 不一致，照抄不調和。

## 來源當初為什麼自宣過期

剪存檔的第一行就是：

> "These results are out of date. We have released results that are current as of early 2026,
> in a continuation of this study. **We believe these historical results no longer reflect the
> current impact of AI models on open-source developer productivity.**"

這不是本頁的推論，是 [[metr|METR]] 掛在原文頁首的橫幅，指向 2026-02-24 的後續研究。
在那份被 ingest 之前，本頁的所有數字都要當成**歷史測量**讀。

## 方法

| 項目 | 內容 |
|---|---|
| 設計 | 隨機對照試驗。每個 issue 隨機分配「允許用 AI」或「禁止用 AI」 |
| 受試者 | **16 位**資深開發者，在自己長期貢獻的 repo 上工作 |
| repo 規模 | 平均 **22k+ stars**、**1M+ 行**（論文另述平均超過 110 萬行） |
| 任務 | **246 個**真實 issue（bug 修復、功能、重構），由開發者自己提出，平均每個約兩小時 |
| 工具 | 允許組可自選，**主要是 Cursor Pro + Claude 3.5/3.7 Sonnet**（當時的前沿模型） |
| 記錄 | 全程錄螢幕，並自陳實作總時數 |
| 報酬 | 每小時 **150 美元** |

## 核心結果

允許用 AI 時，開發者完成 issue 的時間**多了 19%**。

| 測量 | 數字 |
|---|---|
| 事前預測的加速 | **+24%** |
| 事後自認的加速 | **+20%** |
| 實際 | **−19%** |

**事後自陳與實測差 39 個百分點**，而且是在同一批人、同一批任務上。
這條是 [[self-report-vs-measurement]]，也是 [[open-questions]] Q7 的解。

## 五個因子（取自 arXiv 論文，不在 Raw 剪存檔內）

剪存檔只寫「調查了 20 個潛在因素，發現 5 個可能有貢獻」，**那五個放在圖片
`factor-analysis.png` 裡，是 CDN 外連，`Raw/assets/` 沒有存檔**。
以下取自 arXiv 全文（`arxiv.org/html/2507.09089v1`），**出處不在 `Raw/` 之內**：

| 因子 | 機制 | 佐證數字 |
|---|---|---|
| Over-optimism about AI usefulness | **直接的生產力損失** | 事前 +24%、事後 +20%、實際 −19% |
| High developer familiarity with repositories | 拉高**人類**表現 | 開發者在先前接觸度高的 issue 上變慢更多 |
| Large and complex repositories | 限制 AI 表現 | repo 平均超過 110 萬行 |
| Low AI reliability | 限制 AI 表現 | AI 產出的**接受率不到 44%**，約 **9%** 的時間花在審查與清理 |
| Implicit repository context | 限制 AI 表現，**同時**拉高人類表現 | AI 缺少資深開發者仰賴的隱性程式碼庫知識 |

注意第一個因子的分類：過度樂觀不只是量測誤差，METR 把它列為**直接的生產力損失機制**。

## 六個被排除的因子（同樣取自 arXiv）

作者找到證據**反對**這些解釋：

- Unfamiliar development environment
- Cheating or under-use of AI
- Issue dropout
- Non-robust outcome measure
- Non-robust estimator
- **Non-frontier model usage**

最後一項堵掉了最常見的反駁（「他們用的模型太舊」）。
剪存檔的對應敘述是：開發者用的是前沿模型、遵守了分組指派、沒有差別性地放棄 issue、
有沒有 AI 交出的 PR 品質相近；慢下來的效應在不同結果指標、不同估計方法與多種子集分析下都存在。

## 作者自己劃的四條界線

原文用一張表列出「我們**不**提供證據支持的主張」：

| 我們不提供證據支持 | 澄清 |
|---|---|
| AI 目前不會加速多數或大部分軟體開發者 | 不主張受試者或這些 repo 代表軟體開發工作的多數 |
| AI 不會加速軟體開發以外的領域 | 只研究軟體開發 |
| 近期的 AI 在同樣設定下仍不會加速開發者 | 進展難以預測，過去五年已有大幅進展 |
| **沒有更有效的用法能在同樣設定下取得正向加速** | **Cursor 取樣的 token 不多，可能沒有最佳的提示或鷹架，領域／repo 特定的訓練、微調或 few-shot 有可能產生正向加速** |

第四列是 [[harness-engineering|harness]] 那條線的入口，展開見 [[what-the-19-percent-measures]]。

## 三種證據的偏誤方向

原文的討論段在調和 RCT、benchmark 與軼事自陳三者的矛盾，這是本庫第一次拿到
**證據類型的層級討論**，見 [[evidence-types-for-ai-capability]]。原文的判斷：

> "benchmarks may overestimate model capabilities by only measuring performance on
> well-scoped, algorithmically scorable tasks. And we now have **strong evidence that
> anecdotal reports/estimates of speed-up can be very inaccurate**."

另外三句限定條件值得記下來，因為它們界定了這個結果適用到哪裡：

- RCT 的結果在「可以對每個問題抽樣數百上千條軌跡」的情境下**較不相關**——受試者通常不會這樣做。
- Cursor 這類工具可能有**要數百小時才浮現的學習效應**，受試者只用了幾十小時。
- AI 的能力在「品質標準很高、或**有很多隱性要求**（文件、測試覆蓋率、lint／格式）——那些人類要花很多時間才學會的東西」的場景相對更低。

## 值得引用的原文

> "When developers are allowed to use AI tools, they take 19% longer to complete issues—
> a significant slowdown that goes against developer beliefs and expert forecasts."

> "developers expected AI to speed them up by 24%, and even after experiencing the slowdown,
> they still believed AI had sped them up by 20%."

> "we now have strong evidence that anecdotal reports/estimates of speed-up can be very inaccurate."

## 對 wiki 的影響

- 新增：[[metr]]、[[self-report-vs-measurement]]、[[evidence-types-for-ai-capability]]、
  [[what-the-19-percent-measures]]
- 更新：[[the-80-percent-problem]]（那個 19% 要重新定性，Q7 解開）、
  [[can-judgment-be-outsourced]]（本庫唯一的硬數據被作者宣告過期，且原本的用法是誤讀）、
  [[harness-engineering]]（**兩面**：因子 5 是外部佐證，但 benchmark 證據基礎同時被削弱）、
  [[context-engineering]]（隱性脈絡被實證指認為 AI 的瓶頸）、
  [[prompt-obsolescence]]（來源自宣過期，是折舊的新實例）、[[judgment]]、
  [[open-questions]]（Q7 closed）、[[overview]]、[[index]]

## 我的判讀

（推論）這是本庫收到過**方法學最硬的一份**，理由不是它有 RCT，是它對自己的結果最不客氣：
主動列出 20 個可能的替代解釋、公布其中 6 個被自己的資料排除、用一整張表寫出
「我們不提供證據支持什麼」，最後還在頁首掛橫幅說結果已過期。

盲點也要照講：

- **n=16，246 個任務。** 樣本小，作者自己也把「只有 16 人不會複製」列進 FAQ。
- **受試者是在自己長期貢獻的 repo 上工作**，這是刻意選的，但也讓結果只適用於
  「專家在熟悉的大型程式碼庫上」這個特定切面——因子 2 明講這拉高的是人類基準線。
- **harness 那條路完全沒被檢驗。** 它出現在「我們不提供反證」的表格裡，不是發現。
  拿它來解釋 19% 是一個**未經檢驗的假說**，見 [[what-the-19-percent-measures]]。

## 兩個擷取缺口

- **五個因子與六個排除項不在 `Raw/` 的剪存檔內**，本頁的內容取自 arXiv 全文。
  剪存檔對應位置只有一張 CDN 外連的圖。
- **FAQ 只剩問題、答案被剪存工具吃掉**。被吃掉的幾題正好是關鍵反駁：
  「既然可以不用 AI，開發者到底怎麼被拖慢的」「只有 16 人不會複製」
  「開發者是不是 Cursor 新手」「用同方差標準誤不恰當」。
- 原文含一段 canary 字串（用於偵測訓練語料汙染的追蹤碼），本頁不轉錄該識別碼。

## 相關頁面

- [[metr]] —— 執行這份研究的組織
- [[self-report-vs-measurement]] —— 本文最可移植的一條發現
- [[what-the-19-percent-measures]] —— 這個結果對本庫是支持還是削弱
- [[evidence-types-for-ai-capability]] —— RCT、benchmark、自陳三者的偏誤方向
- [[the-80-percent-problem]] —— 原本引用這個 19% 的頁
