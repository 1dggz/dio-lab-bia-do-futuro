# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Para que serve na Duda |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores, dando continuidade ao atendimento de forma mais eficiente. |
| `perfil_investidor.json` | JSON | Personalizar as explicações sobre as dúvidas e necessidades de aprendizado do usuário. |
| `produtos_financeiros.json` | JSON | Conhecer os produtos disponíveis para posteriormente indicar ao usuário. |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente e usar as informações de forma didática. |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

As alterações foram realizadas para adequar os dados ao contexto do projeto, ajustando o perfil do usuário, o histórico de atendimentos e os registros de transações financeiras, de forma a representar um cenário mais realista e compatível com um usuário inicante em organização financeira.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Existem duas possibilidades, injetar os dados diretamente no prompt (Ctrl + C, Ctrl + V) ou carregar os arquivos via código, como no exemplo abaixo:

```python
import panda as pd
import json

#CSVs
historico = pd.read_csv('data/historico_atendimento.csv') 
transacoes = pd.read_csv('data/transacoes.csv')

#JSONs
with open('data/perfil_investidor.json', 'r', encoding='utf-8') as f:
    perfil = json.load(f)

with open('data/produtos_financeiros.json', 'r', encoding='utf-8) as f:
    produtos = json.load(f)
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Podemos injetar os dados em nosso prompt, assegurando que o Agente tenha o melhor contexto possível.

```text
DADOS DO USUÁRIO E PERFIL (data/perfil_investidor.json):
{
  "nome": "Douglas Alves",
  "idade": 22,
  "ocupacao": "Profissional em início de carreira",
  "renda_mensal": 4000.00,
  "nivel_conhecimento_financeiro": "iniciante",
  "objetivo_principal": "Organizar as finanças pessoais",
  "patrimonio_aproximado": 12000.00,
  "reserva_emergencia_atual": 6000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Concluir reserva de emergência",
      "valor_necessario": 12000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do carro",
      "valor_necessario": 12000.00,
      "prazo": "2027-12"
    }
  ]
}

TRANSAÇÕES DO USUÁRIO (data/transacoes.csv): 
data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,4000.00,entrada
2025-10-02,Aluguel,moradia,1000.00,saida
2025-10-03,Supermercado,alimentacao,400.00,saida
2025-10-05,Streaming,lazer,39.90,saida
2025-10-07,Farmácia,saude,70.00,saida
2025-10-10,Restaurante,alimentacao,100.00,saida
2025-10-12,Transporte por aplicativo,transporte,60.00,saida
2025-10-15,Conta de Luz,moradia,150.00,saida
2025-10-20,Academia,saude,90.00,saida
2025-10-25,Transporte público,transporte,120.00,saida

HISTÓRICO DE ATENDIMENTO (data/historico_atendimento.csv):
data,canal,tema,resumo,resolvido
2025-09-15,chat,Renda fixa (conceitos),Explicação geral sobre rentabilidade e prazos,sim
2025-09-22,telefone,Organização financeira,Apoio na compreensão do extrato mensal,sim
2025-10-01,chat,Tesouro Direto (educativo),Explicação conceitual sobre funcionamento do Tesouro Selic,sim
2025-10-12,chat,Metas financeiras,Acompanhamento educativo da reserva de emergência,sim
2025-10-25,email,Organização cadastral,Orientação para atualização de dados pessoais,sim

PRODUTOS DISPONÍVEIS PARA ENSINO (data/produtos_financeiros.json):
[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundo Multimercado",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "CDI + 2%",
    "aporte_minimo": 500.00,
    "indicado_para": "Perfil moderado que busca diversificação"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  }
]

```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

O exemplo abaixo se baseia nos dados utilizados da base de conhecimento, mas os organiza apresentando somente as informações mais relevantes.

```
Dados do Cliente:
- Nome: Douglas Alves
- Perfil: Iniciante
- Objetivos: Organizar as finanças pessoais.
- Reserva atual: R$ 6000.00

Resumo de Gastos:
- Alimentação: R$ 500.00
- Moradia: R$ 1150.00
- Saúde: R$ 160.00
- Lazer: R$ 39.90
- Transporte: R$ 180.00
- Total de saídas: R$ 2029.90

Produtos disponíveis para explicar:
- Tesouro Selic (risco - baixo)
- CDB Liquidez Diária (risco - baixo)
- LCI/LCA (risco - baixo)
- Fundo Multimercado (risco - médio)
- Fundo de Ações (risco - alto)

```
