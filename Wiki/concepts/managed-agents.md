---
title: 受管 agent
type: concept
aliases: [managed agents, software factory, 軟體工廠]
tags: [ai, agent, 組織, 成本]
created: 2026-09-01
updated: 2026-09-01
status: active
confidence: medium
sources: ["[[running-a-software-factory-at-uber-scale]]"]
---

# 受管 agent

> 不再優化幾千個工程師各自的終端機 session，改成經營**一支專用 agent 艦隊**——
> 每一個配自己的評估 benchmark 與 Pareto 最優模型。
> [[running-a-software-factory-at-uber-scale|Uber]] 說這是它整篇文章的核心策略轉移。

## 主張

> "The core strategic shift is **moving from interactive developer workflows to fully managed agents**.
> Transitioning SDLC workloads into managed environments grants complete control over model routing,
> execution harnesses, and operational spend."

理由是控制權：受管環境裡，模型路由、執行 harness、花費全部是可設定的；
互動式 session 裡，這些散在每個工程師的習慣中。

（推論）這是 [[factory-model]]「開發者的產出是產出程式碼的那套系統」推到組織層級的版本——
只是 Uber 把它從心智模型變成了**預算單位**。

## 已經在跑的受管 agent

原文列的：程式碼審查（uReview，處理所有 PR）、CI 失敗自我修復、
帶視覺驗證的端到端 PR、on-call 告警分流、進來的 bug 除錯、各種程式碼維護任務，
全部帶人工審查與升級路徑。

原文說**愈來愈多 session 不是由人發起的**。

## 每個 agent 的固定配方

> "For every new agent, we follow a consistent roadmap: establish target outcome metrics,
> assemble evaluation benchmarks, and identify a Pareto-optimal model."

以 uReview 為例，benchmark 是**從已知有 bug 的真實 PR** 建的，分成易／中／難，
評分是 precision、recall、F1，加上每次審查的成本、延遲、逾時、雜訊。
「Pareto 最優」在這裡的定義是**每個完成任務的成本、輸出品質、模型可靠度**三者一起看。

原文對節奏的說法很直接：**前緣每幾週就移動一次，所以要一直換。**

## 它和本庫既有的兩頁怎麼接

- [[agent-config-evals]] 說「操控 agent 的設定值得程式碼享有的那種回歸測試」，
  對象是 `CLAUDE.md`、skills、hooks。Uber 把同一套機制用在**選模型**上：
  benchmark 是常設的，模型是可替換的變數。
  （推論）兩者是同一個結構——**把 agent 的組成當成可回歸測試的設定**——
  只是換掉的東西不同。
- [[autonomy-tiering]]／[[advisory-vs-deterministic-control]] 說的是**權限**怎麼分級；
  受管 agent 說的是**成本與模型**怎麼集中控制。
  （推論）兩者是同一個集中化的兩個面向：把散在個人手上的決定收回到可設定的位置。

## 它預設了什麼

（推論）這條路線成立有兩個前提，原文沒有明說：

1. **任務要夠標準化**才能建 benchmark。uReview 可以，因為「找出 PR 裡的 bug」有標準答案；
   「這個架構決定對不對」沒有。所以受管 agent 天然只覆蓋得到 SDLC 裡可判定的那一段。
2. **要有規模才划算**。為一個 agent 建 benchmark、選模型、持續重測是固定成本，
   要攤在夠大的用量上。原文自己說「your mileage may vary depending on your codebase,
   team size, and agent workflows」。

（推論）所以這一頁對小團隊的可移植性，比本庫其他實作類的頁面都低。
可移植的是**先定成效指標、再建 benchmark、才選模型**這個順序。

## 相關頁面

- [[running-a-software-factory-at-uber-scale]] —— 來源
- [[uber]] —— 提出者
- [[factory-model]] —— 同一個心智模型的個人版
- [[agent-config-evals]] —— 同一套回歸測試機制，換一個對象
- [[autonomy-tiering]] —— 集中化的另一個面向：權限
- [[context-tax]] —— 受管環境能一次砍掉的成本之一
- [[ai-native-sdlc]] —— 這些 agent 分佈在哪些階段
