---
title: 兩種 wiki 架構
type: synthesis
aliases: [WikiSkill vs 本庫, two wiki architectures]
tags: [ai, agent, 知識庫, 架構, 論點]
created: 2026-09-01
updated: 2026-09-01
status: active
confidence: medium
sources: ["[[wikiskill]]"]
---

# 兩種 wiki 架構

> [[wikiskill]] 的三層與這個知識庫的三層長得幾乎一樣，
> 但**迴圈的驅動力完全不同**——它從自己的失敗學，本庫從別人的文章學。
> 其餘所有差異都是這一條的下游。

## 對得上的部分

| | WikiSkill | 本庫 |
|---|---|---|
| 不可變層 | `raw/` 執行軌跡 | `Raw/` 原始來源（`[L1]`） |
| 知識層 | `wiki/patterns/` + `index.md` + `logs.md` | `Wiki/` + `index.md` + `log.md` |
| 程序層 | `skills/` + `PURPOSE.md` | `.claude/skills/` + `CLAUDE.md` + `.claude/rules-ledger.md` |
| 索引先行 | Skill Proposer 先讀索引，再按需 `read_file` 取 pattern 與軌跡 | `[W0]`／`[W3]` 先讀 `index.md` 再進內文 |
| 增量編輯 | pattern 頁用 append／replace／insert_after，不整頁重寫 | 擴散更新時在既有頁加節，不覆寫 |

`PURPOSE.md` 把每個 skill 反指回啟發它的 pattern，
與 `.claude/rules-ledger.md` 記規則來由是同一個動作（[[open-questions]] Q10）。

這個相似不是巧合：那篇論文明說靈感來自 Karpathy (2026) 的「LLM Wiki」觀點——
把經驗編譯成持久、會複利的知識。本庫是同一個想法的手工版。

## 對不上的部分

| 面向 | WikiSkill | 本庫 |
|---|---|---|
| 迴圈由什麼觸發 | **任務失敗**——對失敗軌跡做根因分析 | **使用者丟一份新來源** |
| `raw/` 裡是什麼 | 自己的執行軌跡 | 第三方文獻 |
| 知識從哪來 | 內省：自己踩到的坑 | 外部：別人寫的東西 |
| 產物是什麼 | 可執行的 skill | 可被查詢的理解 |
| 怎麼知道有沒有變好 | 驗證集分數，有 ground truth | **沒有辦法**；`tools/lint.py` 只驗形式 |
| gating | 分數沒超過歷史最佳就整包回滾 | lint 全綠 + 使用者 review PR |
| 誰能讀知識層 | 執行任務的 agent **被禁止**讀 | 執行者每次 session 開場就讀（`[W0]`） |
| 回滾的切法 | 程序可回滾、知識永不回滾 | 保留型 vs 維護型（`[L5]`） |
| pruning | 沒有（作者自列為限制） | 沒有（靠人工健檢） |

## 三個值得停下來的差異

### 1. 沒有分數，所以閘門長在別的地方

WikiSkill 整個設計繞著一件事轉：**有 ground truth**，所以每次改動都能被判定為改善或退步。
它的接受率是每輪提 3.1 個 skill、只收 1.6 個（[[agent-config-evals]]）。

本庫沒有這東西。wiki 頁面沒有「答對率」，所以閘門只能是形式（`tools/lint.py`）加人。
這不是本庫做得比較差，是**產物不同**——但代價是真的：
[[open-questions]] Q15 至今只有一筆 n=1 的觀察，而那份研究每個設定跑三次、附信賴檢定。

（推論）這也解釋了為什麼本庫的確定性閘門全部長在**形式**那一側
（frontmatter、斷鏈、計數、來由缺漏）。形式是唯一不需要 ground truth 就能判定的東西。

### 2. 回滾的刀切在不同軸上

- WikiSkill 切「**可逆 vs 不可逆**」：skill 隨時可能被退回上一版，知識永不回滾。
- 本庫的 `[L5]` 切「**描述事件 vs 描述當前狀態**」：`log.md` 只增不改，`Wiki/` 頁面隨現況改寫。

差別在於：**本庫的知識層是會被改寫的，它的不會。**

本庫的作法能修掉錯誤——例如 2026-08-29 那次對 METR 的誤讀
（[[what-the-19-percent-measures]]）。代價是改寫過程中「我原本怎麼想」會消失，
只留下一句「本頁先前寫……那是誤讀」。

（推論）兩種切法各自遺失一種東西：它遺失的是「當下最好的版本長什麼樣」，
本庫遺失的是「走到這裡的路徑」。本庫用 `log.md` 補回一部分，但 log 記的是動作，不是想法。

### 3. `[W0]` 可能違反了那個 ablation

WikiSkill 的預設設定**禁止執行任務的 agent 讀知識層**，因為給它讀會掉分
（63.7% → 60.9%）。假說是：agent 直接從 wiki 拿到解法，
於是產生的軌跡對改進程序的資訊量下降（[[context-engineering]]）。

本庫的 `[W0]` 規定每次 session 開場先讀 `index.md` 與 log 尾巴——**正好是它禁止的那件事**。

**但這個類比不成立，理由有兩個**：它的系統裡執行者與知識維護者是**不同的 agent**，
本庫兩者是同一個；本庫也沒有訓練／驗證之分，沒有「軌跡」這種東西。
所以 2026-09-01 決定**不改 `[W0]`**，紀錄在 `.claude/rejected-proposals.md`。

（推論）真正可移植的是**順序而非禁止**：
如果在讀原文之前就先讀了本庫既有的結論，「原文讓我改變想法」的時刻會變少。
2026-09-01 那兩份 ingest 都是先讀完原文才回頭比對既有頁面——
那個順序可能比 `[W0]` 的字面更重要。

## 本庫照著補的那一格

比對之後本庫明確缺一樣東西：**試過、被否決、為什麼不做**。

`log.md` 記做了什麼，`rules-ledger` 記被採用的規則為什麼在，兩者都不記被丟掉的東西。
對應 WikiSkill 的 `skill-impact.md`，它把每個被拒提案的 diff 與分數留在永不回滾的那一層，
用途明寫是「rejected interventions are not proposed again」。

2026-09-01 已補上：規則 `[W9]`、帳在 `.claude/rejected-proposals.md`、
`tools/lint.py` 加 `[否決帳]` 格式檢查、`tools/test_lint.py` 加兩種突變。
建檔時回填 6 筆，最舊的一筆（Q9 的 Inversion 閘門）在建檔前已被重複討論過兩次。

**但要誠實講這道閘門的極限**：lint 驗得到格式，驗不到「否決了卻沒記」。
那一半仍然是建議型控制（[[advisory-vs-deterministic-control]]），
靠健檢時人工比對——這正是 [[open-questions]] Q13 說的那種「成功與停止量測長得一樣」的指標。

## 這份比對本身能主張什麼

（推論）不能主張本庫的架構「被驗證了」。那份研究測的是它自己的系統，
不是本庫；而且是 benchmark 答對率，不是知識庫品質
（[[evidence-types-for-ai-capability]]）。

能主張的是比較弱的一句：**一個獨立團隊在完全不同的目標下，
收斂到了幾乎相同的三層切法，而且用 ablation 顯示中間那層值 15.0 分。**
這對本庫的設計是側面支持，不是證明。

## 相關頁面

- [[wikiskill]] —— 被比對的另一方
- [[persistent-knowledge-layer]] —— 它那一側的設計細節
- [[skill-transfer-across-models]] —— 同一份研究的另一個結果
- [[context-engineering]] —— 「誰該讀到」那條差異的所在
- [[agent-config-evals]] —— 有無 ground truth 造成的閘門差異
- [[advisory-vs-deterministic-control]] —— 新閘門只擋得到形式
- [[open-questions]] —— Q13、Q15 與這份比對的關係
- [[what-the-19-percent-measures]] —— 本庫改寫知識層的一次實例
