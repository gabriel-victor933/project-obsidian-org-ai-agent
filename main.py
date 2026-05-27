import os
import warnings
import argparse
import json

from config import SYSTEM_PROMPT, MAX_AGENT_ITERATIONS
from tool_executer import tool_executer
from functions import schema_write_whole_file, schema_list_files, schema_get_file_content

from dotenv import load_dotenv
from litellm import completion

load_dotenv()

messages=[{ "role":"system", "content": SYSTEM_PROMPT}]

schema_end_session = {
    "type": "function",
    "function": {
        "name": "end_session",
        "description": "Não executa nada apenas indica o fim da conversa e passa a mensagem final que vai ser printada para o usuario",
        "parameters": {
            "type": "object",
            "properties": {
                "message": {
                    "type": "string",
                    "description": "messagem final que será passada para o usuario",
                }
            },
            "required": ["message"],
        },
    },
}

tools = [
            schema_list_files,
            schema_get_file_content,
            schema_write_whole_file,
            schema_end_session
        ]

def main(user_message, verbose=False):

    messages.append({'role': 'user', 'content': user_message})

    for _ in range(MAX_AGENT_ITERATIONS):

        response = completion(
            model='gemini/gemini-3.5-flash',
            messages=messages,
            tools=tools
        )

        response_message = response.choices[0].message
        
        tool_calls = response_message.tool_calls

        if tool_calls:
            if response_message.content is not None:
                print(response_message.content)
            
            messages.append(dict(response_message))
            for tool_call in tool_calls:
            
                function_name = tool_call.function.name

                arguments = json.loads(tool_call.function.arguments)

                should_stop = False
                if function_name == "end_session":
                    print(arguments.get('message'))
                    result = arguments.get('message')
                    should_stop = True

                else:
                    print(f"- Running tool {function_name}...")
                    result = tool_executer(function_name, arguments)

                messages.append({
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": function_name,
                        "content": result,
                })


                if should_stop:
                    return

        else:
            print(response_message.content)
            break


if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="Obsidian AI Agent",description="obsidian ai agent")

    parser.add_argument('user_message',help='Set verbose mode',default=False)
    parser.add_argument('--verbose',help='Set verbose mode',default=False)

    args = parser.parse_args()
    
    main(args.user_message, args.verbose)
