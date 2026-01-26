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