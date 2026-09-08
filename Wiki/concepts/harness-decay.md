---
title: harness 的折舊
type: concept
aliases: [harness decay, build to delete, 鷹架折舊]
tags: [ai, agent, harness, 工作方法]
created: 2026-09-08
updated: 2026-09-08
status: active
confidence: medium
sources: ["[[harness-engineering-complete-guide]]", "[[prompting-claude-opus-5]]", "[[wikiskill]]"]
---

# harness 的折舊

> 折舊的不只是規則檔，是**整個 harness**。
> 為舊模型做的 workaround 留在原地，會擋住新模型改用更好的策略。
> **最好的 harness 不是最大的那個，是最小的那個。**

## 折舊鏈

[[harness-engineering-complete-guide]] §15 給的機制：

```
old model limitation
  -> harness workaround
      -> model improves
          -> workaround remains
              -> system becomes slower or less capable
```

關鍵在第四步：**workaround 不會自己消失**，因為它當初解決了一個真問題，
而沒有人負責宣告那個問題已經不存在。

[[prompting-claude-opus-5]] 是本庫唯一一份實際走完這條鏈的文件：
它逐條列出哪些為前代調校的指令在 [[claude-opus-5]] 上已經變成成本
（過度驗證、多餘的子 agent 委派、視覺 workaround）。
差別在於那份只處理**寫下來的指令**，本頁處理的是**建起來的機制**。

## 五個汰除問題

原文要求對每一個 router、evaluator、記憶層與重試規則逐一問：

1. 這防的是**哪一種**失敗？
2. 那種失敗現在**還多常發生**？
3. 它加了多少延遲與複雜度？
4. 同樣的結果現在有沒有更簡單的達法？
5. **移掉會怎樣？**

> "The best harness is not the largest one. It is **the smallest system that reliably closes the
> gap between intent and evidence**. **Build to delete.**"

## 這一頁與 prompt-obsolescence 的分工

[[prompt-obsolescence]] 已經記了三層折舊（規則檔、測量結果、量測方法本身）。
本頁不是第四層，是把**第一層的對象放大**：

| | [[prompt-obsolescence]] 第一層 | 本頁 |
|---|---|---|
| 折舊的東西 | 寫在 `CLAUDE.md`／skill 裡的**文字** | router、verifier、記憶層、重試規則、工具閘門——**整套機制** |
| 偵測 | eval suite 通過率（[[agent-config-evals]]） | 同上，但要能逐元件關掉重跑 |
| 移除成本 | 刪幾行 | 可能要拆掉一段基礎設施 |

（推論）放大之後有一個新的難處：規則檔的一行刪掉幾乎沒有成本，
**一個跑了半年的 verifier 子 agent 沒有人敢關**——它防過的失敗不會留下紀錄，
而它每天燒的 token 會出現在帳單上。折舊在這一層是**不對稱可見**的：成本看得到，效益看不到。

## 原文自己沒調和的張力

§14 與 §15 直接互推，而原文並置卻沒處理：

| 節 | 主張 |
|---|---|
| §14 harness flywheel | "A corrected answer helps one run. **A corrected harness helps every future run.**" —— 每次失敗都該留下新的 sensor、規則、地圖、測試或工具契約 |
| §15 harness decay | "**Build to delete.**" —— 每個元件都要能回答「移掉會怎樣」 |

只做 §14，harness 單調成長；只做 §15，同一種失敗會反覆發生。
（推論）兩者要並存，**每個被加進來的元件從一開始就得帶著它的汰除條件**——
否則 §14 的產物在 §15 的檢查裡全部無法評估，因為沒有人記得它防的是什麼。

## 本庫已經在做這件事，而且是獨立想到的

`.claude/rules-ledger.md` 的 `[W8]` 要求：新規則進帳時寫一句**可否證的預期效果**
（這條該讓哪一種錯誤變少、怎麼量、目前基準線是多少）。
`[W9]` 的否決帳則記下被丟掉的提案與**什麼會讓它重新成立**。

這兩條對上原文五個汰除問題的第 1、2、5 問，而且是本庫在 2026-08-30 自己加的，
比本份來源早了一週，互不知道對方。

（推論）這不提高本庫規則的正確性——兩邊都沒有數據。
它的意義是把「規則帳」從一個本地習慣變成**有第二個人獨立收斂到的做法**，
也就是 [[open-questions]] Q15 在本庫尺度那個版本的旁證。

**兩邊都沒解決的同一件事**：`[W8]` 要求寫預期效果，但本庫至今
**沒有任何一條規則因為預期效果沒兌現而被刪掉**（見 Q10 結案時的紀錄：一條都沒刪）。
原文也沒有給任何「刪掉之後變好了」的例子。**兩份都只有汰除的協定，沒有汰除的實例。**

## 一個實驗證據

本頁的機制在 [[wikiskill]] 有一筆受控數據，雖然它換的是模型而不是模型版本：
Qwen-3.5-4B 演化出來的 skill 給 Gemini-3.5-Flash 用，SpreadsheetBench
從 50.5% 掉到 **18.1%**——比完全沒有 skill 還差 32.4 分。
原因正是本頁的折舊鏈：那些 skill 編碼的是小模型的權宜之計，
**限制**了強模型改用完整端到端腳本。見 [[skill-transfer-across-models]]。

（推論）這是「workaround remains」造成的傷害第一次被量出來，而且它不是變慢，是變差。

## 相關頁面

- [[harness-engineering-complete-guide]] —— 來源
- [[prompt-obsolescence]] —— 折舊的三層，本頁放大它的第一層
- [[harness-engineering]] —— 被折舊的對象
- [[agent-config-evals]] —— 偵測折舊的機制
- [[skill-transfer-across-models]] —— 折舊傷害的實驗證據
- [[wikiskill]] —— 那筆數據的來源
- [[ai-development-economics]] —— 折舊讓 CapEx 變成 CapEx 加 OpEx
- [[open-questions]] —— Q15 在本庫尺度的版本
- [[completion-evidence]] —— 汰除的前提是知道每個元件防的是什麼失敗
