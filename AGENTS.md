# Regras Gerais do Vault

## Estilo de Formatação e Escrita

1. **Proibição Estrita de Emojis:**
 - É estritamente proibido utilizar emojis em qualquer arquivo Markdown (`.md`), cabeçalhos, tabelas, títulos de notas, listas ou respostas.
 - Todo o conteúdo deve ser mantido em tom profissional, técnico e limpo.

2. **Destaque de Datas em Cronogramas:**
 - Todas as datas e períodos em cronogramas, prazos de entrega e calendários devem ser destacados obrigatoriamente utilizando a sintaxe de highlight do Obsidian (`DD/MM/AAAA`).

3. **Capitalização Frasal (Sentence Case):**
 - Em títulos, cabeçalhos, subcabeçalhos, listas e itens em negrito, utilizar capitalização frasal (*sentence case*), com apenas a primeira palavra em maiúscula (exceto para nomes próprios, acrônimos ou siglas). Evitar o uso de *Title Case* (capitalização de todas as palavras).

## Organização e Numeração de Arquivos

4. **Padronização dos Arquivos de Resumo:**
 - O arquivo principal de resumo de qualquer disciplina deve obrigatoriamente utilizar o prefixo `00.` (ex.: `00. Design de Interacao - Resumo.md`, `00. Engenharia de Requisitos - Resumo.md`).

5. **Numeração Sequencial Única:**
 - Todas as notas de conteúdo e tópicos dentro de uma disciplina devem seguir uma numeração sequencial estrita (01, 02, 03, ...).
 - É estritamente proibido haver números duplicados dentro do mesmo diretório.

## Diretrizes para Diagramas Mermaid

6. **Otimização de Leiturabilidade e Layout Visual:**
 - **Orientação Preferencial:** utilizar preferencialmente orientação vertical (`graph TD` ou `flowchart TD`). Evitar gráficos horizontais muito extensos (`graph LR`) com mais de 3 nós alinhados, pois reduzem o tamanho da fonte em telas menores.
 - **Quebra de Linhas em Nós:** utilizar a tag `<br>` em rótulos de nós que possuam mais de 3 ou 4 palavras para evitar caixas excessivamente largas.
 - **Organização por Subgráficos:** estruturar fluxos longos ou complexos em `subgraph` verticais empilhados.
 - **Sintaxe Padronizada:** envolver todos os textos de rótulos de nós entre aspas duplas `Node["Texto"]` para evitar erros de sintaxe com caracteres especiais.
