# Glossário de conceitos

Este glossário reúne os conceitos efetivamente estudados até agora em Algoritmos e estruturas de dados. Cada termo aponta para a seção do artigo em que aparece no contexto da disciplina.

| Conceito | Definição no contexto estudado | Onde revisar |
| --- | --- | --- |
| **ArrayList** | Coleção de `System.Collections` cujo tamanho pode crescer conforme elementos são adicionados. | [[01. ArrayList, referências e operações em coleções#Capacidade e quantidade de elementos|Capacidade e quantidade de elementos]] |
| **Capacity** | Quantidade de elementos que a `ArrayList` consegue comportar antes de precisar ampliar seu espaço interno. | [[01. ArrayList, referências e operações em coleções#Capacidade e quantidade de elementos|Capacidade e quantidade de elementos]] |
| **Count** | Quantidade de elementos atualmente armazenados em uma coleção. | [[02. Queue e Stack (filas, pilhas, FIFO e LIFO)#Consultando a estrutura sem remover|Queue e Stack: consulta e quantidade]] |
| **foreach** | Estrutura de repetição usada para percorrer os elementos de uma coleção sem controlar manualmente um índice. | [[01. ArrayList, referências e operações em coleções#Percorrendo a coleção com foreach|Percorrendo a coleção com foreach]] |
| **Add** | Método que insere um objeto ao final da `ArrayList`; em `Hashtable`, insere um par chave–valor. | [[01. ArrayList, referências e operações em coleções#Inserção, remoção e consulta|ArrayList: inserção]] |
| **Insert** | Método que insere um objeto em um índice especificado da `ArrayList`. | [[01. ArrayList, referências e operações em coleções#Inserção, remoção e consulta|Inserção, remoção e consulta]] |
| **Remove** | Método de remoção cujo significado depende da estrutura; em `ArrayList`, remove a primeira ocorrência do objeto; em `Hashtable`, remove o elemento associado a uma chave. | [[03. Hashtable (chave, valor, hashing e colisões)#Operações principais|Hashtable: operações principais]] |
| **RemoveAt** | Método que remove o elemento armazenado em um índice específico da `ArrayList`. | [[01. ArrayList, referências e operações em coleções#Inserção, remoção e consulta|Inserção, remoção e consulta]] |
| **RemoveRange** | Método que remove uma quantidade de elementos a partir de um índice da `ArrayList`. | [[01. ArrayList, referências e operações em coleções#Inserção, remoção e consulta|Inserção, remoção e consulta]] |
| **Clear** | Método que remove todos os elementos armazenados em uma coleção. | [[02. Queue e Stack (filas, pilhas, FIFO e LIFO)#Consultando a estrutura sem remover|Queue e Stack: consulta e quantidade]] |
| **Contains** | Método que verifica presença de um objeto ou, no caso de `Hashtable`, de uma chave, conforme a estrutura utilizada. | [[03. Hashtable (chave, valor, hashing e colisões)#Operações principais|Hashtable: operações principais]] |
| **IndexOf** | Método que retorna o índice da primeira ocorrência encontrada em uma `ArrayList`. | [[01. ArrayList, referências e operações em coleções#Inserção, remoção e consulta|Inserção, remoção e consulta]] |
| **LastIndexOf** | Método que retorna o índice da última ocorrência encontrada em uma `ArrayList`. | [[01. ArrayList, referências e operações em coleções#Inserção, remoção e consulta|Inserção, remoção e consulta]] |
| **Reverse** | Método que inverte a ordem dos elementos de toda a `ArrayList` ou de um intervalo. | [[01. ArrayList, referências e operações em coleções#Reorganização, conversão e pesquisa|Reorganização, conversão e pesquisa]] |
| **Sort** | Método usado para ordenar os elementos da `ArrayList`. | [[01. ArrayList, referências e operações em coleções#Reorganização, conversão e pesquisa|Reorganização, conversão e pesquisa]] |
| **ToArray** | Método que copia os elementos da coleção para um array. | [[01. ArrayList, referências e operações em coleções#Reorganização, conversão e pesquisa|Reorganização, conversão e pesquisa]] |
| **TrimToSize** | Método que ajusta `Capacity` à quantidade de elementos atualmente armazenados na `ArrayList`. | [[01. ArrayList, referências e operações em coleções#Reorganização, conversão e pesquisa|Reorganização, conversão e pesquisa]] |
| **BinarySearch** | Método de pesquisa binária que retorna a posição encontrada ou um valor negativo quando não encontra o elemento. | [[01. ArrayList, referências e operações em coleções#Reorganização, conversão e pesquisa|Reorganização, conversão e pesquisa]] |
| **Classe** | Tipo que define os dados e comportamentos que seus objetos terão. | [[01. ArrayList, referências e operações em coleções#Classes, objetos e referências|Classes, objetos e referências]] |
| **Objeto** | Instância criada a partir de uma classe. | [[01. ArrayList, referências e operações em coleções#Classes, objetos e referências|Classes, objetos e referências]] |
| **Referência** | Valor armazenado por uma variável de tipo classe para acessar um objeto; variáveis diferentes podem referenciar a mesma instância. | [[01. ArrayList, referências e operações em coleções#Classes, objetos e referências|Classes, objetos e referências]] |
| **IComparer** | Contrato usado para definir como dois objetos devem ser comparados durante ordenação e pesquisa. | [[01. ArrayList, referências e operações em coleções#Ordenação e pesquisa de objetos|Ordenação e pesquisa de objetos]] |
| **PascalCase** | Convenção de nomes em que cada palavra começa com letra maiúscula, usada nos métodos públicos vistos, como `RemoveAt` e `BinarySearch`. | [[01. ArrayList, referências e operações em coleções#Inserção, remoção e consulta|Inserção, remoção e consulta]] |
| **Queue** | Estrutura de fila em que o primeiro elemento inserido é o primeiro a ser removido. | [[02. Queue e Stack (filas, pilhas, FIFO e LIFO)#Queue e Stack representam ordens diferentes|Queue e Stack]] |
| **Stack** | Estrutura de pilha em que o último elemento inserido é o primeiro a ser removido. | [[02. Queue e Stack (filas, pilhas, FIFO e LIFO)#Queue e Stack representam ordens diferentes|Queue e Stack]] |
| **FIFO** | *First In, First Out*: regra em que o primeiro elemento que entra é o primeiro que sai. | [[02. Queue e Stack (filas, pilhas, FIFO e LIFO)#Queue e Stack representam ordens diferentes|Queue e Stack]] |
| **LIFO** | *Last In, First Out*: regra em que o último elemento que entra é o primeiro que sai. | [[02. Queue e Stack (filas, pilhas, FIFO e LIFO)#Queue e Stack representam ordens diferentes|Queue e Stack]] |
| **Enqueue** | Método que insere um objeto no final de uma `Queue`. | [[02. Queue e Stack (filas, pilhas, FIFO e LIFO)#Inserindo e removendo elementos|Inserindo e removendo elementos]] |
| **Dequeue** | Método que remove e retorna o próximo objeto de uma `Queue`. | [[02. Queue e Stack (filas, pilhas, FIFO e LIFO)#Inserindo e removendo elementos|Inserindo e removendo elementos]] |
| **Push** | Método que insere um objeto no topo de uma `Stack`. | [[02. Queue e Stack (filas, pilhas, FIFO e LIFO)#Inserindo e removendo elementos|Inserindo e removendo elementos]] |
| **Pop** | Método que remove e retorna o objeto no topo de uma `Stack`. | [[02. Queue e Stack (filas, pilhas, FIFO e LIFO)#Inserindo e removendo elementos|Inserindo e removendo elementos]] |
| **Peek** | Método que retorna o próximo objeto a ser removido sem removê-lo. | [[02. Queue e Stack (filas, pilhas, FIFO e LIFO)#Consultando a estrutura sem remover|Consultando a estrutura sem remover]] |
| **Hashtable** | Estrutura de dicionário ou mapa que associa chaves a valores e usa uma transformação para determinar onde procurar os dados. | [[03. Hashtable (chave, valor, hashing e colisões)#Chave e valor|Chave e valor]] |
| **Chave** | Identificador usado como ponto de partida para localizar um valor em uma `Hashtable`. | [[03. Hashtable (chave, valor, hashing e colisões)#Chave e valor|Chave e valor]] |
| **Valor** | Dado associado a uma chave dentro de uma `Hashtable`. | [[03. Hashtable (chave, valor, hashing e colisões)#Chave e valor|Chave e valor]] |
| **Função hash** | Transformação que associa uma chave a uma posição da tabela. | [[03. Hashtable (chave, valor, hashing e colisões)#Da chave até uma posição da tabela|Da chave até uma posição da tabela]] |
| **Colisão** | Situação em que mais de um elemento é direcionado para a mesma posição da tabela. | [[03. Hashtable (chave, valor, hashing e colisões)#Colisões|Colisões]] |
| **Colisão primária** | Nome usado no conteúdo para a colisão em que a posição calculada para uma nova inserção já está ocupada. | [[03. Hashtable (chave, valor, hashing e colisões)#Colisões|Colisões]] |
| **ContainsKey** | Método que verifica se uma `Hashtable` contém determinada chave. | [[03. Hashtable (chave, valor, hashing e colisões)#Operações principais|Operações principais]] |
| **ContainsValue** | Método que verifica se uma `Hashtable` contém determinado valor. | [[03. Hashtable (chave, valor, hashing e colisões)#Operações principais|Operações principais]] |
