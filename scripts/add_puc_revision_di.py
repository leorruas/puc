import json
import os

base_ref = '08. Design de Interacao/'
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
        'id': f'DI-REV-{id_num:03d}',
        'disciplina_id': '08',
        'disciplina': 'Design de Interação',
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
  (1, '04. Perspectivas de interação usuário-sistema - interagir com o sistema vs. por meio do sistema.md',
   'Perspectivas da interação (com o sistema vs. por meio do sistema)', 'medio',
   'Um aplicativo de transporte permite que o passageiro solicite uma corrida e, durante o trajeto, acompanhe as ações do motorista. A equipe discute se o foco do design deve ficar apenas nos botões e nas telas.\n\nQual interpretação da interação é mais adequada para orientar o projeto?',
   'Considerar as ações do passageiro com o sistema e a atividade humana mediada por ele.',
   'Limitar a análise ao desempenho computacional do servidor.',
   'Tratar a interação como exclusivamente uma propriedade visual.',
   'Considerar apenas a troca de comandos entre passageiro e aplicativo.',
   0,
   'Correto: a interação engloba tanto o diálogo direto usuário-sistema (interagir com o sistema) quanto a atividade humana e colaborativa que ocorre através da tecnologia (interagir por meio do sistema).',
   'Incorreto: o desempenho do servidor é requisito técnico de infraestrutura, mas não esgota o design da interação humana.',
   'Incorreto: a interação é comportamental, comunicativa e funcional, não apenas cosmética ou visual.',
   'Incorreto: ignorar a mediação humana entre passageiro e motorista reduz indevidamente o escopo da atividade.',
   'Pense em um telefone celular durante uma ligação com um médico: você aperta botões no aparelho (interagir COM o sistema), mas seu objetivo real é conversar com o médico para cuidar da sua saúde (interagir POR MEIO do sistema). O design precisa cuidar dos dois níveis.',
   'Na teoria de IHC (como em Bødker e Kuutti), os sistemas interativos atuam como artefatos mediadores da atividade humana, integrando o diálogo com a interface e a comunicação social viabilizada por ela.'),

  # Questão 02
  (2, '03. O papel dos sistemas interativos na atividade humana.md',
   'Papel dos sistemas interativos e apoio ao objetivo real do usuário', 'facil',
   'Um município pretende lançar um aplicativo para solicitar manutenção de iluminação pública. O sistema registra solicitações corretamente, mas moradores não conseguem acompanhar se o serviço foi executado, comprometendo a atividade que pretendem realizar.\n\nNa avaliação do papel do sistema interativo nessa atividade, qual evidência deve receber maior atenção?',
   'Quantidade total de menus construídos para o aplicativo.',
   'Capacidade de apoiar o acompanhamento e a conclusão do objetivo real do morador.',
   'Número de ferramentas usadas pelos desenvolvedores.',
   'Quantidade de funcionalidades independentemente de sua utilidade.',
   1,
   'Incorreto: a quantidade de menus não mede o sucesso ou a utilidade da atividade.',
   'Correto: sistemas interativos são meios para apoiar a atividade humana; a qualidade do sistema mede-se por sua capacidade de ajudar o usuário a alcançar seu objetivo final (saber se o poste foi consertado e a rua iluminada).',
   'Incorreto: ferramentas internas da equipe não têm relação com a experiência do cidadão.',
   'Incorreto: funcionalidades inúteis ou desconectadas do objetivo geram sobrecarga e frustração.',
   'O morador não baixou o aplicativo para se divertir abrindo menus; ele baixou porque a rua dele está escura e ele quer segurança. Se o aplicativo grava o chamado mas não avisa quando o poste foi consertado, o objetivo humano ficou pelo caminho.',
   'Na Teoria da Atividade aplicada a IHC, ações intermediárias (abrir chamado) só ganham sentido quando articuladas à motivação da atividade global (resolver o problema da iluminação).'),

  # Questão 03
  (3, '08. Engenharia cognitiva e os problemas da interação usuário-sistema.md',
   'Engenharia Cognitiva e o Golfo de Execução de Donald Norman', 'medio',
   'Em um terminal de autoatendimento, a pessoa sabe que deseja imprimir um comprovante, mas não encontra uma ação correspondente nas opções visíveis. A equipe quer interpretar a dificuldade pela lente cognitiva.\n\nA dificuldade está mais diretamente associada a qual problema?',
   'À distância entre a intenção do usuário e as ações que ele percebe como disponíveis.',
   'À falta de criptografia na comunicação.',
   'À ausência de armazenamento permanente dos dados.',
   'Ao uso de uma linguagem de programação não orientada a objetos.',
   0,
   'Correto: trata-se do clássico Golfo de Execução da Engenharia Cognitiva de Donald Norman: a lacuna entre o que o usuário deseja fazer (intenção psicológica) e os mecanismos físicos/visuais oferecidos pela interface para executar a ação.',
   'Incorreto: criptografia protege a segurança dos dados, mas não resolve a incompreensão da interface.',
   'Incorreto: persistência é camada de banco de dados, sem ligação com a dificuldade de percepção da ação.',
   'Incorreto: o paradigma da linguagem interna não afeta diretamente o modelo mental da interface.',
   'É como estar diante de uma porta automática que não tem maçaneta nem botão visível: você sabe perfeitamente que quer entrar (intenção), mas fica parado sem saber onde empurrar ou pisar para abrir a porta (Golfo de Execução).',
   'O modelo dos Sete Estágios da Ação de Norman divide a interação nos golfos de Execução (planejar e executar ações) e de Avaliação (perceber e interpretar o estado resultante do sistema).'),

  # Questão 04
  (4, '09. Engenharia semiótica - comunicação usuário-sistema e metacomunicação usuário-designer.md',
   'Engenharia Semiótica e metacomunicação designer-usuário', 'medio',
   'Uma tela mostra um ícone pouco convencional para cancelar uma inscrição. Os estudantes interpretam o símbolo como opção de salvar e executam uma ação inesperada. A equipe decide examinar os signos da interface.\n\nQual perspectiva explica mais diretamente o problema?',
   'O cancelamento falha necessariamente por insuficiência de memória RAM.',
   'A interface constitui uma mensagem do projetista que não está sendo interpretada como pretendido.',
   'A causa é exclusivamente o tempo de resposta do servidor.',
   'O comportamento do estudante prova que símbolos visuais dispensam explicação.',
   1,
   'Incorreto: o problema é de significação e semiótica, não de capacidade de memória.',
   'Correto: na Engenharia Semiótica de Clarisse de Souza, a interface é uma mensagem metacomunicativa do designer para o usuário ("eis como compreendi suas necessidades e como concebi que você use este sistema"); quando o signo falha, a comunicação se rompe.',
   'Incorreto: tempo de resposta afeta desempenho, não a interpretação errônea do ícone.',
   'Incorreto: ícones dependem de convenção cultural e repertório compartilhado para serem interpretados corretamente.',
   'A interface é uma carta que o designer escreveu usando botões, cores e ícones: se o designer desenha um símbolo exótico achando que significa "cancelar", mas quem lê a carta entende "salvar", o carteiro entregou a mensagem, mas o diálogo falhou.',
   'A Engenharia Semiótica investiga os signos estáticos, dinâmicos e metalinguísticos para garantir que a intenção do designer seja compreendida pelo usuário.'),

  # Questão 05
  (5, '07. Atributos de qualidade em sistemas interativos - usabilidade, comunicabilidade, acessibilidade e experiência de uso.md',
   'Qualidades da interação: acessibilidade e comunicabilidade de rótulos', 'medio',
   'No portal de uma clínica, o agendamento é rápido quando feito com mouse. Entretanto, usuários que navegam exclusivamente por teclado ficam presos em um menu, e o botão final apresenta o texto genérico "OK", sem indicar que confirmará o atendimento.\n\nConsiderando os atributos de qualidade em design de interação, qual diagnóstico fundamenta melhor a revisão da interface?',
   'A rapidez de agendamento demonstra que a interface atende também aos requisitos de acessibilidade.',
   'As barreiras descritas são exclusivamente problemas de banco de dados.',
   'Basta aumentar o número de cores e animações da tela para eliminar os problemas.',
   'A navegação restrita pelo teclado prejudica a acessibilidade; o rótulo "OK" dificulta compreender o significado da ação.',
   3,
   'Incorreto: velocidade com mouse não compensa nem comprova conformidade de acessibilidade para quem depende de teclado ou leitores de tela.',
   'Incorreto: navegação por teclado e rótulos de botões são problemas de interface e front-end.',
   'Incorreto: cores e animações excessivas pioram a poluição visual e a acessibilidade.',
   'Correto: a impossibilidade de navegar por teclado viola a acessibilidade (princípio Operável da WCAG), e o rótulo vago "OK" prejudica a comunicabilidade, devendo ser substituído por um texto explícito como "Confirmar agendamento".',
   'Dizer apenas "OK" em um botão decisivo é como assinar um contrato que tem apenas uma linha dizendo "Tudo bem": você não sabe se está aceitando pagar, cancelando ou fechando a pasta. E se o teclado não chega lá, a porta está trancada para pessoas com deficiência.',
   'Avaliar a qualidade em IHC exige inspecionar separadamente a usabilidade (eficiência/eficácia), a comunicabilidade (clareza do significado) e a acessibilidade (eliminação de barreiras de entrada).'),

  # Questão 06
  (6, '06. Contexto de uso, interface, interação e papéis do design.md',
   'Contexto de uso: ambiente físico, condições técnicas e objetivos', 'medio',
   'Um aplicativo de consulta a linhas de ônibus funciona bem em um laboratório silencioso. Nas ruas, com luminosidade intensa e conexão instável, pessoas têm dificuldade para ler o horário e atualizar os dados.\n\nQue decisão melhor considera o contexto de uso?',
   'Eliminar as pesquisas com usuários após a implementação.',
   'Projetar e avaliar a solução considerando ambiente físico, condições técnicas e objetivos de quem a utiliza.',
   'Avaliar somente a interface em computadores com conexão estável.',
   'Adotar os mesmos tamanhos de fonte em qualquer dispositivo e situação.',
   1,
   'Incorreto: pesquisas contínuas em campo revelam problemas que o laboratório não antecipa.',
   'Correto: o contexto de uso (segundo a ISO 9241-11) abrange os usuários reais, suas tarefas, seus equipamentos técnicos e o ambiente físico e social onde a interação ocorre.',
   'Incorreto: limitar os testes ao laboratório mascara as dificuldades reais de uso sob sol e 3G instável.',
   'Incorreto: fontes e contraste precisam ser adaptados aos desafios de mobilidade e iluminação externa.',
   'Testar um app de ponto de ônibus sentado na cadeira confortável do escritório com Wi-Fi de alta velocidade é ilusório: na rua tem sol batendo na tela, barulho de caminhão, pressa e sinal de internet fraco. O design precisa resistir à vida real.',
   'O contexto de uso é a moldura de qualquer avaliação de IHC: a mesma interface pode ser excelente em um contexto e inoperante em outro.'),

  # Questão 07
  (7, '01. O que é interação humano-computador e a visão teórica do ser humano.md',
   'Perspectiva humana e multidisciplinaridade em IHC', 'facil',
   'Uma equipe de desenvolvimento de um portal público reúne analistas, profissionais de design e representantes dos cidadãos. Alguns gestores defendem que basta testar o funcionamento do software.\n\nQual orientação está alinhada à Interação Humano-Computador?',
   'Desconsiderar pessoas porque interfaces são exclusivamente técnicas.',
   'Investigar características, necessidades e limitações humanas ao projetar e avaliar a interação.',
   'Substituir a avaliação da experiência por testes de banco de dados.',
   'Concentrar o projeto apenas na escolha da linguagem de programação.',
   1,
   'Incorreto: interfaces existem para conectar pessoas a propósitos; desconsiderar o humano gera sistemas inutilizáveis.',
   'Correto: a disciplina de IHC estuda o design, a avaliação e a implementação de sistemas interativos com foco primário nas capacidades, modelos mentais, limites cognitivos e necessidades dos seres humanos.',
   'Incorreto: testes de banco validam persistência técnica, mas não revelam se o cidadão consegue emitir uma certidão.',
   'Incorreto: a linguagem é meio técnico, não o fim da interação.',
   'Engenharia de software tradicional pergunta: "O código compila sem erros?". Já a Interação Humano-Computador pergunta: "O ser humano de carne, osso, pressa e dúvidas consegue usar isso sem sofrer?".',
   'IHC é um campo multidisciplinar que une computação, psicologia cognitiva, semiótica, ergonomia e design para colocar o humano no centro do projeto.'),

  # Questão 08
  (8, '11. Racionalismo técnico e reflexão em ação - o papel da técnica e da criatividade no design.md',
   'Racionalismo técnico vs. reflexão em ação (Donald Schön)', 'dificil',
   'Ao testar um protótipo de atendimento, uma projetista percebe que um fluxo previsto no planejamento não corresponde à prática dos usuários. Ela altera parte da solução durante a análise da situação, sem abandonar os conhecimentos técnicos.\n\nQue abordagem representa melhor essa atuação?',
   'Aplicação mecânica de uma regra predefinida, sem reconsiderar a situação.',
   'Reflexão em ação, ajustando decisões de projeto diante do problema observado.',
   'Rejeição completa dos métodos de design por causa de um teste.',
   'Adiamento de toda decisão até o sistema estar em produção.',
   1,
   'Incorreto: aplicar cegamente regras prévias ignorando o fracasso empírico é a patologia do racionalismo técnico rígido.',
   'Correto: segundo Donald Schön, o profissional reflexivo pratica a "reflexão em ação", dialogando com a situação de design, reformulando o problema e ajustando as decisões técnicas diante dos imprevistos observados.',
   'Incorreto: a reflexão em ação utiliza o rigor técnico em diálogo com a situação, sem descartar a teoria.',
   'Incorreto: o design iterativo corrige os rumos ainda na fase de prototipagem para evitar custos em produção.',
   'O racionalismo técnico é como um motorista que segue cegamente o GPS mesmo quando vê uma cratera no asfalto; a reflexão em ação é o motorista que usa o mapa, mas olha a pista, desvia da cratera e recalcula a rota na hora.',
   'Projetar sistemas interativos não é mero cálculo dedutivo fechado, mas uma prática reflexiva que combina método técnico com criatividade adaptativa.'),

  # Questão 09
  (9, '10. Envolvimento do usuário no design - projetar de modo independente, centrado ou participativo.md',
   'Níveis de envolvimento: Design Participativo (projetar COM o usuário)', 'medio',
   'Uma prefeitura vai redesenhar seu portal de serviços. Em vez de apenas entrevistar moradores após o lançamento, a equipe os envolve em oficinas para propor fluxos e discutir alternativas desde o início.\n\nEssa decisão corresponde mais diretamente a qual abordagem?',
   'Projeto independente do usuário.',
   'Projeto baseado apenas em requisitos de infraestrutura.',
   'Projeto exclusivamente orientado à estrutura interna do software.',
   'Projeto com o usuário, com participação ativa nas decisões de design.',
   3,
   'Incorreto: o design independente projeta no isolamento sem consultar usuários.',
   'Incorreto: oficinas com cidadãos focam em serviços e fluxos humanos, não infraestrutura de servidores.',
   'Incorreto: a abordagem privilegia a co-criação da experiência, não a arquitetura interna fechada.',
   'Correto: envolver os usuários em oficinas de co-design para propor alternativas e decidir conjuntamente caracteriza o Design Participativo (projetar COM o usuário), indo além do mero teste passivo.',
   'Projetar PARA o usuário é preparar um jantar surpresa e perguntar se ele gostou; projetar COM o usuário (Design Participativo) é ir para a cozinha junto com ele, escolher os temperos e cozinhar a quatro mãos.',
   'A tipologia clássica divide o envolvimento em três posturas: projetar sem o usuário (independente), projetar para o usuário (centrado) e projetar com o usuário (participativo).'),

  # Questão 10
  (10, '13. Prototipagem de sistemas interativos - fidelidade, dimensão, wireframe, mockup e storyboard.md',
   'Papel e benefícios da prototipagem rápida e exploratória', 'facil',
   'Uma equipe possui duas ideias para o fluxo de compra de ingressos e ainda precisa decidir qual delas é mais compreensível. O desenvolvimento completo de ambas seria caro.\n\nQual uso da prototipagem é mais adequado nesse momento?',
   'Escolher a alternativa exclusivamente pela preferência estética do desenvolvedor.',
   'Construir versões simplificadas para discutir alternativas e coletar feedback antes da implementação completa.',
   'Finalizar toda a lógica de produção antes de ouvir os usuários.',
   'Dispensar testes porque protótipos não permitem aprender sobre interação.',
   1,
   'Incorreto: decisões de design devem ser orientadas por evidências empíricas de compreensão do usuário, não gosto pessoal.',
   'Correto: protótipos de baixa ou média fidelidade (como wireframes ou protótipos de papel/clicáveis) permitem testar e descartar ideias concorrentes rapidamente e a baixo custo antes de programar.',
   'Incorreto: programar as duas versões prontas na íntegra seria um desperdício enorme de recursos.',
   'Incorreto: protótipos são exatamente o meio mais eficaz para testar hipóteses de interação precocemente.',
   'Fazer um protótipo é como fazer uma maquete de papelão antes de construir a casa de concreto: você descobre que a escada ficou apertada gastando 10 reais de papelão em vez de 100 mil reais quebrando paredes prontas.',
   'A prototipagem rápida viabiliza o princípio de "falhar cedo e barato" (*fail fast*), refinando os requisitos antes da codificação formal.'),

  # Questão 11
  (11, '15. Componentes e recomendações ergonômicas em sistemas interativos.md',
   'Feedback imediato e prevenção de submissões duplicadas', 'medio',
   'Em um aplicativo de inscrições para atividades culturais, a pessoa toca em "Concluir inscrição" e a tela não apresenta mudança visível enquanto a solicitação é enviada. Para não perder a vaga, ela toca várias vezes e cria registros duplicados.\n\nQual solução de interface responde diretamente à dificuldade observada?',
   'Exibir retorno visível de processamento e impedir novos envios enquanto a operação estiver em andamento.',
   'Trocar a cor do logotipo sem alterar o comportamento da ação.',
   'Ocultar o botão de envio em todos os formulários.',
   'Solicitar que o usuário descubra sozinho se houve cadastro.',
   0,
   'Correto: fornecer feedback imediato (ex.: spinner de carregamento, texto "Enviando...") e desabilitar o botão temporariamente atende à primeira heurística de Nielsen (Visibilidade do estado do sistema) e previne erros operacionais.',
   'Incorreto: alterar o logotipo não altera a falta de feedback da ação.',
   'Incorreto: ocultar o botão impediria os usuários de se inscreverem.',
   'Incorreto: deixar o usuário na dúvida viola o dever primordial de comunicabilidade e transparência da interface.',
   'Apertar um botão sem feedback é como chamar o elevador sem a luz acender: você fica apertando o botão dez vezes seguidas na dúvida se o comando foi registrado.',
   'O feedback oportuno reduz a ansiedade do usuário e garante a integridade transacional ao evitar chamadas duplicadas no back-end.'),

  # Questão 12
  (12, '14. Estética em sistemas interativos - harmonização de cores, fontes e usabilidade.md',
   'Harmonia visual, contraste e legibilidade tipográfica', 'medio',
   'Em um painel de saúde, os resultados aparecem em letras pequenas sobre fundos com contraste reduzido. Alguns usuários relatam dificuldade de leitura, apesar de considerarem o conjunto visual agradável.\n\nQual revisão é a mais adequada?',
   'Usar exclusivamente cores para transmitir alertas importantes.',
   'Priorizar apenas a harmonia estética e manter o contraste atual.',
   'Reavaliar contraste, legibilidade e hierarquia tipográfica sem ignorar a harmonia visual.',
   'Reduzir ainda mais o tamanho das letras para mostrar mais informações.',
   2,
   'Incorreto: usar apenas cor viola a acessibilidade para pessoas daltônicas.',
   'Incorreto: a estética nunca deve sacrificar a legibilidade e a função básica de transmitir informações críticas.',
   'Correto: o design de interface deve equilibrar apelo estético com usabilidade e acessibilidade, ajustando taxas mínimas de contraste (WCAG) e tamanhos adequados de fonte para garantir legibilidade imediata.',
   'Incorreto: diminuir as letras agravaria severamente a barreira de leitura.',
   'Um cardápio com letras cinza-claras minúsculas num papel cinza-escuro à meia-luz pode até parecer sofisticado para o fotógrafo, mas vira um pesadelo para o cliente que só quer conseguir ler o que vai comer.',
   'A diretriz WCAG 2.1 exige contraste mínimo de 4.5:1 para texto normal e 3:1 para texto grande, garantindo que o prazer estético não destrua a legibilidade.'),

  # Questão 13
  (13, '12. Modelagem de usuário - perfil, persona e mapa de empatia.md',
   'Personas e modelagem de usuários baseada em dados reais', 'medio',
   'Uma equipe cria um aplicativo de estudo para públicos com diferentes rotinas. Antes de desenhar telas, reúne dados sobre objetivos, dificuldades e hábitos dos estudantes para representar grupos típicos de uso.\n\nQual artefato ajuda a sintetizar essas características em uma representação de usuário para orientar decisões?',
   'Um registro de commits do código-fonte.',
   'Uma tabela apenas com requisitos de hardware.',
   'Uma persona construída com base nos dados levantados.',
   'Um diagrama de implantação de servidores.',
   2,
   'Incorreto: histórico de commits documenta alterações de código, não necessidades humanas.',
   'Incorreto: requisitos de hardware descrevem máquinas, não motivações e dores de estudantes.',
   'Correto: a Persona (conceito criado por Alan Cooper) é um arquétipo hipotético de usuário construído rigorosamente a partir de dados reais de pesquisa, sintetizando motivações, frustrações e padrões de comportamento para guiar o design.',
   'Incorreto: diagramas de implantação modelam topologia de rede e servidores.',
   'A Persona funciona como um retrato falado humanizado do seu público: em vez de a equipe debater "o que os usuários abstratos querem", eles olham para a "Beatriz, estudante trabalhadora que só estuda no ônibus à noite" e projetam exatamente para a realidade dela.',
   'No Eixo 2, a especificação do projeto exigiu justamente 5 personas detalhadas para evitar decisões baseadas em achismos dos desenvolvedores.'),

  # Questão 14
  (14, '18. Princípios e regras de design - psicologia da gestalt e regras de ouro.md',
   'Princípios da Gestalt: Lei da Proximidade e organização visual', 'dificil',
   'Em um checkout de comércio eletrônico, os campos de endereço estão visualmente misturados com informações de pagamento. Em testes iniciais, usuários relatam dificuldade para reconhecer a quais etapas cada campo pertence.\n\nQual decisão aplica adequadamente o princípio perceptivo de proximidade para melhorar a organização da tela?',
   'Substituir os nomes dos campos por códigos numéricos.',
   'Aproximar visualmente os campos do título "Endereço de entrega" e separá-los dos outros grupos.',
   'Manter o agrupamento, mas reduzir o contraste dos rótulos.',
   'Aumentar a quantidade de campos sem alterar o espaçamento.',
   1,
   'Incorreto: códigos numéricos prejudicam a comunicabilidade e a compreensão.',
   'Correto: a Lei da Proximidade da Gestalt estabelece que elementos visualmente próximos entre si são percebidos pelo cérebro como pertencentes ao mesmo grupo funcional; afastar os blocos de endereço e pagamento e aproximar os campos de seus respectivos títulos organiza a hierarquia visual instantaneamente.',
   'Incorreto: reduzir contraste agrava a confusão perceptiva.',
   'Incorreto: manter o espaçamento uniforme impede o cérebro de reconhecer a separação de grupos.',
   'Se você espalha canetas e garfos misturados numa mesa na mesma distância, o cérebro vê uma bagunça; mas se você junta todas as canetas num copo e todos os garfos numa gaveta (**proximidade**), qualquer pessoa reconhece os grupos em um décimo de segundo.',
   'As leis da Gestalt (Proximidade, Similaridade, Fechamento, Continuidade e Figura-Fundo) formam a gramática da percepção visual em interfaces gráficas.'),

  # Questão 15
  (15, '19. Avaliação de sistemas interativos - por que, quando e quem participa.md',
   'Momentos da avaliação: avaliação formativa vs. avaliação somativa', 'facil',
   'Uma equipe prepara um aplicativo de biblioteca e deseja identificar falhas de navegação enquanto o protótipo ainda pode ser modificado. Há previsão de outra avaliação após a entrega para examinar o resultado final.\n\nComo se caracteriza a avaliação realizada durante a evolução do protótipo?',
   'Formativa, pois busca aperfeiçoar a solução durante seu desenvolvimento.',
   'Exclusivamente financeira, pois não envolve interação.',
   'De manutenção corretiva obrigatoriamente posterior à entrega.',
   'Somativa, pois somente mede o produto concluído.',
   0,
   'Correto: a avaliação **formativa** ocorre durante todo o processo de concepção e prototipagem com o objetivo de diagnosticar problemas e aperfeiçoar o design iterativamente; a avaliação **somativa** ocorre ao final para medir o nível de sucesso do produto consolidado.',
   'Incorreto: o objetivo da avaliação em IHC é aprimorar a usabilidade e a experiência de uso.',
   'Incorreto: manutenção corretiva é fase de operação pós-deploy.',
   'Incorreto: a avaliação somativa avalia o sistema concluído e entregue.',
   'A avaliação formativa é o chef provando o molho da panela enquanto cozinha para ajustar o sal; a avaliação somativa é a nota que o crítico de gastronomia dá para o prato quando ele já foi servido no salão.',
   'Conduzir avaliações formativas em fases preliminares evita lançar produtos com falhas estruturais difíceis de consertar.'),

  # Questão 16
  (16, '22. Avaliação da acessibilidade - diretrizes da wcag e conformidade em sistemas interativos.md',
   'Princípios de acessibilidade da WCAG: Perceptível e Operável', 'dificil',
   'Uma plataforma de aulas oferece explicações importantes somente em vídeos sem legendas e solicita ações que exigem exclusivamente o uso do mouse. A equipe pretende avaliar o produto segundo os princípios de acessibilidade apresentados no curso.\n\nQual diagnóstico e encaminhamento são mais adequados?',
   'A plataforma é acessível porque todos os vídeos podem ser reproduzidos.',
   'O problema é apenas estético; basta trocar a paleta de cores.',
   'Legendas relacionam-se à percepção do conteúdo; alternativas ao mouse favorecem a operação da interface.',
   'Acessibilidade só deve ser avaliada após os testes de segurança.',
   2,
   'Incorreto: reproduzir vídeo sem legendas exclui usuários com deficiência auditiva, violando a acessibilidade.',
   'Incorreto: a ausência de legendas e a barreira de teclado são falhas funcionais e ergonômicas graves.',
   'Correto: a WCAG estrutura-se em quatro princípios fundamentais: **Perceptível** (informações e componentes devem ser apresentados de modo que os usuários consigam percebê-los — ex.: legendas para conteúdo em áudio) e **Operável** (a interface deve permitir interação por teclado para quem não usa mouse).',
   'Incorreto: a acessibilidade deve ser pensada desde as primeiras etapas do design e do código.',
   'Se você só transmite o som sem legenda, quem não ouve fica cego para a aula (**falha de Percepção**); se você só deixa clicar com mouse, quem tem limitação motora ou usa leitor de tela fica de mãos atadas (**falha de Operação**). A acessibilidade abre as duas portas.',
   'Os 4 princípios POUR da WCAG são: Perceptível (*Perceivable*), Operável (*Operable*), Compreensível (*Understandable*) e Robusto (*Robust*).'),

  # Questão 17
  (17, '20. Avaliação por inspeção - avaliação heurística e percurso cognitivo.md',
   'Métodos de inspeção por especialistas: Avaliação Heurística e Percurso Cognitivo', 'dificil',
   'Uma equipe de um sistema de saúde deseja antecipar dificuldades na sequência de tarefas de agendamento antes de envolver pacientes em testes. Profissionais experientes precisam examinar a interface tanto à luz de diretrizes gerais de usabilidade quanto das ações necessárias para atingir cada objetivo.\n\nQue combinação de métodos de inspeção atende melhor a essas duas necessidades?',
   'Inspeção semiótica e questionário SUS.',
   'Grupo focal e teste A/B em produção.',
   'Teste de usabilidade e entrevista estruturada.',
   'Avaliação heurística e percurso cognitivo.',
   3,
   'Incorreto: o SUS é aplicado a usuários finais por questionário, não sendo método de inspeção analítica.',
   'Incorreto: grupo focal e teste A/B envolvem usuários e operação, não inspeção prévia de especialistas.',
   'Incorreto: teste de usabilidade exige observação direta de usuários reais.',
   'Correto: a **Avaliação Heurística** (inspeção contra princípios gerais consolidados, como as 10 heurísticas de Nielsen) combinada com o **Percurso Cognitivo** (*Cognitive Walkthrough*, que avalia passo a passo se o usuário saberá o que fazer e se reconhecerá o progresso em cada ação) é a dobradinha clássica de inspeção por especialistas.',
   'A Avaliação Heurística é como o fiscal sanitário conferindo o checklist geral da cozinha (lixo fechado, geladeira na temperatura certa); o Percurso Cognitivo é o fiscal tentando cozinhar uma receita do manual passo a passo para ver se o cozinheiro se perde em alguma instrução.',
   'Métodos de inspeção não envolvem usuários diretamente, sendo mais rápidos e econômicos para filtrar problemas antes dos testes empíricos.'),

  # Questão 18
  (18, '21. Avaliação da comunicabilidade - método de inspeção semiótica mis e método de avaliação da comunicabilidade mac.md',
   'Método de Inspeção Semiótica (MIS) vs. Avaliação da Comunicabilidade (MAC)', 'medio',
   'Ao revisar um portal, uma especialista examina rótulos, mensagens, telas e instruções para descobrir que visão sobre o usuário e sobre o uso o projetista comunica por meio da interface. Não há observação de usuários em execução nessa etapa.\n\nQual método se aproxima dessa atividade?',
   'Análise de complexidade algorítmica do código.',
   'Teste de carga de servidor, centrado em desempenho.',
   'Método de Avaliação da Comunicabilidade, que exige observar as rupturas na interação real nesse procedimento.',
   'Método de Inspeção Semiótica, centrado na metacomunicação presente nos signos.',
   3,
   'Incorreto: complexidade algorítmica avalia tempo/espaço assintótico (Big-O), não signos de interface.',
   'Incorreto: teste de carga mede concorrência e estresse de infraestrutura.',
   'Incorreto: o MAC (Método de Avaliação da Comunicabilidade) exige expressamente gravar e observar usuários reais executando tarefas para categorizar rupturas comunicativas.',
   'Correto: o **MIS (Método de Inspeção Semiótica)** é um método de inspeção analítica conduzido exclusivamente por avaliadores especialistas, que desconstroem os signos da interface para reconstruir a metamensagem enviada pelo designer ao usuário.',
   'No **MIS**, o especialista lê a interface como um crítico literário lê um romance sozinho na biblioteca, interpretando cada palavra e metáfora que o autor colocou no livro; já no **MAC**, o crítico senta na sala de aula e assiste aos alunos lendo o romance em voz alta para anotar onde eles tropeçam.',
   'Clarisse de Souza formulou tanto o MIS (método de inspeção analítica) quanto o MAC (método de observação empírica com usuários).'),

  # Questão 19
  (19, '24. Avaliação por investigação - método system usability scale sus.md',
   'Avaliação por investigação com a escala SUS (System Usability Scale)', 'medio',
   'Após disponibilizar um protótipo, uma equipe pede que participantes respondam a afirmações padronizadas sobre a facilidade de utilização e suas percepções gerais do sistema. O objetivo é obter uma medida estruturada de usabilidade percebida.\n\nQue técnica discutida no material atende mais diretamente a esse objetivo?',
   'Percurso cognitivo executado apenas por especialistas.',
   'System Usability Scale (SUS), aplicado por questionário aos participantes.',
   'Teste unitário automatizado do software.',
   'Avaliação heurística sem consulta aos usuários.',
   1,
   'Incorreto: o percurso cognitivo é conduzido por especialistas simulando tarefas, sem aplicar questionários psicométricos a usuários.',
   'Correto: o **SUS (System Usability Scale)**, criado por John Brooke em 1986, é uma escala psicométrica composta por 10 afirmações alternadas (escala Likert de 1 a 5) que gera uma pontuação final de 0 a 100 de usabilidade percebida.',
   'Incorreto: testes unitários verificam funções de código em C#, sem relação com percepção humana.',
   'Incorreto: avaliação heurística é método de inspeção pura sem aplicação de questionários ao usuário final.',
   'O SUS é como aquela pesquisa de satisfação padronizada no final do voo: em 10 perguntas rápidas com notas de 1 a 5, a companhia aérea descobre um número objetivo de 0 a 100 sobre o conforto da viagem na visão dos passageiros.',
   'Uma pontuação SUS acima de 68 é considerada dentro da média aceitável de mercado, enquanto pontuações acima de 80 refletem excelente usabilidade percebida.'),

  # Questão 20
  (20, '23. Teste de usabilidade - método empírico formal de avaliação por observação.md',
   'Teste de usabilidade: método empírico por observação de tarefas', 'medio',
   'Um time observa estudantes realizando três tarefas no sistema acadêmico: solicitar documento, consultar presença e localizar o calendário. Durante a sessão são anotados erros, tentativas malsucedidas e dificuldades, sem orientar os participantes durante a execução.\n\nQue evidência caracteriza o método de avaliação empregado?',
   'Inspeção de código-fonte com revisão por pares.',
   'Questionário de preferência aplicado sem execução de tarefas.',
   'Teste exclusivamente de integração entre serviços de dados.',
   'Teste de usabilidade por observação da execução de tarefas por usuários.',
   3,
   'Incorreto: revisão por pares inspeciona código C#/SQL, não a conduta de usuários.',
   'Incorreto: a equipe observou a execução concreta de tarefas em tempo real, não apenas opiniões frias em questionários.',
   'Incorreto: testes de integração validam comunicação entre APIs e bancos de dados.',
   'Correto: o **Teste de Usabilidade** é o método empírico por excelência de observação direta, onde usuários representativos realizam tarefas pré-definidas em ambiente controlado enquanto avaliadores coletam métricas de eficácia, eficiência e satisfação sem interferir na ação.',
   'O Teste de Usabilidade é como a prova prática de direção no Detran: o avaliador senta no banco do carona com uma prancheta calado, enquanto o candidato dirige pelas ruas cumprindo tarefas reais (dar baliza, estacionar, fazer curva). O avaliador anota cada dificuldade sem guiar o volante por ele.',
   'O teste de usabilidade gera dados tanto quantitativos (tempo de tarefa, taxa de conclusão, número de erros) quanto qualitativos (comentários em *Think Aloud* e expressões de frustração).')
]

for item in raw:
    add_q(*item)

print(f"Generated {len(puc_questions)} official PUC revision questions for Design de Interação.")

# Load existing DI file
di_path = os.path.join('/home/antigravity/leorruas/puc/banco-de-questoes', '08.design-de-interacao.json')
with open(di_path, 'r', encoding='utf-8') as f:
    existing_di = json.load(f)

print(f"Existing DI questions: {len(existing_di)}")

for eq in existing_di:
    if 'prioritaria' not in eq:
        eq['prioritaria'] = False
    if 'origem' not in eq:
        eq['origem'] = 'banco_sintetico_vault'

existing_ids = {q['id'] for q in existing_di}
new_to_add = [q for q in puc_questions if q['id'] not in existing_ids]

merged_di = puc_questions + [q for q in existing_di if not q['id'].startswith('DI-REV-')]

with open(di_path, 'w', encoding='utf-8') as f:
    json.dump(merged_di, f, ensure_ascii=False, indent=2)

print(f"Total questions in {di_path} after prepend: {len(merged_di)}")
