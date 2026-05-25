# PROJECT obsidian organizer ai agent

Projeto simples de agent de AI que apenas lê e escreve arquivos .MD com o objetivo de criar conexões entre eles.

A ideia é ter um arquivo base onde eu apenas escrevo e anoto tudo o que eu escrevi no meu obsidian. Então eu peço para o agente organizar tudo o que eu estudei no dia e criar conexões com outros itens.
Dessa forma eu agilizo o problema de criar conexões manualmente porque demora demais.


## Requisitos:

#### Requisitos funcionais:
- Agente deve ser capaz de alterar e corrigir arquivos. 
- Agente deve ser capaz de gerar conexões dentro de um arquivo. 
- Agente deve ser capaz de visualizar e listar os arquivos .md recursivamente dentro da pasta.
- Agente de receber comandos via CLI.

#### Requisitos não funcionais:
- Agente deve ser construido sobre a lib litellm.
- Agente de usar argsparse para ler input do usuario.


## Agent Structute parts

- Agent loop. 
- Function tool executor.
- Agents tools - functions that the agent nows and can ask to execute. 
- Funcao para chamar a LLM