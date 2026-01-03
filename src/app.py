import streamlit as st
from agente import carregar_dados, montar_contexto, perguntar

st.title("🎓Duda, Sua Educadora Financeira")

perfil,transacoes,historico,produtos = carregar_dados()
contexto = montar_contexto(perfil,transacoes,historico,produtos)

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("Pensando..."):
        resposta = perguntar(pergunta,contexto)
        st.chat_message("assistant").write(perguntar(pergunta))
