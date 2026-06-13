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