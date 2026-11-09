import json
import os

base_ref = '07. Engenharia de Requisitos/'
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
        'id': f'REQ-REV-{id_num:03d}',
        'disciplina_id': '07',
        'disciplina': 'Engenharia de Requisitos',
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
  (1, '03. O conceito de requisito de software - definição, níveis e características.md',
   'Conceito de requisito e engenharia de requisitos', 'facil',
   'Ao iniciar um sistema de agendamento, a equipe registra a necessidade de permitir que pacientes marquem consultas. Qual interpretação corresponde ao conceito de requisito apresentado na engenharia de requisitos?',
   'É uma característica que o produto deve possuir para ser aceito.',
   'É somente um teste executado após a entrega do software.',
   'É uma decisão de programação que não precisa ser discutida com usuários.',
   'É exclusivamente o código necessário para implementar uma tela.',
   0,
   'Correto: um requisito expressa uma condição, capacidade ou propriedade que um sistema deve possuir para resolver um problema do usuário ou satisfazer a um contrato.',
   'Incorreto: confunde requisito com caso de teste de aceitação final.',
   'Incorreto: requisitos derivam primordialmente das necessidades dos stakeholders de negócio, e não de decisões isoladas de código.',
   'Incorreto: confunde a especificação do problema com o código de implementação da interface gráfica.',
   'Pense no requisito como a planta e memorial descritivo de um imóvel: ele define o que o edifício precisa oferecer (número de quartos, acessibilidade) para ser entregue e aceito pelo morador.',
   'Na engenharia de software (IEEE 610.12 e Sommerville), requisito é a declaração de um serviço que o sistema deve fornecer ou de uma restrição sob a qual deve operar.'),

  # Questao 02
  (2, '05. Como escrever requisitos de qualidade - critérios, padrões e boas práticas.md',
   'Critérios de qualidade de requisitos (completude)', 'medio',
   'Uma especificação afirma apenas: "o sistema deve calcular descontos", sem detalhar regras, faixas percentuais ou condições aplicáveis. Qual critério de qualidade foi violado prioritariamente?',
   'Rastreabilidade, porque a origem do cálculo não foi anotada.',
   'Prioridade, porque todos os descontos deveriam ser urgentes.',
   'Completude, porque a necessidade não foi descrita integralmente.',
   'Tecnologia, porque a linguagem de programação precisa constar no texto.',
   2,
   'Incorreto: a rastreabilidade vincula o requisito a fontes ou artefatos derivados, não sendo a causa da omissão das regras.',
   'Incorreto: prioridade é atributo de planejamento e alocação de esforço, não da integridade do conteúdo textual.',
   'Correto: o critério de completude exige que o requisito contenha todas as informações necessárias para seu entendimento e implementação inequívoca, sem lacunas de regras essenciais.',
   'Incorreto: requisitos funcionais de software devem ser agnósticos à linguagem de programação.',
   'Se uma receita de bolo diz apenas "adicione açúcar" sem dizer a quantidade nem quando colocar, a receita está incompleta, gerando bolos completamente diferentes dependendo de quem cozinhar.',
   'A completude (*completeness*) garante que todas as entradas, saídas, variações, exceções e regras de negócio pertinentes estejam documentadas na especificação.'),

  # Questao 03
  (3, '05. Como escrever requisitos de qualidade - critérios, padrões e boas práticas.md',
   'Critérios de qualidade de requisitos (rastreabilidade)', 'medio',
   'Em uma auditoria, os analistas precisam demonstrar de qual solicitação de usuário surgiu determinada funcionalidade e quais testes verificam seu funcionamento. Qual característica de qualidade atende diretamente a essa necessidade?',
   'Exequibilidade.',
   'Ambiguidade.',
   'Concisão.',
   'Rastreabilidade.',
   3,
   'Incorreto: exequibilidade diz respeito à viabilidade técnica e financeira da construção.',
   'Incorreto: ambiguidade é um defeito semântico de múltiplos sentidos, não uma qualidade desejada.',
   'Incorreto: concisão é a brevidade do texto, sem relação com vínculos entre artefatos de ciclo de vida.',
   'Correto: a rastreabilidade (*traceability*) permite seguir o ciclo de vida de um requisito em ambas as direções (para trás até a necessidade de origem e para a frente até código e testes).',
   'É como o código de rastreio de uma encomenda internacional: você consegue ver de onde ela partiu, em quais galpões foi triada e qual transportadora realizou a entrega final.',
   'A matriz de rastreabilidade vincula objetivos de negócio, requisitos de usuário, modelos UML, código-fonte e casos de teste, viabilizando análises de impacto precisas.'),

  # Questao 04
  (4, '05. Como escrever requisitos de qualidade - critérios, padrões e boas práticas.md',
   'Critérios de qualidade de requisitos (exequibilidade)', 'medio',
   'Um cliente solicita que o sistema identifique fraudes financeiras com precisão de 100% em tempo real, sem falsos positivos, usando apenas um computador doméstico comum. Ao demonstrar a impossibilidade física e computacional dessa demanda, a equipe avalia qual atributo?',
   'Verificabilidade exclusiva por código.',
   'Rastreabilidade com o banco de dados.',
   'Modularidade da documentação.',
   'Exequibilidade da necessidade proposta.',
   3,
   'Incorreto: verificabilidade é a capacidade de testar o requisito, não a viabilidade de sua realização com os recursos dados.',
   'Incorreto: rastreabilidade conecta artefatos, não avaliando se a demanda é tecnicamente realizável.',
   'Incorreto: modularidade diz respeito à decomposição documental ou de código.',
   'Correto: exequibilidade (viabilidade) avalia se o requisito pode ser construído dentro das restrições reais de tecnologia, orçamento, infraestrutura e prazos disponíveis.',
   'É como pedir para construir um foguete espacial tripulado utilizando apenas peças de bicicleta e madeira: a proposta é fisicamente inexequível com os recursos exigidos.',
   'Um requisito inatingível ou fantasioso deve ser negociado e readequado durante a análise de viabilidade, antes de comprometer o escopo formal do projeto.'),

  # Questao 05
  (5, '04. Requisitos funcionais e não-funcionais.md',
   'Classificação de requisitos (funcional vs. não-funcional)', 'facil',
   'Identifique a sentença que representa um requisito funcional em um sistema acadêmico:',
   'O banco de dados deve utilizar criptografia AES de 256 bits.',
   'O estudante poderá consultar suas notas por disciplina.',
   'O tempo de resposta deve ser inferior a dois segundos.',
   'A interface precisa seguir o padrão visual corporativo da instituição.',
   1,
   'Incorreto: trata-se de um requisito não-funcional de segurança.',
   'Correto: expressa uma funcionalidade, ação ou serviço direto prestado pelo sistema ao usuário.',
   'Incorreto: trata-se de um requisito não-funcional de desempenho.',
   'Incorreto: trata-se de um requisito não-funcional de usabilidade e identidade visual.',
   'O requisito funcional responde a "o que o sistema faz quando o usuário clica?", enquanto o não-funcional responde a "sob quais critérios de qualidade ou restrições ele faz?".',
   'Requisitos funcionais definem os fluxos operacionais, regras de transformação e serviços que satisfazem as necessidades de uso dos atores.'),

  # Questao 06
  (6, '04. Requisitos funcionais e não-funcionais.md',
   'Requisitos não-funcionais e métricas mensuráveis', 'medio',
   'Para um sistema de comércio eletrônico, a equipe precisa redigir uma restrição de desempenho mensurável e testável. Qual formulação cumpre adequadamente o papel de requisito não-funcional?',
   'O sistema deverá ser rápido e agradável ao usuário.',
   'A consulta de pedido deverá responder em até três segundos nas condições de uso especificadas.',
   'O cliente poderá cadastrar itens no carrinho de compras.',
   'Sempre que possível, o sistema processará relatórios em pouco tempo.',
   1,
   'Incorreto: termos como "rápido" e "agradável" são vagos, subjetivos e intestáveis.',
   'Correto: estipula uma métrica objetiva, quantificável e passível de verificação experimental em testes de carga.',
   'Incorreto: expressa um requisito funcional de negócio (adicionar itens ao carrinho).',
   'Incorreto: "sempre que possível" e "pouco tempo" são qualificadores ambíguos que impedem validação rigorosa.',
   'Em vez de dizer "o carro esportivo deve correr muito", a especificação técnica diz "o carro deve atingir 100 km/h em até 3,5 segundos com carga padrão".',
   'Requisitos não-funcionais mensuráveis evitam disputas contratuais porque fornecem critérios binários ou faixas numéricas de aceitação nos testes de desempenho.'),

  # Questao 07
  (7, '01. O que é, afinal, engenharia de requisitos.md',
   'Processo e macroatividades da engenharia de requisitos', 'facil',
   'Qual sequência reflete adequadamente a transição de fases típica das atividades de engenharia de requisitos?',
   'Deploy em produção → codificação rápida → escrita dos manuais.',
   'Homologação final → testes unitários → definição do escopo.',
   'Elicitação → modelagem → verificação e validação.',
   'Refatoração de arquitetura → compilação → levantamento inicial.',
   2,
   'Incorreto: fases tardias de ciclo de vida operacional não compõem a engenharia de requisitos.',
   'Incorreto: inverte testes finais antes de conceber o escopo.',
   'Correto: o ciclo clássico de requisitos envolve descobrir as necessidades (elicitação), representá-las em modelos e textos (modelagem/especificação) e atestar sua correção e valor (verificação e validação).',
   'Incorreto: compilação e refatoração arquitetural são atividades posteriores de construção de código.',
   'Primeiro você conversa com os clientes para colher as ideias (elicitação), depois desenha os diagramas e plantas (modelagem) e, por fim, confere se o projeto bate com as normas e o que o cliente pediu (V&V).',
   'Essas atividades não são estritamente em cascata; em ambientes ágeis ocorrem iterativa e incrementalmente, mantendo a mesma relação de precedência lógica.'),

  # Questao 08
  (8, '06. Técnicas de elicitação de requisitos.md',
   'Técnicas de elicitação (entrevista semiestruturada)', 'medio',
   'Um analista precisa entender as dores de três gestores de logística em profundidade, mas deseja ter liberdade para explorar novos tópicos à medida que surgirem durante a conversa. Qual técnica e formato são mais indicados?',
   'Questionário eletrônico de múltipla escolha com perguntas obrigatórias.',
   'Entrevista com roteiro preparado e possibilidade de adaptação.',
   'Inspeção estática de código-fonte de sistemas concorrentes.',
   'Simulação automatizada de estresse de infraestrutura.',
   1,
   'Incorreto: questionários fechados engessam a conversa e impedem desvios exploratórios.',
   'Correto: a entrevista semiestruturada oferece um esqueleto básico de tópicos planejados com a flexibilidade dialógica para aprofundar insights inesperados.',
   'Incorreto: inspeção de código estuda implementação de software, não as dores humanas dos gestores.',
   'Incorreto: teste de estresse afere carga computacional em servidores.',
   'É como um jornalista experiente: ele leva uma lista de perguntas no bloco de notas, mas se o entrevistado der uma declaração surpreendente, ele puxa esse fio e explora o tema a fundo.',
   'A entrevista semiestruturada equilibra cobertura dos tópicos essenciais do projeto com flexibilidade para descobrir requisitos ocultos e motivações subjacentes.'),

  # Questao 09
  (9, '06. Técnicas de elicitação de requisitos.md',
   'Técnicas de elicitação (brainstorming)', 'medio',
   'No início da concepção de um aplicativo de fidelidade inovador, a equipe precisa gerar grande variedade de ideias sem julgamentos prévios de viabilidade. Qual técnica de elicitação colaborativa deve ser conduzida?',
   'Auditoria de conformidade com normas contábeis.',
   'Revisão formal de especificação com aprovação rígida.',
   'Engenharia reversa de assembly de drivers.',
   'Brainstorming facilitado para estimular diferentes ideias.',
   3,
   'Incorreto: auditoria foca em checagem normativa restritiva.',
   'Incorreto: revisões formais com julgamento precoce inibem a geração de ideias inovadoras.',
   'Incorreto: engenharia reversa de código de máquina é análise técnica de baixo nível.',
   'Correto: o brainstorming busca volume e originalidade de propostas em grupo sob a regra expressa de suspender críticas e julgamentos na fase inicial.',
   'Pense em uma sessão de post-its onde qualquer ideia é colada na parede sem ninguém dizer "isso é impossível", abrindo espaço para soluções fora da caixa antes do filtro final.',
   'O brainstorming foca na divergência criativa; apenas na etapa posterior as propostas são categorizadas, refinadas e submetidas a filtros de viabilidade técnica e financeira.'),

  # Questao 10
  (10, '06. Técnicas de elicitação de requisitos.md',
   'Técnicas de elicitação (questionários em larga escala)', 'medio',
   'Para coletar dados de 5.000 clientes distribuídos geograficamente por todo o país sobre a frequência de uso de recursos em um aplicativo bancário, qual estratégia de elicitação é mais eficiente?',
   'Conduzir reuniões presenciais individuais de duas horas com cada um.',
   'Observação participante de cada cliente em sua residência.',
   'Distribuir questionário predominantemente com perguntas fechadas.',
   'Organizar uma oficina presencial com todos os clientes juntos em uma única sala.',
   2,
   'Incorreto: inviável em termos de tempo e custo financeiro para milhares de pessoas.',
   'Incorreto: logisticamente impossível e com custo proibitivo.',
   'Correto: formulários padronizados com perguntas fechadas atingem grandes públicos geograficamente dispersos a baixo custo e geram dados quantitativos estatisticamente tratáveis.',
   'Incorreto: reunir milhares de pessoas dispersas pelo país em uma sala é inviável operacionalmente.',
   'Para saber a opinião de milhões de eleitores sobre um serviço, os institutos enviam formulários estruturados por telefone ou internet, pois entrevistar presencialmente um a um por horas seria impraticável.',
   'Questionários fechados operam com escalas Likert e múltipla escolha, facilitando a agregação estatística de tendências de adoção de funcionalidades.'),

  # Questao 11
  (11, '06. Técnicas de elicitação de requisitos.md',
   'Técnicas de elicitação (etnografia e observação direta)', 'dificil',
   'Os operadores de uma central de despacho realizam atalhos operacionais e consultas cruzadas não documentadas nos manuais oficiais. Qual técnica é mais indicada para capturar esse conhecimento tácito na prática?',
   'Leitura isolada do manual de políticas da empresa.',
   'Aplicação de prova teórica sobre o processo formal.',
   'Questionário com opções prefixadas sobre regras corporativas.',
   'Etnografia por observação das atividades no ambiente real.',
   3,
   'Incorreto: o manual registra apenas o processo prescrito formal, omitindo os improvisos reais.',
   'Incorreto: provas teóricas apenas aferem o conhecimento do processo idealizado.',
   'Incorreto: questionários fechados não capturam práticas espontâneas que o operador nem percebe que realiza.',
   'Correto: a etnografia e observação direta acompanham o trabalho em seu contexto real, revelando conhecimento tácito, atalhos e gargalos invisíveis no discurso oficial.',
   'É como um documentarista que vai conviver com uma comunidade para filmar a rotina real dos pescadores em vez de apenas ler o estatuto da associação de pesca.',
   'Sommerville destaca que a etnografia é a técnica primorosa para descobrir como as pessoas realmente operam e cooperam no dia a dia, superando a distância entre a norma prescrita e o trabalho real.'),

  # Questao 12
  (12, '06. Técnicas de elicitação de requisitos.md',
   'Técnicas de elicitação (prototipagem)', 'medio',
   'Quando usuários têm dificuldade em expressar o que esperam das telas e do fluxo de navegação a partir de textos formais, qual abordagem auxilia na elicitação e na redução de ambiguidades?',
   'Obrigar os usuários a redigirem scripts de teste em automação.',
   'Substituir reuniões por diagramas de arquitetura de rede interna.',
   'Apresentar um protótipo de tela para obter comentários e ajustes.',
   'Finalizar o desenvolvimento completo antes de exibir qualquer interface.',
   2,
   'Incorreto: usuários finais de negócio não dominam código de testes automatizados.',
   'Incorreto: topologia de rede física não comunica regras de interface e navegação com o usuário.',
   'Correto: protótipos de baixa ou alta fidelidade tornam as ideias visíveis e palpáveis, ajudando o usuário a identificar o que falta, corrigir premissas e elicitar requisitos latentes.',
   'Incorreto: esperar o fim da entrega gera custos catastróficos de retrabalho caso o escopo esteja desalinhado.',
   'É o princípio "eu sei o que quero quando vejo" (IKIWISI): ao ver uma maquete 3D da casa, o comprador percebe na hora se o quarto ficou escuro ou se a porta bate no armário.',
   'A prototipagem atua como ferramenta semiótica de mediação entre analistas e clientes, acelerando ciclos de validação e refinamento de requisitos.'),

  # Questao 13
  (13, '07. Visão geral da uml e tipos de diagramas na modelagem de requisitos.md',
   'Papel e natureza da UML na engenharia de software', 'medio',
   'A respeito do papel da UML (Unified Modeling Language) na engenharia de requisitos e software, qual afirmação é correta?',
   'A UML é uma linguagem de modelagem, não uma metodologia que determina a ordem do trabalho.',
   'A UML é uma linguagem de programação compilada que gera código executável automaticamente.',
   'A UML substitui completamente qualquer necessidade de diálogo com stakeholders.',
   'A UML proíbe o uso de textos explicativos ou tabelas complementares na especificação.',
   0,
   'Correto: a UML define uma notação gráfica formal e semântica de modelagem, sendo agnóstica a metodologias (não dita processo, papéis, fases ou ritos de desenvolvimento).',
   'Incorreto: a UML é uma linguagem visual de especificação e documentação, não um código executável compilável por si só.',
   'Incorreto: modelos UML apoiam o diálogo, não substituindo a comunicação e negociação com stakeholders.',
   'Incorreto: a especificação textual complementar (ex.: cenários de casos de uso) é parte essencial da prática de engenharia de software.',
   'A UML é como o conjunto de símbolos do desenho arquitetônico (símbolo de janela, porta, tomada): ela padroniza como desenhar a casa, mas não decide se você constrói em método ágil ou cascata.',
   'Padronizada pela OMG (Object Management Group), a UML estabelece vocabulário e regras sintáticas para diagramas estruturais e comportamentais sem ditar o processo de desenvolvimento adotado pela empresa.'),

  # Questao 14
  (14, '08. Modelagem de requisitos com casos de uso e especificações textuais.md',
   'Diagrama de casos de uso (atores e fronteira)', 'facil',
   'Em um diagrama de casos de uso de um sistema de vendas online, um gateway de pagamentos terceirizado envia confirmações de transação via webhook. Como esse serviço externo deve ser modelado?',
   'Como ator externo que interage com o sistema.',
   'Como caso de uso interno do sistema.',
   'Como atributo privado de uma classe de domínio.',
   'Como um pacote restrito de banco de dados.',
   0,
   'Correto: atores na UML representam qualquer entidade externa ao sistema (usuários humanos, dispositivos de hardware ou outros sistemas/APIs) que interage com ele.',
   'Incorreto: o gateway é um sistema independente fora da fronteira, e não uma função fornecida pelo sistema em modelagem.',
   'Incorreto: atributos privados são elementos de diagrama de classes, não entidades externas de casos de uso.',
   'Incorreto: pacotes de banco são componentes de arquitetura de implementação estrutural.',
   'Pense no entregador dos Correios: ele não mora dentro da sua casa nem é cômodo da sua casa, mas é uma entidade externa que bate na sua porta para entregar ou retirar encomendas.',
   'Atores representam papéis externos que disparam eventos de entrada ou recebem respostas de saída através da fronteira do sistema (*system boundary*).'),

  # Questao 15
  (15, '08. Modelagem de requisitos com casos de uso e especificações textuais.md',
   'Relacionamentos em casos de uso (inclusão / include)', 'medio',
   'Ao modelar "Realizar transferência bancária" e "Consultar saldo", observa-se que ambos executam invariavelmente a mesma rotina "Autenticar correntista". Qual relacionamento da UML conecta esses casos de uso ao caso de autenticação?',
   'Generalização, porque autenticar é subtipo de transferência.',
   'Inclusão, pois o comportamento é utilizado obrigatoriamente pelo caso principal.',
   'Extensão, porque o comportamento ocorre apenas em caso de falha de conexão.',
   'Agregação simples de classes.',
   1,
   'Incorreto: autenticar e transferir não mantêm vínculo de taxonomia ontológica ("é um tipo de").',
   'Correto: o relacionamento «include» indica que o caso de uso base incorpora obrigatoriamente e incondicionalmente o comportamento do caso incluído como parte de sua execução.',
   'Incorreto: «extend» modela comportamentos condicionais ou opcionais, não etapas mandatórias.',
   'Incorreto: agregação é relação estrutural entre classes, inexistente entre casos de uso.',
   'É como a diretiva `#include` em programação ou uma sub-rotina obrigatória: para transferir ou tirar extrato, o sistema obrigatoriamente roda a rotina de autenticação.',
   'A inclusão fatoriza comportamentos comuns entre múltiplos casos de uso, evitando redundância e promovendo reuso nas especificações textuais.'),

  # Questao 16
  (16, '08. Modelagem de requisitos com casos de uso e especificações textuais.md',
   'Relacionamentos em casos de uso (extensão / extend)', 'medio',
   'No caso de uso "Finalizar compra", o cliente pode optar por inserir um cupom de desconto promocional caso possua um. Qual relacionamento deve ligar "Aplicar cupom promocional" a "Finalizar compra"?',
   'Inclusão, pois o cupom sempre é digitado em todas as compras.',
   'Extensão, porque o desconto depende de condição específica.',
   'Herança múltipla entre casos de uso independentes.',
   'Composição forte com destruição em cascata.',
   1,
   'Incorreto: inclusão obrigaria todos os compradores a possuírem e digitarem um cupom para concluir a compra.',
   'Correto: o relacionamento «extend» especifica que um caso de uso secundário pode estender o fluxo do caso base apenas se determinada condição de extensão (*extension point*) for satisfeita.',
   'Incorreto: herança entre casos de uso expressa especialização de objetivos, não acréscimo condicional de passo opcional.',
   'Incorreto: composição é conceito estrito do diagrama estrutural de classes.',
   'Pense no airbag lateral de um carro: o carro anda e freia normalmente sem ele, mas se o comprador adquirir o pacote opcional (condição), o airbag entra em ação em um ponto específico de colisão.',
   'No relacionamento de extensão, a seta pontilhada aponta do caso estensor para o caso base, indicando que o caso base funciona plenamente sozinho sem conhecimento do estensor.'),

  # Questao 17
  (18, '08. Modelagem de requisitos com casos de uso e especificações textuais.md', # id 17
   'Generalização entre atores em casos de uso', 'medio',
   'Em um hospital, todo Gerente tem acesso a todas as ações permitidas a um Funcionário comum, além de funcionalidades administrativas extras. Como modelar essa relação no diagrama de casos de uso?',
   'Associação bidirecional com cardinalidade 1..* entre os dois.',
   'Inclusão do ator Funcionário pelo ator Gerente com estereótipo «include».',
   'Generalização de Gerente para Funcionário.',
   'Extensão de ator para caso de uso por seta pontilhada.',
   2,
   'Incorreto: associação regular indicaria comunicação de dados entre eles, não herança de direitos funcionais.',
   'Incorreto: «include» é exclusivo para conectar casos de uso a casos de uso, sendo sintaticamente ilegal entre atores.',
   'Correto: a generalização/especialização entre atores faz com que o ator especializado (Gerente) herde automaticamente todas as associações de casos de uso do ator mais geral (Funcionário).',
   'Incorreto: «extend» não conecta atores a casos de uso nem atores entre si.',
   'Todo Gerente de banco é um Funcionário do banco: ele tem o crachá básico para entrar no prédio e usar o refeitório, mas possui chaves adicionais para abrir o cofre.',
   'A generalização entre atores simplifica diagramas ao eliminar teias de setas repetidas: desenham-se apenas as novas associações exclusivas ligadas ao ator filho.'),

  # Questao 18
  (18, '09. Modelagem estrutural com diagrama de classes da uml.md',
   'Elementos do diagrama de classes (atributos vs. operações)', 'medio',
   'Na representação retangular de uma classe UML para "Produto", aparecem "codigo", "preco" e "atualizarPreco()". Como esses elementos são categorizados tecnicamente?',
   'Todos são métodos de execução assíncrona.',
   '“codigo” e “preco” são atributos; “atualizarPreco()” é método.',
   'Todos são atributos persistentes de tabela relacional.',
   '“codigo” é pacote, “preco” é interface e “atualizarPreco()” é classe.',
   1,
   'Incorreto: variáveis de estado de dados não são rotinas executáveis.',
   'Correto: atributos representam o estado e as propriedades estruturais da classe, enquanto métodos/operações expressam os comportamentos e transformações executáveis.',
   'Incorreto: atualizarPreco() denota comportamento (verbo/ação), não coluna de dados persistente.',
   'Incorreto: confunde conceitos de níveis arquiteturais totalmente distintos com membros de classe.',
   'Pense no prontuário de um paciente: nome e tipo sanguíneo são as informações anotadas no papel (atributos); aplicar injeção ou aferir pressão são os procedimentos médicos realizados (métodos).',
   'Na UML, o compartimento intermediário do retângulo lista os atributos com sua tipagem e visibilidade (+, -, #), e o compartimento inferior lista as operações/assinaturas de métodos.'),

  # Questao 19
  (19, '09. Modelagem estrutural com diagrama de classes da uml.md',
   'Relacionamento de herança no diagrama de classes', 'medio',
   'Em uma farmácia, tanto Farmacêutico quanto Atendente compartilham os dados "matricula" e "nome", mas Farmacêutico possui "crf" (registro profissional) e Atendente possui "comissao". Qual relação da UML representa essa estrutura de forma canônica?',
   'Dependência de compilação transitória.',
   'Agregação fraca entre Farmacêutico e Atendente.',
   'Composição estrita em que Farmacêutico contém Atendente.',
   'Herança, com Farmacêutico e Atendente especializados de Funcionário.',
   3,
   'Incorreto: dependência reflete uso efêmero de uma classe por outra, sem reaproveitamento estrutural de atributos.',
   'Incorreto: farmacêutico e atendente não mantêm vínculo todo-parte entre si.',
   'Incorreto: um profissional não é composto internamente por outro profissional.',
   'Correto: a herança (generalização/especialização) define uma superclasse base (Funcionário) contendo dados comuns e subclasses que herdam essa base e agregam suas particularidades.',
   'Na biologia, tanto cães quanto gatos são mamíferos (superclasse) com pelos e sangue quente, mas o cão possui latido e o gato possui miado (subclasses especializadas).',
   'A generalização é indicada por uma linha contínua terminada em um triângulo oco (vazio) apontando da subclasse para a superclasse na notação padrão da UML.'),

  # Questao 20
  (20, '09. Modelagem estrutural com diagrama de classes da uml.md',
   'Composição vs. agregação (ciclo de vida e dependência)', 'dificil',
   'Ao modelar "Pedido" e "ItemPedido", a regra de negócio dita que itens de pedido não podem existir fora de um pedido e são destruídos caso o pedido seja cancelado e excluído. Qual relacionamento UML expressa exatamente essa semântica?',
   'Agregação compartilhada representada por losango branco/vazio.',
   'Associação simples sem multiplicidade definida.',
   'Composição, com dependência de existência da parte em relação ao todo.',
   'Generalização por polimorfismo dinâmico.',
   2,
   'Incorreto: agregação compartilhada (losango vazio) permite que as partes existam independentemente e sobrevivam à destruição do todo.',
   'Incorreto: associação simples não expressa a forte dependência existencial todo-parte exigida pela regra.',
   'Correto: a composição (agregação composta, indicada por losango preenchido no lado do todo) impõe acoplamento vital: as partes pertencem exclusivamente a um todo e são destruídas com ele.',
   'Incorreto: herança trata de hierarquia de tipos, não de agrupamento de instâncias parte-todo.',
   'Pense nas paredes de um prédio: se o edifício for implodido e demolido, as paredes deixam de existir junto com ele (composição). Já os carros no estacionamento do prédio continuam existindo mesmo se o prédio for demolido (agregação).',
   'Na composição da UML, a cardinalidade no lado do todo é estritamente 1 (ou 0..1 em criação inicial), garantindo propriedade exclusiva de ciclo de vida.'),

  # Questao 21
  (21, '09. Modelagem estrutural com diagrama de classes da uml.md',
   'Classe associativa em relacionamentos N:N', 'dificil',
   'Um "Estudante" pode se matricular em várias "Disciplinas", e cada disciplina possui múltiplos estudantes. Para armazenar a "dataMatricula" e a "notaFinal" desse vínculo específico, qual recurso da UML deve ser empregado?',
   'Duplicar o atributo "notaFinal" dentro da classe Disciplina como vetor estático.',
   'Representar uma classe associativa Matrícula vinculada à associação.',
   'Transformar Disciplina em subclasse de Estudante via herança múltipla.',
   'Criar um caso de uso para substituir as duas classes.',
   1,
   'Incorreto: colocar a nota em Disciplina ou em Estudante corrompe o modelo quando há dezenas de notas de alunos diferentes na mesma matéria.',
   'Correto: uma classe associativa anexa atributos e comportamentos ao próprio relacionamento entre duas classes, existindo em função da ligação entre uma instância de Estudante e uma de Disciplina.',
   'Incorreto: herança viola frontalmente a semântica de domínio (uma disciplina não "é um" estudante).',
   'Incorreto: casos de uso modelam intenções comportamentais do usuário, não modelagem relacional orientada a objetos.',
   'A nota não é uma característica só do aluno (pois ele tem notas diferentes em cálculo e biologia) nem só da disciplina (que tem dezenas de alunos). A nota é uma propriedade que só existe no cruzamento do aluno matriculado na matéria.',
   'Graficamente, a classe associativa é exibida como uma classe normal conectada por uma linha pontilhada à linha de associação que une as duas classes participantes.'),

  # Questao 22
  (22, '10. Modelagem estrutural e modularização com diagrama de pacotes da uml.md',
   'Diagrama de pacotes e organização em subsistemas', 'medio',
   'Para organizar um sistema de grande porte em subsistemas modulares (como "ModuloFinanceiro", "ModuloVendas" e "ModuloAutenticacao") e ilustrar as dependências entre eles, qual diagrama da UML é o mais indicado?',
   'Diagrama de máquina de estados de uma variável booleana.',
   'Diagrama de atividades de cálculo de raiz quadrada.',
   'Diagrama de sequência de uma única linha de comando.',
   'Diagrama de pacotes, que agrupa classes relacionadas e representa dependências.',
   3,
   'Incorreto: máquina de estados foca no ciclo de vida dinâmico de instâncias individuais de objetos.',
   'Incorreto: diagrama de atividades ilustra fluxo de processamento operacional algorítmico.',
   'Incorreto: diagrama de sequência detalha troca cronológica de mensagens pontuais entre objetos em tempo de execução.',
   'Correto: o diagrama de pacotes é o artefato estrutural por excelência para agrupar elementos lógicos em subsistemas/camadas e explicitar acoplamentos e dependências de alto nível.',
   'Pense nas pastas e gavetas de um arquivo de escritório: você guarda todos os documentos contábeis na gaveta "Financeiro" e os contratos na gaveta "Jurídico", organizando o caos do escritório.',
   'Pacotes na UML são representados pelo ícone de pasta com aba (*tabbed folder*) e apoiam a visão arquitetural de camadas (como Controller, Service, Repository) e microsserviços.'),

  # Questao 23
  (23, '07. Visão geral da uml e tipos de diagramas na modelagem de requisitos.md',
   'Ferramentas CASE e consistência semântica de modelos', 'dificil',
   'Em um projeto corporativo regulamentado, a equipe precisa garantir que modelos UML mantenham coerência semântica e suporte à geração de relatórios técnicos de engenharia reversa. Qual prática é recomendada?',
   'Desenhar todos os diagramas em editores gráficos genéricos sem checagem de tipos.',
   'Proibir o versionamento de arquivos de modelagem em repositórios de código.',
   'Substituir toda modelagem por transcrições gravadas em áudio.',
   'Utilizar ferramenta CASE com suporte à notação UML, revisando os relacionamentos representados.',
   3,
   'Incorreto: editores de desenho genéricos não validam o metamodelo UML, permitindo erros semânticos graves.',
   'Incorreto: o versionamento em repositórios é essencial para governança e evolução de modelos.',
   'Incorreto: gravações de áudio não fornecem especificação estruturada nem permitem engenharia reversa automatizada.',
   'Correto: ferramentas CASE (*Computer-Aided Software Engineering*) sustentam um metamodelo computável por trás dos diagramas visuais, permitindo validar regras sintáticas, rastreabilidade e sincronização com código.',
   'É a diferença entre desenhar uma planta elétrica no Paint (onde qualquer linha torta é desenhada sem avisar sobre curto-circuito) e desenhar em um CAD profissional com validação automática de circuitos elétricos.',
   'Ferramentas CASE profissionais mantêm um repositório centralizado de elementos de modelo, garantindo que a renomeação de uma classe seja refletida em todos os diagramas de classes, casos de uso e sequência.'),

  # Questao 24
  (24, '11. Verificação e validação de requisitos - técnicas, revisões e qualidade.md',
   'Validação vs. verificação de requisitos', 'medio',
   'A célebre distinção de Boehm pergunta: "Estamos construindo o produto certo?". Na engenharia de requisitos, essa pergunta corresponde a qual atividade fundamental?',
   'Verificação estritamente gramatical do texto do contrato.',
   'Benchmarking do clock do processador em tempo de execução.',
   'Validação dos requisitos frente às necessidades reais do cliente.',
   'Compilação otimizada com flags de depuração ativadas.',
   2,
   'Incorreto: conferência sintática/gramatical é uma técnica local de verificação de padrão textual.',
   'Incorreto: velocidade de clock de CPU é aferição de hardware, sem relação com atendimento das necessidades de negócio.',
   'Correto: a validação certifica se os requisitos expressam exatamente o que o cliente necessita para resolver seus problemas de negócio ("o produto certo").',
   'Incorreto: diretivas de compilação são detalhes operacionais de construção técnica.',
   'Verificação é conferir se a receita culinária foi seguida à risca com as medidas certas; validação é dar o bolo para o cliente provar e confirmar se era mesmo aquele bolo que ele desejava para a sua festa.',
   'A validação foca no valor e na adequação ao usuário final, enquanto a verificação (*Are we building the product right?*) foca na conformidade técnica com normas, padrões e ausência de contradições lógicas.'),

  # Questao 25
  (25, '11. Verificação e validação de requisitos - técnicas, revisões e qualidade.md',
   'Técnicas de verificação (inspeção formal de requisitos)', 'medio',
   'Durante uma sessão de revisão formal da documentação, os engenheiros comparam o diagrama de casos de uso com o diagrama de classes para checar se todos os conceitos citados nas ações possuem classes correspondentes, além de checar conformidade com o padrão da empresa. Qual atividade está sendo realizada?',
   'Deploy contínuo em ambiente de homologação externa.',
   'Verificação por inspeção da consistência entre os modelos produzidos.',
   'Elicitação primária de requisitos por questionário anônimo.',
   'Engenharia reversa automática por descompilador de bytecode.',
   1,
   'Incorreto: deploy é etapa operacional de infraestrutura e entrega de binários executáveis.',
   'Correto: a inspeção técnica de requisitos analisa a consistência interna e cruzada entre artefatos de modelagem, checando conformidade formal com diretrizes metodológicas.',
   'Incorreto: elicitação é a descoberta inicial de requisitos, enquanto o cenário descreve a auditoria crítica de modelos já consolidados.',
   'Incorreto: descompilação de bytecode analisa código compilado, não a coerência semântica de especificações conceituais.',
   'É como o engenheiro chefe revisando a planta hidráulica contra a planta estrutural da obra para ter certeza absoluta de que nenhum cano passa por dentro de uma viga mestra de sustentação.',
   'Inspeções formais (baseadas no método de Fagan) detectam ambiguidades, lacunas e discrepâncias entre modelos antes de uma única linha de código ser escrita, reduzindo brutalmente o custo de defeitos.')
]

# Adjust question 17 tuple which had id_num 18 by mistake in raw
for idx, r in enumerate(raw):
    actual_id = idx + 1
    add_q(actual_id, r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12], r[13], r[14], r[15])

print(f"Geradas {len(puc_questions)} questoes de revisao oficial para Engenharia de Requisitos.")

req_path = '/home/antigravity/leorruas/puc/banco-de-questoes/07.engenharia-de-requisitos.json'
with open(req_path, 'r', encoding='utf-8') as f:
    existing_req = json.load(f)

# Filter out any old REQ-REV
clean_base = [q for q in existing_req if not q.get('id', '').startswith('REQ-REV-')]
print(f"Questoes base preservadas: {len(clean_base)}")

for q in clean_base:
    if 'prioritaria' not in q:
        q['prioritaria'] = False
    if 'origem' not in q:
        q['origem'] = 'banco_sintetico_vault'

merged = puc_questions + clean_base

with open(req_path, 'w', encoding='utf-8') as f:
    json.dump(merged, f, ensure_ascii=False, indent=2)

print(f"Sucesso: {len(merged)} questoes salvas em {req_path}.")
