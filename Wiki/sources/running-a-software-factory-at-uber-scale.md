---
title: "Running a Software Factory Efficiently at Uber Scale"
type: source
aliases: [Uber Software Factory, Uber 成本優化]
tags: [ai, agent, 成本, 組織, 軟體工程]
created: 2026-09-01
updated: 2026-09-01
status: active
confidence: high
source_type: article
author: "@udaykiran（Uber Engineering）"
published: 2026-08-29
url: https://x.com/UberEng/status/2093444169037762840
raw: "[[2026-09-01--running-a-software-factory-at-uber-scale]]"
ingested: 2026-09-01
---

# Running a Software Factory Efficiently at Uber Scale

> Uber 把 agent 用量做到 70% 以上的 PR 由 agent 產出之後，**怎麼讓成本不跟著漲**。
> 本庫**第一份買方視角**的來源——它不賣 agent 工具，它在付錢買，
> 而且是第一份帶真實世界 harness 效果數字的。

## 核心主張

- **成本是可分解、可逐項優化的工程問題**，不是靠殺價或降級工具解決的。
  一次 agent session 的花費被拆成六項相乘的因子，各自量測、各自優化。
- **要隔離「自己的優化」的效果，就必須固定模型**，因為每次模型升級行為都會變。
- 最大的優化空間在**中間三項**——「agent 在工程師實際提出的請求之上，自己給自己加的工作」。
- 工具 schema 是一種脈絡稅，而且是預付的：不管用不用，開場就在脈絡裡（[[context-tax]]）。
- 結論是一個方向性的轉移：**從互動式開發者工作流，轉向受管 agent**（[[managed-agents]]）。

## 關鍵事實與數據

**規模（2026-08 當期）**

| 項目 | 數值 |
|---|---|
| 由本機或雲端 agent 產出的 PR | **超過 70%** |
| 已建的 agent skill | **超過 3,600 個** |
| 每日 agent skill 執行次數 | **超過 30K** |
| 週活躍使用者成長（2026-02 → 08，含非工程師） | **7 倍** |
| 每週 agentic requests 成長（同期） | **9.4 倍** |
| 總 AI 支出 | 自 4 月起「相對持平」 |

**成本優化（固定模型，2026-02 → 07）**

| 指標 | 變化 |
|---|---|
| cost per 1,000 model requests | 自高點下降**將近 34%** |
| cost per session | 自 6 月高點下降 **52%** |

原文對方法的說明是本庫最該記住的一句，見〈值得引用的原文〉。

**工具 schema 的開銷**

| 項目 | 數值 |
|---|---|
| 內部 MCP gateway 後面的 MCP server | 超過 1,000 個 |
| 裝了 100+ 工具時的 schema 開銷 | **約 50K–70K tokens**，且每一輪重送 |
| 某 workspace 套件單一 server | 49 個工具、約 **22K tokens** schema |
| 某訊息軟體／某專案追蹤軟體 | 34 個／46 個工具 |
| code-mode 對比標準 MCP（5 個相同 SQL 查詢） | 即使結果集極小也**省超過 50%**；批次工作**超過 90%** |
| 已預建的 code-mode skill | 超過 25 個 |

**AI Context Graph**

| 項目 | 數值 |
|---|---|
| 節點／邊 | **2,400 萬／8,000 萬** |
| 節點型別／邊型別 | **86 種／117 種** |
| 整合的內部系統 | 超過 30 個（服務、團隊、事故紀錄、PR、架構設計文件、部署、資料集、歷史查詢） |

同一個提示、同一個模型的對照（Figure 10）：

| | 有 graph grounding | 無 |
|---|---|---|
| 時間 | **38 秒** | **20 分鐘** |
| 過程 | 查歷史用量，找到 50 位以上分析師使用的那張表 | 翻 service code、生成 2 個 subagent、撞上 3 個錯誤 |
| 結果 | 答對 | **結論是該資料集無法查詢——錯的** |

**艦隊級預設值**

- **自動壓縮在 400K tokens 觸發，即使是 1M 視窗的模型**（平衡模型表現與 cache burst、重複輸入成本）。
- **reasoning effort 預設 Medium**（輸出與內部推理 token 的計價是輸入的數倍）。
- **prompt cache TTL 從 5 分鐘改為 1 小時**；subagent 維持 5 分鐘。
  快取讀取是標準輸入價的 **0.1 倍**；5 分鐘寫入 **1.25 倍**、1 小時寫入 **2 倍**。
  可選 TTL：Anthropic 5 分鐘與 1 小時、OpenAI 30 分鐘。
- **subagent 預設用較弱、較便宜的模型**，主模型負責任務拆解與評估，subagent 執行。

**可見度機制**

- 狀態列即時顯示本次 session 與跨 harness 的累計花費。
- 共用花費層級（所有互動式 harness 一個池，受管 agent 另計），
  在 **50/80/100%** 發 Slack 提醒，主管核准可升級層級。
- Session 分析儀表板內建於 runtime、免設定，掃過所有 session trace，
  標出 **16 種 anti-pattern**，每種附財務影響與具體修法
  （例：Sonnet 就能做的事跑在 Opus 上、40KB 的 MCP 回應留在脈絡裡被反覆計費、
  中斷太久導致 cache 過期要全價重建前綴、還沒輸入就先載入 10 萬 token 的系統指令與工具定義）。

## 值得引用的原文

方法學那句——本庫先前沒有任何來源這樣講：

> "Since adoption, workload mix, and model upgrades are all continuously changing, **isolating our
> own optimization gains means holding one model fixed, since behavior shifts with every upgrade
> and model family**."

成本方程式中間三項是什麼：

> "The three middle terms provide opportunities for optimization: **the work the agent does on its
> own behalf, on top of the request an engineer actually made**. That is where most of our effort goes."

為什麼 grounding 是最強的槓桿：

> "**An ungrounded agent fails slowly rather than cheaply**, repeatedly sending an expanding context
> window to search one more location."

SaaS MCP 的結構性問題：

> "Vendors design MCP servers to expose full product capabilities because they can't anticipate
> specific customer usage. … Loading two or three vendor servers makes the agent **carry more schema
> overhead than the file being edited** before a user even enters a prompt."

結論的方向：

> "The core strategic shift is **moving from interactive developer workflows to fully managed agents**.
> … Optimizing a fleet of specialized managed agents, each paired with dedicated evaluation
> benchmarks and a Pareto-efficient model, is inherently more cost-effective and scalable than
> optimizing individual terminal sessions across thousands of engineers."

進行中的工作裡，有一條與本庫三天前 ingest 的論文是同一件事：

> "**Continuous Skill Improvement**: We are working on an automated way to record papercuts from
> agent skill executions and **auto-generate skill updates from the collected traces**."

## 原檔的缺漏（重要）

全文的圖都是外部 `pbs.twimg.com` 連結，**一張都沒有抓下來**。受影響的內容：

- **Figure 4：成本方程式的六個項**——內文只交代「前兩項是採用與參與、中間三項是
  agent 自己給自己加的工作」，**六項分別是什麼只存在於圖裡**。
  本頁不猜（`[X2]`）。從各節標題可見至少包含 price/token、tokens/request、requests/turn 三項，
  但它們是不是「中間三項」、其餘兩項是什麼，無法確認。
- **Figure 3：四層 agent 使用架構**——只知道「愈上層對成本、品質、模型選擇的控制力愈強」，
  四層各是什麼看不到。
- 每週／每月追蹤的**指標總表**、**optimization levers 總表**、
  uReview 的 Pareto 圖（Figure 5）、code-mode 的 token 對照表、
  cache TTL 五輪對照（Figure 6）、成本儀表板（Figure 12）——全部只有圖。

（推論）缺的是**數字的細節**，不是主張。上面〈關鍵事實與數據〉裡的每一個數字都出自內文，
不是從圖裡讀的。

## 對 wiki 的影響

- 新增：[[uber]]（seed）、[[context-tax]]、[[managed-agents]]
- 更新：[[ai-development-economics]] —— 成本從 CapEx／OpEx 的定性說法變成可分解的量測
- 更新：[[context-engineering]] —— METR 因子 5 的「解法端」第一次有人做出來（AI Context Graph）
- 更新：[[harness-engineering]] —— 本庫第一份真實世界的 harness 效果數字
- 更新：[[effort-and-thinking]]、[[agent-autonomy-cost]] —— 艦隊級預設值的實作
- 更新：[[agent-skills]] —— 3,600 個 skill 的規模，以及 skill 自動演化的產業版
- 更新：[[agent-config-evals]] —— benchmark 驅動的模型選擇是同一套機制換一個對象
- 更新：[[wikiskill]] —— 它的方法有人在產線上做
- 更新：[[open-questions]] Q15、[[overview]] 的缺口清單（買方視角補上了）
- 衝突：無正面衝突。

## 我的判讀

（推論）這是本庫目前**營運資料最紮實**的一份，理由有三：

1. **立場對了**。前十三份來源全是賣方（Google、Anthropic、DeepLearning.AI）、
   研究方（METR、Lindgren、Bainbridge）或個人。Uber 是第一個**付錢的一方**，
   而它的動機是把成本壓下來——這個方向的偏誤與賣方相反。
2. **方法講清楚了**。「固定模型才能隔離自己的優化」這句是本庫收過最好的方法學自覺之一，
   而且它承認 adoption、workload mix、模型升級三者同時在動。
3. **原文自己畫了界線**：「specific cost reductions we measure are unique to our environment
   and your mileage may vary」，可移植的是方法不是數字。

要打的折同樣明確：

- **自陳，未經稽核**。這是一篇工程部落格，目的包含展示能力與招募。
  沒有第三方驗證，也沒有失敗案例——通篇每個槓桿都有效。
- **成功的定義是成本**，不是產出品質。文中說「improving/maintaining output quality」，
  但**沒有給任何品質數字**（uReview 的 F1 是模型選擇的指標，不是全公司產出的指標）。
  所以它證明的是「用量成長 7 倍而單位成本下降」，不是「產出變好」。
- **規模極端**。1,000+ MCP server、數億行程式碼、2,400 萬節點的 graph——
  這些槓桿在小團隊的成本效益完全不同。

（推論）對本庫最有用的不是那些數字，是**它把成本變成可分解的量測**這件事本身。
[[open-questions]] Q15 問「好的 harness 能不能翻轉那個 19%」——
Uber 沒有回答那題（它量的是成本不是時間），但它示範了那題該怎麼問：
固定一個變數，量一個能歸因的比值。

## 相關頁面

- [[uber]] —— 來源方
- [[context-tax]] —— 工具 schema 的預付脈絡成本
- [[managed-agents]] —— 全篇的結論方向
- [[ai-development-economics]] —— 成本結構被這份升級成可量測的
- [[context-engineering]] —— AI Context Graph 是隱性脈絡那條賭注的實作
- [[harness-engineering]] —— 第一份真實世界的 harness 效果數字
- [[agent-config-evals]] —— benchmark 驅動模型選擇是同一套機制
- [[wikiskill]] —— 它的 skill 自動演化，Uber 說在做
- [[open-questions]] —— Q15 的處境因此改變
