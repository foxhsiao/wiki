---
title: METR：我們正在改變開發者生產力實驗的設計
type: source
aliases: [uplift update, METR 2026, 選擇效應]
tags: [ai, 軟體工程, 實證研究, RCT, 方法學, 生產力]
created: 2026-08-30
updated: 2026-08-30
status: active
confidence: high
source_type: report
author: METR（原檔 author 欄空白，未署個人名）
published: 2026-02-24
url: https://metr.org/blog/2026-02-24-uplift-update/
raw: "[[2026-08-30--metr-2026-uplift-update]]"
ingested: 2026-08-30
---

# METR：我們正在改變開發者生產力實驗的設計

> 一份**宣告自己量不準的研究報告**。
> 新一輪的兩組估計信賴區間**都跨過 0**，而 [[metr|METR]] 自己說中央估計值
> 「很可能是真實生產力影響的糟糕代理」。
> 本庫收到過最誠實、也最難用的一份來源。

## 三組數字並列

| 研究 | 對象 | 估計 | 信賴區間 | 跨過 0？ |
|---|---|---|---|---|
| 2025 早期（Feb–Jun 2025） | 16 位資深開發者 | 慢 **19%** | **+2% 到 +39%** | **否** |
| 2025 晚期（Aug 2025 起） | 原班參與者中的 10 位 | 加速 **−18%**（即慢 18%） | **−38% 到 +9%** | **是** |
| 2025 晚期 | 新招募的 47 位 | 加速 **−4%**（即慢 4%） | **−15% 到 +9%** | **是** |

**這是本庫第一次拿到 2025 那份研究的信賴區間**：`+2% 到 +39%`，不含 0，
所以當年那個「慢 19%」在統計上是顯著的。
而新一輪的兩組**都含 0**——意思是**在統計上與「沒有差別」無法區分**。

注意原文首句寫 2025 那份「造成 20% 的拖慢」，與該研究部落格頁與論文的 **19%** 不一致。
本頁照抄兩個數字，不做調和。

## 但這三個數字不能直接比較

原文的重點不是新數字，是**新數字不可信**，而且不可信的原因是**AI 普及本身**。

> "we believe that the data from our new experiment gives us an unreliable signal of
> the current productivity effect of AI tools."

> "these issues make it challenging to interpret our central estimate, and we believe it is
> **likely a bad proxy** for the real productivity impact of AI tools on these developers."

## 六個問題，前兩個最嚴重

| # | 問題 | 證據 |
|---|---|---|
| 1 | **招募與留任變難**——愈來愈多開發者不願意有一半工作不能用 AI | 即使付每小時 50 美元、任務自選仍然如此。系統性地漏掉**對 AI 期待最高**的人 |
| 2 | **開發者挑任務**——不想在無 AI 條件下做的任務就不提交 | 調查顯示 **30% 到 50%** 的開發者這樣做。系統性地漏掉**AI 增益最高**的任務 |
| 3 | 用 agentic AI 時嘗試的**任務類型**不同，偏向 AI 的強項 | 組內時間差可能不代表價值差 |
| 4 | 同一任務在兩種條件下**產出品質不同**（主觀程式碼品質、文件與測試的量） | — |
| 5 | 被分到「不准用 AI」的任務**比較容易做不完**——有一位開發者**一個都沒完成** | — |
| 6 | 用 agentic 工具時**難以回報工時**，因為等 agent 跑的時候會去做別的事 | — |

前兩項讓估計值成為**下界**：

> "these effects make it likely that our estimate reported above is a **lower-bound** on the
> true productivity effects of AI on these developers."

原文也誠實列出另一個共同原因：時薪從 150 美元降到 **50 美元**，這也加重了選擇效應。

## 方法細節

| 項目 | 2025 早期 | 2025 晚期 |
|---|---|---|
| 開發者 | 16 位 | **57 位**（10 位原班 + 47 位新招募） |
| repo | 大型成熟專案 | **143 個**，含**較小、較新、較不成熟**的專案 |
| 任務 | 246 個 | **800+ 個** |
| 時薪 | 150 美元 | **50 美元** |
| 經驗 | 平均貢獻多年 | 中位數 **10 年** |

隨機化方式不變：開發者先預先指定要做的任務，再由研究方隨機分配到允許或禁止用 AI。
兩份研究的**完整資料集都公開在 GitHub**。

## 三段值得整段記下來的開發者發言

> *"I'm torn. I'd like to help provide updated data on this question but also I really like using AI!"*
> ——原班開發者被邀請參加後續研究時

> *"I found I am actually heavily biased sampling the issues … I avoid issues like AI can finish
> things in just 2 hours, but I have to spend 20 hours. I will feel so painful if the task is
> decided as AI-disallowed."*

> *"my head's going to explode if I try to do too much the old fashioned way because it's like
> trying to get across the city walking when all of a sudden I was more used to taking an Uber."*

第二段是選擇效應的第一人稱證據：開發者**知道**自己在偏誤取樣，並說得出偏誤的方向與量級。

## METR 對趨勢的判斷

> "Based on conversations with study participants, we believe it is likely that developers are
> **more sped up from AI tools now — in early 2026** — compared to our estimates from early 2025.
> However, because of the selection effects in our experiment, our data is
> **only very weak evidence** for the size of this increase."

方向有訊號，**大小沒有**。而且方向的依據是訪談，不是實驗數據。

## 接下來的六條路

METR 列出替代方法，等於承認任務層級的隨機對照試驗這條路在這個題目上快走到底了：

1. **更密集的實驗**——縮短、加強度、提高報酬以拉高順從率
2. **觀察性資料**——從彙總統計（原文引用「約 **4%** 的 GitHub commit 由 Claude Code 撰寫」）到細緻的操作軌跡
3. **問卷**——即使自陳有偏誤，仔細設計的題目加上時間使用研究可能仍有訊號
4. **固定任務實驗**——放棄「開發者自選任務」這個原始設計的創新之處
5. **評估（evals）**——量測 agent 自主完成任務的能力
6. **開發者層級隨機化**——每個人全用或全不用。緩解任務層級的選擇問題，但**加重**開發者層級的選擇問題，且檢定力更低

## 對 wiki 的影響

- 新增：[[control-group-collapse]]
- 更新：[[metr-early-2025-ai-developer-productivity]]（**解除 `stale`**，並補上一直缺的信賴區間）、
  [[what-the-19-percent-measures]]（可主張清單重寫）、[[self-report-vs-measurement]]（被再次強化）、
  [[evidence-types-for-ai-capability]]（RCT 那格的限制變具體）、[[metr]]、
  [[the-80-percent-problem]]、[[can-judgment-be-outsourced]]、[[prompt-obsolescence]]、
  [[open-questions]]（**Q16 closed**，Q15 更新）、[[overview]]、[[index]]

## 我的判讀

（推論）這份東西的價值不在數字，在**它示範了一個領域怎麼失去量測自己的能力**。
一份研究公開說「我們的中央估計值很可能是個糟糕的代理」，這在任何領域都罕見。

它同時讓本庫必須降低對 METR 那條線的依賴：
**現在沒有任何一個數字可以直接引用**——2025 的顯著但過期、2026 的兩組都跨過 0 且被作者宣告不可解讀。
真正存活下來的是[[self-report-vs-measurement|自陳不可信]]這條方法學發現，
以及[[control-group-collapse|對照組崩解]]這個新問題。

盲點：

- **趨勢判斷的依據是訪談，不是數據。** 「2026 年初被加速得更多」這句話，
  證據等級與它自己批評的自陳調查是同一級。
- **時薪腰斬是個未被拆開的共變數。** 原文把它列為次要原因，但 150 → 50 美元是三分之二的降幅，
  它與「不想沒有 AI」對選擇效應各貢獻多少，沒有被分離。
- **新舊兩組的差異無法歸因。** 新招募者的 −4% 同時混雜了：不同的人、較不成熟的 repo、
  更新的工具（Claude Code、Codex 等 agentic 工具）。這對 [[open-questions]] Q15 是壞消息——
  最想被分離的那個變數（harness）正好被綁在另外兩個變數上。

## 相關頁面

- [[metr-early-2025-ai-developer-productivity]] —— 被這份更新的前一輪研究
- [[control-group-collapse]] —— 本文最可移植的發現
- [[what-the-19-percent-measures]] —— 兩份研究合起來能主張什麼
- [[metr]] —— 研究方
- [[evidence-types-for-ai-capability]] —— RCT 的適用邊界
