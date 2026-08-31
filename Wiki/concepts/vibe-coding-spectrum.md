---
title: Vibe coding 到 agentic engineering 的光譜
type: concept
aliases: [vibe coding, agentic engineering, 光譜]
tags: [ai, 軟體工程]
created: 2026-08-01
updated: 2026-09-01
status: active
confidence: high
sources: ["[[the-new-sdlc-with-vibe-coding]]", "[[the-ai-native-sdlc-playbook]]", "[[ai-engineering-skills-map-software-fundamentals]]"]
---

# Vibe coding 到 agentic engineering 的光譜

> 分辨的關鍵不是「有沒有用 AI」，是**AI 的輸出被多少結構、驗證與人類判斷包住**。
> 同一個 agent、同一個開發者，可以在光譜任一端工作。

## 詞的來歷

2025 年 2 月 Karpathy 描述一種新寫法：「完全交給 vibes、擁抱指數、忘記程式碼存在」——
用自然語言描述、接受輸出、壞掉就把錯誤訊息貼回去。這個詞爆紅是因為它命名了很多人早已在做的事。

問題是它被套用得太廣而失去意義。2026 年初 Karpathy 自己承認原本的框法太窄，
提出 **agentic engineering** 來描述光譜紀律的那一端。

## 三段光譜

| 維度 | Vibe Coding | 結構化 AI 輔助 | Agentic Engineering |
|---|---|---|---|
| 意圖描述 | 隨意的自然語言 | 帶範例與限制的詳細提示 | 正式規格、架構文件、記憶檔 |
| 驗證 | 「看起來會動？」 | 手動測試、抽查 | 自動化測試套件、CI/CD 閘門、LM judges |
| 對程式碼的理解 | 極少，可能根本沒讀 | 選擇性審查關鍵路徑 | 全面審查架構，實作細節交給 AI |
| 錯誤處理 | 把錯誤訊息貼回去 | 人診斷根因、AI 實作修正 | agent 在界線內自我診斷，架構問題歸人 |
| 適用範圍 | 原型、腳本、個人專案 | 既有程式碼庫裡的功能 | 生產系統、團隊規模 |
| 風險 | 高（可拋棄的程式碼才可接受） | 中 | 低 |

## 判準只有一條

**輸出怎麼被驗證。**

- **Tests** 驗證確定性的部分：給這個輸入，產出那個輸出。由程式碼檢查。
- **Evals** 驗證非確定性的部分：agent 走的軌跡對不對、工具選得對不對、
  最終回應有沒有到品質線。由標註資料集、評分表、LM judge 檢查。

**兩者缺一，不管提示寫得多精巧，那都還是 vibe coding。**

## 怎麼選位置

由風險決定，不由品味決定。週末原型可以是純 vibe coding；
處理金流的生產 API 要求 agentic engineering。真正的技能是**知道每個任務該畫在哪裡**。

白皮書給團隊的建議是把這條界線變成**明文規範**（哪些專案、哪些分支、哪些環境用哪一種模式），
因為界線模糊的團隊會「不小心把原型上線」。

## 紀律那一端的組織版

白皮書建議把光譜位置變成明文規範（哪些專案、分支、環境用哪一種模式）。
[[the-ai-native-sdlc-playbook]] 把這條建議做成了機制：
**環境本身就是分級維度**——開發環境 agent 自由部署、staging 居中、
生產環境由發布經理授權且 hook 強制（[[autonomy-tiering]]）。

也就是說「這個任務畫在光譜哪裡」不必每次靠人判斷，
可以由 repo、分支與環境的設定決定。本頁說「真正的技能是知道每個任務該畫在哪裡」——
那份 playbook 的回答是：把那個判斷做一次，然後寫進版控。

## 光譜沒說的先決條件：你得看得見旋鈕

本頁把選位置的判準定在「輸出怎麼被驗證」，並說真正的技能是知道每個任務該畫在哪裡。
[[ai-engineering-skills-map-software-fundamentals|Ng]] 補的是**再往前一步**：
要在光譜上選位置，得先知道有哪些東西可選。

他的說法是新手 vibe code 之所以出事，不是因為驗證不足，
是因為「the developer didn’t know such tradeoffs even existed」——
latency、availability、consistency、reliability、maintainability、simplicity、cost
這七條旋鈕看不見（[[tradeoff-literacy]]）。

（推論）這對本頁那張三段表加了一格沒寫出來的東西：
表裡「適用範圍：原型、腳本、個人專案」預設了選位置的人**有能力評估風險**。
不知道可用性與一致性是兩件事的人，不會知道自己正在做一個生產系統的決定。

Ng 給的解法是能力清單（全端、資料、架構、安全可靠、規模化維運）。
本頁給的解法是驗證機制。（推論）兩者互補而不是競爭：
**驗證機制擋得住你想得到的失敗，能力清單決定你想得到多少種。**

## 相關頁面

- [[the-new-sdlc-with-vibe-coding]] —— 來源
- [[harness-engineering]] —— 決定你落在光譜哪裡的實際機制
- [[context-engineering]] —— 從一端走到另一端的橋
- [[factory-model]] —— agentic engineering 那一端的心智模型
- [[the-ai-native-sdlc-playbook]] —— 把光譜位置做成環境設定
- [[autonomy-tiering]] —— 分級的具體機制
- [[two-sdlc-frameworks]] —— 與 Anthropic 那份的框架比較
- [[tradeoff-literacy]] —— 在光譜上選位置的先決條件
- [[ai-engineering-skills-map-software-fundamentals]] —— 補上「該懂什麼」那一軸的來源
