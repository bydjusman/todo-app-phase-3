import requests
import json
import subprocess
import sys
import os

# Add the parent directory to the path so we can import from the project
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_chat_with_auth():
    """Test the chat functionality with proper authentication"""
    print("Testing chat functionality with authentication...")

    # Start the server in the background
    print("Starting the server...")
    server_process = subprocess.Popen([sys.executable, "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"])
    
    # Wait a moment for the server to start
    import time
    time.sleep(5)

    try:
        # Register a test user first
        print("Registering a test user...")
        user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword123"
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

        # Login to get the token
        print("Logging in to get token...")
        login_data = {
            "username": "testuser",
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

        # Get the user ID from the token response
        user_id = login_data_response.get("user", {}).get("id")
        if not user_id:
            print("No user ID found in login response")
            return False

        print(f"User ID: {user_id}")

        # Now test the chat functionality with the token
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

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to server: {e}")
        return False
    finally:
        # Terminate the server process
        print("Stopping the server...")
        server_process.terminate()
        server_process.wait()

if __name__ == "__main__":
    success = test_chat_with_auth()
    if success:
        print("\nChat functionality test with authentication PASSED!")
    else:
        print("\nChat functionality test with authentication FAILED!")