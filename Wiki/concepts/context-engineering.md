---
title: 脈絡工程
type: concept
aliases: [context engineering]
tags: [ai, 工作方法]
created: 2026-08-01
updated: 2026-08-29
status: active
confidence: high
sources: ["[[the-new-sdlc-with-vibe-coding]]", "[[prompting-claude-opus-5]]", "[[the-ai-native-sdlc-playbook]]", "[[metr-early-2025-ai-developer-productivity]]"]
---

# 脈絡工程

> AI 生成程式碼的品質，取決於**脈絡的品質**，不是提示的巧妙。
> 從「提示工程」到「脈絡工程」的轉向反映一件更深的事：
> 模型需要的不是被巧妙措辭誘導，是**跟一個稱職的人類開發者一樣的脈絡**。

## 六種脈絡

| 類型 | 內容 |
|---|---|
| Instructions | agent 的角色、目標、行為邊界 |
| Knowledge | 被檢索的文件、架構圖、領域資料 |
| Memory | 短期 session 記錄（剛剛發生什麼）＋長期狀態（這個專案是什麼） |
| Examples | few-shot 行為示範、程式碼庫裡的參考模式 |
| Tools | API、腳本、外部服務的精確定義 |
| Guardrails | 硬性限制、格式規則、安全驗證 |

## 靜態 vs 動態：真正的架構決策

- **靜態脈絡**永遠載入：系統指令、規則檔（`AGENTS.md`、`CLAUDE.md`、`GEMINI.md`）、
  全域記憶、人格定義。**昂貴**，因為每個 token 在每一次互動都在場，不管相不相關。
- **動態脈絡**按需載入：被任務匹配觸發的 [[agent-skills|skill]]、工具結果、
  RAG 取回的文件、視窗化的歷史。**有效率**，只在需要時付費。

太多靜態 → 浪費 token 且稀釋訊號；太少 → agent 忘掉關鍵規則。
最好的系統把這條界線當成**一級架構決策**，像其他設定一樣被審查與版控。

## 決定性的一問

> 「一個新來的隊友需要知道什麼才能有效貢獻，我怎麼把那份知識編碼成 AI 能用的形式？」

## 它同時是財務決策

在 token 經濟裡，脈絡工程不只是技術技能，是**財務槓桿**——
把 10 萬 token 的整個 repo 塞進每次提示，規模化之後在財務上不可行。
詳見 [[ai-development-economics]]。

## 靜態脈絡會折舊

這一頁把靜態／動態的界線描述成一個要被「審查與版控」的架構決策。
[[prompting-claude-opus-5]] 顯示這還不夠：靜態脈絡不只要考慮**成本**，還要考慮**保鮮期**。
規則檔裡的某些條目會隨模型換代從有用變成有害（[[prompt-obsolescence]]）。

版控保存了歷史，但不會告訴你哪一條已經過期——它需要的是每條規則的**存在理由**。

## 靜態脈絡的長度有一條具體建議

[[the-ai-native-sdlc-playbook]] 對 `CLAUDE.md` 給了本庫目前唯一的量化準則：

> **控制在一頁以內**，因為 Claude 在 session 開頭會全部讀完，任何過期內容都在白佔脈絡。

配套的維護規則同樣具體：**同一個錯誤犯第二次，修正就寫進 `CLAUDE.md`**；
審查發現重複出現的問題也往回寫進去。也就是說靜態脈絡該**只長在被證明需要的地方**，
而不是預先想像 agent 會犯什麼錯。

（推論）這跟本頁的「靜態昂貴、動態便宜」是同一件事的操作版：
一頁的上限強迫你不斷把東西從靜態側搬到 [[agent-skills|skill]] 或
[[artifact-chain|產物]]這些動態側。

## 產物鏈是刻意設計的動態脈絡

[[artifact-chain]]（`intent.md` → `spec.md` → `plan.md` → …）不只是治理設計，
也是脈絡設計：每個階段只讀上一份產物，而不是把整段歷史拖進視窗。
它同時解決了六種脈絡裡的 **Knowledge** 與 **Memory** ——
長期狀態不靠模型記得，靠檔案存在 repo 裡。

## 拿到了外部的實證支持

本頁的核心提問是「一個新來的隊友需要知道什麼才能有效貢獻，
我怎麼把那份知識編碼成 AI 能用的形式」。
[[metr-early-2025-ai-developer-productivity]] 從反面撞到了同一個點。

METR 五個造成拖慢的因子裡，第五個是
**Implicit repository context**，機制標註為「限制 AI 表現，**同時**拉高人類表現」——
AI 缺少資深開發者仰賴的隱性程式碼庫知識。討論段更具體：

> AI 的能力在品質標準很高、或**有很多隱性要求**（文件、測試覆蓋率、lint／格式）
> ——那些人類要花很多時間才學會的東西——的場景相對更低。

那正是規則檔、[[agent-skills|skill]] 與 [[artifact-chain|產物鏈]]在編碼的東西。

這個支持比表面上更有份量，理由是**證據的方向**：
不是廠商說「用我們的脈絡工具會更好」，是一個沒有產品要賣的第三方
（[[metr|METR]]）在解釋**失敗**時指到同一個地方。

（推論）但要誠實界定它證明了什麼：METR 指認隱性脈絡是瓶頸，
**沒有測試過「把它寫成檔案會不會改善」**。前半有實證，後半仍是本庫的賭注。

## 與本知識庫的關係

（推論）這個庫的 `CLAUDE.md` 正是白皮書點名的那種靜態脈絡檔；
`Wiki/index.md` 是刻意做出來的動態脈絡入口——先讀索引再決定載入哪幾頁，
就是 progressive disclosure 的手動版。這條讓 `CLAUDE.md` 的長度變成一個可以被檢討的成本項。

## 相關頁面

- [[the-new-sdlc-with-vibe-coding]] —— 來源
- [[agent-skills]] —— 管理動態脈絡最強的模式
- [[harness-engineering]] —— 脈絡是 harness 的一部分
- [[ai-development-economics]] —— 脈絡的成本面
- [[vibe-coding-spectrum]] —— 脈絡工程是走向紀律那端的橋
- [[prompt-obsolescence]] —— 靜態脈絡的保鮮期問題
- [[the-ai-native-sdlc-playbook]] —— `CLAUDE.md` 一頁以內的準則
- [[artifact-chain]] —— 用產物承載跨階段的記憶
- [[metr-early-2025-ai-developer-productivity]] —— 隱性脈絡是瓶頸的實證
- [[what-the-19-percent-measures]] —— 這份支持的邊界
