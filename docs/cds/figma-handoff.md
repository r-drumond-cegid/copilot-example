# Figma → Code Handoff

## Status
- Blocked until a Figma design URL is provided.

## Generation Plan
1) Use `mcp_cds-mcp_generate-from-figma` with:
   - `figmaUrl`: <provide URL>
   - `componentName`: <target component name>
   - `packageName`: `cds-react-ai`
   - `generateStory`: true
   - `generateTests`: true
2) Validate generated code against project rules:
   - Functional components + hooks
   - Use `@cegid/cds-react` and `@cegid/forms` as required
   - Accessibility expectations from CDS
3) Integrate into app, wire props/state, and theme tokens.

## Acceptance
- Components render with CDS theme and pass basic a11y checks.
- Storybook stories and unit tests generated and running locally.