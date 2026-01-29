---
applyTo: '**'
---

# Directives générales de codage – Dashboard Finance

Objectif: fournir des règles claires, concises et actionnables pour garder le frontend React, le backend FastAPI et l’intégration CDS cohérents, accessibles et sécurisés.

## Quick Links
- Types & CDS: `frontend/src/types/cds-react.d.ts`
- Thème CDS: `frontend/src/theme/cegidTheme.js`
- Frontend config: `frontend/eslint.config.js`, `frontend/vite.config.ts`
- Backend structure: `backend/app/` (routes, services, modèles)
- Tests backend: `backend/tests/`
- Docs CDS: `docs/cds/`

## Style de code (Essentiels)
- HTML5 sémantique: `header`, `main`, `section`, `article`.
- JavaScript ES6+: `const`/`let`, fonctions fléchées, template literals.
- React: composants fonctionnels + hooks (`useState`, `useEffect`, `useMemo`).
- Graphiques: **Plotly.js** modulable et réactif, encapsulé dans des conteneurs UI.

## Conventions de nommage
- PascalCase: composants React, interfaces, types.
- camelCase: variables, fonctions, méthodes.
- `_privé`: membres privés de classe.
- ALL_CAPS: constantes.
- API: noms explicites (`fetchTransactions`, `calculateBalance`).

## Qualité & Sécurité
- Noms clairs; commenter les logiques complexes (filtrage, enrichissement).
- Gérer erreurs pour entrées utilisateur et appels API.
- Séparation stricte: Frontend (UI/graphes), Backend (routes/services/modèles), IA (orchestration).
- Sécurité bancaire: pas de clés en frontend, chiffrer données sensibles, valider/sanitiser toutes les entrées.

## Architecture & Spécifiques projet
- Types données: `Transaction`, `Account`, `BalanceSummary` (structurés et partagés).
- Enrichissement: fonctions de catégorisation/filtrage dédiées (testables).
- Reporting: composants Plotly réutilisables (balances, timelines, alertes).
- Responsiveness: desktop + mobile; layouts fluides.

## Cegid Design System (CDS) — Essentiels
- Composants standards d’abord: `Button`, `Input`, `Select`, `DataTable`, `DatePicker`, `Modal`, `Tabs`, `Accordion`, `Tooltip`, `Toast`, `Card`.
- Imports: utiliser `cds-react` (ou `frontend/src/cds-react-shim.js` si nécessaire). Centraliser types dans `frontend/src/types/cds-react.d.ts`.
- Thèmes: appliquer tokens via `frontend/src/theme/cegidTheme.js`; éviter surcharges non prévues.
- États/variantes: utiliser props officielles (`size`, `disabled`, `loading`, `error`, `success`).
- Formulaires: validations normalisées; empêcher doubles soumissions; désactiver actions pendant chargement.
- Sécurité: pas de secrets côté UI; inputs validés/sanitisés.

## Accessibilité — Checklist rapide (WCAG 2.1 AA)
- Focus visible; navigation clavier complète.
- Libellés clairs; `aria-*` appropriés; associer `label` aux champs.
- Tableaux: `th` avec `scope`; annonces `aria-live` si mises à jour asynchrones.
- Modales: piégeage du focus; fermeture via `Esc`; rôles `dialog`/`alertdialog`.
- Graphiques: descriptions accessibles; dimensions réactives.

## Transactions, Comptes & Reporting
- Types partagés et validations strictes.
- Enrichissement: catégories, filtres, regroupements (documenter et tester).
- Graphiques Plotly: réutilisables, encapsulés dans `Card`/`Panel`, réactifs.

## Chatbot
- Composant UI dédié; flux FastAPI → IA → réponse.
- Historiser les conversations côté backend.

## Outillage MCP CDS
- Consulter le catalogue composants; vérifier props/contraintes/accessibilité avant implémentation.
- Handoff Figma → Code: générer composants; intégrer Storybook/tests.
- Documenter choix & conformité dans `docs/cds/` (catalogue, rapport, recommandations, changelog).

## Tests & Linting (alignement rapide)
- Frontend: respecter `eslint.config.js`; corriger avant PR.
- Backend: maintenir et exécuter `backend/tests/`; cibler d’abord les modules modifiés.
- Accessibilité: vérifier focus, contrastes, labels et annonces.

Notes: cette version est volontairement concise. Utiliser `docs/` et fichiers référencés pour les détails d’implémentation.