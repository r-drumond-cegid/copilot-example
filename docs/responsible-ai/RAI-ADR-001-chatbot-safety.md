# RAI-ADR-001 — Chatbot Safety, Accessibility, and Privacy

Date: 2026-01-30
Status: Accepted
Owner: Platform Team

## Context
A financial assistant chatbot (FastAPI backend + React frontend) provides guidance using Azure OpenAI when configured, and a rule-based fallback otherwise. It processes user prompts and summarizes account balances and transactions from mock data.

## Decision
- Bias safeguards: keep prompts neutral, avoid demographic inferences; add non-discriminatory fallback logic; add test inputs with diverse names and non‑ASCII characters.
- Accessibility: ensure keyboard operation and screen-reader support for chat UI; add aria labels and polite announcements.
- Privacy: do not expose secrets to frontend; limit retained chat history; add session auto-pruning; provide deletion endpoint.
- Explainability: tag each assistant message with metadata indicating source ("azure" or "fallback"), model info, and temperature when applicable.
- Security: keep CORS wide only in development; document production restrictions.

## Details
- Backend changes:
  - `services/chatbot.py`: `generate_ai_response()` now returns `(text, source)`; assistant messages store `metadata` (`source`, `model_name`, optional `temperature`, `explain`).
  - Session retention: `_prune_expired_sessions(max_age_hours=24)` purges inactive sessions; invoked at session creation and when listing sessions.
- Frontend changes:
  - `Chatbot.jsx`: added `aria-label` to open/close `Fab`; dialog has labeled controls; live region for assistant updates.

## Alternatives Considered
- Persist conversations in DB with TTL — postponed to keep scope small and avoid storing PII during prototyping.
- Full explainability UI — deferred; metadata is available for future surfacing.

## Compliance Checklist (WCAG 2.1 AA & RAI Quick Check)
- Keyboard-only usage supported; Enter/Shift+Enter documented.
- Visible labels on controls; screen-reader announcements present.
- Color is not sole indicator; icons/text used.
- Zoom/responsive layout tested (mobile dialog fullscreen).
- Non‑ASCII inputs supported.

## Risks & Mitigations
- Model drift/bias: keep fallback path; test with diverse inputs; log sources.
- Data leakage: environment secrets only on server; no user secrets collected.
- Session accumulation: automatic pruning; delete endpoint available.

## Rollout & Verification
- Run unit tests including bias edge cases.
- Manual a11y quick test: keyboard nav and screen reader labels.
- Verify metadata present in `chat` responses.

## Follow-ups
- Consider configurable retention window.
- Add production CORS allowlist and auth middleware.
- Surface explainability metadata in the UI (tooltip or dev toggle).
