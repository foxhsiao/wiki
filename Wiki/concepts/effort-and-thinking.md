---
title: Effort 與 thinking
type: concept
aliases: [effort, thinking]
tags: [ai, 模型, 成本]
created: 2026-08-02
updated: 2026-09-01
status: active
confidence: high
sources: ["[[prompting-claude-opus-5]]", "[[running-a-software-factory-at-uber-scale]]"]
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

## 艦隊級的實作：預設 Medium

本頁的建議是「用低 effort 控成本，不要關 thinking」。
[[running-a-software-factory-at-uber-scale|Uber]] 把它做成了**全公司預設值**：

> **Reasoning effort defaulted to Medium**

理由是計價結構：輸出 token（含內部推理 token）在主要模型上的計價是輸入的數倍，
所以調這一項直接壓到最貴的那一類 token。原文的判斷是
「對一大類任務，Medium 在成本與品質之間取得好的平衡」。

配套的另外兩個預設值也在同一條線上：

- **自動壓縮在 400K tokens 觸發，即使模型有 1M 視窗**——
  平衡模型表現與 cache burst、重複輸入 token 的成本。
- **subagent 預設用較弱、較便宜的模型**（[[agent-autonomy-cost]]）。

（推論）這是本頁第一次拿到**規模化的佐證**：先前只有供應商文件說「該這樣調」，
現在有一個用量成長 7 倍的組織說「我們把它設成預設，而且成本降下來了」。
但要注意它證明的是**成本**，不是品質——原文沒有給 Medium 與 High 的品質對照。

## 相關頁面

- [[prompting-claude-opus-5]] —— 來源
- [[claude-opus-5]] —— 這些檔位所屬的模型
- [[ai-development-economics]] —— 成本控制的其他槓桿
- [[context-engineering]] —— 另一條成本軸
- [[running-a-software-factory-at-uber-scale]] —— 把這些建議做成艦隊預設值的實例
- [[context-tax]] —— 另一筆在 session 開始前就付掉的成本
