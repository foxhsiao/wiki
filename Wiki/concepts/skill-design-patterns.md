---
title: Skill 設計的五種模式
type: concept
aliases: [skill design patterns, Tool Wrapper, Generator, Reviewer, Inversion, Pipeline]
tags: [ai, agent, skill, 工作方法]
created: 2026-08-01
updated: 2026-08-29
status: active
confidence: high
sources: ["[[agent-skill-design-patterns]]", "[[prompting-claude-opus-5]]", "[[the-ai-native-sdlc-playbook]]"]
---

# Skill 設計的五種模式

> 從 Anthropic 的 repo、Vercel 與 Google 內部指引裡歸納出的五種反覆出現的結構。
> 兩個 SKILL.md 從外面看一模一樣，裡面可以是完全不同的東西——差別就在這五種。

## 五種

### 1. Tool Wrapper —— 讓 agent 秒懂某個函式庫

最簡單的一種。SKILL.md 監聽提示裡的特定關鍵字，
動態載入 `references/` 裡的內部文件，並把那些規則**當成絕對真理**套用。

用途：把團隊的內部編碼規範或框架最佳實務，直接送進開發者的工作流程。
關鍵設計：明確指示 agent「**只在**開始審查或撰寫程式碼時才載入 `conventions.md`」。

### 2. Generator —— 讓每次產出格式一致

Tool Wrapper 套用知識，Generator 強制輸出一致。
用兩個目錄：`assets/` 放輸出模板，`references/` 放風格指南。
指令本身像個專案經理：載入模板 → 讀風格指南 → **向使用者要缺少的變數** → 填空。

關鍵設計：SKILL.md 裡**不放**實際版面或文法規則，它只協調那些資產的取用。

### 3. Reviewer —— 把「檢查什麼」和「怎麼檢查」分開

檢查表存在 `references/review-checklist.md`，指令保持靜態。
換掉 checklist（Python 風格 → OWASP 資安），同一套基礎設施就變成完全不同的稽核。

關鍵設計：強制**按嚴重度分組**輸出（error／warning／info），
並要求解釋**為什麼**是問題，不只是哪裡有問題。

> **[[prompting-claude-opus-5]] 對這個模式的修正**：checklist 裡不要寫
> 「只回報高嚴重度問題」或「保守一點」——模型會照字面遵守而**少報真問題**。
> 該叫它**全部回報，再用另一輪去過濾**。過濾屬於管線的下一步，不屬於審查那一步。

### 4. Inversion —— agent 先訪談你再動作

agent 天生想立刻猜、立刻生成。這個模式把關係倒過來：agent 當訪談者。

靠**不可協商的閘門指令**運作，例如「所有階段完成前，不准開始建造」。
一次問一個問題、等答案、再進下一階段；在拿到完整需求圖像前拒絕綜合出最終產出。

> **這和 [[ai-as-interrogator]] 是同一件事。**
> [[dave-rensin|Rensin]] 從實務經驗描述它、[[shubham-saboo|Saboo]] 把它歸納成模式，
> 兩份來源獨立命名同一個結構——這條的可信度因此高於單一來源。

### 5. Pipeline —— 強制多步驟不被跳過

指令本身就是工作流程定義。用**明確的閘門條件**
（例如未經使用者確認 docstring 就不得進入組裝階段），
確保 agent 不能繞過複雜任務直接端出未驗證的成品。

這個模式會用到所有可選目錄，但**只在需要的那一步才拉對應的參考檔與模板**，保持脈絡視窗乾淨。

> **[[the-ai-native-sdlc-playbook]] 對這個模式的修正**：寫在 SKILL.md 裡的
> 「不可協商的閘門指令」**其實是可以協商的**——供應商明說沒有東西強制 session 遵守 skill。
> 真正不可協商的閘門是 hook。Inversion 要成為控制而不只是設計良好的建議，
> 需要一個確定性的東西墊底。見 [[advisory-vs-deterministic-control]]。

## 選哪一種

每種模式回答不同的問題：

| 你的問題 | 用 |
|---|---|
| agent 不懂我們的技術棧慣例 | Tool Wrapper |
| 每次產出的結構都不一樣 | Generator |
| 我要按一份標準評分 | Reviewer |
| agent 沒問清楚就開始做 | Inversion |
| agent 會跳步驟 | Pipeline |

## 模式會組合

不互斥。Pipeline 尾端可以掛 Reviewer 自我複查；
Generator 開頭可以用 Inversion 先收集變數。

## 哪幾種需要 hook 墊底

（推論）五種模式裡有三種的效力**完全建立在閘門上**：
Reviewer 要求按嚴重度輸出、Inversion 要求問完才動作、Pipeline 要求不得跳步。
三者若沒有確定性的東西在後面，都是很有說服力的建議而不是控制。

Tool Wrapper 與 Generator 不同——它們影響的是產出品質而非合規邊界，
建議型控制對它們夠用。

## 與本知識庫的關係

（推論）這個庫的 `CLAUDE.md` 現在混用了三種：
ingest 流程是 **Pipeline**（十個步驟、有檢查點）、
頁面模板是 **Generator**、
lint 那一節是 **Reviewer**。
唯一缺的是 **Inversion**——ingest 流程第 2 步「回報重點等使用者確認」是很弱的版本，
沒有不可協商的閘門。這是一個可以直接改進的地方。

## 相關頁面

- [[agent-skills]] —— skill 這個機制本身
- [[ai-as-interrogator]] —— 與 Inversion 是同一個模式
- [[agent-skill-design-patterns]] —— 來源
- [[shubham-saboo]] —— 歸納者
- [[prompting-claude-opus-5]] —— Reviewer 模式的一條具體修正
- [[advisory-vs-deterministic-control]] —— 三種模式需要 hook 才算控制
- [[the-ai-native-sdlc-playbook]] —— Inversion 閘門的修正
