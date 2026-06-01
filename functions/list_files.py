import os
import glob

def list_files(working_dir: str, subpath: str = ".", recursive: bool = "true") -> str:
    """
    Lista arquivos dentro de um diretorio e subdiretorio. A listagem pode ser recursiva ou não.
    """
    is_recursive = recursive == "true"
    abs_working_dir = os.path.abspath(working_dir)

    abs_subpath = abs_working_dir if subpath == "." else os.path.abspath(os.path.join(working_dir,subpath))
    
    if not os.path.isdir(abs_subpath):
        raise ValueError(f"Directory {subpath} doesn't exists!")

    arr_paths = glob.glob(abs_subpath + "/**", recursive=is_recursive, root_dir=abs_working_dir)

    return "\n".join(arr_paths)


schema_list_files = {
    "type": "function",
    "function": {
        "name": "list_files",
        "description": "Lista arquivos e pastas dentro de um diretorio e subdiretorio. A listagem pode ser recursiva ou não.",
        "parameters": {
            "type": "object",
            "properties": {
                "working_dir": {
                    "type": "string",
                    "description": "Pasta base onde todos os arquivos estão armazenados",
                },
                "subpath": {
                    "type": "string", 
                    "description": "path do subdiretorio dentro de working dir"
                },
                "recursive": {
                    "type": "string", 
                    "enum": ["true", "false"],
                    "description": "Habilita/Desabilita listagem recursiva"
                },
            },
            "required": ["working_dir","subpath"],
        },
    },
}

if __name__ == "__main__":
    print(list_files('obsidian'))
