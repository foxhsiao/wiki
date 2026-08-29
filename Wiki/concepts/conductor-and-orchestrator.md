---
title: 指揮家與協調者
type: concept
aliases: [conductor, orchestrator]
tags: [ai, 工作方法, 職涯]
created: 2026-08-01
updated: 2026-08-01
status: active
confidence: medium
sources: ["[[the-new-sdlc-with-vibe-coding]]"]
---

# 指揮家與協調者

> 開發者與 AI 協作的兩種模式。同一個人一天內會在兩者間流動，
> 不是階梯，是**依任務選擇**。

## 兩種模式

| | 指揮家 conductor | 協調者 orchestrator |
|---|---|---|
| 節奏 | 即時 | 非同步 |
| 位置 | 在 IDE 裡看著程式碼出現 | 定義目標、指派、之後審查結果 |
| 控制粒度 | 每一個動作都在導引 | 只在檢查點介入 |
| 適合 | 複雜邏輯、除錯、不熟的程式碼庫 | 已知的 bug、既有模式下的功能、遷移、測試生成 |
| 工具 | Copilot、Gemini Code Assist、Cursor、Windsurf | Jules、Copilot agent mode、Cursor 背景 agent、Claude Code |
| 風險 | **人變成瓶頸**——每個按鍵都要導引的話，AI 帶來的吞吐量提升有限 | 品質失控，因為沒有逐行看 |

## 協調者需要的是不同的技能組

不是語法與語言慣用法的深度，而是：

1. **規格**：把任務定義到 agent 不會歧義的程度
2. **拆解**：把大任務切成適合 agent 執行的單位
3. **評估**：快速判斷產出有沒有到標準
4. **系統設計**：設計那些讓 agent 保持生產力的限制、測試與回饋迴圈

## 交叉比對

[[dave-rensin|Rensin]] 從完全不同的來源得到幾乎相同的結論——
「我們都是管理者了」，並建議 IC 現在就去上基礎管理課、從同時管 3–5 個 agent 開始。
兩份來源獨立收斂，這條的可信度比單一來源高。

## 相關頁面

- [[the-new-sdlc-with-vibe-coding]] —— 來源
- [[elephants-goldfish]] —— 獨立得到相同結論的另一份來源
- [[factory-model]] —— 兩種模式都在工廠模型底下
- [[judgment]] —— 兩種模式都在消耗同一種東西
