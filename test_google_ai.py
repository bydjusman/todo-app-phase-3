import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from backend.app.core.google_ai_agent import google_ai_agent_service

def test_google_ai():
    """Test the Google AI integration"""
    print("Testing Google AI Integration...")
    
    # Test message
    user_message = "Hello, can you help me manage my tasks?"
    user_id = 1
    
    try:
        response_text, tool_calls = google_ai_agent_service.process_message(user_message, user_id)
        print(f"Response: {response_text}")
        print(f"Tool calls: {tool_calls}")
        print("Google AI integration is working!")
        return True
    except Exception as e:
        print(f"Error testing Google AI: {e}")
        return False

if __name__ == "__main__":
    test_google_ai()