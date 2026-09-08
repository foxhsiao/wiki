---
title: 任務契約
type: concept
aliases: [task contract, 任務合約, acceptance contract]
tags: [ai, agent, harness, 工作方法]
created: 2026-09-08
updated: 2026-09-08
status: active
confidence: medium
sources: ["[[harness-engineering-complete-guide]]", "[[the-ai-native-sdlc-playbook]]"]
---

# 任務契約

> 在 agent 動手之前，把模糊的意圖轉成**五個問題有答案的結構**。
> 沒有契約，agent 最佳化的是「看起來像在做事」；有契約，它才能最佳化「被驗證的完成」。

## 五個問題

[[harness-engineering-complete-guide]] §2 的形式：

| 問題 | 欄位 |
|---|---|
| 什麼結果必須存在？ | `objective` |
| 什麼在範圍內？ | `scope` |
| 什麼不准動？ | `constraints` |
| 什麼證據證明完成？ | `acceptance` |
| 哪些動作需要人核准？ | `approval_required` |

原文的例子：

```yaml
objective: reduce onboarding drop-off
scope:
  - signup flow
  - onboarding analytics
constraints:
  - do not change authentication
  - preserve existing mobile behavior
acceptance:
  - tests pass
  - analytics event is emitted
  - screenshots cover desktop and mobile
approval_required:
  - production deployment
  - database migration
```

## 它改掉的是 agent 問自己的那句話

> "This changes the agent's question from: *What should I do next?*
> to: *What action moves the environment toward the contracted outcome?*"

> "Without a contract, the agent optimizes for **plausible activity**.
> With a contract, it can optimize for **verified completion**."

（推論）這兩句是本頁存在的理由。[[agent-autonomy-cost]] 記的失效模式——
過度驗證、範圍擴張——在契約的語言裡有更精確的名字：
**範圍擴張是 `scope` 沒寫，過度驗證是 `acceptance` 沒寫**。
自主性高的模型不是不受控，是在沒有終止條件的情況下自己補一個。

## 與 intent.md 的分工

[[intent-md]] 與本頁形狀相近但不是同一件事，混用會出問題：

| | [[intent-md]] | 任務契約 |
|---|---|---|
| 誰寫 | 提案者，**可以不是工程師** | harness，從請求編譯出來 |
| 寫給誰看 | 人，作為產物鏈（[[artifact-chain]]）的第一份產物 | agent，作為單次執行的邊界 |
| 生命週期 | 跨整個變更，迴圈閉合時回寫 | 一次 run |
| 缺什麼會怎樣 | 規格沒有來由，不知道為誰做 | agent 不知道什麼時候該停 |

（推論）兩者的關係是 intent 說「為什麼要做」，契約說「這一次做到哪裡算完」。
一份 intent 可以生出好幾份契約。本庫先前只有前者。

## 兩份來源在「誰定義驗收」上不一致

| 來源 | 驗收標準從哪來 |
|---|---|
| [[harness-engineering-complete-guide]]（2026-09-06） | harness 在動手前從請求編譯出來，agent 拿到即固定 |
| [[the-ai-native-sdlc-playbook]]（2026-08） | 由回饋迴圈與 eval suite（[[agent-config-evals]]）提供，**且 hook 擋住 agent 改測試** |

（推論）差別在**契約可不可以被執行者改**。前者沒有處理這件事——
一份寫在 prompt 裡的 `acceptance` 就是[[advisory-vs-deterministic-control|建議型控制]]，
agent 可以在中途重新解讀它。playbook 那句
「an agent fixing code must not be able to weaken the check on that code」
正是補這個洞。**契約要有效，得放在 agent 改不動的地方。**

## 一個很意外的同構

[[control-loops-human-and-agent]] 記的是：
[[dan-koe]] 給人用的年度重置協定，最後產出六件套——
anti-vision、vision、一年目標、一月專案、每日槓桿、**constraints**——
與本頁的五個欄位幾乎逐格對應，而且兩份來源在同一週進到本庫、互不知道對方。

（推論）這不構成任何證據，但它指出契約結構可能不是 agent 特有的，
而是**任何要在長時間跨度上維持方向的系統都會長出來的形狀**。

## 相關頁面

- [[harness-engineering-complete-guide]] —— 來源
- [[harness-engineering]] —— 契約是八欄位規格的第一欄
- [[intent-md]] —— 上游產物，不是同一件事
- [[completion-evidence]] —— `acceptance` 那一欄怎麼被判定
- [[agent-autonomy-cost]] —— 契約缺哪一欄對應哪一種失效模式
- [[advisory-vs-deterministic-control]] —— 契約寫在哪一層決定它有沒有強制力
- [[artifact-chain]] —— 契約在產物鏈裡的位置
- [[control-loops-human-and-agent]] —— 六件套與五欄位的同構
