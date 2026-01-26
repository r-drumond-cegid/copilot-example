"""Mock chat session data for testing."""

from typing import List, Dict, Any
from datetime import datetime, timedelta


# Sample chat session with balance inquiry
MOCK_CHAT_SESSION_BALANCE_INQUIRY = {
    "session_id": "sess_balance_001",
    "user_id": "user_test_123",
    "created_at": "2026-01-26T09:00:00Z",
    "updated_at": "2026-01-26T09:01:30Z",
    "context": {
        "total_balance": 728501.92,
        "currency": "EUR",
        "account_count": 3,
        "recent_transactions_count": 20,
    },
    "messages": [
        {
            "role": "user",
            "content": "Bonjour, quel est mon solde total ?",
            "timestamp": "2026-01-26T09:00:00Z",
        },
        {
            "role": "assistant",
            "content": "Bonjour ! Votre solde total actuel est de 728,501.92 EUR réparti sur 3 comptes.",
            "timestamp": "2026-01-26T09:00:02Z",
            "context_used": {
                "accounts": [
                    {"account": "Main Business Account", "balance": 151417.60, "currency": "EUR"},
                    {"account": "Savings Account", "balance": 501583.32, "currency": "EUR"},
                    {"account": "USD Operating Account", "balance": 75501.00, "currency": "USD", "converted_to_eur": 75501.00},
                ],
            },
        },
        {
            "role": "user",
            "content": "Quels sont mes comptes disponibles ?",
            "timestamp": "2026-01-26T09:01:00Z",
        },
        {
            "role": "assistant",
            "content": "Vous avez 3 comptes actifs :\n1. Main Business Account (FR76...123) : 151,417.60 EUR\n2. Savings Account (FR76...987) : 501,583.32 EUR\n3. USD Operating Account (US12...345) : 75,501.00 USD",
            "timestamp": "2026-01-26T09:01:02Z",
        },
    ],
}

# Sample chat session with transaction analysis
MOCK_CHAT_SESSION_TRANSACTION_ANALYSIS = {
    "session_id": "sess_trans_002",
    "user_id": "user_test_123",
    "created_at": "2026-01-26T10:30:00Z",
    "updated_at": "2026-01-26T10:35:45Z",
    "context": {
        "total_balance": 728501.92,
        "currency": "EUR",
        "date_range": {"start": "2026-01-01", "end": "2026-01-31"},
        "transaction_count": 20,
        "total_income": 35730.00,
        "total_expense": 28644.65,
    },
    "messages": [
        {
            "role": "user",
            "content": "Quelles sont mes dépenses ce mois-ci ?",
            "timestamp": "2026-01-26T10:30:00Z",
        },
        {
            "role": "assistant",
            "content": "En janvier 2026, vous avez dépensé 28,644.65 EUR répartis ainsi :\n\n📊 Top 5 catégories de dépenses :\n1. Équipement : 12,500.00 EUR\n2. Fournitures : 5,300.75 EUR\n3. Taxes : 3,200.00 EUR\n4. Loyer : 4,300.00 EUR\n5. Déplacements : 1,170.75 EUR\n\nVotre plus grosse dépense était un achat d'équipement chez Dell Business Solutions (12,500 EUR).",
            "timestamp": "2026-01-26T10:30:03Z",
            "context_used": {
                "expense_categories": [
                    {"category": "Équipement", "amount": 12500.00},
                    {"category": "Fournitures", "amount": 5300.75},
                    {"category": "Taxes", "amount": 3200.00},
                    {"category": "Loyer", "amount": 4300.00},
                    {"category": "Déplacements", "amount": 1170.75},
                ],
                "largest_expense": {
                    "merchant": "Dell Business Solutions",
                    "amount": 12500.00,
                    "date": "2026-01-18",
                },
            },
        },
        {
            "role": "user",
            "content": "Est-ce que mes dépenses sont normales ?",
            "timestamp": "2026-01-26T10:33:00Z",
        },
        {
            "role": "assistant",
            "content": "Vos dépenses de janvier sont légèrement supérieures à la moyenne mensuelle (+15% environ), principalement à cause de l'achat d'équipement exceptionnel de 12,500 EUR.\n\nSans cet achat ponctuel, vos dépenses courantes (16,144.65 EUR) sont cohérentes avec les mois précédents.\n\n💡 Conseil : Vos dépenses récurrentes (loyer, services publics, assurances) représentent environ 30% de vos dépenses totales, ce qui est sain.",
            "timestamp": "2026-01-26T10:33:04Z",
        },
        {
            "role": "user",
            "content": "Peux-tu me donner un résumé de mes revenus ?",
            "timestamp": "2026-01-26T10:35:00Z",
        },
        {
            "role": "assistant",
            "content": "Revenus de janvier 2026 : 35,730.00 EUR\n\n💰 Répartition :\n- Salaires : 13,000.00 EUR (2 versements)\n- Paiements clients : 18,480.00 EUR\n- Retours d'investissement : 1,250.00 EUR\n- Paiements US (convertis) : 4,500.00 USD\n\nVotre flux de trésorerie net ce mois : +7,085.35 EUR ✅\n\nVos revenus sont diversifiés, ce qui est un bon signe de stabilité financière.",
            "timestamp": "2026-01-26T10:35:03Z",
            "context_used": {
                "income_breakdown": {
                    "salary": 13000.00,
                    "customer_payments": 18480.00,
                    "investment_returns": 1250.00,
                    "us_payments_usd": 4500.00,
                },
                "net_flow": 7085.35,
            },
        },
    ],
}

# Sample chat session with alerts and recommendations
MOCK_CHAT_SESSION_ALERTS = {
    "session_id": "sess_alert_003",
    "user_id": "user_test_456",
    "created_at": "2026-01-26T14:00:00Z",
    "updated_at": "2026-01-26T14:05:20Z",
    "context": {
        "total_balance": 15000.00,
        "currency": "EUR",
        "account_count": 1,
        "alerts": [
            {
                "severity": "warning",
                "type": "low_balance",
                "message": "Solde faible sur Main Account",
                "threshold": 20000.00,
            }
        ],
    },
    "messages": [
        {
            "role": "assistant",
            "content": "⚠️ Alerte : Le solde de votre compte principal (Main Account) est de 15,000 EUR, ce qui est inférieur au seuil recommandé de 20,000 EUR pour assurer vos paiements récurrents.",
            "timestamp": "2026-01-26T14:00:00Z",
            "proactive": True,
        },
        {
            "role": "user",
            "content": "Que me conseilles-tu ?",
            "timestamp": "2026-01-26T14:02:00Z",
        },
        {
            "role": "assistant",
            "content": "Voici mes recommandations :\n\n1. 💸 **Transfert interne** : Envisagez un transfert de 10,000 EUR depuis votre compte d'épargne pour maintenir un coussin de sécurité.\n\n2. 📅 **Paiements à venir** : Vous avez des paiements récurrents prévus :\n   - Loyer : 2,500 EUR (5 février)\n   - Assurance : 450 EUR (6 février)\n   - Services publics : ~400 EUR (10-11 février)\n\n3. 📊 **Revenus attendus** : Salaire de 6,500 EUR prévu le 1er février.\n\nAvec le salaire à venir, votre solde devrait remonter à 21,500 EUR avant les gros paiements.",
            "timestamp": "2026-01-26T14:02:05Z",
            "context_used": {
                "recommendations": [
                    {"type": "internal_transfer", "amount": 10000.00, "from": "Savings Account"},
                    {"type": "upcoming_payments", "total": 3350.00},
                    {"type": "expected_income", "amount": 6500.00, "date": "2026-02-01"},
                ],
            },
        },
        {
            "role": "user",
            "content": "D'accord, je vais faire le transfert. Merci !",
            "timestamp": "2026-01-26T14:05:00Z",
        },
        {
            "role": "assistant",
            "content": "Parfait ! N'hésitez pas à me contacter si vous avez besoin d'aide pour suivre vos finances. Je reste à votre disposition. 😊",
            "timestamp": "2026-01-26T14:05:02Z",
        },
    ],
}

# Sample chat session with complex financial question
MOCK_CHAT_SESSION_COMPLEX_QUERY = {
    "session_id": "sess_complex_004",
    "user_id": "user_test_123",
    "created_at": "2026-01-26T16:00:00Z",
    "updated_at": "2026-01-26T16:10:15Z",
    "context": {
        "total_balance": 728501.92,
        "currency": "EUR",
        "date_range": {"start": "2025-01-01", "end": "2026-01-31"},
        "year_over_year": True,
    },
    "messages": [
        {
            "role": "user",
            "content": "Compare mes finances de janvier 2026 avec janvier 2025",
            "timestamp": "2026-01-26T16:00:00Z",
        },
        {
            "role": "assistant",
            "content": "📊 **Comparaison Janvier 2025 vs Janvier 2026**\n\n**Soldes** :\n- 2025 : 650,000 EUR\n- 2026 : 728,502 EUR\n- Évolution : +78,502 EUR (+12.1%) ✅\n\n**Revenus** :\n- 2025 : 32,000 EUR\n- 2026 : 35,730 EUR\n- Évolution : +3,730 EUR (+11.7%) ✅\n\n**Dépenses** :\n- 2025 : 25,800 EUR\n- 2026 : 28,645 EUR\n- Évolution : +2,845 EUR (+11.0%) ⚠️\n\n**Flux net** :\n- 2025 : +6,200 EUR\n- 2026 : +7,085 EUR\n- Évolution : +885 EUR (+14.3%) ✅\n\n**Points clés** :\n- 📈 Excellente croissance de votre patrimoine (+12%)\n- 💰 Revenus en hausse, notamment paiements clients\n- 💸 Dépenses légèrement plus élevées (achat équipement)\n- ✅ Flux de trésorerie net amélioré",
            "timestamp": "2026-01-26T16:00:08Z",
            "context_used": {
                "year_over_year_comparison": {
                    "2025": {"balance": 650000.00, "income": 32000.00, "expense": 25800.00, "net": 6200.00},
                    "2026": {"balance": 728502.00, "income": 35730.00, "expense": 28645.00, "net": 7085.00},
                },
            },
        },
        {
            "role": "user",
            "content": "Quelle est ma catégorie de dépenses qui a le plus augmenté ?",
            "timestamp": "2026-01-26T16:05:00Z",
        },
        {
            "role": "assistant",
            "content": "🔍 **Catégories en forte hausse** (Jan 2025 → Jan 2026) :\n\n1. **Équipement** : +8,200 EUR (+190%)\n   - 2025 : 4,300 EUR\n   - 2026 : 12,500 EUR\n   - Raison : Achat exceptionnel Dell Business (12,500 EUR)\n\n2. **Fournitures** : +1,850 EUR (+54%)\n   - 2025 : 3,450 EUR\n   - 2026 : 5,300 EUR\n   - Augmentation régulière, cohérente avec croissance activité\n\n3. **Déplacements** : +470 EUR (+67%)\n   - 2025 : 700 EUR\n   - 2026 : 1,170 EUR\n   - Plus de voyages professionnels ce mois\n\n**Verdict** : L'augmentation principale est ponctuelle (équipement). Les autres hausses sont cohérentes avec la croissance de votre activité (+11% de revenus).",
            "timestamp": "2026-01-26T16:05:06Z",
        },
        {
            "role": "user",
            "content": "Merci pour cette analyse détaillée !",
            "timestamp": "2026-01-26T16:10:00Z",
        },
        {
            "role": "assistant",
            "content": "Avec plaisir ! N'hésitez pas si vous avez d'autres questions sur vos finances. 📊",
            "timestamp": "2026-01-26T16:10:01Z",
        },
    ],
}

# Empty chat session (new conversation)
MOCK_CHAT_SESSION_EMPTY = {
    "session_id": "sess_new_005",
    "user_id": "user_test_789",
    "created_at": "2026-01-26T18:00:00Z",
    "updated_at": "2026-01-26T18:00:00Z",
    "context": {},
    "messages": [],
}

# Collection of all mock chat sessions
MOCK_CHAT_SESSIONS = [
    MOCK_CHAT_SESSION_BALANCE_INQUIRY,
    MOCK_CHAT_SESSION_TRANSACTION_ANALYSIS,
    MOCK_CHAT_SESSION_ALERTS,
    MOCK_CHAT_SESSION_COMPLEX_QUERY,
    MOCK_CHAT_SESSION_EMPTY,
]


def get_mock_session_by_id(session_id: str) -> Dict[str, Any]:
    """Get a mock chat session by session ID.
    
    Args:
        session_id: The session ID to retrieve.
    
    Returns:
        Chat session dictionary or None if not found.
    """
    for session in MOCK_CHAT_SESSIONS:
        if session["session_id"] == session_id:
            return session
    return None


def generate_mock_chat_message(
    role: str,
    content: str,
    timestamp: str = None,
) -> Dict[str, Any]:
    """Generate a mock chat message.
    
    Args:
        role: Message role (user/assistant/system).
        content: Message content.
        timestamp: ISO 8601 timestamp (defaults to now).
    
    Returns:
        Chat message dictionary.
    """
    if timestamp is None:
        timestamp = datetime.utcnow().isoformat() + "Z"
    
    return {
        "role": role,
        "content": content,
        "timestamp": timestamp,
    }
