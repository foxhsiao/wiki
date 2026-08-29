---
title: Prompting Claude Opus 5
type: source
aliases: [Opus 5 提示指南]
tags: [ai, agent, 提示, 官方文件]
created: 2026-08-02
updated: 2026-08-02
status: active
confidence: high
source_type: article
author: Anthropic（官方文件）
published: unknown
url: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
raw: "[[2026-08-02--prompting-claude-opus-5]]"
ingested: 2026-08-02
---

# Prompting Claude Opus 5

> 本庫第一份**模型供應商的一手文件**。它的重要性不在教你寫提示，
> 而在它逐條列出了**哪些為前代模型調校的指令現在會反過來傷害你**。

## 核心主張

### 1. 有些指令現在是負債（[[prompt-obsolescence]]）

文件直接叫你**刪掉**這些東西：

| 該刪的 | 為什麼 |
|---|---|
| 「為任何非瑣碎任務加入最終驗證步驟」「用子 agent 驗證」 | 模型本來就會自我驗證，這類指令造成**過度驗證**，刪掉能省 token 而品質不變 |
| 「再檢查一次答案」「回應前重新驗證」 | 與模型自身行為疊加，只增成本不改善結果 |
| 為前代模型調的視覺 workaround | 可能已經不需要 |
| 沿用自舊模型的 effort 預設值 | 要在自己的 eval 上重跑一次 effort sweep |
| 「不要思考」「不要推理」這類規則 | **會提高內部 XML 標籤洩漏的機率** |

### 2. 模型會自己擴張任務範圍（[[agent-autonomy-cost]]）

> "Claude Opus 5 can also expand the scope of a task, adding steps that weren't requested
> or **applying its own judgment about what the task should be**."

同樣地，它比前代**更主動委派子 agent**——在真正獨立的大工作上划算，用在小任務上則是成本與時間的乘法。

### 3. Effort 控制的是思考量，不是輸出長度（[[effort-and-thinking]]）

降 effort 會減少思考量，但**不可靠地縮短可見回應**。要控制長度就明講。
寫到磁碟的檔案（報告、markdown）也比前代長，需要另外的長度校準指令。

### 4. 對 Reviewer 型任務的一條具體修正

> 如果你的審查提示寫「只回報高嚴重度問題」或「保守一點」，模型**可能照字面執行而少報**。
> 該叫它**全部回報，再用另一輪去過濾**。

這直接修正了 [[skill-design-patterns]] 的 Reviewer 模式。

### 5. 關掉 thinking 的兩種洩漏

- **工具呼叫變成文字**：把工具呼叫寫進使用者可見的文字而不是結構化區塊，該呼叫不會執行，
  而且在 agentic 迴圈裡這段洩漏文字會留在歷史裡影響後續。工具密集的工作（如搜尋）最常見。
- **內部 XML 標籤跑出來**。

首選解法是**不要關 thinking**，改用低 effort 控成本：
「對多數任務，thinking 開著跑 low effort 比關掉 thinking 表現更好，成本相近。」

## 其他可用的事實

| 項目 | 內容 |
|---|---|
| 脈絡視窗 | 1M token，是預設也是上限；指令遵循與工具呼叫在整個視窗內保持一致 |
| 低 effort | `low`／`medium` 用一小部分 token 與延遲就有好品質，應作為成本與延遲的**主要控制桿** |
| 程式碼審查 | 高精確率與高召回率，額外發現多為真問題而非誤報；低 effort 下準確度仍在 |
| 多 agent 協調 | writer-verifier 模式有效，agent 互相覆蓋彼此工作的情況少 |
| 遷移 | 對 Opus 4.8 的既有提示開箱即用；thinking 預設開啟，只能在 `high` 或以下關閉 |

## 對 wiki 的影響

- 新增：[[claude-opus-5]]、[[prompt-obsolescence]]、[[agent-autonomy-cost]]、[[effort-and-thinking]]
- 更新：[[harness-engineering]]（這份文件本身就是 harness 設定指南，且是「多數失敗是設定失敗」的直接印證）、
  [[context-engineering]]（靜態脈絡會折舊）、[[skill-design-patterns]]（Reviewer 模式的修正）、
  [[can-judgment-be-outsourced]]（**模型開始行使判斷，界線正在移動**）
- **與本庫既有規劃衝突**：[[open-questions]] Q9 原本想在 `CLAUDE.md` 加硬閘門，
  這份文件的方向相反——讓模型自己做例行判斷，只在會導致實質不同結果時才確認

## 我的判讀

（推論）這是供應商文件，天然偏向「我們的模型很好」，但它的內容形式讓它比行銷文件可信得多：
**它列的全是要你刪東西、而不是加東西**，而且明確指出模型的失效模式（範圍擴張、過度委派、標籤洩漏）。

真正的價值在一個更普遍的教訓：**規則檔會折舊**。
為某個模型版本寫的護欄，在下個版本可能變成成本來源。
本庫收錄的其他四份來源都預設 harness 是純資產，沒有一份處理過期問題。

## 相關頁面

- [[claude-opus-5]] —— 被描述的模型
- [[prompt-obsolescence]] —— 本文最重要的一般化教訓
- [[agent-autonomy-cost]] —— 自主性的成本面
- [[harness-engineering]] —— 這份文件在 harness 框架裡的位置
