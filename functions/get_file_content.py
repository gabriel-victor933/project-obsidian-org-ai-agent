import os

MAX_FILE_SIZE = 10000

def get_file_content(working_dir: str, file_path: str, start_byte: int = None):

    abs_working_dir = os.path.abspath(working_dir)
    full_path = os.path.join(abs_working_dir, file_path)

    if not os.path.isfile(full_path):
        raise ValueError(f"File {file_path} doesn't exists!")
    
    with open(full_path,'r') as file:
        if start_byte is not None:
            file.seek(start_byte,0)
        
        full_text = file.read(MAX_FILE_SIZE)
        
        if len(full_text) == MAX_FILE_SIZE:
            full_text += F"...\n[-- TEXTO FOI TRUNCADO NO BYTE {MAX_FILE_SIZE}. Utilize o parametro start_byte para continuar lendo arquivo --]\n"

        return full_text
    

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Lê o conteudo de um arquivo. O limite máximo de caracteres é 10000, entretanto a funcao permite começar a leitura a partir de qualquer caracterer usando o parametro start_bytes",
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
                "start_byte": {
                    "type": "integer", 
                    "description": "Byte a partir do qual a leitura do arquivo é iniciada"
                },
            },
            "required": ["working_dir","file_path"],
        },
    },
}

if __name__ == "__main__":
    result1 = get_file_content('obsidian','teste/teste123.md')
    result2 = get_file_content('obsidian','teste/teste123.md',1000)
    result3 = get_file_content('obsidian','teste/teste-second-layer/teste456.md')

    print(result1)
    print(result2)
    print(result3)
