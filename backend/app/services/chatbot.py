"""Chatbot service using Azure OpenAI for financial assistance."""

import os
import uuid
from datetime import datetime
from typing import Optional
from openai import AzureOpenAI
from dotenv import load_dotenv

from ..models.chat import ChatMessage, ChatSession, ChatRequest, ChatResponse

# Load environment variables
load_dotenv()

# Initialize Azure OpenAI client
_azure_client = None

def _get_azure_client() -> AzureOpenAI:
    """Get or create Azure OpenAI client."""
    global _azure_client
    if _azure_client is None:
        api_key = os.getenv("MODEL_API_KEY")
        api_version = os.getenv("MODEL_API_VERSION", "2024-12-01-preview")
        azure_endpoint = os.getenv("MODEL_URL")
        
        if not api_key or api_key == "later":
            # Return None if API key not configured yet
            return None
        
        _azure_client = AzureOpenAI(
            api_key=api_key,
            api_version=api_version,
            azure_endpoint=azure_endpoint,
        )
    return _azure_client


# In-memory session storage (will be replaced with database later)
_sessions: dict[str, ChatSession] = {}


def create_session() -> str:
    """Create a new chat session."""
    session_id = f"sess_{uuid.uuid4().hex[:12]}"
    now = datetime.now().isoformat()
    
    _sessions[session_id] = ChatSession(
        session_id=session_id,
        created_at=now,
        updated_at=now,
        messages=[],
        context={},
        is_active=True,
    )
    
    return session_id


def get_session(session_id: str) -> Optional[ChatSession]:
    """Retrieve a chat session by ID."""
    return _sessions.get(session_id)


def add_message(session_id: str, role: str, content: str) -> ChatMessage:
    """Add a message to a session."""
    session = _sessions.get(session_id)
    if not session:
        raise ValueError(f"Session {session_id} not found")
    
    message = ChatMessage(
        id=f"msg_{uuid.uuid4().hex[:8]}",
        session_id=session_id,
        role=role,
        content=content,
        timestamp=datetime.now().isoformat(),
        metadata={},
    )
    
    session.messages.append(message)
    session.updated_at = datetime.now().isoformat()
    
    return message


def generate_ai_response(
    user_message: str,
    session_id: str,
    context_data: Optional[dict] = None
) -> str:
    """
    Generate AI response using Azure OpenAI.
    
    Args:
        user_message: User's message
        session_id: Current session ID
        context_data: Optional financial context (accounts, transactions)
        
    Returns:
        AI-generated response text
    """
    session = get_session(session_id)
    if not session:
        return "Erreur: Session invalide."
    
    # Get Azure OpenAI client
    client = _get_azure_client()
    
    # If client not configured, use fallback rule-based responses
    if client is None:
        return _generate_fallback_response(user_message, context_data)
    
    try:
        # Build system prompt with financial context
        system_prompt = _build_system_prompt(context_data)
        
        # Build conversation history
        messages = [{"role": "system", "content": system_prompt}]
        
        # Add recent conversation history (last 10 messages)
        for msg in session.messages[-10:]:
            messages.append({
                "role": msg.role,
                "content": msg.content
            })
        
        # Add current user message
        messages.append({
            "role": "user",
            "content": user_message
        })
        
        # Call Azure OpenAI
        model_name = os.getenv("MODEL_NAME", "gpt41")
        temperature = float(os.getenv("MODEL_TEMPERATURE", "0.1"))
        
        response = client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=temperature,
            max_tokens=1000,
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        print(f"Error calling Azure OpenAI: {e}")
        return _generate_fallback_response(user_message, context_data)


def _build_system_prompt(context_data: Optional[dict] = None) -> str:
    """Build system prompt with financial context."""
    base_prompt = """Vous êtes un assistant financier IA expert qui aide les utilisateurs à comprendre et gérer leurs finances personnelles.

Vos responsabilités incluent :
- Analyser les soldes de comptes et les transactions
- Fournir des insights sur les habitudes de dépenses
- Générer des rapports financiers clairs
- Détecter des tendances et anomalies
- Donner des conseils financiers personnalisés

Répondez toujours en français de manière claire, professionnelle et empathique."""
    
    if context_data:
        context_prompt = "\n\nContexte financier actuel :"
        
        if "total_balance" in context_data:
            total = context_data["total_balance"]
            currency = context_data.get("currency", "EUR")
            context_prompt += f"\n- Solde total : {total:,.2f} {currency}"
        
        if "recent_transactions" in context_data:
            count = len(context_data["recent_transactions"])
            context_prompt += f"\n- Nombre de transactions récentes : {count}"
        
        if "accounts" in context_data:
            count = len(context_data["accounts"])
            context_prompt += f"\n- Nombre de comptes : {count}"
        
        return base_prompt + context_prompt
    
    return base_prompt


def _generate_fallback_response(user_message: str, context_data: Optional[dict] = None) -> str:
    """Generate fallback rule-based response when Azure OpenAI is unavailable."""
    message_lower = user_message.lower()
    
    if "solde" in message_lower or "balance" in message_lower:
        if context_data and "total_balance" in context_data:
            total = context_data["total_balance"]
            currency = context_data.get("currency", "EUR")
            return f"Votre solde total actuel est de {total:,.2f} {currency}."
        return "Pour consulter votre solde, j'ai besoin d'accéder à vos données de compte."
    
    elif "transaction" in message_lower or "dépense" in message_lower:
        if context_data and "recent_transactions" in context_data:
            count = len(context_data["recent_transactions"])
            return f"Vous avez {count} transactions récentes. Souhaitez-vous voir les détails ?"
        return "Je peux vous aider à analyser vos transactions. Quelle période vous intéresse ?"
    
    elif "bonjour" in message_lower or "hello" in message_lower or "salut" in message_lower:
        return "Bonjour ! Je suis votre assistant financier. Comment puis-je vous aider aujourd'hui ?"
    
    elif "aide" in message_lower or "help" in message_lower:
        return ("Je peux vous aider avec :\n"
                "- Consulter vos soldes de compte\n"
                "- Analyser vos transactions\n"
                "- Générer des rapports financiers\n"
                "- Détecter des tendances de dépenses\n"
                "Que souhaitez-vous faire ?")
    
    else:
        return ("Je suis votre assistant financier IA. Je peux vous aider à comprendre vos finances. "
                "Posez-moi des questions sur vos soldes, transactions, ou demandez une analyse.")


def get_conversation_suggestions(session: ChatSession) -> list[str]:
    """Generate suggested follow-up questions based on conversation."""
    # Default suggestions
    suggestions = [
        "Quel est mon solde total ?",
        "Montre-moi mes dernières transactions",
        "Génère un rapport mensuel",
    ]
    
    # Context-aware suggestions based on last message
    if session.messages:
        last_message = session.messages[-1].content.lower()
        
        if "solde" in last_message:
            suggestions = [
                "Quelles sont mes dépenses ce mois ?",
                "Y a-t-il des alertes sur mes comptes ?",
                "Affiche un graphique de l'évolution",
            ]
        elif "transaction" in last_message:
            suggestions = [
                "Catégorise ces transactions",
                "Quelle est ma plus grosse dépense ?",
                "Analyse mes habitudes de dépense",
            ]
    
    return suggestions


async def process_chat_message(request: ChatRequest, context_data: Optional[dict] = None) -> ChatResponse:
    """
    Process a chat message and return AI response.
    
    Args:
        request: Chat request with message and optional session_id
        context_data: Optional financial context data
        
    Returns:
        ChatResponse with assistant message and suggestions
    """
    # Create or retrieve session
    if request.session_id:
        session = get_session(request.session_id)
        if not session:
            raise ValueError(f"Session {request.session_id} not found")
        session_id = request.session_id
    else:
        session_id = create_session()
        session = get_session(session_id)
    
    # Add user message
    add_message(session_id, "user", request.message)
    
    # Generate AI response
    ai_response_text = generate_ai_response(request.message, session_id, context_data)
    
    # Add assistant message
    assistant_message = add_message(session_id, "assistant", ai_response_text)
    
    # Get suggestions
    suggestions = get_conversation_suggestions(session)
    
    return ChatResponse(
        session_id=session_id,
        message=assistant_message,
        suggestions=suggestions,
    )


def clear_session(session_id: str) -> bool:
    """Delete a chat session."""
    if session_id in _sessions:
        del _sessions[session_id]
        return True
    return False


def list_active_sessions() -> list[ChatSession]:
    """List all active chat sessions."""
    return [s for s in _sessions.values() if s.is_active]
