# 臺灣選校 / Taiwan Study Finder

> **接手的 AI 請先讀 [`START_HERE_給ChatGPT.md`](START_HERE_給ChatGPT.md)；每校還缺什麼看 [`待補清單.md`](待補清單.md)。**
> 選校板頁面在 `dist/weiquan.html`。要改資料，只改 `research/weiquan-board-2026-09-29/board_data.py`，再跑 `build_board.py` 和 `gaps.py`。
> 舊交接文件放在 `research/old-handoff/`，內容已過期，只供參考。


Burmese and Traditional Chinese static admissions directory. The two target intakes are 2027 spring (115-2) and 2027 fall (116-1). Open through a static web host; no build or account is required.

## Data and maintenance

`dist/schools.json` is the shipped, provenance-bearing snapshot. `research/build_data.py` generated the original baseline. Do not rerun it over the completed history data. Reproduce the additive update with `python research/history/merge.py` and then `python research/history/report.py`. The immutable original snapshot is in `research/backups/`. Schools without a verified intake keep unknown dates; absence of data is not proof of no admission. No automatic update is claimed.

The full registry contains 139 institutions, including junior colleges; the registry is not a list of institutions confirmed to recruit foreign students this intake. Dates remain partial: 86 institutions have fall timing and 56 have spring timing. Counts are mutually exclusive by strongest available event status, include retained baseline records, and do not imply all three fields or undergraduate eligibility. Every record keeps its official site entry; many current brochures and application endpoints remain unverified. The interface exposes this limitation in its source/coverage dialog.

Exact dates require a corresponding official intake announcement. Historical references are displayed as approximate intervals, never future exact days. `sort` is an internal interval ordering key, not an advertised date. Conflicting dates have no ordering key and sort after known dates. Admission results and admission letters are distinct. Some spring intakes are graduate-only. General Study in Taiwan program catalogs are explicitly distinguished from current recruiting departments.

Difficulty is an editorial 1–5 estimate, not a measured Taiwanese admission score, official ranking, or prediction of international-student admission. It is intentionally unrated for specialized institutions where a broad comparison is misleading.

## Interface

Three lexicographic sorting priorities, city/type/ownership filters, abbreviation search, semester switch, device-local favorites, CSV export, and shareable filters. The site registers feature-detected WebMCP filter/read tools using the same visible state and validation functions.

The personal 39-school board is at `dist/weiquan.html`. Its school cards and comparison table share search and filters, including “我的申請”. Filter/sort/language state survives refresh through the URL; the share control omits the QA date override and never includes application notes or progress. Unsaved note drafts survive rerenders and refresh on the same device, and an explicit save publishes the note to the board's current progress store. Storage errors are reported rather than shown as successful saves.

Decision rules live in `dist/wq-core.js`. An official deadline alone does not prove a round is open: a confirmed opening date is required. Graduate-only and unavailable undergraduate intakes are excluded. A known admission letter takes precedence over the public result date for the existing ARC cutoff. Comparison results follow rounds whose deadlines have not passed; the “我的申請” section separately shows upcoming official result references for already-submitted applications. Historical references retain their labels and have no daily countdown. See [the usage review and verification record](research/ux-2026-10-31/REPORT.md).

## Verification

Run `npm ci` and `npm test` (Node 20.19+). JavaScript syntax checks and DOM-simulated interaction tests cover the directory, date provenance, semester isolation, sorting, language switch, filters, favorites, details, unknown dates, conflict display, and personal-board regression cases. The 2026-10-31 update was also exercised in Chrome through the Sites preview, including 390px Chinese and 320px Burmese iframe viewports. This is responsive-browser testing, not a physical iPhone/Safari test. Legacy `test:browser` requires a separately available Playwright browser environment; the current workflow uses the supported Sites browser preview instead.
