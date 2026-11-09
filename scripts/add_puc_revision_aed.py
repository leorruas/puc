import json
import os

base_ref = '04. Algoritmos e Estruturas de Dados/'
puc_questions = []

def add_q(id_num, art, topico, dif, enunc, a_txt, b_txt, c_txt, d_txt, corr_idx, da, db, dc, dd, feynman, analise):
    letters = ['A', 'B', 'C', 'D']
    texts = [a_txt, b_txt, c_txt, d_txt]
    diags = [da, db, dc, dd]
    alts = []
    distrators = {}
    for i in range(4):
        is_corr = (i == corr_idx)
        alts.append({
            'letra': letters[i],
            'texto': texts[i],
            'correta': is_corr,
            'diagnostico': diags[i]
        })
        if not is_corr:
            distrators[letters[i]] = diags[i]
            
    puc_questions.append({
        'id': f'AED-REV-{id_num:03d}',
        'disciplina_id': '04',
        'disciplina': 'Algoritmos e Estruturas de Dados',
        'topico': topico,
        'artigo_origem': art,
        'dificuldade': dif,
        'prioritaria': True,
        'origem': 'revisao_oficial_puc',
        'enunciado': enunc,
        'alternativas': alts,
        'explicacao': {
            'modelo_mental': feynman,
            'analise_correta': analise,
            'distratores': distrators,
            'referencia_vault': base_ref + art
        }
    })

raw = [
  # Questão 01
  (1, '02. Queue e Stack (filas, pilhas, FIFO e LIFO).md',
   'Conceitos de lista, pilha e fila (atendimento ordenado)', 'facil',
   'Uma equipe desenvolve um sistema de atendimento em que as solicitações devem ser processadas exatamente na ordem em que foram registradas. Não há prioridades nem necessidade de escolher uma posição intermediária.\n\nQual estrutura representa melhor a regra de atendimento?',
   'Pilha, pois o último elemento inserido é o primeiro retirado.',
   'Fila, pois o primeiro elemento inserido é o primeiro retirado.',
   'Lista sem regra de remoção, pois ela obriga o atendimento por chegada.',
   'Árvore binária, pois a raiz representa necessariamente o primeiro atendimento.',
   1,
   'Incorreto: pilha opera na política LIFO (Last-In, First-Out), desrespeitando a ordem de chegada.',
   'Correto: fila opera na política FIFO (First-In, First-Out), garantindo que a primeira solicitação registrada seja a primeira atendida.',
   'Incorreto: uma lista genérica permite remoção em qualquer posição e não impõe nativamente a disciplina FIFO.',
   'Incorreto: árvores organizam dados hierarquicamente por chave, não por ordem temporal de chegada.',
   'Pense na fila do banco ou da padaria: quem chega primeiro fica na frente e é atendido primeiro (FIFO). Ninguém fura a fila nem é atendido de trás para frente como em uma pilha de pratos.',
   'A estrutura Queue (fila) implementa estritamente a política FIFO (First-In, First-Out), sendo a escolha clássica para filas de atendimento, buffers de mensagens e spool de impressão.'),

  # Questão 02
  (2, '06. Lista linear (array, contador, inserção e remoção).md',
   'Arrays e indexação base zero em C#', 'facil',
   'Uma empresa utiliza um aplicativo em C# para consultar o estoque de cinco produtos. O desenvolvedor recebeu o vetor abaixo e precisa exibir a quantidade referente ao terceiro produto, lembrando que os índices são contados a partir de zero.\n\n```csharp\nint[] estoque = { 8, 3, 6, 2, 9 };\nConsole.WriteLine(/* expressão a ser inserida */);\n```\n\nQual expressão deve substituir o comentário para exibir o valor 6?',
   'estoque[2]',
   'estoque[5]',
   'estoque[3]',
   'estoque[1]',
   0,
   'Correto: em C#, os índices de um array iniciam em 0. Portanto, o 1º elemento está em estoque[0] (8), o 2º em estoque[1] (3) e o 3º em estoque[2] (6).',
   'Incorreto: o índice 5 está fora dos limites de um array de 5 elementos (gera IndexOutOfRangeException).',
   'Incorreto: estoque[3] acessa o 4º elemento (valor 2).',
   'Incorreto: estoque[1] acessa o 2º elemento (valor 3).',
   'Pense nos andares de um elevador no padrão europeu ou na contagem com réguas: você começa marcando o ponto 0. O primeiro item mora no índice 0, o segundo no índice 1 e o terceiro no índice 2.',
   'A indexação 0-based é padrão em C#, C++, Java e JavaScript, calculando o endereço de memória como base + (índice * tamanho_do_tipo).'),

  # Questão 03
  (3, '01. ArrayList, referências e operações em coleções.md',
   'ArrayList e operação de inserção por índice (Insert)', 'medio',
   'Uma equipe automatiza a sequência de conferência de documentos. O código a seguir cria as etapas iniciais; antes da validação, será necessário inserir uma etapa de conferência sem perder nenhuma das demais.\n\n```csharp\nArrayList etapas = new ArrayList();\netapas.Add("Receber");\netapas.Add("Validar");\netapas.Add("Arquivar");\n// Inserir "Conferir" entre "Receber" e "Validar"\n```\n\nQual operação deve ser acrescentada ao código para manter a ordem solicitada?',
   'Chamar `RemoveAt(1)` e depois `Add("Conferir")`.',
   'Adicionar `Conferir` ao final usando `Add`.',
   'Alterar o elemento de índice 1 para `Conferir`.',
   'Usar `Insert(1, "Conferir")`.',
   3,
   'Incorreto: RemoveAt(1) excluiria "Validar" da lista.',
   'Incorreto: Add adiciona ao final da coleção, deixando "Conferir" após "Arquivar".',
   'Incorreto: atribuir etapas[1] = "Conferir" sobrescreveria "Validar", perdendo essa etapa.',
   'Correto: o método Insert(índice, elemento) insere o novo item na posição indicada e desloca os elementos subsequentes ("Validar" e "Arquivar") uma posição à direita.',
   'Inserir com Insert é como abrir espaço na fila de cadeiras: você pede licença para quem está na cadeira 1 dar um passo para trás e senta ali sem expulsar ninguém.',
   'Em listas baseadas em arrays (como ArrayList e List<T>), o método Insert(index, value) tem complexidade O(N) devido ao deslocamento (shift) dos elementos posteriores.'),

  # Questão 04
  (4, '01. ArrayList, referências e operações em coleções.md',
   'Coleções não genéricas e tipagem fraca em ArrayList', 'medio',
   'Em um protótipo C#, a equipe utiliza `ArrayList` para armazenar um código inteiro e, em seguida, uma descrição em texto. Durante a leitura, surgem conversões e verificações adicionais para utilizar os valores.\n\nQual característica da coleção explica essa situação?',
   'ArrayList pode armazenar objetos de tipos diferentes, exigindo cuidados na recuperação.',
   'ArrayList ordena automaticamente todos os elementos por tipo.',
   'ArrayList aceita apenas valores inteiros.',
   'ArrayList só armazena strings e converte automaticamente os inteiros.',
   0,
   'Correto: o ArrayList é uma coleção não genérica que armazena referências do tipo object, permitindo dados heterogêneos mas exigindo coerção de tipo (cast) e unboxing na leitura.',
   'Incorreto: o ArrayList mantém a ordem de inserção, sem ordenação automática por tipo.',
   'Incorreto: o ArrayList aceita qualquer tipo derivado de object (tipos por valor e tipos por referência).',
   'Incorreto: o ArrayList não converte tipos automaticamente para string.',
   'O ArrayList é como uma sacola plástica sem divisórias onde você joga chaves, moedas e maçãs misturadas: você pode guardar tudo junto, mas na hora de puxar precisa olhar para cada objeto para saber o que é.',
   'Essa ausência de segurança em tempo de compilação motivou a introdução dos tipos genéricos (Generics) no .NET 2.0 com List<T>.'),

  # Questão 05
  (5, '02. Queue e Stack (filas, pilhas, FIFO e LIFO).md',
   'Stack e política LIFO (operações Push e Pop)', 'medio',
   'Um editor registra cada modificação em uma pilha para oferecer a funcionalidade Desfazer. Observe a sequência em que três ações são registradas pelo programa.\n\n```csharp\nStack historico = new Stack();\nhistorico.Push("A");\nhistorico.Push("B");\nhistorico.Push("C");\n// Desfazer uma ação\n```\n\nAo executar a operação adequada de remoção, qual ação será recuperada primeiro e por qual método?',
   'A, por `Pop`, pois a pilha segue FIFO.',
   'A, por `Dequeue`.',
   'C, por `Pop`.',
   'B, por `Peek`, que remove o elemento central.',
   2,
   'Incorreto: a pilha segue a disciplina LIFO (Last-In, First-Out), portanto o último elemento inserido (C) é o primeiro a sair, e não A.',
   'Incorreto: Dequeue é operação exclusiva de fila (Queue).',
   'Correto: na pilha, Pop remove e retorna o elemento do topo, que corresponde à ação mais recente adicionada ("C").',
   'Incorreto: Peek não remove elementos e visualiza apenas o topo (C), sem acessar o elemento central B.',
   'Imagine uma pilha de pratos onde você colocou A embaixo, B no meio e C por cima: na hora de lavar ou desfazer, o primeiro prato que sai da pilha é o C que está no topo.',
   'A funcionalidade "Desfazer" (Undo) é o caso de uso clássico de uma pilha (Stack), onde o método Pop() desempilha o estado mais recente em tempo O(1).'),

  # Questão 06
  (6, '02. Queue e Stack (filas, pilhas, FIFO e LIFO).md',
   'Queue e operação de consulta sem remoção (Peek)', 'medio',
   'Na recepção de uma clínica, um painel consulta qual paciente será chamado, mas não deve retirar seu registro da fila antes da confirmação do atendimento. Considere o trecho C#.\n\n```csharp\nQueue pacientes = new Queue();\npacientes.Enqueue("Ana");\npacientes.Enqueue("Bruno");\npacientes.Enqueue("Carla");\n// Exibir o próximo paciente sem remover da fila\n```\n\nQual método deve ser utilizado para obter o próximo paciente sem alterar a fila?',
   '`Dequeue()`',
   '`Clear()`',
   '`Push()`',
   '`Peek()`',
   3,
   'Incorreto: Dequeue() remove e retorna o elemento da frente da fila.',
   'Incorreto: Clear() remove todos os elementos da coleção.',
   'Incorreto: Push() é o método de inserção em pilhas (Stack).',
   'Correto: Peek() retorna o elemento no início da fila sem removê-lo, permitindo consultar quem é o próximo sem alterar o estado da fila.',
   'Peek é como espiar pelo olho mágico da porta para ver quem é a próxima pessoa da fila sem abrir a porta nem mandar ela entrar.',
   'Tanto Queue quanto Stack oferecem o método Peek(), ambos com custo O(1), permitindo inspeção segura antes do consumo efetivo.'),

  # Questão 07
  (7, '03. Hashtable (chave, valor, hashing e colisões).md',
   'Hashtable e acesso direto por chave', 'medio',
   'Um sistema armazena a descrição de serviços por um código único usando `Hashtable`. O usuário informa o código de um serviço e espera recuperar a descrição correspondente, sem percorrer manualmente todas as posições.\n\nQual abordagem está alinhada ao uso dessa estrutura?',
   'Remover necessariamente o último valor antes de efetuar a busca.',
   'Usar a chave informada para acessar o valor associado.',
   'Converter os registros em uma pilha para fazer busca binária.',
   'Buscar somente pela ordem de chegada dos serviços.',
   1,
   'Incorreto: tabelas hash não exigem remoção para consulta.',
   'Correto: a Hashtable mapeia pares chave-valor por meio de uma função hash, permitindo recuperar o valor diretamente através da chave informada (ex.: tabela[codigo]).',
   'Incorreto: pilhas não oferecem busca binária e converter a coleção aumentaria a complexidade.',
   'Incorreto: tabelas hash não preservam a ordem cronológica de chegada dos elementos.',
   'Uma Hashtable é como o guarda-volumes de um clube: você entrega o seu número de chave e o funcionário vai direto no armário correspondente pegar sua bolsa, sem precisar abrir todos os armários um por um.',
   'Acesso por chave em tabelas hash tem custo médio O(1), utilizando o código hash da chave para computar o índice no array interno.'),

  # Questão 08
  (8, '04. Coleções genéricas em C# (List, LinkedList, Queue, Stack e Dictionary).md',
   'Segurança de tipagem em tempo de compilação com List<T>', 'facil',
   'Uma aplicação calcula médias de avaliações e deve impedir que textos sejam misturados aos valores inteiros armazenados. O desenvolvedor vai substituir a declaração genérica indicada no trecho abaixo.\n\n```csharp\n// Declarar aqui uma coleção de inteiros\n// Em seguida, armazenar notas numéricas\n```\n\nQual declaração C# atende à restrição de tipagem exigida pela aplicação?',
   '`List<int> notas = new List<int>();`',
   '`List<string> notas = new List<string>();`',
   '`Dictionary<int,string> notas = new Dictionary<int,string>();`',
   '`ArrayList notas = new ArrayList();`',
   0,
   'Correto: List<int> parametriza a coleção para aceitar exclusivamente números inteiros, impedindo a inserção de strings já em tempo de compilação.',
   'Incorreto: List<string> armazenaria apenas textos, rejeitando números inteiros.',
   'Incorreto: Dictionary<int,string> é um mapa de chave inteira e valor textual, não uma lista sequencial de notas.',
   'Incorreto: ArrayList não é genérica e permite misturar qualquer tipo derivado de object sem restrição estática.',
   'Declarar List<int> é como colocar um gabarito de triângulos na entrada da caixa: só passam peças triangulares (inteiros); qualquer peça redonda (string) é rejeitada na hora de montar.',
   'Coleções genéricas garantem type safety (segurança de tipos) e eliminam o overhead de boxing/unboxing para tipos por valor como int e double.'),

  # Questão 09
  (9, '04. Coleções genéricas em C# (List, LinkedList, Queue, Stack e Dictionary).md',
   'Coleções sequenciais vs. encadeadas (List vs. LinkedList)', 'medio',
   'Uma equipe compara duas coleções genéricas para organizar tarefas. Uma delas utiliza organização sequencial, enquanto a outra é formada por nós encadeados. O objetivo é representar explicitamente a segunda abordagem no C#.\n\nQual coleção está associada a nós encadeados?',
   '`Stack<T>`',
   '`LinkedList<T>`',
   '`List<T>`',
   '`Queue<T>`',
   1,
   'Incorreto: Stack<T> em .NET é implementada internamente sobre um array sequencial redimensionável.',
   'Correto: LinkedList<T> é a implementação padrão da biblioteca .NET de uma lista duplamente encadeada baseada em nós (LinkedListNode<T>).',
   'Incorreto: List<T> é uma lista sequencial baseada em array dinâmico.',
   'Incorreto: Queue<T> em .NET utiliza internamente um buffer circular baseado em array.',
   'Enquanto a List<T> é como uma fileira de cadeiras coladas no chão de um auditório, a LinkedList<T> é como pessoas de mãos dadas em roda: cada pessoa segura a mão da próxima e da anterior.',
   'LinkedList<T> permite inserções e remoções O(1) quando já se possui a referência do nó, mas tem custo O(N) para acesso indexado por não ser contígua na memória.'),

  # Questão 10
  (10, '04. Coleções genéricas em C# (List, LinkedList, Queue, Stack e Dictionary).md',
   'Organização genérica por chave-valor com Dictionary<TKey, TValue>', 'medio',
   'Em uma aplicação de biblioteca, cada exemplar possui um código inteiro e um título textual. A equipe quer uma coleção genérica que permita localizar o título pela chave numérica e tenha tipos explícitos.\n\nQual estrutura atende melhor a essa necessidade?',
   '`Dictionary<int,string>`',
   '`Queue<int>`',
   '`Stack<string>`',
   '`List<string>`',
   0,
   'Correto: Dictionary<TKey, TValue> é uma tabela hash genérica e fortemente tipada que mapeia chaves do tipo int para valores do tipo string.',
   'Incorreto: Queue<int> gerencia apenas uma fila de inteiros sem armazenar os títulos.',
   'Incorreto: Stack<string> armazena títulos em pilha sem indexação por código numérico.',
   'Incorreto: List<string> indexa por posição ordinal sequencial (0, 1, 2...), não por chaves numéricas de catálogo de livros.',
   'O Dictionary<int,string> é como uma agenda de contatos onde o código do livro é o número de telefone e o título é o nome da pessoa: você disca o código e cai direto no título.',
   'O Dictionary genérico substitui a Hashtable tradicional, oferecendo melhor desempenho e eliminando casting na recuperação.'),

  # Questão 11
  (11, '05. Listas lineares e flexíveis, árvores binárias e tabelas hash.md',
   'Tipos abstratos de dados (TAD) e implementação interna', 'medio',
   'Uma equipe usa `List<T>` em C#, mas precisa compreender o que acontece quando sua capacidade de armazenamento se esgota. Ela descobre que a classe pode criar um vetor maior e copiar os elementos anteriores.\n\nQual conclusão relaciona corretamente a coleção pronta ao estudo dos TADs?',
   'Conhecer a interface dispensa entender qualquer efeito das operações sobre a memória.',
   'Todas as listas são necessariamente implementadas com nós encadeados.',
   'Uma lista sequencial não pode aumentar sua capacidade.',
   'Estudar a implementação ajuda a compreender custos e escolhas de uso da coleção.',
   3,
   'Incorreto: entender a alocação e cópia de memória é crucial para evitar gargalos em operações críticas.',
   'Incorreto: listas podem ser sequenciais (arrays) ou flexíveis (nós encadeados).',
   'Incorreto: listas sequenciais dinâmicas aumentam sua capacidade alocando um array novo maior e copiando os dados.',
   'Correto: compreender a mecânica interna do TAD permite ao desenvolvedor antecipar custos de desempenho (como a cópia O(N) no redimensionamento) e tomar decisões arquiteturais fundamentadas.',
   'Dirigir um carro sem saber o que acontece no motor funciona até você exigir demais na serra; entender que a List<T> dobra de tamanho e copia tudo ao encher ajuda a pré-alocar a capacidade necessária e economizar combustível do processador.',
   'O estudo dos TADs conecta a interface pública (o que a coleção faz) à sua estrutura de dados interna (como ela faz e quanto custa em tempo e espaço).'),

  # Questão 12
  (12, '06. Lista linear (array, contador, inserção e remoção).md',
   'Inserção em lista linear sequencial e deslocamento de elementos', 'medio',
   'Em um módulo didático, uma lista sequencial usa um vetor com capacidade para seis inteiros, mas apenas quatro posições estão ocupadas. O sistema deverá inserir 25 entre 20 e 30, preservando a ordem existente.\n\n```csharp\nint[] valores = new int[6] { 10, 20, 30, 40, 0, 0 };\nint quantidade = 4;\nint novoValor = 25;\n// Inserir novoValor no índice 2\n```\n\nConsiderando a capacidade disponível, que operações devem ser executadas antes de concluir a inserção?',
   'Substituir 30 por 25 e manter o contador inalterado.',
   'Reduzir o contador antes da inserção para liberar uma posição.',
   'Inserir 25 no índice 0 sem mover elementos.',
   'Deslocar 30 e 40 uma posição à direita e gravar 25 no índice 2.',
   3,
   'Incorreto: substituir 30 apagaria esse elemento da lista.',
   'Incorreto: reduzir o contador perderia o controle dos elementos existentes.',
   'Incorreto: gravar no índice 0 quebraria a ordem numérica e sobrescreveria o valor 10.',
   'Correto: para inserir no índice 2 preservando todos os itens, os elementos das posições 2 e 3 (30 e 40) devem ser movidos uma posição à direita (para os índices 3 e 4), gravando 25 na posição 2 e incrementando quantidade para 5.',
   'É como abrir espaço numa fileira de cadeiras numeradas: para colocar alguém na cadeira 2, quem está na 3 passa para a 4, quem está na 2 passa para a 3, e a cadeira 2 fica livre para o novo convidado.',
   'O deslocamento em listas lineares deve sempre ser realizado do final para o início (da direita para a esquerda) para não sobrescrever dados.'),

  # Questão 13
  (13, '06. Lista linear (array, contador, inserção e remoção).md',
   'Limite de capacidade e tratamento de overflow em lista sequencial estática', 'medio',
   'Um cadastro utiliza uma lista sequencial didática com vetor de capacidade fixa igual a 4 e contador igual a 4. Chega um novo registro, mas a implementação adotada no exercício não realiza redimensionamento automático.\n\nComo o método de inserção deve tratar esse caso?',
   'Converter implicitamente o vetor em árvore binária.',
   'Reduzir o contador para 3 e sobrescrever automaticamente o último registro.',
   'Gravar o registro diretamente na quinta posição do vetor.',
   'Detectar que a lista está cheia e impedir a inserção segundo a regra adotada.',
   3,
   'Incorreto: tipos estáticos não realizam conversão automática para outras estruturas.',
   'Incorreto: sobrescrever registros existentes causaria perda silenciosa e imprevisível de dados.',
   'Incorreto: tentar gravar no índice 4 de um vetor de tamanho 4 gera IndexOutOfRangeException.',
   'Correto: em listas lineares de capacidade fixa, antes de qualquer inserção deve-se verificar se quantidade == capacidade; se estiver cheia (overflow), a operação deve ser bloqueada ou lançar exceção.',
   'Um ônibus com 4 bancos ocupados por 4 passageiros atingiu a lotação: o motorista não pode empurrar um passageiro pela janela nem criar um 5º banco do nada — ele avisa que o ônibus está cheio.',
   'A verificação prévia de overflow (`n >= array.Length`) é o primeiro teste de guarda em implementações canônicas de listas sequenciais estáticas.'),

  # Questão 14
  (14, '07. Classes autorreferenciais e células encadeadas.md',
   'Classes autorreferenciais e referências de nó', 'medio',
   'Para implementar uma lista encadeada em C#, um estudante cria uma classe `Celula` que guarda um valor inteiro e uma referência para a próxima célula. O último nó deve indicar que não há sucessor.\n\nQual definição de campo expressa a ligação entre células do mesmo tipo?',
   '`bool prox;`',
   '`int prox;`',
   '`string prox;`',
   '`Celula prox;`',
   3,
   'Incorreto: um booleano indica apenas verdadeiro/falso, sem armazenar referências de memória.',
   'Incorreto: um int armazena inteiros, não referências para objetos Celula.',
   'Incorreto: string armazena texto.',
   'Correto: um campo autorreferencial deve ter como tipo a própria classe (`Celula prox;`), permitindo encadear instâncias do mesmo tipo na memória heap ou armazenar null quando não houver próximo.',
   'Uma classe autorreferencial é como uma pessoa estendendo o braço: o campo "prox" é a mão que só pode segurar o ombro de outra pessoa ("Celula"), formando um cordão humano.',
   'Classes autorreferenciais são a base de todas as estruturas dinâmicas em memória: listas encadeadas, pilhas, filas flexíveis, árvores e grafos.'),

  # Questão 15
  (15, '08. Lista flexível (nó cabeça, inserção, remoção e percurso).md',
   'Lista flexível e o papel da célula sentinela (nó cabeça)', 'medio',
   'Uma implementação de lista flexível utiliza uma célula inicial vazia, apontada por `primeiro`, enquanto os valores reais aparecem nas células seguintes. A equipe contabiliza os registros e percebe que essa célula inicial não deve ser exibida como dado.\n\nQual é a função dessa célula inicial?',
   'Substituir a referência para o último nó em todas as operações.',
   'Atuar como sentinela, simplificando o tratamento de operações e da lista vazia.',
   'Guardar obrigatoriamente o maior valor armazenado.',
   'Garantir que todos os dados permaneçam contíguos em um vetor.',
   1,
   'Incorreto: o ponteiro `ultimo` continua sendo utilizado para apontar para o final da lista.',
   'Correto: a célula cabeça (sentinela) garante que a lista nunca tenha ponteiro `primeiro` nulo, eliminando casos especiais de verificação de lista vazia ou inserção/remoção no primeiro elemento.',
   'Incorreto: a célula cabeça não armazena dados de negócio nem o maior valor.',
   'Incorreto: listas flexíveis alocam nós dispersos na memória heap através de referências.',
   'A célula cabeça é como a locomotiva vazia de um trem de passageiros: ela não carrega passageiros, mas garante que os vagões sempre tenham onde se engatar, mesmo quando não há nenhum passageiro no trem.',
   'O padrão de sentinela é amplamente utilizado na literatura de estruturas de dados (como em Cormen e na tradição da PUC Minas) para reduzir ramificações condicionais (`if/else`) no código.'),

  # Questão 16
  (16, '08. Lista flexível (nó cabeça, inserção, remoção e percurso).md',
   'Remoção de nó intermediário em lista simplesmente encadeada', 'dificil',
   'Uma lista simplesmente encadeada armazena três códigos na ordem 5, 10 e 15. No procedimento de exclusão, o nó de valor 10 deve deixar de fazer parte do encadeamento, mas os outros dois precisam permanecer acessíveis.\n\n```csharp\nclass Celula\n{\n    public int valor;\n    public Celula prox;\n}\n// cel5.prox = cel10;\n// cel10.prox = cel15;\n```\n\nQual atualização de referência remove corretamente o nó intermediário dessa lista?',
   'Mover todos os elementos para um novo vetor obrigatoriamente.',
   'Fazer a célula de 15 apontar para o nó cabeça, mantendo todas as outras ligações.',
   'Fazer a referência `prox` da célula de 5 apontar para a célula de 15.',
   'Eliminar apenas o valor numérico 10 sem alterar as referências.',
   2,
   'Incorreto: listas encadeadas não exigem realocação de vetores para remoção.',
   'Incorreto: fazer 15 apontar para a cabeça criaria um ciclo indevido.',
   'Correto: atualizando `cel5.prox = cel10.prox` (ou seja, `cel5.prox = cel15`), o nó intermediário cel10 é contornado e desvinculado da cadeia, ficando elegível para a coleta pelo Garbage Collector.',
   'Incorreto: zerar o valor numérico manteria o nó 10 na cadeia, apenas com conteúdo vazio.',
   'Para tirar o vagão 10 do meio do trem, você desengata o vagão 5 do vagão 10 e engata o vagão 5 diretamente no vagão 15. O vagão 10 fica solto no pátio e o trem continua rodando.',
   'Em listas simplesmente encadeadas, a remoção de um nó requer acesso ao seu predecessor, permitindo que a operação de desvio de ponteiro ocorra em tempo O(1).'),

  # Questão 17
  (17, '09. Árvore binária de pesquisa (estrutura, busca e operações).md',
   'Pesquisa e navegação por comparação em Árvore Binária de Busca (ABB)', 'medio',
   'Um sistema utiliza uma árvore binária de busca para localizar produtos. A raiz contém 40, seu filho esquerdo contém 20 e o direito contém 60. O procedimento de busca compara o código procurado com cada nó visitado.\n\n```csharp\nint chaveBuscada = 15;\nint raiz = 40;\nint filhoEsquerdo = 20;\nint filhoDireito = 60;\n// Escolher o ramo a visitar a partir das comparações\n```\n\nQuais decisões de navegação são adequadas no início da busca pela chave 15?',
   'Percorrer obrigatoriamente toda a árvore antes de comparar.',
   'Começar por 60 porque é maior que a raiz.',
   'Consultar primeiro o maior valor armazenado, independentemente da chave.',
   'Partir de 40 para 20, prosseguindo à esquerda de 20.',
   3,
   'Incorreto: a ABB descarta metade dos nós a cada comparação, não exigindo visita exaustiva.',
   'Incorreto: 15 é menor que 40, portanto a subárvore direita (60) é descartada.',
   'Incorreto: a busca em ABB sempre se inicia pela raiz.',
   'Correto: como 15 < 40, navega-se para a subárvore esquerda (nó 20); em seguida, como 15 < 20, prossegue-se para a subárvore esquerda de 20.',
   'Uma ABB funciona como o jogo de adivinhar um número: se você pensou no 15 e a raiz chuta 40, você diz "é menor!" e descarta todos os números maiores que 40 de uma vez.',
   'A propriedade fundamental da ABB estabelece que todos os nós da subárvore esquerda são menores que a raiz e todos da subárvore direita são maiores, viabilizando busca com custo médio O(log N).'),

  # Questão 18
  (18, '09. Árvore binária de pesquisa (estrutura, busca e operações).md',
   'Caminhamento em-ordem (in-order) em Árvore Binária de Busca', 'medio',
   'Uma árvore binária de busca tem raiz 8, filho esquerdo 4 e filho direito 12. Um relatório deve apresentar os valores em ordem crescente, utilizando o caminhamento correspondente.\n\nQual sequência será produzida pelo percurso em ordem (esquerda, raiz, direita)?',
   '4, 12, 8',
   '8, 4, 12',
   '12, 8, 4',
   '4, 8, 12',
   3,
   'Incorreto: 4, 12, 8 visita esquerda, direita, raiz (pós-ordem).',
   'Incorreto: 8, 4, 12 visita raiz, esquerda, direita (pré-ordem).',
   'Incorreto: 12, 8, 4 é a ordem decrescente.',
   'Correto: o caminhamento central/em-ordem (in-order) visita recursivamente a subárvore esquerda (4), a raiz (8) e a subárvore direita (12), resultando na sequência ordenada crescente 4, 8, 12.',
   'O percurso em-ordem é como ler uma partitura ou frase ocidental: você lê primeiro o que está à esquerda, depois o centro e depois a direita, gerando a ordem natural crescente dos números.',
   'Uma das propriedades mais elegantes da ABB é que o caminhamento in-order produz os elementos rigorosamente ordenados em complexidade O(N).'),

  # Questão 19
  (19, '09. Árvore binária de pesquisa (estrutura, busca e operações).md',
   'Inserção ordenada em Árvore Binária de Busca', 'medio',
   'Em uma árvore binária de busca com raiz 30 e filho esquerdo 10, um aplicativo deve inserir a chave 20. O procedimento compara sucessivamente a chave nova com os nós visitados.\n\nEm qual posição a chave 20 deve ser inserida?',
   'Como novo filho esquerdo do nó 10.',
   'Substituindo a raiz 30.',
   'Como filho direito do nó 10.',
   'Como novo filho direito da raiz 30.',
   2,
   'Incorreto: 20 é maior que 10, portanto não pode ficar à esquerda de 10.',
   'Incorreto: inserções em ABB não sobrescrevem nós já existentes.',
   'Correto: compara-se 20 com 30 -> como 20 < 30, desce para o nó 10; compara-se 20 com 10 -> como 20 > 10 e o filho direito de 10 é nulo, insere-se 20 como filho direito de 10.',
   'Incorreto: 20 é menor que 30, violando a regra da subárvore direita.',
   'A chave 20 desce pelo funil da árvore: bate no 30 e vai para a esquerda; bate no 10 e vai para a direita, encaixando na folha direita do 10.',
   'A inserção em ABB sempre ocorre em nós folha (ou posições nulas), preservando a invariante de ordenação em todos os nós.'),

  # Questão 20
  (20, '09. Árvore binária de pesquisa (estrutura, busca e operações).md',
   'Remoção de nó com dois filhos em Árvore Binária de Busca', 'dificil',
   'Um sistema mantém uma árvore binária de busca e precisa remover um nó que possui dois filhos. A equipe deseja preservar a propriedade de que as chaves menores ficam à esquerda e as maiores à direita.\n\nQual estratégia é compatível com a remoção desse nó?',
   'Apagar toda a subárvore esquerda sem examinar os valores.',
   'Trocar o nó removido por qualquer folha aleatória sem considerar a ordenação.',
   'Substituir sua chave por uma chave adequada do predecessor ou sucessor em ordem e ajustar a árvore.',
   'Manter seus dois filhos apontando para um nó inexistente.',
   2,
   'Incorreto: apagar a subárvore destruiria registros válidos.',
   'Incorreto: escolher uma folha qualquer violaria imediatamente a propriedade de ordenação da ABB.',
   'Correto: localiza-se o predecessor em ordem (o maior valor da subárvore esquerda) ou o sucessor em ordem (o menor valor da subárvore direita), copia-se seu valor para o nó a ser removido e deleta-se recursivamente aquele predecessor/sucessor (que tem no máximo um filho).',
   'Incorreto: ponteiros nulos ou inválidos deixariam os filhos órfãos e inacessíveis.',
   'Se o presidente da empresa sai e tem dois diretores embaixo, você não pode colocar um estagiário qualquer no lugar: você promove o maior líder da esquerda (predecessor) ou o menor da direita (sucessor), mantendo toda a hierarquia em perfeita harmonia.',
   'O caso de remoção de nó com 2 filhos é o mais complexo em ABB, resolvido elegantemente pela substituição pelo predecessor ou sucessor simétrico.'),

  # Questão 21
  (21, '10. Árvores AVL (balanceamento e rotações).md',
   'Árvores AVL e rotação simples à direita (desbalanceamento LL)', 'dificil',
   'Ao implementar uma árvore AVL para um catálogo, um estudante insere três chaves sucessivamente. A inserção resulta em um desequilíbrio no ramo esquerdo do nó 30, sendo necessário restaurar o balanceamento sem modificar a relação de ordem.\n\n```csharp\nInserir(30);\nInserir(20);\nInserir(10);\n// Reequilibrar a árvore AVL após a terceira inserção\n```\n\nQual rotação é adequada para corrigir o desequilíbrio produzido por essa sequência?',
   'Trocar as chaves 10 e 30 sem alterar os vínculos.',
   'Rotação simples à esquerda em 30.',
   'Rotação simples à direita em 30.',
   'Remover a chave 20 obrigatoriamente.',
   2,
   'Incorreto: trocar valores sem rotacionar ponteiros não restaura as propriedades da AVL.',
   'Incorreto: rotação à esquerda é aplicada em desbalanceamentos do tipo Direita-Direita (RR).',
   'Correto: a sequência 30 -> 20 -> 10 gera uma linha inclinada à esquerda (caso Esquerda-Esquerda / LL), fazendo com que o fator de balanceamento de 30 fique +2 (ou -2 conforme a convenção). A correção é uma rotação simples à direita no nó 30, tornando 20 a nova raiz com 10 à esquerda e 30 à direita.',
   'Incorreto: árvores balanceadas ajustam ponteiros sem descartar chaves inseridas.',
   'A árvore ficou parecendo uma vara de pescar inclinada para a esquerda (30 -> 20 -> 10): você dá um puxão no nó do meio (20) para cima e gira o 30 para a direita, transformando a vara torta em um triângulo equilibrado.',
   'A árvore AVL garante fator de balanceamento entre -1 e +1 em todos os nós, restaurando a altura O(log N) via rotações simples (LL, RR) ou duplas (LR, RL).'),

  # Questão 22
  (22, '11. Tabela hash (função de transformação e tratamento de colisões).md',
   'Colisão em tabela hash e estratégias de tratamento', 'medio',
   'Um cadastro usa uma função de dispersão para calcular o índice de armazenamento de cada cliente. Ao testar duas chaves diferentes, o desenvolvedor observa que elas produzem o mesmo índice.\n\n```csharp\nint Tamanho = 10;\nint indiceA = 21 % Tamanho;\nint indiceB = 31 % Tamanho;\n// Ambos os índices recebem o valor 1\n```\n\nComo é denominada a situação observada e qual providência a implementação deve adotar para preservar ambos os registros?',
   'Ordenação em fila; remover o cliente que chegou primeiro.',
   'Colisão; aplicar uma estratégia de tratamento, como sondagem ou encadeamento.',
   'Encadeamento obrigatório de todas as posições; eliminar a função hash.',
   'Balanceamento; realizar sempre uma rotação à direita.',
   1,
   'Incorreto: não se trata de fila e não se deve descartar registros existentes.',
   'Correto: quando duas chaves distintas resultam no mesmo índice na tabela hash, ocorre uma colisão; a estrutura deve tratá-la via endereçamento aberto (sondagem linear, quadrática ou hash duplo) ou encadeamento externo (listas encadeadas em cada posição).',
   'Incorreto: eliminar a função hash destruiria o próprio conceito de tabela hash.',
   'Incorreto: rotação é mecanismo de árvores balanceadas (AVL/Rubro-Negra), não de tabelas hash.',
   'Colisão é quando duas pessoas compram ingressos e recebem o número da mesma poltrona no teatro: você não joga ninguém fora — você aplica uma regra combinada (como sentar na cadeira livre seguinte [sondagem] ou colocar cadeiras extras na fileira [encadeamento]).',
   'Devido ao Princípio da Casa dos Pombos, colisões são matematicamente inevitáveis quando o conjunto de chaves possíveis é maior que o tamanho da tabela, exigindo algoritmo de resolução de colisões.'),

  # Questão 23
  (23, '11. Tabela hash (função de transformação e tratamento de colisões).md',
   'Eficiência de tabelas hash, dispersão uniforme e fator de carga', 'dificil',
   'Uma organização decide utilizar tabela hash porque espera consultas rápidas aos registros. Entretanto, em testes, várias chaves acabam na mesma posição e algumas buscas exigem comparações adicionais.\n\nQual avaliação técnica é mais adequada?',
   'A ordem de inserção sempre define o custo da busca, como em uma fila.',
   'A eficiência próxima de tempo constante depende de boa dispersão e tratamento apropriado das colisões.',
   'Toda pesquisa em hash realiza necessariamente uma única comparação, mesmo com colisões.',
   'A estrutura deixa automaticamente de funcionar quando ocorre uma colisão.',
   1,
   'Incorreto: o custo em hash não decorre da ordem cronológica de inserção.',
   'Correto: o tempo O(1) de uma tabela hash é uma média que depende de uma função hash de boa qualidade (que distribua uniformemente as chaves) e de um baixo fator de carga; caso haja muitas colisões agrupadas, o custo pode degradar para O(N).',
   'Incorreto: ao colidir, a busca precisa percorrer a lista de encadeamento ou saltos de sondagem, realizando comparações adicionais.',
   'Incorreto: tabelas hash são desenhadas exatamente para continuar funcionando perfeitamente mesmo na presença de colisões.',
   'Uma tabela hash é como um estacionamento com 100 vagas: se o manobrista espalha os carros igualmente (boa dispersão), você acha seu carro num piscar de olhos (O(1)); mas se ele empilhar todos os 100 carros na vaga número 1 (má dispersão), você terá que revirar a pilha toda para achar a sua chave (degradação O(N)).',
   'O dimensionamento correto da tabela e funções hash de dispersão uniforme (como MurmurHash ou multiplicações primas) garantem que a média permaneça próxima de O(1).')
]

for item in raw:
    add_q(*item)

print(f"Generated {len(puc_questions)} official PUC revision questions for AED.")

# Load existing AED file
aed_path = os.path.join('/home/antigravity/leorruas/puc/banco-de-questoes', '04.algoritmos-e-estruturas-de-dados.json')
with open(aed_path, 'r', encoding='utf-8') as f:
    existing_aed = json.load(f)

print(f"Existing AED questions: {len(existing_aed)}")

# Ensure existing ones have prioritaria: False and origem: 'banco_sintetico_vault' if not set
for eq in existing_aed:
    if 'prioritaria' not in eq:
        eq['prioritaria'] = False
    if 'origem' not in eq:
        eq['origem'] = 'banco_sintetico_vault'

# Check if any AED-REV questions already exist
existing_ids = {q['id'] for q in existing_aed}
new_to_add = [q for q in puc_questions if q['id'] not in existing_ids]

# Prepend priority questions to the list so they appear first!
merged_aed = puc_questions + [q for q in existing_aed if not q['id'].startswith('AED-REV-')]

with open(aed_path, 'w', encoding='utf-8') as f:
    json.dump(merged_aed, f, ensure_ascii=False, indent=2)

print(f"Total questions in {aed_path} after prepend: {len(merged_aed)}")
