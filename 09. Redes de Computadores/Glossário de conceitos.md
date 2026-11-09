# Glossário de conceitos

Este glossário reúne a terminologia fundamental e os conceitos consolidados na disciplina de Redes de Computadores. Ele cresce junto com o estudo, registrando as definições precisas e distinções conceituais com links para as seções correspondentes.

## Elementos de rede e conectividade

| Conceito | Definição curta | Distinção ou observação | Onde aparece |
| --- | --- | --- | --- |
| **Nó (*Node*)** | Elemento ativo conectado à rede com capacidade de emitir, receber e processar dados. | Inclui computadores, servidores, switches e roteadores; não se limita a computadores pessoais. | [[09. Redes de Computadores/01. Terminologia e fundamentos de redes de computadores#Elementos constitutivos: nós, enlaces e endereçamento\|Artigo 01 — nós e enlaces]] |
| **Enlace (*Link*)** | Canal físico ou sem fio que conecta diretamente dois nós adjacentes. | Pode utilizar meios elétricos (cobre), ópticos (fibra) ou eletromagnéticos (Wi-Fi). | [[09. Redes de Computadores/01. Terminologia e fundamentos de redes de computadores#Elementos constitutivos: nós, enlaces e endereçamento\|Artigo 01 — nós e enlaces]] |
| **Endereço MAC** | Endereço físico gravado na placa de rede para identificação no enlace local. | É imutável e local; atua como o "DNA" do dispositivo no enlace de hardware. | [[09. Redes de Computadores/01. Terminologia e fundamentos de redes de computadores#Elementos constitutivos: nós, enlaces e endereçamento\|Artigo 01 — endereçamento]] |
| **Endereço IP** | Endereço lógico atribuído a uma interface de rede para fins de localização e roteamento global. | É hierárquico e modificável; atua como o "endereço postal" do nó na Internet. | [[09. Redes de Computadores/01. Terminologia e fundamentos de redes de computadores#Elementos constitutivos: nós, enlaces e endereçamento\|Artigo 01 — endereçamento]] |
| **Segmento de rede** | Porção delimitada de uma rede de computadores que compartilha o mesmo meio de comunicação. | A topologia do segmento pode ser em estrela, barramento ou anel. | [[09. Redes de Computadores/01. Terminologia e fundamentos de redes de computadores#Elementos constitutivos: nós, enlaces e endereçamento\|Artigo 01 — segmentos]] |

## Protocolos e encapsulamento

| Conceito | Definição curta | Distinção ou observação | Onde aparece |
| --- | --- | --- | --- |
| **Protocolo de rede** | Conjunto formal de regras, padrões e formatos que governa a comunicação entre nós. | Permite que sistemas heterogêneos (como Windows e Linux) troquem dados de forma compatível. | [[09. Redes de Computadores/01. Terminologia e fundamentos de redes de computadores#Protocolos, PDU e encapsulamento de dados\|Artigo 01 — protocolos]] |
| **PDU (Protocol Data Unit)** | Bloco estruturado de informações transmitido por um protocolo, composto por cabeçalho e carga útil. | Recebe nomes específicos por camada: quadro no enlace, pacote na rede e segmento/datagrama no transporte. | [[09. Redes de Computadores/01. Terminologia e fundamentos de redes de computadores#Unidade de dados de protocolo (PDU)\|Artigo 01 — PDU]] |
| **Quadro (*Frame*)** | Denominação da PDU na camada de enlace de dados. | Empacota os bits para tráfego físico no enlace, comparável ao "caminhão" que transporta a carga na rodovia. | [[09. Redes de Computadores/01. Terminologia e fundamentos de redes de computadores#Unidade de dados de protocolo (PDU)\|Artigo 01 — quadros]] |

## Modalidades de tráfego e desempenho

| Conceito | Definição curta | Distinção ou observação | Onde aparece |
| --- | --- | --- | --- |
| **Unicast** | Modo de transmissão ponto a ponto direcionado exclusivamente a um único nó destinatário. | Comunicação individual; contrasta com envio coletivo. | [[09. Redes de Computadores/01. Terminologia e fundamentos de redes de computadores#Modalidades de disseminação de tráfego\|Artigo 01 — modalidades de tráfego]] |
| **Multicast** | Modo de transmissão direcionado a um grupo específico de nós assinantes em uma rede. | Apenas membros do grupo processam a mensagem; mais eficiente que múltiplos envios unicast. | [[09. Redes de Computadores/01. Terminologia e fundamentos de redes de computadores#Modalidades de disseminação de tráfego\|Artigo 01 — modalidades de tráfego]] |
| **Broadcast** | Modo de transmissão difusa distribuída compulsoriamente a todos os nós do segmento de rede. | Utilizado para anúncios globais e descobertas de endereços; pode gerar tempestades de tráfego se abusado. | [[09. Redes de Computadores/01. Terminologia e fundamentos de redes de computadores#Modalidades de disseminação de tráfego\|Artigo 01 — modalidades de tráfego]] |
| **Vazão (*Throughput*)** | Quantidade real de bits transferida com sucesso por unidade de tempo (bps). | Difere da largura de banda teórica por refletir a capacidade útil sob condições reais de rede. | [[09. Redes de Computadores/01. Terminologia e fundamentos de redes de computadores#Métricas fundamentais de desempenho de rede\|Artigo 01 — métricas]] |
| **Atraso (*Delay* / Latência)** | Tempo decorrido para um pacote transitar da origem até a recepção completa no destino. | Soma atrasos de propagação, transmissão, processamento e enfileiramento em buffers. | [[09. Redes de Computadores/01. Terminologia e fundamentos de redes de computadores#Métricas fundamentais de desempenho de rede\|Artigo 01 — métricas]] |
| **Perda de pacotes (*Packet Loss*)** | Descarte ou extravio de pacotes durante a transmissão pela rede. | Provocado por ruídos e corrupção no meio físico ou por sobrecarga e estouro de buffer nos roteadores. | [[09. Redes de Computadores/01. Terminologia e fundamentos de redes de computadores#Métricas fundamentais de desempenho de rede\|Artigo 01 — métricas]] |

## Arquitetura e camadas

| Conceito | Definição curta | Distinção ou observação | Onde aparece |
| --- | --- | --- | --- |
| **Camada de rede** | Nível de abstração funcional que executa tarefas especializadas de comunicação. | Presta serviços à camada superior e consome serviços da camada inferior. | [[09. Redes de Computadores/01. Terminologia e fundamentos de redes de computadores#Arquitetura em camadas e tipos de serviços\|Artigo 01 — camadas]] |
| **Serviço orientado à conexão** | Paradigma de comunicação que realiza negociação prévia (*handshake*) antes do envio de dados. | Oferece ordenação, controle de fluxo e retransmissão de dados perdidos (ex.: TCP). | [[09. Redes de Computadores/01. Terminologia e fundamentos de redes de computadores#Serviços orientados versus não orientados à conexão\|Artigo 01 — serviços de conexão]] |
| **Serviço não orientado à conexão** | Paradigma de comunicação em que pacotes são enviados individualmente sem negociação prévia. | Não garante ordem ou entrega confiável, priorizando simplicidade e baixa latência (ex.: UDP). | [[09. Redes de Computadores/01. Terminologia e fundamentos de redes de computadores#Serviços orientados versus não orientados à conexão\|Artigo 01 — serviços de conexão]] |
