# 💰 Finance Dashboard with AI Chatbot

Dashboard financier moderne intégrant un chatbot IA pour la gestion et l'analyse de comptes bancaires et transactions.

## 📊 Présentation

- **Slides en ligne** : [slides/index.html](slides/index.html)
- **PDF** : [slides/slides.pdf](slides/slides.pdf)
- **Source Markdown** : [slides/slides.md](slides/slides.md)

### Commandes Slides

```bash
# Générer HTML
npm run slides

# Générer PDF
npm run slides:pdf

# Générer les deux
npm run slides:all

# Mode watch (auto-refresh)
npm run slides:watch

# Serveur local
npm run slides:serve
```

## 🎯 Fonctionnalités

### Backend (FastAPI)
- ✅ **API REST** pour comptes et transactions
- ✅ **Enrichissement automatique** des transactions (catégorisation, détection de marchands)
- ✅ **Analytics avancées** (tendances, résumés, alertes)
- ✅ **Chatbot IA** avec historique conversationnel
- ✅ **Validation de données** avec Pydantic
- ✅ **Tests complets** avec pytest

### Frontend (React + Vite)
- ✅ **Interface responsive** (desktop, tablet, mobile)
- ✅ **Graphiques interactifs** (Plotly.js)
- ✅ **Chatbot intégré** avec suggestions contextuelles
- ✅ **Filtrage et tri** des transactions
- ✅ **Alertes en temps réel**
- ✅ **Résumés financiers** dynamiques

## 📋 Structure du Projet

```
copilot-example/
├── backend/
│   ├── app/
│   │   ├── models/          # Modèles de données (Account, Transaction, Chat)
│   │   ├── routes/          # Endpoints API (accounts, transactions, chat, analytics)
│   │   └── services/        # Services (enrichment, analytics, chatbot)
│   ├── tests/               # Tests unitaires et d'intégration
│   └── requirements.txt     # Dépendances Python
├── frontend/
│   ├── src/
│   │   ├── api/            # Clients API
│   │   ├── components/     # Composants React
│   │   │   ├── charts/    # Graphiques Plotly
│   │   │   ├── chatbot/   # Interface chatbot
│   │   │   ├── dashboard/ # Composants dashboard
│   │   │   └── layout/    # Layout
│   │   └── pages/         # Pages principales
│   └── package.json       # Dépendances Node.js
└── .github/
    └── instructions/      # Directives de codage
```

## 🚀 Installation et Démarrage

### Prérequis
- **Python 3.10+**
- **Node.js 18+**
- **npm ou yarn**

### 1. Backend

```powershell
# Naviguer vers le dossier backend
cd backend

# Installer les dépendances
pip install -r requirements.txt

# Lancer les tests
pytest

# Démarrer le serveur FastAPI
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Le backend sera accessible sur `http://localhost:8000`
- Documentation API: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### 2. Frontend

```powershell
# Naviguer vers le dossier frontend
cd frontend

# Installer les dépendances
npm install

# Démarrer le serveur de développement
npm run dev
```

Le frontend sera accessible sur `http://localhost:3000`

### 🔐 Registry JFrog pour `@cegid`

Pour installer les packages `@cegid`, configurez l'accès au registre JFrog.

1) Générer un token d'accès depuis JFrog:
- Ouvrir: https://cegid.jfrog.io/ui/user_profile
- Créer un Access Token (ou utiliser "Set Me Up" sur le repo npm)

2) Authentification via commande (recommandé):

```powershell
npm login --registry=https://cegid.jfrog.io/artifactory/api/npm/dsy-npm-all/ --scope=@cegid
```

- Username: votre identifiant JFrog
- Password: collez le token généré
- Email: votre email

3) Configuration `.npmrc` (si besoin):

- Projet (déjà présent): voir [frontend/.npmrc](frontend/.npmrc) et [.npmrc](.npmrc)
- Utilisateur (plus sûr, hors dépôt): `%USERPROFILE%\.npmrc`

Exemple de contenu:

```ini
@cegid:registry=https://cegid.jfrog.io/artifactory/api/npm/dsy-npm-all/
//cegid.jfrog.io/:_authToken=<votre-token>
//cegid.jfrog.io/:email=ronaldo.drumond@cegid.com
//cegid.jfrog.io/:always-auth=true
```

4) Vérification:

```powershell
npm ping --registry=https://cegid.jfrog.io/artifactory/api/npm/dsy-npm-all/
npm whoami --registry=https://cegid.jfrog.io/artifactory/api/npm/dsy-npm-all/
npm view @cegid/cds-react version --registry=https://cegid.jfrog.io/artifactory/api/npm/dsy-npm-all/
```

5) Sécurité:
- Évitez de committer des tokens dans le repo
- Préférez `%USERPROFILE%\.npmrc` pour les secrets
- Si vous utilisez un `.npmrc` de projet, remplacez le placeholder par le token local et ajoutez des règles internes pour la gestion des secrets

## 📊 Endpoints API Principaux

### Comptes
- `GET /api/v1/bank-account-balances` - Liste des soldes
- `GET /api/v1/balance-summary` - Résumé agrégé
- `GET /api/v1/alerts` - Alertes de solde faible

### Transactions
- `GET /api/v1/bank-transactions` - Liste des transactions
- `GET /api/v1/transactions/enriched` - Transactions enrichies avec catégories
- `GET /api/v1/transactions/trends` - Tendances et statistiques
- `GET /api/v1/categories` - Liste des catégories

### Chatbot
- `POST /api/v1/chat` - Envoyer un message
- `GET /api/v1/chat/history/{session_id}` - Historique de conversation
- `DELETE /api/v1/chat/{session_id}` - Supprimer une session
- `GET /api/v1/chat/sessions` - Lister les sessions actives

### Analytics
- `GET /api/v1/analytics/summary` - Résumé analytique
- `GET /api/v1/analytics/trends` - Tendances financières

## 🎨 Technologies Utilisées

### Backend
- **FastAPI** - Framework API moderne
- **Pydantic** - Validation de données
- **Pandas** - Analyse de données
- **Azure OpenAI** - Intelligence artificielle (configurée)
- **LangChain** - Orchestration IA
- **pytest** - Tests

### Frontend
- **React 18** - Interface utilisateur
- **Vite** - Build tool rapide
- **Plotly.js** - Graphiques interactifs
- **Axios** - Client HTTP
- **React Router** - Navigation
- **date-fns** - Manipulation de dates

## 🔧 Configuration

### Variables d'Environnement Backend

Créez un fichier `.env` dans `backend/` (voir `.env.example` pour un modèle):

```env
# Azure OpenAI Configuration
MODEL_NAME=gpt41
MODEL_URL=https://pulse-os-local-resource.cognitiveservices.azure.com/
MODEL_API_KEY=your-actual-api-key-here
MODEL_API_VERSION=2024-12-01-preview
MODEL_API_TYPE=azure
MODEL_TEMPERATURE=0.1

# FastAPI Configuration
BACKEND_PORT=8000
DEBUG=True
```

**📖 Configuration détaillée**: Consultez [backend/CHATBOT_CONFIG.md](backend/CHATBOT_CONFIG.md) pour le guide complet de configuration du chatbot.

### Tester la Configuration

```powershell
cd backend
python test_chatbot_config.py
```

### Variables d'Environnement Frontend

Créez un fichier `.env` dans `frontend/`:

```env
VITE_API_BASE_URL=http://localhost:8000/api/v1
```

## 📝 Modèles de Données

### Account
```python
{
  "account": "Main Business Account",
  "iban": "FR7612345678901234567890123",
  "company": "ACME Corporation",
  "date": "2026-01-26",
  "balance": 150000.50,
  "currency": "EUR",
  "allowed_overdraft": 10000.0
}
```

### Transaction Enrichie
```python
{
  "account": "Main Business Account",
  "operation_date": "2026-01-15",
  "amount": 1500.75,
  "is_debit": true,
  "category": {
    "id": "supplies",
    "name": "Fournitures",
    "color": "#6c757d"
  },
  "merchant": "Office Depot",
  "tags": ["business", "large"]
}
```

## 🧪 Tests

```powershell
# Lancer tous les tests
cd backend
pytest

# Lancer avec couverture
pytest --cov=app --cov-report=html
utilise **Azure OpenAI** (GPT-4) pour fournir une assistance financière intelligente.

### Fonctionnalités

- ✅ **Analyse contextuelle** des comptes et transactions
- ✅ **Réponses personnalisées** basées sur votre situation financière
- ✅ **Historique de conversation** pour un contexte continu
- ✅ **Suggestions intelligentes** de questions
- ✅ **Mode fallback** avec réponses prédéfinies si Azure OpenAI non configuré

### Exemples de questions

- "Quel est mon solde total ?"
- "Quelles sont mes dépenses ce mois ?"
- "Y a-t-il des alertes sur mes comptes ?"
- "Génère un rapport mensuel"
- "Analyse mes habitudes de dépense"

### Configuration

Voir [backend/CHATBOT_CONFIG.md](backend/CHATBOT_CONFIG.md) pour le guide complet de configuration Azure OpenAI
L'interface s'adapte automatiquement aux différentes tailles d'écran:

- **Desktop** (≥1024px): Layout complet avec sidebar
- **Tablet** (768px-1023px): Layout adapté
- **Mobile** (<768px): Layout simplifié avec navigation condensée

## 🤖 Chatbot IA

Le chatbot comprend:
- Questions sur les soldes
- Analyse des transactions
- Génération de rapports
- Détection de tendances

**Note**: L'intégration OpenAI nécessite une clé API. Actuellement, le chatbot utilise des réponses règles-based pour démonstration.

## 🔐 Sécurité

- ✅ CORS configuré
- ✅ Validation stricte des entrées
- ✅ Gestion d'erreurs robuste
- ⚠️ **À implémenter**: Authentification, chiffrement, rate limiting

## 📦 Production

### Backend
```powershell
# Bx] Intégration Azure créer)
docker build -t finance-dashboard-backend .
docker run -p 8000:8000 finance-dashboard-backend
```

### Frontend
```powershell
npm run build
# Les fichiers sont dans dist/
```

## 🛠️ Développement Futur

### Priorité Haute
- [ ] Intégration OpenAI complète
- [ ] Migration vers base de données PostgreSQL
- [ ] Authentification utilisateur
- [ ] Export de rapports (PDF, Excel)

### Priorité Moyenne
- [ ] Notifications push
- [ ] Rapports programmés
- [ ] Multi-devises avancé
- [ ] Intégration bancaire réelle (API)

### Priorité Basse
- [ ] Mode sombre
- [ ] Personnalisation des catégories
- [ ] Budgets et objectifs
- [ ] Prévisions ML

### TODO: Migration CDS (UI)
- [ ] Auditer les imports `@mui/material` restants dans le frontend
- [ ] Remplacer les imports MUI par le shim `@cegid/cds-react` (alias Vite) où nécessaire
- [ ] Intégrer les packages réels `@cegid/cds-react` et `@cegid/forms` via le registre JFrog (voir la section "🔐 Registry JFrog pour @cegid")
- [ ] Retirer les alias de shims et basculer les imports vers les packages `@cegid/*` une fois l’accès au registre configuré

## 📄 Licence

Projet d'exemple - Usage éducatif

## 🔒 Collaboration & Branch Protection

- **Branch protection (UI)**: Settings → Branches → Add rule for `main`.
  - Require a pull request before merging (1 approval)
  - Require review from Code Owners
  - Require branches to be up to date
  - Select required status checks: “Workflow Lint”, “Deploy Slides (GitHub Pages)”
  - Include administrators (optional)
- **Code owners**: [\.github/CODEOWNERS](.github/CODEOWNERS) contains `* @r-drumond-cegid` so your review is required on all PRs.
- **Who can push**:
  - Personal repo: set collaborators to "Read" so only the owner can push; others use forks → PRs.
  - Org repo: use “Restrict who can push” in the branch rule and add your user/team.
- **Pages approvals (UI)**: Settings → Environments → `github-pages` → Protection rules → Required reviewers: add `@r-drumond-cegid`.

## 👥 Contribution

Suivre les directives dans `.github/instructions/chatbot-finance.instructions.md`

## 📞 Support

Pour questions et support, consulter la documentation API sur `/docs`

---

**Développé avec ❤️ en utilisant FastAPI, React et Plotly.js**
