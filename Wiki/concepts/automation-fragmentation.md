---
title: 自動化造成的工作碎片化
type: concept
aliases: [automation fragmentation, 碎片化, irony of fragmentation]
tags: [自動化, 人因工程, 工作方法]
created: 2026-08-30
updated: 2026-08-30
status: active
confidence: medium
sources: ["[[bainbridge-ironies-of-automation]]", "[[ironies-of-automation-public-service]]", "[[the-ai-native-sdlc-playbook]]"]
---

# 自動化造成的工作碎片化

> 設計者想用自動化消除操作員，結果留給操作員的是「電腦做不到」的那些任務——
> **一個任意的碎片集合**。它不是一份被設計過的工作，是剩下來的東西。

## 論證

出自 Bainbridge 1983 的反諷 #2（經 [[ironies-of-automation-public-service|Lindgren]] 整理）：

複雜的工作任務與流程，不是所有部分都能被明確定義並寫進程式。
於是設計者自動化掉能自動化的部分，**剩下的自動落到人身上**。
那些剩餘任務之間沒有內在的連貫性——它們的共同點只有「機器做不到」。

後果是三個：**新的錯誤來源**、**壓力上升**、**工作滿意度下降**。

## 原文的用語

[[bainbridge-ironies-of-automation|Bainbridge 1983]] 講這件事的原句：

> "the designer who tries to eliminate the operator still leaves the operator to do the tasks
> which the designer cannot think how to automate … the operator can be left with an
> **arbitrary collection of tasks**, and little thought may have been given to
> **providing support for them**."

兩個重點：**arbitrary collection of tasks**（任意的任務集合），
以及**沒有人替這些任務設計支援**。後者是本庫先前漏掉的一半——
碎片化的痛不只來自零碎，也來自零碎的部分沒有工具。

## 本庫原本沒有這條

本庫既有的框架都把自動化後的人類工作描述成**被升級**的：
[[factory-model|工廠模型]]說開發者變成產線設計者、
[[conductor-and-orchestrator|指揮家與協調者]]說人變成指揮、
[[the-ai-native-sdlc-playbook]]說人的注意力集中到閘門上。

這一條給了相反的可能：（推論）**剩下的工作不必然是更高階的，也可能只是更零碎的。**
分辨的方式是問——那些留給人的任務，是**被設計成一份工作**，
還是**只是機器做不到的東西的集合**？

## 與 80% 問題的關係

[[the-80-percent-problem]] 說剩下 20% 需要深度脈絡、錯誤性質從語法錯變成概念錯。
碎片化說的是同一批剩餘工作的**另一個屬性**：它們彼此不連貫。

（推論）兩者疊加起來比各自更麻煩：**又難、又零碎、又不累積**。
不累積那一半見 [[monitoring-does-not-teach]]。

## 一個可以自問的檢查

（推論）套到 agent 工作流上：如果一天下來留給你做的是
「審這個 diff、補那個 edge case、確認這個 API 沒被改壞、決定那個命名」——
那是不是一份工作，還是碎片？

原文對這個問題只給了診斷，沒給處方。Lindgren 的建議也只到
「要考慮留給人的任務**合起來是不是一個完整的工作情境**」為止。

## 相關頁面

- [[ironies-of-automation-public-service]] —— 來源
- [[monitoring-does-not-teach]] —— 同一份來源的反諷 #3 與 #4
- [[the-80-percent-problem]] —— 剩餘工作的另一個屬性
- [[factory-model]] —— 主張剩餘工作是升級的那一側
- [[conductor-and-orchestrator]] —— 同上
- [[bainbridge-ironies-of-automation]] —— 原文
