# Prompts de Estudo (LLM) - Programação Modular

Use estes templates de prompt prontos com seu LLM (ChatGPT, Gemini, Claude, etc.) para sanar dúvidas, gerar exemplos práticos e exercitar seu conhecimento nesta disciplina.

---

### Explicar Conceitos Complexos
```text
Aja como um professor sênior de Engenharia de Software. Explique o conceito de [CONCEITO] em Programação Modular de forma intuitiva, usando analogias do mundo real e fornecendo exemplos práticos em C#/Java/Python.
```

### Modularizador de Código
```text
Aja como um especialista em Refatoração. Eu tenho o seguinte bloco de código monolítico. Como posso modularizá-lo em funções/classes com responsabilidade única? [INSIRA O CÓDIGO AQUI]
```

---

### Simulador de Prova Avançado
```text
Aja como um examinador de nível acadêmico avançado em Engenharia de Software e Programação Modular. Gere um simulador de prova composto por 5 questões de múltipla escolha cobrindo:
- Motivação e pilares da programação modular (corretude, robustez, escalabilidade e reuso).
- Estágios evolutivos da programação modular (código sequencial, programação estruturada, decomposição, modularização e gestão do próprio estado).
- Diferença conceitual e sintática entre Funções (abstração de expressão) e Procedimentos (abstração de comandos), efeitos colaterais e retorno (com exemplos como cálculo de DV de CPF e menus de E/S).
- Tipos Abstratos de Dados (TADs) e sua relação formal com a teoria dos conjuntos, encapsulamento e classes/objetos.
- Programação Orientada a Objetos (POO), a visão histórica de Alan Kay (1967) sobre miniprogramas que trocam mensagens, reusabilidade, extensibilidade e a gestão do alto/baixo acoplamento.

Regras da questão:
- Cada questão deve possuir 4 alternativas (A, B, C, D) com distratores altamente plausíveis e complexos.
- Não forneça o gabarito imediatamente; aguarde o usuário responder item a item ou todas juntas.
```

### Parâmetros de Feedback e Diagnóstico de Erros
```text
Com base na resposta fornecida pelo aluno ao simulador de prova, realize o diagnóstico detalhado seguindo a estrutura:
1. Gabarito comentado de cada questão.
2. Análise do erro cometido pelo aluno (classificando em: erro conceitual, erro de leitura/interpretação, erro terminológico ou erro de aplicação prática).
3. Explicação técnica aprofundada demonstrando o porquê de cada distrator estar incorreto.
```
