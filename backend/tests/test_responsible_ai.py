import os
from app.services import chatbot as cb


def test_fallback_handles_diverse_names(monkeypatch):
    # Force fallback by unsetting API key
    monkeypatch.setenv("MODEL_API_KEY", "later")

    session_id = cb.create_session()
    diverse_inputs = [
        "Bonjour",  # French greeting
        "John Smith",  # Anglo
        "José García",  # Hispanic
        "Lakshmi Patel",  # Indian
        "Ahmed Hassan",  # Arabic
        "李明",  # Chinese
        "O'Brien",  # Apostrophe
        "José-María",  # Hyphen + accent
        "X Æ A-12",  # Special characters
    ]

    # Directly exercise fallback generator to avoid async complexity
    for text in diverse_inputs:
        out = cb._generate_fallback_response(text, context_data=None)
        assert isinstance(out, str)
        assert len(out) > 0


def test_generate_ai_response_returns_source(monkeypatch):
    # Force fallback path
    monkeypatch.setenv("MODEL_API_KEY", "later")
    session_id = cb.create_session()
    text, source = cb.generate_ai_response("Bonjour", session_id, None)
    assert isinstance(text, str)
    assert source in ("fallback", "azure")


def test_session_pruning(monkeypatch):
    sid_old = cb.create_session()
    sid_new = cb.create_session()

    # Manually age the old session
    sess = cb.get_session(sid_old)
    assert sess is not None
    sess.updated_at = "2000-01-01T00:00:00"

    # Prune and ensure old session is removed
    cb._prune_expired_sessions(max_age_hours=1)
    assert cb.get_session(sid_old) is None or sid_old not in [s.session_id for s in cb.list_active_sessions()]
    assert cb.get_session(sid_new) is not None
