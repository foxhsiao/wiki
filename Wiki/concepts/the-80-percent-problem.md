---
title: 80% 問題
type: concept
aliases: [the 80% problem]
tags: [ai, 軟體工程]
created: 2026-08-01
updated: 2026-08-30
status: active
confidence: medium
sources: ["[[the-new-sdlc-with-vibe-coding]]", "[[metr-early-2025-ai-developer-productivity]]", "[[metr-2026-uplift-update]]", "[[ironies-of-automation-public-service]]"]
---

# 80% 問題

> AI 能快速生出一個功能約 80% 的程式碼，剩下 20%——邊界情況、錯誤處理、整合點、
> 細微的正確性要求——需要目前模型普遍缺乏的深度脈絡。

## 錯誤的性質變了

從語法錯誤變成**概念錯誤**：對商業邏輯的錯誤假設、遇到含糊需求不主動追問、
漏掉邊界情況、做出會製造長期維護負擔的架構決定。

**這些錯誤更難抓，正是因為程式碼「看起來對」，而且可能通過基本測試。**

## 最有效的姿勢

不是靠「照單全收 AI 的產出」來變快，是靠**把自己的注意力集中在 AI 不行的地方**：
含糊的需求、架構取捨、正確性驗證。AI 負責它擅長的：把定義清楚的任務快速實作出來。

## 支持與反對的數據

| 來源 | 數字 |
|---|---|
| 產業調查（尾註 7） | 生產力提升 25–39% |
| Deloitte（尾註 9） | 全流程 30–35% |
| **METR（尾註 8/10）** | **資深開發者在特定任務上反而多花 19% 時間**，主要花在驗證、除錯、修正 AI 產出 |

白皮書自己並列了這兩組數字但**沒有調和它們**。
（推論）最省事的解釋是：增益高度取決於任務是否已被良好規格化——
這正好與 [[vibe-coding-spectrum|光譜]] 的主張一致，但白皮書沒有明說。

## Q7 解開了：那兩組數字在測不同的東西

上面那張表並列的兩組數字，白皮書沒有調和，本頁先前的推測是
「增益取決於任務是否已被良好規格化」。**讀完原始研究後，那個推測可以退場了。**

| 數字 | 方法 |
|---|---|
| 提升 25–39%、Deloitte 30–35% | **自陳調查** |
| METR 慢 19% | **RCT 實測** |

[[metr-early-2025-ai-developer-productivity]] 在同一批人身上量到：
事前預測 +24%、**事後自認 +20%**、實際 −19%。
自陳與實測差 **39 個百分點**，方向還是反的。
原文的判斷是「已有強證據顯示自陳的加速估計可能非常不準」。

落差來自**量測方法**，不是任務性質。展開見 [[self-report-vs-measurement]]。

## 但這個 19% 不能拿來證明本頁原本想證明的事

本頁把 METR 的數字當成「AI 不消滅實作工作，它把實作轉成審查工作」的佐證。
方向沒錯（因子 4 顯示 AI 產出的接受率不到 44%、約 9% 的時間花在審查與清理），
**但這個數字撐不起「判斷力無法外包」那個更大的主張**——
METR 找到的五個因子沒有一個關於人類判斷不可替代。見 [[what-the-19-percent-measures]]。

另外，原文頁首已由作者宣告這批結果過期，引用時要標明它是歷史測量。

## 那個 19% 現在不能再引用了

[[metr-2026-uplift-update]] 讓本頁表格裡的 METR 那一列失效。

它同時給了本庫先前沒有的信賴區間：2025 那輪是 **19%，區間 `+2% 到 +39%`**，不含 0，
所以當年**是顯著的**。但後續兩組的區間都跨過 0（原班 `−38% 到 +9%`、新招募 `−15% 到 +9%`），
而且 METR 自己說那些數字「很可能是真實生產力影響的糟糕代理」。

所以本頁的表格現在要這樣讀：**「提升 25–39%」仍然是自陳調查（不可靠），
而「慢 19%」是一個顯著但已過期的測量**。兩邊都不能當事實用。
Q7 的解（自陳與實測的方法差異）不受影響，那是方法學發現，不是那個數字。

## 與其他來源的張力

[[dave-rensin|Rensin]] 說既有 monolith「一週就能餵完大象」，同時承認葉節點的 README
約 50% 是錯的、要工程師逐個修。他沒算這在百萬行等級的人力總量。
80% 問題與 METR 的數字都指向同一件事：**AI 不消滅實作工作，它把實作轉成審查工作**，
而審查工作的成本被系統性低估。

## 這條有一個 1983 年的先驅

[[ironies-of-automation-public-service]] 記的 Bainbridge 反諷 #4：

> "… when manual take-over is needed there is likely to be something wrong in the process,
> so that unusual actions will be needed to control it, and one can argue that
> **the operator needs to be more rather than less skilled**"

（推論）這與本頁是同一個結構，只是換了領域與四十三年：
自動化接手的是規律的部分，**留給人的正是最難的那一段**，
所以人需要的技能不降反升。

差別在於本頁把它當成「AI 的能力邊界」，Bainbridge 把它當成
**自動化的結構性後果**——與工具多強無關，因為工具愈強，剩下的殘餘就愈是異常情況。

## 相關頁面

- [[the-new-sdlc-with-vibe-coding]] —— 來源
- [[vibe-coding-spectrum]] —— 增益差異可能的解釋
- [[elephants-goldfish]] —— 張力的另一方
- [[judgment]] —— 那剩下的 20% 需要的東西
- [[metr-early-2025-ai-developer-productivity]] —— 那個 19% 的原始研究
- [[self-report-vs-measurement]] —— Q7 的解
- [[what-the-19-percent-measures]] —— 這個數字能與不能主張什麼
- [[metr-2026-uplift-update]] —— 那個 19% 為什麼不能再引用
- [[control-group-collapse]] —— 新數字不可解讀的原因
- [[ironies-of-automation-public-service]] —— 這條 1983 年的先驅版
