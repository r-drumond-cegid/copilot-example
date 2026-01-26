# Configuration du Chatbot avec Azure OpenAI

## Vue d'ensemble

Le chatbot utilise Azure OpenAI pour fournir une assistance financière intelligente. Il peut analyser les comptes, transactions et fournir des insights personnalisés.

## Configuration

### Variables d'environnement

Créez un fichier `.env` dans le dossier `backend/` avec les paramètres suivants :

```env
MODEL_NAME=gpt41
MODEL_URL=https://pulse-os-local-resource.cognitiveservices.azure.com/
MODEL_API_KEY=your-actual-api-key-here
MODEL_API_VERSION=2024-12-01-preview
MODEL_API_TYPE=azure
MODEL_TEMPERATURE=0.1
```

### Paramètres

- **MODEL_NAME** : Nom du modèle de déploiement dans Azure OpenAI (ex: `gpt41`, `gpt-4`, `gpt-35-turbo`)
- **MODEL_URL** : URL de votre ressource Azure Cognitive Services
- **MODEL_API_KEY** : Clé API Azure OpenAI (à obtenir depuis le portail Azure)
- **MODEL_API_VERSION** : Version de l'API Azure OpenAI
- **MODEL_API_TYPE** : Type d'API (toujours `azure` pour Azure OpenAI)
- **MODEL_TEMPERATURE** : Contrôle la créativité des réponses (0.0 = déterministe, 1.0 = créatif)

## Mode de fonctionnement

### Avec Azure OpenAI configuré

Lorsque la clé API est configurée, le chatbot utilise Azure OpenAI pour :
- Comprendre le contexte financier de l'utilisateur
- Analyser les transactions et soldes
- Fournir des réponses personnalisées et contextuelles
- Générer des insights basés sur les données

### Mode fallback (sans Azure OpenAI)

Si la clé API n'est pas configurée (valeur `later`), le chatbot utilise des réponses prédéfinies basées sur des règles :
- Réponses simples aux questions courantes
- Informations basiques sur les soldes et transactions
- Suggestions prédéfinies

## Fonctionnalités

### 1. Contexte financier enrichi

Le système passe automatiquement le contexte financier à l'IA :
- Soldes des comptes
- Transactions récentes
- Nombre de comptes

### 2. Historique de conversation

- Conserve les 10 derniers messages pour maintenir le contexte
- Sessions persistantes identifiées par `session_id`
- Permet des conversations continues

### 3. Suggestions intelligentes

Génère des suggestions de questions basées sur le contexte de la conversation.

## API Endpoints

### POST `/api/v1/chat`

Envoie un message au chatbot.

**Requête :**
```json
{
  "message": "Quel est mon solde total ?",
  "session_id": "sess_abc123"  // optionnel
}
```

**Réponse :**
```json
{
  "session_id": "sess_abc123",
  "message": {
    "id": "msg_def456",
    "session_id": "sess_abc123",
    "role": "assistant",
    "content": "Votre solde total actuel est de 15,234.50 EUR.",
    "timestamp": "2026-01-26T10:30:00",
    "metadata": {}
  },
  "suggestions": [
    "Quelles sont mes dépenses ce mois ?",
    "Y a-t-il des alertes sur mes comptes ?",
    "Affiche un graphique de l'évolution"
  ]
}
```

### GET `/api/v1/chat/history/{session_id}`

Récupère l'historique d'une session.

### DELETE `/api/v1/chat/{session_id}`

Supprime une session et son historique.

### GET `/api/v1/chat/sessions`

Liste toutes les sessions actives.

## Utilisation dans le frontend

Le composant React `Chatbot` est déjà intégré :

```jsx
import Chatbot from '../components/chatbot/Chatbot';

function Dashboard() {
  const [chatbotOpen, setChatbotOpen] = useState(false);
  
  return (
    <>
      {/* Dashboard content */}
      <Chatbot 
        isOpen={chatbotOpen} 
        onToggle={() => setChatbotOpen(!chatbotOpen)} 
      />
    </>
  );
}
```

## Obtenir une clé API Azure OpenAI

1. Connectez-vous au [portail Azure](https://portal.azure.com)
2. Créez ou accédez à votre ressource Azure OpenAI
3. Allez dans "Keys and Endpoint"
4. Copiez la clé API KEY 1 ou KEY 2
5. Copiez l'URL de l'endpoint
6. Notez le nom de votre déploiement (MODEL_NAME)
7. Mettez à jour le fichier `.env`

## Sécurité

⚠️ **Important** :
- Ne jamais commiter le fichier `.env` dans le contrôle de version
- Le fichier `.gitignore` est configuré pour exclure les fichiers `.env`
- Utiliser des variables d'environnement en production
- Restreindre l'accès à la clé API Azure

## Dépannage

### Le chatbot utilise les réponses fallback

Vérifiez que :
- Le fichier `.env` existe dans `backend/`
- `MODEL_API_KEY` n'est pas égal à `later`
- Les variables d'environnement sont chargées correctement
- La ressource Azure OpenAI est accessible

### Erreurs d'API

Si vous voyez des erreurs dans les logs :
- Vérifiez que la clé API est valide
- Vérifiez que l'URL de l'endpoint est correcte
- Vérifiez que le nom du modèle correspond au déploiement Azure
- Vérifiez la version de l'API

### Installation des dépendances

Assurez-vous que les packages Python sont installés :
```bash
cd backend
pip install -r requirements.txt
```

Packages requis :
- `openai>=1.12.0`
- `python-dotenv>=1.0.0`
