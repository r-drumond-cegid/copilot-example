# CDS Recommendations

## Mapping: UI Area → CDS Component(s)
- Top bar/header: `AppBar`/`Toolbar` → prefer `@cegid/cds-react` equivalents (TopBar/AppBar variants).
- Buttons: Use `Button` from `@cegid/cds-react` (sizes, variants, loading states).
- Forms: Replace MUI `TextField`, `Select`, `FormControl`, `InputLabel` with `@cegid/forms` inputs, selects, helpers.
- Dialogs/Modals: Use `Dialog` from `@cegid/cds-react`.
- Feedback: Use `Alert`, `Snackbar` from `@cegid/cds-react`.
- Data display: Use `Card`, `Chip`, `Table` (or `DataGrid` if applicable) from `@cegid/cds-react`.
- Date picking: Prefer `@cegid/forms` `DatePicker`/`DateRangePicker` (or CDS-provided range picker if available).
- Icons: Use CDS icon set if provided; otherwise align MUI icons to CDS guidelines.

## Integration Notes
- Imports priority: `@cegid/cds-react-ai` → `@cegid/cds-react` → `@cegid/forms` → (last) `@mui/material`.
- Theming: Keep a single `ThemeProvider`, but source tokens from CDS theme provider; align colors/spacing/typography to CDS.
- Forms: Ensure all labels, helper texts, validation messages use `@cegid/forms` patterns for a11y consistency.
- Tables: Add sorting indicators and `aria-sort` when sort is active.
- Charts: Keep Plotly but map colors to CDS theme tokens for consistency.

## Quick Examples
- Button replacement: `import { Button } from '@cegid/cds-react'` and migrate usages of MUI `Button` 1:1 where props align (variant/color/size).
- Text inputs: `import { TextField } from '@cegid/forms'` and move validation/labels to CDS field props.
- Dialog: `import { Dialog } from '@cegid/cds-react'` and keep accessibility props consistent (titles, `aria-labelledby`).

## Acceptance Criteria
- No MUI form fields remain; all forms use `@cegid/forms`.
- Common primitives (Button, Dialog, Alert, Chip, Card, Table) use `@cegid/cds-react`.
- Visuals match CDS theme tokens; typography and spacing align.
- a11y: Table sorting state announced; chat stream has `aria-live` for new messages; charts have descriptive labels.