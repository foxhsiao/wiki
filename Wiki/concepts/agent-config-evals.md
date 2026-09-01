---
title: 設定檔的回歸測試
type: concept
aliases: [continuous evals, agent config evals, eval suite]
tags: [ai, agent, 測試, 工作方法]
created: 2026-08-29
updated: 2026-09-01
status: active
confidence: medium
sources: ["[[the-ai-native-sdlc-playbook]]", "[[prompting-claude-opus-5]]", "[[wikiskill]]", "[[running-a-software-factory-at-uber-scale]]"]
---

# 設定檔的回歸測試

> 操控 agent 的東西——`CLAUDE.md`、skills、hooks——**值得程式碼享有的那種回歸測試**。
> 這是 [[open-questions]] Q11 的直接答案。

## 做法

1. 平台工程師從近期工作蒐集 **20 到 50 個真實任務**，連同期待或已被接受的結果。
2. 每個任務寫成一條 eval：提示，加上「什麼算可接受」的檢查
   （測試通過、lint 乾淨、行為不變、政策被遵守）。
3. suite 在 CI 裡非互動執行，**排程跑**，而且**任何對 `CLAUDE.md`、skills、hooks 的改動都跑**。
4. **設定變更以結果為閘門**：某個 skill 改動讓通過率掉下來，就要先被審查才能 merge。
5. 每一個生產事故都由事故的擁有團隊寫成一條 eval，永久留在 suite 裡當回歸測試。

原文的 GitHub Actions 範例用 `paths: ['CLAUDE.md', '.claude/**']` 觸發，
加上 `cron: '0 2 * * *'` 每日排程，跑 `claude -p` 並限制 `--allowedTools`。

## 為什麼這是 Q11 的答案

[[prompt-obsolescence]] 提出的問題是：規則檔會折舊，
但**版控保存了歷史，卻不會告訴你哪一條已經過期**。
[[prompting-claude-opus-5]] 只說「在自己的 eval 上重跑 sweep」，沒說怎麼判斷哪些規則已經無用。

這一頁補上了流程的形狀：**通過率是唯一的裁判**。換模型、改 skill、刪一條規則，
都在同一組任務上重跑，看分數動不動。折舊因此變成可量測的東西，而不是靠人記得。

**但它沒有完全解決 Q11。** 通過率告訴你「整體有沒有變差」，
不告訴你「是哪一條規則在扣分」。要定位到規則層級，得一條一條移除重跑，成本是線性的。
（推論）這就是為什麼 Q10「每條規則為什麼存在」仍然有價值——
規則的來由能大幅縮小要重驗的範圍。

## 一個會自己老化的東西

> "The evals should be seen as a live suite. As models improve, cases that once discriminated
> stop doing so and new ones must be added that arise from ongoing monitoring."

eval suite 本身也會折舊：模型變強之後，曾經能分辨好壞的案例全部滿分，
suite 就不再有鑑別度。新案例從持續監控裡長出來——這把
[[autonomy-tiering|控制帶]]的事故流接回了測試。

## 它改變了經濟模型

[[ai-development-economics]] 把 harness 算成一次性 CapEx。
維護一組 20–50 條、要跑真實 agent session 的 eval suite 不是一次性成本：
每次排程跑都要付 API 費用，每個事故都要有人寫一條新 eval。
（推論）**harness 從 CapEx 變成 CapEx 加一筆持續的 OpEx。**

原文自己也承認成本問題——它給了一條出口：
「有些團隊可能偏好照固定週期離線跑，而不是每次改動都跑」。

## 與現有測試觀念的接合

[[vibe-coding-spectrum]] 的判準是「輸出怎麼被驗證」，並區分 tests（確定性）與 evals（非確定性）。
這一頁把 eval 的對象往上推了一層：**不只評估 agent 的產出，還評估操控 agent 的設定。**
[[factory-model]] 說開發者的產出是產出程式碼的那套系統——如果那是產出，它就該被測試。

## 一個把這套跑到底的實作

本頁描述的是流程建議。[[wikiskill]] 是本庫第一份**實際跑完這個迴圈並公布結果**的來源，
而且它的 gating 比本頁描述的更硬：

- 候選 skill 在驗證集上**必須超過歷史最佳分數**才被接受，否則整個提案回滾。
- 接受或拒絕，harness 都以程式把提案 metadata、目標 skill、**unified diff**、
  驗證分數、接受結果寫進一份 `skill-impact.md`。
- 驗證分數達到 1.0 就提早結束演化。

接受率很低：以 Qwen-3.5-4B 為例，平均每輪提案新增 3.1 個 skill、**接受 1.6 個**；
提案修改 4.9 次、**接受 1.3 次**。（推論）也就是說**多數對規則檔的「改進」其實沒有改進**，
而本庫至今從來沒有測過任何一次規則改動的效果。

## 被拒絕的提案要留下來

這是本頁原本完全沒有的一格。WikiSkill 的設計是**程序可回滾、知識不回滾**
（[[persistent-knowledge-layer]]），而被拒提案的 diff 就存在不回滾的那一側。原文說用途是：

> "(1) observe the complete skill acceptance history so that **rejected interventions are not
> proposed again**"

（推論）純粹的 gating 只防止壞改動進去，不防止**同一個壞改動被反覆提出**。
本頁列的五個步驟裡沒有任何一步保存被擋下來的東西——CI 擋掉之後，
那次嘗試就只留在某個 PR 的歷史裡，不會出現在下一個 session 的脈絡中。

## 作者自陳的一個代價

WikiSkill 的 gating 要求**每個被接受的提案都要提高驗證分數**，
因此排除了「當下持平、但為後續鋪路」的中性提案。作者把這列為限制。

（推論）這是本頁「通過率是唯一的裁判」那句話的實際代價：
以分數為唯一閘門，會系統性地拒絕重構型的改動。

## 同一套機制，換一個被測的東西

本頁的對象是**設定**（`CLAUDE.md`、skills、hooks）。
[[running-a-software-factory-at-uber-scale|Uber]] 把同一套機制用在**選模型**上，
而且是全公司每個受管 agent 的固定流程：

1. 從該 agent 的**真實工作**建 benchmark。
2. 在一個能接任何模型（前緣或開放權重）的 harness 上跑。
3. 移到 Pareto 最優的那個，然後**持續移動**——原文說前緣每幾週就變一次。

uReview（處理所有 PR 的程式碼審查 agent）的 benchmark 是**從已知有 bug 的真實 PR** 建的，
分易／中／難，評分是 precision、recall、F1，外加每次審查成本、延遲、逾時、雜訊。

（推論）這與本頁的差別只在**變數放在哪一格**：本頁固定模型、改設定、看通過率；
Uber 固定 benchmark、換模型、看 Pareto 前緣。**常設的是 benchmark，可換的是其餘一切。**
兩者合起來說明本頁那句「操控 agent 的東西值得程式碼享有的回歸測試」的完整版本——
被測的不只是設定，是**agent 的整個組成**。

它也補上本頁沒有的一個判準：Pareto 最優在這裡定義為
**每個完成任務的成本、輸出品質、模型可靠度**三者一起看，不是單看通過率。

## 相關頁面

- [[the-ai-native-sdlc-playbook]] —— 來源
- [[prompt-obsolescence]] —— 這一頁回答的問題
- [[open-questions]] —— Q11 的狀態因此改變
- [[vibe-coding-spectrum]] —— tests 與 evals 的區分
- [[ai-development-economics]] —— 持續成本改變 CapEx 的算法
- [[autonomy-tiering]] —— 事故流是新 eval 的來源
- [[wikiskill]] —— 把這套迴圈跑完並公布結果的實作
- [[persistent-knowledge-layer]] —— 被拒提案該存在哪一層
- [[running-a-software-factory-at-uber-scale]] —— 同一套機制用在選模型上
- [[managed-agents]] —— 每個受管 agent 配一組 benchmark 的做法
