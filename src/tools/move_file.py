import os
import shutil
from utils.decorators import error_to_string_handler, validate_tools_params

@error_to_string_handler
@validate_tools_params
def move_file(working_dir: str, file_path: str, destination_path: str):

    abs_working_dir = os.path.abspath(working_dir)

    full_path = os.path.join(abs_working_dir, file_path)
    file_name = os.path.basename(full_path)

    if not os.path.exists(full_path):
        return "ERROR: Cannot move file - file doesnt exist: " + full_path
    
    if not os.path.isfile(full_path):
        return "ERROR: Cannot move file - path is not of a file: " + full_path

    new_full_path = os.path.join(abs_working_dir, destination_path)

    if not os.path.exists(os.path.dirname(new_full_path)):
        return "ERROR: Cannot move file - destination doesnt exist: " + full_path
    

    shutil.move(full_path, new_full_path)
    
    return f"File '{file_name}' moved sucessfully from '{full_path}' to '{new_full_path}'"

schema_move_file = {
    "type": "function",
    "function": {
        "name": "move_file",
        "description": "Move o arquivo entre dois paths passados como parametros",
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
                "destination_path": {
                    "type": "string", 
                    "description": "Path a partir do working_dir para onde o arquivo deve ser movido"
                },
            },
            "required": ["working_dir","file_path","destination_path"],
        },
    },
}

if __name__ == "__main__":
    # para dar erro
    result1 = move_file('obsidian','teste',"testando write function")
    result2 = move_file('obsidian','teste/testeadasjdhakjdhakd.md',"teste")
    result3 = move_file('obsidian','teste/arquivo1.md',"pasta66666/arquivo.m1")
    ## para funcionar
    result4 = move_file('obsidian','teste/arquivo1.md',"teste/teste4")
    result4 = move_file('obsidian','teste/arquivo3.md',"teste2")

    print(result1)
    print(result2)
    print(result3)
    print(result4)

