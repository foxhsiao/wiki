---
title: AI 開發的經濟學
type: concept
aliases: [CapEx OpEx, token economy]
tags: [ai, 軟體工程, 經濟]
created: 2026-08-01
updated: 2026-09-01
status: active
confidence: medium
sources: ["[[bainbridge-ironies-of-automation]]", "[[the-new-sdlc-with-vibe-coding]]", "[[the-ai-native-sdlc-playbook]]", "[[ironies-of-automation-public-service]]", "[[running-a-software-factory-at-uber-scale]]"]
---

# AI 開發的經濟學

> 速度不是重點，**總持有成本**才是。兩種工作方式把負擔推到不同的地方。

## 兩種成本結構

| | Vibe coding | Agentic engineering |
|---|---|---|
| CapEx（前期投入） | 幾乎為零——靠模型的基線能力 | 高——設計 API schema、建確定性測試套件、結構化脈絡 |
| OpEx（持續成本） | **高且複利** | 低——邊際交付與維護成本大幅下降 |

## Vibe coding 的三筆隱藏債

1. **Token 燃燒率**：把大而無結構的檔案倒進脈絡視窗，反覆要模型修它自己未驗證的錯誤。
   這個「提示迴圈」在**低首次成功率**下燒 token。
2. **維護稅**：缺乏結構一致性。六個月後出 bug，工程師要花好幾天逆向工程 AI 生成的義大利麵。
3. **資安補救**：沒有自動化評估 harness，快速生成程式碼等於快速生成漏洞。
   生產環境修一個資安缺陷的成本，比設計階段抓到高出指數級。

## 三個壓低 OpEx 的槓桿

1. **[[context-engineering|脈絡工程]]作為財務策略**：給密度高、訊噪比高的 payload
   （精確的 `AGENTS.md` 與架構護欄），而不是龐雜的雜訊，直接拉高**首次成功率**。
2. **動態脈絡與 [[agent-skills|skills]]**：只為當下用到的能力付 token。
3. **智慧模型路由**：複雜任務（需求、架構、初步實作）走大模型；
   確定性的低複雜度任務（測試生成、程式碼審查、CI/CD 監控）自動路由到更小更快更便宜的模型。

## CapEx 不是一次性的

本頁把 harness 算成前期投入換低 OpEx。兩份後續來源都在拆這個假設：

- [[prompt-obsolescence]]：規則檔會隨模型換代折舊，有些條目從資產變成負債。
- [[the-ai-native-sdlc-playbook]]：維持它需要**持續支出**，而且原文自己標出了成本項——
  [[agent-config-evals|eval suite]] 要有預算跑（20–50 條、非互動跑真實 session、
  每次改設定與每日排程各跑一次）、每個事故要有人寫一條新 eval、
  Claude Security 的排程掃描按用量計費且要求設定支出上限。

（推論）比較誠實的算法是 **CapEx + 持續 OpEx**：
harness 是資產，但它有折舊、有保養費，而保養費隨 repo 數與事故數成長。
原文留的出口是「有些團隊可能偏好照固定週期離線跑 eval，而不是每次改動都跑」——
也就是**用鑑別度換成本**。

## 從定性說法變成可分解的量測

本頁到此為止都是**結構性的說法**：CapEx vs OpEx、三筆隱藏債、三個槓桿。
[[running-a-software-factory-at-uber-scale|Uber]] 把它換成了可以逐項量測的東西——
一次 agent session 的花費被拆成**六項相乘的因子**，各自量測、各自優化。

（本庫只知道其中三項出現在小節標題：price／token、tokens／request、requests／turn。
**六項的完整清單只存在於原文的圖裡，那張圖沒有抓到**，所以本頁不列。見來源頁的〈原檔的缺漏〉。）

原文對這六項的分工說得很清楚：

> "The three middle terms provide opportunities for optimization: **the work the agent does on its
> own behalf, on top of the request an engineer actually made**. That is where most of our effort goes."

（推論）這句話把本頁的「三筆隱藏債」講得更準：真正在燒錢的不是工程師提的那個需求，
是 **agent 為了完成它而自己給自己加的工作**——多餘的回合、找不到東西的搜尋、
重複的推理、被反覆重送的 schema（[[context-tax]]）。

## 第一組真實世界的成本數字

固定模型、2026-02 到 07：

| 指標 | 變化 |
|---|---|
| cost per 1,000 model requests | 自高點下降將近 **34%** |
| cost per session | 自 6 月高點下降 **52%** |

同期用量成長 7 倍（週活躍使用者）、9.4 倍（每週 agentic requests），總支出自 4 月起相對持平。

**方法比數字重要**：

> "isolating our own optimization gains means **holding one model fixed**, since behavior shifts
> with every upgrade and model family."

（推論）這對本頁的 CapEx 論述有個不舒服的意涵：如果每次模型升級都會改變成本結構，
那 harness 的投資不只要重驗**有沒有效**（[[prompt-obsolescence]]、Q11），
還要重驗**划不划算**。兩者的重驗週期都是「每幾週」。

要打的折：這是自陳、未經稽核的工程部落格，而且**成功的定義是成本不是品質**——
原文說品質有維持或改善，但沒有給任何全公司層級的品質數字。

## 判讀

（推論）這一節是白皮書裡最像賣點的部分——三個槓桿剛好都指向 Google 的產品線。
但 CapEx／OpEx 的框法本身站得住，而且它給了一個很實用的檢查問題：
**你現在的做法，成本是被推到前面還是被推到六個月後？**

「首次成功率」值得當成可量測的指標追蹤，白皮書沒給任何實際數字。

## 成本被掩蓋，這條有先例

[[ironies-of-automation-public-service]] 的反諷 #5：
自動化為了省人力成本，卻在組織他處生成本（IT、更高技能人員、外部顧問），
而且**分散在多個功能與部門**，因此**掩蓋了自動化的總成本**。
結果自動化可能比人工更貴，而組織不自知。

（推論）這與本頁的 CapEx／OpEx 框架接得上，但指出一個本頁沒處理的問題：
**不是成本算錯，是成本根本沒被歸戶。** 本頁假設你算得出總持有成本；
反諷 #5 說在真實組織裡那個數字通常沒有人在算。

注意 Lindgren 明說**反諷 #5 是她自己的產物**、不是 Bainbridge 的，
而且應視為待進一步檢驗的假說。

## 一句把這頁算法翻過來的話

[[bainbridge-ironies-of-automation|Bainbridge 1983]] 的結尾：

> "Perhaps the final irony is that it is **the most successful automated systems, with rare
> need for manual intervention, which may need the greatest investment in human operator
> training**."

（推論）本頁的 CapEx／OpEx 框架預設自動化程度愈高、人力成本愈低。
這句話說相反：**自動化愈成功，訓練投資愈高**——
因為需要人介入的次數愈少，人愈沒機會維持介入所需的能力
（[[monitoring-does-not-teach]]），於是只能靠刻意的、不產出的訓練來補。

本頁與 [[ai-native-sdlc]] 都沒有把訓練列成成本項。

## 相關頁面

- [[the-new-sdlc-with-vibe-coding]] —— 來源
- [[context-engineering]] —— 最大的那根槓桿
- [[agent-skills]] —— 動態脈絡的載體
- [[vibe-coding-spectrum]] —— 成本結構對應光譜位置
- [[the-ai-native-sdlc-playbook]] —— harness 的持續成本項
- [[agent-config-evals]] —— 最主要的那筆持續支出
- [[prompt-obsolescence]] —— 折舊那一面
- [[ironies-of-automation-public-service]] —— 反諷 #5：成本沒有被歸戶
- [[bainbridge-ironies-of-automation]] —— 最成功的自動化需要最多訓練投資
- [[running-a-software-factory-at-uber-scale]] —— 第一組真實世界的成本數字
- [[context-tax]] —— 六項裡最容易被忽略的那一筆
- [[managed-agents]] —— 把成本收回可控位置的組織做法
