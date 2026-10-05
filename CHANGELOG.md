# CHANGELOG

## v12 — 2026-09-29（Claude）
### 新增
- 偉銓選校板 `dist/weiquan.html`（+ `wq-board.js`、`wq-board.css`、`wq-board.json`）：現在能報清單、ARC 到期前 2 次機會時間軸、27 校分組卡片（申請費／第一學期學雜費／新生優惠／春季可否報）、獎學金怎麼拿與續領、語言門檻、學士時程與入學許可日、錄取後費用、官方榜單、讀不到的連結、篩選、比較表、進度標記與複製、換居留步驟、繁中／緬文。
- `research/weiquan-board-2026-09-29/`：編輯層 `board_data.py`、產生器 `build_board.py`、真實瀏覽器測試 `qa-browser.mjs`。
- 交接文件 `START_HERE_給GPT.md`。

### 修改
- `dist/app.js`：偉銓捷徑列與每月視窗頂端各加一個連到選校板的連結。其他邏輯未改。
- `dist/styles.css`：末尾加 `.weiquan-board-link`。
- `package.json`：加 `test:browser` 指令。

### 未改
- `dist/schools.json`、`dist/school-insights.json`、`dist/admission-records.json`、`dist/coverage.*` 等所有資料檔與其他 JS 與 v11 相同。

### 測試
- `qa-browser.mjs`：全部 PASS（Chromium，1280 與 390 寬）。
- `npm test`：Claude 環境無法安裝 linkedom（registry 403），未執行；請在 GPT 端執行。
- 選校板新增「今年還沒公布・往年日期參考」區：沒有官方日期的學士梯次也列出（標往年）。
