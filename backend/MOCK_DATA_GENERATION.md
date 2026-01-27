# Mock Data Generation - Guide d'utilisation

Ce dossier contient les scripts et données pour générer des comptes bancaires et transactions de test.

## 📁 Fichiers disponibles

### Scripts Python

- **`generate_new_accounts.py`** - Script principal pour générer de nouveaux comptes avec transactions et balances
- **`verify_accounts.py`** - Script de vérification des données de comptes
- **`verify_transactions.py`** - Script de vérification des données de transactions

### Données actuelles

Les fichiers de fixtures contiennent actuellement :

#### `tests/fixtures/mock_accounts.py`
- **1188 entrées** dans `MOCK_ACCOUNTS_TIMELINE_30_DAYS`
- 6 comptes au total :
  - **Investment Portfolio Account** (FR76...555): 365 jours en EUR
  - **UK Operations Account** (GB12...012): 365 jours en GBP  
  - **Swiss Operations Account** (CH12...789): 365 jours en CHF
  - **Main Business Account**: 31 jours (janvier 2026)
  - **Savings Account**: 31 jours (janvier 2026)
  - **USD Operating Account**: 31 jours (janvier 2026)

#### `tests/fixtures/mock_transactions.py`
- **49 transactions** dans `MOCK_TRANSACTIONS_ENRICHED`
- Réparties sur 6 comptes
- Dates aléatoires tout au long de l'année 2026
- Toutes les transactions incluent :
  - Catégorie enrichie (id, name, icon, color, description)
  - Merchant (nom du marchand)
  - Tags (liste de mots-clés)

## 🚀 Comment générer de nouveaux comptes

### 1. Modifier la configuration dans `generate_new_accounts.py`

```python
NEW_ACCOUNTS = [
    {
        "account_description": "Votre Nouveau Compte",
        "iban": "XX1234567890123456789",
        "holder_company_name": "Votre Société",
        "initial_balance": 50000.0,
        "currency": "EUR",
        "allowed_overdraft": 5000.0,
    },
    # Ajoutez d'autres comptes ici...
]
```

### 2. Personnaliser les modèles de transactions

Modifiez `TRANSACTION_TEMPLATES` pour adapter les types de transactions à vos besoins :

```python
TRANSACTION_TEMPLATES = {
    "salary": {
        "base_amount": 5000.0,
        "variance": 500.0,
        "is_debit": False,
        # ...
    },
    # Autres catégories...
}
```

### 3. Exécuter la génération

```bash
cd backend
python generate_new_accounts.py
```

Le script génère :
- `new_transactions.txt` - 30 transactions formatées pour insertion
- `new_account_balances.txt` - 1095 balances quotidiennes (3 comptes × 365 jours)

### 4. Intégrer les données

Les nouvelles données doivent être ajoutées manuellement aux fichiers de fixtures :

**Pour les transactions** → `tests/fixtures/mock_transactions.py`
```python
MOCK_TRANSACTIONS_ENRICHED = [
    # ... transactions existantes ...
    # Coller ici le contenu de new_transactions.txt
]
```

**Pour les balances** → `tests/fixtures/mock_accounts.py`
```python
MOCK_ACCOUNTS_TIMELINE_30_DAYS = [
    # ... balances existantes ...
    # Coller ici le contenu de new_account_balances.txt
]
```

## 🔍 Vérification des données

### Vérifier les comptes

```bash
python verify_accounts.py
```

Affiche :
- Nombre total d'entrées
- Répartition par compte
- Plages de dates pour chaque compte

### Vérifier les transactions

```bash
python verify_transactions.py
```

Affiche :
- Nombre total de transactions
- Répartition par IBAN
- Détails des nouveaux comptes

## 📊 Structure des données

### Format d'une transaction enrichie

```python
{
    "account_description": "Investment Portfolio Account",
    "iban": "FR7655555555555555555555555",
    "holder_company_name": "ACME Investments",
    "operation_date": "2026-01-13",
    "value_date": "2026-01-13",
    "amount": -1940.88,
    "currency": "EUR",
    "is_debit": True,
    "category": {
        "id": "cat_insurance",
        "name": "Insurance",
        "icon": "🛡️",
        "color": "#8B4513",
        "description": "Insurance premiums and coverage"
    },
    "merchant": "SecureLife Insurance Co.",
    "tags": ["insurance", "protection", "monthly"]
}
```

### Format d'une balance de compte

```python
{
    "account_description": "Investment Portfolio Account",
    "iban": "FR7655555555555555555555555",
    "holder_company_name": "ACME Investments",
    "date": "2026-01-13",
    "value_balance": 248059.12,
    "currency": "EUR",
    "allowed_overdraft": 0.0
}
```

## 🎯 Catégories disponibles

Le script utilise 10 catégories de transactions :

| Catégorie | Icon | Couleur | Description |
|-----------|------|---------|-------------|
| salary | 💰 | #2E7D32 | Salary and compensation |
| rent | 🏢 | #D32F2F | Rent and lease payments |
| supplies | 📦 | #F57C00 | Office and business supplies |
| utilities | ⚡ | #1976D2 | Utilities and services |
| insurance | 🛡️ | #8B4513 | Insurance premiums |
| tax | 📊 | #5E35B1 | Tax payments |
| equipment | 🖥️ | #00796B | Equipment purchases |
| travel | ✈️ | #C2185B | Travel and transportation |
| other_income | 💵 | #388E3C | Other income |
| other_expense | 💸 | #C62828 | Other expenses |

## ⚙️ Configuration avancée

### Seed pour la reproductibilité

Le script utilise `random.seed(42)` pour garantir des résultats reproductibles. Changez cette valeur pour obtenir des données différentes.

### Nombre de transactions par compte

Par défaut, chaque compte génère 10 transactions. Modifiez dans `generate_transactions_for_account()` :

```python
num_transactions = 10  # Changez cette valeur
```

### Période couverte

Les balances sont générées pour toute l'année 2026 (365 jours). Pour changer :

```python
all_dates_2026 = [
    date(2026, 1, 1) + timedelta(days=i) 
    for i in range(365)  # Modifiez ici
]
```

## 📝 Notes importantes

1. **Cohérence des IBANs** : Assurez-vous que les IBANs sont uniques et respectent le format du pays
2. **Impact sur les balances** : Les transactions affectent automatiquement les balances quotidiennes
3. **Dates aléatoires** : Les dates de transactions sont réparties aléatoirement sur l'année 2026
4. **Multi-devises** : Le système supporte EUR, USD, GBP, CHF

## 🔄 Régénération complète

Pour régénérer complètement les données de test :

1. Sauvegarder les fixtures actuelles
2. Modifier `generate_new_accounts.py` selon vos besoins
3. Exécuter le script
4. Vérifier les résultats avec les scripts de validation
5. Intégrer manuellement dans les fixtures
6. Tester avec l'API FastAPI

---

*Dernière mise à jour : 27 janvier 2026*
