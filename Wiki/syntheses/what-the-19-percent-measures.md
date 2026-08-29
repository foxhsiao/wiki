---
title: 那 19% 到底測到了什麼
type: synthesis
aliases: [what the 19% measures, METR 的兩面]
tags: [ai, 論點, 生產力, 方法學]
created: 2026-08-29
updated: 2026-08-29
status: active
confidence: medium
sources: ["[[metr-early-2025-ai-developer-productivity]]", "[[the-new-sdlc-with-vibe-coding]]", "[[elephants-goldfish]]", "[[the-ai-native-sdlc-playbook]]"]
---

# 那 19% 到底測到了什麼

> 本庫把 METR 的「慢 19%」當成站在「判斷力無法外包」那側的硬數據用了四週。
> 讀完原始研究之後：**這個用法是誤讀。**
> 但同一份研究在另一條線上給了本庫真正的外部支持。兩面都要寫。

## 先看五個因子是什麼

[[metr-early-2025-ai-developer-productivity]] 調查了 20 個可能造成拖慢的因素，
找到證據支持其中五個：

| 因子 | 它在講什麼 |
|---|---|
| Over-optimism about AI usefulness | 人對 AI 的信念錯誤 |
| High developer familiarity with repositories | **人類**表現特別高 |
| Large and complex repositories | 環境對 AI 不利 |
| Low AI reliability | 工具本身不夠好 |
| Implicit repository context | 環境裡有 AI 拿不到的知識 |

**沒有一個因子是關於人類判斷力不可替代。**

## 削弱本庫的部分

### 1. 本庫的引用是誤讀

[[can-judgment-be-outsourced]] 把 METR 的數字寫成
「本庫第一次有**數據**站在『判斷力無法外包』那一側」，[[overview]] 主軸 2 也這樣用。

但五個因子指向的是**工具與情境**：模型不夠可靠、repo 太大、隱性知識沒被編碼、人高估了 AI。
這些全都是**可以被改善的條件**，不是「判斷力屬於人類」的證據。
一份研究說「在這個設定下 AI 幫倒忙」，不等於說「這裡需要的東西教不來」。

### 2. 有一部分是人類特別快，不是 AI 特別慢

因子 2 的機制標註是 **Raises developer performance**——
受試者在自己長期貢獻的大型 repo 上工作，而且在先前接觸度高的 issue 上**變慢更多**。

（推論）這代表 19% 裡有一塊來自基準線被拉高。換一批對 repo 不熟的人，
差距很可能縮小甚至反向。「AI 讓開發者變慢」這個標題比它的資料更強。

### 3. harness 假說是未經檢驗的

最誘人的解釋是：受試者用的是 Cursor Pro，而 METR 自己承認
「Cursor 取樣的 token 不多，可能沒有最佳的提示或鷹架」。
所以那 19% 測到的其實是**那套 harness 讓人變慢**，不是 AI 讓人變慢——
這正好印證 [[harness-engineering]] 的「多數 agent 失敗其實是設定失敗」。

**這條救援要非常小心。** 那句話出現在原文的
「我們**不**提供證據支持」表格裡——它是作者主動劃出的界線，**不是他們的發現**。
而且「Non-frontier model usage」在被排除的六個因子裡，
也就是說 METR 檢驗過模型夠不夠新，但**沒有檢驗鷹架夠不夠好**。

拿一個未經檢驗的假說去救本庫另一個未經檢驗的主張，只是把問題往後推一層。
正確的寫法是把它當**待驗證的假說**，不是當證據。

### 4. 更糟的是，harness 那條線的證據基礎被同一份研究削弱

[[harness-engineering]] 最硬的兩個數字——Terminal Bench 只改 harness 進 Top 5、
LangChain +13.7 分——**都是 benchmark**。
而 [[evidence-types-for-ai-capability]] 記的正是 METR 的判斷：
benchmark 因為只量「範圍界定良好、可演算法評分」的任務而**傾向高估**，
且難以直接翻譯成真實世界的影響。

所以這份研究對 harness 論述是雙面的：給了它一個可能的立足點，
同時抽掉了它原本站的那塊地。

### 5. 而且這個數字已經被作者宣告過期

原文頁首的橫幅：「我們相信這些歷史結果已不反映 AI 模型對開源開發者生產力的當前影響」。
在 2026-02-24 的後續研究被 ingest 之前，這 19% 只能當**歷史測量**引用。
這本身是 [[prompt-obsolescence]] 的新實例——不只規則檔會折舊，**測量也會**。

## 支持本庫的部分

### 1. 隱性脈絡被實證指認為瓶頸

因子 5 **Implicit repository context** 的機制標註是
「限制 AI 表現，**同時**拉高人類表現」——AI 缺少資深開發者仰賴的隱性程式碼庫知識。

討論段講得更具體：AI 的表現在「品質標準很高、或**有很多隱性要求**
（文件、測試覆蓋率、lint／格式）——那些人類要花很多時間才學會的東西」的場景相對更低。

**那正是 `CLAUDE.md`、skill、[[artifact-chain|產物鏈]]在編碼的東西。**
[[context-engineering]] 的核心提問——「一個新來的隊友需要知道什麼才能有效貢獻，
我怎麼把那份知識編碼成 AI 能用的形式」——在這裡拿到了外部的、實證的支持。

這個支持比表面上更有份量，因為它來自一份**結論對 AI 不利**的研究。
不是廠商說「用我們的脈絡工具會更好」，是第三方在解釋失敗時指到同一個地方。

### 2. 大型程式碼庫對 AI 不利，支持「設計文件即脈絡」

因子 3 說 repo 平均超過 110 萬行，開發者回報 AI 在複雜環境裡表現更差。
[[design-is-the-new-code]] 的成本論證 **sizeof(docs) << sizeof(code)** ——
用白話設計文件餵脈絡，比逼 AI 讀幾十萬行原始碼便宜可靠——方向一致。

（推論）但注意這只是方向一致，不是驗證。METR 沒有測試「給設計文件會不會改善」。

## 結論：這份研究可以拿來主張什麼

| 主張 | 可以嗎 |
|---|---|
| 自陳的生產力增益可能非常不準 | ✅ 這是研究的直接發現（[[self-report-vs-measurement]]） |
| 隱性脈絡是 AI 在成熟程式碼庫上的瓶頸 | ✅ 因子 5，作者自己的歸因 |
| benchmark 傾向高估真實世界的效用 | ✅ 作者的明確判斷 |
| **判斷力無法外包** | ❌ **五個因子沒有一個支持這件事** |
| AI 讓開發者變慢 | ⚠️ 只在「專家、自己的大型 repo、early-2025 工具」這個切面，且已被作者宣告過期 |
| 好的 harness 就能翻轉這個結果 | ⚠️ 未經檢驗的假說，作者明確表示不提供證據 |

## 尚未解決的部分

- 2026-02-24 的後續研究還沒 ingest。它的估計區間跨過 0，會再次改變上面這張表。
- harness 假說要被檢驗，需要的是同樣設計但換掉鷹架的重跑。沒有人做過。
- 見 [[open-questions]] Q7、Q15。

## 相關頁面

- [[metr-early-2025-ai-developer-productivity]] —— 來源
- [[can-judgment-be-outsourced]] —— 被這一頁指出誤讀的對象
- [[harness-engineering]] —— 同時被支持與削弱的那條線
- [[context-engineering]] —— 拿到外部實證支持的那條線
- [[evidence-types-for-ai-capability]] —— 削弱點 4 的依據
