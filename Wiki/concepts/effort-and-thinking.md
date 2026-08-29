---
title: Effort 與 thinking
type: concept
aliases: [effort, thinking]
tags: [ai, 模型, 成本]
created: 2026-08-02
updated: 2026-08-29
status: active
confidence: high
confidence_note: 同上：effort 與 thinking 是 Anthropic 自家參數的定義與行為，一手文件就是最高證據
sources: ["[[prompting-claude-opus-5]]"]
---

# Effort 與 thinking

> Effort 控制的是**模型想多少**，不是**它說多少**。這兩件事常被混為一談。

## 三個分開的控制項

| 你想控制 | 用什麼 | 不能用什麼 |
|---|---|---|
| 思考量與成本 | effort 檔位（low / medium / high / xhigh） | — |
| 對話回應長度 | 明確的簡潔指令 | 降 effort（不可靠） |
| 寫入磁碟的文件長度 | 另外的長度校準指令 | 上面兩者 |

[[claude-opus-5]] 三者都比前代長，所以三個都要單獨處理。

## 成本控制的建議路徑

從預設的 `high` 開始，依自己的 eval 調整：
**`low` 與 `medium` 要大方地用**，當成 token 成本與延遲的主要控制桿；
只在吃重的編碼與 agentic 工作上升到 `xhigh`。

從舊模型沿用過來的 effort 預設值要重跑一次 sweep——這是 [[prompt-obsolescence]] 的一個實例。

## 不要關 thinking

thinking 只能在 `high` 或以下關閉，而關掉會帶來兩種洩漏：

1. **工具呼叫變成文字**——寫進可見文字而不是結構化區塊，該呼叫不會執行；
   在 agentic 迴圈裡這段文字留在歷史裡繼續影響後續。工具密集的工作最常見。
2. **內部 XML 標籤跑進可見回應**。而且「不要思考」這類指令會**提高**洩漏機率。

> 對多數任務，**thinking 開著跑 low effort，比關掉 thinking 表現更好，成本相近。**

## 與脈絡工程的關係

[[context-engineering]] 把成本問題定位在「送什麼進去」；
effort 是另一條軸——「送進去之後讓它想多久」。
[[ai-development-economics]] 的「智慧模型路由」是第三條（用哪個模型）。
三條可以獨立調，實務上常被混在一起談。

## 相關頁面

- [[prompting-claude-opus-5]] —— 來源
- [[claude-opus-5]] —— 這些檔位所屬的模型
- [[ai-development-economics]] —— 成本控制的其他槓桿
- [[context-engineering]] —— 另一條成本軸
