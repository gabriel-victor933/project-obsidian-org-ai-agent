import os

from utils.decorators import error_to_string_handler, validate_tools_params

@error_to_string_handler
@validate_tools_params
def rename_file(working_dir: str, file_path: str, new_name: str):

    abs_working_dir = os.path.abspath(working_dir)
    full_path = os.path.join(abs_working_dir, file_path)

    if not os.path.exists(full_path):
        return "ERROR: Cannot rename — no file or directory found at: " + full_path
    
    if not os.path.isfile(full_path):
        return "ERROR: Cannot rename — the path exists but is not a file: " + full_path

    old_name = os.path.basename(file_path)

    new_full_path = os.path.join(os.path.dirname(full_path),new_name)

    os.rename(full_path, new_full_path)
    
    return f"File sucessfully rename from '{old_name}' to '{new_name}'"

schema_rename_file = {
    "type": "function",
    "function": {
        "name": "rename_file",
        "description": "Renomeia um arquivo",
        "parameters": {
            "type": "object",
            "properties": {
                "working_dir": {
                    "type": "string",
                    "description": "Pasta base onde todos os arquivos estão armazenados",
                },
                "file_path": {
                    "type": "string", 
                    "description": "path do arquivo a partir do working_dir"
                },
                "new_name": {
                    "type": "string", 
                    "description": "Novo nome do arquivo"
                },
            },
            "required": ["working_dir","file_path","new_name"],
        },
    },
}

if __name__ == "__main__":
    result1 = rename_file('obsidian','teste',"arquivo2.md")
    result2 = rename_file('obsidian','teste/arquivo131.md',"arquivo2.md")
    result3 = rename_file('obsidian','teste/arquivo3.md',"arquivo3.md")

    print(result1)
    print(result2)
    print(result3)

