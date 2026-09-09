# Prompts de estudo (LLM) - Modelagem de Dados

Use estes templates para estudar a disciplina a partir do conteúdo consolidado no próprio vault. Os prompts devem usar os 14 artigos, o resumo e o glossário como referência de escopo, evitando simulados genéricos que cobrem assuntos não estudados.

---

### Tutor de dúvida baseado no vault
```text
Antes de responder, consulte o vault no repositório GitHub `leorruas/puc`, pasta `02. Modelagem de Dados`. Leia primeiro o arquivo de resumo `00.`, depois os artigos numerados relevantes e o `Glossário de conceitos.md` quando existir. Use o vault como fonte primária para delimitar o conteúdo efetivamente estudado. Se precisar complementar ou corrigir algo com conhecimento externo, sinalize explicitamente a diferença. Se você não tiver acesso ao repositório, diga isso e peça as notas relevantes em vez de fingir que consultou o vault. Ao corrigir ou recomendar revisão, indique quais notas do vault devem ser revisitadas.

Explique minha dúvida sobre [CONCEITO OU TRECHO] usando primeiro a formulação adotada nas notas da disciplina. Reconstrua o conceito passo a passo, mostre um exemplo mínimo e contraste com conceitos próximos que costumam gerar confusão. Se minha dúvida revelar uma anotação tecnicamente imprecisa, explique a correção sem apagar o modelo didático usado na aula.
```

### Simulador abrangente da disciplina
```text
Antes de responder, consulte o vault no repositório GitHub `leorruas/puc`, pasta `02. Modelagem de Dados`. Leia primeiro o arquivo de resumo `00.`, depois os artigos numerados relevantes e o `Glossário de conceitos.md` quando existir. Use o vault como fonte primária para delimitar o conteúdo efetivamente estudado. Se precisar complementar ou corrigir algo com conhecimento externo, sinalize explicitamente a diferença. Se você não tiver acesso ao repositório, diga isso e peça as notas relevantes em vez de fingir que consultou o vault. Ao corrigir ou recomendar revisão, indique quais notas do vault devem ser revisitadas.

Gere um simulado de 10 questões inéditas de múltipla escolha com 4 alternativas plausíveis. Distribua as questões pela cobertura real dos artigos 01 a 14, incluindo fundamentos de SGBD, MER/DER, cardinalidades, modelo relacional, PK/FK, integridade, mapeamento, 1FN/2FN/3FN, modelos não-relacionais/NoSQL e segurança de banco de dados. Priorize raciocínio de modelagem e distinções conceituais. Não forneça o gabarito até eu responder.
```

---

### Gerador de DER
```text
Antes de responder, consulte o vault no repositório GitHub `leorruas/puc`, pasta `02. Modelagem de Dados`. Leia primeiro o arquivo de resumo `00.`, depois os artigos numerados relevantes e o `Glossário de conceitos.md` quando existir. Use o vault como fonte primária para delimitar o conteúdo efetivamente estudado. Se precisar complementar ou corrigir algo com conhecimento externo, sinalize explicitamente a diferença. Se você não tiver acesso ao repositório, diga isso e peça as notas relevantes em vez de fingir que consultou o vault. Ao corrigir ou recomendar revisão, indique quais notas do vault devem ser revisitadas.

Com base no seguinte cenário de negócios: [DESCREVA O CENÁRIO]. Identifique as principais Entidades, seus Atributos (incluindo chaves primárias e estrangeiras) e as Relações (com cardinalidade) para criar um Modelo Entidade-Relacionamento lógico.
```

### Validador de Normalização
```text
Antes de responder, consulte o vault no repositório GitHub `leorruas/puc`, pasta `02. Modelagem de Dados`. Leia primeiro o arquivo de resumo `00.`, depois os artigos numerados relevantes e o `Glossário de conceitos.md` quando existir. Use o vault como fonte primária para delimitar o conteúdo efetivamente estudado. Se precisar complementar ou corrigir algo com conhecimento externo, sinalize explicitamente a diferença. Se você não tiver acesso ao repositório, diga isso e peça as notas relevantes em vez de fingir que consultou o vault. Ao corrigir ou recomendar revisão, indique quais notas do vault devem ser revisitadas.

Explique passo a passo como aplicar a 1ª, 2ª e 3ª Formas Normais (FN) na tabela descrita abaixo. Aponte possíveis anomalias de inserção, atualização e deleção:
[DESCREVA A TABELA OU DADOS]
```

---

### Parâmetros de feedback e diagnóstico pedagógico de erros

```text
Antes de responder, consulte o vault no repositório GitHub `leorruas/puc`, pasta `02. Modelagem de Dados`. Leia primeiro o arquivo de resumo `00.`, depois os artigos numerados relevantes e o `Glossário de conceitos.md` quando existir. Use o vault como fonte primária para delimitar o conteúdo efetivamente estudado. Se precisar complementar ou corrigir algo com conhecimento externo, sinalize explicitamente a diferença. Se você não tiver acesso ao repositório, diga isso e peça as notas relevantes em vez de fingir que consultou o vault. Ao corrigir ou recomendar revisão, indique quais notas do vault devem ser revisitadas.

Analise a resposta que eu forneci para a questão de Modelagem de Dados abaixo e diagnostique meus erros utilizando a seguinte estrutura obrigatória de feedback:

1. Diagnóstico do erro:
   - Tipo de erro: [Conceitual / Terminológico / Interpretação de leitura / Sintaxe, notação ou leitura de modelo / Distração]
   - Onde errei: Explique o ponto exato onde a análise falhou (ex: leitura invertida de cardinalidade, confusão entre atributo derivado e composto, dependência parcial vs transitiva).

2. Explicação da resposta correta:
   - Por que a resposta correta é a única válida (fundamentação teórica com autores como Peter Chen, Heuser, Elmasri & Navathe ou Codd).
   - Por que a minha escolha está incorreta (análise do distrator ou da falha de modelagem).

3. Ponte teórica e revisão rápida:
   - Resumo conciso da regra testada e dica prática para não reincidir no erro.
   - Indique os artigos ou seções do vault que devo revisar antes de tentar uma nova questão.

Questão/Cenário: [COLE O ENUNCIADO AQUI]
Minha resposta: [COLE SUA RESPOSTA AQUI]
```

