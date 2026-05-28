from functions import get_file_content, write_whole_file, list_files, rename_file, create_dir, move_file

available_tools = {
    'list_files': list_files,
    'get_file_content': get_file_content,
    'write_whole_file': write_whole_file,
    'rename_file': rename_file,
    'create_dir': create_dir,
    'move_file': move_file,
}

def tool_executer(function_name: str, arguments: dict) -> str:
    
    try:
        func = available_tools.get(function_name)

        if func is None:
            return "Error: Tool não definida. Tente novamente"
        
        return func(**arguments)
    
    except Exception as e:
        return f"Error: erro ao executar tool {function_name}: {repr(e)}"
