# Prompts de Estudo (LLM) - Modelagem de Dados

Use estes templates de prompt prontos com seu LLM (ChatGPT, Gemini, Claude, etc.) para sanar dúvidas, gerar exemplos práticos e exercitar seu conhecimento nesta disciplina.

---

### Gerador de DER
```text
Com base no seguinte cenário de negócios: [DESCREVA O CENÁRIO]. Identifique as principais Entidades, seus Atributos (incluindo chaves primárias e estrangeiras) e as Relações (com cardinalidade) para criar um Modelo Entidade-Relacionamento lógico.
```

### Validador de Normalização
```text
Explique passo a passo como aplicar a 1ª, 2ª e 3ª Formas Normais (FN) na tabela descrita abaixo. Aponte possíveis anomalias de inserção, atualização e deleção:
[DESCREVA A TABELA OU DADOS]
```

---

### Parâmetros de feedback e diagnóstico pedagógico de erros

```text
Analise a resposta que eu forneci para a questão de Modelagem de Dados abaixo e diagnostique meus erros utilizando a seguinte estrutura obrigatória de feedback:

1. Diagnóstico do erro:
   - Tipo de erro: [Conceitual / Terminológico / Interpretação de Leitura / Aplicação de Regra / Sintaxe ou Notação / Distração]
   - Onde errei: Explique o ponto exato onde a análise falhou (ex: leitura invertida de cardinalidade, confusão entre atributo derivado e composto, dependência parcial vs transitiva).

2. Explicação da resposta correta:
   - Por que a resposta correta é a única válida (fundamentação teórica com autores como Peter Chen, Heuser, Elmasri & Navathe ou Codd).
   - Por que a minha escolha está incorreta (análise do distrator ou da falha de modelagem).

3. Ponte teórica e revisão rápida:
   - Resumo conciso da regra testada e dica prática para não reincidir no erro.

Questão/Cenário: [COLE O ENUNCIADO AQUI]
Minha resposta: [COLE SUA RESPOSTA AQUI]
```

