## Job Statement
When reviewing daily cash position, I want to quickly see total balances, changes, and risk exposure at a glance, so I can decide whether to transfer funds, investigate anomalies, or adjust spending without scrolling through dense reports.

## Context & Motivation
- **Situation**: Morning check-in before operations; end-of-day reconciliation; monthly close.
- **Motivation**: Minimize time-to-insight; avoid surprises (overdrafts, sudden drops, cash idle).
- **Outcome**: Clear actions in <30s: transfer, investigate, or confirm stability.

## Personas (Allmybanks clients)
- **Treasury Manager**: Multi-bank cash oversight, cut‑off times, cash pooling.
- **Cash Manager/AP Lead**: Payment approvals, status tracking, bank connectivity health.
- **CFO/Finance Director**: Executive snapshot with risks and actions, export/share.
- **Accountant/Controller**: Reconciliation details; balances by entity/bank; overdraft limits.

## Current Solution & Pain Points (from screenshot & Allmybanks context)
- **Large hero metric** forces vertical scrolling; secondary KPIs fall below the fold on laptops.
- **Redundant date controls** and preset chips crowd the header; unclear hierarchy.
- **Chart area** consumes excessive height without summary deltas; gridlines heavy.
- **Transaction list** dense; missing progressive filtering and saved views (e.g., by bank/entity).
- **Multi-bank context**: Hard to toggle between bank groups, entities, cash pools.
- **Operational risk**: Cut‑off times, approval queues, and connectivity issues not surfaced.
- **Cognitive load**: Many numbers presented at once without grouping (primary vs secondary).

## Desired Outcomes (Success Criteria)
- **Time-to-insight**: Primary KPIs visible above the fold on 1366×768; insight in <30s.
- **Actionability**: Clear exceptions (low balance, overdraft risk) with direct actions.
- **Comparability**: Change vs previous period (%) and absolute deltas.
- **Operational awareness**: Cut‑off countdowns, approval backlog, connectivity status in header.
- **Multi‑bank clarity**: Switch bank group/entity and cash pool summaries without losing context.
- **Responsiveness**: Works well on 13" laptops; compact layout option reduces padding/fonts.
- **Accessibility**: WCAG 2.1 AA; semantic structure; screen-reader labels and announcements.

## Allmybanks Client Context
- **Multi‑bank treasury**: Aggregate balances across banks, entities, currencies.
- **Daily routines**: Morning cash position, payment approvals, FX exposure checks.
- **Decisions**: Sweep transfers, short‑term investments, cover overdrafts, escalate approvals.
- **Key signals**: Cash pool utilization, bank fees/limits, unusual drops, FX volatility.

## Improvement Themes (JTBD-aligned)
- **Visual hierarchy**: Primary (Total Balance, Δ vs prior), Secondary (Avg/Min/Max), Tertiary (Overdraft, Accounts count).
- **Progressive disclosure**: Collapse hero; expand details on demand; sticky filters.
- **Density control**: "Compact mode" toggle to reduce spacing, font sizes, and chart height.
- **Focused comparisons**: Inline chips for period deltas and anomalies; quick insights panel.
- **Operational widgets**: Cut‑off timers, approvals summary, connectivity status, cash pool overview.
