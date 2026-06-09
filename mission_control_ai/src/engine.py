"""Motor de análise da Mission Control AI."""
import os
from ollama import Client
from dotenv import load_dotenv
from pathlib import Path

# 1. IMPORTAÇÕES OBRIGATÓRIAS (Para a IA pegar as informações)
from src.telemetria import coletar
from src.alertas import avaliar

load_dotenv()

# Inicialização do cliente de IA
client = Client(
    host="https://ollama.com",
    headers={'Authorization': 'Bearer ' + os.environ.get('OLLAMA_API_KEY', '')}
)

def llm(prompt, system=None):
    """Manda o texto com os dados injetados direto para a Ollama Cloud."""
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    try:
        response = client.chat(
            model="gpt-oss:120b",
            messages=messages,
            options={"num_predict": 500, "temperature": 0.5},
            stream=False
        )
        return response['message']['content'].strip()
    except Exception as e:
        return f"⚠️ Erro ao consultar IA: {e}"

class MissionEngine:
    def __init__(self):
        self.trilha = "envirosat"
        # O system_prompt treina a IA a agir como o controle da missão
        self.system_prompt = (
            "Você é o Mission Control AI do satélite Envirosat.\n"
            "Sua função é analisar a telemetria recebida, interpretar os alertas lógicos "
            "do Python e explicar ao operador a consequência ambiental na Terra."
        )

    def is_ready(self):
        return True  # Libera a CLI para uso

    def status_snapshot(self):
        """Usa as funções importadas para exibir o resumo inicial na tela."""
        dados = coletar()
        alertas = avaliar(dados)
        return f"🛰️ Telemetria Atual: {dados}\n⚠️ Alertas do Sistema: {alertas}"

    def analyze(self, pergunta_usuario):
        """Cruza a pergunta do usuário com os dados importados do satélite."""

        # 2. CAPTURA DOS DADOS EM TEMPO REAL
        dados_satelite = coletar()
        alertas_python = avaliar(dados_satelite)

        # 3. INJEÇÃO DINÂMICA (Criando o contexto que a IA vai ler)
        contexto_da_missao = (
            f"--- DADOS DO SATÉLITE ENVIADOS PARA A REDE NEURAL ---\n"
            f"Variáveis dos Sensores: {dados_satelite}\n"
            f"Alertas de Threshold Ativos: {alertas_python}\n"
            f"--------------------------------------------------\n\n"
        )

        # Junta os dados brutos com o que você acabou de digitar no terminal
        prompt_final = f"{contexto_da_missao}Mensagem do Operador: {pergunta_usuario}"

        # 4. ENVIO PARA A INTELIGÊNCIA ARTIFICIAL
        resposta_ia = llm(prompt_final, system=self.system_prompt)
        return resposta_ia
