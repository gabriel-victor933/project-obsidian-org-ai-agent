from litellm import Router
from typing import Any

class LLM_Handler:
    def __init__(self, system_propmt: str, model_list: list[dict], fallbacks: list[dict] = None, tools = None, ):
        self._tools = tools if tools is not None else []

        self._messages = [{ "role":"system", "content": system_propmt}]

        self._router = Router(
            model_list=model_list,
            fallbacks=fallbacks, 
            num_retries=3,
            retry_after=10,
            cooldown_time=360,
            allowed_fails=0,
        )

    def add_message(self, new_message: dict):
        self._messages.append(new_message)

    def add_user_message(self, content: str):
        new_message = {
            'role': 'user', 
            'content': content
        }

        self.add_message(new_message)

    def add_tool_message(self, function_name: str, tool_call_id: str, result: str):
        new_message = {
            "tool_call_id": tool_call_id,
            "role": "tool",
            "name": function_name,
            "content": result,
        }

        self.add_message(new_message)

    def add_tool(self, new_tool: dict):
        # preciso validar o formato dessa nova tool de alguma maneira
        self._tools.append(new_tool)

    def completion(self, model):
        response = self._router.completion(
            model=model,
            messages=self._messages,
            tools=self._tools
        )

        response_message = response.choices[0].message

        return response_message