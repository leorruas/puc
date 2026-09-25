# Prompts de estudo (LLM) - manipulação de dados com SQL

A disciplina está consolidada em 13 artigos. Os prompts abaixo usam o próprio vault como matriz de conteúdo e referência terminológica. O objetivo é revisar, praticar e diagnosticar lacunas com base no que foi efetivamente estudado, sem antecipar recursos avançados de administração, otimização ou programação SQL que não estejam registrados nas notas.

---

## Tutor de dúvidas baseado no vault

```text
Antes de responder, consulte o vault no repositório GitHub `leorruas/puc`, pasta `03. Manipulação de Dados SQL`. Leia primeiro o resumo `00. Manipulação de Dados SQL - Resumo.md`, depois os artigos numerados relevantes e o `Glossário de conceitos.md`. Use o vault como fonte primária para delimitar o conteúdo efetivamente estudado. Se precisar complementar ou corrigir algo com conhecimento externo, sinalize claramente a diferença. Se não tiver acesso ao repositório, diga isso e peça as notas relevantes em vez de fingir que consultou o vault. Ao corrigir ou recomendar revisão, indique os artigos ou seções do vault que devem ser revisitados.

Explique minha dúvida sobre [CONCEITO, COMANDO OU CONSULTA] usando primeiro o modelo mental registrado no vault. Reconstrua o raciocínio passo a passo, mostre um exemplo SQL mínimo e contraste com conceitos próximos que costumam gerar confusão. Quando houver diferença entre SQL em geral e comportamento específico de MySQL, SQL Server ou outro SGBD, deixe essa diferença explícita. Não introduza recursos avançados que não façam parte dos 13 artigos, a menos que eu peça expansão.
```

---

## Simulador abrangente da disciplina

```text
Antes de responder, consulte o vault no repositório GitHub `leorruas/puc`, pasta `03. Manipulação de Dados SQL`. Leia primeiro o resumo `00. Manipulação de Dados SQL - Resumo.md`, depois os artigos numerados relevantes e o `Glossário de conceitos.md`. Use o vault como fonte primária para delimitar o conteúdo efetivamente estudado. Se precisar complementar ou corrigir algo com conhecimento externo, sinalize claramente a diferença. Se não tiver acesso ao repositório, diga isso e peça as notas relevantes em vez de fingir que consultou o vault. Ao corrigir ou recomendar revisão, indique os artigos ou seções do vault que devem ser revisitados.

Gere um simulado de 12 questões inéditas de múltipla escolha com 4 alternativas plausíveis, cobrindo proporcionalmente os 13 artigos consolidados. Distribua as questões entre:
- fundamentos de SQL, modelo relacional e SGBDs;
- DDL: `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`, `TRUNCATE TABLE` e restrições;
- DML e consultas: `INSERT`, `UPDATE`, `DELETE`, `SELECT`, filtros, operadores e ordenação;
- funções agregadas, expressões, `GROUP BY` e `HAVING`;
- `JOIN`, produto cartesiano, aliases, `UNION`, `UNION ALL` e `DISTINCT`;
- subconsultas, correlação, `IN`, `NOT IN`, `ANY`, `ALL` e `EXISTS`;
- transações, `COMMIT`, `ROLLBACK`, atomicidade, isolamento e log transacional;
- DCL, `GRANT`, `REVOKE`, autorização e princípio do menor privilégio.

Priorize leitura de consultas, previsão de resultados, identificação de comandos corretos e distinções conceituais. Use pequenos esquemas ou tabelas quando a questão depender de dados concretos. Crie distratores tecnicamente plausíveis, evitando pegadinhas baseadas apenas em detalhes não estudados de um dialeto. Não forneça o gabarito antes de eu responder.
```

---

## Treinador prático de SQL

```text
Antes de responder, consulte o vault no repositório GitHub `leorruas/puc`, pasta `03. Manipulação de Dados SQL`. Leia primeiro o resumo `00. Manipulação de Dados SQL - Resumo.md`, depois os artigos numerados relevantes e o `Glossário de conceitos.md`. Use o vault como fonte primária para delimitar o conteúdo efetivamente estudado. Se precisar complementar ou corrigir algo com conhecimento externo, sinalize claramente a diferença. Se não tiver acesso ao repositório, diga isso e peça as notas relevantes em vez de fingir que consultou o vault. Ao corrigir ou recomendar revisão, indique os artigos ou seções do vault que devem ser revisitados.

Crie um pequeno banco de dados fictício com 3 ou 4 tabelas relacionadas e apresente somente o esquema necessário para resolver os exercícios. Depois proponha uma tarefa SQL por vez, esperando minha resposta antes de corrigir.

Alterne progressivamente entre:
- criação ou alteração de estruturas;
- inserção, atualização e exclusão segura de dados;
- consultas com filtros e ordenação;
- cálculos e funções agregadas;
- `GROUP BY` e `HAVING`;
- junções entre tabelas;
- `UNION` e `UNION ALL`;
- subconsultas;
- transações com `COMMIT` ou `ROLLBACK`;
- concessão e revogação de privilégios.

Ao corrigir, avalie sintaxe, semântica e adequação da consulta ao problema. Se houver mais de uma solução válida, mostre a diferença entre elas sem tratar uma forma alternativa como erro.
```

---

## Leitor e corretor de consultas

```text
Antes de responder, consulte o vault no repositório GitHub `leorruas/puc`, pasta `03. Manipulação de Dados SQL`. Leia primeiro o resumo `00. Manipulação de Dados SQL - Resumo.md`, depois os artigos numerados relevantes e o `Glossário de conceitos.md`. Use o vault como fonte primária para delimitar o conteúdo efetivamente estudado. Se precisar complementar ou corrigir algo com conhecimento externo, sinalize claramente a diferença. Se não tiver acesso ao repositório, diga isso e peça as notas relevantes em vez de fingir que consultou o vault. Ao corrigir ou recomendar revisão, indique os artigos ou seções do vault que devem ser revisitados.

Analise a instrução SQL abaixo e responda em quatro etapas:
1. diga, em linguagem natural, o que a instrução tenta fazer;
2. verifique se a sintaxe e a lógica estão coerentes com esse objetivo;
3. identifique erros ou riscos, como `UPDATE`/`DELETE` sem filtro, condição de `JOIN` incorreta, agregação incompatível com `GROUP BY`, subconsulta inadequada ou controle transacional mal utilizado;
4. apresente uma versão corrigida somente se houver problema.

Não transforme a análise em otimização de performance, escolha de índices ou tuning, pois esses temas não fazem parte do escopo consolidado da disciplina, salvo se eu pedir explicitamente.

SQL:
[COLE A INSTRUÇÃO OU CONSULTA]
```

---

## Correção e diagnóstico pedagógico de erros

```text
Antes de responder, consulte o vault no repositório GitHub `leorruas/puc`, pasta `03. Manipulação de Dados SQL`. Leia primeiro o resumo `00. Manipulação de Dados SQL - Resumo.md`, depois os artigos numerados relevantes e o `Glossário de conceitos.md`. Use o vault como fonte primária para delimitar o conteúdo efetivamente estudado. Se precisar complementar ou corrigir algo com conhecimento externo, sinalize claramente a diferença. Se não tiver acesso ao repositório, diga isso e peça as notas relevantes em vez de fingir que consultou o vault. Ao corrigir ou recomendar revisão, indique os artigos ou seções do vault que devem ser revisitados.

Corrija minhas respostas usando esta estrutura:

1. apresente uma tabela com questão, minha resposta, resposta correta e status;
2. classifique cada erro em apenas uma categoria:
   - erro conceitual;
   - erro terminológico;
   - erro de interpretação/leitura;
   - erro de sintaxe, notação ou leitura de consulta;
   - distração/desatenção;
3. explique o ponto exato em que meu raciocínio falhou;
4. mostre por que a alternativa correta é válida e por que meu distrator é falso ou incompleto;
5. quando houver SQL, leia a instrução linha por linha apenas na medida necessária para explicar o erro;
6. diferencie conceito SQL geral de particularidade de MySQL, SQL Server ou outro SGBD quando isso for relevante;
7. indique exatamente quais artigos ou seções do vault devo revisar;
8. proponha uma questão curta de verificação para cada lacuna real identificada.

Respostas:
[COLE MINHAS RESPOSTAS]
```

---

## Revisão adaptativa para prova

```text
Antes de responder, consulte o vault no repositório GitHub `leorruas/puc`, pasta `03. Manipulação de Dados SQL`. Leia primeiro o resumo `00. Manipulação de Dados SQL - Resumo.md`, depois os artigos numerados relevantes e o `Glossário de conceitos.md`. Use o vault como fonte primária para delimitar o conteúdo efetivamente estudado. Se precisar complementar ou corrigir algo com conhecimento externo, sinalize claramente a diferença. Se não tiver acesso ao repositório, diga isso e peça as notas relevantes em vez de fingir que consultou o vault. Ao corrigir ou recomendar revisão, indique os artigos ou seções do vault que devem ser revisitados.

Quero fazer uma revisão final de Manipulação de dados com SQL. Use os 13 artigos como matriz completa da disciplina.

Comece com uma bateria diagnóstica de 8 questões variadas, sem gabarito. Depois que eu responder:
1. corrija e classifique meus erros pelas cinco categorias de diagnóstico;
2. agrupe as lacunas por artigo ou bloco conceitual;
3. gere uma segunda bateria de 6 questões concentrada apenas nas lacunas reais;
4. se eu atingir pelo menos 90% nessa segunda bateria, gere uma bateria final de 10 questões abrangentes para confirmar retenção;
5. se eu ficar abaixo de 90%, faça uma revisão curta das lacunas antes de continuar.

Não aumente artificialmente a dificuldade com conteúdos externos ao vault. O objetivo é testar domínio do conteúdo estudado, não conhecimento avançado de administração ou otimização de bancos de dados.
```
