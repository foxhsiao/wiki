---
title: 完成的證據
type: concept
aliases: [completion evidence, 驗收證據, verification asymmetry]
tags: [ai, agent, harness, 測試, 工作方法]
created: 2026-09-08
updated: 2026-09-08
status: active
confidence: medium
sources: ["[[harness-engineering-complete-guide]]", "[[the-ai-native-sdlc-playbook]]", "[[prompting-claude-opus-5]]"]
---

# 完成的證據

> agent 說「做完了」不是完成的證據，那只是**另一個模型輸出**。
> 完成只能由環境裡可觀察的改變決定。

## 主張換成證據

[[harness-engineering-complete-guide]] §7 的對照表，照抄：

| claim | evidence |
|---|---|
| "the bug is fixed" | failing test now passes |
| "the page works" | browser flow completed |
| "the migration is safe" | dry run and rollback pass |
| "the report is correct" | values match source data |
| "the task is complete" | every acceptance check passes |

檢查要**由便宜到貴**跑：syntax → types → focused tests → integration tests →
visual or semantic review → human approval。

原文最該記住的成本判準：

> "**Do not use another model where a compiler, schema, checksum, query, or test can answer the
> question.** Use models for ambiguity. Use code for plumbing."

（推論）這與 [[advisory-vs-deterministic-control]] 是同一刀的不同用法：
那一頁問「這個規則有沒有強制力」，這一頁問「這個判定該不該花模型的錢」。
兩題的答案都指向同一個方向——**能用確定性程式碼回答的，就不要問模型。**

## 驗證是嘗試否證，不是第二意見

§8 的核心是**職責不對稱**：worker 要造出最強的解，verifier 要找出它該被退回的理由。

> "If you ask the same agent, in the same context, to 'double-check its work,'
> it often **preserves the assumptions that created the mistake**."

> "Verification is not a second opinion. **It is an attempted disproof.**"

一個合格的驗證階段要有五件東西，其中最後一件本庫先前沒記過：

1. 明確的**拒絕**評分表（rejection rubric）
2. 拿得到產出的成品
3. 拿得到驗收契約（[[task-contract]]）
4. 需要時給它獨立的工具或全新脈絡
5. **有權拒絕而不必負責修好**（permission to reject without repairing）

[[the-ai-native-sdlc-playbook]] 從另一個方向補上同一件事的硬體版本：
用 hook 擋掉修 bug 的 agent 去編輯測試檔——

> "…an agent fixing code must not be able to weaken the check on that code."

（推論）兩份合起來是完整的：職責要分開（本節），
而分開之後還要有[[advisory-vs-deterministic-control|確定型控制]]保證它分得開。

（推論）第 5 點是本頁最實用的一格。一個既要挑錯又要負責修好的 verifier，
有動機把「這裡有問題」降級成「這裡我順手改了」——**於是拒絕不會被記錄下來**，
而拒絕的紀錄正是 [[agent-config-evals]] 用來調校的資料
（同一個道理在 [[autonomy-tiering]] 是「駁回要留理由」）。

## 恢復要對準失效類別

§10：最常見的恢復策略是「失敗了就再試一次」，而那不是恢復，是重複。

| 失效類別 | 對應動作 |
|---|---|
| tool timeout | 退避後重試 |
| invalid arguments | 修好那次工具呼叫 |
| missing context | 去取特定來源 |
| failed test | 檢查失敗的行為 |
| permission denied | 請求核准或改走安全路徑 |
| contradictory requirements | 升級給人 |
| **repeated unchanged failure** | **停止迴圈** |

> "**A retry should change at least one relevant condition.**
> Otherwise the system is paying to reproduce the same failure."

每個迴圈都要有預算：最大嘗試次數、最長時間、最高花費、最大破壞範圍、升級條件。

## change receipt：一次 run 留下的東西

§13 要求每次 run 結束編出一份小收據：OBJECTIVE / CHANGED / VERIFIED /
**NOT VERIFIED** / DECISIONS / RISKS / APPROVAL NEEDED。

> "The receipt is not a summary of what the model said.
> It is a summary of **what the system can prove**."

`NOT VERIFIED` 那一欄是本庫先前沒有的概念——**明確列出沒被證明的部分**，
而不是讓它消失在「完成」兩個字裡。

（推論）本庫 `Wiki/log.md` 的每一筆就是 change receipt 的同構物，
而且它缺的正好是這一欄：log 記「新增、更新、矛盾、新問題」，
沒有一欄記「這次沒有驗證到什麼」。

## 爭議與矛盾：驗證要加還是要減

這是本頁 `confidence` 不是 high 的原因。兩份來源方向相反，而且都不是弱來源。

| 來源 | 日期 | 主張 |
|---|---|---|
| [[harness-engineering-complete-guide]] | 2026-09-06 | 完成必須被證明；worker 之外要有獨立脈絡的 verifier |
| [[prompting-claude-opus-5]] | 2026-08-02 | 「為任何非瑣碎任務加入最終驗證步驟」在 [[claude-opus-5]] 上造成**過度驗證，浪費 token 且品質不變**；「用子 agent 驗證你的工作」同樣，而且**乘以委派成本** |

兩邊各有立場要扣分：前者匿名、零數據、賣的是方法論；
後者是供應商講自家模型，但講的是**對自己不利的方向**（叫你少做事、少花 token）。

**本庫目前的調和（推論）**，可能不對，要標明它是推論：
分歧點不在「要不要驗證」，在**驗證由誰執行**。
[[prompting-claude-opus-5]] 反對的是叫**模型再讀一次自己的輸出**——
那正是 §8 說會保留原有假設的那件事，兩份其實同意。
真正還沒解決的是子 agent：一份說它是必要的獨立脈絡，一份說它乘上委派成本而品質不變。

**要否證這個調和很容易**：跑同一組任務三種條件——無最終驗證、
同脈絡自我複查、獨立脈絡 verifier——比通過率與 token。
本庫沒有做過，也還沒有任何來源做過。

（另一個先前的區分見 [[harness-engineering]]：回饋迴圈跑遍整個任務、
次數由工作量決定；verifier 子 agent 只在 session 自認做完之後跑一次。
那個區分不消解上面的矛盾，只是縮小它的適用範圍。）

## 相關頁面

- [[harness-engineering-complete-guide]] —— 來源
- [[task-contract]] —— 驗收條款在契約裡，判定在這一頁
- [[harness-engineering]] —— 回饋迴圈與 verifier 的既有區分
- [[prompting-claude-opus-5]] —— 與本頁方向相反的那一份
- [[agent-config-evals]] —— 拒絕紀錄是它的輸入
- [[autonomy-tiering]] —— 「駁回要留理由」是同一個機制
- [[advisory-vs-deterministic-control]] —— 能用程式碼判定的就別問模型
- [[the-80-percent-problem]] —— 最難被證據抓到的正是概念錯
- [[harness-decay]] —— 汰除一個 verifier 的前提是知道它防過什麼
