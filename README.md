<div align="center">

<img src="My_Gantt_icon.ico" width="72" alt="My Gantt icon">

# My Gantt

**A single-file, day-level, hierarchical WBS Gantt chart you can run by double-clicking an HTML file.**

일 단위 · 계층형 WBS 간트차트 — HTML 파일 하나로 돌아갑니다.

No build. No framework. No account. Your data stays on your machine.

### 👉 [**Live demo**](https://seobuk.github.io/my-gantt/) — try it right in your browser

</div>

---

## Why

Most Gantt tools want a login, a subscription, and your data on their servers.
My Gantt is the opposite: **one HTML file**, pure vanilla JS, works offline, and
you own the JSON. Point it at a folder and manage multi-year project schedules —
projects → subsystems → tasks, three levels deep (or more) — on one screen.

## Features

- 📅 **Day-level bars** across a multi-year timeline, with a live "today" line.
- 🌳 **3-level+ WBS tree** — expand/collapse, auto-numbered (1 / 1.1 / 1.1.1).
- 🔄 **Automatic roll-up** — a parent's dates and progress are computed from its
  children (duration-weighted progress average).
- ✏️ **Inline editing** — rename, set start/end via native date pickers, drag a
  progress slider, mark done / not-started.
- 🧱 **Structure editing** — add sibling / child, indent / outdent, reorder,
  move a whole subtree to another project, delete.
- 🎛️ **Filter chips** per project + summary stats (avg progress, active/done tasks).
- 🌗 **Light & dark mode**, responsive, **zero external dependencies**.
- 💾 **Dual-mode save** — a Python server writes a JSON file, or it falls back to
  browser `localStorage`. Your choice, same UI.

> The built-in UI labels are in Korean, but every project/task name is free text —
> use any language you like. (PRs to internationalize the UI are welcome.)

## Quick start

### 1. Just open it (no install)
Open `web/projects_gantt.html` in any browser. Edits save to the browser's
`localStorage`. Perfect for a quick look — but tied to that one browser.

### 2. Run with file storage (recommended)
Double-click `run.py` (or `python run.py`) from the project root. It auto-installs
Flask if missing, starts a local server, and opens your browser.

```bash
python run.py
# → http://127.0.0.1:5173
```

Now your data is saved to `data/wbs.json`, so you can back it up or share it via git.

<details>
<summary>Manual server start</summary>

```bash
cd python
pip install -r requirements.txt
python app.py   # → http://127.0.0.1:5173
```
</details>

**Windows:** double-click `run.bat` (uses `py -3.14`; adjust the version inside if needed).

## Data

Your schedule is a plain JSON array of nodes — human-readable and git-friendly.

| File | Role |
|------|------|
| `data/wbs_sample.json` | Seed data. The app loads this on first run. Edit or replace it with your own. |
| `data/wbs.json` | Your live data — created by the server on first save. Git-ignored by default. |

A node is either a **parent** (has `children`) or a **leaf task** (has dates):

```jsonc
// Parent — its dates & progress roll up from children automatically
{ "name": "Mobile App", "co": "Product", "col": "#1baf7a", "children": [ ... ] }

// Leaf task — the actual dated work
{ "name": "Design", "s": "2026-01-01", "e": "2026-03-31", "pr": 100 }
```

| Field | Meaning |
|-------|---------|
| `name` | Task / project name (required) |
| `children` | If present, this is a parent node (any depth) |
| `s`, `e` | Start / end date, `YYYY-MM-DD`. `e` is **inclusive** |
| `pr` | Progress, integer `0`–`100` |
| `co` | Tag / owner — shown on **top-level** nodes only |
| `col` | Project color (hex) — meaningful on **top-level** nodes; children inherit it |

The timeline spans `Y0`–`Y1` (default `2025`–`2027`). To change years, edit the
`Y0` / `Y1` constants near the top of the `<script>` in `web/projects_gantt.html`.

## Project layout

```
my-gantt/
├── web/projects_gantt.html   # the whole app — UI + logic, no build
├── python/
│   ├── app.py                # tiny Flask backend (serves HTML + save API)
│   └── requirements.txt
├── data/
│   ├── wbs_sample.json       # seed data (safe to edit)
│   └── wbs.json              # your live data (git-ignored, auto-created)
├── run.py / run.bat          # one-command launcher
└── CLAUDE.md                 # architecture & conventions
```

## Contributing

Issues and PRs welcome. Good first contributions: UI internationalization (i18n),
PNG/SVG export, or a static report generator. See [CLAUDE.md](./CLAUDE.md) for the
data schema and design principles before making changes.

## License

[MIT](./LICENSE) — do whatever you like.
