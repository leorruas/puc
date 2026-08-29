# Log de alterações do vault

Este arquivo registra o histórico de criações, modificações, edições e reorganizações estruturais realizadas no vault em **ordem cronológica decrescente (mais recente no topo)**.

---

## 2026-08-29

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
