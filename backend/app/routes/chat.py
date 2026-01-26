"""Chat endpoints for conversational AI assistant."""

from fastapi import APIRouter, HTTPException
from typing import Optional

from ..models.chat import ChatRequest, ChatResponse, ChatSession
from ..services.chatbot import (
    process_chat_message,
    get_session,
    clear_session,
    list_active_sessions,
)

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
        # TODO: Add financial context data from database
        context_data = {}
        
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
