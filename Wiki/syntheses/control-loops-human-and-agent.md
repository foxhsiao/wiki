---
title: 人的控制迴圈與 agent 的控制迴圈
type: synthesis
aliases: [control loops human and agent, cybernetic loop, 迴圈同構]
tags: [ai, agent, 能力, 論點, 控制迴圈]
created: 2026-09-08
updated: 2026-09-08
status: active
confidence: low
sources: ["[[how-to-fix-your-entire-life-in-1-day]]", "[[harness-engineering-complete-guide]]", "[[bainbridge-ironies-of-automation]]", "[[the-ai-native-sdlc-playbook]]"]
---

# 人的控制迴圈與 agent 的控制迴圈

> 兩份同一週進到本庫、互不知道對方、讀者完全不同的來源，
> 把「怎麼把事情做成」寫成了同一個迴圈。
>
> **同構本身不是發現。有價值的是它們分岔的那一格：
> agent 的迴圈刻意把「執行」與「評判」拆給不同主體，人的那份明說不准拆。
> 而拆開買到可靠度、賣掉的可能正是 [[open-questions]] Q6 在找的那個東西。**

## 論證

### 支持的證據

**逐格對照。** 左邊是 [[how-to-fix-your-entire-life-in-1-day]] §V 給人的，
右邊是 [[harness-engineering-complete-guide]] §10 給 agent 的：

| Dan Koe（給人） | 原文 | Harness 指南（給 agent） |
|---|---|---|
| 有一個目標 | "To have a goal." | contract |
| 朝目標行動 | "Act toward that goal." | act |
| 感測你在哪 | "Sense where you are." | observe |
| 與目標比較 | "Compare it to the goal." | measure |
| 依回饋再行動 | "And act again based on that feedback." | accept / repair / escalate / stop |

停止條件兩邊也對得上，而且用詞近得可疑：

> Dan Koe：「**The mark of low intelligence is the inability to learn from your mistakes.**」
>
> Harness 指南：「repeated unchanged failure → **stop the loop**」、
> 「**A retry should change at least one relevant condition.**
> Otherwise the system is paying to reproduce the same failure.」

**第二組對照，結構層。** Dan Koe §VII 的六件套對上 [[task-contract]] 的五欄位：

| 六件套 | 任務契約 |
|---|---|
| Vision | `objective` |
| 1 month project / Daily levers | `scope` |
| **Constraints** | `constraints` |
| 1 year goal（一年後可判定的一件具體事） | `acceptance` |
| Anti-vision | **沒有對應** |

`constraints` 兩邊連名字都一樣。

### 反面的證據

**這個同構很可能是無趣的。** 這一節必須寫在支持證據旁邊，不能放在頁尾。

（推論）cybernetics 的詞彙自 1948 年之後滲透進控制論、管理學、認知科學、自助書與軟體工程，
所以**任何一篇談「怎麼把事情做好」的文章都會長成迴圈的形狀**。
兩份來源同時使用 goal / act / sense / compare，可能只證明它們讀過同一批二手材料，
而不是它們各自觀察到了同一個現象。

**兩份來源都是本庫證據等級最低的**（都是零數據的 X 長文、都帶訂閱導流、
都是本庫僅有的兩份 `confidence: low` 來源頁）。
兩個零證據的東西吻合，得到的仍然是零證據。

**Anti-vision 那一格的空缺不能當成發現。** 它可以有兩種解釋，本庫分不出是哪一種：
harness 規格漏了「明確描述要遠離的失敗狀態」這個元件，
或者 agent 根本不需要負面動機，因為它不會因為害怕而拖延。（推論）後者更可能。

## 分岔的那一格

同構不重要，這一節才是。**兩份在「執行者能不能同時當評判者」上給出相反的答案，
而且各自都有很好的理由。**

| | [[harness-engineering-complete-guide]] | [[how-to-fix-your-entire-life-in-1-day]] |
|---|---|---|
| 主張 | worker 與 verifier **不該共享目標**，必要時給 verifier 獨立工具或全新脈絡 | 早上那組挖掘問題 **"Do not attempt to outsource this contemplation to AI"** |
| 理由 | 同一個脈絡裡「再檢查一次」會**保留造成錯誤的那組假設** | 外包會讓你**繞過**心智上的限制器，而突破那個限制器正是重點 |
| 買到什麼 | 可靠度 | 能力 |

（推論）兩邊都對，因為它們要的東西不同。
把迴圈拆給兩個主體，可靠度上升，因為第二個主體不繼承第一個的盲點。
但拆開之後，**沒有任何一個主體跑完整個迴圈**——
而「做出決定 → 看到後果 → 修正」跑完整圈，正是
[[monitoring-does-not-teach]] 說能力累積唯一需要的條件。

這條線接得很直：

- [[bainbridge-ironies-of-automation|Bainbridge 1983]]：監控者拿到後果、拿不到決定，
  所以「there is no opportunity to acquire or maintain the qualities required to
  handle the responsibility」。
- [[the-ai-native-sdlc-playbook]] 把人放在**閘門**上——[[judgment-supply]] 已經指出
  閘門是判斷力的消費端，不是生產端。
- Harness 指南把 verifier 也拆出去，而且要求它
  **有權拒絕而不必負責修好**（[[completion-evidence]]）。
  （推論）這對可靠度是對的設計，對能力累積是又一刀：
  連「發現問題並把它修好」這個完整動作都被拆成兩個主體。

**所以本頁的結論不是「人跟 agent 一樣」，是相反的東西：
迴圈被切開的位置，決定了誰在累積能力。**
agent 的迴圈為了可靠度而切，人的迴圈為了能力而不能切。
（推論）兩者用在同一個工作流程上時，切的方式是被可靠度那一邊決定的，
因為只有可靠度有人量測（[[judgment-supply]] 那張對照表：成本有儀表板，養成沒有）。

## 尚未解決的部分

- **這對 [[open-questions]] Q6 是不是新東西？** 部分是。Q6 既有的機制是
  「工具太好用，人自己不回去」（[[control-group-collapse]] 那條）。
  本頁加的是另一個機制：**即使人還在迴圈裡，迴圈本身已經被切開，
  他站的那一段不含「做出決定」。**（推論）前者是選擇問題，後者是結構問題，
  後者不會因為個人意願而改善。
- **怎麼否證。** 如果本頁成立，長期只擔任 verifier 或閘門審查者的人，
  能力成長應該顯著低於同時執行與驗證的人。可測，**本庫沒有資料，也還沒有來源做過**。
  這與 [[judgment-supply]] H1 的否證條件是同一個實驗。
- **本庫自己就是一個樣本，而且方向不利。** 本庫的 harness 已經照可靠度那一邊切：
  `tools/lint.py` 是確定性檢查、`.claude/rules-ledger.md` 記規則來由、
  使用者站在 ingest 步驟 2 的確認閘門上。（推論）如果本頁的推論對，
  這個設計正在把使用者移到迴圈裡不累積能力的那一段。
  這條沒有解法可提，只能記下來；`[W8]` 的觀察紀錄是目前唯一會累積相關資料的地方。
- **`confidence: low` 的理由**：兩份來源都零數據，同構有更無趣的解釋，
  而分岔那一節的推論鏈（切開迴圈 → 沒人跑完整圈 → 能力不累積）
  中間每一步都是（推論），只有 Bainbridge 那一格有原典支撐。

## 相關頁面

- [[how-to-fix-your-entire-life-in-1-day]] —— 人那一側的來源
- [[harness-engineering-complete-guide]] —— agent 那一側的來源
- [[dan-koe]] —— 人那一側的作者
- [[task-contract]] —— 六件套對上的結構
- [[completion-evidence]] —— 「執行者不能當評判者」的完整版本
- [[monitoring-does-not-teach]] —— 迴圈切開之後誰不累積能力的原典論證
- [[bainbridge-ironies-of-automation]] —— 那個論證的出處
- [[judgment-supply]] —— 本頁補進去的是 Q6 的第二個機制
- [[judgment]] —— 「智力＝操舵」是本庫既有定義的另一種切法
- [[open-questions]] —— Q6 的所在
- [[control-group-collapse]] —— Q6 既有的那個機制，與本頁並列
