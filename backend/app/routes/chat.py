"""Chat endpoints for conversational AI assistant."""

from fastapi import APIRouter, HTTPException
from typing import Optional
from datetime import datetime, timedelta

from ..models.chat import ChatRequest, ChatResponse, ChatSession
from ..services.chatbot import (
    process_chat_message,
    get_session,
    clear_session,
    list_active_sessions,
)
from ..routes.accounts import get_account_balances
from ..routes.transactions import get_transactions
from ..services.analytics import calculate_balance_summary

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def send_chat_message(request: ChatRequest):
    """
    Send a message to the chatbot and receive an AI response.
    
    Args:
        request: Chat request with message and optional session_id
        
    Returns:
        ChatResponse with AI assistant message and suggestions
    """
    try:
        # Fetch financial data for chatbot context
        current_date = datetime.now()
        current_date_str = current_date.strftime("%Y-%m-%d")
        
        # Get account balances for current date
        accounts = await get_account_balances(date=current_date_str)
        
        # Calculate balance summary from accounts
        balance_summary = calculate_balance_summary(accounts, current_date_str)
        
        # Get recent transactions (last 30 days)
        from_date = (current_date - timedelta(days=30)).strftime("%Y-%m-%d")
        to_date = current_date.strftime("%Y-%m-%d")
        all_transactions = await get_transactions(
            from_date=from_date,
            to_date=to_date
        )
        
        # Build context data for chatbot
        context_data = {
            "total_balance": balance_summary.total_balance,
            "currency": balance_summary.currency,
            "account_count": balance_summary.account_count,
            "accounts": [acc.dict() for acc in accounts],
            "recent_transactions": [trans.dict() for trans in all_transactions[-10:]],
        }
        
        response = await process_chat_message(request, context_data)
        return response
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors du traitement: {str(e)}")


@router.get("/chat/history/{session_id}", response_model=ChatSession)
async def get_chat_history(session_id: str):
    """
    Retrieve conversation history for a session.
    
    Args:
        session_id: Session identifier
        
    Returns:
        ChatSession with full message history
    """
    session = get_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail=f"Session {session_id} introuvable")
    
    return session


@router.delete("/chat/{session_id}")
async def delete_chat_session(session_id: str):
    """
    Delete a chat session and its history.
    
    Args:
        session_id: Session identifier
        
    Returns:
        Success message
    """
    success = clear_session(session_id)
    if not success:
        raise HTTPException(status_code=404, detail=f"Session {session_id} introuvable")
    
    return {"message": f"Session {session_id} supprimée avec succès"}


@router.get("/chat/sessions", response_model=list[ChatSession])
async def list_sessions():
    """
    List all active chat sessions.
    
    Returns:
        List of active ChatSession objects
    """
    sessions = list_active_sessions()
    return sessions
