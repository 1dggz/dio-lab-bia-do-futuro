# 🧠 Projeto de IA Aplicada à Educação Financeira

### 📐 Arquitetura do Projeto

A aplicação foi estruturada com **separação de responsabilidades**, facilitando a manutenção, evolução e escalabilidade do sistema.

```text
src/
├── app.py              # Interface da aplicação (Streamlit)
├── agente.py           # Lógica do agente e comunicação com o modelo
├── config.py           # Configurações e prompt do sistema
└── requirements.txt    # Dependências do projeto

data/
├── perfil_investidor.json
├── transacoes.csv
├── historico_atendimento.csv
└── produtos_financeiros.json
```
### 🛠️ Tecnologias Utilizadas

- Python 3.10+
- Streamlit — Interface web interativa
- Ollama — Execução local de modelos LLM
- LLaMA 3 — Modelo de linguagem
- Pandas — Manipulação e análise de dados
- Requests — Comunicação HTTP

### ▶️ Como Executar o Projeto
1️⃣ Instalar o Ollama
Baixe e instale o [Ollama](https://ollama.com):

Após a instalação, abra um novo terminal e execute:
```text
ollama pull llama3
```
Verifique se o modelo foi instalado corretamente:
```text
ollama list
```

2️⃣ Criar ambiente virtual (opcional, recomendado):
```text
python -m venv .venv

source .venv/bin/activate  # Linux / Mac

.venv\Scripts\activate  # Windows
```

3️⃣ Instalar dependências:

```text
pip install -r src/requirements.txt
```

4️⃣ Executar a aplicação:

Na raiz do projeto, execute:
```text
streamlit run src/app.py
```
Acesse o [link](http://localhost:8501) no navegador:

### 🧪 Dados Utilizados

Os dados utilizados neste projeto são simulados, com fins exclusivamente educacionais:
- Perfil do investidor
- Histórico de transações
- Atendimentos anteriores
- Produtos financeiros disponíveis
  
⚠️ Não há uso de dados reais.

### 📌 Observações Importantes
- O projeto não utiliza APIs externas pagas
- Todo o processamento ocorre localmente
- O modelo de linguagem pode ser facilmente substituído no arquivo `config.py`
- A arquitetura permite futura integração com APIs REST ou outros front-ends

### 🚀 Possíveis Evoluções

- Memória de conversa por sessão
- Classificação automática do perfil financeiro
- Interface multiagente
- Exportação de relatórios financeiros educacionais
- Testes automatizados

### 👤 Autor
Projeto desenvolvido por Douglas Alves <br>
Como parte de estudos em Python, IA aplicada e educação financeira.
