import json
import os

base_ref = '02. Modelagem de Dados/'
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
        'id': f'MD-REV-{id_num:03d}',
        'disciplina_id': '02',
        'disciplina': 'Modelagem de Dados',
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
  (1, '02. Abordagem de arquivos vs. abordagem de banco de dados.md',
   'Abordagem de arquivos versus abordagem de BD', 'facil',
   'Uma clínica mantém os dados dos pacientes em arquivos independentes, utilizados por sistemas de agendamento e faturamento. Alterações de endereço precisam ser repetidas e frequentemente ficam inconsistentes. Ao propor a modernização, a equipe considera uma base integrada, gerenciada por SGBD. A recepção relata que é difícil saber qual dos arquivos contém o dado mais recente, e os atendentes precisam conferir manualmente as divergências antes de cada atendimento.\n\nQual benefício responde diretamente ao problema identificado?',
   'Eliminação da necessidade de controle de acesso aos dados.',
   'Compartilhamento de dados com redução da redundância e das inconsistências.',
   'Substituição obrigatória de todas as aplicações por uma única aplicação.',
   'Garantia de que todos os dados serão armazenados apenas em arquivos de texto.',
   1,
   'Incorreto: o controle de acesso e seguranca continua fundamental em bancos de dados integrados.',
   'Correto: a abordagem de banco de dados centraliza a informacao em um repositorio compartilhado, eliminando a redundancia descontrolada e prevenindo as inconsistencias tipicas de sistemas de arquivos isolados.',
   'Incorreto: um mesmo banco centralizado pode atender perfeitamente a multiplas aplicacoes distintas e especializadas.',
   'Incorreto: SGBDs utilizam estruturas binarias otimizadas e blocos de armazenamento em disco, nao apenas arquivos de texto.',
   'Pense em uma familia onde cada pessoa tem uma caderneta propria de telefones: se a vovo mudar de numero, alguem vai esquecer de atualizar e ligar para o numero errado. Se a familia usar uma lista compartilhada na nuvem, qualquer alteracao vale para todos na mesma hora.',
   'A transicao do processamento de arquivos para sistemas de gerenciamento de bancos de dados (SGBDs) resolve a redundancia descontrolada, a isolacao de dados e os graves problemas de inconsistencia mutua descritos por Elmasri & Navathe e Silberschatz.'),

  # Questao 02
  (2, '04. Níveis do sgbd e etapas do projeto de banco de dados.md',
   'Níveis externo, conceitual e interno do SGBD e independência física', 'medio',
   'Uma instituição quer alterar a organização física dos registros em disco para melhorar o desempenho, preservando o esquema lógico e as aplicações que consultam os dados. A mudança deve ser transparente para os usuários, pois os relatórios e cadastros existentes não podem precisar de ajustes apenas porque o armazenamento foi reorganizado.\n\nNa arquitetura de três níveis do SGBD, qual propriedade é necessária?',
   'Exposição do nível físico diretamente a todos os usuários.',
   'Alteração obrigatória das visões externas a cada reorganização de disco.',
   'Independência lógica mediante exclusão do esquema conceitual.',
   'Independência física dos dados entre os níveis interno e conceitual.',
   3,
   'Incorreto: expor o nivel fisico aos usuarios quebra o encapsulamento e a arquitetura ANSI/SPARC.',
   'Incorreto: o objetivo da independencia de dados e justamente evitar alteracoes nas visoes externas e aplicacoes.',
   'Incorreto: o esquema conceitual e indispensavel como mediador logico da arquitetura de tres esquemas.',
   'Correto: a independencia fisica dos dados permite alterar o esquema interno (estruturas de arquivos em disco, indices, metodos de acesso) sem precisar modificar o esquema conceitual nem os programas de aplicacao.',
   'E como trocar o motor a combustao de um carro por um motor eletrico silencioso: o motorista continua usando o mesmo volante, pedais e painel (nivel conceitual e externo) para dirigir, mesmo que a mecanica debaixo do capo (nivel interno/fisico) tenha mudado por completo.',
   'A arquitetura ANSI/SPARC de tres niveis (externo, conceitual e interno) isola a representacao logica de negocio da implementacao fisica de baixo nivel em disco.'),

  # Questao 03
  (3, '04. Níveis do sgbd e etapas do projeto de banco de dados.md',
   'Etapas do projeto de banco de dados: conceitual, lógico e físico', 'medio',
   'Uma equipe levantou regras de negócio de uma biblioteca e desenhou um diagrama de entidades e relacionamentos. Antes de definir índices e estruturas de armazenamento, precisa estabelecer tabelas, chaves e relacionamentos adequados a um SGBD relacional. O diagrama inicial já representa as necessidades do negócio, mas ainda não define como as informações serão organizadas no sistema de banco de dados escolhido.\n\nEm qual etapa está a próxima atividade?',
   'Operação e manutenção do banco já implantado.',
   'Levantamento inicial dos requisitos, sem modelagem.',
   'Projeto lógico.',
   'Projeto físico.',
   2,
   'Incorreto: a operacao ocorre apos o deploy do banco finalizado e povoado.',
   'Incorreto: os requisitos e a modelagem conceitual ja foram concluidos pela equipe.',
   'Correto: o projeto logico transforma o modelo conceitual (DER) no modelo de dados correspondente a tecnologia escolhida (como o modelo relacional de tabelas, chaves primarias e estrangeiras).',
   'Incorreto: o projeto fisico define particionamento, caminhos de acesso, indices e armazenamento em disco, etapa que sucede o projeto logico.',
   'Primeiro voce desenha a ideia da casa e dos comodos no papel de pao (projeto conceitual); depois calcula a planta baixa com paredes, espessuras e portas exatas no padrao da engenharia civil (projeto logico); e por ultimo escolhe a marca do tijolo, fios e canos em disco (projeto fisico).',
   'O ciclo classico de projeto de BD divide-se em: Levantamento de Requisitos -> Projeto Conceitual (DER) -> Projeto Logico (esquema relacional) -> Projeto Fisico (DDL, indices, storage).'),

  # Questao 04
  (4, '03. Linguagens de banco de dados (ddl e dml) e perfis profissionais.md',
   'Linguagens de banco de dados: DDL versus DML', 'facil',
   'Uma aplicação acadêmica precisa criar uma tabela de matrículas e, depois, registrar e consultar matrículas realizadas. O desenvolvedor deve distinguir comandos que definem estruturas daqueles que manipulam registros. O projeto será executado em duas etapas: primeiro será preparada a estrutura persistente e, em seguida, os usuários passarão a operar os registros de matrícula.\n\nQual associação está correta?',
   'CREATE TABLE é DDL; INSERT e SELECT são DML.',
   'Todos os comandos citados pertencem à DDL.',
   'CREATE TABLE é DML; INSERT e SELECT são DDL.',
   'DDL é usada apenas para consultar registros e DML apenas para criar tabelas.',
   0,
   'Correto: CREATE TABLE define o esquema estrutural (DDL - Data Definition Language); INSERT e SELECT inserem e consultam os dados das tuplas (DML - Data Manipulation Language).',
   'Incorreto: INSERT e SELECT operam manipulacao de dados, pertencendo a DML.',
   'Incorreto: inverte as categorias das linguagens.',
   'Incorreto: define de modo exatamente oposto a atribuicao de cada subconjunto SQL.',
   'DDL e o marceneiro construindo as gavetas do armario (CREATE, ALTER, DROP); DML e voce guardando, pegando ou conferindo as roupas dentro das gavetas (INSERT, UPDATE, DELETE, SELECT).',
   'A DDL define metadados estruturais no dicionario de dados; a DML atua nas instancias de tuplas das relacoes.'),

  # Questao 05
  (5, '05. Modelagem de entidades e tipos de atributos.md',
   'Modelagem de entidades e tipos de atributos', 'facil',
   'Uma escola deseja registrar alunos e seus respectivos dados, incluindo matrícula, nome e data de nascimento. Durante a modelagem conceitual, é preciso distinguir o objeto de interesse de suas características. O objetivo é construir um diagrama que represente os estudantes e suas propriedades sem confundir os elementos que serão cadastrados com os valores registrados para cada um.\n\nQual representação é adequada?',
   'ALUNO é um valor de atributo e matrícula é necessariamente um relacionamento.',
   'ALUNO é entidade; matrícula, nome e data de nascimento são atributos.',
   'Matrícula é entidade; ALUNO é atributo de nome.',
   'Nome e data de nascimento são relacionamentos entre alunos.',
   1,
   'Incorreto: ALUNO e o conceito/objeto central de negocio, e matricula e identificador de atributo.',
   'Correto: no modelo Entidade-Relacionamento (Peter Chen), ALUNO e a entidade (objeto do mundo real sobre o qual se deseja manter informacoes) e matricula, nome e data de nascimento sao seus atributos descritivos.',
   'Incorreto: inverte o objeto da entidade com um atributo especifico.',
   'Incorreto: caracteristicas individuais de uma pessoa nao sao relacionamentos entre entidades.',
   'Pense no estudante real: ele e a pessoa/entidade concreta; a altura, o nome no RG e o numero de chamada sao as etiquetas coladas nele (seus atributos).',
   'Entidades representam classes de objetos do mundo real com existencia autonoma, caracterizadas por um conjunto de atributos atomicos ou identificadores.'),

  # Questao 06
  (6, '05. Modelagem de entidades e tipos de atributos.md',
   'Atributos simples, compostos, multivalorados e derivados', 'medio',
   'No cadastro de fornecedores, cada fornecedor pode informar vários telefones de contato. A equipe deseja representar essa regra ainda no diagrama conceitual, sem assumir que todos terão a mesma quantidade de números. Alguns fornecedores disponibilizam apenas um número e outros mantêm contatos para atendimento e faturamento, que devem permanecer vinculados ao mesmo cadastro.\n\nQual classificação é mais apropriada para o atributo telefone?',
   'Composto obrigatoriamente, pois qualquer telefone identifica uma entidade fraca.',
   'Derivado, pois telefones são sempre calculados a partir do nome.',
   'Multivalorado, pois uma ocorrência de fornecedor pode ter diversos telefones.',
   'Identificador único, pois cada fornecedor deve ter um único telefone.',
   2,
   'Incorreto: composto e o atributo que se subdivide em partes menores (como endereco em rua, numero e bairro), nao significando multiplas ocorrencias.',
   'Incorreto: derivado e aquele calculado a partir de outros dados (como idade derivada da data de nascimento).',
   'Correto: um atributo multivalorado pode assumir um conjunto de valores para uma mesma instancia da entidade (graficamente representado por elipse dupla no DER classico de Chen).',
   'Incorreto: a regra do negocio explicita que cada fornecedor pode possuir varios telefones.',
   'Pense no campo "hobbies" de uma pessoa: ela pode ter zero, um ou cinco hobbies diferentes (multivalorado). Já o seu CPF e monovalorado (apenas um por pessoa).',
   'Atributos multivalorados violam a 1FN do modelo relacional caso mantidos diretamente na tupla, exigindo conversao posterior em tabela dependente no projeto logico.'),

  # Questao 07
  (6, '06. Modelagem de relacionamentos, cardinalidade e restrições de participação.md',
   'Cardinalidade de relacionamentos (1:1, 1:N, N:N)', 'medio',
   'Em uma plataforma de cursos, cada turma pertence a exatamente um curso, enquanto um curso pode possuir várias turmas. O analista precisa representar a cardinalidade entre CURSO e TURMA no DER. Essa regra deve ser compreendida antes da criação das tabelas, para que a multiplicidade da associação seja representada corretamente no modelo conceitual.\n\nQual alternativa traduz corretamente a regra?',
   'Relacionamento 1:1 porque cada turma tem um único curso.',
   'Ausência de relacionamento, pois os dois elementos são entidades.',
   'Relacionamento N:N porque toda turma pode pertencer a vários cursos.',
   'Relacionamento 1:N de CURSO para TURMA.',
   3,
   'Incorreto: 1:1 impediria que um curso tivesse mais de uma turma ao longo do ano.',
   'Incorreto: entidades de dominio compartilham associacoes no modelo conceitual.',
   'Incorreto: N:N violaria a premissa de que cada turma pertence a exatamente um curso.',
   'Correto: um curso pode conter multiplas turmas (lado N), mas cada turma especifica vincula-se a apenas um curso (lado 1), configurando cardinalidade 1:N de CURSO para TURMA.',
   'Pense em uma arvore genealógica: uma mae pode ter varios filhos (1:N), mas cada filho tem apenas uma mae biologica.',
   'A cardinalidade de mapeamento 1:N expressa a razao de multiplicidade maxima permitida entre ocorrencias de duas entidades participantes.'),

  # Questao 08
  (8, '06. Modelagem de relacionamentos, cardinalidade e restrições de participação.md',
   'Restrições de participação (totalidade vs. parcialidade)', 'medio',
   'Uma empresa determina que todo pedido deve pertencer a um cliente cadastrado, mas um cliente pode existir sem realizar pedidos. No levantamento de requisitos, ficou claro que a empresa precisa impedir pedidos sem responsável, embora deseje manter cadastros de clientes que ainda não compraram.\n\nAo modelar essa regra, como deve ser representada a participação?',
   'Total para PEDIDO e parcial para CLIENTE.',
   'Parcial para ambas as entidades.',
   'Total para ambas as entidades.',
   'Parcial para PEDIDO e total para CLIENTE.',
   0,
   'Correto: todo pedido exige obrigatoriamente um cliente associado (participacao total / linha dupla no DER); ja o cliente pode existir no banco sem pedidos registrados (participacao parcial / linha simples).',
   'Incorreto: se PEDIDO fosse parcial, o sistema permitiria pedidos orfaos sem cliente responsavel.',
   'Incorreto: se CLIENTE fosse total, nao seria possivel cadastrar um novo cliente antes dele realizar sua primeira compra.',
   'Incorreto: inverte a totalidade e a parcialidade entre as duas entidades.',
   'Pense no cartao de credito e na compra: uma compra nao pode existir sem um titular do cartao (participacao total da compra). Mas uma pessoa pode ter o cartao na carteira e nao fazer compras durante meses (participacao parcial do cliente).',
   'A participacao total (dependencia de existencia) impoe cardinalidade minima igual a 1; a participacao parcial estabelece cardinalidade minima igual a 0.'),

  # Questao 09
  (9, '07. Modelo de entidades e relacionamentos estendido.md',
   'Especialização: subtipos sobrepostos (overlap) vs. disjuntos (disjoint)', 'medio',
   'Em um sistema hospitalar, a entidade PESSOA reúne dados comuns. Uma mesma pessoa pode ser simultaneamente MÉDICO e PACIENTE. A equipe pretende utilizar especialização para representar esses papéis. Os dois papéis compartilham informações cadastrais, mas possuem propriedades específicas e não são mutuamente exclusivos na realidade da instituição.\n\nQue restrição corresponde à regra descrita?',
   'Eliminação da superclasse, pois atributos comuns não podem ser compartilhados.',
   'Subtipos sobrepostos, pois uma instância pode pertencer a ambos.',
   'Especialização necessariamente total com papéis mutuamente exclusivos.',
   'Subtipos disjuntos, pois uma pessoa nunca pode assumir dois papéis.',
   1,
   'Incorreto: a superclasse e o elemento que justamente viabiliza o reuso de dados comuns.',
   'Correto: na restricao de sobreposicao (overlapping, representada pela letra "o" no circulo de especializacao), uma mesma entidade da superclasse pode ser membro simultaneo de mais de uma subclasse.',
   'Incorreto: exclusividade mutua impediria que um medico do hospital tambem consultasse como paciente.',
   'Incorreto: subtipos disjuntos (disjoint, representado por "d") forcam a exclusividade estrita entre os papeis.',
   'E como uma pessoa em uma universidade que faz faculdade a noite e trabalha na secretaria de dia: ela e simultaneamente Aluno e Funcionario da mesma instituicao (sobreposicao de papeis).',
   'No modelo EER, a restricao de disjuncao determina se os subtipos sao mutuamente exclusivos (disjoint) ou se admitem ocorrencia simultanea (overlap).'),

  # Questao 10
  (10, '07. Modelo de entidades e relacionamentos estendido.md',
   'Entidades fracas, dependência de existência e chave parcial', 'dificil',
   'Um condomínio registra APARTAMENTO identificado pelo par (bloco, número) dentro de cada CONDOMÍNIO. O número do apartamento pode se repetir em condomínios diferentes e sua existência no cadastro depende do condomínio. Os analistas observam que um apartamento não pode ser cadastrado isoladamente: é necessário saber a qual condomínio pertence para identificá-lo sem ambiguidades.\n\nQual solução conceitual melhor expressa essa identificação dependente?',
   'Declarar número do apartamento como identificador global, sem referência ao condomínio.',
   'Tratar APARTAMENTO como entidade fraca, identificada com apoio da entidade proprietária e de uma chave parcial.',
   'Substituir APARTAMENTO por um atributo booleano de CONDOMÍNIO.',
   'Estabelecer relacionamento sem identificação, pois entidades fracas não possuem instâncias.',
   1,
   'Incorreto: o numero da sala ou apartamento se repete em outros edificios, gerando colisoes se usado sozinho.',
   'Correto: APARTAMENTO e uma entidade fraca porque nao possui atributos proprios suficientes para formar uma chave primaria global; depende do relacionamento de identificacao com a entidade proprietaria (CONDOMINIO) somado a sua chave parcial discriminadora (bloco, numero).',
   'Incorreto: um atributo booleano nao armazena as multiplas instancias de apartamentos.',
   'Incorreto: entidades fracas possuem ocorrencias e dados normais no banco de dados.',
   'Pense nos quartos de hotel: quase todo hotel tem o "quarto 101". O quarto 101 so faz sentido se você disser de qual hotel ele e (entidade proprietaria + chave parcial discriminadora).',
   'No DER de Chen, a entidade fraca e representada por retangulo duplo, seu relacionamento identificador por losango duplo, e a chave parcial sublinhada com linha tracejada.'),

  # Questao 11
  (11, '08. Conceitos do modelo relacional e chave primária.md',
   'Superchaves, chaves candidatas e chave primária', 'medio',
   'Em uma tabela de funcionários, CPF e matrícula institucional são individualmente únicos e não nulos. A equipe escolhe matrícula como identificador principal. Na revisão do esquema, a equipe precisa distinguir os atributos capazes de identificar registros daqueles efetivamente escolhidos para desempenhar a identificação principal.\n\nQual afirmação sobre as chaves está correta?',
   'Apenas matrícula pode ser chave candidata, porque foi escolhida como primária.',
   'Nenhuma coluna pode ser chave candidata quando há duas opções de identificação.',
   'CPF se torna chave estrangeira automaticamente.',
   'CPF e matrícula são chaves candidatas; matrícula é a chave primária selecionada.',
   3,
   'Incorreto: tanto matricula quanto CPF atendem aos criterios de unicidade e minimalidade, sendo ambas candidatas.',
   'Incorreto: e comum uma relacao possuir multiplas chaves candidatas concorrentes.',
   'Incorreto: CPF e atributo unico alternativo (chave alternativa / UNIQUE), nao chave estrangeira referenciando outra tabela.',
   'Correto: qualquer superchave minima e uma chave candidata. Quando ha mais de uma candidata (CPF e matricula), o projetista escolhe uma para ser a Chave Primaria (PK) e as demais tornam-se chaves alternativas.',
   'Pense em uma pessoa que tem Passaporte e RG: os dois documentos identificam a pessoa de forma unica (ambos sao chaves candidatas). No aeroporto internacional, a policia escolhe usar o Passaporte como identificador oficial (chave primaria).',
   'O modelo relacional formal de Codd estabelece que o conjunto de chaves candidatas e derivado da analise de dependencias funcionais; uma delas e promovida a Primary Key e as outras implementadas com restricoes UNIQUE NOT NULL.'),

  # Questao 12
  (12, '09. Integridade referencial e chave estrangeira.md',
   'Integridade referencial e chave estrangeira', 'medio',
   'Uma tabela PEDIDO contém cliente_id como chave estrangeira referenciando CLIENTE(id). Um usuário tenta cadastrar um pedido com cliente_id=900, que não existe na tabela CLIENTE. O cadastro é realizado por um serviço automatizado, e a equipe deseja impedir que pedidos apontem para clientes inexistentes, preservando a consistência entre tabelas.\n\nConsiderando a integridade referencial habilitada, qual é o comportamento esperado?',
   'A inserção deve ser rejeitada até existir uma chave correspondente em CLIENTE.',
   'O SGBD deve converter cliente_id em chave primária de PEDIDO.',
   'O pedido deve ser gravado e a chave estrangeira removida automaticamente.',
   'O pedido deve ser gravado sem verificação, porque chaves estrangeiras restringem apenas consultas.',
   0,
   'Correto: a restricao de integridade referencial exige que qualquer valor nao nulo de chave estrangeira corresponda a um valor de chave primaria existente na relacao referenciada, rejeitando insercoes invalidas.',
   'Incorreto: cliente_id e FK e nao se converte em PK por erro de insercao.',
   'Incorreto: o SGBD nao altera a estrutura de constraints em tempo de execucao.',
   'Incorreto: chaves estrangeiras atuam principalmente na validacao estrita de gravacoes DML (INSERT, UPDATE, DELETE).',
   'E como tentar enviar uma carta para uma casa que nao existe na rua: os correios recusam a postagem na hora porque o destinatario nao existe no cadastro oficial.',
   'A regra de integridade referencial mantem a consistencia do grafo de dados, impedindo tuplas orfas na base relacional.'),

  # Questao 13
  (13, '10. Mapeamento de entidades e atributos.md',
   'Mapeamento de atributos multivalorados para o modelo relacional', 'medio',
   'No DER de uma clínica, PACIENTE possui um atributo multivalorado telefone. Ao transformar o modelo conceitual em tabelas, a equipe precisa permitir diversos telefones por paciente sem repetir colunas telefone1, telefone2 etc. Os profissionais também precisam consultar e atualizar cada telefone separadamente, mesmo quando um paciente possui diversos contatos.\n\nQual estrutura é mais adequada?',
   'Eliminar os telefones adicionais e manter apenas o primeiro.',
   'Guardar todos os telefones em uma coluna única com valores separados por vírgulas.',
   'Criar um número fixo de colunas para telefones na tabela PACIENTE.',
   'Criar uma relação própria para telefones com chave estrangeira de PACIENTE.',
   3,
   'Incorreto: perda arbitraria de dados cadastrais do negocio.',
   'Incorreto: armazenar listas separadas por virgula viola a primeira forma normal (1FN) e dificulta consultas.',
   'Incorreto: fixar colunas (tel1, tel2) limita artificialmente o cadastro e gera colunas nulas desperdicadas.',
   'Correto: no algoritmo canonico de mapeamento E-R para relacional, cada atributo multivalorado da origem a uma nova tabela contendo o valor do atributo e a chave estrangeira referenciando a tabela principal.',
   'Em vez de tentar espremer tres telefones na mesma linha da ficha, voce cria uma caderneta anexa de contatos onde cada telefone ocupa sua propria linha, ligada pelo codigo do paciente.',
   'A relacao resultante `Paciente_Telefone(paciente_id, telefone)` tem como chave primaria a combinacao `(paciente_id, telefone)`, garantindo atomicidade e flexibilidade total de ocorrencias.'),

  # Questao 14
  (14, '10. Mapeamento de entidades e atributos.md',
   'Mapeamento de entidades fracas e chaves compostas', 'dificil',
   'Uma empresa mantém DEPARTAMENTO(id_departamento) e SALA(numero_sala), sendo que o número da sala só é único dentro de seu departamento. O número 101, por exemplo, pode aparecer em departamentos diferentes. Por isso, o identificador utilizado no banco não pode depender apenas do número isolado.\n\nNa passagem do DER para o esquema relacional, qual chave identifica adequadamente cada sala?',
   'Somente numero_sala, mesmo que se repita entre departamentos.',
   'Chave composta (id_departamento, numero_sala), com referência a DEPARTAMENTO.',
   'Nenhuma chave, pois entidades dependentes não precisam de identificação.',
   'Somente id_departamento, pois cada departamento possui uma única sala.',
   1,
   'Incorreto: o numero isolado causaria violacao de unicidade ao duplicar a sala 101 em departamentos distintos.',
   'Correto: a chave primaria de uma entidade fraca mapeada no modelo relacional e formada pela chave primaria da entidade proprietaria (`id_departamento`) combinada com a chave parcial da entidade fraca (`numero_sala`).',
   'Incorreto: no modelo relacional toda relacao deve possuir uma chave primaria valida.',
   'Incorreto: usar apenas o departamento impediria que o departamento tivesse multiplas salas.',
   'A sala 101 do predio da Engenharia e diferente da sala 101 do predio de Medicina. Para nao ter duplicidade, o cracha da porta deve ser "Engenharia - Sala 101" (chave composta).',
   'A chave estrangeira da entidade proprietaria migra para a relacao fraca compondo a sua chave primaria relacional: `PK (id_departamento, numero_sala)`.'),

  # Questao 15
  (15, '11. Mapeamento de relacionamentos.md',
   'Mapeamento de relacionamento 1:N (regra da chave estrangeira no lado N)', 'medio',
   'Em um sistema de vendas, um vendedor pode atender vários clientes, mas cada cliente possui um vendedor responsável. Ao converter esse relacionamento 1:N para tabelas, a equipe procura uma solução sem tabela associativa desnecessária. O responsável pelo projeto busca preservar o vínculo entre os cadastros, evitando criar estruturas adicionais quando a própria cardinalidade permite uma solução mais simples.\n\nQual alternativa é apropriada?',
   'Incluir em VENDEDOR uma lista de todos os IDs de clientes em uma coluna.',
   'Incluir em CLIENTE uma FK que referencia VENDEDOR.',
   'Criar sempre uma FK única em VENDEDOR apontando para CLIENTE.',
   'Eliminar a referência, pois cardinalidade não é representada no modelo relacional.',
   1,
   'Incorreto: criar listas multivaloradas viola a 1FN.',
   'Correto: no mapeamento canonico de relacionamentos 1:N, a chave primaria da tabela do lado 1 (`VENDEDOR`) e adicionada como chave estrangeira na tabela do lado N (`CLIENTE`), preservando a relacao de forma simples e direta.',
   'Incorreto: colocar a chave em VENDEDOR limitaria o vendedor a atender um unico cliente.',
   'Incorreto: a cardinalidade e rigorosamente preservada no modelo relacional por chaves estrangeiras e restricoes.',
   'Cada cliente anda com o cartao do vendedor que o atende no bolso (FK em cliente). O vendedor nao tem como tatuar no braco o nome de 500 clientes.',
   'A inclusao da foreign key no lado "muitos" evita tabelas intermediarias desnecessarias e preserva a regra de que cada cliente so aponta para um vendedor.'),

  # Questao 16
  (16, '11. Mapeamento de relacionamentos.md',
   'Mapeamento de relacionamentos N:N e tabelas associativas', 'medio',
   'Em uma universidade, um ALUNO pode cursar várias DISCIPLINAS e cada DISCIPLINA recebe vários ALUNOS. O relacionamento MATRÍCULA possui o atributo semestre. A instituição precisa registrar cada matrícula realizada e identificar também o período em que o vínculo ocorreu, sem perder a possibilidade de um aluno cursar várias disciplinas.\n\nQual proposta de mapeamento representa os vínculos e esse atributo?',
   'Adicionar somente disciplina_id na tabela ALUNO, permitindo um curso por aluno.',
   'Guardar todas as disciplinas em texto na coluna disciplina da tabela ALUNO.',
   'Criar uma tabela MATRÍCULA com FKs para ALUNO e DISCIPLINA e o atributo semestre.',
   'Adicionar somente aluno_id na tabela DISCIPLINA, permitindo um aluno por disciplina.',
   2,
   'Incorreto: limitaria o aluno a se matricular em uma unica disciplina.',
   'Incorreto: armazenar dados multivalorados em formato texto viola a 1FN.',
   'Correto: relacionamentos N:N geram obrigatoriamente uma nova relacao associativa (`MATRICULA`) contendo as chaves estrangeiras das entidades participantes mais os atributos proprios do relacionamento (`semestre`).',
   'Incorreto: limitaria a disciplina a possuir um unico aluno.',
   'Pense na lista de presenca da chamada: voce nao altera o diploma do aluno nem o programa da materia; voce cria um livro de chamada onde o nome do aluno se cruza com a materia e a data da aula.',
   'A chave primaria de `Matricula` pode ser composta `(aluno_id, disciplina_id, semestre)` ou uma chave artificial sub-rogada com as duas FKs associadas.'),

  # Questao 17
  (17, '11. Mapeamento de relacionamentos.md',
   'Mapeamento de herança e generalização/especialização', 'dificil',
   'Uma instituição modelou PESSOA como supertipo, com PROFESSOR e ALUNO como subtipos, cada qual com atributos próprios. Deseja manter uma tabela comum e tabelas específicas. No banco, os dados compartilhados devem permanecer associados a uma única pessoa, enquanto as informações dos papéis precisam ficar organizadas de acordo com o subtipo.\n\nQual alternativa é coerente com esse mapeamento?',
   'Armazenar cada subtipo apenas como um texto livre em um atributo de PESSOA.',
   'Duplicar obrigatoriamente todos os atributos comuns em ambas as tabelas e eliminar qualquer possibilidade de identificação compartilhada.',
   'Criar PESSOA com atributos comuns e tabelas PROFESSOR e ALUNO cujas chaves referenciem PESSOA.',
   'Unir todos os atributos dos subtipos em uma tabela sem chave primária.',
   2,
   'Incorreto: reduz subtipos a campos de texto solto, perdendo a estrutura tipada.',
   'Incorreto: duplicar todos os atributos comuns viola principios relacionais e gera anomalias de atualizacao.',
   'Correto: essa abordagem (estrategia table-per-type) cria uma relacao para a superclasse (`PESSOA`) com chave primaria e relacoes para as subclasses (`PROFESSOR` e `ALUNO`) cuja chave primaria e tambem chave estrangeira referenciando `PESSOA`.',
   'Incorreto: tabelas relacionais exigem chave primaria.',
   'Pense em um cadastro central de funcionarios de uma grande corporacao: todos tem nome, CPF e endereco na ficha mestre (tabela PESSOA). Se o funcionario for piloto, ha uma ficha adicional com horas de voo; se for engenheiro, uma com registro no CREA, ambas ligadas pelo mesmo CPF.',
   'No mapeamento de heranca com tabelas multiplas conectadas por FK (Mapeamento Opcao 8C de Elmasri), garante-se a integridade e evita-se colunas nulas nas tabelas especializadas.'),

  # Questao 18
  (18, '12. 1ª, 2ª e 3ª formas normais.md',
   'Primeira forma normal (1FN) e atomicidade de atributos', 'facil',
   'Uma tabela de clientes registra telefones como o valor textual “31999990000;3133330000” em uma única célula. A equipe pretende adequar a estrutura à primeira forma normal, mantendo todos os números disponíveis. Além de dificultar as buscas, a representação atual reúne múltiplos valores em um mesmo campo e impede tratar cada número como uma ocorrência individual.\n\nQual alteração atende melhor ao objetivo?',
   'Manter vários números na mesma célula e apenas trocar ponto e vírgula por barra.',
   'Representar cada telefone como valor atômico em registros adequados, vinculados ao cliente.',
   'Eliminar um dos números, independentemente da necessidade do negócio.',
   'Criar uma coluna que armazene um arquivo com a lista de números.',
   1,
   'Incorreto: trocar o caractere delimitador nao altera o fato de o campo conter dados compostos/multivalorados.',
   'Correto: a 1FN exige que todos os atributos contenham apenas valores atomicos (indivisiveis) e que nao existam grupos repetitivos em uma mesma celula.',
   'Incorreto: descartar dados de contato validos viola os requisitos funcionais do negocio.',
   'Incorreto: arquivos de texto mantem o dado opaco e intestavel por SQL relacional.',
   'Atomicidade vem do grego "indivisivel": uma celula de tabela deve conter um unico valor simples, como uma unica moeda em cada divisoria do caixa, e nao um monte de moedas misturadas que ninguem consegue contar sem separar.',
   'A 1FN proibe atributos multivalorados e atributos compostos no modelo logico relacional, assegurando que o domínio de cada coluna seja estritamente escalar.'),

  # Questao 19
  (19, '12. 1ª, 2ª e 3ª formas normais.md',
   'Segunda forma normal (2FN) e eliminação de dependência funcional parcial', 'medio',
   'Uma tabela ITEM_PEDIDO tem chave composta (pedido_id, produto_id) e atributos quantidade e nome_produto. Sabe-se que nome_produto depende apenas de produto_id, enquanto quantidade depende da combinação completa. Os analistas perceberam que a descrição de um produto se repete em vários pedidos. Alterar seu nome exige atualizar diversos registros de itens, aumentando o risco de divergências.\n\nQual mudança contribui para alcançar a segunda forma normal?',
   'Retirar pedido_id da chave de ITEM_PEDIDO sem analisar a identificação.',
   'Duplicar nome_produto em novas colunas da tabela ITEM_PEDIDO.',
   'Mover nome_produto para a relação PRODUTO, mantendo em ITEM_PEDIDO os dados dependentes da chave completa.',
   'Manter nome_produto porque qualquer atributo depende automaticamente de toda chave composta.',
   2,
   'Incorreto: desestruturaria a chave primaria identificadora dos itens do pedido.',
   'Incorreto: pioraria a redundancia e o desperdicio de espaco.',
   'Correto: a 2FN exige que a tabela esteja na 1FN e que nenhum atributo nao-chave dependa parcialmente de uma chave primaria composta. Como `nome_produto` depende exclusivamente de `produto_id` (parte da chave), deve ser isolado na relacao `PRODUTO`.',
   'Incorreto: nem todo atributo depende de toda a chave; essa dependencia parcial e a causa da violacao da 2FN.',
   'Se você comprar um pacote de canetas e um caderno na mesma compra, o preco do pacote de canetas depende da compra. Mas o fabricante da caneta BIC e sempre o mesmo, nao importa em qual compra ela apareca. O dado do fabricante pertence a caneta, nao a compra.',
   'A remocao de dependencias funcionais parciais atraves da decomposicao em relacoes menores elimina anomalias de alteracao e redundancia de metadados de catalogo.'),

  # Questao 20
  (20, '12. 1ª, 2ª e 3ª formas normais.md',
   'Terceira forma normal (3FN) e eliminação de dependência funcional transitiva', 'dificil',
   'Uma tabela FUNCIONÁRIO contém matricula (PK), setor_id e nome_setor. Cada setor_id determina nome_setor. Assim, matricula determina setor_id, que determina nome_setor. A equipe busca reduzir anomalias de atualização. Quando um setor muda de nome, o mesmo texto precisa ser alterado em todas as linhas dos funcionários vinculados a ele, o que pode produzir inconsistências.\n\nQual medida é compatível com a terceira forma normal?',
   'Manter nome_setor repetido para cada funcionário, pois a PK é simples.',
   'Transformar nome_setor em outra chave primária da mesma tabela.',
   'Remover setor_id e usar apenas nome_setor como uma lista de valores.',
   'Criar SETOR(setor_id, nome_setor) e manter setor_id como FK em FUNCIONÁRIO.',
   3,
   'Incorreto: manter a repeticao perpetua anomalias de atualizacao e inconsistencias graves.',
   'Incorreto: nome_setor nao identifica unicamente os funcionarios.',
   'Incorreto: armazenar nomes como listas viola a 1FN.',
   'Correto: a 3FN exige que a tabela esteja na 2FN e que nenhum atributo nao-chave dependa transitivamente da chave primaria atraves de outro atributo nao-chave (`matricula -> setor_id -> nome_setor`). A decomposicao cria `SETOR(setor_id, nome_setor)` e mantem `setor_id` como FK em `FUNCIONARIO`.',
   'Pense no endereco: o seu CPF diz o seu CEP, e o seu CEP diz a sua cidade. Se a cidade mudar de nome, o banco nao precisa alterar o cadastro de milhoes de moradores; altera apenas no cadastro de CEPs uma unica vez.',
   'A definicao formal de Kent resume: "Todo atributo deve depender da chave (1FN), de toda a chave (2FN) e de nada alem da chave (3FN), com a ajuda de Codd."'),

  # Questao 21
  (21, '13. Bancos de dados não-relacionais.md',
   'Modelos pré-relacionais e não-relacionais: modelo hierárquico', 'medio',
   'Uma equipe compara modelos de banco de dados para uma aplicação legada cuja estrutura organiza registros estritamente como uma árvore, com relações de pai e filho. O grupo precisa identificar a classificação dessa abordagem antes de discutir a migração para outra tecnologia de armazenamento de dados.\n\nQual modelo corresponde mais diretamente a essa organização?',
   'Modelo orientado a objetos cujo requisito principal é não possuir classes.',
   'Modelo hierárquico.',
   'Modelo de rede com obrigatoriedade de árvore única.',
   'Modelo relacional representado necessariamente por tabelas sem dependências.',
   1,
   'Incorreto: o modelo orientado a objetos fundamenta-se estritamente em classes, heranca e encapsulamento.',
   'Correto: o modelo hierarquico (pioneiro no IBM IMS nos anos 1960) organiza as relacoes estritamente em arvore hierarquica invertida, onde cada no filho possui exclusivamente um unico no pai.',
   'Incorreto: o modelo em rede (CODASYL) permite grafos gerais onde um no filho pode ter multiplos pais.',
   'Incorreto: o modelo relacional organiza dados em tabelas matematicas bidimensionais planas (relacoes), nao arvores.',
   'Pense nas pastas do Windows Explorer: um arquivo esta dentro de uma subpasta, que esta dentro de uma pasta maior (arvore estrita pai-filho). Isso e a essencia do modelo hierarquico.',
   'O modelo hierarquico sofre de rigidez estrutural diante de associacoes N:N e exige caminhos fixos de navegacao por ponteiros, superado historicamente pelo modelo relacional.'),

  # Questao 22
  (22, '13. Bancos de dados não-relacionais.md',
   'Bancos de dados NoSQL, esquema flexível e escalabilidade horizontal', 'medio',
   'Uma plataforma recebe grande volume de documentos com estruturas variáveis e necessita distribuí-los entre vários servidores. Ao avaliar alternativas ao armazenamento relacional tradicional, a equipe considera soluções NoSQL. Nem todos os documentos possuem os mesmos campos, e a equipe pretende aumentar a capacidade de processamento adicionando máquinas à infraestrutura.\n\nQual característica é compatível com essa decisão?',
   'Eliminação automática de qualquer requisito de consistência e segurança.',
   'Uso de modelos não relacionais, como documentos, com possibilidades de distribuição e escalabilidade.',
   'Proibição de replicação entre servidores.',
   'Obrigatoriedade de armazenar todo conteúdo em tabelas com esquema fixo e SQL padronizado.',
   1,
   'Incorreto: bancos NoSQL modernos mantem modelos de consistencia (como eventual consistency no teorema CAP) e controle de autenticacao.',
   'Correto: bancos NoSQL orientados a documentos (como MongoDB) oferecem esquema flexivel (schemaless / dynamic schema) em formato JSON/BSON e suporte nativo a escalabilidade horizontal (*scale-out*) via sharding e replicacao distribuida.',
   'Incorreto: a replicacao entre nos e o pilar central da alta disponibilidade em sistemas NoSQL.',
   'Incorreto: esquemas fixos e tabelas rigidas sao a definicao dos bancos relacionais tradicionais.',
   'Pense em uma pasta de documentos fiscais onde cada recibo pode ter campos diferentes (um recibo tem desconto, outro tem imposto retido, outro nao). Em vez de enfiar todos na mesma planilha rigida, voce guarda cada um como um documento flexivel.',
   'A categoria NoSQL (*Not Only SQL*) consolidou-se para suprir demandas de Big Data, variabilidade de esquemas e distribuicao massiva em clusters de computadores comuns.'),

  # Questao 23
  (23, '14. Segurança de banco de dados.md',
   'Tríade CIA: Confidencialidade, Integridade e Disponibilidade', 'medio',
   'Uma empresa detecta que usuários sem autorização consultam registros financeiros. Os dados permanecem corretos e o sistema continua disponível. O incidente ocorreu apesar de não terem sido detectadas alterações indevidas nos valores armazenados nem indisponibilidade dos serviços.\n\nQual propriedade de segurança foi diretamente comprometida?',
   'Normalização do esquema relacional.',
   'Integridade dos valores armazenados.',
   'Confidencialidade.',
   'Disponibilidade.',
   2,
   'Incorreto: normalizacao e tecnica de eliminacao de redundancias lógicas, nao principio da triade de seguranca.',
   'Incorreto: a integridade permaneceu preservada, visto que nenhum registro financeiro foi adulterado.',
   'Correto: a confidencialidade garante que a informacao seja acessivel apenas por entidades devidamente autorizadas. O acesso indevido por usuarios nao autorizados constitui violacao direta de confidencialidade (vazamento de dados).',
   'Incorreto: o sistema permaneceu acessivel e em operacao normal, sem violacao de disponibilidade.',
   'Pense em um diario trancado com chave: se alguem abrir e ler os seus segredos sem mudar nenhuma palavra e devolver o diario no mesmo lugar, sua privacidade (confidencialidade) foi quebrada, mesmo que as paginas continuem intactas (integridade) e o diario continue na sua gaveta (disponibilidade).',
   'A triade fundamental de seguranca da informacao (CIA - *Confidentiality, Integrity, Availability*) norteia as politicas de protecao e controle de acesso a bancos de dados.'),

  # Questao 24
  (24, '14. Segurança de banco de dados.md',
   'Segurança em camadas e defesa em profundidade', 'medio',
   'Um sistema possui perfis de acesso configurados no SGBD, porém a aplicação expõe credenciais em arquivos públicos do servidor. A equipe afirma que os dados estão seguros porque o banco exige autenticação. Na análise de risco, os profissionais verificam que terceiros poderiam obter os dados de autenticação e utilizá-los para se conectar ao banco com permissões legítimas.\n\nQual avaliação é mais adequada?',
   'A divulgação de credenciais não apresenta risco se o esquema estiver na 3FN.',
   'A proteção do SGBD torna irrelevante a segurança da aplicação.',
   'A disponibilidade dos dados substitui a necessidade de confidencialidade.',
   'A segurança deve abranger banco, aplicação, sistema operacional e políticas organizacionais.',
   3,
   'Incorreto: formas normais organizam dados relacionais, nao impedindo o roubo de senhas expostas publicamente.',
   'Incorreto: a aplicacao e a porta de entrada para o banco; se ela vazar credenciais, as defesas do banco serao burladas.',
   'Incorreto: disponibilidade e confidencialidade sao pilares complementares e igualmente indispensaveis.',
   'Correto: o principio de seguranca em profundidade (*defense-in-depth*) preconiza que a protecao deve ocorrer em multiplas camadas integradas: seguranca fisica, sistema operacional, rede, codigo da aplicacao, gestao de credenciais e controle interno no SGBD.',
   'E como instalar uma porta de cofre blindada de banco com senha eletronica, mas anotar a senha em um post-it amarelo e colar do lado de fora na parede da calcada: o cofre e forte, mas o sistema como um todo ficou vulneravel.',
   'A seguranca de bancos de dados depende da robustez da cadeia inteira de desenvolvimento de software (*secure by design*), impedindo vazamento de conexoes, SQL Injection e exposicao de segredos em repositorios.')
]

for idx, r in enumerate(raw):
    actual_id = idx + 1
    add_q(actual_id, r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12], r[13], r[14], r[15])

print(f"Geradas {len(puc_questions)} questoes de revisao oficial para Modelagem de Dados.")

md_path = '/home/antigravity/leorruas/puc/banco-de-questoes/02.modelagem-de-dados.json'
with open(md_path, 'r', encoding='utf-8') as f:
    existing_md = json.load(f)

clean_base = [q for q in existing_md if not q.get('id', '').startswith('MD-REV-')]
print(f"Questoes base preservadas: {len(clean_base)}")

for q in clean_base:
    if 'prioritaria' not in q:
        q['prioritaria'] = False
    if 'origem' not in q:
        q['origem'] = 'banco_sintetico_vault'

merged = puc_questions + clean_base

with open(md_path, 'w', encoding='utf-8') as f:
    json.dump(merged, f, ensure_ascii=False, indent=2)

print(f"Sucesso: {len(merged)} questoes salvas em {md_path}.")
