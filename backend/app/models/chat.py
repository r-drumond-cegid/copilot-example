"""Chat and conversation data models."""

from datetime import datetime
from typing import Optional, Literal

from pydantic import BaseModel, Field


class ChatMessage(BaseModel):
    """Individual chat message in a conversation."""

    id: str = Field(..., description="Unique message identifier")
    session_id: str = Field(..., description="Session identifier for conversation grouping")
    role: Literal["user", "assistant", "system"] = Field(..., description="Message sender role")
    content: str = Field(..., description="Message text content")
    timestamp: str = Field(..., description="Message timestamp (ISO 8601)")
    metadata: dict = Field(default_factory=dict, description="Additional message metadata")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "msg_12345",
                "session_id": "sess_abc123",
                "role": "user",
                "content": "Quel est mon solde total ?",
                "timestamp": "2026-01-26T10:30:00Z",
                "metadata": {},
            }
        }


class ChatSession(BaseModel):
    """Chat conversation session."""

    session_id: str = Field(..., description="Unique session identifier")
    created_at: str = Field(..., description="Session creation timestamp (ISO 8601)")
    updated_at: str = Field(..., description="Last update timestamp (ISO 8601)")
    messages: list[ChatMessage] = Field(default_factory=list, description="Conversation messages")
    context: dict = Field(default_factory=dict, description="Session context data")
    is_active: bool = Field(default=True, description="Session active status")

    class Config:
        json_schema_extra = {
            "example": {
                "session_id": "sess_abc123",
                "created_at": "2026-01-26T10:25:00Z",
                "updated_at": "2026-01-26T10:30:00Z",
                "messages": [],
                "context": {"user_preferences": {}},
                "is_active": True,
            }
        }


class ChatRequest(BaseModel):
    """Request to send a chat message."""

    message: str = Field(..., description="User message content", min_length=1)
    session_id: Optional[str] = Field(None, description="Existing session ID (creates new if None)")

    class Config:
        json_schema_extra = {
            "example": {
                "message": "Quelles sont mes transactions les plus importantes ce mois ?",
                "session_id": "sess_abc123",
            }
        }


class ChatResponse(BaseModel):
    """Response from chatbot."""

    session_id: str = Field(..., description="Session identifier")
    message: ChatMessage = Field(..., description="Assistant response message")
    suggestions: list[str] = Field(default_factory=list, description="Suggested follow-up questions")

    class Config:
        json_schema_extra = {
            "example": {
                "session_id": "sess_abc123",
                "message": {
                    "id": "msg_67890",
                    "session_id": "sess_abc123",
                    "role": "assistant",
                    "content": "Votre solde total est de 850 000,50 EUR.",
                    "timestamp": "2026-01-26T10:30:05Z",
                    "metadata": {},
                },
                "suggestions": [
                    "Quelles sont mes dépenses récentes ?",
                    "Affiche-moi un graphique de mon solde",
                ],
            }
        }
