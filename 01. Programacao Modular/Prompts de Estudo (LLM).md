# Prompts de estudo (LLM) - programação modular

Os prompts desta disciplina usam o próprio vault como referência de escopo. Como a matéria está consolidada, simulados e revisões devem acompanhar a cobertura real das notas atuais, em vez de depender de listas manuais de tópicos que podem ficar desatualizadas.

---

## Tutor de conceitos

```text
Antes de responder, consulte o vault no repositório GitHub `leorruas/puc`, pasta `01. Programacao Modular`. Leia primeiro o resumo `00. Programação modular - Resumo.md`, depois os artigos numerados relevantes e o `Glossário de conceitos.md`. Use o vault como fonte primária para delimitar o conteúdo efetivamente estudado. Se precisar complementar ou corrigir algo com conhecimento externo, sinalize a diferença. Se não tiver acesso ao repositório, diga isso e peça as notas relevantes em vez de fingir que consultou o vault. Ao corrigir ou recomendar revisão, indique as notas do vault que devem ser revisitadas.

Explique [CONCEITO] com a técnica de Feynman. Comece pelo modelo mental mais simples, depois mostre a mecânica em C# e finalize com as nuances técnicas registradas no vault. Diferencie explicitamente regra da linguagem, modelo didático, detalhe de implementação do runtime e consequência prática de design quando essa distinção for relevante. Use um exemplo atômico e, se necessário, um exemplo integrado. Aponte as confusões mais comuns e as notas relacionadas.
```

---

## Revisor e refatorador de código

```text
Antes de responder, consulte o vault no repositório GitHub `leorruas/puc`, pasta `01. Programacao Modular`. Leia primeiro o resumo `00. Programação modular - Resumo.md`, depois os artigos numerados relevantes e o `Glossário de conceitos.md`. Use o vault como fonte primária para delimitar o conteúdo efetivamente estudado. Se precisar complementar ou corrigir algo com conhecimento externo, sinalize a diferença. Se não tiver acesso ao repositório, diga isso e peça as notas relevantes em vez de fingir que consultou o vault. Ao corrigir ou recomendar revisão, indique as notas do vault que devem ser revisitadas.

Analise o código abaixo a partir dos princípios cobertos na disciplina. Identifique problemas de coesão, acoplamento, encapsulamento, invariantes, herança, polimorfismo, generics, coleções, delegates/eventos, SOLID ou padrões de projeto somente quando esses conceitos forem realmente pertinentes. Não force um padrão de projeto onde uma solução simples basta.

Para cada problema:
1. explique o risco ou a limitação;
2. aponte a nota do vault que fundamenta a análise;
3. proponha uma refatoração;
4. mostre o código C# resultante de forma compilável e idiomática.

Código:
[INSIRA O CÓDIGO AQUI]
```

---

## Simulador abrangente da disciplina

```text
Antes de responder, consulte o vault no repositório GitHub `leorruas/puc`, pasta `01. Programacao Modular`. Leia primeiro o resumo `00. Programação modular - Resumo.md`, depois os artigos numerados relevantes e o `Glossário de conceitos.md`. Use o vault como fonte primária para delimitar o conteúdo efetivamente estudado. Se precisar complementar ou corrigir algo com conhecimento externo, sinalize a diferença. Se não tiver acesso ao repositório, diga isso e peça as notas relevantes em vez de fingir que consultou o vault. Ao corrigir ou recomendar revisão, indique as notas do vault que devem ser revisitadas.

Gere um simulado de 10 questões inéditas de múltipla escolha com 4 alternativas plausíveis. Use a cobertura atual do resumo e dos artigos como matriz de conteúdo, distribuindo as questões entre:
- Unidade 1: artigos 01 a 14;
- Unidade 2: artigos 15 a 22, incluindo o artigo 18A sobre interfaces;
- Unidade 3: artigos 23 e 24.

Priorize raciocínio sobre comportamento de código, contratos, encapsulamento, despacho, escolhas de design e distinções conceituais. Não transforme detalhes de runtime em definições da linguagem. Não forneça o gabarito antes de eu responder.
```

---

## Simulador por unidade

```text
Antes de responder, consulte o vault no repositório GitHub `leorruas/puc`, pasta `01. Programacao Modular`. Leia primeiro o resumo `00. Programação modular - Resumo.md`, depois os artigos numerados relevantes e o `Glossário de conceitos.md`. Use o vault como fonte primária para delimitar o conteúdo efetivamente estudado. Se precisar complementar ou corrigir algo com conhecimento externo, sinalize a diferença. Se não tiver acesso ao repositório, diga isso e peça as notas relevantes em vez de fingir que consultou o vault. Ao corrigir ou recomendar revisão, indique as notas do vault que devem ser revisitadas.

Quero estudar a [UNIDADE 1 / UNIDADE 2 / UNIDADE 3]. Consulte no resumo quais artigos pertencem a essa unidade e gere 6 questões de múltipla escolha cobrindo proporcionalmente a cobertura real dessas notas. Use distratores tecnicamente plausíveis e espere minhas respostas antes de corrigir.
```

---

## Correção e diagnóstico pedagógico de erros

```text
Antes de responder, consulte o vault no repositório GitHub `leorruas/puc`, pasta `01. Programacao Modular`. Leia primeiro o resumo `00. Programação modular - Resumo.md`, depois os artigos numerados relevantes e o `Glossário de conceitos.md`. Use o vault como fonte primária para delimitar o conteúdo efetivamente estudado. Se precisar complementar ou corrigir algo com conhecimento externo, sinalize a diferença. Se não tiver acesso ao repositório, diga isso e peça as notas relevantes em vez de fingir que consultou o vault. Ao corrigir ou recomendar revisão, indique as notas do vault que devem ser revisitadas.

Corrija minhas respostas usando esta estrutura:

1. Tabela com questão, minha resposta, resposta correta e status.
2. Diagnóstico de cada erro, classificando-o em apenas uma das cinco categorias:
   - erro conceitual;
   - erro terminológico;
   - erro de interpretação/leitura;
   - erro de sintaxe, notação ou leitura de código/modelo;
   - distração/desatenção.
3. Explique por que meu distrator é falso ou incompleto e por que a alternativa correta é rigorosamente verdadeira.
4. Diferencie, quando necessário, regra do C#, modelo didático e detalhe do runtime.
5. Indique exatamente quais artigos ou seções do vault devo revisar e proponha uma nova questão curta para testar a lacuna identificada.

Respostas:
[COLE MINHAS RESPOSTAS]
```
