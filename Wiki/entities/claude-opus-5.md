---
title: Claude Opus 5
type: entity
aliases: [Opus 5]
tags: [ai, 模型, 產品]
created: 2026-08-02
updated: 2026-08-29
status: seed
confidence: high
confidence_note: 供應商對自家模型的一手描述，屬定義性事實（脈絡視窗、預設值、行為特性），交叉驗證意義不大
sources: ["[[prompting-claude-opus-5]]"]
---

# Claude Opus 5

> Anthropic 的模型，定位在複雜 agentic 編碼與企業工作，長時程任務是強項。
> 本庫收錄它是因為它的官方提示指南揭露了一件更普遍的事：[[prompt-obsolescence|規則檔會折舊]]。

## 規格

| 項目 | 內容 |
|---|---|
| 脈絡視窗 | 1M token（預設即上限） |
| Thinking | 預設開啟，只能在 effort `high` 或以下關閉 |
| Effort 檔位 | low / medium / high（預設）/ xhigh |
| 前代 | Claude Opus 4.8，既有提示開箱即用 |

## 與前代的行為差異（影響提示的部分）

- **話變多**：使用者可見回應比前代長；agentic 工作時會頻繁預告自己要做什麼；寫到磁碟的檔案也更長。
- **自己驗證、自己修錯**：不需要被叫就會做，所以叫它做反而是浪費（[[agent-autonomy-cost]]）。
- **會擴張任務範圍**，對「這個任務應該是什麼」行使自己的判斷。
- **更主動委派子 agent**。
- 低 effort 的性價比大幅提升，應該當成主要的成本控制桿（[[effort-and-thinking]]）。

## 為什麼這對本庫重要

它是本庫第一個**會自己做判斷的實體**。
[[can-judgment-be-outsourced]] 討論的界線，在這一份文件裡不是理論——
供應商直接寫著「模型會對任務應該是什麼行使自己的判斷」，並把它列為需要被**約束**的行為。

## 相關頁面

- [[prompting-claude-opus-5]] —— 來源
- [[prompt-obsolescence]] —— 由它的版本差異推出的教訓
- [[agent-autonomy-cost]] —— 它的自主性帶來的成本
- [[effort-and-thinking]] —— 它的成本控制介面
