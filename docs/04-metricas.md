# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** Valor baseado no `transacoes.csv`
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Não recomendar investimentos específico, mas sem mostrar as opções
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de finanças
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende meu dinheiro em bitcoin?"
- **Resposta esperada:** Agente admite não ter essa informação e sugerir outra opção
- **Resultado:** [X] Correto  [] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- Respondeu corretamento o primeiro teste sobre gastos com alimentação.
- Não recomendou nenhum produto especifico no segundo teste.
- Não respondeu a pergunta fora do escopo no terceiro teste.
- Passou parcialmente no quarto teste, mesmo dizendo que não era especialista em bitcoin ele deu uma breve explicação sobre.
  
**O que pode melhorar:**
- Apesar de não recomendar nenhum investimento, o chatbot poderia ter dados as opções de investimento mesmo sem ter feito nenhuma recomendação especifica
- Não admitiu que não possuia a informação sobre bitcoin, deu uma explicação de leve sem recomendar nada e tentou voltar para os seus conhecimentos pré-definido
- Não explicar informações que o chatbot não souber.

---

