---
title: AI-native SDLC
type: concept
aliases: [agentic SDLC, AI SDLC, agentic software development]
tags: [ai, 軟體工程, 流程, 治理]
created: 2026-08-29
updated: 2026-09-01
status: active
confidence: medium
sources: ["[[the-ai-native-sdlc-playbook]]", "[[the-new-sdlc-with-vibe-coding]]", "[[running-a-software-factory-at-uber-scale]]"]
---

# AI-native SDLC

> 把軟體生命週期從**直線**改成**迴圈**，六個階段每一個都嵌入 AI，
> 階段之間靠版控產物自動交接而不是靠會議與簽核。

## 出發點：瓶頸位移

傳統 SDLC 的控制手段是為「寫程式最貴最慢」設計的。PRD、估點儀式、產品資安審查，
存在的理由都是在數週到數季的開發期間**強迫對齊**。當 build 塌縮成幾小時：

1. 瓶頸移到 build **左右兩側**——plan、review/test、deploy 還在人的速度；
2. 控制手段**失真**——逐行人工審查跟不上 agent 產出的 diff；
3. 治理成本**上升**——例外還在走每週或每月開一次的會。

[[the-ai-native-sdlc-playbook]] 的立場是：實作階段已經被改造過一輪，
生命週期的其餘部分需要**同等程度**的改造，否則產能被卡在原地。

## 與既有框架的關係

| 這一頁 | 既有頁面 | 關係 |
|---|---|---|
| 瓶頸移到 build 兩側 | [[the-80-percent-problem]] | 同一件事的組織版：AI 不消滅實作，它把實作轉成審查，而審查是人的速度 |
| 六階段嵌入 AI | [[factory-model]] | [[addy-osmani]] 描述工廠長什麼樣，這份描述工廠怎麼裝 |
| 產物自動交接 | [[harness-engineering]] | harness 的作用範圍從一個 session 擴到整條流程 |
| 迴圈而非直線 | [[elephant-goldfish-model]] | 後者是單一功能的四階段流程，這份是整個組織的持續迴圈 |

## 非線性：play 的順序不等於階段的順序

原文把 13 個 play 掛在六個階段下，但明說**列出的階段順序不是採用順序**：
依賴圖裡沒有箭頭指進去的 play 可以最先做（`intent.md`、`CLAUDE.md`、skills、hooks、
回饋迴圈都是 prerequisites: None），有箭頭指進來的要先做完上游。

實務意涵：不必從 Plan 開始改造。`CLAUDE.md` 與回饋迴圈是零前置的起點。

## 人在哪裡

> "Human attention concentrates at the gates, reviewing what the agent flagged rather than
> starting each stage from scratch."

起步時每一步由人下提示；終局是每份被接受的產物自動觸發下一道閘門。
人的注意力**不是變少，是換位置**——從「啟動每個階段」變成「在閘門上審 agent 標記出來的東西」。
這對 [[judgment|判斷力]]那條線是新的證據形狀，見 [[can-judgment-be-outsourced]]。

## 邊界

（推論）這套流程預設組織已經有 git、CI、branch protection、metrics store 與 MDM。
原文沒有處理起步成本，也沒有給任何成效數字。
對照 [[the-new-sdlc-with-vibe-coding]]——那份有數據但不談治理，這份談治理但沒數據。

## 這些階段上已經站著受管 agent

本頁描述的是流程形狀。[[running-a-software-factory-at-uber-scale|Uber]]
提供了「每個階段實際站著什麼」的一份清單——全部是受管 agent，帶人工審查與升級路徑：

程式碼審查（處理所有 PR）、CI 失敗自我修復、帶視覺驗證的端到端 PR、
on-call 告警分流、進來的 bug 除錯、各種程式碼維護任務。

原文說**愈來愈多 session 不是由人發起的**。

（推論）這對本頁的迴圈說法是一個具體化，也是一個限定：
受管 agent 覆蓋得到的是 SDLC 裡**可判定**的那一段（「這個 PR 有沒有 bug」有標準答案），
覆蓋不到架構決定這類沒有標準答案的部分。所以本頁那個迴圈**不是均勻被自動化的**，
瓶頸會集中在建不了 benchmark 的階段。展開見 [[managed-agents]]。

## 相關頁面

- [[the-ai-native-sdlc-playbook]] —— 來源
- [[artifact-chain]] —— 貫穿六階段的產物鏈
- [[autonomy-tiering]] —— 迴圈閉合之後的自治分級
- [[factory-model]] —— 同一主張的個人／團隊版
- [[the-80-percent-problem]] —— 瓶頸為什麼卡在審查
- [[two-sdlc-frameworks]] —— 與 Google 白皮書的框架比較
