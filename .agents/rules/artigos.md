# Regras de resposta e armazenamento: artigos técnicos

1. **Metodologia Feynman de explicação (Obrigatório):**
 - Todo artigo deve seguir os 4 passos da **Metodologia Feynman**:
 1. **Conceito em linguagem simples e intuição:** explicar a ideia central como se estivesse ensinando para uma criança ou leigo, usando analogias do cotidiano antes do jargão técnico.
 2. **Identificação de lacunas e simplificação:** detalhar o conceito com precisão técnica sem perder a clareza, desconstruindo termos complexos.
 3. **Exemplos práticos e reais:** sempre ancorar o conceito em casos do mundo real e código/diagramas concretos.
 4. **Síntese e revisão:** concluir com uma síntese direta do aprendizado que consolida o conhecimento intuitivo e formal.
2. **Formato do conteúdo:** Sempre que o usuário solicitar explicações, conceitos ou conteúdos teóricos, o agente deve responder/salvar o conteúdo estruturado no formato de **artigos técnicos completos**, claros e bem fundamentados.
3. **Proibição estrita de emojis:** É **estritamente proibido utilizar emojis** no texto dos artigos, nos títulos de arquivos, nos resumos, nos cabeçalhos ou nas respostas do chat. O tom do material deve ser profissional, limpo e puramente técnico.
4. **Capitalização em português (Capitalization / Sentence Case):**
 - Todos os títulos em português (título do arquivo, títulos `# H1`, `## H2`, `### H3`, etc.), bem como itens de listas e conteúdos após dois-pontos (`:`), devem usar estilo de frase (*sentence case*): **somente a primeira letra da frase/título começa em maiúsculo**.
 - As demais palavras continuam em minúsculo, a menos que sejam nomes próprios ou siglas (ex.: *UML*, *IEEE*, *Uber*, *Google*, *BPMN*, *PCI-DSS*).
 - Após dois-pontos (`:`), a primeira letra continua em minúsculo, exceto se for um nome próprio ou sigla.
 - Exemplo de título de arquivo: `02. Engenharia de requisitos e negócios - o alinhamento estratégico.md`
5. **Ordem pedagógica e renumeração ativa (Obrigatório):**
 - Antes de salvar ou criar qualquer artigo, o agente DEVE avaliar criticamente onde o tema se encaixa no **encadeamento lógico e didático do aprendizado** (trilha de aprendizado).
 - Se um novo artigo for um conceito fundamental que precede tópicos já criados, o agente DEVE renumerar os arquivos existentes para manter a ordem lógica.
6. **Padrão de nomenclatura de arquivos e links:**
 - O nome do arquivo **não** deve conter a palavra "artigo".
 - O nome do arquivo deve começar com a numeração sequencial formatada como `01. `, `02. `, `03. `, etc.
 - O título do arquivo deve usar espaços normais (sem *underscores* `_`).
 - **Proibição estrita de dois-pontos (`:`) em nomes de arquivos:** É **estritamente proibido** utilizar dois-pontos (`:`) no nome do arquivo ou nos links `[[WikiLinks]]`. Utilize hífen com espaços (` - `) para separar títulos e subtítulos.
 - Exemplo correto: `01. Ods 4 educação de qualidade - conceito, metas e fundamentação.md`
7. **Localização dos arquivos:** 
 - Todos os artigos devem ser salvos obrigatoriamente dentro da pasta da disciplina correspondente na estrutura da PUC (ex.: `/Users/leoruas/Library/Mobile Documents/iCloud~md~obsidian/Documents/puc/07. Engenharia de Requisitos/`).
8. **Interconexão com busca ativa e metadados YAML (Obsidian Links & Frontmatter):**
 - **Busca prévia por links internos (Obrigatório):** Antes de escrever qualquer artigo, o agente DEVE pesquisar ativamente no vault por termos e notas existentes para hiperlinkar.
 - Todos os artigos gerados **devem conter um bloco de cabeçalho YAML (Frontmatter)** no início do arquivo com metadados estruturados (`title`, `disciplina`, `modulo`, `tags`, `relacionados`).
 - O corpo do artigo deve utilizar **Wikilinks nativos do Obsidian (`[[Nome da Nota]]`)** ao máximo.
 - Todo novo artigo deve ter seus links internos integrados de volta no arquivo de resumo da disciplina.
