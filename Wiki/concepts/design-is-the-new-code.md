---
title: 設計即新的程式碼
type: concept
aliases: [Design is the new code]
tags: [ai, 軟體工程]
created: 2026-08-01
updated: 2026-08-29
status: active
confidence: medium
sources: ["[[elephants-goldfish]]", "[[the-new-sdlc-with-vibe-coding]]", "[[the-ai-native-sdlc-playbook]]"]
---

# 設計即新的程式碼

> 當程式碼由 AI 寫，人不再留下那串微決策。若不強迫決策**左移**進設計文件，
> 系統對最終要負責的那個人就是不可理解的。

## 論證

歷史上設計判斷存在兩個地方：設計文件，以及程式碼本身。
人寫程式時，會在邏輯裡留下一路的微決策痕跡。AI 寫程式時，那些痕跡不存在。

[[dave-rensin|Rensin]] 認為終局只有兩種，而且**哪一種成真都不重要**：

1. 模型產出的程式碼多到人類不可能全部審查；
2. 模型直接產出二進位檔，跳過程式碼。

> "Whether in a blizzard or a binary, the code is going to become opaque to us
> and when the code becomes opaque, the only artifact that matters is the design."

配套的成本論證是 **sizeof(docs) << sizeof(code)**：
用白話設計文件餵脈絡，比逼 AI 讀幾十萬行原始碼便宜、快、可靠。

## 為什麼這是責任問題不是效率問題

最後會有一個**人**為 agent 的行為負責。
如果那個人不真的理解系統，他沒有理由承擔那個風險。
所以把設計判斷逼進人類可讀、且經過嚴格測試（[[elephant-goldfish-model|金魚測試]]）的文件，
是把「人的理解需求」和「AI 的速度」對齊——作者稱之為終極的去風險。

## 第二份來源怎麼說同一件事

[[the-new-sdlc-with-vibe-coding]] 沒有用這個詞，但 [[factory-model|工廠模型]]
是同一主張的另一種說法：開發者的產出是**產出程式碼的系統**，不是程式碼。
白皮書的收尾句更直接：「Generation is solved. Verification, judgment, and direction
are the new craft.」

一個差別值得記下來：Rensin 要求設計文件列出**每一個**會被改動的檔案；
白皮書說「給 agent 成功判準而不是逐步指令」。兩者表面衝突，
可能的調和是層級不同（架構層給判準、實作層給清單），但兩份來源都沒處理。

## 爭議與矛盾：唯一算數的產物是哪一個

[[the-ai-native-sdlc-playbook]]（2026-08）對同一個問題給了不同答案。

| | [[elephants-goldfish]]（2026-04） | [[the-ai-native-sdlc-playbook]]（2026-08） |
|---|---|---|
| 算數的產物 | **設計文件**，單一份，程式碼變不透明之後唯一剩下的 | **整條 [[artifact-chain]]**，六份接力，每份只服務下一階段 |
| 它為什麼重要 | 人要理解系統才有理由承擔風險（認知問題） | commit chain 就是稽核軌跡，證明誰決定了什麼（責任問題） |
| 設計階段的長度 | 前置的重投入，餵大象要一週 | 需求與設計**壓縮進同一個 session**，由 skill 約束 |

第三行是實質衝突。Rensin 主張把設計判斷前置、重壓；
playbook 主張把需求與設計合併成一次 prompted session，理由是分離「為了問責而存在，
但它慢而且有損」。

（推論）可能的調和是兩者在講不同的東西：Rensin 的「設計」是架構層的取捨，
playbook 壓縮掉的是**需求到設計的文書交接**，不是架構決策本身。
但沒有來源這樣說，先並列。兩份來源都沒有處理產物過期後的維護成本。

## 未解之處

（推論）這條主張把賭注押在「設計文件能完整承載判斷」上。
但 [[judgment]] 的定義本身就是「教不來的模式比對」。
如果判斷力能被完整寫下來，Naval 那條「教不來」的判準就要修正；
如果寫不下來，設計文件就只是判斷力的有損壓縮。見 [[can-judgment-be-outsourced]]。

## 相關頁面

- [[elephants-goldfish]] —— 來源
- [[elephant-goldfish-model]] —— 實作這條主張的流程
- [[judgment]] —— 被寫進文件的那個東西
- [[can-judgment-be-outsourced]] —— 未解之處的展開
- [[factory-model]] —— 同一主張的另一種說法
- [[the-new-sdlc-with-vibe-coding]] —— 第二份來源
- [[the-ai-native-sdlc-playbook]] —— 第三份來源，給出不同答案
- [[artifact-chain]] —— 「產物鏈」而非「單一設計文件」那一側
