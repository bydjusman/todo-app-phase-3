import subprocess
import time
import requests
import signal
import os

def test_server_startup():
    """Test that the server starts properly"""
    print("Starting server for testing...")
    
    # Start the server in a subprocess
    process = subprocess.Popen(['python', 'backend/start_server.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Give the server some time to start
    time.sleep(5)
    
    try:
        # Try to make a request to the server
        response = requests.get('http://localhost:8000/', timeout=10)
        print(f"Server responded with status: {response.status_code}")
        
        if response.status_code == 200:
            print("Server is running and responding correctly!")
            data = response.json()
            print(f"Server info: {data}")
            return True
        else:
            print(f"Server returned unexpected status: {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to server: {e}")
        return False
    finally:
        # Terminate the server process
        try:
            process.terminate()
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()

if __name__ == "__main__":
    success = test_server_startup()
    if success:
        print("\nServer startup test PASSED!")
    else:
        print("\nServer startup test FAILED!")