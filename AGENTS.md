# Regras Gerais do Vault

## Estilo de Formatação e Escrita

1. **Proibição Estrita de Emojis:**
 - É estritamente proibido utilizar emojis em qualquer arquivo Markdown (`.md`), cabeçalhos, tabelas, títulos de notas, listas ou respostas.
 - Todo o conteúdo deve ser mantido em tom profissional, técnico e limpo.

2. **Destaque de Datas em Cronogramas:**
 - Todas as datas e períodos em cronogramas, prazos de entrega e calendários devem ser destacados obrigatoriamente utilizando a sintaxe de highlight do Obsidian (`DD/MM/AAAA`).

3. **Capitalização Frasal (Sentence Case):**
 - Em títulos, cabeçalhos, subcabeçalhos, listas e itens em negrito, utilizar capitalização frasal (*sentence case*), com apenas a primeira palavra em maiúscula (exceto para nomes próprios, acrônimos ou siglas). Evitar o uso de *Title Case* (capitalização de todas as palavras).

4. **Uso Correto de Acentuação nos Nomes de Arquivos e Títulos:**
 - Todos os arquivos Markdown (`.md`), títulos H1, cabeçalhos e frontmatter YAML devem utilizar obrigatoriamente a acentuação correta da língua portuguesa em seus nomes e textos (ex.: `01. Introdução à programação modular.md`, `02. Funções e procedimentos.md`, `Glossário de conceitos.md`).
 - Evitar a remoção artificial de acentos nos títulos das páginas e nomes de arquivos.

5. **Explicabilidade Prática via Técnica de Feynman:**
 - Toda explicação técnica ou conceitual deve empregar a **Técnica de Feynman**: usar linguagem simples, analogias intuitivas do mundo real e explicações passo a passo, desconstruindo a complexidade sem perder o rigor técnico.

## Organização e Numeração de Arquivos

6. **Padronização dos Arquivos de Resumo:**
 - O arquivo principal de resumo de qualquer disciplina deve obrigatoriamente utilizar o prefixo `00.` (ex.: `00. Design de Interacao - Resumo.md`, `00. Engenharia de Requisitos - Resumo.md`, `00. Programação modular - Resumo.md`).

7. **Numeração Sequencial Única:**
 - Todas as notas de conteúdo e tópicos dentro de uma disciplina devem seguir uma numeração sequencial estrita (01, 02, 03, ...).
 - É estritamente proibido haver números duplicados dentro do mesmo diretório.

8. **Manutenção Contínua e Interlinkagem Exaustiva de Sintaxe Multilinguagem:**
 - Sempre que novos conceitos, termos técnicos ou definições fundamentais forem introduzidos na disciplina, o arquivo `Glossário de conceitos.md` do diretório da matéria deve ser obrigatoriamente atualizado.
 - Sempre que um novo trecho de código ou construção de linguagem for apresentado em qualquer nota de disciplina, deve-se obrigatoriamente:
   1. Atualizar ou criar a nota correspondente em `00. Sintaxe Multilinguagem/` com o comparativo multilinguagem (C#, Java, Python, JS), explicação linha por linha e analogia intuitiva (Feynman).
   2. **Interlinkagem Exaustiva Bidirecional:** Incluir links internos explícitos na nota da disciplina apontando diretamente para as notas de `00. Sintaxe Multilinguagem/` relevantes, e vice-versa (adicionar os tópicos das disciplinas na seção de `relacionados` e no corpo do texto do guia de sintaxe).

## Diretrizes para Diagramas Mermaid

9. **Otimização Estrita de Leiturabilidade e Layout Visual Vertical:**
 - **Orientação Vertical Obrigatória:** utilizar exclusivamente `flowchart TD`. É terminantemente proibido o uso de `graph LR` ou qualquer disposição que force mais de 2 nós lado a lado.
 - **Empilhamento Vertical em `subgraph`:** fluxos com mais de 2 ramificações devem ser organizados obrigatoriamente em `subgraph` verticais empilhados (um abaixo do outro), evitando que o Mermaid expanda a largura da imagem e reduza o tamanho da fonte.
 - **Quebra Obrigatória de Linhas (`<br>`):** todo rótulo de nó com mais de 2 palavras deve conter `<br>` a cada 2 ou 3 palavras para garantir caixas estreitas e compactas.
 - **Sintaxe Padronizada:** envolver todos os textos de rótulos de nós entre aspas duplas `Node["Texto com<br>Quebra"]` para evitar erros de renderização com caracteres especiais.

## Links e Navegação Sequencial

10. **Encadeamento Estrito de Links de Navegação e Rolagem ao Topo:**
 - Ao criar uma nova nota de tópico (`N. md`), é obrigatório verificar a nota imediatamente anterior (`N-1. md`) e atualizar ambas:
   - Na nota anterior (`N-1`), incluir/atualizar o link `**Próximo artigo:** [[N. Nome da Nova Nota]]`.
   - Na nova nota (`N`), incluir o link `**Artigo anterior:** [[N-1. Nome da Nota Anterior]]`.
 - Todas as notas de conteúdo de uma disciplina devem manter a cadeia completa e ininterrupta de navegação sequencial (`Artigo anterior` e `Próximo artigo`).
 - **Rolagem Obrigatória ao Topo:** Toda transição de artigo via links internos (`[[...]]`), botões de navegação, cards ou menus deve reposicionar o leitor obrigatoriamente no **topo exato da tela (`scroll(0, 0)`)**, garantindo que o início da leitura nunca fique cortado no meio do documento.

## Revisão de Conteúdo e Prompts de Estudo

   - **Parâmetros de Feedback e Diagnóstico de Erros:** estrutura padronizada para a LLM explicar o tipo de erro cometido (conceitual, leitura, terminologia ou aplicação) e razões do gabarito.

## Preservação de Marcações de Estudo do Usuário

12. **Preservação Absoluta de Highlights do Obsidian (`==texto==`):**
 - Toda marcação de destaque e grifo (`==texto==`) realizada pelo usuário em qualquer nota do vault é considerada **conteúdo crítico de estudo e aprendizado**.
 - É terminantemente proibido remover, sobrescrever ou limpar essas marcações durante qualquer refatoração, edição de código ou interlinkagem.
 - Todos os highlights manuais devem ser preservados integralmente e sincronizados com o GitHub.
