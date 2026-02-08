import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from backend.app.core.google_ai_agent import google_ai_agent_service

def test_chatbot_intent():
    """Test if the chatbot recognizes task addition intent"""
    print("Testing chatbot intent recognition...")
    
    # Test message to add a task
    user_message = "Please add a task to buy groceries"
    user_id = 1
    
    try:
        response_text, tool_calls = google_ai_agent_service.process_message(user_message, user_id)
        print(f"Input message: {user_message}")
        print(f"Response: {response_text}")
        print(f"Tool calls: {tool_calls}")
        
        if tool_calls:
            print("✅ Tool calls detected - chatbot recognized intent!")
            for call in tool_calls:
                print(f"  - Calling tool: {call['name']}")
                print(f"  - Arguments: {call['arguments']}")
        else:
            print("❌ No tool calls detected - chatbot did not recognize intent")
        
        return True
    except Exception as e:
        print(f"Error testing chatbot intent: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_chatbot_list_tasks():
    """Test if the chatbot recognizes task listing intent"""
    print("\nTesting chatbot list tasks intent...")
    
    # Test message to list tasks
    user_message = "Show me my tasks"
    user_id = 1
    
    try:
        response_text, tool_calls = google_ai_agent_service.process_message(user_message, user_id)
        print(f"Input message: {user_message}")
        print(f"Response: {response_text}")
        print(f"Tool calls: {tool_calls}")
        
        if tool_calls:
            print("✅ Tool calls detected - chatbot recognized intent!")
            for call in tool_calls:
                print(f"  - Calling tool: {call['name']}")
                print(f"  - Arguments: {call['arguments']}")
        else:
            print("❌ No tool calls detected - chatbot did not recognize intent")
        
        return True
    except Exception as e:
        print(f"Error testing chatbot intent: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_chatbot_intent()
    test_chatbot_list_tasks()