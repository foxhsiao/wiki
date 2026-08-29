---
title: 判斷力
type: concept
aliases: [judgment, 品味, taste]
tags: [能力, ai, 職涯]
created: 2026-08-01
updated: 2026-08-29
status: active
confidence: high
sources: ["[[arm-yourself-with-specific-knowledge]]", "[[elephants-goldfish]]", "[[the-new-sdlc-with-vibe-coding]]", "[[prompting-claude-opus-5]]", "[[the-ai-native-sdlc-playbook]]"]
---

# 判斷力

> 在複雜環境裡做模式比對累積出來的東西。三份來源、跨七年、領域各異，
> 都把它指認為**唯一不會貶值的能力**——目前是本庫收斂度最高的一條。

## 三種說法

**[[naval-ravikant|Naval]]（2019）**：判斷力是四件套之一，靠在職訓練累積——
在高度複雜的環境裡做模式比對。他舉的例子刻意平凡：投資是經典款，但也可以是
「管一支卡車隊的判斷力」或「氣象預報的判斷力」。它與[[specific-knowledge|特定知識]]同源，
都不是能被教出來的。

**[[dave-rensin|Rensin]]（2026）**：公司雇你就是為了判斷力。
資淺的人是公司賭你能快速累積它；資深的人是公司買你已經累積的那份。
而模型**做不到這種判斷，只是非常擅長生成表面上像判斷的字串**。

> "Do not make the mistake of outsourcing your judgment to the machine."

**[[addy-osmani|Osmani]] 等（2026）**：白皮書的收尾句是
「**Generation is solved. Verification, judgment, and direction are the new craft.**」
並把它變成組織建議：**依判斷力而非實作能力重新設計招募**——
瓶頸從實作移到規格、評估、架構判斷與審查。
這是三份來源裡唯一把判斷力接到可執行的人事決策上的。

## 交會點

兩人的差別在於下一步：
Naval 沒有處理「判斷力如何規模化」；Rensin 的整套 [[elephant-goldfish-model]]
就是在做這件事——把判斷力**寫成文件**，讓 agent 照著執行。

這產生一個張力：判斷力若能被完整寫進設計文件，它還算「教不來」嗎？
論證見 [[can-judgment-be-outsourced]]。

## 第四份來源換了說話的人

前三份都是**人在談人的判斷力**。[[prompting-claude-opus-5]] 是供應商在談**模型的判斷**——
而且用的是同一個詞：模型「對任務應該是什麼行使自己的判斷」。

它被寫在文件裡是因為它是個**要被約束的問題**，不是賣點。
但這句話本身就讓「判斷力是人類專屬」這個前提站不住了。
展開見 [[can-judgment-be-outsourced]] 與 [[agent-autonomy-cost]]。

## 第五份來源：判斷力有位置了

前四份都在談判斷力**是什麼**。[[the-ai-native-sdlc-playbook]] 是第一份談它**該放在哪**的來源：

> "Human attention concentrates at the gates, reviewing what the agent flagged rather than
> starting each stage from scratch."

> "Humans remain accountable for every decision that requires judgment.
> In the agentic SDLC world, **the human attention shifts along with the artifacts that must be reviewed**."

具體的落點是六個閘門：接受 `intent.md`、簽核 `spec.md`、核准 `plan.md`、
code owner 的 PR 核准、生產發布授權、事故發現的分流。
每個閘門都問同一組問題——**這個變更做的是計畫要做的事嗎，風險可以接受嗎**。

全文最後一句把立場講完：

> "The loop keeps running. Human judgement stays above it."

（推論）這是本庫第一次有來源把判斷力接到**具體的介面**上，而不只是接到人事決策。
但它同時暴露一件事：閘門上的判斷是**審查別人做完的東西**，
不是在複雜環境裡從頭做模式比對。如果 Naval 對判斷力來源的說法成立，
這種形狀的判斷力可能無法自我再生產——見 [[open-questions]] Q6。

## 怎麼練

- Naval：靠真實好奇心撐住長期投入，靠[[first-principles-foundation|第一原理地基]]分辨真假。
- Rensin：靠[[ai-as-interrogator|被拷問]]逼出自己的盲點；靠持續專注的肌肉訓練
  （每天 30–45 分鐘起跳，每週加 5–10 分鐘）。

## 各來源怎麼說

| 來源 | 說法 | 日期 |
|---|---|---|
| [[arm-yourself-with-specific-knowledge]] | 四件套之一，在複雜環境做模式比對而來 | 2019-03 |
| [[elephants-goldfish]] | 公司買的就是它；模型只會模仿它的表面 | 2026-04 |
| [[the-new-sdlc-with-vibe-coding]] | 生成已被解決，驗證／判斷／指揮才是新技藝；照判斷力招募 | 2026-05 |
| [[prompting-claude-opus-5]] | **模型會「對任務應該是什麼行使自己的判斷」**，且被列為需要約束的行為 | 2026 |
| [[the-ai-native-sdlc-playbook]] | 人的判斷力集中到**閘門**上；迴圈一直跑，人的判斷留在它上面 | 2026 |

## 相關頁面

- [[specific-knowledge]] —— 同源概念
- [[can-judgment-be-outsourced]] —— 兩份來源的對撞
- [[elephant-goldfish-model]] —— 把判斷力寫成文件的具體做法
- [[ai-as-interrogator]] —— 逼出判斷力的方法
- [[the-80-percent-problem]] —— 剩下那 20% 就是判斷力的所在
- [[conductor-and-orchestrator]] —— 判斷力被消耗的兩種模式
- [[the-ai-native-sdlc-playbook]] —— 判斷力在流程裡的落點
