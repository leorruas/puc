## 2026-09-23

* **Desenvolvimento Web Back-End 01 — continuidade na seção sobre respostas HTTP**:
  - Removida a abertura solta “Não. Essa afirmação, se tomada literalmente, está errada.”.
  - A seção agora começa diretamente pela ideia de que uma resposta HTTP não precisa conter uma página completa com HTML, CSS e JavaScript.
  - O Mapa de aprendizagem do semestre foi revisado e permanece inalterado, pois a mudança é editorial.

## 2026-09-23

* **Desenvolvimento Web Back-End 01 — hierarquia, continuidade e definição de domínio**:
  - Reorganizado o artigo em quatro blocos hierárquicos: fundamentos de arquitetura; cliente-servidor na Web; estilos e características arquiteturais; conexões e consolidação.
  - Rebaixados subtópicos para níveis de heading coerentes, reduzindo a sensação de sequência plana de seções independentes.
  - Adicionadas transições entre os blocos para explicitar a progressão do geral para o concreto.
  - Incluída a definição de **domínio** como área de problema, com conceitos, regras, operações e restrições, distinguindo domínio de banco de dados, framework e arquitetura.
  - A definição de domínio também foi adicionada ao glossário.
  - O Mapa de aprendizagem do semestre foi revisado e permanece inalterado, pois a mudança melhora organização e clareza sem alterar o estado de aprendizagem.

## 2026-09-23

* **Desenvolvimento Web Back-End 01 — clareza na separação entre organização e implantação**:
  - Reescrita a frase que contrastava separação “lógica” e “física”, substituindo-a por uma explicação mais direta entre organização do software e distribuição na implantação.
  - O Mapa de aprendizagem do semestre foi revisado e permanece inalterado, pois a mudança é apenas editorial.

## 2026-09-23

* **Desenvolvimento Web Back-End — revisão editorial dos artigos 01 a 06**:
  - Revisados os seis artigos para remover referências narrativas desnecessárias a “a aula”, “o professor”, “as anotações” e “o material”.
  - As explicações agora entram diretamente nos conceitos, sem relatar a origem de cada ponto.
  - Mantidas referências explícitas à PUC apenas onde são semanticamente necessárias para interpretar gabaritos ou enquadramentos específicos de prova.
  - Preservadas ressalvas técnicas que distinguem simplificações introdutórias de definições mais amplas.
  - O Mapa de aprendizagem do semestre foi revisado e permanece inalterado, pois a alteração é editorial.

## 2026-09-22

* **Desenvolvimento Web Back-End 04 — correção do contexto exibido no app**:
  - Removido o blockquote usado apenas para enfatizar que “linguagem de script” também é linguagem de programação; a ideia agora aparece integrada ao parágrafo.
  - Reescrita a introdução da seção para eliminar metadiscurso desnecessário sobre a aula.
  - Corrigido o leitor Web para usar no cabeçalho “Contexto” somente blocos explicitamente marcados com `> **Contexto:**`, evitando que qualquer citação comum do artigo seja promovida indevidamente a contexto.
  - O Mapa de aprendizagem do semestre foi revisado e permanece inalterado, pois a mudança é editorial e de navegação.

## 2026-09-22

* **Desenvolvimento Web Back-End 06 — definição de DTO**:
  - Adicionada no artigo 06 a definição de DTO (`Data Transfer Object`) logo após sua primeira ocorrência.
  - Incluído exemplo simples de `CriarPessoaDto` para distinguir objeto de transporte de entidade persistida.
  - Adicionado DTO ao glossário da disciplina, deixando explícito que não precisa ser uma tabela nem ser mapeado pelo EF Core.
  - O Mapa de aprendizagem do semestre foi revisado e permanece inalterado, pois a mudança apenas esclarece terminologia já usada no artigo.

## 2026-09-22

* **Desenvolvimento Web Back-End 06 — definição de contexto no EF Core**:
  - Adicionada uma seção antes de `ApplicationDbContext` explicando que contexto não é o banco de dados, mas o objeto do EF Core que coordena o trabalho da aplicação com o banco.
  - Incluída comparação direta entre banco de dados, `DbContext`, `ApplicationDbContext`, `DbSet<T>`, connection string e provider.
  - Acrescentado ao glossário o termo `Contexto de dados` e refinada a definição de `DbContext`.
  - O Mapa de aprendizagem do semestre foi revisado e permanece inalterado, pois a mudança aprofunda um conceito já coberto no artigo 06.

## 2026-09-22

* **Desenvolvimento Web Back-End 06 — Model, validação, DI e persistência no ASP.NET Core MVC**:
  - Criado o artigo [[05. Desenvolvimento Web Back-End/06. Model, validação e persistência no ASP.NET Core MVC|Model, validação e persistência no ASP.NET Core MVC]] a partir da leitura direta das imagens de estudo registradas entre 14:17 e 17:02.
  - Organizado o fluxo Model → Data Annotations → `ApplicationDbContext` → registro no contêiner → injeção no controller → consulta pelo `DbSet` → banco.
  - Explicados `DbContextOptions`, `DbSet<Pessoa>`, `IdentityDbContext`, `readonly`, injeção por construtor, connection strings, `appsettings.json`, migrations e `Find/FindAsync`.
  - Registrada a diferença entre o padrão antigo com `Startup.ConfigureServices` e o padrão atual com `Program.cs`.
  - Corrigida tecnicamente a interpretação de `DataType.EmailAddress`: ele fornece metadados, enquanto `EmailAddress` é o atributo destinado à validação do formato.
  - Registrado que a connection string com SQL Server LocalDB é específica do Windows e não funciona diretamente no macOS.
  - Atualizados o artigo 05 com navegação para o próximo artigo, o resumo da disciplina, o glossário e o Mapa de aprendizagem do semestre; Desenvolvimento Web Back-End permanece “Em estudo”.

## 2026-09-22

* **Leitor Web — correção de links para arquivos com títulos repetidos**:
  - Corrigida a navegação de notas com nomes repetidos entre disciplinas, como `Glossário de conceitos`.
  - `abrirArtigo()` agora pode receber a referência exata do artigo do catálogo, evitando que um conteúdo ainda não carregado seja reidentificado apenas pelo título e abra a primeira ocorrência encontrada no vault.
  - Atualizados os acessos pela lista da disciplina, busca, navegação anterior/próximo, wikilinks e rotas diretas para preservar a referência exata do artigo.
  - Qualificados explicitamente no resumo de Desenvolvimento Web Back-End os links para `Glossário de conceitos` e `Prompts de Estudo (LLM)`.
  - O Mapa de aprendizagem do semestre foi revisado e permanece inalterado, pois a correção afeta apenas navegação do leitor.

## 2026-09-22

* **Desenvolvimento Web Back-End — migrations no glossário**:
  - Refinada a entrada de `Migration` para `Migrations`, deixando explícito que representam um histórico versionado de alterações do modelo refletidas no esquema do banco.
  - Mantida a distinção entre criar uma migration e aplicar migrations pendentes com `database update`.
  - O Mapa de aprendizagem do semestre foi revisado e permanece inalterado, pois a alteração apenas consolida terminologia já estudada.

## 2026-09-22

* **Desenvolvimento Web Back-End 05 — ajuste editorial em scaffolding**:
  - Removida a formulação “citada na aula” da seção de scaffolding, mantendo a explicação direta do conceito.
  - O Mapa de aprendizagem do semestre foi revisado e permanece inalterado, pois a mudança é apenas editorial.

## 2026-09-22

* **Desenvolvimento Web Back-End 05 — relação com frameworks de negócios movida para a introdução**:
  - A comparação entre frameworks de software e frameworks de negócios/Service Design foi incorporada à introdução do artigo, onde funciona melhor como ponte conceitual inicial.
  - Removida a seção isolada para evitar fragmentação e repetição.
  - O Mapa de aprendizagem do semestre foi revisado e permanece inalterado, pois a alteração é apenas estrutural/editorial.

## 2026-09-22

* **Desenvolvimento Web Back-End 05 — remoção de metadiscurso**:
  - Removidas formulações como “a aula destaca”, “a disciplina apresenta”, “citado na aula” e referências desnecessárias ao professor quando o conteúdo podia ser explicado diretamente.
  - Mantidas referências à transcrição apenas onde a origem é relevante para distinguir reconstrução didática de reprodução literal.
  - O Mapa de aprendizagem do semestre foi revisado e permanece inalterado, pois a mudança é editorial.

## 2026-09-22

* **Desenvolvimento Web Back-End — controller e handler no glossário**:
  - Adicionado o termo `Handler` ao glossário da disciplina.
  - Refinada a definição de `Controller` para explicitar sua relação com MVC e distingui-lo de `handler`, que é um termo mais genérico para o código que trata uma requisição, evento ou mensagem.
  - O Mapa de aprendizagem do semestre foi revisado e permanece inalterado, pois a alteração consolida terminologia já presente no artigo 05.

## 2026-09-22

* **Diretriz editorial — prosa didática direta**:
  - Adicionada ao `AGENTS.md` a regra de evitar metadiscurso desnecessário sobre a origem do conteúdo em artigos, como “citados na aula estão”, “a aula destaca” e “nas anotações aparecem”.
  - Atribuições explícitas à PUC, aula, professor ou fonte ficam reservadas para casos em que a origem realmente altera a interpretação do conteúdo.
  - Ajustada no artigo [[05. Desenvolvimento Web Back-End/05. Frameworks Web, MVC e mapeamento objeto-relacional|Frameworks Web, MVC e mapeamento objeto-relacional]] a frase “Entre os recursos citados na aula estão” para uma formulação didática direta.
  - O Mapa de aprendizagem do semestre foi revisado e permanece inalterado, pois a alteração é editorial.

## 2026-09-22

* **Desenvolvimento Web Back-End 05 — exemplo completo do tutorial de ORM**:
  - Incorporado ao final do artigo [[05. Desenvolvimento Web Back-End/05. Frameworks Web, MVC e mapeamento objeto-relacional|Frameworks Web, MVC e mapeamento objeto-relacional]] um exemplo consolidado baseado na transcrição `17_Mapeamento Objeto-Relacional Orm-Português.txt`.
  - Reconstruído em um único bloco o fluxo completo demonstrado no vídeo: entidades `Genero` e `Filme`, relacionamento 1:N, `ApplicationContext`, `DbSet<T>`, configuração SQL Server, inserção de gênero e filme e `SaveChanges()`.
  - Acrescentados os comandos de migration tanto no Package Manager Console quanto na CLI `dotnet ef`, além dos pacotes necessários para o fluxo atual no macOS.
  - O texto explicita que o código é uma reconstrução didática a partir de uma transcrição automática ruidosa, e não uma reprodução literal do tutorial.
  - O Mapa de aprendizagem do semestre foi revisado e permanece inalterado, pois a alteração aprofunda um exemplo já registrado sem mudar o estado de aprendizagem.

## 2026-09-22

* **Desenvolvimento Web Back-End 05 — ajuste editorial em Razor**:
  - Removida a correção explícita de grafia no título e no texto da seção sobre Razor, mantendo apenas a explicação do conceito.
  - O Mapa de aprendizagem do semestre foi revisado e permanece inalterado, pois a mudança é apenas editorial.

## 2026-09-22

* **Desenvolvimento Web Back-End 05 — frameworks Web, MVC e ORM**:
  - Criado o artigo [[05. Desenvolvimento Web Back-End/05. Frameworks Web, MVC e mapeamento objeto-relacional|Frameworks Web, MVC e mapeamento objeto-relacional]] a partir do arquivo de estudo `web-backend 05.md`.
  - Consolidados conceito de framework Web, abordagens server-centric/browser-centric, frameworks horizontais/verticais, benefícios, trade-offs, MVC, Razor, roteamento, scaffolding e sessões.
  - Corrigida a sigla OMR para ORM e aprofundada a impedância objeto-relacional, distinguindo objetos, propriedades de navegação, chaves estrangeiras e tabelas.
  - Reconstruído de forma autoral o exemplo Genero–Filme, sem reproduzir o tutorial em vídeo, explicando `ICollection<Filme>`, `DbContext`, `DbSet<T>` e migrations.
  - Adicionado caminho equivalente para macOS com .NET CLI e EF Core; registrado que SSMS é somente Windows e que VS Code com extensão MSSQL oferece suporte atual ao macOS.
  - Atualizados o resumo, o glossário e o Mapa de aprendizagem do semestre, mantendo Desenvolvimento Web Back-End em “Em estudo”.

## 2026-09-22

* **Desenvolvimento Web Back-End 04 — correção de escopo editorial**:
  - Reestruturado o artigo [[05. Desenvolvimento Web Back-End/04. Linguagens de programação back-end e PHP|Linguagens de programação back-end]] para refletir o escopo real da aula: características gerais de linguagens e ambientes back-end, com PHP como estudo de caso principal.
  - Adicionada uma seção explícita sobre o papel geral de qualquer linguagem server-side e uma tabela com os eixos apresentados na aula: modelo de execução, tipagem, portabilidade, integração Web, acesso a dados e templates.
  - Mantidos PHP, C# e ASP.NET Core MVC apenas nos papéis sustentados pelo material: PHP como foco da sessão, C# como contraste em tipagem/execução e ASP.NET Core MVC/Razor como conteúdo posterior anunciado pela disciplina.
  - Atualizado o resumo da disciplina. O Mapa de aprendizagem do semestre foi revisado e permanece inalterado, pois a alteração corrige o enquadramento do artigo sem mudar o estado de aprendizagem.

## 2026-09-21

* **Desenvolvimento Web Back-End 04 — linguagens back-end e PHP**:
  - Criado o artigo [[05. Desenvolvimento Web Back-End/04. Linguagens de programação back-end e PHP|Linguagens de programação back-end e PHP]] a partir do arquivo de estudo `web-backend 04.md`.
  - O conteúdo copiado da página da PUC foi usado apenas como base conceitual e reescrito em linguagem própria.
  - Consolidados PHP, processamento server-side, GET/POST, templates Web, Apache/MySQL/PHP e pilha WAMP.
  - Refinadas as anotações sobre script versus linguagem de programação, compilação versus interpretação, modelos híbridos e tipagem estática versus dinâmica.
  - Corrigidos pontos conceituais das notas: PHP significa “PHP: Hypertext Preprocessor”; código interpretado não implica código-fonte visível ao usuário; portabilidade não decorre de tipagem dinâmica; servidor Web não se limita a servir arquivos.
  - Atualizados o resumo, o glossário e o Mapa de aprendizagem do semestre, mantendo a disciplina no estado “Em estudo”.

## 2026-09-21

* **Desenvolvimento Web Back-End — correção do glossário**:
  - Corrigida a quebra de tabela introduzida na expansão do glossário após o artigo 03.
  - Separados os conceitos em duas seções: “Cliente, servidor e comunicação Web” e “Aplicações Web e renderização”.
  - Refinadas definições de endereço IP, porta, TCP, conteúdo estático, DOM, AJAX, SSR, SSG, hidratação e SEO para maior precisão e consistência com o artigo 03.
  - Mantidos os wikilinks protegidos com `\|` nas tabelas.
  - O Mapa de aprendizagem do semestre foi revisado e permanece inalterado, pois a alteração corrige organização e precisão conceitual sem mudar o estado de estudo da disciplina.

## 2026-09-21

* **Desenvolvimento Web Back-End 03 — links das referências complementares**:
  - Adicionados links diretos para MDN Web Docs, web.dev, Google Search Central, documentação do Next.js e Microsoft Learn na seção de referências do artigo [[05. Desenvolvimento Web Back-End/03. Tipos de aplicações Web e estratégias de renderização|Tipos de aplicações Web e estratégias de renderização]].
  - O Mapa de aprendizagem do semestre foi revisado e permanece inalterado, pois a alteração é apenas bibliográfica.

## 2026-09-21

* **Desenvolvimento Web Back-End 03 — diagramas da aula convertidos para Mermaid**:
  - Incorporada ao artigo [[05. Desenvolvimento Web Back-End/03. Tipos de aplicações Web e estratégias de renderização|Tipos de aplicações Web e estratégias de renderização]] a leitura dos dois diagramas enviados pelo estudante: aplicação Web tradicional e SPA.
  - Criados dois diagramas Mermaid compactos, preservando a separação client-side/server-side e os fluxos centrais apresentados na aula.
  - No fluxo tradicional, explicitados navegador, servidor Web, servidor de aplicação, arquivos/templates e banco de dados.
  - No fluxo SPA, explicitados carregamento inicial, atualização do DOM/componentes e chamadas assíncronas a Web APIs.
  - Registrada a ressalva de que AJAX é a técnica/conceito de comunicação assíncrona, não uma tecnologia obrigatória, e de que JSON é um formato comum, mas não exclusivo.
  - O Mapa de aprendizagem do semestre foi revisado e permanece inalterado, pois a alteração aprofunda visualmente conteúdo já estudado.

## 2026-09-21

* **Desenvolvimento Web Back-End 03 — comparação visual entre SSR e SPA/CSR**:
  - Expandida a seção de SSR no artigo [[05. Desenvolvimento Web Back-End/03. Tipos de aplicações Web e estratégias de renderização|Tipos de aplicações Web e estratégias de renderização]] para explicar por que o carregamento inicial pode ser mais rápido quando o HTML é produzido no servidor.
  - Adicionado diagrama Mermaid comparando, passo a passo, o carregamento inicial de uma SPA com CSR e de uma aplicação com SSR.
  - Registrada a ressalva de que “SSR é muito mais rápido que SPA” não é uma regra universal; a vantagem depende da carga do servidor, tamanho dos bundles, cache, rede, dispositivo e implementação.
  - O Mapa de aprendizagem do semestre foi revisado e permanece inalterado, pois a alteração aprofunda um conceito já registrado sem mudar o estado da disciplina.

## 2026-09-21

* **Desenvolvimento Web Back-End 03 — tipos de aplicações Web e renderização**:
  - Criado o artigo [[05. Desenvolvimento Web Back-End/03. Tipos de aplicações Web e estratégias de renderização|Tipos de aplicações Web e estratégias de renderização]] a partir do arquivo de estudo `web-backend 03.md`.
  - O material da página da PUC foi usado apenas como referência de conteúdo: os trechos foram reestruturados e reescritos em linguagem própria para evitar reprodução literal no vault público.
  - Consolidadas as distinções entre MPA e SPA, CSR, SSR e SSG, além de DOM, AJAX/Fetch, portas, TCP, templates, controllers, topologia e hidratação.
  - Corrigidas simplificações das anotações: SPA não exige AJAX; SSR não é requisito absoluto para indexação pelo Google; Next.js não é sinônimo de SSG; o framework Microsoft citado é Blazor; controller não determina arquitetura monolítica.
  - Atualizados o resumo, o glossário e o Mapa de aprendizagem do semestre para registrar a nova cobertura, mantendo o estado da disciplina como “Em estudo”.

## 2026-09-21

* **Desenvolvimento Web Back-End — criação do glossário de conceitos**:
  - Criado [[05. Desenvolvimento Web Back-End/Glossário de conceitos|Glossário de conceitos]] com os termos efetivamente estudados nos artigos 01 e 02.
  - Organizados conceitos de arquitetura, cliente-servidor, HTTP, características arquiteturais, segurança e trade-offs, com links para os artigos correspondentes.
  - Registradas separadamente as simplificações didáticas usadas pela PUC sobre escalabilidade cliente-servidor e vantagens iniciais da arquitetura monolítica.
  - Atualizado o resumo da disciplina para incluir o glossário como material de apoio. O Mapa de aprendizagem do semestre foi revisado e permanece inalterado, pois a alteração organiza conteúdo já estudado sem acrescentar nova evidência de domínio.

## 2026-09-21

* **Desenvolvimento Web Back-End 02 — estilos arquiteturais**:
  - Criado o artigo [[05. Desenvolvimento Web Back-End/02. Estilos arquiteturais - camadas, monolítico e cliente-servidor|Estilos arquiteturais: camadas, monolítico e cliente-servidor]], consolidando arquitetura em camadas, distinção entre *layers* e *tiers*, escalabilidade cliente-servidor e arquitetura monolítica.
  - Registrado o gabarito da PUC para a questão sobre os três estilos: I e III verdadeiras e II falsa.
  - Incluída ressalva técnica de que monolítico e arquitetura em camadas não são categorias mutuamente exclusivas e de que a facilidade de teste atribuída ao monólito é contextual.
  - Atualizado o resumo da disciplina e o Mapa de aprendizagem do semestre: Desenvolvimento Web Back-End passa de “Ainda não estudado” para “Em estudo”, com dois artigos de cobertura inicial.

## 2026-09-21

* **Desenvolvimento Web Back-End 01 — uso de material visual como fonte de apoio**:
  - Removida a incorporação direta do screenshot da aula no artigo [[05. Desenvolvimento Web Back-End/01. Arquitetura de software e cliente-servidor|Arquitetura de software e cliente-servidor]].
  - Imagens e demais arquivos da inbox devem ser tratados como fontes de apoio para leitura, interpretação e enriquecimento dos artigos, sendo incorporados visualmente apenas quando isso acrescentar valor didático.
  - O conteúdo em elaboração do artigo 02 não foi alterado.
  - A alteração é editorial e não muda o estado de aprendizagem da disciplina; o Mapa de aprendizagem do semestre foi revisado e permanece inalterado.

# Log de alterações do vault

Este arquivo registra o histórico de criações, modificações, edições e reorganizações estruturais realizadas no vault em **ordem cronológica decrescente (mais recente no topo)**.

## 2026-09-08

* **Compatibilidade progressiva para iPad mini e Safari/iOS 12**:
  - O leitor moderno agora é carregado de forma condicional; navegadores atuais mantêm o mesmo `script.js` modular e o Mermaid interativo.
  - Adicionado um leitor de compatibilidade para navegadores sem módulos, como o Safari do iPad mini 2: catálogo, busca por título/matéria, navegação entre notas, tema claro/escuro e leitura de Markdown continuam disponíveis.
  - A folha de compatibilidade foi isolada em `compat-ios12.css`; usa exclusivamente os tokens azul, fundo, texto e contraste já definidos no PUC, sem importar a identidade cromática do repositório Programação.
  - Para esse navegador legado, blocos Mermaid mostram o código-fonte de forma rolável e explícita, em vez de produzir um diagrama quebrado.
  - A alteração é de acesso e apresentação, sem impacto em evidências de aprendizagem; o Mapa de aprendizagem do semestre foi revisado e permanece inalterado.

## 2026-09-07

* **Engenharia de Requisitos — autores e referências consolidados**:
  - Adicionado ao resumo o quadro de autores, métodos e normas centrais, com ligações para as notas em que cada contribuição é estudada.
  - Registradas no resumo as referências de Wiegers e Beatty e da ISO/IEC/IEEE 29148.
  - Incluídas as referências que faltavam nas notas de alinhamento com negócios, conceito de requisito, critérios de qualidade e técnicas de elicitação.
  - A alteração é bibliográfica e não muda evidências de aprendizagem; o Mapa de aprendizagem do semestre foi revisado e permanece inalterado.

## 2026-09-07

* **Design de Interação — autores e referências consolidados**:
  - Adicionado ao resumo da disciplina o quadro de autores, grupos e normas que fundamentam os métodos estudados, com vínculo para as notas correspondentes.
  - Incluídas as referências formais de Alan Cooper e das normas ISO 9241-11/210 na nota de modelagem de usuário.
  - Incluída a referência de Charles S. Peirce na nota de projeto de ícones, que usa sua classificação semiótica.
  - A alteração é bibliográfica e não muda evidências de aprendizagem; o Mapa de aprendizagem do semestre foi revisado e permanece inalterado.

## 2026-09-07

* **Gatilho obrigatório para o mapa de aprendizagem do semestre**:
  - Incluída no `AGENTS.md` a Regra 8.1, exigindo a revisão do impacto transversal de toda nota criada ou editada antes do commit.
  - Quando houver mudança de progresso, evidência de domínio, lacuna, prioridade de revisão ou ponte interdisciplinar, o arquivo [[00. Geral/Mapa de aprendizagem do semestre.md|Mapa de aprendizagem do semestre]] deve ser atualizado no mesmo conjunto de alterações.
  - A diretriz operacional correspondente foi adicionada a `.obsidian/vault_rules.md`, preservando o compromisso de registrar apenas estados sustentados por evidências reais do vault.

## 2026-09-05

* **Formalização da compatibilidade obrigatória com o explorador Mermaid e política de integridade**:
  - Atualização da Regra 9 em `AGENTS.md` e da Regra 10 em `.obsidian/vault_rules.md`, estabelecendo a compatibilidade mandatória de todo diagrama Mermaid com o pipeline do leitor web (`js/mermaid.js` e `script.js`).
  - Formalizada a separação estrita de responsabilidades: Markdown define conteúdo e semântica; Mermaid define a representação gráfica; `js/mermaid.js` gerencia renderização, temas, classes semânticas, wrapper, toolbar e o botão `ampliar` com modal interativo (*fit*, zoom e pan).
  - Proibição absoluta de visualizações alternativas (SVG manual, conversão para imagens, screenshots, HTML customizado ou scripts na nota).
  - Instituído o critério obrigatório de aceite pré-commit (`renderiza → sem erro → ampliar aparece → explorador abre → fechar → abrir novamente`) e a regra de que qualquer falha de Mermaid (`Syntax error in text` ou diagrama quebrado) é regressão bloqueante.
* **Revisão da sintaxe Mermaid no artigo `07. Modelo de entidades e relacionamentos estendido`**:
  - Diagnóstico do erro léxico (`Syntax error in text`) no primeiro diagrama do artigo 07: remoção de formas instáveis (`[["..."]]` para entidade fraca e `[Total]` dentro de rótulo de aresta com colchetes) e adoção de sintaxe padrão e robusta com retângulo simples `Agencia["AGENCIA<br>(entidade fraca)"]`, preservando a semântica conceitual e os atributos.
  - Revisão estática de sintaxe dos demais diagramas (Diagrama 2: Funcionário/Projeto com `Função`; Diagrama 3: Relacionamento ternário; Diagrama 4: Critério de decisão).
  - Diferenciação expressa no log entre revisão estática de código e validação operacional em tempo de execução no leitor web.

## 2026-09-04

* **Harmonização de regras e aplicação de sentence case editorial**:
  - Harmonização normativa entre `AGENTS.md` (regra 3), `.obsidian/vault_rules.md` (regras 1 e 2) e `.agents/rules/artigos.md` (regra 4), estabelecendo o sentence case editorial como padrão obrigatório para toda redação gerada no vault (títulos H1 a H6, rótulos em negrito antes de dois-pontos, microtítulos, itens de lista, tabelas e subgraphs Mermaid).
  - Preservação estrita das exceções legítimas: nomes próprios, marcas e produtos (`GitHub`, `Azure App Service`, `Visual Studio`), siglas e acrônimos (`C#`, `SQL`, `UML`, `CRUD`, `SOLID`, `TAD`, `POO`), referências ABNT, termos de código e transcrições literais de reuniões.
  - Correção editorial e remoção de Title Case em notas de reuniões de acompanhamento do projeto (`05`, `06`, `07` e resumo `00`), na Aula Inaugural e em artigos da disciplina de Programação Modular (`02`, `03`, `04`, `05`, `06`, `07`, `09` e `13`).
  - Preservação integral dos destaques de estudo do usuário (`==texto==`) e remoção de emojis residuais.
* **Auditoria e refinamento da regra de proibição de ASCII art**:
  - Auditoria realizada na diretriz de diagramas e ASCII art em `AGENTS.md` e consolidação em `.obsidian/vault_rules.md`.
  - Esclarecida a fronteira entre diagramas estruturais/conceituais (onde Mermaid nativo e tabelas Markdown são estritamente obrigatórios) e árvores de diretórios/arquivos de projeto (`tree`), autorizadas exclusivamente em blocos de código (`text` ou `bash`).
  - Alinhamento pleno com a regra de *sentence case* editorial (`Proibição de diagramas em ASCII art`).

## 2026-09-02

* **Revisão funcional do vault e harmonização de regras**:
  - Auditoria completa das regras em `AGENTS.md`, `.obsidian/vault_rules.md` e `.agents/rules/`.
  - Corrigida a quebra de numeração da Regra 11 em `AGENTS.md` e formalizadas as Regras 20 (*Preservação do Desenvolvimento Incremental e Não-Enciclopedismo*) e 21 (*Distinção Editorial entre Conteúdo da PUC e Complementação Didática*).
  - Atualizado `.obsidian/vault_rules.md`, removendo referências a scripts inexistentes (`fix_title_capitalization.py` e `link_linter.py`) e alinhando a diretriz de interlinkagem com foco qualitativo e significado intelectual claro (sem hiperconexão artificial).
  - Alinhadas as regras em `.agents/rules/artigos.md` e `.agents/rules/interlinkagem.md`.
* **Criação do Mapa de Aprendizagem do Semestre**: criada a nota transversal [[00. Geral/Mapa de aprendizagem do semestre.md|Mapa de aprendizagem do semestre]] em `00. Geral/`, consolidando critérios objetivos de estado (`Ainda não estudado`, `Em estudo`, `Compreendido`, `Revisar`) baseados estritamente nas evidências reais do vault, acompanhada por matriz visual em Mermaid (`flowchart TD`) das pontes entre teoria, modelagem e código.
* **Padronização da taxonomia de diagnóstico de erros**: expandido o protocolo pedagógico de feedback nos prompts de estudo com LLM ([[01. Programacao Modular/Prompts de Estudo (LLM).md|Programação Modular]], [[02. Modelagem de Dados/Prompts de Estudo (LLM).md|Modelagem de Dados]], [[07. Engenharia de Requisitos/Prompts de Estudo (LLM).md|Engenharia de Requisitos]] e [[08. Design de Interacao/Prompts de Estudo (LLM).md|Design de Interação]]) para categorizar erros em 6 dimensões: *conceitual*, *terminológico*, *leitura/interpretação*, *aplicação*, *sintaxe/leitura de código* e *distração/desatenção*.
* **Modernização do `index.md`**: reformulação da página inicial como hub acadêmico funcional; remoção de blocos de configuração cosmética do Obsidian (tema/accent), inserção de atalho em destaque para o *Mapa de Aprendizagem*, atualização do status do Projeto Integrador (Etapa 02) e explicitação do estado real de cada microfundamento.
* **Refinamento dos estados no Mapa de Aprendizagem e index.md**: calibrados os estados para diferenciar rigorosamente cobertura no vault, progresso da disciplina e evidência real de aprendizagem do aluno; o status `Compreendido` foi mantido exclusivamente em Programação Modular (devido ao histórico consistente de simuladores com correção taxonômica, modelo mental dominado e código C# compilado), enquanto Engenharia de Requisitos e Design de Interação foram ajustadas para `Em estudo` (aguardando baterias práticas de validação).
* **Integração e visibilidade no app web (`index.html` e `script.js`)**:
  - Inserido atalho direto `mapa` na barra de navegação superior (`sticky-nav`), com roteamento instantâneo via `navegarParaLinkObsidian`.
  - Atualizado o card de `00. Geral` na página inicial destacando o Mapa de Aprendizagem.
  - Dividido o diagrama de pontes conceituais do mapa em dois blocos verticais Mermaid (`flowchart TD`) autocontidos (Fluxo A: Requisitos, Arquitetura e Código; Fluxo B: Dados Relacionais e Interface), otimizando a legibilidade em telas compactas e desktop nos temas claro e escuro.
  - Adicionado link reverso para o Mapa em [[00. Geral/Aula Inaugural (04-08-2026) - Resumo.md|Aula Inaugural]].

---

## 2026-08-29

* **Correção no roteador do leitor web (resolução de links internos com C#)**: implementada a função `separarDestinoEHash()` no `script.js` para diferenciar sustenidos de linguagens (`C#`) de âncoras de seção (`#secao`), corrigindo a quebra de navegação em links como `[[00. Evolução das linguagens e genealogia do C (C, C++, Java, C#, JS, Python)]]` no índice de sintaxe multilinguagem.
* **Atualização dos prompts de estudo com LLM de Programação Modular**: reformulação completa de [[01. Programacao Modular/Prompts de Estudo (LLM).md|Prompts de Estudo (LLM)]], integrando a ementa de todos os 24 tópicos da disciplina, simulador global de prova, simuladores temáticos por unidade (Unidades 1, 2 e 3) e o protocolo de diagnóstico pedagógico estruturado de erros com categorização de falhas.
* **Inclusão da matriz bidimensional de padrões de projeto GoF**: inserida a tabela de classificação do GoF (cruzamento entre Escopo de Classe vs. Escopo de Objeto e os 3 propósitos: Criacional, Estrutural e Comportamental) na nota [[01. Programacao Modular/24. Padrões de projeto (design patterns) e o catálogo GoF.md|24. Padrões de projeto e o catálogo GoF]].
* **Correção no leitor web (ocultação da caixa de contexto em páginas sem contexto)**: corrigida a regra de especificidade CSS (`.artigo-contexto[hidden], .artigo-contexto.escondido, [hidden] { display: none !important; }`) e no script JavaScript (`classList.add("escondido")`), garantindo que em notas, transcrições e resumos que não possuem parágrafo de `> **Contexto:**`, o container visual de contexto fique 100% oculto, eliminando caixas vazias ou espaçamentos residuais.
* **Auditoria da regra de interlinkagem interdisciplinar (Regra 18)**: auditoria completa realizada em todo o acervo do vault, implementando pontes conceituais e interlinkagens bidirecionais entre:
  1. *Diagrama de Classes da UML* ([[07. Engenharia de Requisitos/09. Modelagem estrutural com diagrama de classes da uml.md|ER 09]]) ↔ *Encapsulamento, Herança, Abstração e SOLID (DIP/Composição)* ([[01. Programacao Modular/07. Atributos e métodos (classes, objetos e definição de membros).md|PM 07]], [[01. Programacao Modular/15. Herança (generalização, especialização e extensibilidade modular).md|PM 15]], [[01. Programacao Modular/18. Classes abstratas e métodos abstratos (contratos de herança e polimorfismo puro).md|PM 18]], [[01. Programacao Modular/23. Princípios SOLID de design orientado a objetos.md|PM 23]]) e *Etapa 02 do Projeto* ([[06. Projeto - Aplicacao Interativa/03. Cronograma semanal e entregas de etapas.md|Projeto 03]]).
  2. *Diagrama de Pacotes da UML* ([[07. Engenharia de Requisitos/10. Modelagem estrutural e modularização com diagrama de pacotes da uml.md|ER 10]]) ↔ *Namespaces e Modularização em Larga Escala* ([[01. Programacao Modular/14. Namespaces e partial classes (espaços de nomes e modularização em larga escala).md|PM 14]]).
  3. *Modelagem de Personas e Prototipagem/Wireframes* ([[08. Design de Interacao/12. Modelagem de usuário - perfil, persona e mapa de empatia.md|IHC 12]], [[08. Design de Interacao/13. Prototipagem de sistemas interativos - fidelidade, dimensão, wireframe, mockup e storyboard.md|IHC 13]]) ↔ *Escopo, Histórias de Usuário e Entregas do Projeto Integrador* ([[06. Projeto - Aplicacao Interativa/02. Requisitos e diretrizes de escopo do projeto.md|Projeto 02]], [[06. Projeto - Aplicacao Interativa/03. Cronograma semanal e entregas de etapas.md|Projeto 03]]).
* **Regra de interlinkagem interdisciplinar obrigatória**: inserida a regra 18 em `AGENTS.md` e criada a regra global em `.agents/rules/interlinkagem.md`, formalizando a obrigatoriedade de conectar e explicitar analogias entre conceitos teóricos de modelagem (UML, IHC, Requisitos) e suas materializações práticas em código (Programação Modular, Guia de Sintaxe e Projeto Integrador), com interlinkagem bidirecional e atualização de frontmatter.
* **Interlinkagem interdisciplinar (include e extend da UML com funções, exceções e condicionais)**: consolidação e interconexão profunda dos conceitos arquiteturais ensinados pela Profa. Rosilane nas notas de [[07. Engenharia de Requisitos/08. Modelagem de requisitos com casos de uso e especificações textuais.md|Engenharia de Requisitos]], [[01. Programacao Modular/02. Funções e procedimentos.md|Programação Modular]], [[00. Sintaxe Multilinguagem/04. Sub-rotinas (funções e procedimentos).md|Guia de Sub-rotinas]], [[00. Sintaxe Multilinguagem/09. Tratamento de exceções e erros (try, catch, finally, throw).md|Guia de Exceções]], [[00. Sintaxe Multilinguagem/02. Estruturas condicionais (if, else, switch).md|Guia de Condicionais]] e [[06. Projeto - Aplicacao Interativa/02. Requisitos e diretrizes de escopo do projeto.md|Diretrizes de Escopo do Projeto]]. O relacionamento `«include»` foi contextualizado como a chamada de função/procedimento puro (obrigatório e reutilizável), e o `«extend»` como o tratamento de exceção (`try-catch-throw`) e ramificação condicional opcional (`if`).

## 2026-08-28

* **Criação da nota de acompanhamento do projeto (Semana 4)**: processada e criada a nota [[06. Projeto - Aplicacao Interativa/06. Reunião de acompanhamento do grupo 4 (27-08-2026) - resumo e transcrição integral.md|06. Reunião de acompanhamento do grupo 4 (27-08-2026)]], contendo o resumo executivo e a transcrição integral da revisão final da Etapa 01, casos de uso, restrições de projeto e vídeo com a Profa. Rosilane Ribeiro da Mota.

## 2026-08-26

* **Regra de padronização de datas em reuniões e aulas síncronas**: inserida a regra 15 em `AGENTS.md` e em `.agents/rules/reunioes.md`, tornando obrigatória a inclusão da data no nome do arquivo `(DD-MM-AAAA)`, no título principal `# H1` `(DD/MM/AAAA)` e no bloco de metadados `==DD/MM/AAAA==`. Todas as notas de reuniões existentes foram renomeadas e seus links internos e manifesto web sincronizados.
* **Criação da nota de acompanhamento do projeto**: processada e criada a nota [[06. Projeto - Aplicacao Interativa/05. Reunião de acompanhamento do grupo 4 (20-08-2026) - resumo e transcrição integral.md|05. Reunião de acompanhamento do grupo 4 (20-08-2026)]], contendo o resumo executivo e a transcrição na íntegra do encontro com a Profa. Rosilane Ribeiro da Mota.
* **Atualização visual**: o leitor acadêmico passou a usar a mesma linguagem editorial do Guia do Portal IFMG, com índice amplo por matérias, busca lateral em telas grandes, fundo contínuo e navegação por filetes. A identidade da PUC foi preservada com azul como cor de apoio; o modo claro usa fundo branco. Na capa, “ads” recebeu o destaque principal e “puc minas” passou a atuar como assinatura menor. As notas passam a ser carregadas pela cópia pública do repositório, para que a grade de matérias também funcione quando o arquivo é aberto pelo Obsidian.

* **Diagramas Mermaid**: os diagramas passam a usar paletas próprias para claro e escuro, com texto e conectores de alto contraste. A troca de tema redesenha o diagrama aberto para manter o resultado legível.
* **Integração editorial dos diagramas**: removidos cantos arredondados e superfícies de cartão; nós e conectores usam linhas finas, alinhadas aos filetes de navegação do leitor.
* **Escala tipográfica dos diagramas**: rótulos, conectores e títulos internos usam 16 px no desktop e 14 px em telas compactas, com espaçamento de fluxo padronizado.

## 2026-08-02

* **Instalação de Dependência**: Instalação do .NET 8.0 SDK
 * Executado instalador local para configurar o .NET SDK 8.0.423 em `~/.dotnet/` permitindo compilação e execução de C# no ambiente local.

* **Criação de Código e Nota**: Introdução a C# e Arrays
 * Criação do código [[04. Algoritmos e Estruturas de Dados/SomaDoisNumeros.cs\|SomaDoisNumeros.cs]] que lê dois números e exibe a soma.
 * Criação da nota explicativa [[04. Algoritmos e Estruturas de Dados/Recordando C# e arrays.md\|Recordando C# e arrays.md]] detalhando compiladores, tipagem e arrays usando o Método Feynman.
 * Atualização da nota principal [[04. Algoritmos e Estruturas de Dados/00. Algoritmos e Estruturas de Dados - Resumo.md\|Algoritmos e Estruturas de Dados - Resumo]] para referenciar os novos arquivos.

* **Atualização de Regra**: Reforço de Cross-linking Exaustivo
 * Atualização da regra de conexões em [[.obsidian/vault_rules.md\|vault_rules.md]] e [[mim.md\|mim.md]] para exigir o máximo de links cruzados e conexões possíveis a cada nova inserção de conteúdo.

* **Criação de Nota**: [[mim.md\|Sobre mim e diretrizes do vault]]
 * Renomeada de `me.md` para `mim.md` conforme solicitação.
 * Perfil pessoal de Leonardo Ruas Santos detalhando formação em Design, Publicidade, MBA e a graduação atual em ADS na PUC Minas.
 * Integração das 8 regras do vault e a grade completa do 1º período.
 * Definição explícita do Método Feynman e instruções obrigatórias para agentes de IA.

* **Criação de Estrutura**: Setup inicial do LLM Wiki da PUC
 * Importação das regras e diretrizes de estilo do vault a partir de `programação/.obsidian/vault_rules.md` para [[.obsidian/vault_rules.md|vault_rules.md]].
 * Criação da página inicial [[index|Portal Acadêmico PUC Minas - ADS]] com tabela limpa e links protegidos (`\|`) em conformidade com as regras.
 * Criação de 11 diretórios organizados para cada microfundamento/projeto do semestre do curso de Análise e Desenvolvimento de Sistemas:
 * `01. Programacao Modular`
 * `02. Modelagem de Dados`
 * `03. Manipulacao de Dados SQL`
 * `04. Algoritmos e Estruturas de Dados`
 * `05. Desenvolvimento Web Back-End`
 * `06. Projeto - Aplicacao Interativa`
 * `07. Engenharia de Requisitos`
 * `08. Design de Interacao`
 * `09. Redes de Computadores`
 * `10. Lideranca e Competencias`
 * `11. Desafios Contemporaneos`
 * Criação das notas de resumo individuais para cada disciplina (ex: `00. Programacao Modular - Resumo.md`) e guias específicos de prompt de estudo com LLM (`Prompts de Estudo (LLM).md`), estruturados didaticamente de acordo com o Método Feynman.
 * Execução do pós-processamento para remoção de emojis de todo o vault para cumprir a Regra 8 de estética estritamente textual.
* 2026-08-29: Padronizada a hierarquia de títulos dos artigos, com escala progressiva do `h1` ao `h6` e marcador azul discreto nos três primeiros níveis.
* 2026-08-29: Navegação de artigo alinhada ao padrão do Guia do Portal, com anterior e próximo em faixa editorial e retorno separado.
* 2026-08-29: Busca global consolidada na navbar; removido o campo duplicado da sidebar e preservado o filtro específico de seções.
