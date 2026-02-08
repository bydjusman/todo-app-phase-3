import requests
import json

def test_chat_functionality():
    """Test the chat functionality of the server"""
    print("Testing chat functionality...")
    
    # Test data
    user_id = 1
    chat_data = {
        "message": "Hello, can you help me add a task?",
        "token": "fake-token-for-testing"  # This is just for testing purposes
    }
    
    try:
        # Make a request to the chat endpoint
        response = requests.post(
            f'http://localhost:8000/api/chat/{user_id}',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(chat_data)
        )
        
        print(f"Chat endpoint responded with status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("Chat response received successfully!")
            print(f"Response: {data.get('response', 'No response text')}")
            print(f"Tool calls: {data.get('tool_calls', [])}")
            return True
        else:
            print(f"Chat endpoint returned unexpected status: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to chat endpoint: {e}")
        return False

if __name__ == "__main__":
    success = test_chat_functionality()
    if success:
        print("\nChat functionality test PASSED!")
    else:
        print("\nChat functionality test FAILED!")