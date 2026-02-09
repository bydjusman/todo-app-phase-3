import requests
import json

def test_api_endpoints():
    """Test the API endpoints to make sure they're working"""
    print("Testing API endpoints...")

    # Register a test user
    print("Registering a test user...")
    user_data = {
        "username": "testuser2",
        "email": "test2@example.com",
        "password": "testpassword123",
        "confirm_password": "testpassword123"
    }

    register_response = requests.post(
        'http://localhost:8000/api/auth/register',
        headers={'Content-Type': 'application/json'},
        data=json.dumps(user_data)
    )

    if register_response.status_code != 200:
        print(f"Failed to register user: {register_response.status_code} - {register_response.text}")
        return False

    print("User registered successfully!")
    user_info = register_response.json()
    user_id = user_info.get("id")
    print(f"User ID: {user_id}")

    # Login to get the token
    print("Logging in to get token...")
    login_data = {
        "username": "testuser2",
        "password": "testpassword123"
    }

    login_response = requests.post(
        'http://localhost:8000/api/auth/login',
        data=login_data  # Note: login uses form data, not JSON
    )

    if login_response.status_code != 200:
        print(f"Failed to login: {login_response.status_code} - {login_response.text}")
        return False

    login_data_response = login_response.json()
    token = login_data_response.get("access_token")
    
    if not token:
        print("No token received from login")
        return False

    print("Login successful! Got token.")

    # Test the chat functionality with the token
    print("Testing chat functionality...")
    chat_data = {
        "message": "Hello, can you help me add a task?",
        "token": token
    }

    chat_response = requests.post(
        f'http://localhost:8000/api/chat/{user_id}',
        headers={'Content-Type': 'application/json'},
        data=json.dumps(chat_data)
    )

    print(f"Chat endpoint responded with status: {chat_response.status_code}")

    if chat_response.status_code == 200:
        data = chat_response.json()
        print("Chat response received successfully!")
        print(f"Response: {data.get('response', 'No response text')}")
        print(f"Tool calls: {data.get('tool_calls', [])}")
        print(f"Conversation ID: {data.get('conversation_id')}")
        
        # Test another message to list tasks
        print("\nTesting list tasks...")
        list_data = {
            "message": "Can you show me my tasks?",
            "token": token,
            "conversation_id": data.get("conversation_id")  # Use the same conversation
        }

        list_response = requests.post(
            f'http://localhost:8000/api/chat/{user_id}',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(list_data)
        )

        if list_response.status_code == 200:
            list_data_response = list_response.json()
            print("List tasks response received successfully!")
            print(f"Response: {list_data_response.get('response', 'No response text')}")
            return True
        else:
            print(f"List tasks endpoint returned unexpected status: {list_response.status_code}")
            print(f"Response: {list_response.text}")
            return False
    else:
        print(f"Chat endpoint returned unexpected status: {chat_response.status_code}")
        print(f"Response: {chat_response.text}")
        return False

if __name__ == "__main__":
    success = test_api_endpoints()
    if success:
        print("\nAPI endpoints test PASSED!")
    else:
        print("\nAPI endpoints test FAILED!")