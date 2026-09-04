# Regras Gerais do Vault

## Estilo de Formatação e Escrita

1. **Proibição estrita de emojis:**
 - É estritamente proibido utilizar emojis em qualquer arquivo Markdown (`.md`), cabeçalhos, tabelas, títulos de notas, listas ou respostas.
 - Todo o conteúdo deve ser mantido em tom profissional, técnico e limpo.

2. **Destaque de datas em cronogramas:**
 - Todas as datas e períodos em cronogramas, prazos de entrega e calendários devem ser destacados obrigatoriamente utilizando a sintaxe de highlight do Obsidian (`DD/MM/AAAA`).

3. **Sentence case editorial obrigatório:**
 - **Princípio normativo:** Toda redação editorial criada ou reescrita para o vault deve seguir a capitalização normal de frases em português (*sentence case*), onde **apenas a primeira palavra da frase/item inicia com letra maiúscula**. É expressamente proibido utilizar *Title Case* para indicar importância conceitual, categoria, tópico, rótulo ou estrutura textual. A regra não se limita a nomes de arquivos ou títulos; aplica-se a toda redação editorial no corpo do texto.
 - **Onde o sentence case é obrigatório:** Aplica-se a toda redação editorial produzida pelo agente, incluindo:
   - Títulos H1 a H6 e subcabeçalhos;
   - Campo `title:` de frontmatter YAML;
   - Títulos de seções, subtítulos, chamadas e legendas produzidas pelo vault;
   - Rótulos em negrito no início de parágrafos ou antes de dois-pontos (ex.: incorreto `**Configuração e Publicação de Aplicativos Web na Azure:**` → correto `**Configuração e publicação de aplicativos web na Azure:**`; incorreto `**Tratamento de Exceções:**` → correto `**Tratamento de exceções:**`);
   - Itens de listas com marcadores (`*`, `-`), tabelas nativas e nomes editoriais de etapas;
   - Analogias, definições destacadas, rótulos explicativos e qualquer microtítulo no corpo do texto;
   - Títulos e rótulos contextuais produzidos dentro de diagramas Mermaid (ex.: incorreto `Processar Pagamento` → correto `Processar pagamento`).
 - **Preservação de maiúsculas legítimas (não confundir sentence case com lowercase):** Devem ser rigorosamente preservadas maiúsculas exigidas pela grafia convencional:
   - Siglas e acrônimos: `C#`, `SQL`, `UML`, `SOLID`, `GoF`, `CRUD`, `API`, `TAD`, `POO`, `GC`, `SGBD`, `DER`, `MER`, `IHC`, `REST`;
   - Nomes próprios, marcas, produtos e plataformas: `GitHub`, `JavaScript`, `Mermaid`, `Azure`, `Azure App Service`, `Node.js`, `SQL Server`, `Python`, `Bootstrap`, `Figma`, `Microsoft Teams`;
   - Nomes próprios de pessoas, autores e instituições: `PUC Minas`, `Rosilane Ribeiro da Mota`, `Feynman`.
 - **Distinção fundamental entre redação editorial e conteúdo reproduzido:** NÃO alterar automaticamente a capitalização de conteúdo que o vault está apenas reproduzindo, citando ou referenciando de fontes externas. Preservar a grafia original de:
   - Títulos de livros, artigos acadêmicos e vídeos de terceiros (ex.: `[Azure App Service Node - Parte 1](...)`);
   - Títulos de aulas quando reproduzidos formalmente de cronogramas oficiais;
   - Referências bibliográficas, citações literais e transcrições integrais de reuniões/aulas;
   - Nomes oficiais de documentos e especificações institucionais.
 - **Conceitos não viram nomes próprios por serem importantes:** Maiúscula não deve ser usada simplesmente porque uma expressão designa disciplina, área de conhecimento, conceito, metodologia, paradigma, etapa, categoria, princípio ou técnica.
   - Incorreto: `Engenharia de Requisitos` | Correto editorialmente: `Engenharia de requisitos`
   - Incorreto: `Programação Modular` | Correto editorialmente: `Programação modular`
   - Incorreto: `Modelagem de Dados` | Correto editorialmente: `Modelagem de dados`
   - Incorreto: `Orientação a Objetos` | Correto editorialmente: `orientação a objetos`
   - Incorreto: `Design de Interação` | Correto editorialmente: `Design de interação`
   - Usar Markdown (negrito/itálico) para ênfase semântica, nunca capitalização.
 - **O que não deve ser modificado:** A regra não afeta código-fonte, identificadores de linguagens, nomes de classes, métodos, propriedades, rotas de APIs, comandos de shell ou expressões literais.
 - **Protocolo de validação pré-escrita e pré-commit mandatório:**
   - Antes de salvar ou commitar qualquer Markdown, executar a pergunta de controle: *"Se esta expressão estivesse no meio de uma frase normal em português, essas palavras continuariam exigindo maiúscula?"*. Se a resposta for não, usar minúsculas.
   - Fazer uma varredura explícita em cada bloco gerado antes de salvar, convertendo para minúsculas qualquer palavra intermediária em negrito, parênteses ou microtítulo que não seja nome próprio, marca ou sigla.

4. **Uso correto de acentuação nos nomes de arquivos e títulos:**
 - Todos os arquivos Markdown (`.md`), títulos H1, cabeçalhos e frontmatter YAML devem utilizar obrigatoriamente a acentuação correta da língua portuguesa em seus nomes e textos (ex.: `01. Introdução à programação modular.md`, `02. Funções e procedimentos.md`, `Glossário de conceitos.md`).
 - Evitar a remoção artificial de acentos nos títulos das páginas e nomes de arquivos.

5. **Explicabilidade prática via técnica de Feynman:**
 - Toda explicação técnica ou conceitual deve empregar a **Técnica de Feynman**: usar linguagem simples, analogias intuitivas do mundo real e explicações passo a passo, desconstruindo a complexidade sem perder o rigor técnico.

## Organização e numeração de arquivos

6. **Padronização dos arquivos de resumo, consolidação bibliográfica e autores citados:**
 - O arquivo principal de resumo de qualquer disciplina deve obrigatoriamente utilizar o prefixo `00.` (ex.: `00. Design de Interacao - Resumo.md`, `00. Engenharia de Requisitos - Resumo.md`, `00. Programação modular - Resumo.md`).
 - **Consolidação obrigatória de bibliografia:** O arquivo de resumo `00.` deve conter obrigatoriamente a seção completa e consolidada de **Referências bibliográficas** (Bibliografia Básica e Complementar em normas ABNT com links de acesso), centralizando todas as referências mencionadas nos artigos individuais da matéria.
 - **Quadro histórico obrigatório de autores citados com links da Wikipedia:** O arquivo de resumo `00.` deve conter obrigatoriamente a seção **Autores e pioneiros citados na disciplina**, apresentada em formato de tabela Markdown contendo o nome do autor, sua contribuição central para a matéria, os artigos relacionados na disciplina e o link direto para seu perfil biográfico na Wikipedia.

7. **Numeração sequencial única:**
 - Todas as notas de conteúdo e tópicos dentro de uma disciplina devem seguir uma numeração sequencial estrita (01, 02, 03, ...).
 - É estritamente proibido haver números duplicados dentro do mesmo diretório.

8. **Manutenção contínua e interlinkagem exaustiva de sintaxe multilinguagem:**
 - Sempre que novos conceitos, termos técnicos ou definições fundamentais forem introduzidos na disciplina, o arquivo `Glossário de conceitos.md` do diretório da matéria deve ser obrigatoriamente atualizado.
 - Sempre que um novo trecho de código ou construção de linguagem for apresentado em qualquer nota de disciplina, deve-se obrigatoriamente:
   1. Atualizar ou criar a nota correspondente em `00. Sintaxe Multilinguagem/` com o comparativo multilinguagem (C#, Java, Python, JS), explicação linha por linha e analogia intuitiva (Feynman).
   2. **Interlinkagem exaustiva bidirecional:** Incluir links internos explícitos na nota da disciplina apontando diretamente para as notas de `00. Sintaxe Multilinguagem/` relevantes, e vice-versa (adicionar os tópicos das disciplinas na seção de `relacionados` e no corpo do texto do guia de sintaxe).

## Diretrizes para diagramas Mermaid

9. **Arquitetura visual e cognitiva para diagramas Mermaid:**
 - **Critério topológico de orientação (fim da regra rígida TD vs. LR):** Não há orientação universal pré-definida. A escolha entre `TD`, `LR` ou outra disposição deve seguir a topologia do conhecimento estudado:
   - *Processos e sequências temporais/lineares:* `LR` (para fluxos com poucas etapas encadeadas) ou `TD` (para fluxos longos ou com desvios).
   - *Hierarquias, árvores taxonômicas e herança:* `TD` como padrão estrutural.
   - *Comparações lado a lado e árvores conceituais:* Orientação balanceada pela proporção largura/profundidade para evitar diagramas excessivamente esticados.
   - *Dependências e grafos relacionais:* Orientação que minimize o cruzamento visual de arestas (*edge crossing*).
   - *Sistemas sistêmicos e interdisciplinares:* Preservar a visão de conjunto quando as conexões simultâneas agregarem valor cognitivo.
 - **Avaliação de complexidade relacional (sem limites numéricos rígidos):** Diagramas com muitos nós simples e bem espaçados são bem-vindos; diagramas com poucos nós hipercarregados de texto devem ser evitados. Avaliar sempre: densidade de arestas, cruzamentos, profundidade, tamanho dos rótulos e função didática.
 - **Visão global vs. detalhamento focal (estratégia de duas camadas):**
   - Para matérias ou modelos de alta complexidade (matriz GoF, arquiteturas, DER conceitual, mapas interdisciplinares), manter a **visão global integrada** para formação do modelo mental sistêmico.
   - Sempre que útil, complementar com **diagramas focais ou setoriais** que detalham subsistemas específicos logo abaixo.
 - **Nós como identificadores conceituais sintéticos:** Rótulos de nós devem ser sintéticos e objetivos. A explicação textual completa e detalhada pertence ao corpo do artigo, e não ao interior de caixas gráficas. Preservar apenas qualificadores indispensáveis para distinguir conceitos.
 - **Escolha semântica do tipo de diagrama:** Não forçar tudo para `flowchart`. Usar o tipo nativo Mermaid correspondente à natureza da informação:
   - `classDiagram` para modelagem orientada a objetos (classes, atributos, métodos, multiplicidade, herança e composição);
   - `erDiagram` para modelos conceituais/lógicos de banco de dados (entidades, atributos e relacionamentos com cardinalidades);
   - `sequenceDiagram` para interações temporais e troca de mensagens entre componentes;
   - `stateDiagram-v2` para máquinas de estados e transições de ciclo de vida;
   - `flowchart` para fluxogramas de controle, arquiteturas e mapas conceituais relacionais.
 - **Sistema semântico global de classes de estilo:** Em vez de declarar cores hexadecimais arbitrárias inline em cada diagrama, utilizar as classes padronizadas do vault (definidas no leitor web):
   - `:::core`: Conceito central, nó raiz ou elemento de maior relevância.
   - `:::component`: Módulo, classe concreta, componente ou bloco operacional regular.
   - `:::data`: Estrutura de dados, tabela/entidade de banco, payload ou estado.
   - `:::warning`: Exceção, ponto crítico de atenção, restrição ou erro.
   - `:::external`: Ator externo, terceiro, sistema legado ou fronteira de escopo.
 - **Proibição de diagramas em ASCII art:** Diagramas conceituais, pirâmides, caixas relacionais ou fluxos desenhados com caracteres de texto (`+---+`, `| |`, `----->`) são expressamente proibidos. Toda representação estrutural, arquitetural, relacional ou comportamental deve utilizar o tipo Mermaid nativo adequado ou tabelas nativas Markdown. Árvores de diretórios e arquivos de projeto (`tree`) são permitidas exclusivamente dentro de blocos de código (`text` ou `bash`).
 - **Anotação de cardinalidades e papéis sobre as linhas:** Em fluxogramas e modelos conceituais, especificações de cardinalidade `(min, max)` e papéis devem ser posicionados sobre as linhas de conexão (`---|"(min, max)"|`).
 - **Sintaxe padronizada e quebra suave de linhas:** Rótulos em `flowchart` devem ser delimitados por aspas duplas `Node["Texto<br>Conciso"]` para evitar quebras por pontuação.

## Links e navegação sequencial

10. **Encadeamento estrito de links de navegação e rolagem ao topo:**
 - Ao criar uma nova nota de tópico (`N. md`), é obrigatório verificar a nota imediatamente anterior (`N-1. md`) e atualizar ambas:
   - Na nota anterior (`N-1`), incluir/atualizar o link `**Próximo artigo:** [[N. Nome da Nova Nota]]`.
   - Na nova nota (`N`), incluir o link `**Artigo anterior:** [[N-1. Nome da Nota Anterior]]`.
 - Todas as notas de conteúdo de uma disciplina devem manter a cadeia completa e ininterrupta de navegação sequencial (`Artigo anterior` e `Próximo artigo`).
 - **Rolagem obrigatória ao topo:** Toda transição de artigo via links internos (`[[...]]`), botões de navegação, cards ou menus deve reposicionar o leitor obrigatoriamente no **topo exato da tela (`scroll(0, 0)`)**, garantindo que o início da leitura nunca fique cortado no meio do documento.

## Revisão de conteúdo e prompts de estudo

11. **Parâmetros de feedback e diagnóstico pedagógico de erros:**
 - Estrutura padronizada nos prompts de estudo para a LLM explicar erros com base em 6 dimensões taxonômicas:
   1. **Erro conceitual:** incompreensão do princípio teórico, invariante ou regra estrutural.
   2. **Erro terminológico:** confusão de nomenclaturas formais, padrões de mercado ou termos técnicos.
   3. **Erro de interpretação/leitura:** leitura incorreta ou desatenção aos requisitos e premissas do enunciado/cenário.
   4. **Erro de aplicação:** falha ao traduzir a teoria em modelagem ou na escolha de projeto.
   5. **Erro de sintaxe ou leitura de código:** engano na mecânica de linguagem, despacho ou execução.
   6. **Distração / desatenção:** equívoco circunstancial quando a fundamentação teórica já estava dominada.

## Preservação de marcações de estudo do usuário

12. **Preservação absoluta de highlights do Obsidian (`==texto==`):**
 - Toda marcação de destaque e grifo (`==texto==`) realizada pelo usuário em qualquer nota do vault é considerada **conteúdo crítico de estudo e aprendizado**.
 - É terminantemente proibido remover, sobrescrever ou limpar essas marcações durante qualquer refatoração, edição de código ou interlinkagem.
 - Todos os highlights manuais devem ser preservados integralmente e sincronizados com o GitHub.

## Diretrizes para apresentação de código didático

13. **Apresentação dual de código (exemplos atômicos + código completo integrado):**
 - Sempre que um tópico técnico envolver múltiplos conceitos de programação (ex.: classes, atributos, construtores, métodos, instanciação), o artigo deve apresentar obrigatoriamente duas formas de código:
   1. **Trechos atômicos e isolados:** Pequenos snippets de código demonstrando exatamente o conceito explicado logo abaixo de sua respectiva seção ou definição teórica (mostrando apenas a classe, apenas os atributos, apenas o construtor ou apenas a chamada).
   2. **Exemplo completo e integrado:** Um bloco de código integral, compilável e executável (com namespace, classe, construtor, métodos e função `Main`) que una todas as partes explicadas para demonstrar o fluxo completo em ação.

## Definição de terminologias do projeto

14. **Referência ao termo "App":**
 - Sempre que o usuário mencionar o termo **"app"** nas solicitações e conversas, refere-se exclusivamente à aplicação web / leitor de notas hospedado no GitHub Pages: `https://leorruas.github.io/puc`.

## Padronização de reuniões e aulas síncronas

15. **Inclusão obrigatória de data nos nomes e títulos de reuniões:**
 - Todas as notas de reuniões de orientação, encontros de equipe, alinhamentos e aulas inaugurais/síncronas devem conter obrigatoriamente a data do encontro no nome do arquivo e no título principal (`# H1`).
 - **Formato no nome do arquivo:** Inserir a data entre parênteses com hifens (ex.: `04. Reunião inicial da turma 5 (08-08-2026) - resumo e transcrição integral.md`, `05. Reunião de acompanhamento do grupo 4 (20-08-2026) - resumo e transcrição integral.md`, `Aula Inaugural (04-08-2026) - Resumo.md`).
 - **Formato no título H1 e metadados:** Inserir a data no título principal em formato `(DD/MM/AAAA)` e no bloco de metadados com destaque Obsidian `==DD/MM/AAAA==` (ex.: `# Reunião de acompanhamento do grupo 4 (20/08/2026): resumo e transcrição integral`).
 - **Manutenção de índices e leitor web:** Manter os nomes sincronizados no índice da disciplina (`00. ... - Resumo.md`), em `index.md` e no arquivo `script.js` (leitor web do GitHub Pages).

## Sincronização e versionamento

16. **Sincronização obrigatória com o GitHub:**
 - Sempre que qualquer arquivo for criado, modificado ou refatorado no vault ou no app web, as alterações devem ser obrigatoriamente commitadas e enviadas (*push*) para o repositório remoto no GitHub (`origin/main`).
 - Manter o repositório sempre sincronizado e atualizado a cada intervenção realizada.

## Tratamento de caracteres especiais e URLs no app web

17. **Tratamento obrigatório de caracteres especiais e codificação de URLs (`#`, `&`, `+`, acentos):**
 - O método nativo `encodeURI()` do JavaScript **não codifica** caracteres como o sustenido (`#`), pois o trata como fragmento/âncora de rota. Arquivos com termos de linguagens como `C#` no nome resultam em erro HTTP 404 ao buscar o conteúdo bruto no GitHub se a URL não estiver devidamente escapada.
 - **Padrão obrigatório de codificação:** Toda requisição `fetch` de arquivos brutos no `script.js` deve codificar cada segmento do caminho individualmente utilizando `encodeURIComponent` (ex.: `path.split("/").map(encodeURIComponent).join("/")`), garantindo que o `#` vire `%23`.
 - **Proteção de links internos com dunder / underlines:** Todos os links Obsidian (`[[...]]`) que contenham nomes com múltiplos *underlines* (como métodos mágicos `__eq__`, `__str__` ou atributos `_campo`) devem ser blindados antes do parser Markdown (`marked.js`) para evitar que a engine converta os *underlines* em tags HTML de negrito/itálico (`<strong>` ou `<em>`), quebrando a âncora de navegação.

## Conexões e interlinkagem qualitativa

18. **Interlinkagem qualitativa e conexões interdisciplinares relevantes:**
 - A interlinkagem deve priorizar relações intelectualmente úteis e significativas (pré-requisito, aprofundamento, modelo → código, teoria → prática, requisito → arquitetura), evitando ligações forçadas apenas pela ocorrência de palavras semelhantes.
 - Sempre que um conceito introduzido em uma disciplina possuir correspondência direta, analogia ou desdobramento prático em outra matéria (ex.: os relacionamentos `«include»` e `«extend»` da UML na Engenharia de Requisitos correspondendo a funções/sub-rotinas e tratamento de exceções/condicionais na Programação Modular e no Guia de Sintaxe; ou princípios SOLID e padrões de projeto conectando-se a modelagem de classes da UML e ao Projeto Integrador), deve-se obrigatoriamente:
   1. **Explicitar a ponte conceitual:** Inserir uma subseção dedicada explicando a analogia e o mapeamento entre o modelo teórico/arquitetural e a sua materialização em código.
   2. **Interlinkagem bidirecional estruturada:** Incluir links internos (`[[...]]`) conectando os artigos de todas as disciplinas envolvidas, atualizando o bloco `relacionados` do frontmatter YAML e o corpo das notas.
   3. **Visão holística do aprendizado:** Garantir que o estudante compreenda como os modelos conceituais (Engenharia de Requisitos, Design de Interação, Modelagem de Dados) se traduzem diretamente em código limpo, modular e de alta qualidade (Programação Modular, Guia de Sintaxe e Projeto Integrador).

## Integração de anotações de aula

19. **Integração e expansão contínua de anotações de aula do usuário:**
 - Sempre que o usuário fornecer anotações, transcrições ou tópicos brutos capturados durante suas aulas síncronas/assíncronas:
   1. **Verificação prévia:** Comparar os tópicos fornecidos com o conteúdo já existente no artigo da disciplina correspondente.
   2. **Integração completa sem perdas:** Incorporar todos os pontos, exemplos práticos mencionados pelo professor (ex.: tabelas de produtos duplicadas para vendas/compras/produção), sinônimos técnicos, ferramentas citadas (PostgreSQL, Oracle, MySQL, SQL Server, IBM Db2, Firebird), links de materiais complementares e capítulos de bibliografia.
   3. **Expansão didática Feynman:** Expandir os tópicos em linguagem simples, modelos mentais intuitivos, diagramas Mermaid verticais (`flowchart TD`) e tabelas comparativas nativas de Markdown.
   4. **Sincronização imediata:** Atualizar os arquivos relacionados, o `Glossário de conceitos.md` (se novos termos surgirem), o resumo `00.` e sincronizar via Git (`push`).

## Princípios de maturação e arquitetura do vault

20. **Preservação do desenvolvimento incremental e não-enciclopedismo:**
 - O vault é construído de forma estritamente incremental ao longo do semestre acadêmico: cada disciplina amadurece conforme o aluno assiste às aulas, lê os materiais didáticos da PUC Minas, realiza exercícios práticos e identifica lacunas reais de estudo.
 - Diferenças de maturidade e profundidade entre disciplinas são esperadas e legítimas (disciplinas como Programação Modular estão avançadas porque os estudos avançaram primeiro nelas).
 - **Proibição de preenchimento artificial:** É terminantemente proibido gerar artigos antecipadamente apenas para preencher pastas, unidades ou ementas de matérias pouco desenvolvidas com conteúdo genérico.
 - **Critério de relevância didática:** O acervo não deve se transformar em enciclopédia genérica. Antes de acrescentar qualquer conteúdo, responder: *"Isso melhora a compreensão de algo que o aluno está estudando no curso de ADS da PUC Minas ou apenas torna a nota maior?"*. Se for apenas expansão enciclopédica desvinculada do momento acadêmico, não deve ser adicionado.

21. **Distinção editorial entre conteúdo da PUC e complementação didática:**
 - As notas devem manter clareza editorial sobre a origem do conhecimento, permitindo identificar com sobriedade quando uma informação é proveniente da ementa e aulas da PUC Minas, quando é complementação técnica/aprofundamento externo ou quando se trata de metáfora pedagógica (Técnica de Feynman).
 - Essa distinção deve ser feita de forma elegante e limpa, utilizando o parágrafo de `> **Contexto:**` no início da nota, cabeçalhos de seção objetivos (ex.: *As analogias de Feynman*, *Ponte conceitual*, *Aprofundamento técnico*) ou notas de rodapé pontuais, evitando sobrecarregar o texto com banners ou avisos repetitivos.




