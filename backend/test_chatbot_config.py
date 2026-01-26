"""Test script for Azure OpenAI chatbot configuration."""

import os
import sys
from pathlib import Path

# Add backend to path
backend_path = Path(__file__).parent
sys.path.insert(0, str(backend_path))

from dotenv import load_dotenv
from app.services.chatbot import (
    create_session,
    process_chat_message,
    _get_azure_client,
)
from app.models.chat import ChatRequest

# Load environment variables
load_dotenv()


def test_environment_variables():
    """Test that environment variables are properly configured."""
    print("=== Testing Environment Variables ===")
    
    required_vars = [
        "MODEL_NAME",
        "MODEL_URL",
        "MODEL_API_KEY",
        "MODEL_API_VERSION",
        "MODEL_API_TYPE",
        "MODEL_TEMPERATURE",
    ]
    
    all_present = True
    for var in required_vars:
        value = os.getenv(var)
        if value:
            # Mask API key for security
            if var == "MODEL_API_KEY":
                masked = value[:4] + "..." + value[-4:] if len(value) > 8 else "***"
                print(f"✓ {var}: {masked}")
            else:
                print(f"✓ {var}: {value}")
        else:
            print(f"✗ {var}: NOT SET")
            all_present = False
    
    return all_present


def test_azure_client():
    """Test Azure OpenAI client initialization."""
    print("\n=== Testing Azure OpenAI Client ===")
    
    api_key = os.getenv("MODEL_API_KEY")
    if api_key == "later" or not api_key:
        print("⚠ API key not configured - will use fallback mode")
        return False
    
    try:
        client = _get_azure_client()
        if client:
            print("✓ Azure OpenAI client initialized successfully")
            return True
        else:
            print("✗ Failed to initialize Azure OpenAI client")
            return False
    except Exception as e:
        print(f"✗ Error initializing client: {e}")
        return False


async def test_chatbot_session():
    """Test chatbot session creation and message processing."""
    print("\n=== Testing Chatbot Session ===")
    
    try:
        # Create session
        session_id = create_session()
        print(f"✓ Session created: {session_id}")
        
        # Test message
        request = ChatRequest(
            message="Bonjour, peux-tu m'aider avec mes finances ?",
            session_id=session_id,
        )
        
        print(f"→ Sending message: {request.message}")
        
        # Process message
        response = await process_chat_message(request, context_data={
            "total_balance": 15234.50,
            "currency": "EUR",
            "accounts": [{"id": "1", "name": "Compte Courant"}],
            "recent_transactions": [{"id": "t1", "amount": -50.0}],
        })
        
        print(f"✓ Response received:")
        print(f"  Session ID: {response.session_id}")
        print(f"  Message ID: {response.message.id}")
        print(f"  Content: {response.message.content}")
        print(f"  Suggestions: {response.suggestions}")
        
        return True
        
    except Exception as e:
        print(f"✗ Error testing chatbot: {e}")
        import traceback
        traceback.print_exc()
        return False


async def main():
    """Run all tests."""
    print("=" * 60)
    print("Azure OpenAI Chatbot Configuration Test")
    print("=" * 60)
    
    # Test environment
    env_ok = test_environment_variables()
    
    # Test Azure client
    client_ok = test_azure_client()
    
    # Test chatbot
    chatbot_ok = await test_chatbot_session()
    
    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    print(f"Environment Variables: {'✓ PASS' if env_ok else '✗ FAIL'}")
    print(f"Azure OpenAI Client: {'✓ PASS' if client_ok else '⚠ FALLBACK MODE'}")
    print(f"Chatbot Session: {'✓ PASS' if chatbot_ok else '✗ FAIL'}")
    
    if not client_ok:
        print("\n⚠ Note: Chatbot is running in fallback mode with rule-based responses.")
        print("  Configure MODEL_API_KEY in .env to enable Azure OpenAI.")
    
    print("=" * 60)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
