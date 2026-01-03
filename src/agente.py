import json
import pandas as pd
import requests
from config import OLLAMA_URL, MODELO, SYSTEM_PROMPT

# CARREGAR DADOS
def carregar_dados():
    with open('./data/perfil_investidor.json', encoding='utf-8') as f:
        perfil = json.load(f)

    transacoes = pd.read_csv('./data/transacoes.csv')
    historico = pd.read_csv('./data/historico_atendimento.csv')

    with open('./data/produtos_financeiros.json', encoding='utf-8') as f:
        produtos = json.load(f)

    return perfil, transacoes, historico, produtos

# MONTAR CONTEXTO
def montar_contexto(perfil, transacoes, historico, produtos):    
    return f"""
    CLIENTE; {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['nivel_conhecimento_financeiro']}
    OBJETIVO: {perfil['objetivo_principal']}
    PATRIMÔNIO: R$ {perfil['patrimonio_aproximado']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

    TRANSAÇÕES RECENTES:
    {transacoes.to_string(index=False)}

    ATENDIMENTO ANTERIORES:
    {historico.to_string(index=False)}

    PRODUTOS DISPONÍVEIS:
    {json.dumps(produtos, indent=2, ensure_ascii=False)}
    """


def perguntar(msg,contexto):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE: 
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={'model': MODELO, 'prompt': prompt, 'stream': False})
    return r.json()['response']
