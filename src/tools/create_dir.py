import os
from utils.decorators import error_to_string_handler, validate_tools_params

@error_to_string_handler
@validate_tools_params
def create_dir(working_dir: str, dir_path: str):

    abs_working_dir = os.path.abspath(working_dir)
    dir_full_path = os.path.join(abs_working_dir, dir_path)
    
    if os.path.isfile(dir_full_path):
        return "ERROR: Cannot create directory — a file with the same name already exists at: " + dir_full_path

    if os.path.exists(dir_full_path):
        return f"Dir {dir_full_path} already exist!!"

    if not os.path.isdir(dir_full_path):
        os.makedirs(dir_full_path, exist_ok=True)
    
    return f"Dir {dir_full_path} created with sucess!!"

schema_create_dir = {
    "type": "function",
    "function": {
        "name": "create_dir",
        "description": "Cria uma nova pasta vazia. Função pode criar variaveis pastas aninhadas de uma só vez.",
        "parameters": {
            "type": "object",
            "properties": {
                "working_dir": {
                    "type": "string",
                    "description": "Pasta base onde todos os arquivos estão armazenados",
                },
                "dir_path": {
                    "type": "string", 
                    "description": "path do pasta a ser criada a partir do working_dir"
                }
            },
            "required": ["working_dir","dir_path"],
        },
    },
}

if __name__ == "__main__":
    result1 = create_dir('obsidian','teste/teste-write-archive/teste')
    result2 = create_dir('obsidian','teste/teste4/teste5/teste6/teste7/teste8')

    print(result1)
    print(result2)

