---
title: 自陳與實測的落差
type: concept
aliases: [self-report vs measurement, 感知落差, perception gap]
tags: [ai, 生產力, 方法學, 量測]
created: 2026-08-29
updated: 2026-08-29
status: active
confidence: medium
sources: ["[[metr-early-2025-ai-developer-productivity]]"]
---

# 自陳與實測的落差

> 同一批人、同一批任務：自認被 AI 加速 **20%**，實際被拖慢 **19%**。
> **差 39 個百分點，而且方向是反的。**

## 三個數字

[[metr-early-2025-ai-developer-productivity]] 在 16 位資深開發者、246 個真實 issue 上量到：

| 測量 | 數字 |
|---|---|
| 事前預測 | **+24%** |
| **事後自認**（做完之後） | **+20%** |
| 實際 | **−19%** |

關鍵不在事前預測錯了——預測本來就會錯。關鍵是**做完之後、親身經歷了那個拖慢，
自陳仍然是 +20%**。體驗沒有修正信念。

## 它是 Q7 的解

本庫的 [[the-80-percent-problem]] 並列過兩組互斥數字，來源自己沒有調和：

| 數字 | 方法 |
|---|---|
| 生產力提升 25–39% | **自陳調查** |
| 資深開發者慢 19% | **RCT 實測** |

它們不是互斥，是**在測不同的東西**。原文的判斷很硬：

> "we now have strong evidence that anecdotal reports/estimates of speed-up
> can be very inaccurate."

（推論）本庫先前對 Q7 的暫用解釋是「增益取決於任務是否已被良好規格化」——
那個推論沒有來源支撐，現在可以退場了。落差的來源是**量測方法**，不是任務性質。

## 它不只是量測誤差

METR 把「對 AI 有用性的過度樂觀」列為五個因子之一，而且分類是
**Over-optimism about AI usefulness (Direct productivity loss)**——
不是「讓數字失真的偏誤」，是**直接造成生產力損失的機制**。

（推論）機制大概是這樣：因為相信 AI 會更快，所以選擇用它、接受它的產出、
花時間修它——而這些選擇本身就是成本。信念錯誤直接轉成工時。

## 可移植的推論

（推論）這條的適用範圍遠大於寫程式。任何「導入 AI 之後感覺快很多」的自我評估，
在沒有對照組的情況下都要當成**未經量測**。這對本庫其他來源是一個通用的折扣係數：
[[the-new-sdlc-with-vibe-coding]] 引用的 25–39%、Deloitte 的 30–35%，
只要是自陳調查就適用。

但別過度延伸——這是**一份**研究、**16** 個人、**特定**設定。
它證明的是「自陳可能非常不準」，不是「自陳一定反向」。

## 相關頁面

- [[metr-early-2025-ai-developer-productivity]] —— 來源
- [[the-80-percent-problem]] —— 那兩組互斥數字的所在
- [[evidence-types-for-ai-capability]] —— 自陳在證據層級裡的位置
- [[what-the-19-percent-measures]] —— 這個 19% 到底能拿來主張什麼
