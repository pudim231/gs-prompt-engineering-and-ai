# gs-prompt-engineering-and-ai


# 🚀 Mission Control AI - EnviroSat

## Integrante

Rubens Henrique - RM: 572667

## O que o projeto faz

O sistema simula a operação de um satélite ambiental chamado EnviroSat. 
Dados de telemetria são analisados por IA generativa através do modelo gpt-oss:120b da Ollama Cloud.

## Persona atendida

Operador de Centro de Controle Ambiental.

## Tecnologias

- Python
- Ollama Cloud
- Rich
- Prompt Toolkit
- PyFiglet

## Como executar

1. Criar ambiente virtual
2. Instalar dependências

## Exemplos de Comandos para Testar no Chat
Após iniciar o sistema e o prompt `❯` aparecer, você pode interagir com a IA usando linguagem natural:
* Quais são as condições atuais dos sensores ambientais?
* Caso a bateria caia para menos de 20%, qual o impacto no monitoramento do IBAMA?
* Escreva um relatório de status focado na saúde do sensor térmico.`
* /status (Comando nativo do sistema para visualizar a telemetria crua)
* /clear (Limpa a tela do terminal)
* /exit (Encerra a simulação com segurança)

- version 1.0 - ficou estatico e não respondia nada, não saia do menu
- version 2.0 - saiu di menu porem ficou com resposta programada
- version 3.0 - a AI consegue falar caso pergunte alguma coisa aleatória.
teve problema em ler o alerta e telemetria.
- version 4.0 - tudo corrigido e pronto para perguntas.


```bash
pip install -r requirements.txt