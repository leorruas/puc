import json
import os

base_ref = '01. Programacao Modular/'
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
        'id': f'PM-REV-{id_num:03d}',
        'disciplina_id': '01',
        'disciplina': 'Programação Modular',
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
  # Questao 01
  (1, '01. Introdução à programação modular.md',
   'Programação modular e gerenciamento da complexidade', 'facil',
   'Contexto: Uma instituição está substituindo um sistema acadêmico monolítico. No planejamento, a equipe identifica três funcionalidades que evoluem em ritmos diferentes: cadastro de estudantes, matrículas e emissão de relatórios. O coordenador deseja que mudanças em relatórios não exijam reescrever o cadastro.\n\nComando: Considerando esse objetivo de organização e manutenção, qual abordagem de desenvolvimento deve ser adotada?',
   'Eliminação das interfaces entre componentes.',
   'Concentração de todas as operações em um único procedimento extenso.',
   'Programação modular, com decomposição em componentes coesos.',
   'Duplicação integral do código em cada funcionalidade.',
   2,
   'Incorreto: interfaces bem definidas sao essenciais para desacoplar modulos.',
   'Incorreto: concentrar operacoes em bloco unico gera monolitos dificeis de testar e manter.',
   'Correto: a programacao modular divide o sistema em partes menores (modulos), cada qual com alta coesao e baixo acoplamento, permitindo manutencoes isoladas e evolucao independente.',
   'Incorreto: duplicacao de codigo viola o principio DRY (Dont Repeat Yourself) e gera inconsistencias.',
   'Pense em blocos de montar Lego ou componentes de um computador: se a placa de video estragar ou precisar de um upgrade, voce troca apenas ela sem precisar soldar uma nova placa-mae ou jogar fora o monitor.',
   'A decomposicao modular (proposta pioneiramente por Parnas e Dijkstra) estabelece que modulos devem encapsular decisoes de projeto independentes, minimizando o impacto de mudancas atraves de interfaces estaveis.'),

  # Questao 02
  (2, '05. Fatores externos de qualidade de software.md',
   'Fatores externos de qualidade de software', 'facil',
   'Contexto: Depois de implantar um aplicativo de atendimento, uma escola pergunta aos usuários se as funções estão corretas e se as tarefas podem ser realizadas de maneira satisfatória. Os avaliadores não têm acesso ao código-fonte; observam apenas o comportamento do produto durante seu uso.\n\nComando: A partir dessa forma de avaliação, qual grupo de fatores de qualidade está sendo considerado?',
   'Internos, por examinarem a organização do código-fonte.',
   'Exclusivamente sintáticos, por dependerem do compilador.',
   'De infraestrutura, sem relação com a qualidade do software.',
   'Externos, por serem percebidos por quem utiliza o produto.',
   3,
   'Incorreto: fatores internos dizem respeito a arquitetura e elegancia do codigo, invisiveis ao usuario final.',
   'Incorreto: aspectos sintaticos sao verificados em compilacao, nao na experiencia de operacao do usuario.',
   'Incorreto: corretude e usabilidade sao fatores centrais de qualidade do software.',
   'Correto: fatores externos (conforme Bertrand Meyer) sao aqueles diretamente perceptiveis pelos usuarios no uso do sistema (ex.: corretude, robustez, facilidade de uso, eficiencia perceptivel).',
   'E como avaliar um carro fazendo um test-drive: o motorista avalia o conforto dos bancos, o ar-condicionado e a firmeza dos freios (fatores externos), mesmo sem entender nada de como os pistoes foram usinados na fabrica (fatores internos).',
   'A distincao de Meyer enfatiza que os fatores internos (modularidade, legibilidade) sao os meios necessarios para alcancar os fatores externos (confiabilidade, manutenibilidade para o usuario final).'),

  # Questao 03
  (3, '06. Fatores internos de qualidade de software.md',
   'Legibilidade, modularidade e manutenibilidade', 'medio',
   'Contexto: Uma empresa recebe um sistema cuja manutenção leva semanas, embora as mudanças solicitadas sejam pequenas. A análise técnica revela métodos extensos, responsabilidades misturadas e nomes pouco expressivos. A equipe decide refatorar o código antes de ampliar as funcionalidades.\n\nComando: Quais fatores de qualidade são diretamente priorizados por essa decisão?',
   'Apenas aparência visual e satisfação do usuário.',
   'Escalabilidade geográfica e largura de banda.',
   'Fatores internos como legibilidade, modularidade e manutenibilidade.',
   'Privacidade de rede e transmissão de pacotes.',
   2,
   'Incorreto: aparencia visual e fator externo de interface com o usuario.',
   'Incorreto: escalabilidade geografica refere-se a infraestrutura de telecomunicacoes e distribuicao.',
   'Correto: refatorar metodos longos, separar responsabilidades e melhorar nomenclatura atacam diretamente os fatores internos de qualidade (legibilidade, modularidade, testabilidade e manutenibilidade).',
   'Incorreto: privacidade de rede e protocolo de seguranca de comunicacao.',
   'Pense na fiaçao eletrica dentro da parede de uma casa: se os fios estiverem todos emaranhados e sem etiquetas, o eletricista gasta horas para consertar uma simples tomada. Arrumar a fiacao e refatorar os fatores internos para facilitar reparos futuros.',
   'Os fatores internos de qualidade sao avaliados pela equipe de engenharia e afetam diretamente a velocidade de entrega (*time-to-market*) e a taxa de insercao de bugs em manutenções corretivas e evolutivas.'),

  # Questao 04
  (4, '06. Fatores internos de qualidade de software.md',
   'Coesão, dependências e manutenibilidade', 'dificil',
   'Contexto: Em um sistema de pagamentos, os módulos de emissão de comprovantes e cálculo de taxas foram criados por equipes diferentes. Apesar disso, ambos dependem de detalhes internos um do outro: alterar uma regra de cálculo exige modificar também o módulo de comprovantes. A equipe busca reduzir esse efeito em cascata.\n\nComando: Qual intervenção de projeto é a mais adequada para melhorar a qualidade interna do sistema?',
   'Substituir nomes descritivos por abreviações para diminuir o tamanho do código.',
   'Aumentar o compartilhamento de detalhes internos para facilitar alterações simultâneas.',
   'Definir responsabilidades mais claras e reduzir dependências desnecessárias entre módulos.',
   'Reunir todos os módulos em uma única classe sem divisão de responsabilidades.',
   2,
   'Incorreto: abreviacoes obscuras prejudicam a legibilidade sem resolver acoplamento.',
   'Incorreto: expor detalhes internos aumenta ainda mais o acoplamento nocivo.',
   'Correto: delimitar fronteiras claras de responsabilidade (alta coesao) e reduzir o acoplamento entre os modulos elimina efeitos colaterais em cascata.',
   'Incorreto: agrupar tudo em classe monolitica cria a antipattern God Class.',
   'Se você mudar a tomada da sua sala de dois pinos para o padrao novo de tres pinos, a TV continua funcionando normalmente atraves do plugue padronizado (interface), sem você precisar abrir a TV e trocar seus circuitos internos.',
   'O principio de baixo acoplamento e alta coesao garante que cada modulo tenha um unico proposito bem definido e se comunique exclusivamente por contratos estaveis de interface, prevenindo mudancas em cascata.'),

  # Questao 05
  (5, '07. Atributos e métodos (classes, objetos e definição de membros).md',
   'Classes, objetos, atributos e métodos', 'facil',
   'Contexto: Uma loja está informatizando seu estoque. Ao observar as regras de negócio, os desenvolvedores identificam que cada produto possui descrição, preço e quantidade disponível, além de uma operação para verificar se ainda pode ser vendido. Essas informações serão representadas por uma classe Produto.\n\nComando: Na modelagem orientada a objetos, como esses elementos devem ser classificados?',
   'Descrição, preço e quantidade são atributos; verificar estoque é método.',
   'Descrição e preço são métodos; verificar estoque é atributo.',
   'A classe Produto é um único valor numérico sem comportamento.',
   'Cada produto é obrigatoriamente uma classe diferente.',
   0,
   'Correto: atributos sao variaveis que armazenam o estado do objeto (descricao, preco, quantidade), enquanto metodos sao funcoes/procedimentos que definem o comportamento (verificarEstoque).',
   'Incorreto: caracteristicas estruturais de dados sao atributos, nao metodos.',
   'Incorreto: uma classe e um molde completo que engloba dados e metodos de comportamento.',
   'Incorreto: produtos individuais sao instancias (objetos) de uma unica classe generica Produto.',
   'Pense em um carro: a cor, a placa e o nivel de combustivel sao os atributos; dar partida, acelerar e frear sao os metodos.',
   'Em linguagens orientadas a objetos como C# e Java, classes atuam como tipos definidos pelo usuario, estruturando estado em campos/propriedades e operacoes em membros de metodo.'),

  # Questao 06
  (6, '07. Atributos e métodos (classes, objetos e definição de membros).md',
   'Identidade, estado e comportamento dos objetos', 'medio',
   'Contexto: Em um sistema de almoxarifado, dois registros de produtos têm a mesma descrição e o mesmo preço, mas correspondem a unidades cadastradas separadamente. Durante os testes, um estudante conclui que valores iguais significam que os objetos são a mesma instância.\n\nComando: Qual afirmação corrige essa interpretação sobre estado e identidade dos objetos?',
   'Objetos podem compartilhar valores de atributos e continuar sendo instâncias distintas.',
   'Métodos definem a identidade, e atributos não podem armazenar estado.',
   'Uma classe não pode gerar mais de uma instância.',
   'Objetos com o mesmo estado possuem necessariamente a mesma identidade.',
   0,
   'Correto: a identidade de um objeto independe de seu estado; dois objetos alocados em posicoes distintas na memoria heap continuam sendo entidades individuais, mesmo que todos os seus atributos possuam valores identicos.',
   'Incorreto: a identidade e determinada pelo endereco ou referencia do objeto em memoria, e atributos sao exatamente o que armazena estado.',
   'Incorreto: uma classe pode gerar infinitas instancias distintas em memoria.',
   'Incorreto: confunde igualdade de conteudo (valor de estado) com igualdade de referencia (identidade de instancia).',
   'Pense em gemeos univitelinos: eles tem o mesmo sobrenome, a mesma altura e a mesma cor de olhos (mesmo estado), mas continuam sendo duas pessoas fisicas diferentes com CPFs e certidoes de nascimento separadas (identidades distintas).',
   'Em C#, o operador `==` em tipos de referencia compara a identidade (enderecos de memoria por padrao), enquanto o metodo `.Equals()` pode ser sobrescrito para comparar equivalencia de estado de negocio.'),

  # Questao 07
  (7, '08. Construtores (inicialização, sobrecarga e garantia de invariantes).md',
   'Construtores e inicialização de atributos', 'medio',
   'Contexto: O sistema de uma papelaria apresenta falhas porque alguns objetos Produto são criados sem descrição ou com valores iniciais inválidos. A equipe estabelece que essas condições devem ser verificadas no momento da criação de cada objeto, antes de seu uso pelas demais funcionalidades.\n\nComando: Qual recurso de programação orientada a objetos atende diretamente a essa necessidade?',
   'Namespace que define a ordem de criação dos objetos.',
   'Destrutor que é executado antes da criação do objeto.',
   'Método estático que altera todas as instâncias indiscriminadamente.',
   'Construtor que recebe e valida os dados necessários à inicialização.',
   3,
   'Incorreto: namespaces organizam escopo de nomes de tipos, sem executar logica de instanciacao.',
   'Incorreto: destrutores sao executados ao final do ciclo de vida do objeto para liberacao de recursos, nunca antes da criacao.',
   'Incorreto: metodos estaticos nao sao disparados automaticamente na alocacao de uma nova instancia.',
   'Correto: o construtor e o metodo especial invocado no ato da instanciacao (`new`), sendo o local ideal para receber parametros obrigatorios, aplicar validacoes e garantir que o objeto nasca em estado valido (invariante de classe).',
   'E como a certidao de nascimento no cartorio: o bebe so sai registrado se os pais informarem nome e data validos; o cartorio nao deixa criar um registro em branco.',
   'O construtor garante o principio de invariante de classe: nenhum objeto deve existir na memoria em estado inconsistente ou sem inicializacao de membros essenciais.'),

  # Questao 08
  (8, '09. Atributos estáticos e propriedades (compartilhamento de estado e encapsulamento).md',
   'Membros estáticos e membros de instância', 'medio',
   'Contexto: Uma aplicação de monitoramento cria centenas de objetos de uma mesma classe durante sua execução. O responsável técnico precisa exibir um indicador geral com a quantidade de objetos criados, e esse valor deve ser único para a classe, não um contador independente em cada instância.\n\nComando: Qual implementação é compatível com esse requisito?',
   'Substituir o contador por um destrutor sem estado compartilhado.',
   'Declarar um membro estático da classe para armazenar o contador.',
   'Declarar o contador como variável local em cada método de consulta.',
   'Copiar o contador para cada instância sem sincronizar os valores.',
   1,
   'Incorreto: destrutores nao gerenciam contagem compartilhada persistente.',
   'Correto: membros estaticos (`static`) pertencem a propria classe e sao compartilhados por todas as instancias daquele tipo, mantendo uma copia unica na memoria para a contagem global.',
   'Incorreto: variaveis locais sao destruidas assim que o metodo finaliza sua execucao.',
   'Incorreto: campos de instancia mantem copias isoladas em cada objeto, impedindo um acumulador global.',
   'Pense em um predio com 50 apartamentos: a caixa de correspondencia na portaria e compartilhada por todo o condominio (estatica), enquanto a geladeira dentro de cada apartamento pertence apenas aquela casa (de instancia).',
   'Campos estaticos sao alocados uma unica vez na area de metadados da CLR quando a classe e carregada, permanecendo acessiveis sem necessidade de referenciar uma instancia especifica (`Classe.Contador`).'),

  # Questao 09
  (9, '10. Destrutores e finalizadores (desalocação de memória e liberação de recursos).md',
   'Destrutores e gerenciamento de memória no C#', 'medio',
   'Contexto: Ao investigar o consumo de memória de uma aplicação C#, a equipe observa que alguns objetos deixaram de ser referenciados após o encerramento de operações. Um desenvolvedor afirma que a memória de cada objeto é necessariamente liberada no instante exato em que a última referência desaparece.\n\nComando: Considerando o gerenciamento de memória em C#, qual conclusão é tecnicamente adequada?',
   'O programador precisa chamar diretamente o destrutor em toda remoção de referência.',
   'O destrutor substitui a execução automática do coletor de lixo.',
   'O coletor de lixo pode liberar objetos não alcançáveis em momento posterior.',
   'A memória é sempre liberada no mesmo instante em que sai do escopo.',
   2,
   'Incorreto: em C#, o desenvolvedor nao pode invocar destrutores/finalizadores manualmente.',
   'Incorreto: o Garbage Collector e quem gerencia a chamada de finalizadores na fila de finalizacao.',
   'Correto: o gerenciamento de memoria gerenciada no .NET e nao deterministico; o Garbage Collector (GC) roda periodicamente em momentos oportunos para coletar objetos inalcançaveis, sem garantia de liberacao instantanea.',
   'Incorreto: desalocacao imediata ao sair do escopo e caracteristica de ponteiros manuais (C++) ou RAII estrito, nao da memoria gerenciada do C#.',
   'Pense no caminhao de lixo do bairro: quando voce joga uma casca de banana na lixeira da calcada, o caminhao nao passa imediatamente naquele segundo; ele passa na rota programada dele mais tarde para recolher tudo de uma vez.',
   'O coletor de lixo do C# opera por geracoes (Gen 0, 1 e 2). Para recursos nao gerenciados que exigem liberacao deterministica (arquivos, sockets), deve-se implementar o padrao `IDisposable` com o bloco `using`.'),

  # Questao 10
  (10, '11. Princípio da ocultação da informação (information hiding e encapsulamento).md',
   'Ocultação da informação e encapsulamento', 'facil',
   'Contexto: Em um sistema bancário didático, uma alteração direta no campo saldo permitiu registrar um valor inconsistente, sem verificar as regras de negócio. Para impedir novas ocorrências, a equipe decidiu restringir a exposição do estado interno e disponibilizar operações controladas para as alterações.\n\nComando: Que princípio orienta essa decisão de projeto?',
   'Herança múltipla de atributos.',
   'Instanciação de classes abstratas.',
   'Encapsulamento e ocultação da informação.',
   'Substituição de métodos virtuais.',
   2,
   'Incorreto: heranca multipla trata de derivacao de classes e nem e suportada para classes concretas em C#.',
   'Incorreto: classes abstratas nao podem ser instanciadas diretamente.',
   'Correto: o principio de encapsulamento e ocultacao da informacao (*information hiding*) determina que o estado interno do objeto deve ser protegido contra manipulacoes externas diretas, expondo apenas metodos ou propriedades seguras.',
   'Incorreto: substituicao de metodos virtuais refere-se a polimorfismo dinamico.',
   'Pense em um caixa eletronico de banco: você nao abre a gaveta do cofre com uma chave de fenda para pegar as notas com a mao; você usa o teclado e a tela (interface publica), e a maquina confere sua senha e seu saldo antes de soltar o dinheiro.',
   'David Parnas formulou a ocultacao da informacao para assegurar que detalhes volateis de implementacao e regras de consistencia interna fiquem ocultos atras de contratos estaveis.'),

  # Questao 11
  (11, '12. Modificadores de acesso (visibilidade e níveis de proteção no encapsulamento).md',
   'Modificadores de acesso em C# (private)', 'medio',
   'Contexto: Durante a revisão de uma classe Conta em C#, percebeu-se que qualquer outra classe do projeto poderia atribuir um valor ao campo saldo. A nova regra exige que apenas os métodos definidos na própria classe Conta tenham acesso direto a esse campo.\n\nComando: Qual modificador de acesso deve ser aplicado ao campo para atender à regra?',
   'public.',
   'protected, que proíbe acesso também nas subclasses.',
   'internal, que equivale a acesso exclusivo na classe.',
   'private.',
   3,
   'Incorreto: `public` torna o campo acessivel a qualquer classe externa.',
   'Incorreto: `protected` permite acesso pelas subclasses derivadas.',
   'Incorreto: `internal` permite acesso a qualquer classe dentro do mesmo assembly/projeto.',
   'Correto: o modificador `private` restringe a visibilidade do membro estritamente ao escopo interno do corpo da propria classe onde foi declarado.',
   'Pense no seu diario pessoal: so você mesmo tem permissao de ler e escrever nele (private). Se você colocasse em uma mesa aberta na praca, qualquer pessoa poderia mexer (public).',
   'Em C#, o nivel de acesso padrao para membros de classe e `private`, forcando o desenvolvedor a declarar explicitamente qualquer exposicao publica controlada.'),

  # Questao 12
  (12, '13. Métodos de acesso e propriedades (publicação de contratos e garantia de invariantes).md',
   'Getters, setters e validação em propriedades', 'medio',
   'Contexto: Uma aplicação controla o estoque de medicamentos e exige que a quantidade cadastrada nunca seja negativa. O valor precisa continuar disponível para consulta, mas toda atualização deve passar por uma verificação antes de ser aceita.\n\nComando: Qual estratégia de implementação de propriedade melhor garante essa regra?',
   'Usar acesso controlado e validar o novo valor no setter.',
   'Permitir atualização do valor somente no destrutor.',
   'Guardar a quantidade exclusivamente em um membro estático compartilhado.',
   'Tornar o campo público e aceitar qualquer alteração.',
   0,
   'Correto: em C#, propriedades com assessor `set` permitem interceptar a atribuicao, validar se o `value` atende a regra de negocio (ex.: `value >= 0`) e rejeitar alteracoes inconsistentes.',
   'Incorreto: destrutores nao sao chamados em operacoes de negocio do estoque.',
   'Incorreto: membro estatico compartilharia a mesma quantidade entre todos os remedios da farmacia.',
   'Incorreto: campo publico permite que qualquer codigo atribua valores negativos livremente.',
   'E como a catraca de um onibus: qualquer um pode olhar para ver se a catraca esta livre (getter), mas para passar para o outro lado, a catraca exige que voce passe um cartao com saldo valido (setter com validacao).',
   'Propriedades encapsulam campos de suporte (*backing fields*), oferecendo a aparencia sintatica de campo direto com o poder de execucao de metodos de validacao de invariantes.'),

  # Questao 13
  (13, '14. Namespaces e partial classes (espaços de nomes e modularização em larga escala).md',
   'Namespaces e classes parciais', 'medio',
   'Contexto: Uma equipe mantém uma aplicação C# com dezenas de classes. Para evitar conflitos de nomes, pretende agrupá-las por áreas funcionais; além disso, quer dividir a implementação de uma classe extensa em dois arquivos, mantendo uma única definição lógica da classe.\n\nComando: Quais recursos da linguagem atendem, respectivamente, a essas duas necessidades?',
   'Modificadores sealed e override.',
   'Delegates e destrutores.',
   'Namespaces e declaração partial.',
   'Construtores e métodos abstratos.',
   2,
   'Incorreto: sealed e override tratam de heranca e polimorfismo.',
   'Incorreto: delegates e destrutores tratam de ponteiros de funcao e desalocacao de recursos.',
   'Correto: `namespaces` criam espacos de nomes hierarquicos que evitam colisoes de nomes, e o modificador `partial` permite que a definicao de uma classe seja fracionada em multiplos arquivos de codigo-fonte compilados como uma unica unidade.',
   'Incorreto: construtores inicializam dados e metodos abstratos definem contratos nao implementados.',
   'O namespace e como o sobrenome de uma familia para nao confundir o "Joao da Silva" com o "Joao Santos"; a classe partial e como escrever um capitulo de um livro em duas folhas de papel diferentes, mas que continuam formando o mesmo capitulo.',
   'Classes parciais (`partial class`) sao amplamente utilizadas em geradores de codigo (.NET Windows Forms, WPF e Entity Framework) para separar o codigo gerado por ferramentas da logica manual do desenvolvedor.'),

  # Questao 14
  (14, '15. Herança (generalização, especialização e extensibilidade modular).md',
   'Generalização, especialização e herança', 'medio',
   'Contexto: Uma locadora mantém objetos Carro e Motocicleta. Ambos possuem modelo e ano, mas cada tipo também apresenta operações específicas. Na revisão do projeto, identificou-se duplicação dos atributos comuns e decidiu-se criar uma classe Veiculo para reuni-los.\n\nComando: Como essa decisão deve ser interpretada em termos de generalização, especialização e herança?',
   'Veiculo generaliza Carro e Motocicleta, que o especializam.',
   'Veiculo é uma instância de Carro.',
   'Cada veículo deve duplicar os atributos sem compartilhar uma classe-base.',
   'Carro e Motocicleta são métodos de Veiculo.',
   0,
   'Correto: `Veiculo` atua como a classe-base mais geral (generalizacao), enquanto `Carro` e `Motocicleta` sao classes derivadas que herdam os atributos comuns e acrescentam caracteristicas particulares (especializacao).',
   'Incorreto: Veiculo e uma classe conceitual mais ampla, nao um objeto/instancia.',
   'Incorreto: a duplicacao foi eliminada intencionalmente pela heranca.',
   'Incorreto: Carro e Motocicleta sao tipos/classes, nao funcoes executaveis.',
   'Na biologia, "Animal" generaliza "Cachorro" e "Passaro"; "Cachorro" especializa "Animal", herdando a condicao de respirar e ter celulas, mas acrescentando a habilidade exclusiva de latir.',
   'A heranca implementa a relacao "e-um" (*is-a*), permitindo que subclasses reutilizem codigo da superclasse e sejam tratadas polimorficamente por meio da referencia da classe-base.'),

  # Questao 15
  (15, '16. Construtores em classes filhas (ordem de inicialização e a cláusula base).md',
   'Construtores de subclasses e chamada a base', 'dificil',
   'Contexto: Um sistema de recursos humanos define a classe Funcionario com um construtor responsável por receber e validar o nome. A classe Gerente herda Funcionario e acrescenta o setor de atuação. Ao criar um Gerente, é necessário inicializar corretamente os dados herdados e os dados específicos.\n\nComando: Qual estratégia de construção deve ser empregada em C# para aproveitar a inicialização da classe-base?',
   'Ignorar o construtor da classe-base, que jamais é executado.',
   'Chamar manualmente o destrutor da classe-base.',
   'Encaminhar o nome ao construtor da classe-base usando base(...).',
   'Tornar todos os atributos herdados estáticos.',
   2,
   'Incorreto: o construtor da classe-base e sempre executado obrigatoriamente antes do corpo da classe derivada.',
   'Incorreto: destrutores desalocam objetos, nao inicializando membros.',
   'Correto: a palavra-chave `: base(nome)` na declaracao do construtor da subclasse repassa explicitamente os argumentos necessarios para o construtor correspondente da classe-base.',
   'Incorreto: atributos estaticos compartilhariam o mesmo nome entre todos os gerentes da empresa.',
   'Pense na construcao de um sobrado: antes de erguer as paredes do segundo andar (classe filha Gerente), os pedreiros precisam assentar a fundacao e as paredes do primeiro andar (classe-base Funcionario).',
   'Em C#, se a superclasse nao tiver um construtor padrao sem parametros, a classe filha e sintaticamente obrigada a declarar a chamada explicita `: base(...)` em seus construtores.'),

  # Questao 16
  (16, '17. Sobreposição de métodos (virtual e override).md',
   'Polimorfismo; virtual e override', 'medio',
   'Contexto: Uma empresa produz relatórios comuns e financeiros. A classe Relatorio já disponibiliza o método virtual Gerar(), mas o relatório financeiro precisa adaptar a geração ao seu formato, mantendo o comportamento polimórfico previsto pela hierarquia.\n\nComando: Qual recurso permite à subclasse fornecer essa implementação específica?',
   'Substituir a classe derivada por uma variável local.',
   'Usar sealed na classe-base para permitir novas sobrescritas.',
   'Declarar Gerar() como private static na classe-base.',
   'Implementar Gerar() na classe derivada com override.',
   3,
   'Incorreto: variaveis locais nao herdam nem sobrescrevem metodos polimorficos.',
   'Incorreto: `sealed` bloqueia a sobrescrita, impedindo novas especializacoes.',
   'Incorreto: metodos privados e estaticos nao podem ser virtuais nem participam de polimorfismo dinamico.',
   'Correto: o par `virtual` (na classe-base) e `override` (na classe derivada) viabiliza o polimorfismo por sobrescrita dinamica, fazendo com que a chamada em tempo de execucao invoque o comportamento da classe concreta.',
   'Pense no comando "tocar som" de um instrumento musical: o instrumento base tem a intencao (virtual), mas a flauta assopra (override) e o tambor bate (override). Quem ouve a musica apenas manda o instrumento tocar.',
   'A ligacao tardia (*late binding*) utiliza a tabela de metodos virtuais (vtable) da CLR para despachar a chamada ao metodo sobrescrito pelo tipo real da instancia alocada na memoria heap.'),

  # Questao 17
  (17, '18. Classes abstratas e métodos abstratos (contratos de herança e polimorfismo puro).md',
   'Classes e métodos abstratos', 'medio',
   'Contexto: Uma aplicação gráfica trabalha com círculos e retângulos. Todas as formas devem oferecer a operação CalcularArea(), mas a regra do cálculo depende do tipo concreto. A equipe quer definir um contrato comum e impedir a criação de objetos de uma forma genérica sem implementação.\n\nComando: Qual modelagem atende simultaneamente a essas condições?',
   'Delegate sem método associado.',
   'Classe abstrata com método abstrato.',
   'Classe sealed com método estático.',
   'Classe comum com todos os atributos públicos.',
   1,
   'Incorreto: delegates desacoplam chamadas de funcao mas nao representam hierarquias de classes graficas.',
   'Correto: uma classe abstrata (`abstract class`) nao pode ser instanciada diretamente e pode conter metodos abstratos (`abstract method`) sem corpo, forcando todas as subclasses concretas a implementarem o metodo.',
   'Incorreto: classes seladas proíbem heranca, impedindo que circulos e retangulos derivem dela.',
   'Incorreto: classe comum permitiria instanciar uma "Forma" vazia sem formulas de area conhecidas.',
   'Pense na ideia generica de "Documento Oficial": nao existe um documento que seja apenas "documento"; ele precisa ser algo concreto como um RG, CNH ou Passaporte. O conceito e abstrato, mas exige campos concretos.',
   'Classes abstratas servem como raizes de hierarquias polimorficas quando certos comportamentos conceituais sao obrigatorios mas nao possuem implementacao logica comum na base.'),

  # Questao 18
  (18, '19. Classes e membros selados (sealed).md',
   'Classes sealed e membros sealed override', 'medio',
   'Contexto: Uma biblioteca de componentes C# contém uma classe cuja lógica foi concluída e verificada. Seus mantenedores não desejam permitir que outros desenvolvedores criem subclasses para modificar ou ampliar o comportamento dessa classe.\n\nComando: Qual recurso da linguagem expressa diretamente essa restrição de herança?',
   'Declarar a classe como abstract.',
   'Marcar apenas todos os campos como public.',
   'Declarar todos os métodos como virtual.',
   'Declarar a classe como sealed.',
   3,
   'Incorreto: `abstract` forca a criacao de subclasses para que a classe possa ser usada.',
   'Incorreto: campos publicos expositivos quebram o encapsulamento sem impedir derivacao.',
   'Incorreto: metodos virtuais convidam expressamente a sobrescrita por heranca.',
   'Correto: a palavra-chave `sealed` em C# impede que outras classes herdem daquela classe, garantindo a imutabilidade do design e permitindo otimizacoes de compilacao (como *devirtualization*).',
   'E como passar lacre de seguranca inviolavel em uma caixa de encomendas: uma vez selada (sealed), ninguem mais pode abrir para embutir coisas novas la dentro.',
   'Classes como `System.String` no .NET sao declaradas como `sealed` por razoes criticas de seguranca e desempenho, evitando que subclasses subvertam operacoes fundamentais de texto.'),

  # Questao 19
  (19, '20. Tipos genéricos (generics, type safety e coleções homogêneas).md',
   'Tipos genéricos e polimorfismo paramétrico', 'medio',
   'Contexto: Três módulos de uma aplicação utilizam repositórios para armazenar produtos, clientes e pedidos. As operações são praticamente idênticas, mas a equipe quer evitar três implementações copiadas e, ao mesmo tempo, manter a verificação de tipos em tempo de compilação.\n\nComando: Qual solução de programação atende melhor a esses requisitos?',
   'Definir uma classe genérica Repositorio<T> com tipo parametrizado.',
   'Converter todos os elementos em valores numéricos arbitrários.',
   'Usar exclusivamente campos string para todo tipo de dado.',
   'Duplicar manualmente as operações em três classes sem parametrização.',
   0,
   'Correto: tipos genericos (*generics*) permitem parametrizar classes e metodos com um tipo `T`, viabilizando maximo reuso de codigo de logica comum com seguranca estatica de tipos (*type safety*) e sem custo de *boxing/unboxing*.',
   'Incorreto: conversao para inteiros perde semantica, seguranca e orientacao a objetos.',
   'Incorreto: transformar tudo em string perde tipagem e exige conversoes manuais perigosas.',
   'Incorreto: duplicacao manual viola principios de manutencao e reaproveitamento.',
   'Pense em uma forma de bolo: a forma tem o mesmo desenho e funcao, mas você pode despejar massa de chocolate, cenoura ou fuba (`Forma<Chocolate>`, `Forma<Cenoura>`), sem precisar inventar uma forma mecanica diferente para cada receita.',
   'Os Generics do C# preservam a informacao do tipo real em tempo de execucao (reificacao de tipos na CLR), proporcionando alto desempenho com verificacao estrita em tempo de compilacao.'),

  # Questao 20
  (20, '21. Coleções genéricas em C# (estruturas de dados, propósitos e performance assintótica).md',
   'Listas e operações em coleções', 'facil',
   'Contexto: Um pequeno comércio começou a desenvolver seu sistema de estoque. A quantidade de produtos cadastrados varia ao longo do tempo e o programa precisa inserir, consultar e remover objetos Produto sem criar manualmente um campo para cada registro.\n\nComando: Qual estrutura estudada em C# é apropriada para esse armazenamento?',
   'Uma classe sealed sem qualquer armazenamento.',
   'Um construtor de Produto usado como banco de dados.',
   'Uma propriedade booleana sem objetos associados.',
   'Uma coleção, como List<Produto>.',
   3,
   'Incorreto: classe vazia nao armazena dados dinamicos.',
   'Incorreto: construtor instancia um unico objeto, nao atuando como colecao de multiplos itens.',
   'Incorreto: tipo booleano so armazena true ou false.',
   'Correto: `List<Produto>` e uma colecao generica dinamica baseada em array redimensionavel que permite adicionar (`Add`), remover (`Remove`) e iterar sobre uma quantidade variavel de elementos com tipagem estrita.',
   'Pense em uma pasta sanfonada: você pode colocar uma ficha de produto hoje, adicionar mais dez amanha e tirar duas depois; a pasta expande e encolhe conforme a necessidade.',
   'Diferente de arrays primitivos de tamanho fixo, `List<T>` encapsula a realocacao de capacidade automaticamente conforme o numero de elementos ultrapassa o limite interno.'),

  # Questao 21
  (21, '21. Coleções genéricas em C# (estruturas de dados, propósitos e performance assintótica).md',
   'Dicionários e coleções genéricas', 'dificil',
   'Contexto: Uma plataforma comercial realiza milhares de consultas de produtos por um código inteiro único. A implementação atual percorre uma lista inteira até encontrar cada código, aumentando o trabalho necessário à medida que o catálogo cresce. A equipe quer associar diretamente cada código ao respectivo objeto.\n\nComando: Qual estrutura de dados se ajusta melhor a essa necessidade?',
   'Um Dictionary<int, Produto> com código como chave.',
   'Um array de tamanho zero com referências para todos os produtos.',
   'Um delegate que armazena todos os produtos em uma variável.',
   'Uma lista sem nenhum índice de consulta.',
   0,
   'Correto: o `Dictionary<TKey, TValue>` implementa uma tabela hash onde a chave (`int`) e mapeada diretamente para o valor (`Produto`), proporcionando busca quase instantanea em complexidade media O(1).',
   'Incorreto: array de tamanho zero nao armazena nenhum item.',
   'Incorreto: delegates sao ponteiros para metodos, nao estruturas de armazenamento de catalogos.',
   'Incorreto: listas nao indexadas exigem busca linear O(n), exatamente o problema de lentidao que se quer resolver.',
   'Pense em um armario de correios com escaninhos numerados: em vez de revirar uma pilha de 10.000 cartas para achar a sua, você vai direto no escaninho com o numero do seu apartamento (chave) e pega a sua encomenda na hora (O(1)).',
   'O dicionario utiliza funcoes hash internas para computar o indice do balde (*bucket*) correspondente a chave, eliminando a necessidade de varredura sequencial elemento por elemento.'),

  # Questao 22
  (22, '22. Delegates, funções anônimas, expressões lambda e eventos em C#.md',
   'Delegates, lambda e eventos', 'dificil',
   'Contexto: Em uma aplicação de pedidos, a conclusão de uma compra deve acionar rotinas distintas: registrar uma notificação, atualizar a interface e enviar uma mensagem. O componente que finaliza a compra não deve conhecer diretamente a implementação de cada rotina interessada.\n\nComando: Qual mecanismo da linguagem C# permite organizar essa comunicação desacoplada?',
   'Um namespace que executa métodos automaticamente.',
   'Uma classe sealed que proíbe qualquer comunicação entre objetos.',
   'Um evento associado a delegates, com tratadores que podem usar lambdas.',
   'Um construtor privado chamado após cada clique.',
   2,
   'Incorreto: namespaces organizam nomes, nao disparando fluxos reativos em runtime.',
   'Incorreto: classe selada impede heranca, nao tendo relacao com envio de mensagens assincronas ou desacopladas.',
   'Correto: o padrao de eventos (`event`) baseado em delegates do C# implementa o padrao Observer, permitindo que multiplos assinantes se cadastrem para serem notificados quando a acao ocorrer sem acoplamento direto.',
   'Incorreto: construtor privado impede a instanciacao livre por outras classes.',
   'Pense no sino de uma igreja: o sineiro apenas puxa a corda e faz o sino tocar (evento). Os moradores da vila escutam o sino e cada um faz o que precisa (um vai para a missa, outro olha o relogio), sem o sineiro precisar bater de porta em porta.',
   'O modificador `event` protege o delegate subjacente, permitindo que clientes externos utilizem apenas os operadores de inscricao `+=` e desinscricao `-=`, garantindo o encapsulamento da lista de disparos.'),

  # Questao 23
  (23, '23. Princípios SOLID de design orientado a objetos.md',
   'SOLID: princípio da responsabilidade única (SRP)', 'medio',
   'Contexto: Uma classe de um sistema universitário cadastra estudantes, produz relatórios e envia mensagens automáticas. Após algumas atualizações, a equipe percebe que mudanças em qualquer uma dessas funções exigem alterar e testar toda a classe, mesmo quando as demais funções não mudaram.\n\nComando: Qual princípio SOLID orienta a reorganização dessas responsabilidades?',
   'Princípio da segregação de interfaces, pois todos os atributos devem ser públicos.',
   'Princípio da substituição de Liskov, pois todas as atividades formam hierarquias.',
   'Princípio da responsabilidade única, por concentrar em cada classe um motivo principal de mudança.',
   'Princípio da inversão de dependência, que exige uma única classe para o sistema.',
   2,
   'Incorreto: ISP trata de dividir interfaces extensas em interfaces especificas menores.',
   'Incorreto: LSP assegura que subclasses possam substituir superclasses sem quebrar o programa.',
   'Correto: o Principio da Responsabilidade Unica (SRP - *Single Responsibility Principle*) afirma que "uma classe deve ter um, e apenas um, motivo para mudar", recomendando separar cadastro, relatorios e mensageria em classes distintas.',
   'Incorreto: DIP prega depender de abstracoes, nao unificar tudo em uma classe.',
   'Pense em um canivete suico que tem faca, tesoura, lanterna e secador de cabelo: se o secador de cabelo queimar, você tem que mandar o canivete inteiro para o conserto e fica sem a faca para cozinhar.',
   'Robert C. Martin define responsabilidade como um "eixo de mudanca". Classes com multiplas responsabilidades acumulam alto acoplamento e sofrem de fragilidade sob manutencoes corriqueiras.'),

  # Questao 24
  (24, '23. Princípios SOLID de design orientado a objetos.md',
   'SOLID: princípio aberto/fechado (OCP)', 'dificil',
   'Contexto: Uma loja virtual oferece descontos para diferentes perfis de clientes. Hoje, cada nova campanha exige alterar uma longa sequência de condições dentro do método central de cálculo. A equipe deseja incorporar novas políticas de desconto sem precisar modificar continuamente esse método já testado.\n\nComando: Qual decisão de projeto melhor aplica o princípio aberto/fechado?',
   'Modificar obrigatoriamente a classe central a cada novo tipo, sem abstração.',
   'Permitir incluir novas estratégias de desconto por extensão, evitando modificar o código central já estabilizado.',
   'Eliminar interfaces e colocar todas as regras em um único método estático.',
   'Tornar todas as regras privadas e copiar a sequência de condicionais para cada módulo.',
   1,
   'Incorreto: modificar continuamente codigo estavel quebra a premissa de fechamento para modificacao.',
   'Correto: o Principio Aberto/Fechado (OCP - *Open/Closed Principle*) preconiza que entidades de software devem estar abertas para extensao (adicionar novos descontos via polimorfismo ou padrao Strategy), mas fechadas para modificacao (preservando o nucleo testado intacto).',
   'Incorreto: metodos estaticos com condicionais acumuladas sao a causa do problema.',
   'Incorreto: copiar blocos condicionais agrava drasticamente a duplicacao de regras.',
   'Pense na porta USB do seu computador: ela esta fechada para modificacao (ninguem abre o computador com chave de fenda para soldar novos fios), mas esta totalmente aberta para extensao (voce pode conectar teclado, mouse, pendrive ou caixa de som nova).',
   'Bertrand Meyer e Martin destacam que o OCP e alcancado principalmente pelo uso de interfaces ou classes abstratas (como a aplicacao do padrao de projeto Strategy).'),

  # Questao 25
  (25, '24. Padrões de projeto (design patterns) e o catálogo GoF.md',
   'Padrões de projeto e suas categorias (GoF)', 'medio',
   'Contexto: Durante a evolução de um sistema de vendas, os desenvolvedores encontram problemas recorrentes na criação de objetos, na organização de relações entre classes e na comunicação entre componentes. Em vez de propor uma solução inédita a cada ocorrência, buscam alternativas de projeto documentadas e reutilizáveis.\n\nComando: Como devem ser caracterizadas essas soluções recorrentes no desenvolvimento orientado a objetos?',
   'São trechos de código obrigatórios e idênticos em toda linguagem.',
   'São padrões de projeto que descrevem soluções recorrentes, incluindo categorias criacionais, estruturais e comportamentais.',
   'São recursos exclusivos do compilador que substituem princípios de projeto.',
   'São regras que dispensam análise das necessidades do sistema.',
   1,
   'Incorreto: padroes de projeto nao sao receitas de copia e cola de codigo engessado, mas solucoes conceituais adaptadas ao contexto.',
   'Correto: padroes de projeto (*design patterns*, catalogados pelo GoF - Gang of Four) sao solucoes comprovadas e consolidadas para problemas recorrentes de design de software, categorizados em Criacionais (Factory, Singleton), Estruturais (Adapter, Composite) e Comportamentais (Observer, Strategy).',
   'Incorreto: padroes de projeto sao arquiteturais e conceituais, nao instrucoes proprietarias do compilador.',
   'Incorreto: a aplicacao de um padrao exige avaliacao cuidadosa para evitar superengenharia desnecessaria (*overengineering*).',
   'Pense nas jogadas ensaiadas no futebol ou nas aberturas no xadrez: grandes mestres nao inventam movimentos do zero a cada jogo; eles conhecem padroes testados e aprovados ao longo de decadas para resolver situacoes tipicas.',
   'Erich Gamma, Richard Helm, Ralph Johnson e John Vlissides estabeleceram um vocabulario comum indispensavel para a engenharia de software atraves do catalogo dos 23 padroes GoF.')
]

for idx, r in enumerate(raw):
    actual_id = idx + 1
    add_q(actual_id, r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12], r[13], r[14], r[15])

print(f"Geradas {len(puc_questions)} questoes de revisao oficial para Programacao Modular.")

pm_path = '/home/antigravity/leorruas/puc/banco-de-questoes/01.programacao-modular.json'
with open(pm_path, 'r', encoding='utf-8') as f:
    existing_pm = json.load(f)

clean_base = [q for q in existing_pm if not q.get('id', '').startswith('PM-REV-')]
print(f"Questoes base preservadas: {len(clean_base)}")

for q in clean_base:
    if 'prioritaria' not in q:
        q['prioritaria'] = False
    if 'origem' not in q:
        q['origem'] = 'banco_sintetico_vault'

merged = puc_questions + clean_base

with open(pm_path, 'w', encoding='utf-8') as f:
    json.dump(merged, f, ensure_ascii=False, indent=2)

print(f"Sucesso: {len(merged)} questoes salvas em {pm_path}.")
