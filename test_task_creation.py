import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from backend.app.database.session import get_session
from backend.app.core.task_service import TaskService
from backend.app.models.task import TaskStatus


def test_task_creation_directly():
    """Test task creation directly using TaskService"""
    print("Testing task creation directly...")
    
    # Get a session
    session_gen = get_session()
    session = next(session_gen)
    
    try:
        # Create a task directly using TaskService
        task_data = {
            'title': 'Test task from direct call',
            'description': 'This is a test task created directly',
            'status': 'pending'
        }
        
        task = TaskService.create_task(
            db_session=session,
            user_id=3,  # Using the test user ID
            task_data=task_data
        )
        
        print(f"Task created successfully: {task.title}")
        print(f"Task ID: {task.id}")
        print(f"User ID: {task.user_id}")
        
        # Commit the session
        session.commit()
        
        # Verify the task exists by querying it
        from sqlmodel import select
        stmt = select(type(task)).where(type(task).id == task.id)
        retrieved_task = session.exec(stmt).first()
        
        if retrieved_task:
            print(f"Task verified in database: {retrieved_task.title}")
            return True
        else:
            print("ERROR: Task not found in database after creation")
            return False
            
    except Exception as e:
        print(f"Error creating task: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        session.close()


def test_tool_execution():
    """Test executing the add_task tool directly"""
    print("\nTesting add_task tool execution...")
    
    # Get a session
    session_gen = get_session()
    session = next(session_gen)
    
    try:
        # Import the tool
        from backend.app.tools.add_task import AddTaskTool
        
        # Create an instance of the tool
        tool = AddTaskTool()
        
        # Prepare tool arguments
        tool_args = {
            'user_id': 3,
            'title': 'Test task from tool execution',
            'description': 'This is a test task created via tool'
        }
        
        # Run the tool
        import asyncio
        result = asyncio.run(tool.run(session=session, **tool_args))
        
        print(f"Tool execution result: {result}")
        
        if result.get('success'):
            print("Tool execution was successful")
            # Commit the session
            session.commit()
            return True
        else:
            print(f"Tool execution failed: {result.get('error')}")
            return False
            
    except Exception as e:
        print(f"Error executing tool: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        session.close()


if __name__ == "__main__":
    success1 = test_task_creation_directly()
    success2 = test_tool_execution()
    
    if success1 and success2:
        print("\n✅ Both direct task creation and tool execution are working!")
    else:
        print("\n❌ There are issues with task creation or tool execution")