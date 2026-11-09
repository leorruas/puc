import json
import os

base_ref = '09. Redes de Computadores/'
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
        'id': f'RED-REV-{id_num:03d}',
        'disciplina_id': '09',
        'disciplina': 'Redes de Computadores',
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
  (1, '01. Terminologia e fundamentos de redes de computadores.md',
   'Protocolo, nó, enlace e comunicação', 'facil',
   'Uma empresa integra dispositivos de fabricantes diferentes. Todos precisam interpretar mensagens e responder conforme regras comuns. Qual conceito descreve o conjunto de regras que possibilita essa comunicação?',
   'Largura de banda do enlace.',
   'Protocolo de comunicação.',
   'Topologia física da rede.',
   'Quantidade de nós conectados.',
   1,
   'Incorreto: largura de banda é a capacidade de transmissão do canal, não as regras semânticas de diálogo.',
   'Correto: um protocolo de comunicação é a convenção formal que define o formato, a ordem das mensagens trocadas e o significado das ações disparadas entre entidades comunicantes.',
   'Incorreto: topologia física é a disposição geométrica dos cabos e equipamentos.',
   'Incorreto: a quantidade de nós indica o porte da rede, não a linguagem ou regras de interação.',
   'Pense em duas pessoas de países diferentes conversando: elas só conseguem se entender se concordarem em falar o mesmo idioma (por exemplo, inglês) e seguirem regras de etiqueta da conversa. O protocolo é esse idioma padronizado.',
   'Kurose e Ross definem protocolo como a especificação formal que rege o formato e a sequência temporal das mensagens enviadas e recebidas entre entidades de rede, viabilizando a interoperabilidade entre sistemas heterogêneos.'),

  # Questao 02
  (2, '01. Terminologia e fundamentos de redes de computadores.md',
   'Modalidades de transmissão (unicast, multicast e broadcast)', 'medio',
   'Em uma rede local, um sistema precisa enviar o mesmo aviso a todos os dispositivos do segmento, e não apenas a um destinatário ou a um grupo previamente definido. Qual modalidade de comunicação corresponde a essa necessidade?',
   'Multicast.',
   'Broadcast.',
   'Unicast.',
   'Comunicação ponto a ponto restrita.',
   1,
   'Incorreto: multicast direciona a mensagem a um grupo seletivo de assinantes cadastrados, não a todos indiscriminadamente.',
   'Correto: o broadcast (difusão ampla) envia um único pacote que é replicado e processado por todos os nós presentes no domínio de difusão da rede local.',
   'Incorreto: unicast é a transmissão ponto a ponto direcionada a uma única máquina de destino.',
   'Incorreto: conexão ponto a ponto restringe o tráfego estritamente aos dois extremos do enlace físico.',
   'Pense no sistema de som de um aeroporto: quando anunciam a chamada no alto-falante, todas as pessoas no saguão ouvem ao mesmo tempo (broadcast). Falar no ouvido de uma pessoa é unicast; reunir apenas os passageiros de um voo específico é multicast.',
   'No padrão Ethernet e IPv4, o broadcast atinge o endereço de destino reservado (como `255.255.255.255` ou `FF:FF:FF:FF:FF:FF`), forçando todos os adaptadores de rede do domínio a receberem e analisarem o quadro.'),

  # Questao 03
  (3, '02. Tipos de redes de computadores por abrangência geográfica.md',
   'Classificação geográfica de redes (PAN, LAN, MAN, WAN)', 'facil',
   'Uma organização possui escritórios em cidades diferentes e precisa interligar suas redes locais por conexões de longa distância. Qual classificação corresponde à rede que cobre essa abrangência?',
   'WAN.',
   'PAN.',
   'WLAN.',
   'LAN.',
   0,
   'Correto: a WAN (*Wide Area Network*, rede de longa distância) conecta cidades, estados ou países distintos através de infraestrutura pública ou enlaces de telecomunicações de longa distância.',
   'Incorreto: PAN (*Personal Area Network*) abrange o espaço pessoal de um indivíduo em torno de poucos metros (ex.: Bluetooth).',
   'Incorreto: WLAN (*Wireless Local Area Network*) é uma rede local sem fio limitada a um edifício ou escritório.',
   'Incorreto: LAN (*Local Area Network*) restringe-se a uma área geográfica contígua como uma sala, andar ou prédio corporativo.',
   'Pense nas estradas: uma LAN é a garagem e o quintal da sua casa; uma MAN é a avenida municipal da sua cidade; e uma WAN é o sistema de rodovias federais que conecta diferentes capitais pelo país.',
   'As WANs utilizam provedores de telecomunicações (*carriers*), enlaces de fibra submarina, satélites e roteadores de borda para interligar redes geograficamente dispersas.'),

  # Questao 04
  (4, '03. Topologias de redes de computadores.md',
   'Topologia física vs. lógica e comportamento de hubs', 'medio',
   'Um laboratório liga os computadores a um hub central. Visualmente, os cabos formam uma estrela; porém, o hub repete os sinais recebidos para todas as suas portas. Qual interpretação é adequada?',
   'A presença do hub transforma a rede em uma WAN.',
   'A topologia física é estrela, mas a propagação lembra um barramento.',
   'A topologia física e a propagação são necessariamente em anel.',
   'A topologia física é malha, pois todos os computadores se conectam diretamente entre si.',
   1,
   'Incorreto: o hub é equipamento de rede local (LAN), sem relação com abrangência geográfica de WAN.',
   'Correto: o arranjo físico dos cabos converge para um nó central (física em estrela), mas o hub atua na camada 1 inundando o sinal eletricamente para todas as portas, funcionando logicamente como um meio compartilhado (barramento lógico).',
   'Incorreto: em topologia em anel cada nó passa o token ou sinal para o vizinho sequencialmente.',
   'Incorreto: topologia em malha exige cabos dedicados interligando diretamente os pares de nós sem passar por concentrador.',
   'Pense em várias pessoas em uma sala com cabos ligados a um megafone central: visualmente os cabos parecem raios de uma roda (estrela), mas quando qualquer um fala, o megafone grita para todos ouvirem e competirem pelo silêncio (barramento).',
   'O hub não examina endereços MAC nem comuta quadros; ele apenas repete os bits eletricamente, mantendo todos os hosts no mesmo domínio de colisão.'),

  # Questao 05
  (5, '04. Padronização de redes de computadores e organismos internacionais.md',
   'Padronização de redes, RFCs e IETF', 'medio',
   'Uma empresa pretende criar um equipamento de rede compatível com soluções de diferentes fabricantes. A equipe precisa consultar especificações públicas que descrevem padrões e protocolos utilizados na Internet. Qual caminho está de acordo com o material?',
   'Utilizar somente convenções internas da empresa.',
   'Consultar RFCs disponibilizadas no âmbito da IETF.',
   'Copiar o funcionamento de um produto sem consultar especificações.',
   'Substituir padrões por nomes comerciais dos equipamentos.',
   1,
   'Incorreto: convenções proprietárias internas impedem a interoperabilidade aberta com o mercado.',
   'Correto: as RFCs (*Request for Comments*), mantidas e publicadas sob a égide da IETF (*Internet Engineering Task Force*), são os documentos técnicos canônicos abertos que definem os protocolos da Internet.',
   'Incorreto: engenharia reversa empírica não garante conformidade com casos de borda e especificações normativas.',
   'Incorreto: nomes de produtos de marcas privadas não constituem especificações arquiteturais abertas.',
   'As RFCs são como os manuais internacionais de aviação da ICAO: qualquer construtora de aeronaves precisa seguir essas especificações públicas para que seus aviões possam pousar com segurança em qualquer aeroporto do mundo.',
   'A IETF organiza o desenvolvimento de padrões da pilha TCP/IP por meio de grupos de trabalho abertos, onde as propostas amadurecem como *Internet Drafts* antes de virarem padrões formais via RFC.'),

  # Questao 06
  (6, '05. Sinais na transmissão de dados, analógicos, digitais e parâmetros de onda.md',
   'Características fundamentais de sinais (frequência, período e amplitude)', 'medio',
   'Ao comparar duas ondas periódicas, um técnico verifica que a segunda completa mais ciclos em cada segundo do que a primeira. Sem alterar a unidade de tempo, qual grandeza necessariamente é maior na segunda onda?',
   'Frequência.',
   'Atraso de propagação.',
   'Período.',
   'Amplitude.',
   0,
   'Correto: a frequência mede precisamente o número de ciclos completos executados por uma onda em um intervalo de um segundo (unidade Hertz, Hz). Mais ciclos por segundo significam maior frequência.',
   'Incorreto: atraso de propagação depende da distância física do enlace e da velocidade de propagação do meio condutor.',
   'Incorreto: o período é o inverso da frequência (T = 1/f); portanto, uma frequência maior resulta em um período estritamente menor.',
   'Incorreto: amplitude mede a intensidade máxima de crista ou vale da onda, sem relação com a cadência temporal de oscilação.',
   'Pense no motor de dois carros: o motor que gira mais vezes a cada segundo está em uma rotação (frequência) mais alta, e o tempo que ele gasta para dar uma única volta (período) é menor.',
   'A relação fundamental $f = 1/T$ estabelece uma proporção estritamente inversa entre a frequência em Hertz e a duração temporal de um ciclo (período em segundos).'),

  # Questao 07
  (6, '06. Sinais compostos, análise de Fourier e largura de banda.md',
   'Domínios do tempo e da frequência', 'medio',
   'Uma equipe analisa um sinal senoidal em dois gráficos. No primeiro, o eixo horizontal mostra o tempo; no segundo, o eixo horizontal informa a frequência. Qual informação o segundo gráfico permite destacar diretamente?',
   'A frequência e a amplitude da componente senoidal.',
   'O endereço lógico de destino.',
   'A posição física do transmissor.',
   'A sequência de protocolos aplicada ao sinal.',
   0,
   'Correto: no gráfico do domínio da frequência (espectro de Fourier), o eixo horizontal plota a frequência e a altura da barra/pico representa diretamente a amplitude correspondente àquela componente espectral.',
   'Incorreto: endereços lógicos pertencem à camada de rede, não a representações físicas de sinal eletromagnético.',
   'Incorreto: coordenadas espaciais geográficas não são exibidas em gráficos de espectro de sinal.',
   'Incorreto: a pilha de protocolos de software não é mapeada no domínio espectral da frequência.',
   'O domínio do tempo é como ouvir uma orquestra inteira tocando junta ao longo dos minutos; o domínio da frequência é ver na partitura quais notas específicas (frequências) estão soando e o volume de cada instrumento (amplitude).',
   'Pela análise de Fourier, qualquer sinal periódico composto pode ser decomposto em uma soma de ondas senoidais simples, cada uma identificada por sua frequência e amplitude no gráfico espectral.'),

  # Questao 08
  (8, '06. Sinais compostos, análise de Fourier e largura de banda.md',
   'Faixa de frequência e cálculo de largura de banda', 'medio',
   'Na análise de um sinal composto, os componentes relevantes ocupam frequências de 2 kHz a 8 kHz. Considerando a diferença entre a maior e a menor frequência, qual é sua largura de banda?',
   '4 kHz.',
   '8 kHz.',
   '6 kHz.',
   '2 kHz.',
   2,
   'Incorreto: cálculo incorreto de subtração.',
   'Incorreto: 8 kHz é a frequência máxima isolada, não a largura da faixa.',
   'Correto: a largura de banda (B) de um sinal analógico é a extensão da faixa espectral calculada pela diferença direta entre a frequência mais alta e a mais baixa: $8\\text{ kHz} - 2\\text{ kHz} = 6\\text{ kHz}$.',
   'Incorreto: 2 kHz é a frequência mínima isolada.',
   'Pense na largura de uma ponte: se ela começa no quilômetro 2 da rodovia e termina no quilômetro 8, a extensão da ponte é de exatamente 6 quilômetros (8 - 2 = 6).',
   'A largura de banda ($B = f_{max} - f_{min}$) determina a capacidade do meio de transmitir os harmônicos fundamentais de um sinal composto sem distorção excessiva.'),

  # Questao 09
  (9, '07. Modulação digital, chaveamento e técnicas em quadratura.md',
   'Técnicas de modulação digital (FSK, ASK, PSK)', 'medio',
   'Um sistema transmite dados modificando a frequência de uma onda portadora enquanto mantém o princípio de codificar símbolos por variações de frequência. Qual técnica listada no material corresponde a essa operação?',
   'FSK.',
   'ASK.',
   'PSK.',
   'TDM.',
   0,
   'Correto: FSK (*Frequency Shift Keying*, chaveamento por desvio de frequência) altera a frequência da portadora senoidal para representar bits (ex.: uma frequência mais alta para bit 1 e mais baixa para bit 0).',
   'Incorreto: ASK (*Amplitude Shift Keying*) varia a amplitude da portadora, mantendo a frequência fixa.',
   'Incorreto: PSK (*Phase Shift Keying*) varia a fase da portadora senoidal.',
   'Incorreto: TDM (*Time Division Multiplexing*) é técnica de multiplexação temporal, não de modulação de onda portadora.',
   'Pense em uma buzina com dois tons: quando o motorista aperta um tom agudo rápido significa "sim" (bit 1) e quando toca um tom grave significa "não" (bit 0). Alterar o tom é mudar a frequência (FSK).',
   'A modulação por chaveamento digital permite converter sequências binárias de banda-base em sinais analógicos adequados para propagação através de canais passa-faixa.'),

  # Questao 10
  (10, '07. Modulação digital, chaveamento e técnicas em quadratura.md',
   'Modulação de amplitude em quadratura (QAM)', 'dificil',
   'Uma equipe avalia técnicas de modulação para representar símbolos por alterações nas características da portadora. Ela precisa identificar a técnica indicada no material como modulação de amplitude em quadratura. Qual é a opção correta?',
   'QAM.',
   'FSK.',
   'QPSK.',
   'WDM.',
   0,
   'Correto: a QAM (*Quadrature Amplitude Modulation*, modulação de amplitude em quadratura) combina variações simultâneas de amplitude e de fase de duas portadoras defasadas em 90 graus (em quadratura), aumentando a densidade de bits por símbolo.',
   'Incorreto: FSK varia exclusivamente a frequência da portadora.',
   'Incorreto: QPSK varia apenas a fase da portadora em quatro ângulos possíveis, sem combinar modulação multinível de amplitude.',
   'Incorreto: WDM é multiplexação por divisão de comprimento de onda em fibras ópticas.',
   'Em vez de enviar sinais apenas acendendo a lâmpada mais forte ou mais fraca (amplitude) ou mudando a cor da luz (fase), a QAM combina os dois ajustes ao mesmo tempo, criando uma matriz de dezenas de símbolos diferentes para transmitir vários bits de uma só vez.',
   'A QAM (como 16-QAM, 64-QAM ou 256-QAM) é amplamente utilizada em redes Wi-Fi, modems de cabo e redes 4G/5G pela sua altíssima eficiência espectral.'),

  # Questao 11
  (11, '08. Multiplexação em redes, compartilhamento de enlaces por FDM, WDM e TDM.md',
   'Multiplexação e demultiplexação de sinais', 'facil',
   'Uma operadora reúne dados de várias fontes em um único enlace compartilhado e, na outra extremidade, precisa separá-los para seus respectivos destinos. Que processo descrito no material atende a essa necessidade?',
   'Multiplexação e posterior demultiplexação.',
   'Substituição dos dados por endereços IP.',
   'Criação de uma topologia em anel.',
   'Roteamento entre redes.',
   0,
   'Correto: multiplexação (*multiplexing*) é o processo de combinar múltiplos fluxos de dados de canais independentes em um único meio físico compartilhado, enquanto a demultiplexação reconstrói os fluxos separados no receptor.',
   'Incorreto: alterar cabeçalhos de endereços IP não compartilha nem condensa sinais físicos em um enlace.',
   'Incorreto: topologia em anel é uma forma geométrica de enlace, não o mecanismo de compartilhamento físico de sinal.',
   'Incorreto: roteamento escolhe caminhos lógicos entre redes na camada 3, sem atuar na modulação e multiplexação de sinais físicos de enlace.',
   'Pense em uma rodovia de quatro pistas que entra em um túnel estreito de pista única e, ao sair do túnel, os carros se reorganizam novamente em suas pistas individuais de destino.',
   'Dispositivos multiplexadores (MUX) e demultiplexadores (DEMUX) maximizam a taxa de utilização da infraestrutura física de transmissão, reduzindo custos operacionais de cabeamento.'),

  # Questao 12
  (12, '08. Multiplexação em redes, compartilhamento de enlaces por FDM, WDM e TDM.md',
   'Multiplexação por divisão de comprimento de onda (WDM)', 'medio',
   'Uma rede óptica deve transmitir simultaneamente diferentes fluxos pelo mesmo meio, atribuindo a cada fluxo um comprimento de onda distinto. Qual técnica é a mais adequada entre as apresentadas no material?',
   'PSK.',
   'FDM.',
   'TDM.',
   'WDM.',
   3,
   'Incorreto: PSK é modulação digital por chaveamento de fase, não técnica de compartilhamento de canal óptico.',
   'Incorreto: FDM opera dividindo faixas de frequência em sinais elétricos ou de rádio convencionais.',
   'Incorreto: TDM divide o tempo em fatias temporais (*time slots*), não o comprimento de onda luminoso.',
   'Correto: WDM (*Wavelength Division Multiplexing*) é a técnica de multiplexação desenvolvida para fibras ópticas que transmite múltiplos feixes de luz simultâneos, cada um com seu próprio comprimento de onda (cor) pela mesma fibra.',
   'Pense em um prisma que junta feixes de luz de cores diferentes (vermelho, verde, azul) em um único feixe para atravessar um vidro óptico, e do outro lado um prisma inverso separa as cores de volta para os seus destinos.',
   'Variações de alta capacidade como o DWDM (*Dense WDM*) permitem transmitir dezenas ou centenas de canais a taxas de terabits por segundo em um único filamento de fibra óptica.'),

  # Questao 13
  (13, '09. Meios de transmissão guiados e não guiados.md',
   'Meios guiados e propagação por luz', 'facil',
   'No projeto de um enlace, a equipe precisa diferenciar o meio que transporta informação por fluxo luminoso daquele que utiliza sinais elétricos. Qual alternativa identifica corretamente o meio guiado que utiliza luz?',
   'Fibra óptica.',
   'Par trançado UTP.',
   'Par trançado STP.',
   'Cabo de cobre convencional.',
   0,
   'Correto: a fibra óptica é um meio guiado composto por núcleo de vidro ou polímero que transporta pulsos luminosos através do princípio da reflexão interna total.',
   'Incorreto: par trançado UTP utiliza pulsos elétricos de voltagem através de fios de cobre sem blindagem.',
   'Incorreto: par trançado STP é condutor elétrico metálico de cobre com blindagem.',
   'Incorreto: cabos de cobre convencionais operam por corrente elétrica e elétrons livres, não fótons de luz.',
   'Enquanto os cabos de cobre funcionam como fios elétricos que conduzem eletricidade para acender uma lâmpada, a fibra óptica é um canudo de vidro espelhado por onde feixes de laser viajam refletindo nas paredes.',
   'A transmissão por luz na fibra óptica oferece imunidade total a interferências eletromagnéticas (EMI/RFI), atenuação significativamente menor e largura de banda na escala de gigabits ou terabits por segundo.'),

  # Questao 14
  (14, '09. Meios de transmissão guiados e não guiados.md',
   'Meios guiados vs. não guiados, mobilidade e interferência', 'medio',
   'Uma instituição precisa conectar dispositivos móveis sem cabos, sabendo que a transmissão ficará sujeita às condições de propagação do ambiente. Que opção corresponde à escolha e à limitação descritas no material?',
   'Meio não guiado, pois favorece mobilidade e exige atenção a interferências.',
   'Meio guiado, pois dispensa a instalação física de cabos.',
   'Fibra óptica, pois permite mobilidade sem meio físico.',
   'Par trançado, pois transmite os dados exclusivamente por luz.',
   0,
   'Correto: meios não guiados (como ondas de rádio, micro-ondas e infravermelho) propagam ondas pelo espaço livre sem limites físicos rígidos, viabilizando a mobilidade à custa de maior suscetibilidade a atenuação, ruídos e interferências.',
   'Incorreto: meios guiados exigem condutores físicos (cabos de cobre ou filamentos de fibra óptica).',
   'Incorreto: fibra óptica é um meio físico guiado de vidro/plástico, exigindo cabeamento fixo.',
   'Incorreto: par trançado transmite sinais elétricos por cobre metálico, não luz.',
   'É a diferença entre falar com alguém pelo interfone com fio da portaria (meio guiado, sem ruídos externos mas preso na parede) versus falar por um walkie-talkie andando na rua (não guiado, alta mobilidade mas sujeito a chiados e prédios bloqueando o sinal).',
   'As redes sem fio (IEEE 802.11 Wi-Fi, redes móveis celulares) são meios não guiados cujo sinal sofre reflexão, difração, espalhamento e absorção por obstáculos físicos no ambiente.'),

  # Questao 15
  (15, '10. Introdução ao modelo de referência OSI e arquitetura em camadas.md',
   'Sete camadas do modelo OSI e prestação de serviços', 'medio',
   'Uma empresa documenta funções de comunicação de rede para separar responsabilidades e facilitar a interoperabilidade entre componentes. Segundo o modelo OSI apresentado no material, qual afirmação expressa essa organização?',
   'O modelo tem sete camadas, e cada uma oferece serviços à camada superior.',
   'Todas as funções de comunicação são executadas exclusivamente pela aplicação.',
   'O modelo possui apenas as camadas aplicação, transporte e internet.',
   'As camadas são definidas conforme a localização geográfica dos computadores.',
   0,
   'Correto: o modelo de referência OSI da ISO organiza a pilha em exatamente sete camadas conceituais, onde cada camada `N` encapsula suas operações internas e disponibiliza serviços padronizados à camada imediatamente superior `N+1`.',
   'Incorreto: a essência da arquitetura em camadas é a distribuição modular de papéis (enlace, rede, transporte, etc.), e não centralizar tudo no aplicativo.',
   'Incorreto: modelo de 3 ou 4 camadas descreve variações da pilha TCP/IP prática, enquanto o OSI padroniza sete camadas.',
   'Incorreto: a divisão em camadas é funcional e de protocolo lógico, sem qualquer relação com a distância geográfica dos hosts.',
   'Pense em uma empresa com cargos bem definidos: o operário monta a peça, entrega ao inspetor de qualidade, que entrega ao empacotador, que entrega ao despachante. Cada pessoa executa seu trabalho e passa o pacote pronto para o colega do nível acima.',
   'As sete camadas do modelo OSI são: 1-Física, 2-Enlace, 3-Rede, 4-Transporte, 5-Sessão, 6-Apresentação e 7-Aplicação (mnemônico clássico: FERTSAA).'),

  # Questao 16
  (16, '11. Camadas física e de enlace do modelo OSI.md',
   'Camada física, repetidores e hubs', 'medio',
   'Ao identificar equipamentos de uma rede, um estudante classifica cabos, conectores, repetidores e hubs como dispositivos associados à transmissão de sinais. A qual camada OSI essa classificação corresponde?',
   'Enlace.',
   'Rede.',
   'Física.',
   'Transporte.',
   2,
   'Incorreto: camada de enlace trabalha com quadros (*frames*), controle de acesso ao meio (MAC) e switches.',
   'Incorreto: camada de rede lida com pacotes, endereçamento IP e roteadores.',
   'Correto: a camada física (camada 1 do OSI) trata da transmissão de bits brutos pelo canal físico, especificando padrões elétricos, mecânicos, conectores (como RJ-45), cabos, repetidores e hubs.',
   'Incorreto: camada de transporte coordena comunicação fim a fim entre processos usando portas.',
   'Pense na fiação elétrica e nas tomadas da sua casa: se você plugar um benjamim (hub elétrico) ou um cabo de extensão, você está apenas estendendo a eletricidade física, sem entender o que os eletrodomésticos estão dizendo.',
   'Dispositivos de camada física não têm capacidade de ler endereços lógicos ou físicos nem inspecionar cabeçalhos de dados; limitam-se a amplificar, regenerar ou replicar sinais elétricos/ópticos.'),

  # Questao 17
  (17, '11. Camadas física e de enlace do modelo OSI.md',
   'Camada de enlace e encapsulamento em quadros (frames)', 'medio',
   'Dois equipamentos diretamente conectados por um enlace precisam organizar os bytes transmitidos em unidades próprias dessa camada, conhecidas como frames. Qual camada OSI realiza essa função?',
   'Enlace.',
   'Aplicação.',
   'Sessão.',
   'Transporte.',
   0,
   'Correto: a camada de enlace de dados (camada 2 do OSI) empacota o fluxo contínuo de bits em unidades lógicas denominadas quadros (*frames*), controlando o envio confiável nó a nó, delimitação de início/fim e endereçamento físico (MAC).',
   'Incorreto: camada de aplicação trata de protocolos de usuário como HTTP, DNS e SMTP.',
   'Incorreto: camada de sessão gerencia diálogos e sincronização entre aplicações.',
   'Incorreto: camada de transporte encapsula dados em segmentos ou datagramas, controlando fluxos fim a fim.',
   'Se a camada física é como uma esteira transportando areia de forma contínua, a camada de enlace coloca essa areia dentro de caixas padronizadas com etiquetas de remetente e destinatário físico (quadros).',
   'A camada de enlace subdivide-se historicamente no padrão IEEE 802 em subcamada LLC (*Logical Link Control*) e subcamada MAC (*Media Access Control*).'),

  # Questao 18
  (18, '12. Camadas de rede e transporte do modelo OSI.md',
   'Funções de rede (roteamento) e transporte (comunicação fim a fim)', 'medio',
   'Uma mensagem precisa atravessar várias redes até chegar ao destino. Além de escolher encaminhamentos entre redes, a arquitetura também precisa fornecer comunicação fim a fim entre os sistemas participantes. Qual associação de camadas é correta?',
   'Física para roteamento; enlace para comunicação entre aplicações.',
   'Aplicação para escolha de cada enlace físico; rede para codificação da onda.',
   'Rede para roteamento; transporte para comunicação fim a fim.',
   'Sessão para encaminhamento IP; apresentação para portas de transporte.',
   2,
   'Incorreto: física lida com bits e sinais, e enlace atua estritamente nó a nó dentro da mesma rede local.',
   'Incorreto: aplicação não gerencia enlaces de rede e rede não codifica ondas analógicas.',
   'Correto: a camada de rede é responsável pelo endereçamento lógico e roteamento de pacotes através de múltiplas redes intermediárias; a camada de transporte fornece o canal lógico de comunicação processo a processo fim a fim.',
   'Incorreto: encaminhamento de pacotes é atribuição de rede, e portas pertencem ao nível de transporte.',
   'A camada de rede é o serviço de triagem dos Correios que decide por quais rodovias o caminhão vai passar para cruzar o país (roteamento); a camada de transporte é você ligando para o seu amigo para confirmar se todos os itens da encomenda chegaram intactos na casa dele (fim a fim).',
   'Enquanto os nós intermediários da rede (roteadores) executam protocolos até a camada 3, a camada de transporte opera exclusivamente nos sistemas finais (*hosts* nas bordas), concretizando o princípio fim-a-fim da arquitetura.'),

  # Questao 19
  (19, '13. Camadas de sessão, apresentação e aplicação do modelo OSI.md',
   'Camada de sessão, pontos de sincronização e controle de diálogo', 'medio',
   'Durante uma longa transferência, a conexão sofre uma interrupção. O projeto prevê pontos de sincronização que ajudem a retomar o trabalho a partir de um ponto conhecido. Em qual camada OSI o material apresenta essa responsabilidade?',
   'Física.',
   'Sessão.',
   'Enlace.',
   'Rede.',
   1,
   'Incorreto: camada física transmite sinais elétricos/ópticos brutos sem memória de sessão.',
   'Correto: a camada de sessão (camada 5 do OSI) é responsável pelo estabelecimento, gerenciamento, controle de diálogo e inserção de pontos de verificação/sincronização (*checkpoints*) para retomar transmissões interrompidas.',
   'Incorreto: camada de enlace garante apenas a entrega de quadros em um enlace direto local.',
   'Incorreto: camada de rede trata do roteamento de pacotes individuais sem manter checkpoints de transferências longas.',
   'Pense no salvamento automático de um editor de texto na nuvem: se faltar energia após digitar 100 páginas, os pontos de sincronização da sessão permitem continuar da página 95, sem precisar redigir o documento inteiro do zero.',
   'No modelo OSI formal, a camada de sessão gerencia o controle de turno (simplex, half-duplex, full-duplex) e o restabelecimento coordenado do estado de diálogo entre duas entidades colaborativas.'),

  # Questao 20
  (20, '13. Camadas de sessão, apresentação e aplicação do modelo OSI.md',
   'Camada de apresentação e tradução de formatos de dados', 'medio',
   'Duas aplicações trocam dados, mas usam representações internas diferentes. Para que possam interpretar a informação transferida, é necessário tratar a representação dos dados durante a comunicação. Qual camada OSI é relacionada diretamente a essa função?',
   'Rede.',
   'Sessão.',
   'Apresentação.',
   'Transporte.',
   2,
   'Incorreto: camada de rede opera no encaminhamento de pacotes, indiferente à codificação de texto ou imagens.',
   'Incorreto: camada de sessão cuida do diálogo e sincronização, não da representação semântica dos bytes.',
   'Correto: a camada de apresentação (camada 6 do OSI) cuida da sintaxe e da semântica dos dados transferidos, realizando tradução de formatos (como ASCII/EBCDIC, big-endian/little-endian), compressão e criptografia.',
   'Incorreto: transporte garante entrega ordenada e controle de fluxo fim a fim, sem interpretar formatos internos dos dados.',
   'Pense em um intérprete e tradutor juramentado: um diplomata fala japonês e o outro fala português; o intérprete (camada de apresentação) converte as frases para que ambos compreendam o conteúdo sem precisarem mudar sua língua nativa.',
   'A camada de apresentação abstrai a arquitetura interna do hardware emissor e receptor, garantindo que os dados cheguem à camada de aplicação em formato compreensível.'),

  # Questao 21
  (21, '14. Introdução ao modelo TCP-IP e arquitetura da Internet.md',
   'Comutação por pacotes e resiliência com rotas dinâmicas', 'medio',
   'Uma rede precisa continuar operando quando um de seus enlaces deixa de funcionar. O projeto permite que pacotes sigam caminhos alternativos entre origem e destino, em vez de depender de um único circuito fixo. Qual princípio da arquitetura estudada corresponde a essa solução?',
   'Comutação por pacotes com possibilidade de rotas diferentes.',
   'Obrigatoriedade de uma rota única para todos os pacotes.',
   'Transmissão somente por circuito dedicado.',
   'Eliminação de endereços de rede em todos os equipamentos.',
   0,
   'Correto: a comutação por pacotes divide a informação em unidades independentes (datagramas), permitindo que cada pacote seja roteado dinamicamente por caminhos alternativos conforme a disponibilidade da malha, garantindo alta tolerância a falhas.',
   'Incorreto: forçar rota única inviabiliza a tolerância a falhas caso o caminho intermediário sofra interrupção.',
   'Incorreto: comutação por circuitos dedicados (típica da antiga rede telefônica fixa) exige caminho estático pré-alocado que derruba a chamada se o enlace romper.',
   'Incorreto: o endereçamento global de rede em cada host e roteador é indispensável para viabilizar o encaminhamento dos pacotes.',
   'Pense em uma frota de carros saindo da mesma fábrica rumo a uma cidade vizinha: se a rodovia principal fechar por causa de um acidente, cada motorista pode consultar o GPS e pegar desvios por estradas alternativas para chegar ao mesmo destino.',
   'Essa resiliência foi o requisito arquitetural fundante da ARPANET durante a Guerra Fria (Paul Baran e Donald Davies), dando origem ao protocolo IP sem conexão (*connectionless*).'),

  # Questao 22
  (22, '15. Camada de interface do modelo TCP-IP e análise com Wireshark.md',
   'Camada de interface de rede (Host-to-Network) no modelo de 4 camadas', 'medio',
   'Uma equipe compara o modelo OSI ao TCP/IP e encontra representações com números diferentes de camadas. Considerando expressamente a abordagem adotada no microfundamento, qual descrição da camada de interface é correta?',
   'Realiza exclusivamente o controle das portas TCP e UDP.',
   'Substitui exclusivamente a camada de aplicação do OSI.',
   'Equivale somente à camada de rede do OSI.',
   'Reúne funções correspondentes às camadas física e de enlace do OSI.',
   3,
   'Incorreto: portas TCP e UDP são funções pertencentes exclusivamente à camada de transporte.',
   'Incorreto: a camada de aplicação do modelo TCP/IP agrupa as camadas de aplicação, apresentação e sessão do OSI.',
   'Incorreto: a camada de rede do OSI equivale à camada de internet do modelo TCP/IP.',
   'Correto: no modelo original de 4 camadas do TCP/IP (RFC 1122), a camada mais baixa é denominada Interface com a Rede (*Host-to-Network* ou *Link Layer*), englobando tanto os aspectos físicos de transmissão quanto a estruturação em quadros e controle de acesso ao meio do OSI.',
   'Pense na placa de rede do seu computador: ela possui tanto a tomada metálica onde entra o cabo (física) quanto o chip controlador que monta os quadros Ethernet e confere o endereço MAC (enlace). O modelo TCP/IP consolidou tudo isso em uma única camada de interface.',
   'Essa abordagem pragmática da Internet permitiu que o protocolo IP operasse sobre qualquer tecnologia de enlace e física subjacente (Ethernet, Wi-Fi, fibra óptica, satélite) sem exigir reestruturação da pilha superior.'),

  # Questao 23
  (23, '16. Camada de internet do modelo TCP-IP, roteamento e protocolo ICMP.md',
   'Encaminhamento, roteamento entre redes e traceroute/tracert', 'medio',
   'Um administrador quer observar um dos possíveis percursos que os pacotes seguem de seu computador até um servidor remoto. Ele utiliza o comando tracert no Windows. Que função da camada internet é investigada por essa ferramenta?',
   'Controle de quadros em um único enlace.',
   'Criação de sessões entre aplicações.',
   'Encaminhamento e roteamento de pacotes entre redes.',
   'Codificação da amplitude da portadora.',
   2,
   'Incorreto: quadros pertencem à camada de enlace, atuando nó a nó no segmento local.',
   'Incorreto: sessões entre aplicações pertencem às camadas superiores de software.',
   'Correto: o comando `tracert` (ou `traceroute`) mapeia a sequência de saltos (*hops*) de roteadores intermediários que encaminham os pacotes IP através da camada de internet até o host de destino.',
   'Incorreto: modulação de amplitude da portadora é assunto de física e transmissão eletromagnética na camada 1.',
   'É como pedir a um viajante que anote o nome de cada pedágio e trevo rodoviário por onde ele passa ao cruzar o país de carro até a cidade final.',
   'O `tracert` funciona enviando pacotes com valores crescentes no campo TTL (*Time to Live*) do cabeçalho IP; ao atingirem zero, os roteadores descartam o pacote e retornam uma mensagem ICMP *Time Exceeded*, revelando seus endereços IP.'),

  # Questao 24
  (24, '17. Camada de transporte do modelo TCP-IP, portas e protocolos TCP e UDP.md',
   'Multiplexação de processos e portas de transporte TCP/UDP', 'dificil',
   'Em um computador, navegador, cliente de e-mail e outra aplicação usam simultaneamente a rede. Os pacotes chegam ao mesmo endereço IP, mas precisam ser direcionados aos processos corretos. Qual mecanismo cumpre esse papel no nível de transporte?',
   'Identificação por números de porta.',
   'Separação exclusiva por largura de banda óptica.',
   'Escolha das rotas pela camada de aplicação.',
   'Mudança da topologia física para anel.',
   0,
   'Correto: as portas lógicas da camada de transporte (números inteiros de 16 bits de 0 a 65535) atuam como identificadores de processos, permitindo a multiplexação e demultiplexação de tráfego para que cada mensagem chegue ao aplicativo correto na mesma máquina.',
   'Incorreto: divisão óptica de banda ocorre em enlaces físicos de fibra, não discernindo processos locais no sistema operacional.',
   'Incorreto: o roteamento é atribuição de camada de rede, não de processos de aplicação.',
   'Incorreto: topologia física em anel é disposição de cabeamento de rede local.',
   'Pense em um grande prédio comercial: o endereço IP é o CEP e número do prédio na rua; o número de porta é o número da sala comercial (ex.: sala 80 para a empresa web, sala 443 para a empresa segura, sala 25 para o correio).',
   'O par composto por Endereço IP + Número de Porta define um ponto terminal de comunicação (*endpoint* ou *socket*), viabilizando conexões simultâneas concorrentes no mesmo sistema operacional.'),

  # Questao 25
  (25, '18. Camada de aplicação do modelo TCP-IP, soquetes de Berkeley e inspeção HTTP.md',
   'API de sockets de Berkeley e abstração de transporte', 'dificil',
   'Uma equipe cria um aplicativo que trocará mensagens com outro sistema pela rede. Para não programar diretamente as funções de todas as camadas inferiores, decide usar uma interface de programação que abstrai a comunicação fim a fim. Qual recurso citado no material atende a essa necessidade?',
   'Representação de sinais exclusivamente no domínio do tempo.',
   'Protocolo de ligação física por repetidores.',
   'Topologia lógica de barramento implementada por hub.',
   'Interface de soquetes (sockets de Berkeley).',
   3,
   'Incorreto: gráficos no domínio do tempo exibem ondas analógicas de sinal elétrico.',
   'Incorreto: repetidores físicos apenas regeneram bits na camada 1.',
   'Incorreto: topologia em barramento é uma arquitetura de canal de rede local com colisões.',
   'Correto: a API de *sockets* de Berkeley (soquetes de rede) fornece uma interface de programação de alto nível padronizada que abstrai os detalhes operacionais das camadas inferiores (TCP/UDP e IP), permitindo que a aplicação leia e escreva dados na rede como se manipulasse arquivos.',
   'Pense na tomada de energia da parede: você apenas conecta o plugue do seu aparelho para consumir eletricidade, sem precisar projetar os geradores da usina hidrelétrica ou as subestações de alta tensão da cidade.',
   'Desenvolvida originalmente no BSD Unix, a interface de sockets (`socket()`, `bind()`, `listen()`, `accept()`, `connect()`, `send()`, `recv()`) consolidou-se como o padrão universal de programação de redes em praticamente todas as linguagens modernas.')
]

for idx, r in enumerate(raw):
    actual_id = idx + 1
    add_q(actual_id, r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12], r[13], r[14], r[15])

print(f"Geradas {len(puc_questions)} questoes de revisao oficial para Redes de Computadores.")

red_path = '/home/antigravity/leorruas/puc/banco-de-questoes/09.redes-de-computadores.json'
with open(red_path, 'r', encoding='utf-8') as f:
    existing_red = json.load(f)

clean_base = [q for q in existing_red if not q.get('id', '').startswith('RED-REV-')]
print(f"Questoes base preservadas: {len(clean_base)}")

for q in clean_base:
    if 'prioritaria' not in q:
        q['prioritaria'] = False
    if 'origem' not in q:
        q['origem'] = 'banco_sintetico_vault'

merged = puc_questions + clean_base

with open(red_path, 'w', encoding='utf-8') as f:
    json.dump(merged, f, ensure_ascii=False, indent=2)

print(f"Sucesso: {len(merged)} questoes salvas em {red_path}.")
