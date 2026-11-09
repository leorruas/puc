import json

base_ref = '01. Programacao Modular/'
questions = []

def q(id_num, art, topico, dif, enunc, a_txt, b_txt, c_txt, d_txt, corr_idx, da, db, dc, dd, feynman, analise):
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
            
    questions.append({
        'id': f'PM-{id_num:03d}',
        'disciplina_id': '01',
        'disciplina': 'Programação Modular',
        'topico': topico,
        'artigo_origem': art,
        'dificuldade': dif,
        'enunciado': enunc,
        'alternativas': alts,
        'explicacao': {
            'modelo_mental': feynman,
            'analise_correta': analise,
            'distratores': distrators,
            'referencia_vault': base_ref + art
        }
    })

# 01
q(1, '01. Introdução à programação modular.md', 'Decomposição modular e limites cognitivos', 'medio',
  'Na engenharia de software e na programação modular, qual é o principal objetivo da decomposição de um sistema complexo em módulos autônomos e bem delimitados?',
  'Permitir que o compilador elimine a verificação de tipos em runtime para acelerar a execução.',
  'Reduzir a carga cognitiva do desenvolvedor (princípio de Miller: 7 +- 2 elementos), permitindo compreender, testar e manter cada parte isoladamente sem depender do todo simultâneo.',
  'Obrigar o uso de variáveis globais para agilizar o compartilhamento de dados na memória RAM.',
  'Evitar a divisão de tarefas em equipes ágeis, centralizando toda a lógica em um único arquivo de código-fonte monolítico.',
  1,
  'Erro conceitual: compilação estática com verificação de tipos é reforçada pela modularidade, não eliminada.',
  'Correto: a decomposição modular permite gerenciar a complexidade respeitando os limites da cognição humana.',
  'Erro conceitual: variáveis globais quebram a modularidade ao gerar acoplamento espúrio e imprevisibilidade.',
  'Erro absurdo: modularização viabiliza o trabalho paralelo em equipe e a manutenibilidade do código.',
  'Dividir um programa em módulos é como organizar uma oficina com gavetas identificadas: em vez de revirar uma pilha caótica de ferramentas, você abre apenas a gaveta necessária para aquele conserto específico.',
  'A modularização combate a explosão de complexidade ao dividir o sistema em subsistemas com alta coesão e baixo acoplamento.')

q(2, '01. Introdução à programação modular.md', 'Critérios de Meyer para modularidade', 'dificil',
  'Segundo Bertrand Meyer em seu tratado sobre construção de software orientado a objetos, quais são os cinco critérios fundamentais para avaliar a modularidade de uma arquitetura?',
  'Decomponibilidade, componibilidade, compreensibilidade, continuidade e proteção modular.',
  'Polimorfismo estático, herança múltipla, garbage collection, reflexão e compilação JIT.',
  'Normalização em 1FN, 2FN, 3FN, Boyce-Codd e chave primária composta.',
  'Conexão TCP, enlace Ethernet, roteamento IP, encapsulamento e multiplexação.',
  0,
  'Correto: os 5 critérios canônicos de modularidade estabelecidos por Meyer (1988/1997).',
  'Erro taxonômico: esses itens são recursos de linguagens e runtimes, não critérios conceituais de modularidade de Meyer.',
  'Erro de disciplina: essas são formas normais de modelagem de banco de dados relacional.',
  'Erro de disciplina: esses são conceitos de arquitetura de redes de computadores.',
  'Os critérios de Meyer são como normas de engenharia para peças de Lego: você deve poder separar em blocos (decomponibilidade), montar blocos novos (componibilidade), entender cada bloco sozinho (compreensibilidade), trocar um bloco sem quebrar o castelo inteiro (continuidade) e evitar que um defeito em um bloco destrua os outros (proteção).',
  'Meyer definiu esses 5 critérios para guiar o design de sistemas modulares verdadeiramente extensíveis e robustos.')

# 02
q(3, '02. Funções e procedimentos.md', 'Efeitos colaterais e transparência referencial', 'medio',
  'Qual é a diferença conceitual e semântica essencial entre um procedimento (procedure) e uma função pura (pure function)?',
  'Funções puras sempre alteram o estado de variáveis globais e de banco de dados; procedimentos nunca retornam valores e nunca produzem efeitos colaterais.',
  'Procedimentos executam sequências de comandos com objetivo primordial de produzir efeitos colaterais de estado; funções puras calculam e retornam um valor dependente exclusivamente de seus parâmetros, com transparência referencial.',
  'Procedimentos são compilados em código de máquina; funções são interpretadas em JavaScript sem otimização.',
  'Não há nenhuma diferença técnica, tratando-se apenas de preferências estéticas de nomenclatura entre desenvolvedores.',
  1,
  'Erro inverso: funções puras evitam efeitos colaterais; procedimentos atuam via mutação de estado.',
  'Correto: procedimentos alteram estados; funções puras preservam a transparência referencial (mesma entrada = mesma saída).',
  'Erro conceitual: procedimentos e funções são compilados de forma idêntica pelo compilador de linguagens modernas como C#.',
  'Erro conceitual grave: a distinção entre computação orientada a estado (procedural) e transformações de valores (funcional) é basilar na ciência da computação.',
  'Uma função pura é como uma calculadora matemática: você digita 2 + 2 e ela sempre devolve 4 sem alterar nada na sua casa. Um procedimento é como apertar o botão de ligar a cafeteira: não te dá um número, mas altera o mundo real esquentando a água.',
  'Funções puras garantem determinismo, testabilidade e paralelização segura, enquanto procedimentos comandam mutações no sistema.')

q(4, '02. Funções e procedimentos.md', 'Passagem de parâmetros em C#', 'dificil',
  'Em C#, o que ocorre internamente na memória quando uma variável do tipo primitivo int é passada para um método com o modificador ref em comparação com a passagem padrão sem modificador?',
  'Na passagem padrão, copia-se o valor contido na variável para a pilha do método chamado; com ref, passa-se o próprio endereço de memória da variável original, permitindo mutação direta.',
  'Com ref, o runtime aloca o valor na heap gerenciada transformando o int compulsoriamente em um objeto da classe String.',
  'Sem modificador, qualquer alteração dentro do método reflete automaticamente na variável original do chamador.',
  'O modificador ref é apenas um comentário decorativo ignorado pelo compilador C# em modo Release.',
  0,
  'Correto: por padrão tipos de valor são passados por cópia; o modificador ref passa a referência de memória (endereço).',
  'Erro taxonômico: o modificador ref não realiza boxing em String nem aloca o tipo de valor na heap.',
  'Erro conceitual: a passagem por valor isola a variável original contra alterações feitas dentro do escopo do método.',
  'Erro técnico: ref altera a assinatura da instrução IL (emissão de ponteiro gerenciado &).',
  'Passagem por valor é como enviar uma fotocópia de uma folha de caderno: a pessoa pode rabiscar a cópia que o original fica intacto. Passagem por ref é entregar o próprio caderno original na mão da pessoa.',
  'C# diferencia passagem de tipos de valor por valor (cópia) e por referência explícita (ponteiro gerenciado via ref, out ou in).')

# 03
q(5, '03. Tipos abstratos de dados.md', 'Invariantes de classe e integridade de TAD', 'medio',
  'O que caracteriza a invariante de uma classe em um Tipo Abstrato de Dados (TAD)?',
  'Uma condição ou regra de consistência de negócio que deve ser estritamente verdadeira em todo estado estável do objeto (após a conclusão do construtor e de qualquer método público).',
  'Uma variável global estática que nunca pode ter seu valor lido por nenhum módulo externo.',
  'Uma diretiva do compilador que impede a criação de mais de uma instância da classe na aplicação.',
  'Um método que é executado compulsoriamente a cada milissegundo pelo thread de segundo plano.',
  0,
  'Correto: a invariante é o contrato interno de sanidade que o objeto se compromete a manter intacto durante todo o seu ciclo de vida.',
  'Erro conceitual: confunde invariante de integridade com variável estática protegida.',
  'Erro conceitual: confunde invariante com o padrão Singleton de criação.',
  'Erro conceitual: invariantes são asserções lógicas de consistência, não timers de execução de tarefas.',
  'A invariante é como a regra biológica da temperatura do corpo humano: o corpo pode suar, tremer ou se alimentar, mas no final de qualquer ação ele precisa manter a temperatura em torno de 36,5°C para continuar vivo.',
  'O encapsulamento existe primordialmente para proteger as invariantes de um TAD contra corrupções causadas por clientes externos.')

q(6, '03. Tipos abstratos de dados.md', 'Vazamento de representação em TADs', 'dificil',
  'Em uma classe C# Agenda que encapsula internamente uma coleção privada List de compromissos, qual implementação de propriedade ou método configura um clássico vazamento de representação (representation exposure)?',
  'Expor o método ObterCompromissos() devolvendo uma visão somente-leitura através de AsReadOnly().',
  'Expor uma propriedade pública que devolve a referência direta à lista interna mutável List.',
  'Expor o método Adicionar() que valida conflitos de horário antes de inserir o novo compromisso.',
  'Declarar o campo interno com modificador private readonly.',
  1,
  'Boa prática: expõe apenas uma visão somente-leitura, protegendo a coleção interna contra modificações externas.',
  'Correto: entregar a referência da coleção privada permite que clientes externos façam Clear(), quebrando invariantes sem que a classe saiba.',
  'Comportamento correto de um TAD que protege o estado interno com validações.',
  'Boa prática: protege a referência interna contra reatribuição acidental.',
  'Entregar a lista privada mutável é como trancar a porta da frente da sua casa com senha eletrônica, mas entregar a chave mestra de todas as portas dos fundos para qualquer estranho na rua.',
  'Vazamento de representação ocorre quando referências a objetos mutáveis internos são devolvidas a clientes, permitindo quebrar invariantes sem passar pela API da classe.')

# 04
q(7, '04. Programação orientada a objetos e acoplamento.md', 'Acoplamento aferente vs eferente', 'dificil',
  'Na análise estrutural de acoplamento entre classes e módulos de software, qual é a distinção exata entre acoplamento aferente (Ca) e acoplamento eferente (Ce)?',
  'Acoplamento aferente mede quantos módulos externos dependem do módulo em questão; acoplamento eferente mede de quantos módulos externos o módulo em questão depende.',
  'Acoplamento aferente é medido em megabytes de memória consumida; acoplamento eferente é medido em gigahertz da CPU.',
  'Acoplamento aferente só ocorre em herança de classes; acoplamento eferente só ocorre em polimorfismo de interface.',
  'Acoplamento aferente mede o número de bugs de sintaxe; acoplamento eferente mede o tempo de compilação.',
  0,
  'Correto: Ca (responsabilidade/centralidade: quem aponta para mim) vs. Ce (instabilidade/dependência: para quem eu aponto).',
  'Erro de categoria: acoplamento é métrica estrutural e relacional de design de software, não consumo de hardware.',
  'Erro conceitual: ambos aplicam-se a qualquer tipo de dependência de código (composição, parâmetros, retorno, herança).',
  'Erro taxonômico: métricas de qualidade de design não se confundem com contagem de erros de compilação.',
  'Pense em uma celebridade: ela tem milhões de seguidores (alto acoplamento aferente - muita gente depende do que ela fala), mas ela segue apenas 3 perfis (baixo acoplamento eferente - ela depende de quase ninguém para viver).',
  'As métricas de Robert C. Martin definem estabilidade com base no equilíbrio entre quem depende do módulo e de quem ele depende.')

q(8, '04. Programação orientada a objetos e acoplamento.md', 'Acoplamento de conteúdo vs acoplamento de dados', 'medio',
  'Na taxonomia clássica de tipos de acoplamento (Myers/Page-Jones), qual das seguintes opções representa o tipo de acoplamento mais danoso (pior nível) e qual o mais desejável?',
  'O pior é o acoplamento de dados; o mais desejável é o acoplamento de conteúdo.',
  'O pior é o acoplamento de conteúdo (um módulo modifica diretamente dados internos de outro); o mais desejável é o acoplamento de dados (módulos comunicam-se passando apenas parâmetros atômicos necessários).',
  'O pior é o acoplamento por interface; o mais desejável é o acoplamento por herança múltipla irrestrita.',
  'Todos os tipos de acoplamento têm o mesmo impacto na manutenibilidade de um sistema.',
  1,
  'Erro inverso: acoplamento de dados é o mais limpo e saudável; conteúdo é o pior.',
  'Correto: acoplamento de conteúdo destrói o encapsulamento, enquanto acoplamento de dados promove modularidade estrita.',
  'Erro conceitual: acoplamento por interface abstrata é excelente e recomendado na arquitetura de software.',
  'Erro conceitual: o espectro de acoplamento é amplamente documentado como fator crítico na manutenibilidade.',
  'Acoplamento de conteúdo é como um vizinho entrar na sua cozinha sem bater e mudar os ingredientes da sua receita enquanto você cozinha. Acoplamento de dados é ele tocar a campainha e pedir educadamente uma xícara de açúcar.',
  'O acoplamento deve ser minimizado, preferindo passagens de dados explícitas e desacoplamento via contratos.')

# 05
q(9, '05. Fatores externos de qualidade de software.md', 'Fatores externos de Bertrand Meyer', 'medio',
  'No modelo de qualidade de Bertrand Meyer, fatores externos são aqueles perceptíveis diretamente pelos usuários finais do software. Qual dos seguintes pares representa exclusivamente fatores externos?',
  'Corretitude e Robustez.',
  'Coesão e Baixo Acoplamento.',
  'Complexidade Ciclomática e Profundidade da Árvore de Herança.',
  'Indentação de código e comentários no cabeçalho.',
  0,
  'Correto: corretitude (fazer exatamente o que foi especificado) e robustez (comportamento adequado sob condições anormais) são qualidades externas primordiais.',
  'Erro conceitual: coesão e acoplamento são fatores internos, perceptíveis apenas pelos desenvolvedores que mantêm o código.',
  'Erro conceitual: métricas de código (métrica de McCabe e DIT) são fatores internos.',
  'Erro de estilo: formatação de texto e comentários são propriedades internas do código-fonte.',
  'Fatores externos são como a segurança dos freios e a economia de combustível de um carro (o motorista sente no uso); fatores internos são a disposição ordenada dos cabos dentro do motor (só o mecânico vê na revisão).',
  'Meyer separa rigorosamente qualidades externas (que justificam o software) e internas (que viabilizam as externas ao longo do tempo).')

q(10, '05. Fatores externos de qualidade de software.md', 'Corretitude vs. Robustez', 'dificil',
  'Na formalização de Bertrand Meyer, como se diferenciam com precisão matemática os conceitos de Corretitude e Robustez?',
  'Corretitude é a capacidade do software funcionar sob hardware defeituoso; Robustez é a conformidade formal com o manual de design visual.',
  'Corretitude é a capacidade de executar exatamente de acordo com a especificação formal sob condições normais previstas; Robustez é a capacidade de reagir adequadamente quando ocorrem condições anormais fora da especificação.',
  'Corretitude só se aplica a linguagens dinâmicas; Robustez só se aplica a linguagens estáticas compiladas.',
  'Ambas são idênticas e avaliadas unicamente pelo tempo médio de resposta de ping em rede.',
  1,
  'Erro inverso e conceitual sobre especificações e hardware.',
  'Correto: corretitude trata do domínio das entradas especificadas; robustez trata de entradas imprevistas e falhas de ambiente.',
  'Erro de categoria: conceitos teóricos de engenharia de software independentes de tipagem da linguagem.',
  'Erro de disciplina: métrica de rede não define correção lógica de software.',
  'Corretitude é um avião decolar e pousar perfeitamente no dia de céu claro previsto no plano de voo; Robustez é o piloto conseguir planar e pousar com segurança mesmo se um raio atingir uma asa no meio de uma tempestade imprevista.',
  'A corretitude exige prova ou teste de aderência contratual; a robustez exige tratamento de exceções, tolerância a falhas e degradação graciosa.')

# 06
q(11, '06. Fatores internos de qualidade de software.md', 'Modularidade como viabilizadora de fatores internos', 'medio',
  'Qual é a relação fundamental entre os fatores internos de qualidade (como legibilidade, modularidade e testabilidade) e os fatores externos de qualidade de um sistema?',
  'Fatores internos são irrelevantes em projetos comerciais, pois clientes só pagam por interfaces gráficas atraentes.',
  'Fatores internos constituem o meio essencial pelo qual os desenvolvedores conseguem alcançar e sustentar os fatores externos (manutenibilidade, extensibilidade e robustez) a médio e longo prazo.',
  'Fatores internos reduzem a performance de execução em runtime porque o processador precisa ler comentários no disco.',
  'Fatores internos eliminam a necessidade de testes de regressão automatizados.',
  1,
  'Erro mercadológico grave: código interno de má qualidade torna a evolução inviável e gera falhas externas constantes.',
  'Correto: qualidades internas excelentes são a fundação estrutural para a entrega de qualidades externas duradouras.',
  'Erro técnico grosseiro: compiladores removem comentários e otimizam código; legibilidade interna não degrada CPU.',
  'Erro conceitual: código modular facilita testes automatizados, nunca os elimina.',
  'Se você construir uma casa com tijolos tortos e canos furados escondidos dentro da parede (fatores internos ruins), a pintura bonita da fachada (fator externo) vai desmoronar na primeira chuva forte.',
  'A qualidade interna garante que o software não se transforme em uma massa rígida, frágil e imóvel com o passar do tempo.')

q(12, '06. Fatores internos de qualidade de software.md', 'Extensibilidade e Reusabilidade', 'medio',
  'Dentre os fatores internos descritos na engenharia de software, o que distingue o conceito de Reusabilidade da Extensibilidade?',
  'Reusabilidade é a capacidade de usar módulos em aplicações distintas para as quais não foram originalmente concebidos; Extensibilidade é a facilidade de adaptar o software a mudanças nas suas próprias especificações.',
  'Reusabilidade exige sempre herança múltipla; Extensibilidade só pode ser atingida com código estático procedural.',
  'Reusabilidade mede o consumo de memória RAM; Extensibilidade mede o tamanho do disco rígido.',
  'Não há distinção, pois ambos referem-se à velocidade de inicialização do executável.',
  0,
  'Correto: distinção clássica de Meyer entre reaproveitar blocos em novos contextos (reuso) vs. evoluir o mesmo sistema perante novos requisitos (extensão).',
  'Erro conceitual: reuso por composição é superior à herança e código procedural prejudica a extensibilidade.',
  'Erro taxonômico: confusão entre métricas arquiteturais e dimensões de hardware.',
  'Erro conceitual: velocidade de inicialização é tempo de boot/desempenho, não atributos de design interno.',
  'Reusabilidade é criar uma roda padrão que serve tanto em um carrinho de bebê quanto em um cortador de grama. Extensibilidade é projetar o chassi do carro de modo que você possa acoplar um bagageiro no teto sem precisar serrar a lataria.',
  'Módulos modulares de alta coesão possibilitam alto reuso em novas aplicações e fácil extensão através de herança e polimorfismo.')

# 07
q(13, '07. Atributos e métodos (classes, objetos e definição de membros).md', 'Estado e comportamento em POO', 'facil',
  'Em programação orientada a objetos em C#, qual é o papel desempenhado pelos atributos (ou campos de instância) e pelos métodos dentro de uma definição de classe?',
  'Atributos representam o estado (dados estruturais) mantido por cada objeto instanciado; métodos representam o comportamento (operações executáveis que manipulam ou consultam esse estado).',
  'Atributos definem algoritmos de criptografia; métodos servem exclusivamente para declarar variáveis na pilha de chamadas.',
  'Atributos são compartilhados obrigatoriamente por todos os processos do sistema operacional; métodos são estáticos por padrão.',
  'Atributos só podem armazenar texto; métodos só podem retornar números decimais.',
  0,
  'Correto: uma classe une estado (atributos) e comportamento (métodos) sob um mesmo encapsulamento semântico.',
  'Erro conceitual: atributos armazenam dados da instância, não são algoritmos executáveis.',
  'Erro de escopo: atributos de instância pertencem a cada objeto específico na heap do processo.',
  'Erro conceitual e de tipos: campos aceitam qualquer tipo suportado pelo sistema de tipos da linguagem.',
  'Um cachorro tem características como raça, cor e idade (atributos/estado) e sabe latir, correr e abanar o rabo (métodos/comportamento).',
  'A união indissociável de dados e rotinas que operam sobre esses dados em uma mesma entidade é a definição fundacional de objeto.')

q(14, '07. Atributos e métodos (classes, objetos e definição de membros).md', 'Alocação de objetos e referências em C#', 'medio',
  'Considere o código C#: `Conta c1 = new Conta(); Conta c2 = c1; c2.Saldo = 100;`. O que ocorre com o saldo acessado através da variável `c1` e por qual razão?',
  '`c1.Saldo` permanece zero, pois a atribuição `c2 = c1` cria uma cópia profunda de todos os dados do objeto.',
  '`c1.Saldo` passa a valer 100, pois `Conta` é um tipo de referência (classe), fazendo com que `c1` e `c2` apontem para a mesmíssima instância alocada na memória heap.',
  'O compilador emite um erro de compilação porque em C# é proibido ter duas variáveis referenciando o mesmo objeto.',
  'Ocorre uma violação de acesso à memória (NullReferenceException) durante a atribuição em c2.',
  1,
  'Erro conceitual: atribuição de variáveis de referência copia apenas o ponteiro/endereço, não o objeto na heap.',
  'Correto: ambas as variáveis na stack contêm o mesmo endereço de memória apontando para o objeto na heap gerenciada.',
  'Erro conceitual: aliasing de referências é comportamento nativo e padrão de linguagens orientadas a objetos.',
  'Erro de execução: `c1` foi instanciado com `new`, logo a referência é válida e não nula.',
  'É como duas pessoas segurando cópias da mesma chave da mesma casa: se uma pessoa entra e pinta a sala de azul (`c2.Saldo = 100`), quando a outra entrar na casa com a sua chave (`c1`), verá a sala azul.',
  'Classes são tipos por referência alocados na heap gerenciada; variáveis locais armazenam referências que podem compartilhar o mesmo objeto.')

# 08
q(15, '08. Construtores (inicialização, sobrecarga e garantia de invariantes).md', 'Papel do construtor na garantia de invariantes', 'medio',
  'Por que o construtor é considerado o guardião inicial das invariantes de um objeto na programação modular?',
  'Porque o construtor é o único local onde é permitido declarar comandos if e loops while.',
  'Porque o construtor garante que nenhum objeto seja colocado em uso no sistema em um estado inicial inválido, incompleto ou inconsistente.',
  'Porque o construtor impede que a coleta de lixo desalavanque o objeto após o encerramento do programa.',
  'Porque o construtor compila o código C# diretamente em instruções binárias do microprocessador.',
  1,
  'Erro conceitual: estruturas de controle condicionais e de repetição podem ser utilizadas em qualquer método.',
  'Correto: o papel primordial do construtor é estabelecer o estado válido inicial exigido pelas invariantes da classe.',
  'Erro técnico: gerenciamento de ciclo de vida e coleta de lixo são funções do Garbage Collector do runtime.',
  'Erro de arquitetura: compilação é tarefa do compilador Roslyn e do JIT do .NET.',
  'O construtor é o controle de qualidade na saída da fábrica de automóveis: o carro só sai para a concessionária se o volante, os freios e o motor estiverem instalados e funcionando perfeitamente.',
  'Ao exigir parâmetros mandatórios e validar regras no construtor, eliminam-se objetos anêmicos e estados inconsistentes.')

q(16, '08. Construtores (inicialização, sobrecarga e garantia de invariantes).md', 'Sobrecarga de construtores e a cláusula : this()', 'dificil',
  'Em C#, qual é a melhor prática ao implementar sobrecarga de construtores (*constructor chaining*) utilizando a sintaxe `: this(...)`?',
  'Duplicar todo o código de validação em cada um dos construtores sobrecarregados para garantir redundância de segurança.',
  'Fazer com que construtores secundários (com menos parâmetros) deleguem a inicialização para o construtor principal canônico via `: this(...)`, centralizando as validações de invariantes em um único ponto.',
  'Utilizar `: this()` apenas para chamar métodos privados estáticos da classe ancestral.',
  'Declarar todos os construtores com visibilidade privada para que a classe não possa ser instanciada nem por ela mesma.',
  1,
  'Erro de design: duplicação de validações viola o princípio DRY (Don\'t Repeat Yourself) e gera risco de divergência.',
  'Correto: o encadeamento de construtores via `: this(...)` centraliza as regras no construtor mais completo.',
  'Erro de sintaxe e semântica: `: this(...)` invoca construtores da própria instância, não métodos estáticos.',
  'Erro conceitual: construtores puramente privados sem fábricas públicas impedem qualquer uso da classe.',
  'O construtor canônico é a receita completa do bolo; os construtores sobrecarregados são atalhos para quem não quer escolher tudo: eles usam valores padrão pré-definidos e chamam a receita principal.',
  'Delegar para um construtor centralizado evita inconsistências e garante que nenhuma regra de validação seja esquecida em sobrecargas.')

# 09
q(17, '09. Atributos estáticos e propriedades (compartilhamento de estado e encapsulamento).md', 'Membros estáticos vs. de instância', 'medio',
  'Qual é a diferença fundamental entre um atributo de instância e um atributo estático (`static`) em uma classe C#?',
  'Atributos de instância pertencem e são replicados para cada objeto criado; atributos estáticos pertencem à própria classe e possuem um único espaço de armazenamento na memória compartilhado por todas as instâncias.',
  'Atributos estáticos só podem armazenar números negativos; atributos de instância armazenam cadeias de texto.',
  'Atributos estáticos são destruídos assim que um método qualquer termina sua execução.',
  'Atributos de instância podem ser acessados diretamente sem instanciar a classe via `Classe.Atributo`.',
  0,
  'Correto: o modificador `static` vincula o membro ao tipo (armazenado na memória do domínio de aplicação) e não a instâncias individuais.',
  'Erro conceitual absurdo: tipos de dados suportados são idênticos em ambos os tipos de membros.',
  'Erro taxonômico: variáveis locais da stack morrem ao final do método; atributos estáticos persistem enquanto o domínio de aplicação viver.',
  'Erro inverso: acesso direto pelo nome da classe é a característica exclusiva de membros estáticos.',
  'Um atributo de instância é o RG de cada cidadão (cada pessoa tem o seu cartão físico). Um atributo estático é o relógio público na praça da cidade: existe apenas um e todos olham para o mesmo marcador.',
  'Campos estáticos representam estado global compartilhado e devem ser usados com extrema parcimônia para evitar acoplamento oculto e problemas de concorrência.')

q(18, '09. Atributos estáticos e propriedades (compartilhamento de estado e encapsulamento).md', 'Propriedades estáticas e validação global', 'dificil',
  'Ao utilizar uma propriedade estática com acessores `get` e `set` para gerenciar uma configuração global de sistema, qual risco arquitetural deve ser considerado pelo projetista de software?',
  'O compilador C# emitirá uma exceção de compilação em tempo de execução.',
  'Introduzir estado mutável compartilhado globalmente, que prejudica a testabilidade (testes paralelos interferindo uns nos outros) e introduz acoplamento de ambiente indesejado.',
  'Propriedades estáticas não permitem execução de código de validação dentro de blocos set.',
  'O consumo de banda da placa de rede será multiplicado exponencialmente.',
  1,
  'Erro de terminologia: compilador opera em tempo de compilação, não tempo de execução.',
  'Correto: estado mutável global compartilhado dificulta testes unitários isolados e cria dependências invisíveis.',
  'Erro conceitual: propriedades estáticas suportam blocos completos de lógica e validação em get e set.',
  'Erro de categoria: consumo de memória local estática não se comunica espontaneamente com a placa de rede.',
  'Um estado global mutável é como um quadro de avisos comunitário em uma república de estudantes onde qualquer um pode rabiscar o recado do outro a qualquer hora: ninguém tem certeza de quem alterou o que e quando.',
  'Prefira injeção de dependências e objetos de configuração imutáveis em vez de classes estáticas com estado mutável.')

# 10
q(19, '10. Destrutores e finalizadores (desalocação de memória e liberação de recursos).md', 'Gerenciamento de memória gerenciada e o padrão IDisposable', 'dificil',
  'No ecossistema .NET em C#, qual é a recomendação canônica para liberação determinística de recursos não gerenciados (como handles de arquivos, sockets de rede e conexões de banco de dados)?',
  'Confiar exclusivamente no finalizador (`~Classe()`), pois ele é executado imediatamente no exato instante em que o objeto sai de escopo.',
  'Implementar a interface `IDisposable` com o padrão Dispose e consumir o objeto por meio do bloco `using`, garantindo liberação determinística mesmo em caso de exceções.',
  'Reiniciar a máquina virtual do sistema operacional a cada requisição de cliente para forçar o descarte.',
  'Desativar o coletor de lixo (Garbage Collector) permanentemente através de diretivas de compilação.',
  1,
  'Erro técnico grave: finalizadores são executados de forma não determinística em uma thread secundária de baixa prioridade pelo GC.',
  'Correto: a interface IDisposable com a instrução using assegura chamada determinística ao método Dispose() via bloco try-finally gerado pelo compilador.',
  'Erro absurdo: reinicialização do sistema destruiria a disponibilidade de qualquer aplicação comercial.',
  'Erro conceitual: desativar o GC causaria exaustão rápida de memória (Memory Leak generalizado).',
  'O GC é como a equipe de limpeza pública que passa na rua em horários indeterminados para recolher o lixo reciclável (memória gerenciada). O Dispose do using é você fechar a torneira de água imediatamente após lavar as mãos para não inundar o banheiro (recurso não gerenciado).',
  'Recursos não gerenciados devem ser liberados de forma determinística via IDisposable/using para evitar bloqueios e exaustão de descritores no sistema operacional.')

q(20, '10. Destrutores e finalizadores (desalocação de memória e liberação de recursos).md', 'Funcionamento do Garbage Collector por gerações', 'dificil',
  'Como o Garbage Collector (GC) do .NET organiza os objetos na memória heap gerenciada para otimizar o desempenho de coleta?',
  'Ele organiza os objetos em três gerações (Geração 0 para objetos recém-alocados e de vida curta, Geração 1 como zona de transição e Geração 2 para objetos de vida longa).',
  'Ele aloca todos os objetos em um disco rígido externo particionado em setores FAT32.',
  'Ele utiliza contadores manuais de referência que travam a CPU em todas as atribuições de variáveis.',
  'Ele realiza a varredura e realocação completa de 100% da memória RAM a cada instrução aritmética executada.',
  0,
  'Correto: a hipótese geracional estabelece que a grande maioria dos objetos morre jovem (Geração 0 é limpa rapidamente e com alta frequência).',
  'Erro de hardware: a heap gerenciada reside na memória RAM volátil do processo.',
  'Erro de tecnologia: contadores de referência (ARC) são usados em outros ambientes (como Swift/Objective-C), não no .NET com Mark-and-Sweep geracional.',
  'Erro de escala: varreduras completas (Gen 2 / Full GC) são raras e custosas, ocorrendo apenas quando necessário.',
  'Pense na triagem de cartas de correspondência: a caixa de entrada imediata (Gen 0) é checada toda hora para descartar panfletos inúteis rapidamente. Documentos importantes que sobrevivem a várias checagens vão para o arquivo definitivo do cofre (Gen 2), que só é reorganizado uma vez por ano.',
  'O GC geracional do .NET baseia-se na constatação empírica de que novos objetos têm ciclos de vida curtos, tornando as coletas de Gen 0 ultrarrápidas.')

print('Questões 1 a 20 geradas com sucesso.')


# 11
q(21, '11. Princípio da ocultação da informação (information hiding e encapsulamento).md', 'Information Hiding de David Parnas', 'dificil',
  'David Parnas (1972) formulou o princípio de ocultamento de informação (Information Hiding). Qual é o critério de decomposição de módulos preconizado por Parnas?',
  'Decompor o sistema com base na sequência cronológica dos passos do fluxograma de processamento.',
  'Cada módulo deve encapsular e ocultar uma decisão de design difícil ou propensa a mudanças (como estrutura de dados interna, formato de arquivo ou algoritmo específico), expondo apenas uma interface estável.',
  'Colocar todo o código em um único arquivo para que o compilador oculte os símbolos dos invasores de rede.',
  'Ocultar o código-fonte de modo que nem a equipe de desenvolvimento saiba quais métodos existem.',
  1,
  'Erro histórico e conceitual: decomposição por etapas cronológicas é o modelo clássico procedural que Parnas comprovou ser frágil a mudanças.',
  'Correto: o princípio de Parnas postula que segredos de design que podem mudar devem ser confinados dentro de módulos independentes.',
  'Erro taxonômico absurdo: compilação monolítica não tem relação com o princípio arquitetural de Parnas.',
  'Erro conceitual: information hiding refere-se a interfaces públicas claras ocultando detalhes internos dos consumidores de código, não ofuscação de equipe.',
  'Pense em uma tomada elétrica na parede: o segredo de como a fiação passa pelo tijolo e qual usina gerou a energia fica oculto atrás do espelho; você só precisa do padrão estável de 3 pinos para ligar seu aparelho.',
  'Information hiding isola o impacto de mudanças futuras: se a estrutura interna mudar, nenhum cliente quebrado precisará ser reescrito.')

q(22, '11. Princípio da ocultação da informação (information hiding e encapsulamento).md', 'Encapsulamento vs. Information Hiding', 'dificil',
  'Embora frequentemente usados como sinônimos no jargão cotidiano, qual é a distinção teórica precisa entre Encapsulamento e Ocultamento de Informação (Information Hiding)?',
  'Encapsulamento é o mecanismo sintático da linguagem que agrupa dados e métodos e controla visibilidade; Ocultamento de Informação é o princípio arquitetural e heurística de design sobre quais decisões devem ser isoladas.',
  'Encapsulamento só existe em C++; Information Hiding só existe em bancos de dados relacionais.',
  'Encapsulamento torna todo o código público; Information Hiding impede a compilação do executável.',
  'Não há distinção teórica nem prática em nenhum livro clássico de computação.',
  0,
  'Correto: encapsulamento é o invólucro/mecanismo (técnica de empacotar e proteger membros); information hiding é a estratégia de design que orienta o que esconder.',
  'Erro conceitual e geográfico de linguagens.',
  'Erro inverso e absurdo.',
  'Erro histórico: autores como Booch, Meyer e Parnas explicitam a diferença entre técnica de empacotamento e estratégia de isolamento de volatilidade.',
  'Encapsulamento é a caixa de remédios com tampa plástica e trava de segurança (o mecanismo); Information Hiding é a decisão do médico de colocar a fórmula química complexa dentro da cápsula para você engolir sem precisar entender os compostos moleculares (a estratégia).',
  'Encapsulamento provê as ferramentas de barreira (como modificadores de acesso), enquanto information hiding determina onde essas barreiras devem ser erguidas.')

# 12
q(23, '12. Modificadores de acesso (visibilidade e níveis de proteção no encapsulamento).md', 'Modificadores de acesso em C#', 'medio',
  'Em C#, qual é a restrição de visibilidade imposta pelo modificador de acesso `protected internal` em um membro de classe?',
  'O membro só é visível dentro da própria classe e em nenhuma outra parte do universo.',
  'O membro é acessível em qualquer classe dentro do mesmo assembly atual OU por tipos derivados (subclasses) mesmo que localizados em outros assemblies externos.',
  'O membro só pode ser acessado se a aplicação for executada em ambiente Linux.',
  'O membro torna-se automaticamente estático e assíncrono.',
  1,
  'Erro conceitual: isso descreve o modificador `private`.',
  'Correto: `protected internal` combina união disjuntiva (mesmo assembly OU subclasses em qualquer assembly).',
  'Erro absurdo: modificadores de acesso são regras do sistema de tipos do CLR, independentes de SO.',
  'Erro taxonômico: visibilidade de membro é ortogonal a ciclo de vida estático ou assincronia.',
  'É como uma festa onde entram todos os parentes da família (subclasses onde quer que morem) MAIS todos os moradores da mesma rua (classes do mesmo assembly).',
  'C# oferece granularidade fina de modificadores: private, protected, internal, protected internal e private protected.')

q(24, '12. Modificadores de acesso (visibilidade e níveis de proteção no encapsulamento).md', 'Private protected em C#', 'dificil',
  'Introduzido em versões recentes do C#, qual é o comportamento do modificador `private protected`?',
  'O membro é acessível apenas por classes derivadas que estejam localizadas estritamente DENTRO do mesmo assembly (interseção entre protected e internal).',
  'O membro fica disponível para qualquer classe do sistema sem restrições.',
  'O membro pode ser lido mas nunca escrito mesmo pela própria classe declarante.',
  'O membro é destruído automaticamente a cada 10 segundos pelo coletor de lixo.',
  0,
  'Correto: `private protected` representa a interseção (somente subclasses E dentro do mesmo assembly).',
  'Erro conceitual: isso descreve o modificador `public`.',
  'Erro conceitual: isso descreve um campo `readonly`.',
  'Erro taxonômico: modificadores tratam de regras de compilação/acesso, não temporizadores de descarte.',
  'Se `protected internal` é união (família OU vizinhos da rua), `private protected` é interseção estrita: só entram os parentes que moram na mesma casa.',
  'Use `private protected` quando você desenvolve uma biblioteca e quer que suas classes internas herdem membros auxiliares sem expô-los para consumidores externos do pacote.')

# 13
q(25, '13. Métodos de acesso e propriedades (publicação de contratos e garantia de invariantes).md', 'Propriedades com get público e set privado', 'medio',
  'Por que declarar uma propriedade como `public decimal Saldo { get; private set; }` é superior a expor um campo público `public decimal Saldo;`?',
  'Porque o compilador C# converte a propriedade em um arquivo XML externo gravado no disco.',
  'Porque permite leitura livre por consumidores externos, mas restringe a mutação exclusivamente aos métodos internos da própria classe, permitindo auditar e validar alterações de invariantes.',
  'Porque propriedades com get e private set eliminam o uso de memória RAM na execução.',
  'Porque campos públicos são convertidos automaticamente em código de máquina não seguro (unsafe).',
  1,
  'Erro técnico: auto-properties geram um backing field privado em tempo de compilação no IL, sem arquivos XML.',
  'Correto: leitura pública preserva o contrato de consulta, enquanto escrita restrita impede mutações arbitrárias por clientes externos.',
  'Erro conceitual: o backing field ocupa normalmente memória na heap gerenciada.',
  'Erro de linguagem: campos públicos continuam sendo código gerenciado seguro (safe CLR).',
  'É como um relógio de parede no escritório: qualquer cliente ou funcionário pode olhar para o mostrador e ver as horas (get público), mas só o gerente tem a chave para acertar os ponteiros (set privado/interno).',
  'Auto-properties com `private set` ou `init` fornecem encapsulamento idiomático e seguro em C#.')

q(26, '13. Métodos de acesso e propriedades (publicação de contratos e garantia de invariantes).md', 'Propriedades init-only em C#', 'dificil',
  'O modificador de acessor `init` introduzido no C# 9 permite que uma propriedade seja atribuída:',
  'A qualquer momento durante a execução de qualquer método da classe consumidora.',
  'Apenas durante a inicialização do objeto (no construtor ou por meio de inicializadores de objeto `new Classe { Prop = val }`), tornando o objeto imutável após a conclusão da construção.',
  'Exclusivamente por meio de reflexão (Reflection) em tempo de execução.',
  'Apenas em noites de lua cheia de acordo com o calendário do servidor.',
  1,
  'Erro conceitual: mutação contínua a qualquer momento é o papel do acessor `set`.',
  'Correto: `init` garante imutabilidade pós-construção com suporte fluido a object initializers.',
  'Erro técnico: init é recurso de primeira classe da linguagem validado em tempo de compilação pelo Roslyn.',
  'Erro cômico e absurdo.',
  'O acessor init é como moldar um vaso de argila molhada: enquanto a peça está no torno de modelagem (construção), você pode dar a forma que quiser; depois que ela vai ao forno e seca, ninguém mais altera sem quebrar o vaso.',
  'Propriedades `init` unem a expressividade dos inicializadores de objeto com a segurança da imutabilidade pós-instanciação.')

# 14
q(27, '14. Namespaces e partial classes (espaços de nomes e modularização em larga escala).md', 'Resolução de ambiguidades com namespaces', 'facil',
  'Em projetos com múltiplas bibliotecas e módulos, qual é a função essencial das diretivas `namespace` em C#?',
  'Impedir que classes tenham mais de 10 linhas de código-fonte.',
  'Organizar logicamente o sistema em escopos hierárquicos e evitar conflitos de nomes (colisões de identificadores) entre classes homônimas de diferentes módulos.',
  'Traduzir o código C# para linguagem Java em tempo real.',
  'Configurar a velocidade do clock da placa gráfica.',
  1,
  'Erro de métrica: namespaces não impõem limites de contagem de linhas físicas de código.',
  'Correto: namespaces fornecem espaços de nomes lógicos para desambiguação e modularização hierárquica.',
  'Erro taxonômico de linguagens.',
  'Erro de hardware de vídeo.',
  'Namespaces são como sobrenomes de pessoas ou códigos de discagem telefônica por cidade: existem muitas pessoas chamadas Maria, mas ao usar o nome completo e o DDD sabemos com exatidão a quem estamos nos referindo.',
  'Namespaces modularizam o ecossistema de classes e evitam colisões em projetos corporativos complexos.')

q(28, '14. Namespaces e partial classes (espaços de nomes e modularização em larga escala).md', 'Partial classes em C#', 'medio',
  'Para que serve o modificador `partial` em uma classe C#?',
  'Para dividir a definição de uma mesma classe em dois ou mais arquivos de código-fonte separados, combinados pelo compilador em uma única classe durante a compilação.',
  'Para indicar que a classe está com erros de sintaxe e não deve ser compilada.',
  'Para criar uma classe que só executa metade de seus métodos.',
  'Para proibir o uso de métodos assíncronos e interfaces.',
  0,
  'Correto: `partial class` permite que desenvolvedores ou geradores de código (como designers visuais ou EF Core) dividam o arquivo da mesma classe.',
  'Erro conceitual: código parcial deve ser sintaticamente válido em todas as partes.',
  'Erro literal e absurdo.',
  'Erro técnico: classes parciais suportam plenamente assincronia, interfaces e atributos.',
  'Uma partial class é como um livro publicado em dois volumes separados para facilitar a leitura na estante, mas que formam exatamente a mesma história contínua quando o leitor junta as partes.',
  'Partial classes são muito utilizadas em geradores de código (como Razor, WPF, Windows Forms e EF Core) para separar código gerado de código manual.')

# 15
q(29, '15. Herança (generalização, especialização e extensibilidade modular).md', 'Relação é-um vs. tem-um', 'medio',
  'Na modelagem orientada a objetos, qual é o critério conceitual fundamental para aplicar Herança em vez de Composição entre duas entidades?',
  'Herança deve modelar estritamente uma relação taxonômica de especialização \'é-um\' (onde todo subtipo atende aos contratos do tipo base); Composição deve modelar relações de posse, agregação ou colaboração funcional \'tem-um\'.',
  'Herança só deve ser usada para economizar três linhas de código em classes pequenas; Composição é proibida em linguagens modernas.',
  'Herança cria cópias físicas do banco de dados no computador do usuário; Composição roda apenas na memória cache L1.',
  'Herança só pode ser utilizada se a classe filha tiver menos métodos que a classe pai.',
  0,
  'Correto: o princípio basilar da modelagem taxonômica: herança é especialização \'é-um\', composição é acoplamento funcional \'tem-um\'.',
  'Erro grave de design: reuso cego de código via herança espúria é o antipadrão mais comum em POO.',
  'Erro de hardware e banco de dados.',
  'Erro conceitual: subclasses tipicamente expandem ou especializam comportamentos do tipo base.',
  'Um Carro \'é-um\' Veículo (herança legítima); mas um Carro \'tem-um\' Motor (composição - o carro não \'é\' um motor, ele possui um motor para funcionar).',
  'Favorecer composição sobre herança é uma das diretrizes mais importantes de design para evitar hierarquias frágeis e acoplamento rígido.')

q(30, '15. Herança (generalização, especialização e extensibilidade modular).md', 'Problema da classe base frágil', 'dificil',
  'O que é o clássico \'problema da classe base frágil\' (fragile base class problem) na programação orientada a objetos baseada em herança?',
  'Ocorre quando a classe base é apagada do disco rígido pelo sistema operacional.',
  'Ocorre quando alterações aparentemente inofensivas no código interno da classe base quebram silenciosamente o comportamento de classes filhas derivadas devido ao acoplamento íntimo de implementação herdada.',
  'Ocorre quando uma classe filha tem mais atributos do que o processador pode calcular.',
  'Ocorre quando a memória RAM quebra fisicamente durante a compilação do executável.',
  1,
  'Erro físico e de arquivo.',
  'Correto: definição clássica de fragilidade por herança de implementação: dependências implícitas entre métodos da base quebram os subtipos.',
  'Erro de arquitetura de hardware.',
  'Erro cômico e absurdo de hardware.',
  'É como puxar uma gaveta de baixo de um armário mal projetado: você só queria pegar uma meia, mas todo o fundo da gaveta de cima desaba porque as prateleiras estavam apoiadas de forma frágil umas nas outras.',
  'A herança de implementação cria o acoplamento mais forte possível entre classes; por isso, prefira composição ou interfaces para extensibilidade segura.')

# 16
q(31, '16. Construtores em classes filhas (ordem de inicialização e a cláusula base).md', 'Ordem de inicialização em hierarquias de classes', 'dificil',
  'Em C#, qual é a ordem exata de execução dos construtores quando uma instância de uma subclasse derivada `Cachorro` (que herda de `Animal`) é criada com `new Cachorro()`?',
  'Primeiro executa o corpo do construtor de Cachorro e, se sobrar tempo na CPU, executa o construtor de Animal.',
  'Primeiro inicializam-se os inicializadores de campos da classe derivada; em seguida, o construtor da classe base (`Animal`) é obrigatoriamente concluído antes que o corpo do construtor de `Cachorro` execute.',
  'Ambos executam simultaneamente em threads paralelas assíncronas sem ordem determinística.',
  'Apenas o construtor de Cachorro executa; construtores de classes base são totalmente ignorados em C#.',
  1,
  'Erro conceitual grave: uma classe filha não pode manipular seu estado antes que os alicerces herdados da base existam.',
  'Correto: o runtime do CLR garante que a base esteja validada e estável antes que o corpo do construtor derivado opere.',
  'Erro de concorrência: a instanciação de um objeto é estritamente síncrona e determinística.',
  'Erro conceitual: o construtor da base é sempre executado (implicitamente via construtor padrão ou explicitamente via `: base(...)`).',
  'Você não pode construir as paredes do segundo andar da casa (construtor da filha) antes de concretar a fundação e o primeiro andar (construtor da base).',
  'A cláusula `: base(...)` assegura passagem determinística de argumentos para que a superclasse inicialize suas invariantes com segurança.')

q(32, '16. Construtores em classes filhas (ordem de inicialização e a cláusula base).md', 'A cláusula base(...) e ausência de construtor padrão', 'dificil',
  'Se a classe base `Veiculo` possui apenas um construtor explícito parametrizado `public Veiculo(string chassi)` e não define nenhum construtor sem parâmetros, o que acontece com a classe derivada `Carro`?',
  'Carro compila normalmente sem construtores porque o C# gera um chassi aleatório em tempo de execução.',
  'Carro não compilará a menos que declare explicitamente um construtor que invoque `: base(chassi)` passando o parâmetro obrigatório exigido pela classe base.',
  'O compilador transforma a classe Carro em uma interface pública com métodos virtuais.',
  'O programa executa normalmente mas emite um aviso sonoro no alto-falante da placa-mãe.',
  1,
  'Erro conceitual: compiladores estáticos não inventam dados de negócio para suprir parâmetros contratuais ausentes.',
  'Correto: a ausência do construtor padrão na base obriga todas as derivadas a proverem construtores que invoquem explicitamente `: base(...)`.',
  'Erro taxonômico: classes não viram interfaces por falha de inicialização.',
  'Erro cômico e absurdo.',
  'Se para matricular um aluno na universidade (base) é obrigatório apresentar o CPF, qualquer inscrição específica para o curso de medicina (derivada) tem a obrigação de recolher o CPF e repassá-lo para a matrícula geral.',
  'Construtores de classes base garantem que os atributos herdados e suas invariantes nunca fiquem em estado não inicializado.')

# 17
q(33, '17. Sobreposição de métodos (virtual e override).md', 'Despacho dinâmico e tabela virtual (vtable)', 'dificil',
  'Em C#, como o runtime (CLR) implementa o mecanismo de sobreposição polimórfica (dynamic dispatch) quando um método marcado como `virtual` na base é sobreposto com `override` na classe derivada?',
  'Ele faz uma busca no Google durante a execução para saber qual método chamar.',
  'Ele utiliza a tabela de métodos virtuais (vtable / Method Table) do objeto real instanciado na memória heap, despachando a chamada para a implementação mais especializada da classe real, independentemente do tipo da variável de referência.',
  'Ele ignora a classe derivada e sempre executa a versão da classe base para evitar lentidão.',
  'Ele recompila o sistema operacional toda vez que um método virtual é invocado.',
  1,
  'Erro cômico e absurdo.',
  'Correto: o ponteiro de tipo na cabeçalho do objeto (Type Handle) aponta para a Method Table do tipo concreto real alocado na heap.',
  'Erro conceitual: isso anularia completamente o polimorfismo dinâmico.',
  'Erro de escala: tabelas de métodos virtuais são estruturas estáticas de memória resolvidas em tempo constante O(1).',
  'A variável de referência é apenas o crachá genérico \'Funcionário\'; mas o objeto real na mesa de trabalho é um \'Cirurgião\'. Quando chamamos `operar()`, olhamos para a especialidade real da pessoa concreta sentada na cadeira, não para o rótulo escrito no crachá.',
  'Virtual e override habilitam o despacho dinâmico via tabela de métodos virtuais do objeto concreto alocado na heap.')

q(34, '17. Sobreposição de métodos (virtual e override).md', 'Override vs. New (method hiding) em C#', 'dificil',
  'Qual é a consequência fundamental de declarar um método na subclasse utilizando o modificador `new` (ocultamento de método) em vez de `override` em C#?',
  'Não há nenhuma consequência; `new` e `override` são sinônimos idênticos no IL compilado.',
  'Com `new`, o método da base é apenas ocultado estaticamente: se o objeto for acessado por uma referência do tipo base (`Base b = new Filha()`), será chamado o método da classe base e NÃO o da filha, quebrando o despacho dinâmico polimórfico.',
  'Com `new`, o método da classe base é apagado da memória e não pode mais ser chamado por ninguém.',
  'O modificador `new` força a classe a ser executada em modo não gerenciado com ponteiros C++.',
  1,
  'Erro técnico: `override` preenche o slot da vtable; `new` cria um método independente com novo slot na tabela.',
  'Correto: method hiding (`new`) desativa o despacho dinâmico polimórfico para referências tipadas na base.',
  'Erro conceitual: o método da base continua perfeitamente acessível via casting ou chamadas de tipo base.',
  'Erro taxonômico: modificador de membro não altera o modelo de gerenciamento de memória gerenciada do CLR.',
  'Usar `override` é substituir o chip de comando original por um melhor (qualquer um que aperte o botão aciona o novo). Usar `new` é colar um adesivo por cima do botão: quem olhar por trás (referência da base) continua apertando o botão velho.',
  'Evite usar `new` para ocultar métodos em hierarquias polimórficas, pois isso introduz bugs sutis de comportamento dependentes do tipo da variável de referência.')

# 18
q(35, '18. Classes abstratas e métodos abstratos (contratos de herança e polimorfismo puro).md', 'Classes abstratas e instanciação', 'medio',
  'O que caracteriza uma classe abstrata (`abstract class`) em C# e qual é sua principal restrição operacional?',
  'Classes abstratas podem ser instanciadas livremente com o operador new em qualquer método.',
  'Classes abstratas não podem ser diretamente instanciadas com new; seu propósito é servir como molde conceitual incompleto e contrato base para que subclasses concretas herdem e implementem seus membros abstratos.',
  'Classes abstratas não podem conter código implementado nem métodos concretos em nenhuma hipótese.',
  'Classes abstratas só podem ser usadas em programas de console sem interface gráfica.',
  1,
  'Erro conceitual básico: classes abstratas são explicitamente impedidas de instanciação direta pelo compilador.',
  'Correto: classes abstratas representam abstrações que exigem especialização concreta por subclasses.',
  'Erro conceitual: classes abstratas podem conter estado (atributos), construtores e métodos concretos completamente implementados.',
  'Erro de escopo: classes abstratas são conceitos de POO puros, agnósticos a tipo de interface.',
  'Você não compra um \'Animal\' genérico no pet shop: você compra um cachorro, um gato ou um papagaio. O conceito de \'Animal\' é abstrato e une o que todos os bichos têm em comum.',
  'Classes abstratas compartilham código comum (métodos concretos e estado) e impõem contratos mandatórios (métodos abstratos).')

q(36, '18. Classes abstratas e métodos abstratos (contratos de herança e polimorfismo puro).md', 'Métodos abstratos em subclasses concretas', 'medio',
  'Se uma classe abstrata `FormaGeometrica` declara um método abstrato `public abstract double CalcularArea();`, o que é compulsoriamente exigido de uma subclasse não-abstrata (concreta) `Retangulo` que herda dessa base?',
  'Ela não precisa fazer nada, pois métodos abstratos se implementam sozinhos por inteligência artificial.',
  'Ela é estritamente obrigada a fornecer uma implementação concreta do método utilizando a palavra-chave `override`, sob pena de erro de compilação.',
  'Ela deve transformar todos os seus atributos em variáveis globais estáticas.',
  'Ela deve ser deletada do projeto para não causar conflitos de herança.',
  1,
  'Erro conceitual e absurdo.',
  'Correto: classes concretas devem implementar todos os métodos abstratos herdados para que possam ser instanciadas.',
  'Erro conceitual de escopo.',
  'Erro de arquivo absurdo.',
  'A classe abstrata assina um contrato com uma cláusula em branco: toda subclasse concreta que herdar esse contrato tem a obrigação jurídica de preencher essa cláusula com sua própria assinatura antes de poder operar.',
  'Métodos abstratos não possuem corpo na superclasse (`{}`); o corpo deve ser fornecido via `override` nos subtipos concretos.')

# 18A
q(37, '18A. Interfaces, contratos e polimorfismo por interface.md', 'Interfaces vs. Classes Abstratas em C#', 'dificil',
  'Na programação modular em C#, qual é a principal flexibilidade arquitetural proporcionada pelo uso de Interfaces (`interface`) em comparação com Classes Abstratas?',
  'Interfaces ocupam menos espaço na memória RAM porque não suportam comentários de código.',
  'C# suporta apenas herança simples de classes (uma classe só pode herdar de uma única classe base, seja ela abstrata ou concreta), mas permite a implementação de múltiplas interfaces por uma mesma classe, viabilizando polimorfismo multifacetado e desacoplamento de papéis.',
  'Interfaces não podem ser utilizadas como tipo de parâmetros em métodos de controladores Web.',
  'Interfaces compilam mais rápido porque são convertidas diretamente em arquivos de áudio MP3.',
  1,
  'Erro técnico grosseiro.',
  'Correto: interfaces viabilizam composição de múltiplos contratos de capacidades (ex.: `IComparable`, `IDisposable`, `IValidatableObject`) contornando a restrição de herança simples.',
  'Erro conceitual: interfaces são a fundação da injeção de dependências em aplicações modernas.',
  'Erro cômico e absurdo.',
  'Uma pessoa pode ter apenas um pai biológico (herança simples de classe), mas pode ter múltiplos certificados profissionais: carteira de motorista, licença de piloto e diploma de engenheiro (múltiplas interfaces implementadas simultaneamente).',
  'Use classes abstratas para compartilhar identidade de domínio e código base; use interfaces para definir contratos de capacidades desacoplados da hierarquia taxonômica.')

q(38, '18A. Interfaces, contratos e polimorfismo por interface.md', 'Implementação explícita de interface em C#', 'dificil',
  'Em C#, o que caracteriza a implementação explícita de uma interface (ex.: `void IDisposable.Dispose()`) e qual o seu benefício no design modular?',
  'O método torna-se público para todas as classes do sistema e pode ser chamado sem conversão.',
  'O método não ganha modificador de acesso público na classe e só pode ser invocado quando o objeto é referenciado explicitamente por meio da interface correspondente, evitando poluir a API pública da classe e resolvendo conflitos entre interfaces homônimas.',
  'O método é executado de forma assíncrona em uma GPU externa de mineração.',
  'O método não pode conter linhas de código com mais de 80 caracteres.',
  1,
  'Erro inverso: a implementação explícita oculta o método da API direta da classe concreta.',
  'Correto: resolve colisões de nomes entre interfaces distintas e mantém a superfície pública do objeto limpa.',
  'Erro de hardware de vídeo.',
  'Erro de estilo cosmético.',
  'É como ter um plugue de manutenção oculto atrás de uma tampa técnica: o usuário comum da TV não vê o botão no controle remoto, mas o técnico que conecta o cabo diagnóstico apropriado (referência da interface) consegue acioná-lo perfeitamente.',
  'A implementação explícita é uma ferramenta poderosa para segregação de interfaces e preservação de APIs coesas.')

# 19
q(39, '19. Classes e membros selados (sealed).md', 'Finalidade do modificador sealed em C#', 'medio',
  'Qual é o efeito de aplicar o modificador `sealed` na declaração de uma classe em C#?',
  'A classe não pode ser herdada por nenhuma outra classe no sistema, impedindo que novas subclasses sejam derivadas a partir dela.',
  'A classe não pode ser instanciada nem pode ter construtores.',
  'A classe passa a ser criptografada com chave RSA de 4096 bits.',
  'A classe só pode conter métodos estáticos que retornem booleanos.',
  0,
  'Correto: `sealed` fecha a hierarquia de herança, garantindo que o comportamento da classe não seja modificado por especialização.',
  'Erro conceitual: classes seladas são instanciadas normalmente via `new`.',
  'Erro de segurança e criptografia.',
  'Erro conceitual: classes seladas suportam métodos de qualquer tipo de retorno e visibilidade.',
  'Uma classe selada é como um documento oficial plastificado e carimbado: você pode ler e tirar fotocópias para usar (instanciar e compor), mas ninguém pode acrescentar novos parágrafos na folha (herdar).',
  'Declarar classes como `sealed` previne o problema da classe base frágil e possibilita otimizações de desvirtualização (devirtualization) pelo compilador JIT.')

q(40, '19. Classes e membros selados (sealed).md', 'Sobrescrita selada de métodos', 'dificil',
  'Em C#, é possível aplicar o modificador `sealed` em um método específico? Em que condição isso é válido?',
  'Não, sealed só pode ser aplicado em variáveis globais.',
  'Sim, em métodos que já estejam realizando uma sobreposição (`override`), indicando que subclasses subsequentes na árvore de herança não poderão mais sobrepor esse método.',
  'Sim, em métodos abstratos para forçar a subclasse a não ter corpo de código.',
  'Apenas se o método tiver mais de 5 parâmetros inteiros.',
  1,
  'Erro conceitual: sealed em métodos é recurso suportado e canônico do C#.',
  'Correto: a sintaxe `public sealed override void Metodo()` trava a extensibilidade a partir daquele nível da hierarquia.',
  'Erro conceitual: métodos abstratos exigem implementação por definição; selar um método abstrato geraria um paradoxo sintático impossível.',
  'Erro de sintaxe absurdo.',
  'É como um rei que confirma uma lei antiga do reino e coloca seu selo real final nela: os próximos governadores abaixo dele terão que cumprir a lei exatamente daquela forma, sem autorização para mudar mais nada.',
  'Selar um método sobreposto protege um algoritmo contra adulterações em ramificações mais profundas da hierarquia.')

# 20
q(41, '20. Tipos genéricos (generics, type safety e coleções homogêneas).md', 'Generics e eliminação de boxing/unboxing', 'dificil',
  'Qual é a grande vantagem de desempenho e confiabilidade ao utilizar coleções genéricas (como `List<int>`) em vez das coleções não genéricas arcaicas (como `ArrayList`) em C#?',
  'Coleções genéricas salvam os dados em arquivos CSV no HD automaticamente.',
  'Coleções genéricas garantem segurança de tipos (type safety) em tempo de compilação e eliminam o custo de overhead de boxing e unboxing na manipulação de tipos de valor (structs/primitivos) na memória heap.',
  'Coleções genéricas exigem que todos os elementos sejam strings de no máximo 10 letras.',
  'Não há diferença de desempenho, pois ambas utilizam reflexão dinâmica a cada acesso por índice.',
  1,
  'Erro de persistência em arquivo.',
  'Correto: generics evitam o empacotamento na heap (boxing) e validação manual de casting, reduzindo pressão no GC e falhas de runtime.',
  'Erro conceitual de tipos.',
  'Erro técnico grave: `List<T>` compila código especializado em IL nativo com custo zero de reflexão.',
  'Usar ArrayList antigo é como uma caixa de papelão escura onde você joga qualquer coisa embrulhada em plástico (boxing) e para usar precisa rasgar o plástico e adivinhar o que tem dentro (unboxing com risco de quebrar). List<int> é um organizador de moedas sob medida onde só entram moedas de verdade sem embalagem nenhuma.',
  'Generics foram introduzidos no C# 2.0 e representam um dos maiores avanços de robustez e eficiência da plataforma .NET.')

q(42, '20. Tipos genéricos (generics, type safety e coleções homogêneas).md', 'Restrições de generics (generic constraints)', 'dificil',
  'Em C#, para que servem as cláusulas `where T : class, new()` na declaração de uma classe genérica `Repositorio<T>`?',
  'Para impedir que a classe seja compilada em sistemas operacionais de 64 bits.',
  'Para estabelecer restrições de tipo (constraints), exigindo que o parâmetro genérico `T` seja obrigatoriamente um tipo de referência (`class`) e possua um construtor público sem parâmetros (`new()`), permitindo ao repositório instanciar novos objetos do tipo `T`.',
  'Para forçar que o tipo T seja um arquivo de texto criptografado.',
  'Para permitir apenas números pares na coleção.',
  1,
  'Erro de arquitetura de CPU.',
  'Correto: constraints informam ao compilador capacidades garantidas pelo tipo genérico, permitindo operações como `new T()`.',
  'Erro conceitual de tipos.',
  'Erro de lógica de negócio absurdo.',
  'A cláusula where é o edital de uma vaga de emprego: ela avisa que para concorrer à vaga (usar o parâmetro T), o candidato precisa comprovar que é uma pessoa física (class) e que sabe preencher a própria ficha cadastral sozinho (construtor sem parâmetros new()).',
  'Restrições genéricas ampliam as operações válidas sobre tipos genéricos preservando a verificação estática do compilador.')

# 21
q(43, '21. Coleções genéricas em C# (estruturas de dados, propósitos e performance assintótica).md', 'List vs. LinkedList em C#', 'medio',
  'Qual é a diferença estrutural e de performance assintótica entre `List<T>` e `LinkedList<T>` em C#?',
  '`List<T>` baseia-se em um array redimensionável com acesso por índice em O(1) e inserção no final amortizada em O(1); `LinkedList<T>` é uma lista duplamente encadeada onde o acesso por índice custa O(N), mas inserções/remoções em nós já referenciados custam O(1).',
  '`List<T>` só pode armazenar 10 itens; `LinkedList<T>` armazena até 1 bilhão de itens.',
  '`LinkedList<T>` é alocada no disco SSD; `List<T>` é alocada na memória ROM.',
  'Ambas possuem a mesmíssima estrutura interna de ponteiros encadeados sem diferenças assintóticas.',
  0,
  'Correto: distinção clássica de estruturas de dados: array contíguo vs. nós independentes com ponteiros anterior/próximo.',
  'Erro conceitual de capacidade: ambas crescem dinamicamente conforme a memória disponível.',
  'Erro grosseiro de hardware de armazenamento.',
  'Erro conceitual grave: List é vetor contíguo na heap e LinkedList é lista ligada duplamente encadeada.',
  'List<T> é uma fileira contínua de poltronas numeradas no teatro: você acha a poltrona 42 instantaneamente (O(1)), mas se quiser empurrar alguém no meio, todos para a direita precisam trocar de cadeira. LinkedList<T> é uma roda de ciranda onde cada um dá as mãos para o vizinho: para achar a pessoa 42 você tem que contar um por um desde o início (O(N)), mas para colocar alguém na roda é só soltar as mãos de dois vizinhos e encaixar.',
  'A localidade de referência (cache spatial locality) faz `List<T>` ser consideravelmente mais rápida para quase todos os cenários práticos modernos.')

q(44, '21. Coleções genéricas em C# (estruturas de dados, propósitos e performance assintótica).md', 'Dictionary e complexidade média de busca', 'medio',
  'Qual é a estrutura de dados utilizada internamente pela coleção `Dictionary<TKey, TValue>` em C# e qual o custo computacional médio para busca de elementos?',
  'Árvore binária desbalanceada com custo médio de busca O(N^2).',
  'Tabela hash interna com vetores de baldes (buckets) e cadeias de entradas, proporcionando complexidade assintótica média de busca, inserção e remoção em tempo constante O(1).',
  'Fila sequencial circular com busca em tempo logarítmico O(N!).',
  'Arquivo de banco de dados SQLite embutido em memória RAM.',
  1,
  'Erro conceitual e assintótico.',
  'Correto: Dictionary é uma tabela hash de alto desempenho com dispersão em buckets.',
  'Erro conceitual: complexidade fatorial não tem relação com dicionários hash.',
  'Erro de implementação: Dictionary é uma estrutura nativa do runtime em C#, não um SGBD SQLite embutido.',
  'O dicionário é como a portaria de um condomínio com armários numerados: você diz o número do seu apartamento (chave) e o porteiro vai direto na caixinha correspondente pegar a sua encomenda em um único movimento (O(1)).',
  'Dictionary oferece acesso ultraveloz por chave mediante cálculo de hash code, exigindo que a chave implemente adequadamente GetHashCode() e Equals().')

# 22
q(45, '22. Delegates, funções anônimas, expressões lambda e eventos em C#.md', 'Delegates como ponteiros de função com segurança de tipos', 'dificil',
  'Em C#, o que é tecnicamente um `delegate` e como ele se diferencia de ponteiros de função brutos arcaicos do C/C++?',
  'Um delegate é uma variável global que armazena senhas de usuários em texto plano.',
  'Um delegate é um tipo por referência seguro (type-safe) e gerenciado pelo CLR que encapsula a assinatura e a referência de um ou mais métodos, suportando invocação múltipla (multicast) e captura de instâncias associadas.',
  'Delegates são instruções de compilação que convertem o programa para execução em placas Arduino.',
  'Delegates só aceitam métodos estáticos que não possuam parâmetros.',
  1,
  'Erro de segurança da informação absurdo.',
  'Correto: delegates herdam de `System.MulticastDelegate`, garantindo segurança de tipos na chamada de funções.',
  'Erro de microcontrolador e plataforma.',
  'Erro técnico: delegates suportam métodos de instância (mantendo referência a `target`) e métodos estáticos indistintamente.',
  'Um delegate é como um contrato oficial de procuração: você assina um papel dizendo \'autorizo a execução de qualquer tarefa que tenha esta assinatura específica\'. Quem segurar a procuração pode chamar o método sem saber quem o escreveu.',
  'Delegates são a fundação dos eventos, do LINQ e da programação funcional idiomática em C#.')

q(46, '22. Delegates, funções anônimas, expressões lambda e eventos em C#.md', 'Eventos e o modificador event em C#', 'dificil',
  'Qual é a proteção essencial proporcionada pela palavra-chave `event` ao encapsular um delegate (ex.: `public event EventHandler AoClicar;`) em uma classe?',
  'Ela impede que o evento seja invocado em dias úteis.',
  'Ela restringe o acesso externo aos operadores de inscrição (`+=`) e desinscrição (`-=`), impedindo que assinantes externos invoquem o evento diretamente ou sobrescrevam/limpem a lista de inscritos com uma atribuição direta (`AoClicar = null`).',
  'Ela converte todos os dados do formulário em mensagens SMS enviadas para a operadora telefônica.',
  'Ela força o método de tratamento a ser executado em código binário assembly.',
  1,
  'Erro temporal absurdo.',
  'Correto: o modificador `event` fornece encapsulamento estrito sobre o delegate subjacente, protegendo o publicador contra adulterações externas.',
  'Erro de telecomunicação cômico.',
  'Erro de linguagem: event handlers continuam sendo código IL gerenciado.',
  'É como uma caixa de sugestões na parede da empresa: qualquer pessoa de fora pode colocar um bilhete (inscrever-se via `+=`) ou tirar o seu próprio bilhete (desinscrever-se via `-=`), mas só o dono da empresa pode abrir a caixa e ler todos os bilhetes em voz alta (invocar o evento).',
  'A palavra-chave `event` impede que um consumidor mal-intencionado ou desatento limpe os ouvintes dos outros módulos ou dispare eventos falsos.')

# 23
q(47, '23. Princípios SOLID de design orientado a objetos.md', 'Princípio da Responsabilidade Única (SRP)', 'medio',
  'O Princípio da Responsabilidade Única (SRP), o primeiro do acrônimo SOLID formulado por Robert C. Martin, estabelece que:',
  'Cada classe deve ter apenas uma única linha de código-fonte em seu arquivo.',
  'Uma classe ou módulo deve ter um, e apenas um, motivo para mudar (ou seja, deve ser responsável perante apenas um ator, contexto de negócio ou stakeholder do sistema).',
  'Cada desenvolvedor só pode criar uma única classe durante todo o projeto de software.',
  'O sistema deve rodar em apenas um único núcleo de processador para economizar eletricidade.',
  1,
  'Erro de tamanho de arquivo.',
  'Correto: SRP trata de coesão e fronteiras de mudança ligadas aos atores do negócio.',
  'Erro organizacional absurdo.',
  'Erro de hardware e consumo de energia.',
  'Uma caneta esferográfica serve exclusivamente para escrever: ela não tenta ser canivete, lanterna e rádio ao mesmo tempo. Se o design da lanterna precisar mudar, a caneta não quebra.',
  'Uma classe que mistura cálculo de regras financeiras com persistência em SQL e renderização em HTML viola o SRP e torna-se um monólito frágil.')

q(48, '23. Princípios SOLID de design orientado a objetos.md', 'Princípio Aberto/Fechado (OCP)', 'dificil',
  'Como o Princípio Aberto/Fechado (OCP) orienta a evolução de módulos de software perante novos requisitos de negócio?',
  'Módulos devem estar abertos para extensão (seu comportamento pode ser estendido com novas regras ou subtipos) e fechados para modificação (seu código-fonte existente e já testado não deve ser adulterado a cada nova variação).',
  'O código-fonte deve ser aberto na internet como open source, mas o executável deve ser fechado com senha.',
  'Módulos devem abrir portas de rede TCP e fechar conexões UDP para evitar invasões.',
  'Classes devem ser abertas durante o horário comercial e fechadas aos domingos e feriados.',
  0,
  'Correto: OCP alcança extensibilidade estável utilizando polimorfismo, interfaces e abstrações sem quebrar o código existente.',
  'Erro jurídico de licenciamento de software.',
  'Erro de protocolo de redes de computadores.',
  'Erro cômico e absurdo de horário.',
  'Pense no navegador web com suporte a extensões: você instala uma nova extensão para traduzir textos (aberto para extensão) sem precisar mexer nem recompilar o código-fonte original do navegador (fechado para modificação).',
  'Implemente OCP substituindo grandes estruturas de `switch/case` sobre tipos por polimorfismo dinâmico e injeção de dependências.')

# 24
q(49, '24. Padrões de projeto (design patterns) e o catálogo GoF.md', 'Classificação dos padrões GoF', 'medio',
  'O catálogo clássico dos 23 padrões de projeto do Gang of Four (GoF) organiza os patterns em três famílias fundamentais com base no seu propósito de design. Quais são essas três famílias?',
  'Padrões Analógicos, Padrões Digitais e Padrões Ópticos.',
  'Padrões Criacionais (criação de objetos), Padrões Estruturais (composição de classes e objetos) e Padrões Comportamentais (interação e distribuição de responsabilidades).',
  'Padrões Físicos, Padrões Químicos e Padrões Biológicos.',
  'Padrões de Interface Gráfica, Padrões de Servidor e Padrões de Banco de Dados.',
  1,
  'Erro de física e telecomunicações.',
  'Correto: a divisão canônica do GoF: Criacionais (ex.: Factory, Singleton, Builder), Estruturais (ex.: Adapter, Composite, Decorator) e Comportamentais (ex.: Strategy, Observer, Command).',
  'Erro de ciências naturais.',
  'Erro taxonômico de camadas de software.',
  'Padrões Criacionais são as formas de fundição na fábrica; Padrões Estruturais são as engrenagens e montagens físicas que unem as peças; Padrões Comportamentais são as regras de trânsito que ditam como os carros conversam e se movimentam na rua.',
  'Padrões de projeto fornecem vocabulário comum e soluções consagradas para problemas recorrentes de arquitetura orientada a objetos.')

q(50, '24. Padrões de projeto (design patterns) e o catálogo GoF.md', 'Padrão Strategy vs. Padrão Observer', 'dificil',
  'Na família de padrões comportamentais do GoF, qual é a distinção de propósito entre o padrão Strategy e o padrão Observer?',
  'Strategy desacopla algoritmos intercambiáveis encapsulando cada variação em classes concretas sob uma interface comum; Observer define uma dependência um-para-muitos onde múltiplos objetos assinantes são notificados automaticamente quando o estado do sujeito observado muda.',
  'Strategy só pode ser usado em jogos de tabuleiro; Observer só pode ser usado em telescópios astronômicos.',
  'Strategy é um padrão criacional que substitui o operador new; Observer é um padrão de compressão de arquivos zip.',
  'Ambos são exatamente idênticos e servem apenas para instanciar classes estáticas.',
  0,
  'Correto: Strategy foca na variação algorítmica independente do contexto; Observer foca no mecanismo desacoplado de publicação e assinatura de eventos.',
  'Erro conceitual cômico.',
  'Erro taxonômico: nenhum dos dois é criacional ou de compressão.',
  'Erro conceitual: possuem estruturas e propósitos de interação completamente distintos.',
  'Strategy é como escolher a rota do GPS: você pode ir de carro, a pé ou de bicicleta (o objetivo é o mesmo, mas a estratégia de cálculo muda). Observer é como assinar um jornal diário: sempre que a redação (sujeito) imprime uma nova notícia, todos os assinantes (observadores) recebem uma cópia na sua porta.',
  'Strategy e Observer são dois dos padrões comportamentais mais utilizados na arquitetura limpa e no desenvolvimento de software modular.')

print(f'Total de questões concluídas: {len(questions)}')

# Salvar no JSON da disciplina
with open('/home/antigravity/leorruas/puc/banco-de-questoes/01.programacao-modular.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print('Arquivo 01.programacao-modular.json atualizado com 50 questões com sucesso!')

