---
title: 總覽
type: synthesis
aliases: [overview]
tags: [樞紐]
created: 2026-08-01
updated: 2026-09-01
status: active
confidence: medium
sources: ["[[arm-yourself-with-specific-knowledge]]", "[[read-what-you-love]]", "[[elephants-goldfish]]", "[[agent-skill-design-patterns]]", "[[the-new-sdlc-with-vibe-coding]]", "[[prompting-claude-opus-5]]", "[[the-ai-native-sdlc-playbook]]", "[[metr-early-2025-ai-developer-productivity]]", "[[metr-2026-uplift-update]]", "[[ironies-of-automation-public-service]]", "[[bainbridge-ironies-of-automation]]", "[[ai-engineering-skills-map-software-fundamentals]]", "[[wikiskill]]"]
---

# 總覽

> 這個知識庫在累積什麼、目前的整體判斷是什麼。每次 ingest 後若有實質變動就更新這一頁。

## 這個庫在做什麼

累積多主題的個人知識。原始來源放 `Raw/`，由 LLM 讀完後寫成互相連結的 wiki 頁面放 `Wiki/`。
規則寫在根目錄的 `CLAUDE.md`。

**分工**：使用者負責找來源、提問、判斷方向；LLM 負責閱讀、萃取、歸檔、交叉引用、維持一致性。

## 目前的主軸

十三份來源大致收斂到同一個問題：**在機器能做掉實作之後，人還剩下什麼，以及那個東西怎麼運作。**

### 1. 判斷力是共同答案（5 份來源，跨 7 年）—— 本庫收斂度最高的一條

[[naval-ravikant|Naval]]（2019）、[[dave-rensin|Rensin]]（2026-04）、
[[addy-osmani|Osmani]] 等（2026-05）從完全不同的方向出發，都指向 [[judgment|判斷力]]。
白皮書的收尾句最直接：**「Generation is solved. Verification, judgment, and direction
are the new craft.」**——並把它變成人事建議：依判斷力而非實作能力招募。

### 2. 但它能不能被寫下來交給機器（本庫核心矛盾，已有數據）

Rensin 說「不要把判斷力外包給機器」，可是他的整套方法就是把判斷寫進文件交給 agent 執行。
若判斷力寫得下來，它就通過了 Naval 的「可訓練即可量產」判準，於是會貶值。

白皮書沒有解決這個矛盾，但**畫出了界線**：架構是「最頑固的人類環節」，
AI 擅長的是決策做成之後的實作。
三種解法與各自的證據見 [[can-judgment-be-outsourced]]。

**⚠️ 更正（2026-08-29）**：本頁先前寫「第一次提供了數據站在『無法外包』那側」，
引用的是 METR 的「慢 19%」。讀完
[[metr-early-2025-ai-developer-productivity]] 原始研究後，**那是誤讀**——
METR 找到的五個原因全是工具與情境（過度樂觀、開發者太熟悉 repo、repo 太複雜、
AI 可靠度低、隱性脈絡缺失），沒有一個關於人類判斷不可替代。
扣掉它之後，「無法外包」那一側**回到沒有實證數據的狀態**。
見 [[what-the-19-percent-measures]]。

**第四份來源換了說話的人**：[[prompting-claude-opus-5]] 是供應商在描述**模型的判斷**——
「模型會對任務應該是什麼行使自己的判斷」。它被寫進文件是因為它是要被約束的問題，
不是賣點，但這句話讓「判斷力是人類專屬」站不住了。
自我驗證、範圍判斷、自主委派這三層都在被吃掉（[[agent-autonomy-cost]]）。

**第五份來源給了它一個位置**：[[the-ai-native-sdlc-playbook]] 不辯論判斷力是什麼，
它直接**設計判斷力放在哪**——六個閘門（接受 `intent.md`、簽核 `spec.md`、核准 `plan.md`、
PR 核准、生產發布授權、事故分流），而且用 branch protection 與 hook 把人強制留在那些點上。
「寫程式的 agent 沒有辦法核准自己的程式碼。」

但它同時把政策本身寫成 skill 交出去了，
而且（推論）**閘門上的判斷是審查別人做完的東西，不是從頭做模式比對**——
這讓 Q6 更尖銳而不是更緩和。

**第六份來源說這題四十三年前就有答案了**：[[ironies-of-automation-public-service]]
把 Bainbridge 1983 帶進本庫。它的反諷 #3 直接反駁了「判斷力上移到閘門」這個安排——
監控**結構上不提供能力累積的條件**，而且 Bainbridge 預測這會**逐代惡化**。
展開見 [[monitoring-does-not-teach]] 與 [[judgment-supply]]。

（推論）本庫花了九份來源、四週，重新發現了一個 1983 年的結論。

**原文已補進本庫**（[[bainbridge-ironies-of-automation]]），並更正了轉引的數處失真。
原文比轉引版強：現在這代自動系統之所以能運作，是因為它們
「**riding on their skills**」——騎在一批**在自動化之前就練成**的人身上，
而「later generations of operators cannot be expected to have」那些技能。
原文也自己給了對策（每班保留一段手動時間，做不到就用模擬器），
以及一句把成本算法翻過來的話：**最成功的自動化，需要最多的人員訓練投資**。

**新的裂縫（兩條）**：

1. 如果判斷力持續上移，新的判斷力要從哪裡長出來？**這條在 2026-08-30 換了形狀**：
   它原本是九份來源共同的盲點，現在不是——Bainbridge 1983 完整描述過問題，**而且給了對策**
   （每班保留一段手動時間，做不到就用模擬器）。剩下的缺口從「沒有人談過」變成
   **「那些對策在軟體開發脈絡下有沒有效，沒有人驗證過」** → [[open-questions]] Q6、[[judgment-supply]]。
2. **界線移動得比框架快**：談 AI 的六份來源只橫跨六個月，
   但 [[elephants-goldfish]]（4 月）建議的部分做法已被 8 月的官方文件列為該刪的東西。
   如果界線每幾個月移動一次，「哪些判斷屬於人」可能沒有穩定答案，只有適應速度。

### 3. 什麼東西教不來（2 份來源）

[[specific-knowledge|特定知識]]的判準是反向的：能被訓練的就能被量產。
辨識訊號是「對你像玩、對別人像工作」。它的燃料是好奇心，
而好奇心不是被培養的，是[[love-of-reading|沒被弄丟]]的；
地基要打在能自己推導的東西上（[[first-principles-foundation]]）。

### 4. 規則檔會折舊（2 份來源）

[[prompt-obsolescence]]：為某個模型版本寫的護欄，在下個版本可能變成成本來源。
[[prompting-claude-opus-5]] 整份文件都在叫你**刪東西**——過度驗證指令、
「再檢查一次」、為前代調的 workaround、沿用的 effort 預設值。

這條**直接挑戰**其他來源的一個共同假設：
[[harness-engineering]] 說 harness 是「建一次、精煉很多次」的共享資產、
[[ai-development-economics]] 把它算成一次性 CapEx、
[[elephant-goldfish-model]] 說設計文件「是你新的原始碼」——
**沒有一份處理版本升級時的折舊**。如果每次換代都要重驗整套規則檔，經濟模型要重算（Q11）。

**第二份來源給了做法**：[[the-ai-native-sdlc-playbook]] 說操控 agent 的設定檔
（`CLAUDE.md`、skills、hooks）值得程式碼享有的那種回歸測試——
20–50 個真實任務組成 eval suite，設定一改就在 CI 跑，通過率掉了擋 merge
（[[agent-config-evals]]）。這解決**偵測**，沒解決**定位**（哪一條在扣分），
所以 Q10 還在；而且它讓 harness 從一次性 CapEx 變成 **CapEx 加持續 OpEx**。

### 5. 證據等級是本庫自己的問題（2 份來源，新主軸）

[[metr-early-2025-ai-developer-productivity]] 是本庫**第一份實證研究**，
也是第一份隨機對照試驗。它帶進來的不只是一個數字，是一把尺：

- **[[self-report-vs-measurement|自陳與實測差 39 個百分點]]**——同一批人自認快 20%、實際慢 19%。
  這解開了 Q7：白皮書並列的「提升 25–39%」是自陳調查，「慢 19%」是 RCT，兩者在測不同的東西。
- **[[evidence-types-for-ai-capability|三種證據各自的偏誤方向]]**——benchmark 傾向高估、
  自陳更不可靠、RCT 適用範圍窄。本庫十二份來源裡**九份是敘事或框架**，
  而這把尺說那一類最弱。
- **測量也會折舊**：這份研究被作者自己在頁首宣告過期（[[prompt-obsolescence]]）。
- **而且量測方法本身也會失效**：[[metr-2026-uplift-update]] 記錄了
  [[control-group-collapse|對照組崩解]]——開發者拒絕在無 AI 條件下工作、
  30–50% 承認會避開 AI 增益高的任務，使 RCT 在這個題目上正在失去可行性。
  **工具愈有價值，關於它的知識折舊愈快。**

**代價要講清楚：本庫現在一個生產力數字都不能直接引用。**
2025 那份顯著（區間 `+2% 到 +39%`）但已過期；2026 那份當期但兩組區間都跨過 0
且被作者宣告不可解讀。存活下來的只有[[self-report-vs-measurement|自陳不可信]]這條方法學發現。
連帶地，「判斷力無法外包」那一側**連一個可引用的數字都沒有了**——
沒有證據不等於證據為否，但本庫應該停止說它有數據支撐。

最不舒服的一條：它同時**支持與削弱**本庫的 harness 論述。
支持的是因子 5「隱性脈絡」正是規則檔與 skill 在編碼的東西；
削弱的是 [[harness-engineering]] 現有最硬的兩個數字都是 benchmark，
而 benchmark 正是這份研究說會高估的那一類。
本庫目前**沒有任何真實世界的 harness 效果數據**（Q15）。

**本庫終於有一份方法紮實的實驗來源了（2026-09-01）**：[[wikiskill]] 是
三次獨立重跑、paired bootstrap 顯著性檢定、四格 ablation 隔離變數、
負面結果照登、限制自列四條。按 [[evidence-types-for-ai-capability]] 的尺，
它落在 benchmark 那一格——會高估，但**它量的東西和其他 benchmark 不同**：
不是「有沒有 AI」，是**同一套工具的兩種組法**。這正是 Q15 缺的那種對照。
要打的折：arXiv 預印本、提出方法的人測自己的方法、對照組由他們自己實作。

### 6. 治理是本庫原本完全空白的一軸（1 份來源）

前六份來源談的都是**個人或小團隊**怎麼跟 AI 工作。
[[the-ai-native-sdlc-playbook]] 是第一份談**受監管的組織**怎麼做的，
它帶進三樣本庫原本沒有的東西：

1. **[[artifact-chain|產物鏈]]**：`intent.md` → `spec.md` → `plan.md` → diff 與測試 →
   PR 與審查發現 → 事故紀錄，每階段以 commit 收尾、下一階段讀它開始。
   **commit chain 本身就是稽核軌跡**，不必另建一套稽核系統。
2. **[[advisory-vs-deterministic-control|建議型控制 vs 確定型控制]]**：
   skill 讓違規變罕見，hook 讓違規變幾乎不可能。這是本庫收到過最有用的一刀，
   因為它修正了 [[agent-skills]]、[[skill-design-patterns]] 對 skill 的定位——
   **skill 是制度知識的散布機制，不是控制**。
3. **[[autonomy-tiering|自治分級]]**：偵測保持確定性（統計，不含模型），
   模型只在越界後被叫進來，而且訊號強度決定它拿得到哪些工具。
   最高等級也只是「開 PR 進審查閘門」。

原則一句話：**agent 可以做到 production gate 為止，過不了那道門。**

### 7. 「該懂什麼」是新的一軸（1 份來源，本庫證據最弱的一份）

前面六條軸線談的是流程、姿勢、機制、證據與治理，**沒有一條談能力清單**。
[[ai-engineering-skills-map-software-fundamentals]] 補上這一格：
五塊技能（全端、資料管理、系統架構、安全與可靠、規模化與維運），
以及 coding agent 在無人引導時會做壞取捨的七條軸線
（latency、availability、consistency、reliability、maintainability、simplicity、cost）。

它的主張是：不懂這些的人不是選錯，是**根本不知道有得選**，於是 agent 用預設值填。
本庫把這條記成 [[tradeoff-literacy]]，並把它定位成
[[the-80-percent-problem]] 的輸入端——同一個失敗的另一半，而且**在 diff 裡不留痕跡**。

它最有用的一句在資料架構那段：**AI 的輸入脈絡來自你的資料來源，
所以資料架構選壞了，「the AI doesn’t know what it doesn’t know」。**
這把 [[context-engineering]] 的上限從提示與檔案層推到**資料模型層**，
而那是本庫所有脈絡決策裡最早做、最難反悔的一個。

**但要把它的份量講清楚：這是本庫證據等級最低的一份來源。**
零數字、零外部引用，唯一依據是「our study of AI Engineering Skills shows」
——一份沒公開、沒方法、沒樣本數的內部研究；而作者的商業形式是課程，
結論與產品方向一致。它提供的是**角度**，不是證據。

它同時把裂縫 1 又拉大一格：它是本庫對「上移之後需要什麼能力」講得最具體的一份，
**卻通篇不談那些能力從哪裡長出來**（見下方缺口與 [[judgment-supply]]）。

### 8. 知識層與程序層要分開（1 份來源，本庫方法最紮實的一份）

[[wikiskill]] 把 agent 工作區切成三層，並且證明這個切法本身有價值：

| 層 | 性質 |
|---|---|
| 原始執行軌跡 | Permanent, Write Once |
| 持久知識層 | **Compounding, Never Reset** |
| 現行程序（skill） | Reversible, Conditional Update |

**核心不對稱是：程序可回滾，知識不回滾。** 因為「某個提案被試過而且被拒絕」本身就是知識，
跟著回滾就會被反覆重提。展開見 [[persistent-knowledge-layer]]。

三個結果直接動到本庫既有的頁：

1. **知識層值 +15.0 分**（48.7% → 63.7%）。這是本庫**第一個把 harness 的單一元件
   隔離出來測**的數字（[[harness-engineering]]、Q15）。
2. **同一份脈絡給錯角色會扣分**：讓執行任務的 agent 也讀知識層，
   成績從 63.7% 掉到 60.9%。（推論）[[context-engineering]] 因此多了第三個維度——
   不只「什麼時候載入」，還有「**誰該載入**」。
3. **程序知識可以跨模型移轉，而且常常勝過自己演化的**，
   但寫著低階權宜之計的會**害到**強模型（SpreadSheet 50.5% → 18.1%）。
   這同時是 [[prompt-obsolescence]] 第一層的實驗證據，
   也是 [[can-judgment-be-outsourced]] 解法 1 的反向證據（[[skill-transfer-across-models]]）。

### 9. 已經可以直接照做的操作（5 份來源）

這是庫裡不需要再驗證就能今天動手的部分：

- [[vibe-coding-spectrum]] —— 先決定這個任務該落在光譜哪裡（判準只有一條：輸出怎麼被驗證）
- [[harness-engineering]] —— agent 出錯時先查設定不要先怪模型；規則檔、工具、沙箱、hooks、可觀測性
- [[context-engineering]] —— 靜態 vs 動態脈絡是一級架構決策，也是成本決策
- [[ai-as-interrogator]] / [[skill-design-patterns]] —— 三段式提問法；五種 skill 模式
- [[elephant-goldfish-model]] —— 四階段九步驟，含金魚測試
- [[agent-autonomy-cost]] —— 畫界線而不是禁止；那段範圍約束句可以直接抄
- [[effort-and-thinking]] —— 用低 effort 控成本，不要關 thinking
- [[advisory-vs-deterministic-control]] —— 分清楚哪些規則是建議、哪些需要確定性的東西墊底
- [[intent-md]] —— 讓非工程師也能提出可執行的提案
- [[agent-config-evals]] —— 規則檔改動要有回歸測試
- [[tradeoff-literacy]] —— 動手前先問：這個任務有哪幾條取捨軸線我還沒說出來
- [[persistent-knowledge-layer]] —— 知識與程序分層，且被否決的提案要留下來

### 10. 這個庫在照鏡子

四個概念直接指向本庫自己的設計：`CLAUDE.md` 是白皮書定義的**靜態脈絡**與
[[harness-engineering|harness 規則檔]]；`Wiki/index.md` 是 progressive disclosure 的手工版；
`tools/lint.py` 是確定性 guardrail；ingest 流程混用了
[[skill-design-patterns|Pipeline、Generator、Reviewer]] 三種模式，
原本認為缺的是 **Inversion** 硬閘門——[[prompting-claude-opus-5]] 給了相反方向的建議
（例行判斷讓模型自己做），Q9 一度因此擱置，後來被第七份來源改寫成「閘門該寫在哪裡」。
**現在 `tools/lint.py` 已有兩道確定性閘門**：規則來由缺漏、以及 `confidence` 與來源數不符。
反而 `CLAUDE.md` 沒有記錄**每條規則為什麼存在**，這在折舊問題下是實際的缺陷（Q10）。

**第七份來源給了三面新鏡子**：

- `CLAUDE.md` 建議控制在**一頁以內**（session 開頭全讀，過期內容白佔脈絡）。
  **已照做**（2026-08-29）：204 行壓到 76 行，細節搬進 `.claude/skills/`。
  代價是那些規則的執行力從常駐降成按需觸發（[[advisory-vs-deterministic-control]]）。
- Q9 被改寫了：問題不是「該不該加 Inversion 閘門」，是**閘門寫在哪裡**。
  寫在 `CLAUDE.md` 裡的是建議，`tools/lint.py` 才是確定性的閘門。
  已據此加了兩道：規則來由缺漏、`confidence` 與來源數不符。
  候選的下一條：ingest 完成前強制 lint 通過。
- Q13 是本庫自己的量測問題：**lint 全綠不代表 wiki 健康**，
  只代表機械性檢查沒抓到東西。「趨近於零」的指標，成功與停止量測長得一樣。

**Q10 已結案（2026-08-29）**：`CLAUDE.md` 每條規則加了穩定編號，來由記進 `.claude/rules-ledger.md`。
但證據狀況比預期差——**26 條規則裡只有 1 條的來由是有紀錄的**，其餘全是推論或未知，
因為建庫時沒記、而且這個 repo 不是 git repo。
教訓很直接：**來由要在寫規則的當下記，事後補不回來。**
改用「這條規則實際被觸發過嗎」當替代指標後跑出四個發現，最硬的一條是
**`query` 流程從未被執行過**（當時 log 8 筆全是 ingest 與 lint），W3、W4 兩條規則從未被驗證。

**鏡子換成別人拿了（2026-09-01）**：[[wikiskill]] 不是在談本庫，
但它的三層架構與本庫是同一個形狀，而且它明說靈感來自 Karpathy (2026) 的「LLM Wiki」。
逐格比對之後，本庫缺的那一格很清楚：

| WikiSkill | 本庫 |
|---|---|
| `raw/` 不可變執行軌跡 | `Raw/`（`[L1]`） |
| `wiki/patterns/` + `index.md` + `logs.md` | `Wiki/` + `index.md` + `log.md` |
| `skills/` + `PURPOSE.md` | `.claude/skills/` + `CLAUDE.md` + `.claude/rules-ledger.md` |
| `skill-impact.md`：被拒提案的 diff、分數、結果 | **沒有** |

`log.md` 記的是**做了什麼**，`rules-ledger` 記的是**被採用的規則為什麼在**。
本庫沒有任何地方記錄**試過、被否決、為什麼不做**。
（推論）這是可以直接照做的一條，而且照 WikiSkill 的說法，
它的用途是防止同一個壞主意被反覆提出。

**已照做（2026-09-01，使用者同意改 `CLAUDE.md`）**：規則 `[W9]`、帳在 `.claude/rejected-proposals.md`（建檔回填 6 筆）、`tools/lint.py` 加 `[否決帳]` 格式檢查、`tools/test_lint.py` 的突變從 20 種增為 22 種。逐格比對存成 [[two-wiki-architectures]]。**這道閘門只擋得到格式**——「否決了卻沒記」偵測不到，那一半仍是建議型控制。

第二面鏡子比較不舒服：那份研究的提案接受率是每輪提 3.1 個 skill、只接受 1.6 個。
**本庫至今沒有測過任何一次規則改動的效果**——`[W8]` 的預期效果協定是往這個方向走的第一步，
但目前只有一筆觀察（見 Q15）。

**2026-08-30 的現況**：`query` 已執行 3 次，W3、W4 在 Q14 結案時處理掉了。
規則從 26 條長到 35 條，來由是**有紀錄**的從 1 條增加到 7 條——
全部是 2026-08-29 之後新增的規則，也就是 `[W8]` 那道閘門開始生效之後的。
建庫時那批仍然是 18 條推論、10 條來由未知，**而且補不回來**。

## 目前的缺口

- **已經跨出領域，但只跨了一條線**：十三份裡有**兩份**不談軟體開發——
  [[ironies-of-automation-public-service]]（公共服務，2024）與
  [[bainbridge-ironies-of-automation]]（工業製程控制，1983）。兩份是同一條線的兩端，
  後者是前者的原始出處。所以**跨出去的是一個領域、一條論證，不是多個獨立領域**。
  時間尺度倒是真的拉開了：從六個月變成四十三年。
- **來源獨立性（十三份的實際分布）**：

  | 來源方 | 份數 | 有沒有東西要賣 |
  |---|---|---|
  | Google 或 Google 員工 | 3 | [[the-new-sdlc-with-vibe-coding]]、[[agent-skill-design-patterns]]、[[elephants-goldfish]] |
  | Anthropic | 2 | [[prompting-claude-opus-5]]、[[the-ai-native-sdlc-playbook]] |
  | [[naval-ravikant]] | 2 | [[arm-yourself-with-specific-knowledge]]、[[read-what-you-love]] |
  | [[metr]] | 2 | 沒有產品，但組織動機是 AI 風險評估 |
  | 學術（Lindgren、Bainbridge） | 2 | 沒有 |
  | [[andrew-ng]] | 1 | [[ai-engineering-skills-map-software-fundamentals]]，商業形式是課程 |
  | Google Research（學術） | 1 | [[wikiskill]]，沒有產品，但提出方法的人測自己的方法 |

  **賣方 6/13**，剛好又回到未過半。（推論）新增的 [[wikiskill]] 不是賣方，
  但也不是中立第三方——它的偏誤方向是「自己的方法會贏」，
  這在 ablation 與負面結果照登這兩件事上被部分抵銷。
  （推論）METR 的方向偏誤是對
  「AI 能力被高估」的證據更敏感；學術那兩份的偏誤是領域不同，移植成不成立要自己論證。
- Naval 的兩篇都在 AI 普及之前（2019）。他 2026 年的說法是最大的缺口（Q1）。
- **十三份裡只有四份帶資料**（白皮書、METR 兩份、[[wikiskill]]），其餘九份全是敘事與框架。
  而 METR 兩份的數字現在都不可直接引用，白皮書引用的數字多半是自陳調查。
  **實質上本庫沒有可用的量化證據。**
  Bainbridge 帶進來的唯一數字是轉引的——vigilance 上限約半小時（Mackworth 1950）。
  最新一份（[[ai-engineering-skills-map-software-fundamentals]]）連轉引的數字都沒有。
  **但 [[wikiskill]] 改變了這一格**：它是本庫唯一有 ablation 與顯著性檢定的來源，
  代價是它量的是 benchmark 答對率，不是真實工作。
- [[leverage-and-compounding]] 仍是 seed，撐著主軸 3 的關鍵一步。
- **治理那一軸目前只有一份來源，而且是賣方的**。需要一份買方或監管方視角的來源來對撞。
- **一個結構性的缺口浮出來了（2026-09-01）**：把十二份排開之後，
  **要求某種能力的來源不談那種能力從哪來，描述供給消失的來源不談軟體開發，
  量到人不願回頭的來源不談能力累積**——沒有一份同時處理兩邊。
  對照表在 [[judgment-supply]]。（推論）這不是還沒找到，是要處理兩邊
  得追蹤同一批人在 agentic 環境裡數年的能力變化，而工具穩定的時間比養成一個資深工程師短。
- 十六個開放問題見 [[open-questions]]，Q7、Q10、Q12、Q13、Q14、Q16 已結案，Q9 改寫。
  **最大的證據缺口仍是 Q15（好的 harness 能不能翻轉那個 19%），而且比一個月前更難填**——
  2026 那份把 harness 這個變數綁在「不同的人」與「不同成熟度的 repo」上，無法歸因。
  （推論）外部研究做不動的情況下，本庫自己記錄「加規則前後的返工次數」可能是唯一可行的路。
  Q12、Q13、Q14 不需要新來源，動手就能推進。

## 統計

| 項目 | 數量 |
|---|---|
| 來源 | 13 |
| Wiki 頁面 | 63 |
| 開放問題 | 16（6 條 closed、1 條改寫） |
| 已標記的矛盾 | 6（**本庫對 METR 的誤讀，見 [[what-the-19-percent-measures]]**、[[can-judgment-be-outsourced]]、[[the-80-percent-problem]] 的數據衝突、[[design-is-the-new-code]] 的判準 vs 清單、[[prompt-obsolescence]] 對 harness 是純資產的挑戰、[[design-is-the-new-code]] 的「唯一算數的產物是哪一個」） |
