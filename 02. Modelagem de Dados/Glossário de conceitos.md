---
title: "Glossário de conceitos: modelagem de dados"
disciplina: "02. Modelagem de Dados"
modulo: "Referência geral"
tags:
  - modelagem-de-dados
  - glossario
  - conceitos-fundamentais
  - banco-de-dados
relacionados:
  - "[[00. Modelagem de Dados - Resumo]]"
  - "[[01. Introdução à modelagem de dados e sua importância]]"
  - "[[02. Abordagem de arquivos vs. abordagem de banco de dados]]"
---

# Glossário de conceitos: modelagem e projeto de bancos de dados

> **Contexto:** Dicionário terminológico e conceitual consolidado da disciplina de Modelagem de Dados, reunindo definições formais, modelos mentais, papéis arquiteturais e analogias didáticas.

---

## Índice alfabético

* [[#A|A]]: [[#Abstração de dados|Abstração de dados]], [[#Anomalia de modificação|Anomalia de modificação]], [[#Arquitetura ANSI/SPARC|Arquitetura ANSI/SPARC]], [[#Atributo|Atributo]]
* [[#B|B]]: [[#Banco de Dados (BD)|Banco de Dados (BD)]]
* [[#C|C]]: [[#Catálogo do sistema (Dicionário de dados)|Catálogo do sistema (Dicionário de dados)]], [[#Chave estrangeira (FK)|Chave estrangeira (FK)]], [[#Chave primária (PK)|Chave primária (PK)]], [[#Conhecimento|Conhecimento]]
* [[#D|D]]: [[#Dado|Dado]], [[#Dependência lógica e física|Dependência lógica e física]], [[#Diagrama Entidade-Relacionamento (DER)|Diagrama Entidade-Relacionamento (DER)]]
* [[#E|E]]: [[#Entidade|Entidade]]
* [[#I|I]]: [[#Independência física de dados|Independência física de dados]], [[#Independência lógica de dados|Independência lógica de dados]], [[#Informação|Informação]], [[#Integridade referencial|Integridade referencial]]
* [[#M|M]]: [[#Modelagem de dados|Modelagem de dados]], [[#Modelo conceitual|Modelo conceitual]], [[#Modelo físico|Modelo físico]], [[#Modelo lógico|Modelo lógico]], [[#Modelo relacional|Modelo relacional]]
* [[#P|P]]: [[#Perda de atualização (Lost update)|Perda de atualização (Lost update)]], [[#Propriedades ACID|Propriedades ACID]]
* [[#R|R]]: [[#Redundância de dados|Redundância de dados]], [[#Relacionamento|Relacionamento]]
* [[#S|S]]: [[#Sistema de Banco de Dados (SBD)|Sistema de Banco de Dados (SBD)]], [[#Sistema Gerenciador de Banco de Dados (SGBD)|Sistema Gerenciador de Banco de Dados (SGBD)]]
* [[#T|T]]: [[#Transação|Transação]]
* [[#V|V]]: [[#Visão (View)|Visão (View)]]

---

## A

### Abstração de dados
* **Definição formal:** O processo de ocultar detalhes operacionais e físicos de baixo nível sobre como os dados são armazenados na máquina, expondo apenas as estruturas essenciais e a semântica necessária para usuários e aplicações.
* **Modelo mental / Feynman:** É como o painel de um automóvel. O motorista só precisa enxergar o velocímetro, o marcador de combustível e os pedais, sem precisar saber a quantidade de injeção eletrônica de combustível ocorrendo no motor a cada segundo.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

### Anomalia de modificação
* **Definição formal:** Inconsistências indesejadas que ocorrem em tabelas mal projetadas ou não normalizadas durante operações de inserção, alteração ou exclusão de registros.
* **Tipos:**
  - *Anomalia de inserção:* Impossibilidade de registrar um fato sem registrar outro fato não relacionado.
  - *Anomalia de exclusão:* Perda indesejada de dados essenciais ao apagar um registro secundário.
  - *Anomalia de alteração:* Necessidade de atualizar o mesmo dado em múltiplos registros, correndo o risco de inconsistência.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

### Arquitetura ANSI/SPARC
* **Definição formal:** Padrão arquitetural tripartite para sistemas de bancos de dados proposto pelo comitê ANSI/X3/SPARC em 1975, que divide o sistema em três níveis de esquemas: externo (visões do usuário), conceitual (estrutura lógica global e regras de negócio) e interno/físico (alocação e estruturas de arquivos).
* **Objetivo principal:** Garantir a independência total entre dados lógicos e o armazenamento físico em disco.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

### Atributo
* **Definição formal:** Propriedade, característica ou elemento descritivo associado a uma entidade ou a um relacionamento.
* **Modelo mental:** Se a entidade for o substantivo "Aluno", os atributos são os adjetivos e dados cadastrais: `Matrícula`, `Nome`, `CPF` e `Data de Nascimento`.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

---

## B

### Banco de Dados (BD)
* **Definição formal:** (*Database*) Coleção estruturada, integrada e logicamente coerente de dados correlacionados que modelam e representam entidades e eventos de um domínio do mundo real (*mini-mundo*).
* **Modelo mental / Feynman:** É o acervo de livros organizado nas estantes de uma biblioteca, contendo todas as obras e registros da instituição.
* **Artigo correspondente:** [[02. Abordagem de arquivos vs. abordagem de banco de dados]]

---

## C

### Catálogo do sistema (Dicionário de dados)
* **Definição formal:** Repositório interno e autocontido do SGBD que armazena os metadados — a descrição formal da estrutura, tabelas, colunas, tipos de dados, restrições de integridade e permissões de segurança de todo o banco de dados.
* **Artigo correspondente:** [[02. Abordagem de arquivos vs. abordagem de banco de dados]]

### Chave estrangeira (FK)
* **Definição formal:** (*Foreign Key*) Um atributo ou conjunto de atributos em uma tabela que faz referência direta à chave primária (PK) de outra tabela (ou da mesma tabela), estabelecendo e assegurando um vínculo relacional entre os registros.
* **Papel:** Garantir a integridade referencial, impedindo registros órfãos.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

### Chave primária (PK)
* **Definição formal:** (*Primary Key*) Um identificador único e irredutível escolhido para individualizar de forma inequívoca cada tupla (linha/registro) dentro de uma tabela relacional. Uma chave primária nunca pode aceitar valores nulos (`NOT NULL`) nem repetidos (`UNIQUE`).
* **Modelo mental:** É o CPF ou o número de chassi de um veículo no banco de dados.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

### Conhecimento
* **Definição formal:** A integração de informações contextualizadas com regras de negócio, experiência humana, princípios analíticos e heurísticas, capacitando a tomada de decisões estratégicas e ações fundamentadas.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

---

## D

### Dado
* **Definição formal:** Um valor ou registro atômico e bruto, desprovido de contexto, semântica ou interpretação inerente.
* **Modelo mental:** O número isolado `42` anotado em um papel solto.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

### Dependência lógica e física
* **Definição formal:** Acoplamento indesejável presente nos sistemas de arquivos legados, onde qualquer alteração no formato de gravação dos dados exigia a reescrita de todos os programas consumidores.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[02. Abordagem de arquivos vs. abordagem de banco de dados]]

### Diagrama Entidade-Relacionamento (DER)
* **Definição formal:** Notação gráfica e formal criada por Peter Chen em 1976 para representar o modelo conceitual de dados por meio de retângulos (entidades), losangos (relacionamentos) e elipses/linhas (atributos).
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

---

## E

### Entidade
* **Definição formal:** Qualquer objeto, conceito, evento ou elemento do mundo real com existência distinta e sobre o qual o sistema necessita armazenar dados. Pode ser concreta (ex.: `Cliente`, `Livro`) ou abstrata (ex.: `Empréstimo`, `Matrícula`, `Voo`).
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

---

## I

### Independência física de dados
* **Definição formal:** Capacidade de modificar o esquema físico (como trocar o disco por SSD, mudar o tipo de índice de B-Tree para Hash ou reorganizar partições de arquivos) sem precisar alterar o esquema conceitual, o modelo lógico ou os programas de aplicação.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

### Independência lógica de dados
* **Definição formal:** Capacidade de alterar o esquema conceitual (como adicionar novas tabelas, novos atributos ou novas regras) sem que as aplicações existentes que não utilizam esses novos dados precisem ser reescritas ou recompiladas.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

### Informação
* **Definição formal:** O dado bruto estruturado, processado, rotulado e associado a um significado e contexto claro, tornando-o interpretável pelo ser humano e pelo sistema.
* **Modelo mental:** "A temperatura do sensor 04 atingiu 39.5 °C às 10h".
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

### Integridade referencial
* **Definição formal:** Regra fundamental de consistência relacional que estabelece que o valor de uma chave estrangeira em uma tabela deve corresponder obrigatoriamente a uma chave primária válida existente na tabela pai referenciada, ou ser nulo (quando permitido).
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[02. Abordagem de arquivos vs. abordagem de banco de dados]]

---

## M

### Modelagem de dados
* **Definição formal:** O conjunto sistemático de conceitos, técnicas, processos e notações gráficas utilizados para abstrair, estruturar, definir e documentar os requisitos de dados e as regras de negócio de um domínio, desde a concepção abstrata até o esquema físico no banco de dados.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

### Modelo conceitual
* **Definição formal:** A representação abstrata de mais alto nível dos dados de um sistema, focada exclusivamente nas regras de negócio e no que existe no mundo real, completamente independente de qualquer SGBD ou detalhe de implementação computacional.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

### Modelo físico
* **Definição formal:** A especificação técnica de mais baixo nível, detalhando como os dados são implementados e alocados fisicamente no hardware e no SGBD específico, incluindo arquivos de dados, índices, tablespaces e parâmetros de armazenamento.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

### Modelo lógico
* **Definição formal:** A representação intermediária dos dados adaptada a um paradigma de banco de dados específico (geralmente o modelo relacional), descrevendo tabelas, colunas, chaves primárias e estrangeiras, tipos de dados e cardinalidades, sem descer aos detalhes de alocação física em disco.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

### Modelo relacional
* **Definição formal:** Modelo formal de banco de dados introduzido por Edgar F. Codd em 1970, baseado na teoria matemática dos conjuntos e na lógica de predicados de primeira ordem, onde todos os dados são representados na forma de relações (tabelas bidimensionais com linhas e colunas).
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

---

## P

### Perda de atualização (Lost update)
* **Definição formal:** Falha crítica de concorrência que ocorre quando duas transações leem o mesmo registro simultaneamente e ambas gravam alterações baseadas no valor lido, fazendo com que a última gravação sobrescreva e destrua silenciosamente a alteração realizada pela primeira.
* **Artigo correspondente:** [[02. Abordagem de arquivos vs. abordagem de banco de dados]]

### Propriedades ACID
* **Definição formal:** Conjunto de quatro propriedades fundamentais que garantem a confiabilidade de transações em um SGBD:
  - **A (Atomicidade):** A transação é indivisível; ou todas as suas operações são confirmadas com sucesso (*commit*), ou nenhuma é aplicada (*rollback*).
  - **C (Consistência):** A transação leva o banco de um estado válido a outro estado igualmente válido, respeitando todas as regras e restrições.
  - **I (Isolamento):** Transações simultâneas são executadas como se fossem as únicas no sistema, sem interferência mútua antes da confirmação.
  - **D (Durabilidade):** Uma vez confirmada a transação, suas alterações são permanentes e não serão perdidas mesmo em caso de falha de energia ou travamento do servidor.
* **Artigo correspondente:** [[02. Abordagem de arquivos vs. abordagem de banco de dados]]

---

## R

### Redundância de dados
* **Definição formal:** A repetição desnecessária do mesmo dado em múltiplos locais da base de dados, gerando desperdício de espaço de armazenamento e criando risco crítico de inconsistência.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[02. Abordagem de arquivos vs. abordagem de banco de dados]]

### Relacionamento
* **Definição formal:** Associação semântica e lógica entre duas ou mais entidades do modelo de dados, refletindo como elas interagem nas regras de negócio do mundo real (ex.: um `Aluno` *cursa* uma `Disciplina`).
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

---

## S

### Sistema de Banco de Dados (SBD)
* **Definição formal:** O ecossistema integrado completo composto pelo Banco de Dados, o Sistema Gerenciador de Banco de Dados (SGBD), as aplicações clientes de software, a infraestrutura de hardware e as pessoas (administradores de banco DBA, desenvolvedores e usuários finais).
* **Artigo correspondente:** [[02. Abordagem de arquivos vs. abordagem de banco de dados]]

### Sistema Gerenciador de Banco de Dados (SGBD)
* **Definição formal:** (*DBMS - Database Management System*) O software de sistema responsável por gerenciar, controlar, proteger, consultar e manter bancos de dados, fornecendo interfaces padronizadas para definição (DDL), manipulação (DML) e controle (DCL) dos dados.
* **Modelo mental / Feynman:** É o bibliotecário-chefe de uma grande biblioteca, responsável por catalogar os livros, controlar os empréstimos, impedir furtos e garantir a organização do acervo.
* **Exemplos:** PostgreSQL, MySQL, Microsoft SQL Server, Oracle Database, SQLite.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[02. Abordagem de arquivos vs. abordagem de banco de dados]]

---

## T

### Transação
* **Definição formal:** Uma unidade lógica de processamento que inclui uma ou mais operações de acesso ao banco de dados (como leitura, inserção, alteração ou exclusão) que devem ser executadas com garantia estrita das propriedades ACID.
* **Modelo mental:** Uma transferência bancária de R$ 100 da conta A para a conta B. A operação exige subtrair R$ 100 de A e somar R$ 100 em B. Se a energia cair após subtrair de A, o sistema desfaz o débito para não sumir com o dinheiro do cliente.
* **Artigo correspondente:** [[02. Abordagem de arquivos vs. abordagem de banco de dados]]

---

## V

### Visão (View)
* **Definição formal:** Uma tabela virtual baseada no conjunto de resultados de uma consulta SQL pré-definida. Não armazena dados fisicamente (exceto no caso de visões materializadas), mas fornece uma janela customizada e segura sobre as tabelas subjacentes.
* **Papel:** Simplificar consultas complexas e restringir o acesso a colunas sensíveis para perfis específicos de usuários.
* **Artigo correspondente:** [[02. Abordagem de arquivos vs. abordagem de banco de dados]]

---

## Artigos relacionados e navegação

* **Voltar ao artigo 01:** [[01. Introdução à modelagem de dados e sua importância]]
* **Voltar ao artigo 02:** [[02. Abordagem de arquivos vs. abordagem de banco de dados]]
* **Resumo da disciplina:** [[00. Modelagem de Dados - Resumo]]
* **Índice geral do vault:** [[index.md|Página Inicial do Vault]]
