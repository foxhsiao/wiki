---
title: 規則檔的折舊
type: concept
aliases: [prompt obsolescence, 提示過期]
tags: [ai, agent, 工作方法]
created: 2026-08-02
updated: 2026-09-01
status: active
confidence: medium
sources: ["[[prompting-claude-opus-5]]", "[[the-ai-native-sdlc-playbook]]", "[[metr-early-2025-ai-developer-productivity]]", "[[metr-2026-uplift-update]]", "[[wikiskill]]"]
---

# 規則檔的折舊

> 為某個模型版本寫的護欄，在下個版本可能變成成本來源。
> **harness 不是純資產，它有折舊。**

## 證據

[[prompting-claude-opus-5]] 是本庫目前唯一處理這件事的來源，而且它的形式很特別：
整份文件叫你**刪東西**，不是加東西。

| 曾經是最佳實務 | 在 [[claude-opus-5]] 上變成 |
|---|---|
| 「為任何非瑣碎任務加入最終驗證步驟」 | 過度驗證，浪費 token 且品質不變 |
| 「用子 agent 驗證你的工作」 | 同上，且乘以委派成本 |
| 「再檢查一次」「回應前重新驗證」 | 與模型自身的自我修正疊加 |
| 為前代調校的視覺 workaround | 可能已經不需要 |
| 沿用的 effort 預設值 | 需要在自己的 eval 上重跑 sweep |
| 「不要思考」「不要推理」 | **提高內部標籤洩漏機率** |

還有一條反直覺的：審查任務寫「只回報高嚴重度」或「保守一點」，
模型會照字面遵守而**少報**——該叫它全報再另一輪過濾。

## 為什麼這對既有框架是個問題

本庫收錄的其他來源都把 harness 當成純資產：

- [[harness-engineering]] 說「投資 harness 元件作為團隊共享資產，建一次、精煉很多次」
- [[elephant-goldfish-model]] 說設計文件「是你新的原始碼」
- [[ai-development-economics]] 把 harness 算成 CapEx，前期投入換低 OpEx

**沒有一份處理版本升級時的折舊。** 如果每次模型換代都要重新驗證整套規則檔，
那 CapEx 就不是一次性的，[[ai-development-economics|經濟模型]]要重算。

## 可操作的推論

（推論）規則檔應該像程式碼一樣有「棄用」流程：
每條規則要能追到它為什麼被加進來（哪個模型的哪個失效模式），
否則升級時你分不清哪些還需要、哪些已經在扣分。

[[harness-engineering]] 建議把規則檔當程式碼版控——這是對的，但還不夠：
**版控保存了歷史，卻不會告訴你哪一條已經過期。**

## 折舊怎麼被偵測（部分解答）

這一頁原本的結論是：版控保存了歷史，卻不會告訴你哪一條已經過期。
[[the-ai-native-sdlc-playbook]] 給了流程上的答案——
把 `CLAUDE.md`、skills、hooks 當成**要被回歸測試的設定**，
用 20–50 個真實任務組成的 eval suite 在 CI 跑，通過率掉了就擋 merge
（[[agent-config-evals]]）。

**這解決了偵測，沒解決定位。** 通過率告訴你整體變差了，
不告訴你是哪一條規則在扣分；要定位得逐條移除重跑。
所以 [[open-questions]] Q10「每條規則為什麼存在」仍然有價值——
來由能大幅縮小要重驗的範圍。

代價也要記下來：這讓 harness 從一次性 CapEx 變成 CapEx 加持續 OpEx。
見 [[ai-development-economics]]。

## 不只規則檔會折舊，測量也會

[[metr-early-2025-ai-developer-productivity]] 把這一頁的範圍推廣了一級。
那份 2025-07-10 的隨機對照試驗，**作者自己在原文頁首掛橫幅宣告它過期**：

> "We believe these historical results no longer reflect the current impact of AI models
> on open-source developer productivity."

這是本庫第一頁 `status: stale`，而且不是我們判斷它過期，是來源自己說的。

差別值得記下來：規則檔的折舊要靠 [[agent-config-evals|eval suite]] 才偵測得到，
**一份被引用的測量結果過期時，引用它的人通常不會收到通知**。
Google 白皮書（2026-05）引用這個 19% 時，就沒有提到任何時效限定。

（推論）所以 `sources` 欄位不只要記「哪一份來源」，還要記「那份來源什麼時候被測量」。
本庫目前沒有這個欄位——來源頁有 `published`，但引用它的概念頁看不到。

## 折舊的第三層：量測方法本身

[[metr-2026-uplift-update]] 把這一頁再推一級。三層由淺到深：

| 層 | 什麼過期 | 實例 |
|---|---|---|
| 1 | **規則檔** | [[prompting-claude-opus-5]] 列出該刪的指令 |
| 2 | **測量結果** | [[metr-early-2025-ai-developer-productivity]] 被作者宣告過期 |
| 3 | **量測方法本身** | RCT 因為受試者拒絕無 AI 條件而失效（[[control-group-collapse]]） |

第三層最麻煩，因為前兩層都還有辦法偵測——
規則檔靠 [[agent-config-evals|eval suite]]、測量結果靠作者更新。
但方法失效時，你拿到的是**看起來正常的數字**，只有做研究的人知道它不能解讀。

（推論）而驅動這三層的是同一件事：工具變好。
**工具愈有價值，關於它的知識折舊愈快。**

## 第一層終於有實驗證據了

本頁的第一層（規則檔會折舊）一直只有一份供應商文件撐著。
[[wikiskill]] 提供了一個**受控的同構實驗**：換的不是模型版本，是模型本身。

同一份演化出來的 skill 換一個模型使用，可能**大幅倒退**：
Qwen-3.5-4B 演化的 skill 讓 Gemini-3.5-Flash 在 SpreadsheetBench
從 **50.5% 掉到 18.1%**——比完全沒有 skill 差 32.4 分。
換成 Qwen-3.6-27B 演化的 skill 則升到 63.4%。

原文的錯誤分析指出機制：4B 的 skill 編碼的是**低階權宜之計**
（單行 Python 指令、字串轉換規則），這些讓小模型避開執行失敗，
卻**限制**強模型改用完整的端到端腳本；破碎的診斷步驟還會耗光互動預算。

（推論）這就是本頁那張表在講的事，只是用實驗做出來的：
**為某個模型的弱點寫的規則，在沒有那個弱點的模型身上是純粹的成本。**
本頁原本只能說「供應商說會這樣」，現在可以說「有人測到，而且量到 32.4 分」。
展開見 [[skill-transfer-across-models]]。

判準也跟著清楚了一格：**寫通則的規則會活下來，寫補丁的規則會折舊。**
（推論）所以規則檔的來由裡該記的不只是「為什麼加」，還有
**「這是通則還是補丁」**——後者從寫下的那一刻就該預期它會過期。

## 只增不減的知識庫沒有出口

[[wikiskill]] 的設計是知識層**永不重置**（[[persistent-knowledge-layer]]），
而作者自己把「**沒有自動 pruning 機制**」列為限制：
pattern 頁、演化日誌、提案 diff 持續累積，跑久了可能需要修剪。

（推論）這是本頁與那個設計之間的直接張力。永不重置保護了學習速度，
但它同時保證了**過期的知識沒有出口**。兩邊都對，而沒有人給出調和的機制——
`[L5]` 的保留型／維護型之分是本庫目前的答案，但那是靠人工健檢執行的，
不是自動的。

## 對本知識庫自己的意涵

`CLAUDE.md` 目前沒有這份文件點名的反模式（沒有「再檢查一次」這類指令，
第 9 步跑的是 `tools/lint.py` 這種確定性工具而非模型自我複查，這是被推薦的做法）。
但它也沒有記錄**每條規則為什麼存在**。見 [[open-questions]] Q10。

## 相關頁面

- [[prompting-claude-opus-5]] —— 來源
- [[harness-engineering]] —— 被這條挑戰的框架
- [[claude-opus-5]] —— 觸發這個觀察的版本差異
- [[ai-development-economics]] —— 折舊改變 CapEx 的算法
- [[agent-config-evals]] —— 偵測折舊的做法
- [[the-ai-native-sdlc-playbook]] —— Q11 的部分答案
- [[metr-early-2025-ai-developer-productivity]] —— 測量也會折舊的實例
- [[metr-2026-uplift-update]] —— 折舊的第三層
- [[control-group-collapse]] —— 方法失效的機制
- [[wikiskill]] —— 第一層的實驗證據
- [[skill-transfer-across-models]] —— 補丁型規則怎麼害到別的模型
- [[persistent-knowledge-layer]] —— 永不重置與折舊之間的張力
