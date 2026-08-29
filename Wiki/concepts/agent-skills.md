---
title: Agent Skills
type: concept
aliases: [skills, SKILL.md, progressive disclosure]
tags: [ai, agent, skill]
created: 2026-08-01
updated: 2026-08-29
status: active
confidence: high
sources: ["[[the-new-sdlc-with-vibe-coding]]", "[[agent-skill-design-patterns]]", "[[the-ai-native-sdlc-playbook]]"]
---

# Agent Skills

> 結構化、可攜的**程序性知識**包，agent 只在任務需要時才載入。
> 它讓 agent 維持輕量的通才狀態，按需展開成專才。

## 機制：progressive disclosure

三層揭露：

1. 啟動時只看到**輕量 metadata**（名稱與 description）
2. 任務匹配時載入**完整指令**（SKILL.md 本體）
3. 明確需要時才拉**深度參考資料**（`references/`、`assets/`）

結果是：一個 agent 可以攜帶數十種專門能力，但**只為當下實際用到的那一種付 token**。

## 它解決的四個問題

- 提示過載造成的 context rot
- LLM 缺乏程序性記憶
- 多 agent 架構的維運負擔
- 跨工具、跨廠商的可攜性

## 格式已經不是問題了

[[agent-skill-design-patterns]] 的起手主張：30 多種 agent 工具
（Claude Code、Gemini CLI、Cursor 等）已收斂到同一套佈局，**格式問題實務上已經過時**。
規格書說明怎麼打包，但**對裡面的邏輯該怎麼組織零指引**——
這才是現在的難題，答案見 [[skill-design-patterns]]。

## 在脈絡工程裡的位置

[[context-engineering]] 把 skill 定位為「管理動態脈絡最強的模式」——
它是靜態／動態那條界線上，把東西從昂貴的靜態側搬到便宜的動態側的主要工具。
成本面見 [[ai-development-economics]]。

## 但 skill 不是控制

[[the-ai-native-sdlc-playbook]] 對這件事講得很明白，而且是供應商自己說的：

> "A skill is a control, though an advisory one. ... **nothing forces a session to comply with it**."

skill 讓政策在程式碼被寫的當下就**很可能**被套用，但沒有任何東西強制 session 遵守它。
必須永遠成立的政策，後面要墊一個確定性的層：擋掉動作的 hook，或在 PR 再檢一次的審查回合。
**skill 讓違規變罕見，hook 讓違規變幾乎不可能。**（[[advisory-vs-deterministic-control]]）

這修正了把 skill 當成「制度知識即控制」的讀法。它是**制度知識的散布機制**，
散布很有效（改一次，所有人下一個 session 自動拿到新版），但它的執行力是機率性的。

實務上的判準，原文給了一句：
**要被一致套用的制度知識寫成 skill；屬於 `CLAUDE.md` 或屬於單次提示的東西不要寫成 skill。**

## 相關頁面

- [[skill-design-patterns]] —— skill 內容的五種設計模式
- [[context-engineering]] —— skill 在脈絡架構裡的位置
- [[agent-skill-design-patterns]] —— 來源
- [[the-new-sdlc-with-vibe-coding]] —— 來源
- [[advisory-vs-deterministic-control]] —— skill 的執行力有多強
- [[the-ai-native-sdlc-playbook]] —— 來源
