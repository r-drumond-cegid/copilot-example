# 💰 Finance Dashboard with AI Chatbot

Dashboard financier moderne intégrant un chatbot IA pour la gestion et l'analyse de comptes bancaires et transactions.

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

## 🎨 Technologies Utilisées

### Backend
- **FastAPI** - Framework API moderne
- **Pydantic** - Validation de données
- **Pandas** - Analyse de données
- **OpenAI** (à configurer) - Intelligence artificielle
- **LangChain** (à configurer) - Orchestration IA
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

Créez un fichier `.env` dans `backend/`:

```env
# OpenAI API (à configurer pour activer l'IA)
OPENAI_API_KEY=your_api_key_here

# Database (optionnel - actuellement en mémoire)
DATABASE_URL=postgresql://user:password@localhost/financedb
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

# Lancer un fichier spécifique
pytest tests/test_accounts.py -v
```

## 📱 Design Responsive

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
# Build Docker (à créer)
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

## 📄 Licence

Projet d'exemple - Usage éducatif

## 👥 Contribution

Suivre les directives dans `.github/instructions/chatbot-finance.instructions.md`

## 📞 Support

Pour questions et support, consulter la documentation API sur `/docs`

---

**Développé avec ❤️ en utilisant FastAPI, React et Plotly.js**
