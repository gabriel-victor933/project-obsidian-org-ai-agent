# Obsidian Organizer AI Agent

Agente de AI que lê e escreve arquivos `.md` com o objetivo de organizar notas do Obsidian automaticamente.

A ideia é ter um arquivo base onde o usuário anota tudo o que estudou no dia, e então pede ao agente para organizar o conteúdo e criar conexões com outras notas existentes — agilizando um processo que feito manualmente seria muito demorado.

---

## O que o agente faz

- **Corrige o texto** — revisa e corrige erros de português nas notas
- **Cria conexões entre notas** — insere links no formato `[[nome-da-nota]]` do Obsidian entre notas relacionadas (novas e antigas)
- **Organiza em subpastas** — move notas para uma estrutura hierárquica do mais geral para o mais específico
- **Sinaliza possíveis erros** — adiciona um callout de aviso em notas com conteúdo potencialmente incorreto ou desatualizado, sem alterar o conteúdo em si

---

## Arquitetura

```
src/
├── main.py              # Agent loop + entrada CLI
├── config.py            # System prompt e constantes
├── tool_executer.py     # Executor de ferramentas
├── tools/               # Ferramentas disponíveis para o agente
│   ├── list_files.py
│   ├── get_file_content.py
│   ├── write_whole_file.py
│   ├── create_dir.py
│   ├── move_file.py
│   ├── rename_file.py
│   └── end_session.py
└── utils/
    ├── llm_handler.py       # Wrapper do LiteLLM Router (histórico + tool calls)
    ├── logger_utility.py    # Logger customizado para observabilidade
    ├── decorators.py
    └── exceptions.py
```

### Componentes principais

| Componente | Descrição |
|---|---|
| Agent loop | Executa até 50 iterações até o agente chamar `end_session` |
| LLM Handler | Gerencia histórico de mensagens e chama o LiteLLM Router |
| Tool Executor | Recebe o nome da função e argumentos do modelo e executa a tool correspondente |
| Tools | Funções que o agente pode chamar para interagir com o sistema de arquivos |
| Logger | Callback customizado do LiteLLM que salva logs das chamadas em `logs/` |

---

## Ferramentas disponíveis para o agente

| Tool | Descrição |
|---|---|
| `list_files` | Lista arquivos `.md` recursivamente dentro da pasta base |
| `get_file_content` | Lê o conteúdo de um arquivo |
| `write_whole_file` | Escreve/sobrescreve um arquivo completo |
| `create_dir` | Cria um diretório |
| `move_file` | Move um arquivo para outro caminho |
| `rename_file` | Renomeia um arquivo |
| `end_session` | Finaliza a sessão e retorna a resposta final ao usuário |

---

## Stack

- **Python** 3.12+
- **LiteLLM** — abstração de LLM com suporte a Router e fallback automático entre modelos
- **Google Gemini** — modelo primário `gemini-2.5-flash` com fallback para outros modelos Gemini
- **python-dotenv** — gerenciamento de variáveis de ambiente
- **argparse** — interface de linha de comando

---

## Como usar

### Instalação

```bash
# Instalar dependências (recomendado: uv)
uv sync

# Ou com pip
pip install -e .
```

### Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
GEMINI_API_KEY=sua_chave_aqui
```

### Executando

```bash
# Dentro de src/
python main.py "organize minhas anotações de hoje e crie conexões com as notas existentes"

# Com modo verbose
python main.py "sua mensagem" --verbose
```

---

## Melhorias futuras

- Conversa multi-turn — o usuário pergunta, o agente responde e faz perguntas de volta antes de executar
