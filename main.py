import os
import warnings
import argparse

from config import SYSTEM_PROMPT

from dotenv import load_dotenv
from litellm import completion

load_dotenv()

messages=[{ "role":"system", "content": SYSTEM_PROMPT}]

tools = [
            {
                "type": "function",
                "function": {
                    "name": "get_file_content",
                    "description": "Obtem o conteudo de um arquivo em formato de texto",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "workdir": {
                                "type": "string",
                                "description": "Pasta base onde todos os arquivos estão armazenados",
                            },
                            "path": {
                                "type": "string", 
                                "description": "path do arquivo dentro de workdir"
                            },
                        },
                        "required": ["workdir","path"],
                    },
                },
            },
        ]


def main(user_message, verbose=False):

    messages.append({'role': 'user', 'content': user_message})

    response = completion(
        model='gemini/gemini-3.5-flash',
        messages=messages,
        tools=tools
    )

    print(response)

    response_message = response.choices[0].message

    print("\n\n",response_message,"\n\n")

    tool_calls = response_message.tool_calls

    print("\n\n",tool_calls,"\n\n")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="Obsidian AI Agent",description="obsidian ai agent")

    parser.add_argument('user_message',help='Set verbose mode',default=False)
    parser.add_argument('--verbose',help='Set verbose mode',default=False)

    args = parser.parse_args()
    
    main(args.user_message, args.verbose)
