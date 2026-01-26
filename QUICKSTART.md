# Quick Start Guide

## Installation Rapide

### 1. Backend
```powershell
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 2. Frontend
```powershell
cd frontend
npm install
npm run dev
```

### 3. Accéder à l'application
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## Tester l'API

```powershell
# Obtenir les soldes
curl http://localhost:8000/api/v1/bank-account-balances

# Obtenir les transactions
curl "http://localhost:8000/api/v1/bank-transactions?from_date=2026-01-01&to_date=2026-01-26"

# Tester le chatbot
curl -X POST http://localhost:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Quel est mon solde total ?"}'
```

## Structure Créée

✅ **Backend complet**:
- 4 nouveaux modèles (BalanceSummary, TransactionCategory, EnrichedTransaction, Chat models)
- 3 services (enrichment, analytics, chatbot)
- 4 routers (accounts, transactions, chat, analytics)
- 10+ nouveaux endpoints

✅ **Frontend complet**:
- Architecture React complète avec Vite
- 8 composants principaux
- 4 clients API
- Graphiques Plotly.js interactifs
- Chatbot UI intégré
- Design 100% responsive

✅ **Fonctionnalités**:
- Enrichissement automatique des transactions
- Catégorisation intelligente
- Analytics et tendances
- Alertes de solde
- Chatbot conversationnel
- Visualisations interactives
