---
title: 判斷力能不能外包
type: synthesis
aliases: [judgment outsourcing]
tags: [ai, 能力, 論點]
created: 2026-08-01
updated: 2026-08-30
status: active
confidence: medium
sources: ["[[arm-yourself-with-specific-knowledge]]", "[[elephants-goldfish]]", "[[the-new-sdlc-with-vibe-coding]]", "[[prompting-claude-opus-5]]", "[[the-ai-native-sdlc-playbook]]", "[[metr-early-2025-ai-developer-productivity]]", "[[metr-2026-uplift-update]]"]
---

# 判斷力能不能外包

> 五份來源都說：[[judgment|判斷力]]是唯一不會貶值的東西。
> 但一份說它教不來，另外兩份的整套方法就是在把它寫下來交給機器執行。
> 第三份來源（Google 白皮書）沒有解決這個矛盾，但**畫出了那條分界線**。

## 兩邊的說法

| | [[naval-ravikant|Naval]]（2019） | [[dave-rensin|Rensin]]（2026） |
|---|---|---|
| 判斷力是什麼 | 在複雜環境做模式比對累積出來的東西 | 公司雇你的唯一理由 |
| 能不能教 | **教不來**，只能學（[[specific-knowledge]]） | 沒直接談，但整套流程在教 |
| 怎麼變現 | 靠[[leverage-and-compounding|槓桿]]放大 | 寫成設計文件，交給 agent 執行 |
| 對機器的態度 | 可訓練的東西終將被機器取代 | **不要把判斷力外包給機器** |

（Naval 這一欄出自 [[arm-yourself-with-specific-knowledge]]，2019 年的兩篇之一。）

## 矛盾在哪

Rensin 說「不要把判斷力外包給機器」，但 [[elephant-goldfish-model]] 做的事情是：
把所有設計判斷逼進一份文件（[[design-is-the-new-code]]），然後把文件交給 agent 執行。
文件寫得夠好的判準，是**一個零記憶的金魚 session 能只靠它重建整個理解**。

如果判斷力能被壓縮到一份文件、且能被一個沒有脈絡的實體完整還原——
那它就通過了 Naval 的「可訓練」判準，於是它可被量產，於是它會貶值。
Rensin 的方法若成功，會摧毀他自己的前提。

## 第三份來源把界線畫在哪

[[the-new-sdlc-with-vibe-coding]] 沒有處理這個矛盾，但它的立場最明確：
**架構是「最頑固的人類環節」**，因為架構決策是取捨（一致性 vs 可用性、複雜度 vs 彈性、
自建 vs 採購），依賴 AI 抓不到的商業脈絡與長期考量。AI 擅長的是**在決策做成之後實作它**。

同一份來源用兩個東西補強了這條界線：

- **[[the-80-percent-problem|80% 問題]]**：剩下的 20%（邊界情況、整合點、細微正確性）
  需要模型缺乏的深度脈絡，而且錯誤性質從語法錯變成概念錯，**因為看起來對所以更難抓**。
- **METR 的數據**：資深開發者在特定任務上反而多花 **19%** 時間，
  幾乎全花在驗證、除錯、修正 AI 產出。

這是本庫第一次有**數據**站在「判斷力無法外包」那一側。

## 第四份來源改變了問題的形狀

前三份都在辯論「人的判斷力能不能被寫下來交給機器」。
[[prompting-claude-opus-5]] 讓這個問法過時了，因為它報告的是**模型已經在自己做判斷**：

> "Claude Opus 5 can also expand the scope of a task, adding steps that weren't requested
> or **applying its own judgment about what the task should be**."

三個具體變化，每一個都在移動界線：

1. **自我驗證**：模型自己會驗證與修錯，所以叫它驗證反而是浪費。
   [[elephant-goldfish-model]] 的金魚協定有一部分正在變成過期的鷹架（[[prompt-obsolescence]]）。
2. **範圍判斷**：模型會決定「這個任務應該是什麼」——這正是 Naval 定義的
   「在複雜環境裡做模式比對」。
3. **委派**：模型自己決定要不要生成子 agent，也就是**它在管理其他 agent**——
   [[conductor-and-orchestrator|協調者]]那一層的工作。

**注意方向**：這些全被寫進文件是因為它們是**要被約束的問題**，不是能力賣點。
供應商的立場其實與 Rensin 一致——別把判斷交出去——但它同時承認模型已經在做了。

## 第五份來源把判斷力放到閘門上

[[the-ai-native-sdlc-playbook]] 是第一份不辯論、直接**設計位置**的來源。
它的答案是「層級移動說」的工程實作：判斷力既不外包也不留在原地，
它被搬到六個**閘門**上——接受 `intent.md`、簽核 `spec.md`、核准 `plan.md`、
PR 核准、生產發布授權、事故分流。

三個細節值得注意，因為它們同時支持與削弱這條路線：

**支持的：職責分離被明文保住。**

> "Separation of duties is preserved, because the agent that wrote the code has no way to approve it."

寫程式的 agent 沒有路徑核准自己的程式碼；branch protection 要求人類 code owner 核准；
生產部署要求具名的發布授權。人的判斷不是禮貌性的，它被確定型控制強制在流程裡
（[[advisory-vs-deterministic-control]]）。

**削弱的一：政策本身被寫成 skill 交出去了。**
brand、security、compliance、UX 政策被編碼成 skill，在 `spec.md` 被寫的當下自動套用，
而不是在幾週後的審查裡被發現。這正是 [[dave-rensin|Rensin]] 那條路線的延伸——
**把判斷寫進文件**——只是這次寫的是組織政策而非架構設計。
原文自己給的落後指標更露骨：引用該政策的 PR 審查發現數量**應該趨近於零**。

**削弱的二：閘門上的判斷是審查，不是從頭做模式比對。**
（推論）在閘門上判斷「這個變更做的是計畫要做的事嗎、風險可以接受嗎」，
和 Naval 說的「在高度複雜的環境裡做模式比對」不是同一種活動。
前者需要看得懂 agent 標記出來的東西；後者需要自己踩過那些坑。
這讓 Q6 的問題更尖銳而不是更緩和——**閘門是判斷力的消費端，不是生產端**。

## 更正：本頁對 METR 的引用是誤讀

本頁先前寫「這是本庫第一次有**數據**站在『判斷力無法外包』那一側」，
把 METR 的 19% 當成那條線的證據。讀完
[[metr-early-2025-ai-developer-productivity]] 原始研究之後，**這個用法站不住**。

METR 調查 20 個潛在因素、找到證據支持五個：對 AI 的過度樂觀、開發者對 repo 高度熟悉、
repo 太大太複雜、AI 可靠度低、隱性脈絡缺失。
**沒有一個因子是關於人類判斷力不可替代。** 五個全都指向工具與情境——
而那些是可以被改善的條件。

而且因子 2 的機制標註是「拉高**開發者**表現」，
意思是那 19% 有一塊來自人類基準線特別高（專家在自己長年貢獻的 repo 上），
不是 AI 特別差。

**本頁保留這條記錄而不是刪掉它**，因為誤讀本身是有價值的資料：
一份方法學嚴謹的研究，很容易被拿去支持它沒有主張的東西。
完整的兩面分析見 [[what-the-19-percent-measures]]。

（推論）扣掉 METR 之後，「判斷力無法外包」那一側**又回到沒有實證數據的狀態**，
只剩 [[the-80-percent-problem|80% 問題]]這種框架式論證。
本庫核心矛盾的證據天平因此往「可以外包」那側偏了一格。

## 後續研究讓這一側的處境更差

[[metr-2026-uplift-update]] 之後，本頁先前那個誤讀不只是「用錯了」，
而是**那個數字現在整個不能用**：2025 那輪已過期，2026 那輪的兩組信賴區間都跨過 0，
且被作者宣告不可解讀（[[control-group-collapse]]）。

（推論）淨效果是：「判斷力無法外包」那一側**連一個可引用的數字都沒有了**，
剩下的全是框架式論證（[[the-80-percent-problem|80% 問題]]、架構是最頑固的人類環節）。
而框架式論證正是 [[evidence-types-for-ai-capability]] 裡最弱的那一類。

這不代表那一側是錯的——**沒有證據不等於證據為否**。
但本庫應該停止把它描述成「有數據支撐」。

## 三種可能的解法

1. **有損壓縮說**：設計文件承載的是判斷的**結論**，不是產生結論的能力。
   金魚能執行，不能生成下一份文件。（這一條最符合兩份來源的實際文字，但沒有被證明。）
2. **層級移動說**：可寫下來的那層判斷確實被量產了，人類判斷力往上移一層。
   Naval 的邏輯仍成立，只是邊界一直在移動。
   **[[the-new-sdlc-with-vibe-coding]] 實質上採取了這個立場**：實作被吃掉，
   瓶頸移到規格、評估、架構判斷與審查，所以它的組織建議是
   「依判斷力而非實作能力重新設計招募」。
   [[conductor-and-orchestrator|協調者模式]]要的四種技能（規格、拆解、評估、系統設計）
   就是上移之後那一層的具體內容。**這是目前證據最多的一種解法。**
   [[prompting-claude-opus-5]] 又補了第二層證據：不只實作被吃掉，
   連「驗證」與「決定任務範圍」這兩層也開始被吃掉，人再被推上去一層。
3. **Naval 判準過強說**：「可訓練 = 可量產 = 報酬歸零」在現實中有大量反例
   （執照、工會、資訊不對稱）。若判準本身不成立，矛盾就消失。

## 解法 1（有損壓縮說）有第一筆證據了

本頁列的三種解法裡，「設計文件承載的是判斷的**結論**，不是產生結論的能力」
一直被標為「最符合來源文字但沒有被證明」。**2026-08-30 有了第一筆資料，來自本庫自己。**

規則 `[K1]` 寫進 `CLAUDE.md` 的隔天，我在單一頁面違反它 9 次，
全部由確定性檢查擋下。（推論）**結論傳遞成功了，能力沒有。**

n=1、觀察者就是受試者，不能推廣。但方向與有損壓縮說預測的一致，
而且與 [[advisory-vs-deterministic-control]] 記的供應商說法同向。
展開見 [[judgment-supply]]。

## 為什麼這對本知識庫重要

這個庫的整個結構就站在這條矛盾上：`CLAUDE.md` 是一份「把判斷寫成文件」的嘗試，
而 wiki 頁面是 agent 依照它產出的東西。這個庫成不成立，等於在測解法 1 到底對不對。

## 界線移動的速度快過框架

（推論）本庫五份談 AI 的來源橫跨 2026 年 3 月到 8 月，只有五個月，
但 [[elephants-goldfish]]（4 月）建議的部分做法，
已經被 [[prompting-claude-opus-5]] 明確列為該刪的東西。

這對整條論證有個尷尬的意涵：如果界線每幾個月就移動一次，
那「哪些判斷屬於人」可能**沒有穩定答案**，只有「此刻的分工」，
以及**適應速度**這件事本身——而適應速度剛好又是一種判斷力。

## 一條沒人談的反論

（推論）如果判斷力持續上移，那**判斷力要從哪裡長出來**就成了問題。
Naval 說它來自在複雜環境裡做模式比對；如果那些環境全部被 agent 接手，
資淺的人就沒有累積判斷力的場域了。白皮書建議「依判斷力招募」，
卻沒有回答那些判斷力該從哪個管道生產出來——這是三份來源共同的盲點。

## confidence 為什麼是 medium

五份來源裡有兩份（Rensin、白皮書）在同一年、同一個產業、同一個利益方向上，
不算真正獨立。白皮書是 Google 出的，結論指向自家產品線。
另外兩份（[[prompting-claude-opus-5]]、[[the-ai-native-sdlc-playbook]]）都是 Anthropic 出的，
而且後者通篇在推薦自家產品線。**四份 2026 年的來源只出自兩家公司。**
Naval 那兩篇是 2019 年、AI 普及之前的說法，他在 2026 年會不會改口未知——這仍是最大的缺口。

## 尚未解決的部分

見 [[open-questions]] Q1、Q2。

## 相關頁面

- [[judgment]] —— 爭議的核心概念
- [[specific-knowledge]] —— Naval 那一側的地基
- [[design-is-the-new-code]] —— Rensin 那一側的地基
- [[open-questions]] —— 待補的來源
- [[the-new-sdlc-with-vibe-coding]] —— 第三份來源，畫出了界線
- [[the-80-percent-problem]] —— 站在「無法外包」那側的數據
- [[agent-autonomy-cost]] —— 模型行使判斷的具體表現
- [[prompting-claude-opus-5]] —— 第四份來源，供應商的一手描述
- [[the-ai-native-sdlc-playbook]] —— 第五份來源，把判斷力放到閘門上
- [[advisory-vs-deterministic-control]] —— 人的判斷靠什麼被強制留在流程裡
- [[metr-early-2025-ai-developer-productivity]] —— 被誤讀的那份研究
- [[what-the-19-percent-measures]] —— 誤讀的完整拆解
- [[metr-2026-uplift-update]] —— 讓這一側連數字都沒有了
- [[judgment-supply]] —— 供給端的問題，本頁只處理傳遞端
