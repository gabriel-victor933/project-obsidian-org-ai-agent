import os
import warnings
import argparse
import json
import logging
from datetime import datetime 
import random
import sys

from config import SYSTEM_PROMPT, MAX_AGENT_ITERATIONS
from tool_executer import tool_executer
from tools import tools
from utils import AgentCustomLogger, LLM_Handler

from dotenv import load_dotenv
import litellm

load_dotenv()

model_list = [
    {
        'model_name': 'gemini-3.5-flash',
        'litellm_params': {
            'model': 'gemini/gemini-3.5-flash',
            'api_key': os.getenv('GEMINI_API_KEY'),
            'order': 1
        }
    },
    {
        'model_name': 'gemini-3.1-flash-lite',
        'litellm_params': {
            'model': 'gemini/gemini-3.1-flash-lite',
            'api_key': os.getenv('GEMINI_API_KEY'),
            'order': 2
        }
    },
    {
        'model_name': 'gemini-2.5-flash',
        'litellm_params': {
            'model': 'gemini/gemini-2.5-flash',
            'api_key': os.getenv('GEMINI_API_KEY'),
            'order': 3
        }
    },
]

fallbacks = [{"gemini-3.5-flash": ["gemini-3.1-flash-lite", "gemini-2.5-flash"]}]

## Custom callback para print e/ou salvar logs
customHandler = AgentCustomLogger('obsidian_agent_logger')
litellm.callbacks = [customHandler]

def main(user_message, verbose=False):
    
    llm_handler = LLM_Handler(
        SYSTEM_PROMPT, 
        model_list,
        fallbacks,
        tools
    )

    llm_handler.add_user_message(user_message)
    try:
        for _ in range(MAX_AGENT_ITERATIONS):

            response_message = llm_handler.completion('gemini-3.5-flash')
            
            tool_calls = response_message.tool_calls

            if tool_calls:
                if response_message.content is not None:
                    print(response_message.content)
                
                llm_handler.add_message(dict(response_message))
                for tool_call in tool_calls:
                
                    function_name = tool_call.function.name

                    arguments = json.loads(tool_call.function.arguments)

                    should_stop = False
                    if function_name == "end_session":
                        print(arguments.get('message'))
                        result = arguments.get('message')
                        should_stop = True

                    else:
                        print(f"- Running tool {function_name} with args: {arguments}")
                        result = tool_executer(function_name, arguments)

                    llm_handler.add_tool_message(function_name, tool_call.id, result)

                    if should_stop:
                        return

            else:
                print(response_message.content)
                break
    except Exception as e:
        print(f"\nErro geral no agente! por favor tente novamente mais tarde...\n")
        sys.exit(0)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="Obsidian AI Agent",description="obsidian ai agent")

    parser.add_argument('user_message',help='Set verbose mode',default=False)
    parser.add_argument('--verbose',help='Set verbose mode',default=False)

    args = parser.parse_args()
    
    main(args.user_message, args.verbose)
