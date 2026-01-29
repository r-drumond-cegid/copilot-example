## User Flow: Compact Finance Dashboard

**Entry Point**: User opens dashboard to review today’s balances.

**Flow Steps**:
1. **Compact Summary Header**
   - Left: App title + date range picker (single control with presets: 7/30/90 days).
   - Center: **Bank/Entity switcher** and **Cash Pool** selector (sticky).
   - Right: `Compact Mode` toggle (reduces paddings/fonts, chart height; persists in localStorage).
   - Info chips: "Δ vs previous period" (absolute + %), "Last updated" timestamp, **Cut‑off timer** for today.

2. **Primary KPIs (Row)**
   - `Total Balance` (dominant), `Change vs prior`, `Risk (Overdraft exposure)`.
   - Optional badges: **FX exposure** and **Connectivity status** (banks OK / issues).
   - Optional: collapse/expand hero banner to save vertical space.

3. **Secondary KPIs (Row)**
   - `Average`, `Minimum`, `Maximum`, `Accounts count` with lighter visual weight.
   - **Cash pool utilization** and **Number of approvals pending**.

4. **Trend Chart (Responsive)**
   - Height: 30–40vh in compact; 45–55vh in regular.
   - Lighter gridlines; tooltip with deltas; optional brush/zoom.
   - Accessible description; ARIA live for data updates.

5. **Quick Insights & Alerts**
   - Exceptions: low balance, overdraft nearing, unusual drop, **connectivity issues**, **cut‑off risk**.
   - Action buttons: initiate transfer/sweep, open transactions, share/export report.

6. **Transactions & Approvals (Tabs)**
   - `Transactions` (priority-first): date, account, amount, category, note.
   - Progressive filters: date, category, amount range, account, bank/entity; saved views.
   - Density mode: compact row height; virtualization for performance.
   - `Approvals`: payment items with status, amount, cut‑off; bulk actions; counts in tab label.

**Exit Points**:
- Success: No exceptions; compact overview confirms stability.
- Action: Exception triggered → investigate in table → perform transfer.
- Partial: Save filters/state; resume later.

## Design Principles
1. **Progressive Disclosure**: Collapse large hero; surface primary KPIs first; expand details on demand.
2. **Visual Hierarchy**: Clear tiers: Primary (Total, Δ), Secondary (Avg/Min/Max), Tertiary (Overdraft, Accounts).
3. **Compact Density**: Toggle reduces paddings/fonts; chart height adjusts; cards use CDS tokens.
4. **Accessible & Semantic**: HTML5 regions; descriptive labels; ARIA announcements for updates.
5. **Consistency with CDS**: Use `Card`, `Tabs`, `DataTable`, `DateRangePicker`, `Toast`.

## Accessibility Requirements

### Keyboard Navigation
- [ ] All interactive elements reachable via Tab; logical order.
- [ ] Visible focus indicators beyond browser default.
- [ ] Enter/Space activate buttons; Escape closes modals.

### Screen Reader Support
- [ ] Alt text for icons/images; chart description.
- [ ] Inputs have associated labels; error messages announced.
- [ ] Dynamic KPI changes announced via `aria-live`.
- [ ] Headings form logical structure: header → sections → cards.

### Visual Accessibility
- [ ] Contrast ≥ 4.5:1 for text; icons + color, not color alone.
- [ ] Minimum touch targets 24×24px; button height ≥ 44px.
- [ ] Text resizes to 200% without breaking layout.
- [ ] Focus visible at all times.

## Implementation Notes (for dev handoff)
- **Compact Mode**: Store `compact=true|false` in localStorage; expose via context/hook; apply CDS spacing/typography scale.
- **Date Range**: Single `DateRangePicker` with presets; remove duplicated controls.
- **Bank/Entity Switcher**: CDS `Select` with recent selections; sticky in header.
- **Cut‑off Timer**: Small countdown component; warns in alerts panel when nearing.
- **KPI Cards**: Components with tiers and optional collapse; include delta chips.
- **Chart**: Plotly responsive container inside CDS `Card`; height bound to mode.
- **Transactions/Approvals**: `Tabs` with `DataTable`; prioritized columns; virtualization; saved views.
- **Connectivity Status**: Inline health indicators for bank connections; toast notifications on failures.
