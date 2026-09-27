# Glossário de conceitos

Este glossário reúne os conceitos efetivamente estudados até agora em Algoritmos e estruturas de dados. Os termos estão agrupados por função para facilitar revisão e comparação entre estruturas.

## Estruturas e modelos de organização

| Conceito | Definição no contexto estudado | Onde revisar |
| --- | --- | --- |
| **ArrayList** | Coleção de `System.Collections` cujo tamanho pode crescer conforme elementos são adicionados. | [[01. ArrayList, referências e operações em coleções#Array e ArrayList|Array e ArrayList]] |
| **Queue** | Estrutura de fila em que o primeiro elemento inserido é o primeiro a ser removido. | [[02. Queue e Stack (filas, pilhas, FIFO e LIFO)#Queue e Stack representam ordens diferentes|Queue e Stack]] |
| **Stack** | Estrutura de pilha em que o último elemento inserido é o primeiro a ser removido. | [[02. Queue e Stack (filas, pilhas, FIFO e LIFO)#Queue e Stack representam ordens diferentes|Queue e Stack]] |
| **Hashtable** | Estrutura de dicionário ou mapa que associa chaves a valores e usa uma transformação para determinar onde procurar os dados. | [[03. Hashtable (chave, valor, hashing e colisões)#Chave e valor|Chave e valor]] |
| **List<T>** | Lista genérica sequencial e redimensionável, com acesso por índice e tipo de elemento definido. | [[01. ArrayList, referências e operações em coleções#Da ArrayList para List<T>|Da ArrayList para List<T>]] |
| **LinkedList<T>** | Lista genérica ligada em que cada elemento pertence a um nó conectado aos nós vizinhos; em .NET, é duplamente ligada. | [[04. Coleções genéricas em C# (List, LinkedList, Queue, Stack e Dictionary)#LinkedList<T> organiza elementos como nós conectados|LinkedList<T>]] |
| **LinkedListNode<T>** | Nó de `LinkedList<T>` que contém o valor e referências `Next` e `Previous` para os nós vizinhos. | [[04. Coleções genéricas em C# (List, LinkedList, Queue, Stack e Dictionary)#LinkedList<T> organiza elementos como nós conectados|Nós de LinkedList<T>]] |
| **Dictionary<TKey, TValue>** | Dicionário genérico que associa chaves de tipo `TKey` a valores de tipo `TValue`. | [[04. Coleções genéricas em C# (List, LinkedList, Queue, Stack e Dictionary)#Dictionary<TKey, TValue> tipa separadamente chave e valor|Dictionary<TKey, TValue>]] |
| **Lista linear** | Lista baseada em armazenamento sequencial, normalmente sobre um array e um controle da quantidade de elementos. | [[05. Listas lineares e flexíveis, árvores binárias e tabelas hash#Listas lineares e flexíveis|Listas lineares e flexíveis]] |
| **Lista flexível** | Lista formada por nós ou células conectados por referências, sem depender de um bloco sequencial de memória. | [[05. Listas lineares e flexíveis, árvores binárias e tabelas hash#Listas lineares e flexíveis|Listas lineares e flexíveis]] |
| **Árvore binária** | Estrutura hierárquica de nós em que cada nó pode se relacionar com, no máximo, dois filhos. | [[05. Listas lineares e flexíveis, árvores binárias e tabelas hash#Árvores binárias|Árvores binárias]] |
| **Nó** | Unidade de uma estrutura flexível que armazena um valor e referências usadas para conectá-la a outros elementos. | [[05. Listas lineares e flexíveis, árvores binárias e tabelas hash#Listas lineares e flexíveis|Listas lineares e flexíveis]] |
| **Aresta** | Ligação entre dois nós de uma árvore. | [[05. Listas lineares e flexíveis, árvores binárias e tabelas hash#Árvores binárias|Árvores binárias]] |

## Ordem, estado e organização interna

| Conceito | Definição no contexto estudado | Onde revisar |
| --- | --- | --- |
| **FIFO** | *First In, First Out*: regra em que o primeiro elemento que entra é o primeiro que sai. | [[02. Queue e Stack (filas, pilhas, FIFO e LIFO)#Queue e Stack representam ordens diferentes|Queue e Stack]] |
| **LIFO** | *Last In, First Out*: regra em que o último elemento que entra é o primeiro que sai. | [[02. Queue e Stack (filas, pilhas, FIFO e LIFO)#Queue e Stack representam ordens diferentes|Queue e Stack]] |
| **Count** | Quantidade de elementos atualmente armazenados em uma coleção. | [[01. ArrayList, referências e operações em coleções#Capacidade e quantidade de elementos|ArrayList]] • [[02. Queue e Stack (filas, pilhas, FIFO e LIFO)#Operações em comum entre Queue e Stack|Queue e Stack]] • [[03. Hashtable (chave, valor, hashing e colisões)#Operações principais|Hashtable]] |
| **Capacity** | Quantidade de elementos que a `ArrayList` consegue comportar antes de precisar ampliar seu espaço interno. | [[01. ArrayList, referências e operações em coleções#Capacidade e quantidade de elementos|Capacidade e quantidade de elementos]] |
| **Chave** | Identificador usado como ponto de partida para localizar um valor em uma `Hashtable`. | [[03. Hashtable (chave, valor, hashing e colisões)#Chave e valor|Chave e valor]] |
| **Valor** | Dado associado a uma chave dentro de uma `Hashtable`. | [[03. Hashtable (chave, valor, hashing e colisões)#Chave e valor|Chave e valor]] |
| **Função hash** | Transformação que associa uma chave a uma posição da tabela. | [[03. Hashtable (chave, valor, hashing e colisões)#Da chave até uma posição da tabela|Da chave até uma posição da tabela]] |
| **Colisão** | Situação em que mais de um elemento é direcionado para a mesma posição da tabela. | [[03. Hashtable (chave, valor, hashing e colisões)#Colisões|Colisões]] |
| **Colisão primária** | Nome usado no conteúdo para a colisão em que a posição calculada para uma nova inserção já está ocupada. | [[03. Hashtable (chave, valor, hashing e colisões)#Colisões|Colisões]] |

## Custo e crescimento

| Conceito | Definição no contexto estudado | Onde revisar |
| --- | --- | --- |
| **Θ (Theta)** | Notação usada para expressar a ordem de crescimento do custo de uma operação em função do tamanho da entrada. | [[05. Listas lineares e flexíveis, árvores binárias e tabelas hash#O que significa Θ(log n)|Θ(log n)]] |
| **lg n** | Logaritmo de `n` na base 2; aparece na análise de estruturas cuja altura ou número de etapas cresce logaritmicamente. | [[05. Listas lineares e flexíveis, árvores binárias e tabelas hash#O que significa Θ(log n)|Θ(log n)]] |
| **Θ(log n)** | Crescimento logarítmico: o número de etapas aumenta lentamente quando `n` cresce. Em árvores, depende de a altura permanecer logarítmica. | [[05. Listas lineares e flexíveis, árvores binárias e tabelas hash#O que significa Θ(log n)|Θ(log n)]] |
| **Θ(1)** | Crescimento constante: o custo esperado não aumenta proporcionalmente ao número de elementos. É uma referência importante para acesso em tabelas hash em condições adequadas. | [[05. Listas lineares e flexíveis, árvores binárias e tabelas hash#Tabelas hash|Tabelas hash]] |

## Operações de listas e ArrayList

| Conceito | Definição no contexto estudado | Onde revisar |
| --- | --- | --- |
| **Add** | Método que insere um objeto ao final da `ArrayList`; em `Hashtable`, insere um par chave–valor. | [[01. ArrayList, referências e operações em coleções#Inserção, remoção e consulta|ArrayList]] • [[03. Hashtable (chave, valor, hashing e colisões)#Operações principais|Hashtable]] |
| **Insert** | Método que insere um objeto em um índice especificado da `ArrayList`. | [[01. ArrayList, referências e operações em coleções#Inserção, remoção e consulta|Inserção, remoção e consulta]] |
| **Remove** | Método de remoção cujo significado depende da estrutura; em `ArrayList`, remove a primeira ocorrência do objeto; em `Hashtable`, remove o elemento associado a uma chave. | [[01. ArrayList, referências e operações em coleções#Inserção, remoção e consulta|ArrayList]] • [[03. Hashtable (chave, valor, hashing e colisões)#Remove trabalha com a chave, não com o valor|Hashtable]] |
| **RemoveAt** | Método que remove o elemento armazenado em um índice específico da `ArrayList`. | [[01. ArrayList, referências e operações em coleções#Inserção, remoção e consulta|Inserção, remoção e consulta]] |
| **RemoveRange** | Método que remove uma quantidade de elementos a partir de um índice da `ArrayList`. | [[01. ArrayList, referências e operações em coleções#Inserção, remoção e consulta|Inserção, remoção e consulta]] |
| **IndexOf** | Método que retorna o índice da primeira ocorrência encontrada em uma `ArrayList`. | [[01. ArrayList, referências e operações em coleções#Inserção, remoção e consulta|Inserção, remoção e consulta]] |
| **LastIndexOf** | Método que retorna o índice da última ocorrência encontrada em uma `ArrayList`. | [[01. ArrayList, referências e operações em coleções#Inserção, remoção e consulta|Inserção, remoção e consulta]] |
| **Reverse** | Método que inverte a ordem dos elementos de toda a `ArrayList` ou de um intervalo. | [[01. ArrayList, referências e operações em coleções#Reorganização, conversão e pesquisa|Reorganização, conversão e pesquisa]] |
| **Sort** | Método usado para ordenar os elementos da `ArrayList`. | [[01. ArrayList, referências e operações em coleções#Reorganização, conversão e pesquisa|Reorganização, conversão e pesquisa]] |
| **ToArray** | Método que copia os elementos da coleção para um array. | [[01. ArrayList, referências e operações em coleções#Reorganização, conversão e pesquisa|Reorganização, conversão e pesquisa]] |
| **TrimToSize** | Método que ajusta `Capacity` à quantidade de elementos atualmente armazenados na `ArrayList`. | [[01. ArrayList, referências e operações em coleções#Reorganização, conversão e pesquisa|Reorganização, conversão e pesquisa]] |
| **BinarySearch** | Método de pesquisa binária que retorna a posição encontrada ou um valor negativo quando não encontra o elemento. | [[01. ArrayList, referências e operações em coleções#Reorganização, conversão e pesquisa|Reorganização, conversão e pesquisa]] |

## Operações de fila, pilha e dicionários

| Conceito | Definição no contexto estudado | Onde revisar |
| --- | --- | --- |
| **Enqueue** | Método que insere um objeto no final de uma `Queue`. | [[02. Queue e Stack (filas, pilhas, FIFO e LIFO)#Inserindo e removendo elementos|Inserindo e removendo elementos]] |
| **Dequeue** | Método que remove e retorna o próximo objeto de uma `Queue`. | [[02. Queue e Stack (filas, pilhas, FIFO e LIFO)#Inserindo e removendo elementos|Inserindo e removendo elementos]] |
| **Push** | Método que insere um objeto no topo de uma `Stack`. | [[02. Queue e Stack (filas, pilhas, FIFO e LIFO)#Inserindo e removendo elementos|Inserindo e removendo elementos]] |
| **Pop** | Método que remove e retorna o objeto no topo de uma `Stack`. | [[02. Queue e Stack (filas, pilhas, FIFO e LIFO)#Inserindo e removendo elementos|Inserindo e removendo elementos]] |
| **Peek** | Método que retorna o próximo objeto a ser removido sem removê-lo. Em `Queue`, mostra a frente; em `Stack`, mostra o topo. | [[02. Queue e Stack (filas, pilhas, FIFO e LIFO)#Peek: olhar o próximo sem remover|Peek: olhar o próximo sem remover]] |
| **Clear** | Método que remove todos os elementos armazenados em uma coleção. | [[01. ArrayList, referências e operações em coleções#Inserção, remoção e consulta|ArrayList]] • [[02. Queue e Stack (filas, pilhas, FIFO e LIFO)#Operações em comum entre Queue e Stack|Queue e Stack]] • [[03. Hashtable (chave, valor, hashing e colisões)#Operações principais|Hashtable]] |
| **Contains** | Método que verifica presença de um objeto ou, no caso de `Hashtable`, de uma chave, conforme a estrutura utilizada. | [[01. ArrayList, referências e operações em coleções#Inserção, remoção e consulta|ArrayList]] • [[02. Queue e Stack (filas, pilhas, FIFO e LIFO)#Operações em comum entre Queue e Stack|Queue e Stack]] • [[03. Hashtable (chave, valor, hashing e colisões)#Operações principais|Hashtable]] |
| **ContainsKey** | Método que verifica se uma `Hashtable` ou um dicionário contém determinada chave. | [[03. Hashtable (chave, valor, hashing e colisões)#Operações principais|Hashtable]] • [[04. Coleções genéricas em C# (List, LinkedList, Queue, Stack e Dictionary)#Dictionary<TKey, TValue> tipa separadamente chave e valor|Dictionary<TKey, TValue>]] |
| **ContainsValue** | Método que verifica se uma `Hashtable` ou um dicionário contém determinado valor. | [[03. Hashtable (chave, valor, hashing e colisões)#Operações principais|Hashtable]] • [[04. Coleções genéricas em C# (List, LinkedList, Queue, Stack e Dictionary)#Dictionary<TKey, TValue> tipa separadamente chave e valor|Dictionary<TKey, TValue>]] |
| **TryGetValue** | Método de `Dictionary<TKey, TValue>` que retorna se uma chave existe e, quando existe, disponibiliza seu valor por um parâmetro `out`. | [[04. Coleções genéricas em C# (List, LinkedList, Queue, Stack e Dictionary)#Dictionary<TKey, TValue> tipa separadamente chave e valor|TryGetValue]] |
| **KeyValuePair<TKey, TValue>** | Representação tipada de um par chave–valor ao percorrer um dicionário genérico. | [[04. Coleções genéricas em C# (List, LinkedList, Queue, Stack e Dictionary)#Dictionary<TKey, TValue> tipa separadamente chave e valor|KeyValuePair<TKey, TValue>]] |

## Tipagem, objetos e referências

| Conceito | Definição no contexto estudado | Onde revisar |
| --- | --- | --- |
| **Classe** | Tipo que define os dados e comportamentos que seus objetos terão. | [[01. ArrayList, referências e operações em coleções#Classes, objetos e referências|Classes, objetos e referências]] |
| **Objeto** | Instância criada a partir de uma classe. | [[01. ArrayList, referências e operações em coleções#Classes, objetos e referências|Classes, objetos e referências]] |
| **Referência** | Valor armazenado por uma variável de tipo classe para acessar um objeto; variáveis diferentes podem referenciar a mesma instância. | [[01. ArrayList, referências e operações em coleções#Classes, objetos e referências|Classes, objetos e referências]] |
| **Tipo genérico** | Tipo ou classe parametrizada por um ou mais tipos, como `List<T>` ou `Dictionary<TKey, TValue>`, permitindo reutilizar a mesma implementação com contratos de tipo diferentes. | [[04. Coleções genéricas em C# (List, LinkedList, Queue, Stack e Dictionary)#O tipo entre sinais de menor e maior funciona como um contrato|O tipo genérico como contrato]] |
| **T** | Parâmetro convencional que representa o tipo de elemento de uma classe ou coleção genérica até que um tipo concreto seja fornecido. | [[04. Coleções genéricas em C# (List, LinkedList, Queue, Stack e Dictionary)#O tipo entre sinais de menor e maior funciona como um contrato|Parâmetro de tipo T]] |
| **Segurança de tipagem** | Capacidade de impedir combinações incompatíveis de tipos antes da execução, como tentar inserir uma `string` em `List<int>`. | [[04. Coleções genéricas em C# (List, LinkedList, Queue, Stack e Dictionary)#Segurança de tipos, menos casts e boxing/unboxing|Segurança de tipos]] |
| **Cast (casting)** | Conversão explícita em que o programa pede que um valor ou referência seja tratado como outro tipo compatível, como `int numero = (int)objeto;`. Em coleções não genéricas, casts aparecem com frequência porque os elementos são recuperados como `object`. | [[04. Coleções genéricas em C# (List, LinkedList, Queue, Stack e Dictionary)#Segurança de tipos, menos casts e boxing/unboxing|Casts e coleções genéricas]] |
| **Boxing** | Conversão de um tipo de valor, como `int`, para `object` ou para uma interface implementada por esse tipo, fazendo o valor passar a ser tratado como objeto. | [[04. Coleções genéricas em C# (List, LinkedList, Queue, Stack e Dictionary)#Segurança de tipos, menos casts e boxing/unboxing|Boxing e unboxing]] |
| **Unboxing** | Extração de um tipo de valor que estava empacotado como `object`, recuperando seu tipo original; normalmente exige um cast explícito. | [[04. Coleções genéricas em C# (List, LinkedList, Queue, Stack e Dictionary)#Segurança de tipos, menos casts e boxing/unboxing|Boxing e unboxing]] |

## Percurso, comparação e convenções

| Conceito | Definição no contexto estudado | Onde revisar |
| --- | --- | --- |
| **foreach** | Estrutura de repetição usada para percorrer os elementos de uma coleção sem controlar manualmente um índice. | [[01. ArrayList, referências e operações em coleções#Percorrendo a coleção com foreach|Percorrendo a coleção com foreach]] |
| **IComparer** | Contrato usado para definir como dois objetos devem ser comparados durante ordenação e pesquisa. | [[01. ArrayList, referências e operações em coleções#Ordenação e pesquisa de objetos|Ordenação e pesquisa de objetos]] |
| **IComparer<T>** | Contrato genérico para definir como dois objetos do tipo `T` devem ser comparados em ordenação e pesquisa. | [[04. Coleções genéricas em C# (List, LinkedList, Queue, Stack e Dictionary)#Comparação tipada com IComparer<T>|Comparação tipada com IComparer<T>]] |
| **PascalCase** | Convenção de nomes em que cada palavra começa com letra maiúscula, usada nos métodos públicos vistos, como `RemoveAt` e `BinarySearch`. | [[01. ArrayList, referências e operações em coleções#Inserção, remoção e consulta|Inserção, remoção e consulta]] |
