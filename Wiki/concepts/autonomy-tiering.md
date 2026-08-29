---
title: 自治分級
type: concept
aliases: [autonomy tiering, control bands, bands.yaml, 控制帶]
tags: [ai, agent, 治理, 工作方法]
created: 2026-08-29
updated: 2026-08-29
status: active
confidence: medium
sources: ["[[the-ai-native-sdlc-playbook]]"]
---

# 自治分級

> 不問「要不要讓 agent 自己跑」，問「在什麼訊號強度下，它可以做到哪一步」。
> **偵測保持確定性，模型只在越界之後被叫進來。**

## 機制：把回應層級寫進版控設定

[[the-ai-native-sdlc-playbook]] 的 `bands.yaml`：

| 帶 | 動作 | agent 拿到什麼 |
|---|---|---|
| 1σ | `log` | 什麼都不做，只記錄 |
| 2σ | `diagnose` | **唯讀**工具：`Read,Grep,Bash(gh run view *)` |
| 3σ | `propose` | 可行動，但只能走 `pull_request` 或 `runbook:rollback-deploy` |

基線是 `rolling_30d`，規則用 Western Electric 一類，讓控制帶抓得到緩慢漂移而不只是尖峰。
偵測腳本版控、有單元測試，**完全不含模型**。

## 三個設計決定值得單獨記下來

1. **偵測與回應分離。** 判斷「有沒有異常」是確定性的統計，
   判斷「異常是什麼、怎麼辦」才交給模型。這讓自治的觸發條件可被審計與單元測試。
2. **最高權限仍然只是「提議」。** 3σ 不是「agent 可以修生產環境」，
   是「agent 可以開一個 PR 進審查閘門，或觸發一份**事先核准過**的 runbook」。
3. **rollback 必須是管線裡最常被演練的路徑**，因為閉環會呼叫它。
   原文要求它是單一指令、定期在 staging 演練——在 agent 需要用它之前就證明它會動。

## 環境也是一個分級維度

| 環境 | agent 可以做什麼 |
|---|---|
| 開發 | 自由部署 |
| Staging | 介於兩者之間 |
| 生產 | **準備發布，由發布經理授權**，hook 強制這道閘門 |

> "The governing principle is that the agent may act up to the production gate and cannot pass it."

配套的三條：branch protection 讓 agent 寫的任何東西都變成 PR，沒有直達 main 的路；
非互動執行用 agent 自己的身分，所以管線日誌分得出來哪些是 agent 做的、哪些是觸發它的工程師做的；
每個環境有自己的權限層級。

## 對「自主性的成本」是具體答案

[[agent-autonomy-cost]] 的結論是：模型自主性上升之後，
harness 的工作從「補能力」變成「設邊界」，但那一頁只有原則沒有機制。
這一頁是機制：**邊界不是寫在提示裡的一句話，是版控設定加上
[[advisory-vs-deterministic-control|確定型控制]]強制的路由。**

差別在於，提示裡的邊界靠模型願意遵守；分級的邊界靠工具清單與可用路由，
模型想越界也沒有工具可用。

## 誰在分流

分級不會消滅人的工作，它把人的工作換成**分流佇列**：
服務負責人或 on-call 決定修、排程、或駁回。原文特別要求**駁回要留理由**，
因為駁回是調校控制帶的資料來源，用來降噪。

修好之後要為那個事故加一條 eval（[[agent-config-evals]]），
所以同一類問題不會靠同一個人記得而不再發生。

## 相關頁面

- [[the-ai-native-sdlc-playbook]] —— 來源
- [[agent-autonomy-cost]] —— 這一頁是那一頁的機制
- [[advisory-vs-deterministic-control]] —— 邊界靠什麼強制
- [[intent-md]] —— 診斷結果寫成什麼
- [[ai-native-sdlc]] —— 閉環所在的框架
