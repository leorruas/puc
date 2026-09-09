# Prompts de estudo (LLM) - modelagem de dados

A disciplina está consolidada em 14 artigos. Os prompts abaixo devem usar o vault como matriz de conteúdo e referência terminológica, preservando a distinção entre modelo conceitual, modelo lógico, implementação física e regras específicas de SGBDs.

---

## Tutor de dúvida baseado no vault

```text
Antes de responder, consulte o vault no repositório GitHub `leorruas/puc`, pasta `02. Modelagem de Dados`. Leia primeiro o resumo `00. Modelagem de Dados - Resumo.md`, depois os artigos numerados relevantes e o `Glossário de conceitos.md`. Use o vault como fonte primária para delimitar o conteúdo efetivamente estudado. Se precisar complementar ou corrigir algo com conhecimento externo, sinalize a diferença. Se não tiver acesso ao repositório, diga isso e peça as notas relevantes em vez de fingir que consultou o vault. Ao corrigir ou recomendar revisão, indique as notas do vault que devem ser revisitadas.

Explique minha dúvida sobre [CONCEITO OU TRECHO] usando primeiro a formulação adotada nas notas da disciplina. Reconstrua o conceito passo a passo, mostre um exemplo mínimo e contraste com conceitos próximos que costumam gerar confusão. Se minha anotação estiver tecnicamente imprecisa, corrija-a sem apagar o modelo didático usado na aula.
```

---

## Simulador abrangente da disciplina

```text
Antes de responder, consulte o vault no repositório GitHub `leorruas/puc`, pasta `02. Modelagem de Dados`. Leia primeiro o resumo `00. Modelagem de Dados - Resumo.md`, depois os artigos numerados relevantes e o `Glossário de conceitos.md`. Use o vault como fonte primária para delimitar o conteúdo efetivamente estudado. Se precisar complementar ou corrigir algo com conhecimento externo, sinalize a diferença. Se não tiver acesso ao repositório, diga isso e peça as notas relevantes em vez de fingir que consultou o vault. Ao corrigir ou recomendar revisão, indique as notas do vault que devem ser revisitadas.

Gere um simulado de 10 questões inéditas de múltipla escolha com 4 alternativas plausíveis. Distribua as questões pela cobertura real dos artigos 01 a 14, incluindo fundamentos de SGBD, MER/DER, cardinalidades, MER Estendido, modelo relacional, PK/FK, integridade, mapeamento, 1FN/2FN/3FN, modelos não-relacionais/NoSQL e segurança de banco de dados. Priorize raciocínio de modelagem, leitura de dependências e distinções entre níveis conceitual, lógico e de implementação. Não forneça o gabarito até eu responder.
```

---

## Validador de DER e mapeamento relacional

```text
Antes de responder, consulte o vault no repositório GitHub `leorruas/puc`, pasta `02. Modelagem de Dados`. Leia primeiro o resumo `00. Modelagem de Dados - Resumo.md`, depois os artigos numerados relevantes e o `Glossário de conceitos.md`. Use o vault como fonte primária para delimitar o conteúdo efetivamente estudado. Se precisar complementar ou corrigir algo com conhecimento externo, sinalize a diferença. Se não tiver acesso ao repositório, diga isso e peça as notas relevantes em vez de fingir que consultou o vault. Ao corrigir ou recomendar revisão, indique as notas do vault que devem ser revisitadas.

Com base neste cenário de negócio:
[DESCREVA O CENÁRIO]

1. identifique entidades, atributos identificadores, relacionamentos, papéis, cardinalidades e participações para um DER conceitual;
2. não introduza chaves estrangeiras no DER conceitual apenas por antecipar a implementação relacional;
3. depois faça separadamente o mapeamento para o modelo relacional, mostrando relações, PKs, FKs e restrições necessárias;
4. explique as decisões de mapeamento para 1:1, 1:N, N:N, atributos multivalorados, entidades fracas ou generalização/especialização somente quando aparecerem no cenário.
```

---

## Treinador de normalização

```text
Antes de responder, consulte o vault no repositório GitHub `leorruas/puc`, pasta `02. Modelagem de Dados`. Leia primeiro o resumo `00. Modelagem de Dados - Resumo.md`, depois os artigos numerados relevantes e o `Glossário de conceitos.md`. Use o vault como fonte primária para delimitar o conteúdo efetivamente estudado. Se precisar complementar ou corrigir algo com conhecimento externo, sinalize a diferença. Se não tiver acesso ao repositório, diga isso e peça as notas relevantes em vez de fingir que consultou o vault. Ao corrigir ou recomendar revisão, indique as notas do vault que devem ser revisitadas.

Analise a relação abaixo:
[DESCREVA A TABELA, CHAVES E DEPENDÊNCIAS FUNCIONAIS]

Faça o processo de normalização até a 3FN. Em cada etapa:
1. identifique a chave candidata ou as chaves candidatas;
2. mostre as dependências funcionais relevantes;
3. verifique 1FN, 2FN e 3FN separadamente;
4. identifique dependências parciais e transitivas;
5. mostre a decomposição necessária;
6. explique quais anomalias de inserção, atualização ou exclusão são reduzidas pela mudança.

Não trate a criação de mais tabelas como objetivo em si; justifique cada decomposição pelas dependências.
```

---

## Correção e diagnóstico pedagógico de erros

```text
Antes de responder, consulte o vault no repositório GitHub `leorruas/puc`, pasta `02. Modelagem de Dados`. Leia primeiro o resumo `00. Modelagem de Dados - Resumo.md`, depois os artigos numerados relevantes e o `Glossário de conceitos.md`. Use o vault como fonte primária para delimitar o conteúdo efetivamente estudado. Se precisar complementar ou corrigir algo com conhecimento externo, sinalize a diferença. Se não tiver acesso ao repositório, diga isso e peça as notas relevantes em vez de fingir que consultou o vault. Ao corrigir ou recomendar revisão, indique as notas do vault que devem ser revisitadas.

Analise minha resposta para a questão abaixo e use exatamente uma das cinco categorias de diagnóstico:
- erro conceitual;
- erro terminológico;
- erro de interpretação/leitura;
- erro de sintaxe, notação ou leitura de modelo;
- distração/desatenção.

Explique o ponto exato em que meu raciocínio falhou, por que a resposta correta é válida e por que minha escolha é falsa ou incompleta. Quando houver diferença entre a simplificação usada em aula e uma formulação mais rigorosa, apresente as duas. Termine indicando os artigos ou seções do vault que devo revisar e proponha uma questão curta de verificação.

Questão/cenário:
[COLE O ENUNCIADO]

Minha resposta:
[COLE MINHA RESPOSTA]
```
