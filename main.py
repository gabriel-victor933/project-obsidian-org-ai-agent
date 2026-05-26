import os
import warnings
import argparse

from config import SYSTEM_PROMPT, MAX_AGENT_ITERATIONS
from functions import schema_write_whole_file, schema_list_files, schema_get_file_content

from dotenv import load_dotenv
from litellm import completion

load_dotenv()

messages=[{ "role":"system", "content": SYSTEM_PROMPT}]

tools = [
            schema_list_files,
            schema_get_file_content,
            schema_write_whole_file
        ]


def main(user_message, verbose=False):

    messages.append({'role': 'user', 'content': user_message})

    response = completion(
        model='gemini/gemini-3.5-flash',
        messages=messages,
        tools=tools
    )

    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    if tool_calls:
        print("\nTool Choice:\n", tool_calls)
    else:
        print(response_message.content)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="Obsidian AI Agent",description="obsidian ai agent")

    parser.add_argument('user_message',help='Set verbose mode',default=False)
    parser.add_argument('--verbose',help='Set verbose mode',default=False)

    args = parser.parse_args()
    
    main(args.user_message, args.verbose)
