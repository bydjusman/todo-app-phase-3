"""
Google AI Agent Integration for Todo Chatbot
This module integrates Google's Generative AI with the MCP tools
"""
import os
import json
from typing import Dict, Any, List
from ..database.session import get_session
from ..config import chat_model


class GoogleAIAgentService:
    """
    Service class to handle Google AI Agent interactions and MCP tool integration.
    """

    def __init__(self):
        # The model is already initialized in config
        self.model = chat_model

    def process_message(self, user_message: str, user_id: int, conversation_history: List[Dict[str, str]] = None) -> tuple[str, List[Dict[str, Any]]]:
        """
        Process a user message and return response with tool calls.
        """
        # Prepare the conversation history for the model
        formatted_history = []
        
        if conversation_history:
            for entry in conversation_history:
                role = "user" if entry["role"] == "user" else "model"
                formatted_history.append({
                    "role": role,
                    "parts": [{"text": entry["content"]}]
                })
        
        # Add the current user message
        formatted_history.append({
            "role": "user",
            "parts": [{"text": user_message}]
        })

        # Create a prompt that guides the model to recognize intents and call tools
        prompt = f"""
        You are a helpful assistant for managing todo tasks. The current user ID is {user_id}.
        Based on the user's message, determine if they want to perform any of the following actions:
        
        1. Add a task: if user wants to create/add a new task
        2. List tasks: if user wants to see their tasks
        3. Update a task: if user wants to modify an existing task
        4. Complete a task: if user wants to mark a task as done
        5. Delete a task: if user wants to remove a task
        
        Respond in the following JSON format:
        {{
          "response": "Your friendly response to the user",
          "tool_calls": [
            {{
              "name": "add_task|list_tasks|update_task|complete_task|delete_task",
              "arguments": {{
                "user_id": {user_id},
                "title": "task title for add/update",
                "task_id": task_id for update/complete/delete,
                "status": "filter for list_tasks (pending/completed/all)"
              }}
            }}
          ]
        }}
        
        Only include tool_calls in the response if the user intends to perform one of the actions.
        If you can't determine a specific action, just respond to the user without tool calls.
        
        User message: {user_message}
        """

        # Generate content using the model
        response = self.model.generate_content(prompt)
        
        # Extract the text response
        text_response = response.text.strip()
        
        # Try to parse the JSON response to extract tool calls
        tool_calls = []
        
        # Look for JSON in the response
        try:
            # Attempt to extract JSON from the response
            start_idx = text_response.find('{')
            end_idx = text_response.rfind('}') + 1
            
            if start_idx != -1 and end_idx != 0:
                json_str = text_response[start_idx:end_idx]
                parsed_response = json.loads(json_str)
                
                # Extract the actual response text (before or after JSON)
                response_text = parsed_response.get("response", "I processed your request.")
                tool_calls = parsed_response.get("tool_calls", [])
                
                # If response_text contains JSON-like structure, clean it up
                if isinstance(response_text, dict):
                    response_text = str(response_text)
            else:
                response_text = text_response
        except json.JSONDecodeError:
            # If JSON parsing fails, return the raw response without tool calls
            response_text = text_response
        
        return response_text, tool_calls

    def execute_tool_call(self, function_name: str, function_args: Dict[str, Any]) -> Any:
        """
        Execute a tool call locally.
        """
        # Import here to avoid circular import
        from .agent_service import TodoAgentService
        from ..database.session import Session, engine
        
        # Create a session directly using the engine
        with Session(engine) as session:
            agent_service = TodoAgentService(session)

            # Map function names to actual tool calls
            if function_name == "add_task":
                return agent_service.tools["add_task"].run(session=session, **function_args)
            elif function_name == "list_tasks":
                return agent_service.tools["list_tasks"].run(session=session, **function_args)
            elif function_name == "complete_task":
                return agent_service.tools["complete_task"].run(session=session, **function_args)
            elif function_name == "delete_task":
                return agent_service.tools["delete_task"].run(session=session, **function_args)
            elif function_name == "update_task":
                return agent_service.tools["update_task"].run(session=session, **function_args)
            else:
                return {"error": f"Unknown function: {function_name}"}

    def execute_tool_call_with_session(self, function_name: str, function_args: Dict[str, Any], db_session) -> Any:
        """
        Execute a tool call using an existing session.
        """
        # Import here to avoid circular import
        from .agent_service import TodoAgentService
        
        # Use the provided session
        agent_service = TodoAgentService(db_session)

        # Map function names to actual tool calls
        if function_name == "add_task":
            return agent_service.tools["add_task"].run(session=db_session, **function_args)
        elif function_name == "list_tasks":
            return agent_service.tools["list_tasks"].run(session=db_session, **function_args)
        elif function_name == "complete_task":
            return agent_service.tools["complete_task"].run(session=db_session, **function_args)
        elif function_name == "delete_task":
            return agent_service.tools["delete_task"].run(session=db_session, **function_args)
        elif function_name == "update_task":
            return agent_service.tools["update_task"].run(session=db_session, **function_args)
        else:
            return {"error": f"Unknown function: {function_name}"}


# Singleton instance
google_ai_agent_service = GoogleAIAgentService()