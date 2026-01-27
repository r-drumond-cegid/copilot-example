# CDS Conformity Report

Date: 2026-01-27
Scope: Frontend (React, Vite, MUI), Backend (FastAPI) — design/system checks only.

## Summary
- Overall: Good foundational design and accessibility. Charts are responsive and sections are semantically labeled. No API keys in frontend.
- Main gap: UI uses MUI directly instead of CDS packages (`@cegid/cds-react`, `@cegid/forms`).

## Checks vs Project Rules

1) Semantic HTML5 structure
- Finding: PASS. Native `<main>` used in frontend/src/App.jsx; semantic roles via MUI `component="header"` (Header) and `component="section"` for content blocks in pages/Dashboard.jsx and dashboard components. Sections labelled with `aria-label` / `aria-labelledby`.

2) React functional components + hooks
- Finding: PASS. No class components detected; all components are functional and use hooks (`useState`, `useEffect`, `useMemo`, `useLayoutEffect`).

3) Naming conventions
- Finding: PASS. Components in PascalCase; variables/functions camelCase; constants ALL_CAPS (e.g., API_BASE_URL). Private class member prefix N/A (no classes).

4) Plotly.js usage (modular, reactive)
- Finding: PASS. Using `react-plotly.js`; responsive config (`useResizeHandler`, `responsive: true`), dynamic height per breakpoint, and layout recalculation via `useLayoutEffect`.

5) Error handling & input validation
- Finding: PASS (frontend scope). API client centralizes errors via interceptors; Dashboard shows error `Alert` with retry; transactions/category chart guard invalid input. Date inputs use min/max to constrain ranges.

6) Security basics (frontend)
- Finding: PASS. No API keys exposed. Base URL via `VITE_API_BASE_URL` with safe default. No secrets found in sources.

7) Responsiveness
- Finding: PASS. MUI breakpoints, fluid containers, responsive chart heights; meta viewport present in frontend/index.html.

8) CDS adherence (packages/components)
- Finding: GAP. Current UI uses MUI components directly (AppBar, Button, TextField, Select, Dialog, Table, Chip, Alert, Card). Per CDS rules, prefer `@cegid/cds-react` and use `@cegid/forms` for all form fields.

## Accessibility Notes
- Positives: Landmarks (header/main), labelled sections, chart `aria-label`s, dialog has close button with `aria-label`, inputs have labels.
- Improvements:
  - Tables: consider `aria-sort` on sortable columns; ensure column headers convey scope.
  - Live updates: add `aria-live="polite"` near chat message stream to announce new assistant messages.
  - Chart contrast: ensure chosen colors meet contrast guidelines, especially on light backgrounds.

## Priority Fixes
1. Migrate MUI form fields (`TextField`, `Select`, `FormControl`, `InputLabel`) to `@cegid/forms`.
2. Replace common MUI primitives with CDS (`Button`, `AppBar/TopBar`, `Dialog`, `Alert`, `Chip`, `Card`, `Table`).
3. Add minor a11y enhancements (table sorting state; `aria-live` for chat messages).