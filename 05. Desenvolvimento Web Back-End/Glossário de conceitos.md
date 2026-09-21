# Glossário de conceitos

Este glossário reúne os termos que já apareceram no estudo de Desenvolvimento Web Back-End. Ele deve crescer junto com a disciplina: conceitos só entram aqui depois de aparecerem nas aulas, exercícios ou artigos do vault.

Quando a forma como a PUC apresenta um conceito simplifica uma distinção técnica importante, a observação é registrada explicitamente para separar **o que a disciplina espera na prova** de **como o conceito costuma ser tratado tecnicamente**.

## Arquitetura e organização do sistema

| Conceito | Definição curta | Distinção ou observação | Onde aparece |
| --- | --- | --- | --- |
| **Arquitetura de software** | Organização fundamental de um sistema, incluindo seus elementos, relações e princípios de evolução. | Não é apenas uma lista de tecnologias ou um diagrama. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Descrição arquitetural** | Conjunto de artefatos usados para documentar e comunicar uma arquitetura. | A arquitetura é o sistema organizado; a descrição é a representação dessa arquitetura. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Visão arquitetural** | Representação da arquitetura orientada a determinado interesse ou parte interessada. | Uma visão não representa necessariamente toda a arquitetura. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Estilo arquitetural** | Forma recorrente de organizar componentes e relações de um sistema. | Um sistema pode combinar ideias de mais de um estilo. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Arquitetura em camadas** | Organização lógica do sistema em grupos de responsabilidades. | Não determina sozinha onde cada parte será executada fisicamente. | [[05. Desenvolvimento Web Back-End/02. Estilos arquiteturais - camadas, monolítico e cliente-servidor\|Artigo 02]] |
| **Layer** | Camada lógica usada para separar responsabilidades do software. | Responde principalmente a “como o software está organizado?”. | [[05. Desenvolvimento Web Back-End/02. Estilos arquiteturais - camadas, monolítico e cliente-servidor\|Artigo 02]] |
| **Tier** | Separação física ou de implantação entre partes do sistema. | Responde principalmente a “onde essa parte está executando?”. Várias layers podem existir em um único tier. | [[05. Desenvolvimento Web Back-End/02. Estilos arquiteturais - camadas, monolítico e cliente-servidor\|Artigo 02]] |
| **Arquitetura monolítica** | Organização em que a aplicação é agrupada e implantada como uma unidade principal. | Um monólito pode ser internamente modular e organizado em camadas. | [[05. Desenvolvimento Web Back-End/02. Estilos arquiteturais - camadas, monolítico e cliente-servidor\|Artigo 02]] |
| **Deploy** | Processo de disponibilizar uma versão do software em um ambiente de execução. | A PUC trata a simplicidade inicial de deploy como uma vantagem do monólito. | [[05. Desenvolvimento Web Back-End/02. Estilos arquiteturais - camadas, monolítico e cliente-servidor\|Artigo 02]] |
| **Modularidade** | Organização do sistema em partes com responsabilidades bem delimitadas. | Ajuda a reduzir dependências desnecessárias e facilitar evolução. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Acoplamento** | Grau de dependência entre partes de um sistema. | Dependências excessivas tendem a dificultar alterações e testes. Relaciona-se diretamente a [[01. Programacao Modular/04. Programação orientada a objetos e acoplamento\|Programação Modular]]. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |

## Cliente, servidor e comunicação Web

| Conceito | Definição curta | Distinção ou observação | Onde aparece |
| --- | --- | --- | --- |
| **Cliente** | Componente que inicia uma solicitação a outro componente. | Em aplicações Web, o navegador costuma exercer esse papel. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Servidor** | Componente que recebe solicitações e fornece respostas ou serviços. | Pode executar regras, acessar dados e conversar com outros serviços. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Arquitetura cliente-servidor** | Organização em que clientes solicitam recursos ou operações a servidores. | Na forma simples com um único servidor, esse servidor pode se tornar um gargalo. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] e [[05. Desenvolvimento Web Back-End/02. Estilos arquiteturais - camadas, monolítico e cliente-servidor\|Artigo 02]] |
| **Client-side** | Parte do sistema executada no lado do cliente. | Na Web, normalmente corresponde ao que executa no navegador. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Server-side** | Parte do sistema executada no servidor. | Pode implementar regras de negócio, autenticação, persistência e geração de respostas. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Endereço IP** | Identificador atribuído a uma interface em uma rede IP. | No modelo mental da aula, funciona como o “endereço” que permite localizar uma origem ou destino na rede; a porta identifica um ponto lógico de comunicação. | [[05. Desenvolvimento Web Back-End/03. Tipos de aplicações Web e estratégias de renderização\|Artigo 03]] |
| **Porta** | Número lógico usado para direcionar a comunicação de rede a um processo ou serviço. | HTTP usa convencionalmente a porta 80 e HTTPS a 443, mas aplicações podem usar outras portas. | [[05. Desenvolvimento Web Back-End/03. Tipos de aplicações Web e estratégias de renderização\|Artigo 03]] |
| **TCP** | Protocolo de transporte orientado a conexão que entrega um fluxo de bytes de forma confiável e ordenada. | HTTP/1.1 e HTTP/2 usam TCP; HTTP/3 usa QUIC sobre UDP. | [[05. Desenvolvimento Web Back-End/03. Tipos de aplicações Web e estratégias de renderização\|Artigo 03]] |
| **Requisição HTTP** | Mensagem enviada por um cliente a um servidor para solicitar um recurso ou operação. | Uma página pode gerar várias requisições diferentes. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Resposta HTTP** | Mensagem enviada pelo servidor após processar uma requisição. | Pode transportar HTML, JSON, CSS, JavaScript, imagens, PDFs ou outros tipos de conteúdo. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Content-Type** | Cabeçalho HTTP que informa o tipo de conteúdo transportado na mensagem. | Exemplos estudados: `text/html`, `application/json`, `text/css` e `image/png`. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Conteúdo estático** | Recurso disponibilizado sem precisar ser gerado dinamicamente para cada requisição. | Imagens, arquivos CSS e arquivos JavaScript podem ser servidos como conteúdo estático. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Conteúdo dinâmico** | Conteúdo produzido ou composto pela aplicação conforme a requisição, o estado do sistema ou dados armazenados. | Pode resultar em HTML, JSON ou outros formatos. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |

## Aplicações Web e renderização

| Conceito | Definição curta | Distinção ou observação | Onde aparece |
| --- | --- | --- | --- |
| **DOM** | Representação em memória de um documento Web como uma árvore de objetos. | JavaScript pode manipular o DOM para alterar estrutura, conteúdo e comportamento sem trocar o documento inteiro. | [[05. Desenvolvimento Web Back-End/03. Tipos de aplicações Web e estratégias de renderização\|Artigo 03]] |
| **Renderização** | Processo de produzir a interface que será apresentada ao usuário a partir de código, componentes e dados. | Pode acontecer principalmente no cliente, no servidor ou antecipadamente durante o *build*. | [[05. Desenvolvimento Web Back-End/03. Tipos de aplicações Web e estratégias de renderização\|Artigo 03]] |
| **Template** | Modelo de interface com estrutura definida e partes preenchidas dinamicamente. | Pode ser processado no servidor ou por ferramentas de geração, conforme a arquitetura. | [[05. Desenvolvimento Web Back-End/03. Tipos de aplicações Web e estratégias de renderização\|Artigo 03]] |
| **Controller** | Componente que recebe ou coordena uma ação da aplicação e direciona o processamento necessário. | É uma responsabilidade lógica comum em MVC e não determina, sozinho, que a aplicação seja monolítica. | [[05. Desenvolvimento Web Back-End/03. Tipos de aplicações Web e estratégias de renderização\|Artigo 03]] |
| **Topologia** | Forma como nós, serviços ou componentes estão dispostos e conectados. | Não é sinônimo de tier: tier descreve separação física ou de implantação. | [[05. Desenvolvimento Web Back-End/03. Tipos de aplicações Web e estratégias de renderização\|Artigo 03]] |
| **MPA** | Aplicação de múltiplas páginas em que a navegação principal normalmente solicita um novo documento para cada página ou rota. | Pode usar JavaScript e atualizações assíncronas sem deixar de ser MPA. | [[05. Desenvolvimento Web Back-End/03. Tipos de aplicações Web e estratégias de renderização\|Artigo 03]] |
| **SPA** | Aplicação que mantém um documento principal e atualiza a interface durante a navegação. | Não é sinônimo de CSR: uma SPA pode receber HTML inicial via SSR e depois continuar interativa no cliente. | [[05. Desenvolvimento Web Back-End/03. Tipos de aplicações Web e estratégias de renderização\|Artigo 03]] |
| **AJAX** | Abordagem para realizar requisições assíncronas no navegador e atualizar a página sem recarregamento completo. | O termo surgiu associado a `XMLHttpRequest`; hoje `fetch()` e abstrações de frameworks são comuns. | [[05. Desenvolvimento Web Back-End/03. Tipos de aplicações Web e estratégias de renderização\|Artigo 03]] |
| **Fetch API** | API do navegador para realizar requisições HTTP programaticamente. | É uma alternativa moderna ao `XMLHttpRequest` para muitos casos de comunicação assíncrona. | [[05. Desenvolvimento Web Back-End/03. Tipos de aplicações Web e estratégias de renderização\|Artigo 03]] |
| **CSR** | Estratégia em que a interface é renderizada principalmente no navegador. | É muito associada a SPAs, mas não é sinônimo de SPA. | [[05. Desenvolvimento Web Back-End/03. Tipos de aplicações Web e estratégias de renderização\|Artigo 03]] |
| **SSR** | Estratégia em que o servidor produz HTML para uma requisição e o envia já renderizado ao navegador. | Pode ser usado em aplicações tradicionais ou em aplicações modernas que depois realizam hidratação no cliente. | [[05. Desenvolvimento Web Back-End/03. Tipos de aplicações Web e estratégias de renderização\|Artigo 03]] |
| **SSG** | Estratégia em que páginas HTML são geradas antecipadamente, normalmente durante o *build*. | É adequada quando o conteúdo pode ser conhecido antes da requisição; não é sinônimo de Next.js. | [[05. Desenvolvimento Web Back-End/03. Tipos de aplicações Web e estratégias de renderização\|Artigo 03]] |
| **Hidratação** | Processo em que o JavaScript associa a aplicação interativa ao HTML previamente renderizado. | Permite reaproveitar o HTML inicial e ativar estado, eventos e comportamento no cliente. | [[05. Desenvolvimento Web Back-End/03. Tipos de aplicações Web e estratégias de renderização\|Artigo 03]] |
| **API** | Interface que expõe operações ou dados para serem utilizados por outro software. | Em SPAs, o backend frequentemente fornece dados por APIs enquanto o cliente decide como apresentá-los. | [[05. Desenvolvimento Web Back-End/03. Tipos de aplicações Web e estratégias de renderização\|Artigo 03]] |
| **SEO** | Conjunto de práticas para favorecer descoberta, rastreamento, indexação e compreensão de páginas por mecanismos de busca. | CSR pode exigir cuidados adicionais; SSR e pré-renderização podem tornar o conteúdo inicial mais diretamente acessível aos rastreadores. | [[05. Desenvolvimento Web Back-End/03. Tipos de aplicações Web e estratégias de renderização\|Artigo 03]] |

## Características arquiteturais

| Conceito | Definição curta | Distinção ou observação | Onde aparece |
| --- | --- | --- | --- |
| **Característica arquitetural** | Propriedade de qualidade que influencia decisões estruturais do sistema. | Também pode aparecer na literatura como atributo de qualidade ou requisito não funcional, dependendo do contexto. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Desempenho** | Capacidade do sistema de responder e processar trabalho dentro de limites adequados. | Inclui tempo de resposta, latência, vazão e uso de recursos. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Escalabilidade** | Capacidade de continuar operando adequadamente quando a demanda aumenta. | Muitos clientes conectados a um único servidor não tornam o sistema automaticamente escalável. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] e [[05. Desenvolvimento Web Back-End/02. Estilos arquiteturais - camadas, monolítico e cliente-servidor\|Artigo 02]] |
| **Elasticidade** | Capacidade de aumentar ou reduzir recursos de acordo com a demanda. | É relacionada à escalabilidade, mas não é sinônimo dela. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Disponibilidade** | Proporção de tempo ou condição em que o sistema permanece acessível e operacional. | Não é sinônimo de confiabilidade. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Confiabilidade** | Capacidade de executar corretamente suas funções durante determinado período e sob determinadas condições. | Sistemas críticos podem exigir níveis especialmente altos de confiabilidade. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Continuidade** | Capacidade de manter ou restabelecer serviços diante de incidentes e desastres. | Relaciona-se a planejamento de continuidade e recuperação. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Recuperabilidade** | Capacidade de recuperar funcionamento e dados depois de uma falha. | Pode incluir a rapidez com que o serviço volta a operar. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Robustez** | Capacidade de lidar adequadamente com erros, entradas inesperadas e situações de limite. | Busca evitar que condições anormais levem o sistema a estados inadequados. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Extensibilidade** | Facilidade de adicionar novas funcionalidades sem exigir mudanças excessivas no restante do sistema. | Relaciona-se à organização modular e ao controle de dependências. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Configurabilidade** | Capacidade de alterar comportamentos por configuração em vez de modificar código. | Pode permitir ajustes diferentes para ambientes ou usuários. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Portabilidade** | Capacidade de executar ou ser adaptado para diferentes ambientes e plataformas. | Pode envolver sistema operacional, infraestrutura e dependências tecnológicas. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Manutenibilidade** | Facilidade de corrigir, modificar e aprimorar o sistema ao longo do tempo. | É influenciada por modularidade, acoplamento, legibilidade e outras decisões internas. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Instalabilidade** | Facilidade de instalar e preparar o sistema nos ambientes necessários. | Não é a mesma coisa que portabilidade. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Localização** | Capacidade de adaptar o software a idiomas, moedas, datas, unidades e convenções locais. | Não significa apenas tradução textual. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |

## Segurança, acesso e uso

| Conceito | Definição curta | Distinção ou observação | Onde aparece |
| --- | --- | --- | --- |
| **Segurança** | Proteção do sistema e de seus dados contra acesso, alteração, exposição ou interrupção indevidos. | Criptografia é apenas um dos mecanismos de segurança. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Autenticação** | Processo de verificar a identidade de um usuário ou sistema. | Modelo mental: “quem é você?”. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Autorização** | Processo de determinar o que uma identidade pode acessar ou fazer. | Modelo mental: “o que você pode fazer?”. Normalmente ocorre depois da autenticação. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Privacidade** | Tratamento adequado de dados pessoais ou sensíveis ao longo de coleta, acesso, armazenamento e compartilhamento. | É relacionada à segurança, mas não se reduz a ela. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Acessibilidade** | Capacidade de permitir o uso do sistema por pessoas com diferentes necessidades e condições de interação. | Não se restringe a impedimentos físicos. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Usabilidade** | Grau em que usuários conseguem atingir seus objetivos com eficácia, eficiência e esforço adequado. | É uma característica de qualidade e também se conecta à disciplina de [[08. Design de Interacao/00. Design de Interacao - Resumo\|Design de Interação]]. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Arquivabilidade** | Capacidade de aplicar regras de retenção, arquivamento e exclusão de dados ao longo do tempo. | Pode ser influenciada por requisitos legais e de negócio. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |

## Decisões e trade-offs

| Conceito | Definição curta | Distinção ou observação | Onde aparece |
| --- | --- | --- | --- |
| **Trade-off** | Situação em que melhorar uma característica pode aumentar custo, complexidade ou impacto sobre outra. | Arquitetura exige priorizar qualidades de acordo com o contexto do sistema. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Segurança versus desempenho** | Exemplo de trade-off em que mecanismos de proteção acrescentam processamento ou armazenamento. | A solução não é remover segurança, mas equilibrar requisitos e recursos. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |
| **Disponibilidade versus custo** | Exemplo de trade-off em que redundância aumenta tolerância a falhas, mas também aumenta infraestrutura e operação. | Mostra que maior qualidade arquitetural frequentemente possui custo associado. | [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor\|Artigo 01]] |

## Como a PUC está tratando alguns conceitos

Alguns exercícios usam simplificações adequadas ao nível introdutório da disciplina, mas que não devem ser transformadas em regras universais.

**Cliente-servidor e escalabilidade:** a PUC considera falsa a ideia de que uma arquitetura cliente-servidor é altamente escalável apenas porque muitos clientes podem se conectar a um único servidor. O ponto central é que esse servidor pode se tornar um gargalo.

**Monolítico e facilidade de teste/deploy:** a PUC considera como vantagem do monólito a simplicidade inicial de teste e implantação. Tecnicamente, essa vantagem depende do tamanho, da organização e do estágio do sistema.

**Monolítico versus camadas:** o exercício os compara como alternativas, mas os conceitos podem coexistir. Uma aplicação monolítica pode ser organizada internamente em layers.

## Termos ainda não consolidados

O glossário não antecipa tópicos apenas porque costumam aparecer em cursos de back-end. Conceitos como API REST, endpoint, middleware, rota, ORM, autenticação por token e outros serão adicionados quando efetivamente aparecerem nas aulas, exercícios ou artigos da disciplina.
