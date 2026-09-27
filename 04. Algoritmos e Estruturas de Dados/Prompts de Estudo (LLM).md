# Prompts de estudo (LLM) - Algoritmos e Estruturas de Dados

> **Base obrigatória:** antes de responder, consulte o vault no repositório GitHub `leorruas/puc`, pasta `04. Algoritmos e Estruturas de Dados`. Leia primeiro `00. Algoritmos e Estruturas de Dados - Resumo.md`, depois os artigos numerados relevantes e o `Glossário de conceitos.md`. Use o vault como fonte primária para delimitar o conteúdo efetivamente estudado. Se precisar acrescentar conhecimento externo, identifique explicitamente o complemento. Não introduza algoritmos ou estruturas que não façam parte do conteúdo consolidado sem marcar que são externos ao vault.

## Revisão geral da disciplina

```text
Faça uma revisão ativa de toda a disciplina Algoritmos e Estruturas de Dados com base no vault.

Cubra as duas unidades:
- ArrayList, Queue, Stack e Hashtable;
- coleções genéricas: List<T>, LinkedList<T>, Queue<T>, Stack<T> e Dictionary<TKey, TValue>;
- listas lineares e flexíveis;
- classes autorreferenciais, células, nó cabeça e percurso por referências;
- árvores binárias de pesquisa, altura, busca, inserção, remoção e percursos;
- árvores AVL, fator de balanceamento e rotações;
- tabelas hash, função de transformação, colisões, overflow, rehash e encadeamento.

Não faça apenas um resumo. Para cada bloco:
1. peça que eu explique o conceito com minhas palavras;
2. identifique lacunas na minha explicação;
3. faça uma pergunta curta de aplicação;
4. só depois avance para o próximo bloco.

Ao corrigir, cite o nome do artigo do vault que devo revisar.
```

## Simulado completo

```text
Crie um simulado de 20 questões de múltipla escolha usando somente o conteúdo consolidado no vault de Algoritmos e Estruturas de Dados.

Distribua as questões entre:
- coleções não genéricas e genéricas;
- FIFO e LIFO;
- referências, nós e listas lineares/flexíveis;
- árvores binárias de pesquisa;
- percursos em ordem, pré-ordem e pós-ordem;
- inserção e remoção em árvores;
- AVL e rotações;
- tabelas hash e colisões;
- análise de custo com Θ(1), Θ(log n) e Θ(n).

Use código C# quando fizer sentido. Crie distratores plausíveis, especialmente com erros de índice, referência, condição de parada, direção de percurso e interpretação de complexidade.

Apresente uma questão por vez e espere minha resposta. Depois:
- diga se acertei ou errei;
- classifique o erro como conceitual, terminológico, leitura, sintaxe/notação/código ou distração;
- explique por que cada alternativa está certa ou errada;
- indique o artigo e a seção do vault que devo revisar.
```

## Rastreamento de código e estruturas

```text
Use o vault como referência e gere um exercício de rastreamento manual em C# sobre um dos seguintes temas:
- ArrayList, Queue, Stack ou Dictionary;
- lista linear com array + contador;
- lista flexível com células e referências;
- árvore binária de pesquisa;
- tabela hash com colisões.

Mostre apenas o código e a pergunta inicialmente. Peça que eu determine o estado final da estrutura, a saída do programa ou a sequência de nós/posições visitados.

Depois da minha tentativa, faça a execução passo a passo, mostrando somente os estados que realmente mudam. Evite rastreamento repetitivo sem valor didático.
```

## Árvores binárias e AVL

```text
Treine comigo árvores binárias de pesquisa e AVL com base nos artigos 09 e 10 do vault.

Alterne entre exercícios de:
- identificar raiz, folhas, nós internos, altura e subárvores;
- determinar caminhos de pesquisa;
- inserir valores;
- remover folhas, nós com um filho e nós com dois filhos;
- obter percurso em ordem, pré-ordem e pós-ordem;
- calcular fator de balanceamento usando altura da direita - altura da esquerda;
- identificar se a rotação é simples ou dupla e sua direção.

Sempre desenhe a árvore em Mermaid na correção. Não mostre a resposta antes da minha tentativa.
```

## Tabelas hash e colisões

```text
Treine comigo tabelas hash usando exclusivamente os modelos estudados no artigo 11 do vault.

Crie exercícios com uma tabela de tamanho pequeno e função h(k) = k mod m. Alterne entre:
- inserção sem colisão;
- área de reserva (overflow);
- rehash com segunda função;
- encadeamento com lista flexível;
- pesquisa de elemento existente e inexistente;
- contagem de comparações;
- avaliação da qualidade de uma função hash.

Depois da minha resposta, reconstrua a tabela em formato visual e explique exatamente onde ocorreu cada colisão e como ela foi tratada.
```

## Comparação entre estruturas e custo

```text
Apresente cenários curtos e peça que eu compare as estruturas estudadas no vault sem escolher automaticamente uma "melhor".

Para cada cenário, peça que eu discuta:
- forma de organização dos dados;
- acesso por índice, chave ou referência;
- comportamento de inserção e remoção;
- necessidade de deslocamento ou reconexão;
- custo esperado estudado no vault;
- efeito de balanceamento ou colisões.

Use apenas ArrayList/List<T>, Queue/Stack, LinkedList/lista flexível, árvore binária de pesquisa/AVL e tabela hash. Corrija minha justificativa com base nos artigos correspondentes.
```

## Diagnóstico rápido de dúvida

```text
Vou enviar uma dúvida, trecho de código ou questão de prova de Algoritmos e Estruturas de Dados.

Antes de responder:
1. identifique quais artigos do vault são diretamente relevantes;
2. responda primeiro usando apenas o conteúdo consolidado nesses artigos;
3. diferencie claramente qualquer complemento externo;
4. se houver erro na minha interpretação, diga exatamente qual regra ou modelo mental foi confundido;
5. termine com uma regra curta para eu lembrar na prova.
```
