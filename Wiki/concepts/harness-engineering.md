---
title: Harness 工程
type: concept
aliases: [harness, Agent = Model + Harness]
tags: [ai, 軟體工程, agent]
created: 2026-08-01
updated: 2026-08-29
status: active
confidence: high
sources: ["[[the-new-sdlc-with-vibe-coding]]", "[[prompting-claude-opus-5]]", "[[the-ai-native-sdlc-playbook]]"]
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
