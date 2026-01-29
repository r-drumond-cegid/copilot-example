# 🧭 Guide de Contribution

Ce dépôt utilise une stratégie « PR only » avec branche `main` protégée. Les PRs doivent passer les vérifications CI/CD et être approuvées par `@r-drumond-cegid` (Code Owner) avant fusion.

## 🔁 Flux de travail
- Créez une branche depuis `main` (ex: `feature/xyz`, `fix/bug-123`).
- Commitez vos changements et poussez la branche sur votre fork ou sur le repo si vous avez les droits.
- Ouvrez une Pull Request vers `main` et décrivez clairement vos changements.
- Attendez la validation CI/CD et la revue obligatoire de `@r-drumond-cegid`.
- Fusionnez via l’option standard (selon les règles du dépôt) lorsque tous les contrôles sont verts et l’approbation accordée.

## 🌿 Nommage et commits
- Branches: `feature/<sujet>`, `fix/<sujet>`, `docs/<sujet>`
- Commits (recommandé): `feat: …`, `fix: …`, `docs: …`, `chore: …`, `test: …`

## ✅ Avant d’ouvrir une PR
- Frontend:
  - `npm ci` puis `npm run lint` (si applicable) et `npm run build`
- Backend:
  - `pip install -r backend/requirements.txt` puis `pytest`
- Slides (si modifiés):
  - `npm run slides` (voir section Slides dans le README)

Les workflows CI exécuteront ces étapes automatiquement, mais lancer localement aide à détecter les erreurs plus tôt.

## 🔒 Vérifications obligatoires (CI/CD)
Consultez l’aperçu détaillé dans le README: [CI/CD Workflows (Overview)](README.md#️-cicd-workflows-overview)
- Workflow Lint: lint des fichiers `.github/workflows/*`
- CI: build frontend + tests backend
- Dependency Review: bloque des vulnérabilités « high »
- CodeQL: analyse SAST JS & Python (également planifié chaque semaine)

Ces contrôles doivent être au vert pour fusionner dans `main`.

## 👁️ Revues & Code Owners
- Les PRs nécessitent au moins 1 approbation.
- Les revues des Code Owners sont requises. Voir [.github/CODEOWNERS](.github/CODEOWNERS).

## 🌐 Déploiement GitHub Pages
- Les slides sont déployés depuis `slides/` via le workflow Pages.
- Si l’environnement `github-pages` exige une approbation, `@r-drumond-cegid` approuve le déploiement après fusion.

## 🔐 Sécurité & secrets
- Ne commitez jamais de secrets (tokens, clés API). Utilisez des variables d’environnement/Secrets GitHub.
- Pour le registre JFrog/npm privé, préférez la configuration utilisateur (`%USERPROFILE%/.npmrc`) plutôt qu’un fichier de projet commité.

## 📝 Bonnes pratiques
- Petites PRs, descriptions claires, screenshots pour les changements UI.
- Mettez à jour la documentation si nécessaire (README, docs/…).
- Ajoutez des tests pertinents lorsque c’est applicable.

## ▶️ Commandes utiles
```powershell
# Créer une branche
git checkout -b feature/mon-sujet

# Enregistrer les changements
git add .
git commit -m "feat: mon changement"

# Pousser la branche et créer la PR
git push -u origin feature/mon-sujet
# Ouvrez ensuite une PR vers main depuis GitHub
```

Pour toute question, consultez le README ou ouvrez une discussion.