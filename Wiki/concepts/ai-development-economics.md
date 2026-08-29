---
title: AI 開發的經濟學
type: concept
aliases: [CapEx OpEx, token economy]
tags: [ai, 軟體工程, 經濟]
created: 2026-08-01
updated: 2026-08-29
status: active
confidence: medium
sources: ["[[the-new-sdlc-with-vibe-coding]]", "[[the-ai-native-sdlc-playbook]]"]
---

# AI 開發的經濟學

> 速度不是重點，**總持有成本**才是。兩種工作方式把負擔推到不同的地方。

## 兩種成本結構

| | Vibe coding | Agentic engineering |
|---|---|---|
| CapEx（前期投入） | 幾乎為零——靠模型的基線能力 | 高——設計 API schema、建確定性測試套件、結構化脈絡 |
| OpEx（持續成本） | **高且複利** | 低——邊際交付與維護成本大幅下降 |

## Vibe coding 的三筆隱藏債

1. **Token 燃燒率**：把大而無結構的檔案倒進脈絡視窗，反覆要模型修它自己未驗證的錯誤。
   這個「提示迴圈」在**低首次成功率**下燒 token。
2. **維護稅**：缺乏結構一致性。六個月後出 bug，工程師要花好幾天逆向工程 AI 生成的義大利麵。
3. **資安補救**：沒有自動化評估 harness，快速生成程式碼等於快速生成漏洞。
   生產環境修一個資安缺陷的成本，比設計階段抓到高出指數級。

## 三個壓低 OpEx 的槓桿

1. **[[context-engineering|脈絡工程]]作為財務策略**：給密度高、訊噪比高的 payload
   （精確的 `AGENTS.md` 與架構護欄），而不是龐雜的雜訊，直接拉高**首次成功率**。
2. **動態脈絡與 [[agent-skills|skills]]**：只為當下用到的能力付 token。
3. **智慧模型路由**：複雜任務（需求、架構、初步實作）走大模型；
   確定性的低複雜度任務（測試生成、程式碼審查、CI/CD 監控）自動路由到更小更快更便宜的模型。

## CapEx 不是一次性的

本頁把 harness 算成前期投入換低 OpEx。兩份後續來源都在拆這個假設：

- [[prompt-obsolescence]]：規則檔會隨模型換代折舊，有些條目從資產變成負債。
- [[the-ai-native-sdlc-playbook]]：維持它需要**持續支出**，而且原文自己標出了成本項——
  [[agent-config-evals|eval suite]] 要有預算跑（20–50 條、非互動跑真實 session、
  每次改設定與每日排程各跑一次）、每個事故要有人寫一條新 eval、
  Claude Security 的排程掃描按用量計費且要求設定支出上限。

（推論）比較誠實的算法是 **CapEx + 持續 OpEx**：
harness 是資產，但它有折舊、有保養費，而保養費隨 repo 數與事故數成長。
原文留的出口是「有些團隊可能偏好照固定週期離線跑 eval，而不是每次改動都跑」——
也就是**用鑑別度換成本**。

## 判讀

（推論）這一節是白皮書裡最像賣點的部分——三個槓桿剛好都指向 Google 的產品線。
但 CapEx／OpEx 的框法本身站得住，而且它給了一個很實用的檢查問題：
**你現在的做法，成本是被推到前面還是被推到六個月後？**

「首次成功率」值得當成可量測的指標追蹤，白皮書沒給任何實際數字。

## 相關頁面

- [[the-new-sdlc-with-vibe-coding]] —— 來源
- [[context-engineering]] —— 最大的那根槓桿
- [[agent-skills]] —— 動態脈絡的載體
- [[vibe-coding-spectrum]] —— 成本結構對應光譜位置
- [[the-ai-native-sdlc-playbook]] —— harness 的持續成本項
- [[agent-config-evals]] —— 最主要的那筆持續支出
- [[prompt-obsolescence]] —— 折舊那一面
