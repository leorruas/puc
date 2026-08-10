# Log de alterações do vault

Este arquivo registra o histórico de criações, modificações, edições e reorganizações estruturais realizadas no vault em **ordem cronológica decrescente (mais recente no topo)**.

---

## 2026-08-02

* **Instalação de Dependência**: Instalação do .NET 8.0 SDK
 * Executado instalador local para configurar o .NET SDK 8.0.423 em `~/.dotnet/` permitindo compilação e execução de C# no ambiente local.

* **Criação de Código e Nota**: Introdução a C# e Arrays
 * Criação do código [[04. Algoritmos e Estruturas de Dados/SomaDoisNumeros.cs\|SomaDoisNumeros.cs]] que lê dois números e exibe a soma.
 * Criação da nota explicativa [[04. Algoritmos e Estruturas de Dados/Recordando C# e arrays.md\|Recordando C# e arrays.md]] detalhando compiladores, tipagem e arrays usando o Método Feynman.
 * Atualização da nota principal [[04. Algoritmos e Estruturas de Dados/04. Algoritmos e Estruturas de Dados - Resumo.md\|Algoritmos e Estruturas de Dados - Resumo]] para referenciar os novos arquivos.

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
 * Criação das notas de resumo individuais para cada disciplina (ex: `01. Programacao Modular - Resumo.md`) e guias específicos de prompt de estudo com LLM (`Prompts de Estudo (LLM).md`), estruturados didaticamente de acordo com o Método Feynman.
 * Execução do pós-processamento para remoção de emojis de todo o vault para cumprir a Regra 8 de estética estritamente textual.
