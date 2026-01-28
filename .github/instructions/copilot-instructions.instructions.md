---
applyTo: '**'
---

# Directives générales de codage – Dashboard Finance

## Style de code

* Utiliser les éléments HTML5 sémantiques (`header`, `main`, `section`, `article`, etc.)
* Préférer les fonctionnalités modernes de JavaScript (ES6+) : `const`/`let`, fonctions fléchées, template literals
* Dans React, privilégier les **Functional Components** et les hooks (`useState`, `useEffect`, `useMemo`, etc.)
* Pour les graphiques, utiliser **Plotly.js** de manière modulable et réactive

---

## Conventions de nommage

* **PascalCase** pour les composants React, interfaces et types
* **camelCase** pour les variables, fonctions et méthodes
* Préfixer les membres privés d'une classe avec un underscore `_`
* **ALL_CAPS** pour les constantes
* Pour les endpoints et fonctions d'API, utiliser des noms explicites (ex : `fetchTransactions`, `calculateBalance`)

---

## Qualité du code

* Utiliser des noms de variables et fonctions **clairs et explicites**
* Ajouter des commentaires pour les logiques complexes (ex : filtrage et enrichissement des transactions)
* Gérer les erreurs pour toutes les entrées utilisateurs et appels API
* Modulariser le code pour séparer clairement :

  * Frontend (UI, composants, graphiques)
  * Backend (FastAPI : routes, services, modèles de données)
  * Services IA (OpenAI / LangGraph)
* Respecter les bonnes pratiques de sécurité pour les données bancaires :

  * Ne jamais exposer les clés API dans le frontend
  * Chiffrement des données sensibles
  * Validation stricte des entrées utilisateurs

---

## Bonnes pratiques spécifiques au projet

* **Transactions et comptes** : créer des interfaces/types pour structurer les données (`Transaction`, `Account`, `BalanceSummary`)
* **Enrichissement des données** : ajouter des fonctions claires pour catégoriser et filtrer les transactions
* **Reporting** : prévoir des composants réutilisables pour graphiques Plotly (balances, timelines, alertes)
* **Chatbot** :

  * Créer un composant dédié pour l'interface conversationnelle
  * Orchestrer les appels FastAPI → IA → réponse utilisateur
  * Maintenir l'historique des conversations côté backend
* **Responsiveness** : tous les composants doivent être adaptés aux écrans desktop et mobile

---

## Cegid Design System (CDS)

* **Composants CDS** : utiliser les composants standards du DS (`Button`, `Input`, `Select`, `Checkbox`, `Radio`, `Textarea`, `FormField`, `DataTable`, `DatePicker`/`DateRangePicker`, `Modal`, `Tabs`, `Accordion`, `Tooltip`, `Toast`/`Notification`, `Card`). Éviter les composants maison si une alternative CDS existe.
* **Imports** : privilégier le paquet `cds-react` (ou le shim local `src/cds-react-shim.js` si nécessaire en attendant l'intégration). Les types doivent être centralisés dans `src/types/cds-react.d.ts`.
* **Thématisation** : appliquer les tokens CDS (couleurs, typographies, espacements) via `src/theme/cegidTheme.js`. Ne pas surcharger les styles au-delà des variables et thèmes prévus.
* **Accessibilité** : respecter WCAG 2.1 AA. États de focus visibles, navigation clavier complète, libellés clairs et `aria-*` appropriés. Associer `label` aux champs, utiliser des `th` avec `scope` dans les tableaux, et fournir des descriptions pour les graphiques.
* **États & variantes** : utiliser les variantes et props officielles (ex : `size`, `disabled`, `loading`, `error`, `success`). Éviter les styles ad hoc ou classes non standard.
* **Formulaires** : utiliser les composants de formulaire CDS, validations synchrones/asynchrones avec messages d’erreur normalisés. Empêcher les doubles soumissions et désactiver les actions pendant le chargement.
* **Modales/Dialogs** : gérer le piégeage du focus, fermeture via `Esc`, et rôles ARIA (`dialog`, `alertdialog`). Ne pas masquer du contenu sans rôles/accessibilité corrects.
* **Notifications** : utiliser `Toast`/`Alert` CDS pour les retours utilisateur (succès/erreur/info) avec messages concis et non intrusifs.
* **Listes & tableaux** : utiliser `DataTable` pour pagination, tri, sélection, et mises à jour asynchrones (prévoir `aria-live` si nécessaire).
* **Réactivité** : respecter les points de rupture CDS et layouts fluides. Les composants doivent s’adapter automatiquement aux tailles d’écran.
* **Graphiques** : conserver Plotly, mais encapsuler dans des conteneurs CDS (`Card`/`Panel`) et fournir des descriptions accessibles. Les dimensions doivent être réactives.
* **Sécurité** : aucune clé/secret en frontend, validation stricte des entrées et sanitisation des contenus.

---

## Intégration MCP CDS (outillage)

* **Catalogue & recherche** : consulter le catalogue des composants CDS pour sélectionner les bons composants et variantes.
* **Détails des composants** : vérifier les props, contraintes et attentes d’accessibilité avant implémentation.
* **Handoff Figma → Code** : lorsque des maquettes sont disponibles, générer les composants via l’outillage MCP et intégrer les artefacts produits (Storybook/tests) dans le projet.
* **Documentation** : consigner les choix et conformités dans `docs/cds/` (catalogue, rapport de conformité, recommandations, changelog).