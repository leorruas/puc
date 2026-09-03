# Diretrizes de estilo e formatação do vault

Regras consolidadas para o desenvolvimento e manutenção das notas no Obsidian Vault:

1. **Protocolo de validação de títulos e links**: Realizar verificação ativa de integridade de links internos (`[[...]]`) e de capitalização (*sentence case*) a cada criação ou edição de arquivo Markdown.
2. **Capitalização estrita em português (Sentence Case)**: Títulos e subcabeçalhos (incluindo termos após dois-pontos `:`) devem ser rigorosamente em minúsculas (ex: "1. Introdução à programação modular: da construção algorítmica à gestão do estado"), exceto a primeira palavra do título e nomes próprios de marcas/tecnologias/siglas.
3. **Registro de histórico em `log.md` (ordem decrescente)**: Registrar obrigatoriamente todas as criações, edições, movimentações de arquivos e reorganizações no arquivo `log.md` na raiz do vault, com as entradas mais recentes no topo.
4. **Links protegidos em tabelas**: Em tabelas Markdown, usar sempre `\|` para rótulos de wikilinks (ex: `[[01. Programacao Modular/01. Introdução à programação modular\|Introdução]]`) evitando a quebra de colunas pelo separador `|`.
5. **Método Feynman**: Explicar conceitos técnicos através de analogias simples do mundo real, modelos mentais didáticos e intuitivos.
6. **Interlinkagem qualitativa e conexões interdisciplinares**: Priorizar links internos com significado intelectual claro (pré-requisito, conceito → exemplo, teoria → prática, modelagem → código), evitando enlaces superficiais.
7. **Sem emojis**: Manter a estética do vault estritamente textual, profissional e sem emojis.
8. **Preservação de highlights (`==texto==`)**: Preservar integralmente todas as marcações de grifo realizadas pelo usuário em arquivos do vault.
