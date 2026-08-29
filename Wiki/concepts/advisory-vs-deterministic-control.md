---
title: 建議型控制與確定型控制
type: concept
aliases: [advisory vs deterministic control, skill vs hook, 軟控制 硬控制]
tags: [ai, agent, 治理, 工作方法]
created: 2026-08-29
updated: 2026-08-29
status: active
confidence: high
confidence_note: 供應商對自家機制執行力的一手陳述（skill 不強制、hook 才強制），且是對自家產品的不利陳述
sources: ["[[the-ai-native-sdlc-playbook]]"]
---

# 建議型控制與確定型控制

> **skill 讓違規變罕見，hook 讓違規變幾乎不可能。**
> 必須永遠成立的政策，後面一定要墊一個確定性的東西。

## 供應商自己的話

[[the-ai-native-sdlc-playbook]] 對自家機制講得罕見地保守：

> "A skill is a control, though an advisory one. It makes Claude likely to apply the policy
> while the code is written, and **nothing forces a session to comply with it**.
> A policy that must always hold needs something deterministic behind the skill,
> such as a hook that blocks the action or a review pass that re-checks the policy at the PR.
> **The skill makes violations rare and the hook makes them close to impossible.**"

## 兩層的分工

| | 建議型（skill、`CLAUDE.md`、提示） | 確定型（hook、permissions、sandbox、branch protection） |
|---|---|---|
| 機制 | 模型讀到之後**傾向**遵守 | 程式碼在動作發生前執行，允許／詢問／阻擋 |
| 失效方式 | 沒觸發、脈絡被稀釋、文字與政策漂移 | 只在規則寫錯時失效 |
| 適用 | 慣例、風格、如何做得好 | 不能有例外的事：受保護路徑、憑證、生產部署 |
| 證據 | session 追蹤裡的 skill 呼叫紀錄 | 帶時間戳的允許／阻擋判定 |

原文對「政策擁有者」也分得很清楚：skill 由工程師照政策擁有者的權威來源寫，
政策改了就改 skill 並由政策擁有者簽核；不可協商的 hook 放在平台或 IT 管理的 managed settings，
**個別工程師關不掉**。

## 這對本庫既有頁面是修正

[[agent-skills]] 把 skill 描述成制度知識的載體，[[skill-design-patterns]] 的
**Inversion** 模式說它「靠不可協商的閘門指令運作」。這份來源指出那句話有問題：
寫在 SKILL.md 裡的閘門指令**不是不可協商的**，它只是很有說服力的建議。
真正不可協商的閘門是 hook。

（推論）五種 skill 模式裡，Reviewer、Inversion、Pipeline 都依賴閘門才成立，
所以三種都需要 hook 墊底才是控制，否則它們是設計良好的建議。

## hook 也分兩種，別放錯階段

| | build 期 hook | deploy 期 hook |
|---|---|---|
| 行為 | 無人介入地允許或阻擋 | **問人**，暫停到特定人核准 |
| 要求 | 快、只掃改動的那個檔案 | 阻擋時要說明理由與核准路徑 |
| 典型用途 | 擋受保護路徑、跑 formatter、擋憑證進 diff | 生產部署授權、變更管理簽核 |

原文的警告值得記住：把「要人核准」的 hook 放進 build 期，
等於把一個人放回**所有平行 session 的關鍵路徑**上。重的檢查（完整測試套件）屬於 commit 或 PR。

## 一個漂亮的應用：保護回饋迴圈本身

> "...an agent fixing code must not be able to weaken the check on that code."

修 bug 的任務裡，用 hook 擋掉對測試檔的編輯。
**一個在修復之前就存在、而且 agent 改不動的測試，才是 bug 消失的證明。**
替代方案是在審查時看 diff、退回任何動到測試的改動。

同一個原則的另一個面向：寫程式的 agent 沒有辦法核准自己的程式碼（branch protection），
職責分離因此被保住。

## 相關頁面

- [[the-ai-native-sdlc-playbook]] —— 來源
- [[agent-skills]] —— 被這一頁修正的對象
- [[skill-design-patterns]] —— 三種模式需要 hook 才算控制
- [[harness-engineering]] —— hook 是 harness 的確定性層
- [[autonomy-tiering]] —— 分級的邊界靠確定型控制強制
