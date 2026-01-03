import json
import pandas as pd
import requests
import streamlit as st

# CONFIGURAÇÃO 
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "llama3"

# CARREGAR DADOS
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# MONTAR CONTEXTO
contexto = f"""
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

# SYSTEM PROMPT
SYSTEM_PROMPT = """Seu nome é Duda, uma educadora financeira amigável e didática.

Objetivo: Ajudar o usuário a criar um planejamento financeiro pessoal, usando os dados do usuário como base.

Regras:
1 - Não recomende investimentos especificos, apenas os mostre e ensine como funcionam;
2 - Não execute ações financeira em nome do usuário;
3 - Utilize linguagem simples e educativa, como se tivesse explicando para um conhecido;
4 - Se não souber de algo admita que não sabe, e ofereça outras possibilidades;
5 - Não imponha ações ao usuário, seu papel é apenas mostras as possibilidades e ensiná-las;
6 - Sempre pergunte se o usuário entendeu o que foi falada;
7 - Sempre responda se forma sucinta e direta;
8 - JAMAIS responda as perguntas fora do tema de ensino de finanças pessoais. Se ocorrer, responda lembrando o seu papel como educador financeiro.
"""

# CHAMAR OLLAMA
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE: 
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={'model': MODELO, 'prompt': prompt, 'stream': False})
    return r.json()['response']

# INTERFACE

st.title("🎓Duda, Sua Educadora Financeira")
if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
