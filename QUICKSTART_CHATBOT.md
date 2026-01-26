# 🚀 Quick Start Guide - Finance Dashboard avec Chatbot IA

## Démarrage rapide (5 minutes)

### 1. Configuration Azure OpenAI ⚙️

Le fichier `.env` est déjà créé dans `backend/` avec la configuration suivante :

```env
MODEL_NAME=gpt41
MODEL_URL=https://pulse-os-local-resource.cognitiveservices.azure.com/
MODEL_API_KEY=later
MODEL_API_VERSION=2024-12-01-preview
MODEL_API_TYPE=azure
MODEL_TEMPERATURE=0.1
```

**Note** : La clé API est actuellement définie à `later`. Le chatbot fonctionnera en mode fallback jusqu'à ce que vous configuriez une vraie clé.

### 2. Démarrer les serveurs 🖥️

#### Option A : Script automatique (Recommandé)

```powershell
# À la racine du projet
.\start-servers.ps1
```

#### Option B : Démarrage manuel

**Terminal 1 - Backend:**
```powershell
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Frontend:**
```powershell
cd frontend
npm install
npm run dev
```

### 3. Accéder à l'application 🌐

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **Documentation API**: http://localhost:8000/docs

### 4. Tester le chatbot 🤖

1. Ouvrez le frontend : http://localhost:3000
2. Cliquez sur l'icône du chatbot en bas à droite
3. Essayez ces questions :
   - "Bonjour"
   - "Quel est mon solde total ?"
   - "Montre-moi mes dernières transactions"

**Mode actuel** : Fallback (réponses prédéfinies)

## Configuration de la vraie clé Azure OpenAI 🔑

### Étape 1 : Obtenir une clé API

1. Connectez-vous au [portail Azure](https://portal.azure.com)
2. Accédez à votre ressource Azure OpenAI
3. Allez dans "Keys and Endpoint"
4. Copiez KEY 1 ou KEY 2

### Étape 2 : Mettre à jour la configuration

Éditez `backend/.env` et remplacez :

```env
MODEL_API_KEY=later
```

par :

```env
MODEL_API_KEY=votre-vraie-cle-api
```

### Étape 3 : Redémarrer le backend

```powershell
# Arrêter le serveur (Ctrl+C dans le terminal)
# Relancer
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Étape 4 : Tester la configuration

```powershell
cd backend
python test_chatbot_config.py
```

Vous devriez voir :
```
✓ Azure OpenAI client initialized successfully
✓ Chatbot Session: ✓ PASS
```

## Vérification rapide ✅

### Backend fonctionne ?

```powershell
curl http://localhost:8000/api/v1/balance-summary
```

Devrait retourner des données JSON.

### Frontend fonctionne ?

Ouvrez http://localhost:3000 dans votre navigateur.

### Chatbot fonctionne ?

Cliquez sur l'icône de chat et envoyez "Bonjour".

## Dépannage commun 🔧

### Erreur : Port 8000 déjà utilisé

```powershell
# Trouver le processus
Get-Process -Id (Get-NetTCPConnection -LocalPort 8000).OwningProcess

# Arrêter le processus ou utiliser un autre port
uvicorn app.main:app --reload --port 8001
```

### Erreur : Dépendances manquantes

**Backend:**
```powershell
cd backend
pip install -r requirements.txt
```

**Frontend:**
```powershell
cd frontend
npm install
```

### Chatbot ne répond pas

1. Vérifiez que le backend est démarré
2. Vérifiez la console du navigateur (F12) pour les erreurs
3. Vérifiez que `VITE_API_BASE_URL` dans `frontend/.env` pointe vers le bon port

### Azure OpenAI retourne des erreurs

1. Vérifiez que la clé API est valide
2. Vérifiez que l'URL de l'endpoint est correcte
3. Vérifiez que le nom du modèle correspond au déploiement Azure
4. Consultez [backend/CHATBOT_CONFIG.md](CHATBOT_CONFIG.md) pour plus de détails

## Fonctionnalités disponibles 🎯

### Dashboard
- ✅ Résumé des soldes de comptes
- ✅ Liste des transactions enrichies
- ✅ Graphiques interactifs (balance, catégories)
- ✅ Filtrage par date
- ✅ Alertes de solde faible

### Chatbot IA
- ✅ Questions en français
- ✅ Analyse contextuelle des finances
- ✅ Suggestions intelligentes
- ✅ Historique de conversation

### API
- ✅ Endpoints REST complets
- ✅ Documentation Swagger interactive
- ✅ Validation des données
- ✅ Gestion d'erreurs

## Données de test 📊

Le système utilise des données mocké enrichies incluant :

- **3 comptes** avec historique de 30 jours
- **500+ transactions** enrichies avec :
  - Catégories (alimentation, logement, transport, etc.)
  - Marchands identifiés
  - Tags automatiques
  - Montants réalistes

## Prochaines étapes 📚

1. **Explorer l'API** : http://localhost:8000/docs
2. **Personnaliser les catégories** : Voir `backend/app/services/enrichment.py`
3. **Ajouter des comptes** : Modifier `backend/tests/fixtures/mock_accounts.py`
4. **Activer Azure OpenAI** : Suivre le guide ci-dessus
5. **Lire la doc complète** : [README.md](../README.md)

## Documentation complète 📖

- **Guide principal** : [../README.md](../README.md)
- **Configuration chatbot** : [CHATBOT_CONFIG.md](CHATBOT_CONFIG.md)
- **Tests** : [tests/README.md](tests/README.md)
- **API** : http://localhost:8000/docs (après démarrage)

## Support 💬

Pour toute question :
1. Consultez la documentation complète
2. Vérifiez les logs du backend et frontend
3. Utilisez le test de configuration : `python test_chatbot_config.py`

---

**Bon développement ! 🚀**
