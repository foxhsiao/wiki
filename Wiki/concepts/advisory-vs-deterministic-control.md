---
title: 建議型控制與確定型控制
type: concept
aliases: [advisory vs deterministic control, skill vs hook, 軟控制 硬控制]
tags: [ai, agent, 治理, 工作方法]
created: 2026-08-29
updated: 2026-09-08
status: active
confidence: high
sources: ["[[the-ai-native-sdlc-playbook]]", "[[harness-engineering-complete-guide]]"]
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

## 兩格其實是一道階梯的兩端

本頁的區分是二元的：建議型／確定型。
[[harness-engineering-complete-guide]] §11 把它撐成五格，而且中間三格是本頁原本沒有的：

```
explanation
  -> checklist
      -> template
          -> automated check
              -> enforced policy
```

原文給的規則是：**一條規則如果反覆重要，就把它往下搬。**

| 寫在提示裡的話 | 搬下去之後 |
|---|---|
| "use the formatter" | 自動跑 formatter |
| "do not import across layers" | 加一條架構測試 |
| "include a migration rollback" | CI 要求 rollback 檔存在 |
| "do not modify generated files" | 擋掉對 generated 路徑的寫入 |
| "cite every external claim" | 驗證引用覆蓋率 |

> "The prompt should explain judgment. The harness should enforce invariants."

（推論）中間三格對本庫是有用的補充，因為本頁原本的二分**逼人做全有全無的選擇**：
一條規則要嘛只是建議，要嘛得寫成 hook。實際上多數規則卡在中間——
它值得一個 checklist 或模板，但還不值得一段會 exit 1 的程式碼。
本庫的 `Wiki/_templates/` 正好落在第三格，而先前沒有被歸類過。

**本庫目前的分布**（推論，以 `CLAUDE.md` 的規則編號估）：
`[S1]`–`[S5]`、`[C1]`–`[C2]` 停在第一格；`[I3]` 的十個步驟是第二格；
`[N4]` 靠 `Wiki/_templates/` 是第三格、靠 `tools/lint.py` 是第四格；
`[K1]`、`[N5]`、`[N6]`、`[W8]` 在第四格。**第五格（動作發生前被擋下）本庫一條都沒有**——
`tools/lint.py` 是事後檢查，不是前置閘門。

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
- [[two-wiki-architectures]] —— 本庫新加的否決帳只擋得到格式，是這條區分的又一個實例
- [[managed-agents]] —— 把決定收回可控位置的另一個面向：成本與模型
- [[harness-engineering-complete-guide]] —— 把兩格撐成五格的來源
- [[completion-evidence]] —— 「能用程式碼判定的就別問模型」是同一刀的另一個用法
