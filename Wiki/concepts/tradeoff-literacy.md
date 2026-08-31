---
title: 取捨識讀
type: concept
aliases: [tradeoff literacy, 知道有哪些取捨存在, steering]
tags: [ai, 軟體工程, 能力]
created: 2026-09-01
updated: 2026-09-01
status: active
confidence: low
sources: ["[[ai-engineering-skills-map-software-fundamentals]]"]
---

# 取捨識讀

> 操縱 agent 的前提不是會下指令，是**知道有哪些取捨可下**。
> 不知道某個取捨存在的人，不會做錯選擇——他根本不會做選擇，於是 agent 替他選了。

## 七條軸線

[[ai-engineering-skills-map-software-fundamentals|Ng]] 點名 coding agent 在缺乏引導時
會做壞取捨的七個維度：

| 軸線 | 典型的對立面 |
|---|---|
| latency | 快取與預算 vs 資料新鮮度 |
| availability | 冗餘成本 vs 停機容忍 |
| consistency | 強一致 vs 可用性與延遲 |
| reliability | 失敗處理與降級 vs 交付速度 |
| maintainability | 抽象與測試 vs 現在寫得快 |
| simplicity | 少一個元件 vs 少一段自幹的邏輯 |
| cost | 全部以上 |

原文沒有把這七條展開成上表的對立面，右欄是（推論）。
重點不在這張表完不完整，在於**它是一份存在清單**：
每一條都是一個「你可以要求 agent 往哪邊偏」的旋鈕，而旋鈕看不見就轉不動。

## 它和 80% 問題是同一個失敗的兩端

[[the-80-percent-problem]] 描述的是**輸出端**的殘餘：AI 生出來的東西看起來對、
可能通過基本測試，但概念上錯。取捨識讀描述的是**輸入端**的殘缺：
人給的方向裡缺了一整個維度，所以 agent 只能用預設值填。

兩者合起來解釋了為什麼「AI 產出很難審」——
審查者要抓的不只是寫錯的東西，還有**沒被提出來的選項**。
沒被提出來的選項在 diff 裡不留痕跡。

（推論）這也讓 80% 問題那條「把注意力集中在 AI 不行的地方」變得更難執行：
你沒辦法把注意力集中在你不知道存在的東西上。

## 它和判斷力的關係是上下游

[[judgment]] 是**選哪一邊**。取捨識讀是**知道有幾邊可選**。
後者是前者的前提：判斷力再好，作用不到看不見的維度上。

（推論）這給了 [[can-judgment-be-outsourced]] 一個新的切法。
那一頁問的是判斷的**結論**能不能寫成文件交出去；
取捨識讀問的是更前面一層——**選項空間**能不能寫下來。
選項空間比結論容易寫（它就是一張清單，Ng 那篇本身就是），
但一張清單不會告訴你在你的情境裡哪一條該優先。
所以（推論）**清單可以外包，權重不行**，這與 Q2 的問法一致。

## Ng 沒有處理的部分

- **這種識讀從哪來**，通篇沒談。他要求「deeply understand how software works」，
  但那種理解過去來自反覆做實作決定並承受後果，而那正是 agentic coding 接手的部分。
  對上 [[monitoring-does-not-teach]] 就是 [[open-questions]] Q6 的形狀。
- **「知道存在」與「選得對」被混為一談**。原文的因果是
  「不知道取捨存在 → 沒有 steer → 壞結果」，但知道之後選得對不對是另一件事，
  他沒有區分。
- **零證據**。這一頁的 `confidence` 設 `low` 就是這個原因：
  單一來源，而該來源本身沒有任何數據支撐，見
  [[ai-engineering-skills-map-software-fundamentals]] 的〈我的判讀〉。

## 相關頁面

- [[ai-engineering-skills-map-software-fundamentals]] —— 來源
- [[andrew-ng]] —— 提出者
- [[the-80-percent-problem]] —— 同一個失敗的輸出端
- [[judgment]] —— 取捨識讀的下游
- [[can-judgment-be-outsourced]] —— 「清單可外包、權重不可」這一刀的所屬爭論
- [[vibe-coding-spectrum]] —— 光譜講怎麼做，這一頁講先決條件
- [[monitoring-does-not-teach]] —— 這種識讀的供給問題
