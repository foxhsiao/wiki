---
title: 技能跨模型移轉
type: concept
aliases: [skill transfer, cross-model transfer, 負移轉]
tags: [ai, agent, skill, 能力]
created: 2026-09-01
updated: 2026-09-01
status: active
confidence: medium
sources: ["[[wikiskill]]", "[[prompting-claude-opus-5]]"]
---

# 技能跨模型移轉

> 一個模型從自己的失敗裡長出來的程序知識，**寫成檔案之後可以給別的模型用，
> 而且常常比對方自己長出來的更好**。
> 但只有當那份知識寫的是通則；寫的是自己的權宜之計時，它會**害到別人**。

## 移轉是有效的，方向還不只往下

[[wikiskill]] 讓五個模型各自演化 skill，再交叉套用：

| 情境 | 無 skill | 自己演化的 | 別的模型演化的 |
|---|---|---|---|
| Qwen-3.5-9B / ALFWorld | 34.7% | 63.4% | **70.2%**（Qwen-3.6-27B 的） |
| Qwen-3.5-9B / SpreadSheet | 24.3% | 33.6% | **50.5%**（Qwen-3.6-27B 的） |
| Gemma-4-31B / LiveMath | 33.9% | 56.7% | **73.7%**（Qwen-3.6-27B 的） |

而且**小模型演化的 skill 能幫到大模型**：Qwen-3.5-4B 的 skill 讓 Gemma-4-31B
在 LiveMath 拿 73.1%、ALFWorld 拿 66.9%。原文的結論是：

> "**stronger source models do not necessarily produce better skills**"

## 所以發現與執行是兩種能力

> "These results suggest that **skill discovery and skill execution are distinct capabilities**."

（推論）這句話比它看起來重要。它意味著「從經驗裡歸納出一條可用的程序」
與「照著那條程序把事做好」可以分開發生在不同的主體上，
而中介物只是一個 markdown 檔。

## 但負移轉是真的，而且機制很具體

同一份研究裡，Qwen-3.5-4B 的 skill 讓 Gemini-3.5-Flash 在 SpreadSheet
從 **50.5% 掉到 18.1%**——比完全沒有 skill 還糟得多。
換成 Qwen-3.6-27B 的 skill 則升到 63.4%。

原文的錯誤分析給了兩個原因：

1. Qwen-3.5-4B 的 skill 編碼的是**低階權宜之計**（單行 Python 指令、字串轉換規則）。
   這些讓小模型避開執行失敗，卻**限制**強模型改用完整的端到端腳本。
2. 破碎的診斷步驟帶來多餘的工具呼叫，把 Gemini-3.5-Flash 的互動預算**在完成任務前耗光**。

判準因此很清楚：**移轉得動的是通則，移轉不動的是為特定模型的弱點做的補丁。**

## 這是規則檔折舊的實驗證據

[[prompt-obsolescence]] 主張「為某個模型版本寫的護欄，在下個版本可能變成成本來源」，
本庫先前只有 [[prompting-claude-opus-5]] 這一份供應商文件支撐它。

負移轉是同一件事的**受控實驗版本**：換的不是版本而是模型，但機制一模一樣——
針對 A 的弱點寫的規則，在沒有那個弱點的 B 身上變成純粹的限制。
（推論）這讓折舊的第一層從「供應商說會這樣」升級為「有人測到，而且量到掉 32.4 分」。

## 對本庫核心矛盾的意義

[[can-judgment-be-outsourced]] 列的解法 1（**有損壓縮說**）主張：
文件承載的是判斷的**結論**，不是產生結論的能力。

移轉結果對這條是**反向證據**。被移轉的不只是「這題的答案」，
是一套面對整類任務的程序，而接收方用它拿到比自己摸索更好的成績——
（推論）這比較像**能力也跟著過去了**，至少在「執行」這一面上。

但要誠實界定範圍，有三條：

1. 接收方拿到的是**執行能力**，不是**發現能力**。
   沒有任何結果顯示接收方因此更會產生下一份 skill。
   這反而支持了有損壓縮說切開的那條線。
2. 移轉的是 **agent 之間**，不是人之間。人的判斷力怎麼傳遞是另一個問題（[[judgment-supply]]）。
3. 負移轉顯示這種傳遞**有條件**：知識要抽象到不綁在傳遞者的弱點上，才傳得動。
   （推論）這對人也成立得可疑地順——資深者的訣竅若綁在他自己的習慣上，教下去也可能有害。

## 相關頁面

- [[wikiskill]] —— 來源
- [[persistent-knowledge-layer]] —— 產生這些 skill 的機制
- [[can-judgment-be-outsourced]] —— 被這一頁影響的解法 1
- [[prompt-obsolescence]] —— 負移轉是它的實驗版本
- [[agent-skills]] —— 被移轉的東西是什麼
- [[judgment-supply]] —— 人的那一側，本頁不涵蓋
- [[open-questions]] —— Q2 的新證據
