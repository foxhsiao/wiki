---
title: Harness 工程
type: concept
aliases: [harness, Agent = Model + Harness]
tags: [ai, 軟體工程, agent]
created: 2026-08-01
updated: 2026-09-01
status: active
confidence: high
sources: ["[[bainbridge-ironies-of-automation]]", "[[the-new-sdlc-with-vibe-coding]]", "[[prompting-claude-opus-5]]", "[[the-ai-native-sdlc-playbook]]", "[[metr-early-2025-ai-developer-productivity]]", "[[ironies-of-automation-public-service]]", "[[wikiskill]]"]
---

# Harness 工程

> **Agent = Model + Harness。** 把模型當成系統是錯的直覺，而且會導致錯誤的投資。
> 裸模型不是 agent；當 harness 給了它狀態、工具執行、回饋迴圈與可強制的限制，它才變成 agent。

## harness 裡有什麼

| 元件 | 內容 |
|---|---|
| 指令與規則檔 | `AGENTS.md`、`CLAUDE.md`、`GEMINI.md`、skill 檔、子 agent 提示 |
| 工具 | 函式、MCP server、API，**以及告訴模型何時怎麼呼叫它們的那些散文** |
| 沙箱與執行環境 | 程式碼實際跑在哪、碰得到什麼、碰不到什麼 |
| 編排邏輯 | 子 agent 生成、模型路由、專家之間的交接、各自何時觸發 |
| Guardrails／Hooks | 在特定生命週期點跑的**確定性程式碼**：工具呼叫前、檔案編輯後、commit 前。放那些 agent 不該忘但常忘的事 |
| 可觀測性 | 日誌、追蹤、評估、成本與延遲計量。沒有它就無法分辨 agent 是做得好還是在悄悄漂移 |

**這些是團隊的責任範圍，不是模型供應商的。**

## 證據

| 實驗 | 結果 |
|---|---|
| Terminal Bench 2.0，只改 harness、完全不換模型 | 從 Top 30 之外進到 **Top 5** |
| LangChain，只調系統提示、工具、middleware | **+13.7 分** |

## 最實用的一句

> **Most agent failures, examined honestly, are configuration failures.**

agent 出錯時第一直覺是怪模型。但更常見的原因是：少了一個工具、規則寫得含糊、
缺一道 guardrail、或者脈絡視窗塞滿雜訊。

## harness 在 SDLC 各階段

| 階段 | 用到的 harness 元件 | 動作 |
|---|---|---|
| 需求、規劃、架構 | 指令與規則檔 | **設定 harness**：寫 `AGENTS.md`、定架構限制、定義工具、訂不可違反的規則 |
| 實作 | 沙箱、工具 | **運行 harness**：模型在隔離沙箱裡執行產出的程式碼 |
| 測試與 QA | 編排邏輯、guardrails | **回饋迴圈**：測試失敗時把錯誤路由回模型，形成 think→act→observe |
| 審查、部署、維護 | hooks、可觀測性 | **觀測 harness**：hook 擋掉硬編密碼的 commit；追蹤 token 成本、延遲、漂移 |

## 一份 harness 設定指南長什麼樣

[[prompting-claude-opus-5]] 是本庫唯一一份**具體的 harness 設定文件**，
也是「多數 agent 失敗是設定失敗」的直接印證——它逐條列出哪些設定會造成
過度驗證、範圍擴張、過度委派與標籤洩漏。

但它同時**挑戰**了這一頁的一個假設。這一頁說「建一次、精煉很多次」，
把 harness 當成會複利的團隊資產；那份文件顯示規則檔會隨模型換代而**折舊**，
有些條目從資產變成負債。見 [[prompt-obsolescence]]。

還有一個性質上的轉變：當模型自主性提高，harness 的工作從「補能力」變成「設邊界」。
見 [[agent-autonomy-cost]]。

## harness 的作用範圍會擴到組織

前面這張表把 harness 描述成一個 session 或一個 repo 的東西。
[[the-ai-native-sdlc-playbook]] 顯示它會長到組織層級，而且多出一個本頁沒有的維度：
**誰有權關掉它。**

原文的 managed settings 由平台團隊經 MDM 或管理主控台派送，工程師改不動也覆蓋不了：

| 設定 | 買到什麼控制 |
|---|---|
| `permissions.deny` / `allow` | 密鑰不進脈絡、擋工具層的網路外連；同時預先核准安全的內圈以免權限疲勞 |
| `disableBypassPermissionsMode` + `allowManagedPermissionRulesOnly` | 沒有工程師、專案檔或命令列旗標能放寬規則 |
| `sandbox` + `failIfUnavailable` | 補權限補不到的洞：工具層擋掉 WebFetch 不會擋住 shell 指令連網，OS 層網域白名單才會；沙箱起不來就拒絕啟動 |
| `credentials` | 沙箱內的 shell 仍讀得到 `~/.ssh`、`~/.aws/credentials`，這一塊把它們關掉並從環境變數剝掉指定密鑰 |
| `allowManagedHooksOnly` | 本地不能新增或替換核准閘門 |
| `disableSideloadFlags` + `strictKnownMarketplaces` | 每個 skill、agent、hook、MCP server 都來自組織核可的 marketplace |
| `requiredMinimumVersion` | 低於核可版本就不啟動，控制由組織實際評估過的建置強制 |

原文自己加了一句限定：**「當成起點來調整，不是照抄的建議。每一條 deny 都在拿能力去換。」**

這也讓本頁「多數 agent 失敗是設定失敗」多一層意思——
設定不只是有沒有寫對，還包括**寫在誰改得動的地方**。
分層見 [[advisory-vs-deterministic-control]]。

## 回饋迴圈：harness 裡最零成本的那一件

原文列的 13 個 play 裡，「給 Claude 一個回饋迴圈」的前置需求是 None，
而它決定了其他所有 play 需要多少人力監督：能自己驗證的 session 才不需要人盯。

一個容易混掉的區分：**回饋迴圈跑遍整個任務，次數由工作量決定；
verifier 子 agent 是在 session 自認做完之後，用一個全新的脈絡視窗跑一次最終檢查**——
目的是讓判定不被產生程式碼的那組假設污染。兩者不能互相取代。

## 一份研究同時支持與削弱這一頁

[[metr-early-2025-ai-developer-productivity]] 對本頁是雙面的，兩面都要記。

**支持的一面。** METR 自己在「我們不提供證據支持」的表格裡寫：
「Cursor 取樣的 token 不多，可能沒有最佳的提示或鷹架，
領域／repo 特定的訓練、微調或 few-shot 有可能產生正向加速」。
而且被排除的六個因子裡包含 **Non-frontier model usage**——
模型夠不夠新被檢驗過並排除了，**鷹架夠不夠好沒有被檢驗**。
（推論）這個形狀很符合本頁那句「多數 agent 失敗其實是設定失敗」。

**但這條救援不能當證據用。** 那句話是作者主動劃出的界線，不是他們的發現。
拿它解釋 19% 是一個**未經檢驗的假說**。

**削弱的一面，而且更麻煩。** 本頁最硬的兩個數字——
Terminal Bench 只改 harness 進 Top 5、LangChain +13.7 分——**都是 benchmark**。
而同一份 METR 研究的判斷是：benchmark 因為只量「範圍界定良好、可演算法評分」的任務而
**傾向高估**，且難以直接翻譯成真實世界的影響（[[evidence-types-for-ai-capability]]）。

也就是說：這份研究給了 harness 論述一個可能的立足點，
同時抽掉了它原本站的那塊地。**本頁目前沒有任何真實世界的 harness 效果數據。**
完整拆解見 [[what-the-19-percent-measures]]。

## 「多數失敗是設定失敗」有個 1983 年的同構命題

[[ironies-of-automation-public-service]] 的反諷 #1：所有涉入者都可能出錯，
**包括設計者**，而設計者的錯誤是操作問題的主因之一。
自動化不是消除錯誤，**是換一個錯誤來源**。

（推論）本頁那句「多數 agent 失敗，誠實檢視之後，都是設定失敗」
與它隔了四十三年但形狀相同——**錯誤從執行者移到設計者**，
而設計者的錯誤更難被察覺，因為它嵌在系統裡而不是發生在動作上。

差別是本頁把這當成好消息（設定可以改進），Bainbridge 把它當成反諷
（自動化宣稱要消除人為錯誤，實際上只是換了個人來犯）。

## 原文對「設計者的錯誤」多說了一句

[[bainbridge-ironies-of-automation|Bainbridge 1983]] 的第一個反諷是
"designer errors can be a major source of operating problems"，
但他接著補的那句本庫該記住：

> Unfortunately people who have collected data on this are **reluctant to publish** them,
> as the actual figures are difficult to interpret.

（推論）四十三年後這個問題沒變——本庫收錄的十份來源裡，
沒有一份公布過自己的 harness 失敗率。[[the-new-sdlc-with-vibe-coding]] 給的兩個
benchmark 數字是**改進幅度**，不是失敗率。

**一個 1983 年沒有的差異**：Bainbridge 的自動系統是確定性的，設計者原則上知道它會做什麼。
agent 不是。（推論）這讓反諷 #1 在 LLM 上更嚴重——連設計者都無法完全預期系統行為。

## 第一個被單獨隔離出來的 harness 效果

本頁的證據一直有同一個弱點：所有數字都在比「有 agent vs 沒有 agent」，
沒有一個在比「同一個 agent，harness 好一點 vs 差一點」。
[[open-questions]] Q15 就是這個缺口。

[[wikiskill]] 是本庫第一份把 harness 的**一個元件**當成單一變數來測的來源。
其他條件全部固定，只切換提出 skill 更新的那個 agent 讀不讀得到持久知識層
（Gemini-3.5-Flash，四個 benchmark 平均）：**48.7% → 63.7%，差 15.0 分**。
三次獨立重跑，paired bootstrap `p < 0.05`。展開見 [[persistent-knowledge-layer]]。

**但這不能結案 Q15**，理由要說清楚：

| Q15 問的 | 這份來源給的 |
|---|---|
| 真實開發工作的時間 | benchmark 答對率 |
| 人使用 agent | agent 改進 agent |
| 換掉鷹架重跑同一組人 | 換掉知識層重跑同一組任務 |

（推論）它證明的是「**harness 的組成方式會造成很大的差距**」這件事本身——
這比本頁原有的兩個 benchmark 數字（Terminal Bench、LangChain）更接近本頁的主張，
因為那兩個比的是有沒有工具，這個比的是**同一套工具的兩種組法**。
而 [[metr-early-2025-ai-developer-productivity]] 明說沒有檢驗過鷹架好壞，
所以這是本庫在那個方向上的第一筆資料，不是最後一筆。

還有一條反面的：**同一份脈絡放給不同角色，價值符號會相反**
（給執行者讀反而 −2.8 分）。harness 設計因此不只是「準備哪些東西」，
還是「**哪個角色看得到哪些東西**」（[[context-engineering]]）。

## 與本知識庫的關係

（推論）這個庫的 harness 就是 `CLAUDE.md`（規則檔）＋ `tools/lint.py`（確定性 guardrail）
＋ `Wiki/log.md`（可觀測性）。
[[elephant-goldfish-model]] 的整套流程也是一種 harness，只是沒有用這個詞。

## 相關頁面

- [[the-new-sdlc-with-vibe-coding]] —— 來源
- [[vibe-coding-spectrum]] —— harness 的深淺決定你落在光譜哪裡
- [[context-engineering]] —— 規則檔與 skill 是 harness 的一部分
- [[factory-model]] —— harness 是工廠裡那台機器周邊的所有東西
- [[prompt-obsolescence]] —— harness 會折舊，這一頁沒處理
- [[prompting-claude-opus-5]] —— 一份具體的 harness 設定指南
- [[the-ai-native-sdlc-playbook]] —— harness 擴到組織層級的樣子
- [[advisory-vs-deterministic-control]] —— harness 元件的兩種執行力
- [[agent-config-evals]] —— harness 自己要被回歸測試
- [[metr-early-2025-ai-developer-productivity]] —— 同時支持與削弱本頁的研究
- [[evidence-types-for-ai-capability]] —— benchmark 證據的偏誤方向
- [[what-the-19-percent-measures]] —— 兩面的完整拆解
- [[ironies-of-automation-public-service]] —— 反諷 #1 與本頁隔 43 年同構
- [[bainbridge-ironies-of-automation]] —— 反諷 #1 的原文
- [[wikiskill]] —— 第一個被單獨隔離出來的 harness 效果數字
- [[persistent-knowledge-layer]] —— 那個數字量的是哪個元件
