---
title: 流水帳
type: synthesis
aliases: [log]
tags: [樞紐]
created: 2026-08-01
updated: 2026-08-01
status: active
confidence: high
sources: []
---

# 流水帳

> Append-only，新的加在最下面。格式固定，可用 `grep "^## \[" Wiki/log.md | tail -5` 取最近紀錄。
> 動作只有四種：ingest / query / lint / publish（`publish` 於 2026-08-29 加入）。

## [2026-08-01] lint | 建庫
- 建立目錄結構、`CLAUDE.md` schema、五種頁面模板、`tools/lint.py`
- 建立樞紐頁：[[index]]、[[log]]、[[overview]]

## [2026-08-01] lint | 清除建庫示範內容
- 移除 7 個範例頁與範例來源，wiki 回到空庫狀態，只留樞紐頁與模板
- 待處理：`Raw/` 已有 3 份未 ingest 的來源

## [2026-08-01] ingest | Arm Yourself With Specific Knowledge、Read What You Love、Elephants Goldfish
- 來源：三份一起處理（使用者指定批次），Raw 檔名改為 `YYYY-MM-DD--slug` 格式
- 新增來源頁：[[arm-yourself-with-specific-knowledge]]、[[read-what-you-love]]、[[elephants-goldfish]]
- 新增實體：[[naval-ravikant]]、[[dave-rensin]]
- 新增概念：[[specific-knowledge]]、[[judgment]]、[[leverage-and-compounding]]（seed）、[[love-of-reading]]、[[first-principles-foundation]]、[[elephant-goldfish-model]]、[[design-is-the-new-code]]、[[ai-as-interrogator]]
- 新增綜合：[[can-judgment-be-outsourced]]
- 更新：[[overview]]（建立四條主軸）、[[index]]
- **矛盾**：Naval「判斷力教不來」vs Rensin「把設計判斷寫進文件交給 agent」——記在 [[can-judgment-be-outsourced]]，兩邊都保留，confidence 壓在 medium
- 新問題：[[open-questions]] Q1–Q5。下一份該找的來源是 Naval 談 leverage 的篇章（Q4）

## [2026-08-01] ingest | 5 Agent Skill Design Patterns、The New SDLC With Vibe Coding
- 來源：兩份一起處理。PDF 51 頁以文字擷取閱讀，Raw 檔名改為 `YYYY-MM-DD--slug` 格式
- 新增來源頁：[[agent-skill-design-patterns]]、[[the-new-sdlc-with-vibe-coding]]
- 新增實體：[[addy-osmani]]、[[shubham-saboo]]（唯一橫跨兩份來源的作者）
- 新增概念：[[vibe-coding-spectrum]]、[[context-engineering]]、[[harness-engineering]]、[[factory-model]]、[[conductor-and-orchestrator]]、[[the-80-percent-problem]]、[[ai-development-economics]]、[[agent-skills]]、[[skill-design-patterns]]
- 更新：[[judgment]]（第三份來源，confidence medium→high）、[[can-judgment-be-outsourced]]（白皮書畫出界線，層級移動說取得最多證據）、[[ai-as-interrogator]]（發現它等於 Inversion 模式）、[[design-is-the-new-code]]、[[elephant-goldfish-model]]（用 harness 詞彙重述）、[[overview]]、[[index]]
- **矛盾（新增 2 條）**：
  - 生產力數字互斥：25–39% 提升 vs METR「資深開發者慢 19%」，白皮書自己並列但沒調和 → Q7
  - 「給成功判準」vs「列出每一個檔案」：[[factory-model]] 與 [[elephant-goldfish-model]] 表面衝突 → Q8
- **收斂（2 條）**：[[ai-as-interrogator]] = Inversion 模式；[[conductor-and-orchestrator]] 與 Rensin 的「我們都是管理者了」獨立同構
- 新問題：Q6（判斷力上移後新判斷力從哪長出來，五份來源共同盲點）、Q7、Q8、Q9
- 下一份該找：METR 原始研究（白皮書尾註 10）

## [2026-08-02] ingest | Prompting Claude Opus 5
- 來源：Anthropic 官方文件，本庫第一份**供應商一手文件**
- 新增來源頁：[[prompting-claude-opus-5]]
- 新增實體：[[claude-opus-5]]
- 新增概念：[[prompt-obsolescence]]、[[agent-autonomy-cost]]、[[effort-and-thinking]]
- 更新：[[harness-engineering]]（harness 會折舊）、[[context-engineering]]（靜態脈絡有保鮮期）、[[skill-design-patterns]]（Reviewer 模式修正：別寫「只報高嚴重度」）、[[judgment]]（第四份來源，改由供應商描述模型的判斷）、[[can-judgment-be-outsourced]]（問題形狀改變）、[[overview]]、[[index]]
- **矛盾（新增 1 條）**：本文顯示規則檔會折舊，直接挑戰 [[harness-engineering]]「建一次精煉很多次」與 [[ai-development-economics]] 把 harness 當一次性 CapEx 的假設 → [[prompt-obsolescence]]、Q11
- **反轉**：Q9 原本打算在 CLAUDE.md 加 Inversion 硬閘門，本文建議相反方向（例行判斷讓模型自己做）→ 暫時擱置，兩份來源方向相反
- **新主軸**：規則檔的折舊（overview 主軸 4）
- 新問題：Q10（每條規則為什麼存在）、Q11（換代時 harness 怎麼重驗）
- 本庫自檢：`CLAUDE.md` 沒有本文點名的反模式（無「再檢查一次」類指令，第 9 步用的是確定性 lint 而非模型自我複查），但沒有記錄任何規則的來由 → Q10

## [2026-08-29] ingest | The AI-Native SDLC Playbook
- 來源：Anthropic Applied AI team，`claude.com/blog/the-ai-native-sdlc-playbook`，六階段 13 個 play
- Raw 改名：`The AI-Native SDLC playbook  Claude by Anthropic.md` → `2026-08-29--the-ai-native-sdlc-playbook.md`（只改檔名，內容未動）
- 新增來源頁：[[the-ai-native-sdlc-playbook]]
- 新增概念：[[ai-native-sdlc]]、[[artifact-chain]]、[[intent-md]]、[[advisory-vs-deterministic-control]]、[[autonomy-tiering]]、[[agent-config-evals]]
- 更新：[[agent-skills]]（**skill 不是控制，只是建議**）、[[skill-design-patterns]]（Inversion 的「不可協商閘門」寫在 SKILL.md 裡其實可協商）、[[agent-autonomy-cost]]（畫界線的機制＝分級）、[[prompt-obsolescence]]（折舊可被偵測）、[[harness-engineering]]（managed settings；harness 擴到組織層級；回饋迴圈 vs verifier 子 agent）、[[context-engineering]]（`CLAUDE.md` 一頁以內）、[[design-is-the-new-code]]（新矛盾）、[[factory-model]]（Q8 新證據）、[[can-judgment-be-outsourced]]（第五份來源）、[[judgment]]、[[ai-development-economics]]（CapEx 不是一次性）、[[vibe-coding-spectrum]]（光譜位置可寫進環境設定）、[[overview]]、[[index]]
- **新主軸**：治理（overview 主軸 5）。前六份來源全是個人／小團隊視角，這是第一份組織視角
- **矛盾（新增 1 條）**：「唯一算數的產物是哪一個」——[[elephants-goldfish]] 說是單一設計文件、本份說是整條產物鏈；且 Rensin 把設計前置重壓，本份把需求與設計壓縮進同一個 session → 記在 [[design-is-the-new-code]]
- **收斂（3 條）**：
  - Q11（換代時 harness 怎麼重驗）→ partial，答案是 [[agent-config-evals]]，但只解決偵測不解決定位
  - Q8（給判準還是給清單）→ 大致收斂，答案是拆成 `spec.md` 與 `plan.md` 兩份分別核准的文件
  - Q9 被**改寫**：問題不是要不要有 Inversion 閘門，是閘門寫在哪裡。寫在規則檔裡的是建議，`tools/lint.py` 才是閘門
- 新問題：Q12（產物鏈拉長之後誰讓它不過期）、Q13（「趨近於零」的指標，成功與停止量測長得一樣）
- 本庫自檢：`CLAUDE.md` 遠超過原文建議的「一頁以內」；lint 全綠不等於 wiki 健康（Q13）
- 來源獨立性警訊：七份來源裡兩份出自 Anthropic、三份出自 Google 或其員工。**治理這一軸目前只有賣方視角**
- 下一份該找：METR 原始研究（Q7）仍是第一順位；治理軸需要一份買方或監管方的來源

## [2026-08-29] lint | 清掉關聯圖上的雜訊
- 起因：使用者從 Obsidian 關聯圖看出異常。**四團雜訊沒有一項來自 wiki 內容**
- **刪除 `_to_delete/`**：2026-08-01「清除建庫示範內容」那次其實只把 7 個示範頁搬走沒刪，檔案一直在 vault 裡，包含一個與現行頁**同名的 `open-questions`**。該次 log 寫「移除」與事實不符，此處更正
- 調整 `.obsidian/graph.json`：`search: -path:_templates`（模板與其佔位連結不入圖）、`hideUnresolved: true`（隱藏 Raw 擷取檔 frontmatter 帶進來的 `Naval`、`Dave Rensin`、`Google Cloud Tech (@GoogleCloudTech)` 這類幽靈節點——Raw 不可改，只能隱藏）、`showOrphans: false`（收掉 CLAUDE／README 孤島）
- `tools/lint.py` 新增「走失頁」檢查：Wiki/ 以外出現帶合法 `type` frontmatter 的頁面就報。與 Wiki/ 現行頁同名 → 問題；否則 → 提醒。已用暫存檔自我驗證兩條路徑都會觸發
- **這是 Q13 的第一個實例**：lint 當時全綠，但 vault 裡躺著 7 個重複頁。漏掉的原因是 lint 只掃 `Wiki/`——**檢查範圍本身就是盲點的來源**

## [2026-08-29] lint | CLAUDE.md 精簡到一頁
- 起因：[[the-ai-native-sdlc-playbook]] 建議 `CLAUDE.md` 控制在一頁以內（session 開頭全讀，過期內容白佔脈絡）。使用者指示照做
- **204 行 / 5,211 字元 → 69 行 / 1,852 字元**（減 64%）
- 做法是**搬不是砍**，配合原文「制度知識寫成 skill」的建議，把只在特定時刻需要的內容移到按需載入的地方：
  - `.claude/skills/wiki-ingest/SKILL.md` —— 完整 frontmatter 規範、ingest 十步、擴散更新與矛盾處理、`index.md` 與 `log.md` 的格式、目錄結構
  - `.claude/skills/wiki-lint/SKILL.md` —— 六項判斷性檢查、輸出方式、lint 自身的盲點（接 Q13）
- CLAUDE.md 留下每次 session 都用得到的：三層權限、分類判斷順序、命名、連結規範、三種流程的入口、寫作風格、七條禁止
- 逐條核對搬移，補回三條壓縮時漏掉的具體規則：query 的輸出格式（表格／時間軸／Marp／matplotlib）、「## 相關頁面」每條要附說明、頁面長度區間
- 新增一條這次踩到的規則：帶別名的 wikilink（雙括號加豎線）別放進表格（跳脫與否都會壞——不跳脫壞排版，跳脫壞 lint 的連結解析）
- **這是靜態脈絡搬到動態側的實例**（見 [[context-engineering]]、[[agent-skills]]）。但要記得 [[advisory-vs-deterministic-control]]：搬進 skill 之後這些規則的執行力從「常駐」降成「按需觸發」，是**建議型控制**。真正不可退讓的仍靠 `tools/lint.py`
- 未做：Q10（每條規則為什麼存在）沒有一併處理，規則的來由仍未記錄

## [2026-08-29] lint | 規則來由帳（Q10 結案）
- 使用者指示：每條規則加上來由
- `CLAUDE.md` 每條規則加穩定編號（L／C／N／K／W／S／X 共 26 條），69 → 73 行，仍在一頁內
- 新增 `.claude/rules-ledger.md`：每條規則記**防什麼**、**證據等級**、**實際觸發紀錄**
- **證據狀況比預期差**：建庫那筆 log 只寫「建立 `CLAUDE.md` schema」，沒記任何規則的理由；此 repo 不是 git repo，無版本歷史可查。結果 **26 條裡只有 1 條（K1，本 session 加的）證據等級是「有紀錄」**，其餘全是「推論」或「來由未知」
- 帳裡明文禁止事後補一個聽起來合理的理由——編出來的來由讓沒人記得為什麼的規則看起來有據可查，比沒有來由更糟
- 改用可查證的替代指標「這條規則實際被觸發過嗎」，跑出四個發現：
  1. **`query` 流程從未被執行過**——log 8 筆全是 ingest 與 lint，零筆 query。W3、W4 從未被驗證
  2. W2「不批次」的例外條款在早期是常態：2026-08-01 兩筆都是使用者指定批次，合計五份
  3. 「禁止」那一節 7 條裡有 4 條是前文重述（L1、K3、W2、L3），改規則要改兩處
  4. 編號規則裡只有 4 條有確定性後盾（N4、N5、K3、K4 由 lint 強制），其餘全是建議型控制
- 自我驗證：帳裡的量化主張逐條回查，修正 2 處（log 筆數 9→8；lint 檢查項 4→9 種，其中 4 種對應編號規則）
- Q10 → **closed**；新問題 Q14（沒有觸發紀錄的規則該刪還是該留——與 Q13 同構，在規則層）
- 未做：日後每加一條規則要同時補一列到帳裡，這條紀律**沒有確定性後盾**，靠自覺

## [2026-08-29] lint | 規則來由的閘門化，並發布到 GitHub
（發布不屬於 W1 的三種動作，暫記在 `lint` 底下）

**規則來由閘門**
- `tools/lint.py` 新增 `[來由]` 檢查，把「加規則要同時記來由」從自覺變成會擋的閘門
- 四種情況：編號無對應列 → 問題；「防什麼」留空 → 問題；證據等級不是三個合法值 → 問題；帳裡有孤兒列 → 提醒
- 後兩項是為了擋「補一列空的來交差」，確保閘門逼出的是來由本身而不只是一列
- 已用暫存修改逐一驗證四條路徑，檔案已還原
- 第一次跑就抓到真問題：K1 那列的敘述裡有未跳脫的豎線把欄位切斷——**正是 K1 自己描述的那個坑**
- Q10 的結論因此改寫：後續紀律已機制化，從建議型控制變成確定型控制

**發布到 GitHub**
- `git@github.com:foxhsiao/wiki.git`（PUBLIC），64 個檔案
- **`Raw/` 排除在版控外**：那是七份第三方文章的全文副本（含 9.5MB 白皮書 PDF），推上公開 repo 等於重新發布他人著作。經使用者確認後加進 `.gitignore`
- 已確認內文沒有任何連結指向 Raw 檔名，排除不會產生斷鏈；只有 source 頁 frontmatter 的 `raw:` 欄位在 clone 後會指向不存在的檔案，已寫進 README
- README 更正：「目前狀態」原本寫「空庫」，與實際的 7 份來源 / 43 頁不符
- `.gitignore` 移除已失效的 `_to_delete/`
- commit 作者信箱改用 GitHub noreply（帳號開了 email 隱私保護，原信箱會被 GH007 擋下），已設為本 repo 預設

## [2026-08-29] publish | 新增 publish 動作，並推送本次變更
- 使用者指示：加 `publish` 這個動作，並補來由。**本筆是第一筆 `publish` 動作**
- `CLAUDE.md`：W1 從三種動作改為四種；新增 `[W6]` publish——推上遠端前先查遠端 repo 的可見性並確認推送範圍、`Raw/` 永遠不入版控、commit 作者用 GitHub noreply 信箱
- **閘門在真實情境驗證成功**：只加 `[W6]` 沒補來由時，lint 立刻報「規則 W6 在 CLAUDE.md，但 rules-ledger 沒有對應列」並 exit 1。補完才過
- `.claude/rules-ledger.md`：新增 W6 列，證據等級 **有紀錄**——這是帳裡第二條有紀錄的規則（另一條是 K1），因為它的來由就發生在今天，三條子規則當天全部觸發過
- W1 那列的敘述與筆數一併更新
- 同步「四種動作」到 `.claude/skills/wiki-ingest/SKILL.md` 與 `Wiki/log.md` 表頭；README 的「怎麼用」加上發布一節
- 未動：2026-08-29 前幾筆 log 裡「三種動作」的敘述保持原狀（append-only，當時是準確的）

## [2026-08-29] lint | 完整健檢
- 機械性檢查：43 頁全綠，零提醒
- **過期（3 處，都是今天自己造成的）**：
  - [[overview]]「本庫的 `CLAUDE.md` 遠超過一頁」——今天已壓到 76 行
  - [[overview]]「唯一缺的是 Inversion 的硬閘門」——已有兩道確定性閘門
  - [[skill-design-patterns]] 的「與本知識庫的關係」一節完全沒反映 Q9 的改寫：上半部已寫「三種模式需要 hook 墊底」，下半部還停在「唯一缺的是 Inversion」。三處都已改寫
- **證據薄弱（5 頁違反本庫自己的規範）**：frontmatter 規範寫「單一來源 → medium 以下」，但這 5 頁是 high + 單一來源。建庫就寫了規則卻沒有機制，所以違規累積了四週沒被發現
  - 處理方式：新增規則 `[N6]`——單一來源要 high 必須加一行 `confidence_note:` 說明理由。**豁免做成「必須寫理由」而不是靜默白名單**，理由與 Q10 相同：靜默豁免會讓「這頁為什麼可以 high」再次變成沒人記得的事
  - 豁免 3 頁（供應商描述自家產品的定義性事實）：[[claude-opus-5]]、[[effort-and-thinking]]、[[advisory-vs-deterministic-control]]
  - 降級 2 頁：[[elephant-goldfish-model]]（單一實踐者的方法，不是定義性事實）、[[the-80-percent-problem]]（頁內就並列未調和的互斥數據，Q7 仍 open）
- `tools/lint.py` 新增 `[confidence]` 檢查，加入後第一次跑就抓到那 5 頁，與人工判讀完全一致
- **無問題的部分**：未記錄的矛盾 0 條；缺頁無強候選（Inversion／Reviewer／Pipeline 等都是 [[skill-design-patterns]] 的子概念）；index 各節宣告數與實際檔案數完全相符；stale 標記 0 頁
- **弱連結（未達孤兒，記錄備查）**：[[effort-and-thinking]] 與 [[shubham-saboo]] 各只有 2 條入鏈
- **缺口不變**：METR 原始研究（Q7）仍是第一順位；治理軸只有賣方視角；[[leverage-and-compounding]] 仍是 seed 且 confidence low（Q4）
- **git 管理原則改為 GitHub flow**（使用者指定）：新增 `[W7]`，`main` 永遠可用，改動走分支開 PR 才合併。本次變更是第一個走這個流程的分支

## [2026-08-29] lint | 界定 log 的記錄範圍
- 起因：`[W7]`（GitHub flow）上路後出現迴圈——log 條目本身是對 repo 的改動，照 W7 要開分支開 PR，而那次合併又該被記進 log，無限遞迴
- 決定（使用者選擇）：**log 記知識庫的變化，純 git 操作（合併 PR、刪分支）由 git 歷史負責，不另記一筆**。不加豁免機制，只把 W1 本來的範圍講清楚
- 代價：log 不反映合併時間點。可接受，因為 git 記得比 log 精確
- 順帶校正：來由帳裡 W1 的觸發紀錄原本寫「至今 9 筆」，實際是 12 筆（4 ingest、7 lint、1 publish）。那個數字是先前沒回查就寫下的——**在一份專講證據的檔案裡放未驗證的數字**。已改成標註日期的快照，並註明以 `Wiki/log.md` 為準
- 閘門紀錄：想在證據等級欄寫「推論（範圍界定部分為有紀錄）」被 lint 擋下，嚴格詞彙不允許混合值。改用保守的「推論」，細節移到「防什麼」欄

## [2026-08-29] query | 找 METR 原始研究
- **本庫第一筆 `query` 動作**。健檢時發現 W3／W4 從未被觸發過，這次補上了 W3；W4（輸出格式）仍未觸發
- 使用者要求找 [[open-questions]] Q7 指的 METR 研究。網路搜尋結果**已先聲明**再寫入，並在 Q7 標明「不可當作本庫主張」
- 找到兩份，都還沒 ingest：
  - 原始研究 2025-07-10（Becker、Rush、Barnes、Rein；16 位開發者、246 個 issue；工具是 Cursor Pro + Claude 3.5/3.7 Sonnet）
  - **後續更新 2026-02-24**——這是意外收穫。METR 沒有撤回 19%，但做了限定，新一輪的估計區間跨過 0
- 若後續更新屬實，本庫把「慢 19%」當硬數據的用法（[[the-80-percent-problem]]、[[can-judgment-be-outsourced]]）要修正，而且它會變成 [[prompt-obsolescence]] 的另一個實例
- **刻意沒做**：沒有把搜尋結果寫進任何概念頁。依 `[X3]`，那些在來源頁建立前不算數。Q7 那段是待辦不是主張
- 下一步：使用者用 Web Clipper 把 2025 原始研究剪進 `Raw/inbox/`，再 ingest。2026 更新留待下一輪去撞它

## [2026-08-29] lint | README 補上 Prompt 使用說明
- 使用者要求：README 要寫怎麼用的 prompt
- 「怎麼用」一節從四段散文改寫成依四種動作（ingest／query／lint／publish）分節，每節給可直接照抄的 prompt
- 補上三塊原本沒寫的：**改規則**的說法（含「這條規則為什麼存在？」）、**agent 會拒絕的事**（寫 `Raw/`、覆寫矛盾、無來源主張、直推 main）、**怎麼跳過 ingest 的確認步驟**及其代價
- 「agent 會拒絕的事」那張表是刻意加的：規則寫在 `CLAUDE.md` 給 agent 看，但**使用者不知道哪些要求會被擋**，這是這份 README 原本的缺口
- 未動 wiki 內容；METR 那份來源仍停在 ingest 第 2 步等使用者確認方向（lint 的 `[待處理]` 提醒正確反映了這件事）
## [2026-08-29] ingest | METR：Early-2025 AI 對資深開源開發者生產力的影響
- 來源：METR 2025-07-10，RCT。**本庫第一份實證研究**，也是第一頁 `status: stale`——**來源自己在頁首宣告結果過期**
- Raw 改名：`Measuring the Impact of...md` → `2026-08-29--metr-early-2025-ai-developer-productivity.md`（只改檔名）
- 新增來源頁：[[metr-early-2025-ai-developer-productivity]]
- 新增實體：[[metr]]（seed）
- 新增概念：[[self-report-vs-measurement]]、[[evidence-types-for-ai-capability]]
- 新增綜合：[[what-the-19-percent-measures]]
- 更新：[[the-80-percent-problem]]（Q7 解開）、[[can-judgment-be-outsourced]]（**更正誤讀**）、[[harness-engineering]]（兩面）、[[context-engineering]]（外部實證支持）、[[prompt-obsolescence]]（測量也會折舊）、[[judgment]]（第六份來源，且不支持該線）、[[design-is-the-new-code]]、[[overview]]、[[index]]
- **Q7 closed**：兩組數字不是互斥，是在測不同的東西。25–39% 是自陳調查、19% 是 RCT 實測。同一批人：事前 +24%、事後自認 +20%、實際 −19%，**自陳與實測差 39 個百分點**。本頁原本「增益取決於任務是否已規格化」的推測退場
- **矛盾（新增 1 條，且是本庫自己造成的）**：本庫把這個 19% 當成「判斷力無法外包」的實證用了四週，**那是誤讀**。METR 的五個因子全是工具與情境，沒有一個關於判斷力。記在 [[what-the-19-percent-measures]]，並在 [[can-judgment-be-outsourced]] 與 [[overview]] 明文更正。**保留誤讀紀錄而非刪除**，因為它本身是資料：方法學嚴謹的研究很容易被拿去支持它沒有主張的東西
- **兩面都寫（使用者指定）**：harness 那條線同時被支持與削弱——支持的是因子 5「隱性脈絡」正是規則檔與 skill 在編碼的東西；削弱的是 [[harness-engineering]] 現有最硬的兩個數字（Terminal Bench、LangChain）都是 benchmark，而 METR 說 benchmark 傾向高估。且 harness 假說出現在原文「我們不提供證據支持」的表格裡，是作者劃的界線不是發現
- **五個因子與六個被排除的因子取自 arXiv 全文，明確標註出處不在 `Raw/` 之內**（剪存檔對應位置只有 CDN 外連的圖）。未改規則
- 其他擷取缺口：FAQ 只剩問題、答案被剪存工具吃掉
- 新問題：**Q15（好的 harness 能不能翻轉那個 19%——本庫最大的證據缺口，取代原本 Q7 的位置）**、Q16（2026-02-24 後續研究，下一份要 ingest）
- 下一份：METR 2026-02-24 更新（使用者已指示接著做，兩次分開不算批次）

## [2026-08-29] lint | 把機械性樞紐從關聯圖濾掉
- 起因：使用者從關聯圖看出 `index` 變成知識庫的視覺核心，但它只是目錄、不是概念核心
- 量化確認：`log` **48 條出鏈**（append-only，只會愈長）、`index` 47 條、`overview` 36 條。前兩者純粹是機械性樞紐
- `.obsidian/graph.json` 的 filter 加上 `-path:"Wiki/index.md" -path:"Wiki/log.md"`。**保留 `overview`**——它有 36 條出鏈但內容是真的綜合判斷，不是目錄
- 濾掉之後浮現的真實概念樞紐（入鏈數，已扣掉三個 hub）：[[the-ai-native-sdlc-playbook]] 19、[[the-new-sdlc-with-vibe-coding]] 18、[[judgment]] 17、[[can-judgment-be-outsourced]] 16、[[harness-engineering]] 15、[[context-engineering]] 14
- 安全性確認：濾掉不會讓任何頁面變孤島，因為 `tools/lint.py` 的孤兒檢查本來就把 index／log／overview 排除在入鏈計算之外——**每頁都被強制要有樞紐以外的入鏈**
- README 的「關係圖檢視」一條補上這個設定的理由
- （推論）這是 [[context-engineering]] 靜態／動態那條線的視覺版：`index` 是導覽用的，不是知識結構的一部分；把導覽層混進知識層，兩邊都看不清楚

## [2026-08-29] lint | 修掉自己帶進 main 的衝突標記
- **我造成的錯誤**：合併 PR #4 與 #5 時 `Wiki/log.md` 衝突，我用 regex 解衝突，
  但那次是 diff3 格式，中段的 `|||||||` 標記被當成內容吞進解法，跟著 PR #5 進了 `main`
- 直接原因是驗證不足：當時只 grep 了 `<<<<<<<`、`=======`、`>>>>>>>` 三種標記，**漏掉第四種**
- 已移除殘留標記，並全庫掃描確認沒有其他殘留
- `tools/lint.py` 新增 `[衝突標記]` 檢查：掃 `.md`／`.py`／`.json`／`.yml`，四種標記全查，`Raw/` 除外（唯讀不歸它管）。已用假標記自我驗證
- （推論）這是本庫第三次出現同一個形狀的問題：**規則或紀律靠人工驗證時，出錯的是驗證者自己而且看不到**。前兩次是規則來由、confidence 與來源數。解法一樣——把驗證做成會 exit 1 的檢查

## [2026-08-30] lint | 清掉誤入版控的每日筆記
- **我造成的**：`2026-08-29.md`（0 byte，Obsidian daily-notes 外掛在 vault 根目錄建的）被我用 `git add -A` 帶進版控，推上了公開 repo。原因是提交前沒有逐一檢查暫存內容
- 已刪除該檔，並在 `.gitignore` 加上 `/20??-??-??.md`
- **pattern 刻意加了根目錄錨點**：不加的話會誤傷 `Raw/` 的 `YYYY-MM-DD--slug.md` 命名（規則 `[N2]`）。已驗證：`2026-08-30.md` 命中、`2026-08-29--metr-early-2025-ai-developer-productivity.md` 不命中
- （推論）`git add -A` 在一個同時是 Obsidian vault 的 repo 裡是有風險的預設——外掛會在你不知情時建檔。這與 `[W6]` 的「推之前確認推送範圍」是同一件事，只是尺度更小

## [2026-08-30] ingest | METR：我們正在改變開發者生產力實驗的設計
- 來源：METR 2026-02-24。**一份宣告自己量不準的研究報告**
- Raw：`Raw/inbox/We are Changing...md` → `Raw/2026-08-30--metr-2026-uplift-update.md`（只改檔名）
- 新增來源頁：[[metr-2026-uplift-update]]
- 新增概念：[[control-group-collapse]]
- 更新：[[metr-early-2025-ai-developer-productivity]]（**解除 stale**、補上信賴區間）、[[what-the-19-percent-measures]]（可主張清單重寫）、[[self-report-vs-measurement]]、[[evidence-types-for-ai-capability]]、[[metr]]、[[the-80-percent-problem]]、[[can-judgment-be-outsourced]]、[[prompt-obsolescence]]、[[open-questions]]、[[overview]]、[[index]]
- **重壓的那條：三組信賴區間**
  - 2025 早期：慢 19%，區間 **`+2% 到 +39%`**，**不含 0**——這是本庫第一次拿到，當年的結果是**顯著的**
  - 2025 晚期・原班 10 位：慢 18%，區間 `−38% 到 +9%`，**跨過 0**
  - 2025 晚期・新招募 47 位：慢 4%，區間 `−15% 到 +9%`，**跨過 0**
  - METR 自己：中央估計值「很可能是真實生產力影響的糟糕代理」
- **淨結果：本庫一個生產力數字都不能直接引用。** 2025 那份顯著但過期，2026 那份當期但不可解讀。存活的只有 [[self-report-vs-measurement]] 這條方法學發現
- **連帶影響**：「判斷力無法外包」那一側連一個可引用的數字都沒有了。沒有證據不等於證據為否，但本庫應停止說它有數據支撐
- **對 Q15 是壞消息（本 ingest 最重要的判斷）**：2026 那份表面像在回答 harness 問題（估計值從 −19% 移到 −4%），**但無法歸因**——新招募組同時換了三件事：不同的人、較小較新較不成熟的 repo、更新的 agentic 工具。而 2025 的因子 3 與因子 5 已指出 repo 規模與隱性脈絡本身就是主因。**最想被分離的變數正好被綁在另外兩個已知有影響的變數上。** Q15 因此比一個月前更難填
- **Q16 closed**；Q15 狀態更新為「仍是最大缺口，且更難填」
- **新概念 [[control-group-collapse]] 是本次最可移植的收穫**：工具好到受試者拒絕在沒有它的條件下工作，RCT 就失效。它把 [[prompt-obsolescence]] 推到第三層——規則過期 → 結果過期 → **量測方法本身失效**。也是 Q13「成功與停止量測長得一樣」在真實研究上發生的樣子，而答案是**分不出來**
- 判讀保留的三個盲點：趨勢判斷的依據是訪談不是數據；時薪 150→50 美元這個共變數未被分離；新舊兩組的差異無法歸因

