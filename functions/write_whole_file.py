import os


def write_whole_file(working_dir: str, file_path: str, content: str):

    abs_working_dir = os.path.abspath(working_dir)
    full_path = os.path.join(abs_working_dir, file_path)
    
    subdir = os.path.dirname(full_path)

    if not os.path.isdir(subdir):
        os.makedirs(subdir, exist_ok=True)
    
    with open(full_path,'w') as file:
        file.write(content)

        return f"File {file_path} writed with sucess!!"

schema_write_whole_file = {
    "type": "function",
    "function": {
        "name": "write_whole_file",
        "description": "Escreve o conteudo do parametro content no arquivo. Funcao substitui qualquer coisa que ja existir no arquivo",
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
                "content": {
                    "type": "string", 
                    "description": "Conteudo que seja escrito no arquivo"
                },
            },
            "required": ["working_dir","file_path","content"],
        },
    },
}

if __name__ == "__main__":
    result1 = write_whole_file('obsidian','teste/teste-write-archive/teste/teste4.md',"testando write function")
    result2 = write_whole_file('obsidian','teste/teste4.md',"testando write function novamente")

    print(result1)
    print(result2)

