---
title: 對照組崩解
type: concept
aliases: [control group collapse, 選擇效應, selection effects, 量測失能]
tags: [ai, 方法學, 量測, 實證研究]
created: 2026-08-30
updated: 2026-08-30
status: active
confidence: medium
sources: ["[[metr-2026-uplift-update]]", "[[metr-early-2025-ai-developer-productivity]]"]
---

# 對照組崩解

> 當一項工具好用到受試者**拒絕在沒有它的條件下工作**，隨機對照試驗本身就失效了。
> 不是結果變糟，是**方法變得不可用**。

## 它長什麼樣

[[metr-2026-uplift-update]] 記錄了完整的一次崩解。同一套實驗設計，2025 年初跑得很好，
半年後就量不準了，原因全部指向同一件事——AI 普及本身：

| 崩解的環節 | 具體表現 |
|---|---|
| **招募** | 開發者不願意有一半工作不能用 AI，即使付錢、任務自選。漏掉的是**對 AI 期待最高**的人 |
| **任務提交** | **30% 到 50%** 的開發者承認會避開「AI 兩小時、自己二十小時」的任務。漏掉的是**增益最高**的任務 |
| **順從** | 被分到「不准用 AI」的任務比較容易做不完——有一位開發者**一個都沒完成** |
| **量測** | 用 agentic 工具時工時難以回報，因為等 agent 的時候會去做別的事 |

一位開發者的第一人稱說明最清楚：

> *"I found I am actually heavily biased sampling the issues … I avoid issues like AI can finish
> things in just 2 hours, but I have to spend 20 hours."*

他**知道**自己在偏誤取樣，也說得出方向與量級——但那不會讓偏誤消失。

## 偏誤方向是可推的

四個環節漏掉的都是同一側：最熱衷的人、增益最高的任務、最不願意沒有 AI 的行為。
所以估計值是**下界**，這是 METR 自己的結論。

方向可推、**大小不可推**——這正是它比一般雜訊更麻煩的地方。
知道「至少這麼多」對決策幫助有限。

## 為什麼它會愈來愈嚴重

崩解的驅動力是**工具變好**，而工具會繼續變好。

> "As AI capabilities continue to increase and developers' expectations grow as well,
> these effects will only get more dramatic, further limiting the validity of this study design."

也就是說：**一個工具愈有價值，愈難量測它到底有多少價值。**
（推論）這不限於 AI——任何普及到成為預設的工具都會遇到。
要求外科醫師隨機放棄一半病例的影像檢查，同樣招不到人。

## 它跟本庫既有的兩條線接得上

**接 [[prompt-obsolescence]]**：那一頁講規則檔會折舊，[[metr-early-2025-ai-developer-productivity]]
把它推廣到「測量也會折舊」。這一頁再推一級——**產生測量的那個方法也會折舊**。
折舊的三層由淺到深：規則過期 → 結果過期 → **量測方法本身失效**。

**接 [[open-questions]] Q13**（「趨近於零」的指標，成功與停止量測長得一樣）：
同一個結構。Q13 問的是指標怎麼分辨成功與失去量測能力；
這一頁是那個問題在真實研究上發生的樣子，而且**答案是分不出來**——
METR 有訪談、有調查、有第一人稱證詞，仍然只能說「方向大概是這樣，大小不知道」。

## 出路不是修實驗，是換方法

METR 列的六條替代路徑裡，只有一條是修補原設計（更密集的實驗），
其餘五條都在換工具：觀察性資料、問卷、固定任務實驗、agent 能力評估、開發者層級隨機化。

值得注意的是第六條的取捨：開發者層級隨機化能緩解**任務層級**的選擇問題，
但**加重開發者層級**的選擇問題，而且檢定力更低。
（推論）沒有免費的修法——每一種設計都在不同的地方漏水。

## 相關頁面

- [[metr-2026-uplift-update]] —— 來源，完整的一次崩解紀錄
- [[metr-early-2025-ai-developer-productivity]] —— 崩解之前那一輪
- [[prompt-obsolescence]] —— 折舊的第一層
- [[evidence-types-for-ai-capability]] —— RCT 的適用邊界因此縮小
- [[self-report-vs-measurement]] —— 被迫回頭依賴的那種證據
