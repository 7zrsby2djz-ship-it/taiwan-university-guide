# CHANGELOG

## 2026-10-31 — 實際操作後的選校板改善

- 搜尋、篩選與「我的申請」條件同時套用到學校卡片及比較表；新增多關鍵字搜尋、清除搜尋、無結果恢復與篩選連結分享。
- 修正搜尋後從其他區塊點學校無法開啟詳情；查詢、排序及語言可在重新整理後恢復。
- 備註草稿在切換語言、篩選和重新整理後保留；儲存失敗會提示並保留輸入。
- 開始日期未確認的梯次獨立顯示；官方概略日期不再被標為往年。比較表改用尚未截止梯次的放榜時間，已報名者另保留等待結果提示。
- 排序支援升降冪，未知費用、日期及榜單人數在兩個方向都排最後。
- 新增首頁申請摘要，往年月份參考預設收合且不再逐日倒數。
- 新增 `qa-board.mjs` 回歸測試、依賴鎖檔及 `research/ux-2026-10-31/REPORT.md` 實測紀錄。招生資料仍為原查核快照。

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
