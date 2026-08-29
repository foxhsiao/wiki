---
title: 5 Agent Skill Design Patterns Every ADK Developer Should Know
type: source
aliases: [五種 Skill 設計模式]
tags: [ai, agent, skill, 工作方法]
created: 2026-08-01
updated: 2026-08-01
status: active
confidence: high
source_type: article
author: Shubham Saboo、Lavi Nigam（Google Cloud Tech）
published: 2026-03-18
url: https://x.com/GoogleCloudTech/article/2033953579824758855
raw: "[[2026-08-01--agent-skill-design-patterns]]"
ingested: 2026-08-01
---

# 5 Agent Skill Design Patterns Every ADK Developer Should Know

> 格式問題已經解決了——30 多種 agent 工具都收斂到同一套 SKILL.md 佈局。
> 剩下的問題是**內容設計**：規格書告訴你怎麼打包，完全沒告訴你裡面的邏輯該怎麼組織。

## 核心主張

- 開發者過度執著於格式（YAML、目錄結構、規格），但格式已經標準化，那不再是問題。
- 兩個 SKILL.md 從外面看一模一樣，裡面的運作邏輯可以完全不同——
  包 FastAPI 慣例的 skill 和四步驟的文件產線，是兩種東西。
- 從 Anthropic 的 repo、Vercel、Google 內部指引裡歸納出**五種反覆出現的模式**。
- **模式可以組合**：Pipeline 尾端可以掛 Reviewer 自我複查；Generator 開頭可以用 Inversion 收集變數。
- 靠 ADK 的 SkillToolset 與 progressive disclosure，agent 只為當下用到的那個模式付 token。

## 五種模式

詳見 [[skill-design-patterns]]。摘要：

| 模式 | 回答的問題 | 機制 |
|---|---|---|
| Tool Wrapper | 怎麼讓 agent 秒懂某個函式庫 | 關鍵字觸發載入 `references/`，把規則當絕對真理 |
| Generator | 怎麼讓每次產出格式一致 | `assets/` 放模板、`references/` 放風格指南，填空 |
| Reviewer | 怎麼按檢查表評分 | 把「檢查什麼」抽成外部 checklist，按嚴重度分組輸出 |
| Inversion | 怎麼讓 agent 先訪談再動作 | 不可協商的閘門指令：「所有階段完成前不准開始建造」 |
| Pipeline | 怎麼強制多步驟不被跳過 | 硬檢查點，例如未經使用者確認不得進入下一步 |

## 值得引用的原文

> "The specification explains how to package a skill, but offers zero guidance on how to
> structure the logic inside it."

> "Stop trying to cram complex and fragile instructions into a single system prompt."

## 對 wiki 的影響

- 新增：[[skill-design-patterns]]、[[agent-skills]]、[[shubham-saboo]]
- **重要連結**：Inversion 模式與 [[ai-as-interrogator]] 是同一件事被兩份來源獨立命名
- 與 [[the-new-sdlc-with-vibe-coding]] 同一作者群，且後者把 skill 放進 [[context-engineering]] 的框架裡

## 我的判讀

（推論）這篇的價值在**分類本身**，不在 ADK。五種模式與工具無關，換成任何 SKILL.md 相容的 agent 都成立。
最弱的是「30 多種工具已標準化」這句沒有出處。
最有用的是「模式可組合」那一段——它把 skill 從「一份 prompt」提升成可組裝的元件。

## 相關頁面

- [[skill-design-patterns]] —— 五種模式的完整拆解
- [[agent-skills]] —— skill 這個機制本身
- [[ai-as-interrogator]] —— 與 Inversion 模式重合
- [[shubham-saboo]] —— 共同作者
