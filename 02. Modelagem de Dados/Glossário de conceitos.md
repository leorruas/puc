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
  - "[[03. Linguagens de banco de dados (ddl e dml) e perfis profissionais]]"
  - "[[04. Níveis do sgbd e etapas do projeto de banco de dados]]"
  - "[[05. Modelagem de entidades e tipos de atributos]]"
  - "[[06. Modelagem de relacionamentos, cardinalidade e restrições de participação]]"
  - "[[07. Modelo de entidades e relacionamentos estendido]]"
---

# Glossário de conceitos: modelagem e projeto de bancos de dados

> **Contexto:** Dicionário terminológico e conceitual consolidado da disciplina de Modelagem de Dados, reunindo definições formais, modelos mentais, papéis arquiteturais e analogias didáticas.

---

## Índice alfabético

* [[#A|A]]: [[#Abstração de dados|Abstração de dados]], [[#Administrador de Banco de Dados (DBA)|Administrador de Banco de Dados (DBA)]], [[#Administrador de Dados (AD)|Administrador de Dados (AD)]], [[#Anomalia de modificação|Anomalia de modificação]], [[#Arquitetura ANSI/SPARC|Arquitetura ANSI/SPARC]], [[#Atores do banco de dados|Atores do banco de dados]], [[#Atributo|Atributo]], [[#Atributo Armazenado (Base)|Atributo Armazenado (Base)]], [[#Atributo Chave (Identificador)|Atributo Chave (Identificador)]], [[#Atributo Complexo|Atributo Complexo]], [[#Atributo Composto|Atributo Composto]], [[#Atributo Derivado (Calculado)|Atributo Derivado (Calculado)]], [[#Atributo Monovalorado (Univalorado)|Atributo Monovalorado (Univalorado)]], [[#Atributo Multivalorado|Atributo Multivalorado]], [[#Atributo Nulo (Opcional)|Atributo Nulo (Opcional)]], [[#Atributo Obrigatório|Atributo Obrigatório]], [[#Atributo Simples (Atômico)|Atributo Simples (Atômico)]], [[#Autorrelacionamento|Autorrelacionamento]]
* [[#B|B]]: [[#Banco de Dados (BD) / Base de dados|Banco de Dados (BD) / Base de dados]]
* [[#C|C]]: [[#Cardinalidade Máxima|Cardinalidade Máxima]], [[#Cardinalidade Mínima|Cardinalidade Mínima]], [[#Catálogo do sistema (Dicionário de dados)|Catálogo do sistema (Dicionário de dados)]], [[#Chave estrangeira (FK)|Chave estrangeira (FK)]], [[#Chave parcial (Discriminador)|Chave parcial (Discriminador)]], [[#Chave primária (PK)|Chave primária (PK)]], [[#Conhecimento|Conhecimento]], [[#Conjunto de Entidades (Entity Set)|Conjunto de Entidades (Entity Set)]]
* [[#D|D]]: [[#Dado|Dado]], [[#DCL (Data Control Language)|DCL (Data Control Language)]], [[#DDL (Data Definition Language)|DDL (Data Definition Language)]], [[#Dependência lógica e física|Dependência lógica e física]], [[#Diagrama Entidade-Relacionamento (DER)|Diagrama Entidade-Relacionamento (DER)]], [[#Disjunção (Disjointness)|Disjunção (Disjointness)]], [[#DML (Data Manipulation Language)|DML (Data Manipulation Language)]], [[#DML Não Procedural (Declarativa)|DML Não Procedural (Declarativa)]], [[#DML Procedural (Navegacional)|DML Procedural (Navegacional)]]
* [[#E|E]]: [[#Entidade|Entidade]], [[#Entidade Fraca (Dependente)|Entidade Fraca (Dependente)]], [[#Entidade Forte (Regular)|Entidade Forte (Regular)]], [[#Especialização|Especialização]], [[#Esquema (Schema / Intensão)|Esquema (Schema / Intensão)]], [[#Esquema conceitual|Esquema conceitual]], [[#Esquema externo (Visão)|Esquema externo (Visão)]], [[#Esquema interno (Físico)|Esquema interno (Físico)]]
* [[#G|G]]: [[#Generalização|Generalização]], [[#Grau de Relacionamento|Grau de Relacionamento]]
* [[#H|H]]: [[#Herança de Atributos|Herança de Atributos]]
* [[#I|I]]: [[#Independência física de dados|Independência física de dados]], [[#Independência lógica de dados|Independência lógica de dados]], [[#Informação|Informação]], [[#Instância (Instance / Estado / Extensão)|Instância (Instance / Estado / Extensão)]], [[#Integridade referencial|Integridade referencial]]
* [[#L|L]]: [[#Levantamento de Requisitos de Dados|Levantamento de Requisitos de Dados]]
* [[#M|M]]: [[#Mapeamento entre níveis|Mapeamento entre níveis]], [[#MER Estendido (EER)|MER Estendido (EER)]], [[#Mini-mundo (Universo de discurso)|Mini-mundo (Universo de discurso)]], [[#Modelagem de dados|Modelagem de dados]], [[#Modelo conceitual|Modelo conceitual]], [[#Modelo físico|Modelo físico]], [[#Modelo lógico|Modelo lógico]], [[#Modelo relacional|Modelo relacional]]
* [[#N|N]]: [[#Nível de Visão (Externo)|Nível de Visão (Externo)]], [[#Nível Físico (Interno)|Nível Físico (Interno)]], [[#Nível Lógico (Conceitual)|Nível Lógico (Conceitual)]]
* [[#P|P]]: [[#Participação Parcial|Participação Parcial]], [[#Participação Total (Restrição de Existência)|Participação Total (Restrição de Existência)]], [[#Perda de atualização (Lost update)|Perda de atualização (Lost update)]], [[#Projeto Conceitual|Projeto Conceitual]], [[#Projeto Físico|Projeto Físico]], [[#Projeto Lógico|Projeto Lógico]], [[#Propriedades ACID|Propriedades ACID]]
* [[#R|R]]: [[#Redundância de dados|Redundância de dados]], [[#Relacionamento|Relacionamento]], [[#Relacionamento Binário|Relacionamento Binário]], [[#Relacionamento Identificador|Relacionamento Identificador]], [[#Relacionamento Muitos para Muitos (N:M)|Relacionamento Muitos para Muitos (N:M)]], [[#Relacionamento Ternário|Relacionamento Ternário]], [[#Relacionamento Um para Muitos (1:N)|Relacionamento Um para Muitos (1:N)]], [[#Relacionamento Um para Um (1:1)|Relacionamento Um para Um (1:1)]]
* [[#S|S]]: [[#Sistema de Banco de Dados (SBD)|Sistema de Banco de Dados (SBD)]], [[#Sistema Gerenciador de Banco de Dados (SGBD)|Sistema Gerenciador de Banco de Dados (SGBD)]], [[#Sobreposição (Overlap)|Sobreposição (Overlap)]]
* [[#T|T]]: [[#TCL (Transaction Control Language)|TCL (Transaction Control Language)]], [[#Tipo de Entidade (Entity Type)|Tipo de Entidade (Entity Type)]], [[#Transação|Transação]]
* [[#V|V]]: [[#Visão (View)|Visão (View)]]

---

## A

### Abstração de dados
* **Definição formal:** O processo de ocultar detalhes operacionais e físicos de baixo nível sobre como os dados são armazenados na máquina, expondo apenas as estruturas essenciais e a semântica necessária para usuários e aplicações.
* **Modelo mental / Feynman:** É como o painel de um automóvel. O motorista só precisa enxergar o velocímetro, o marcador de combustível e os pedais, sem precisar saber a quantidade de injeção eletrônica de combustível ocorrendo no motor a cada segundo.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

### Administrador de Banco de Dados (DBA)
* **Definição formal:** (*Database Administrator*) O profissional responsável pela infraestrutura técnica, desempenho físico (*tuning*), segurança operacional, políticas de backup/restore, alta disponibilidade e integridade física do SGBD e servidores.
* **Modelo mental / Feynman:** É o engenheiro de tráfego, saneamento e manutenção pesada de uma grande cidade.
* **Artigo correspondente:** [[03. Linguagens de banco de dados (ddl e dml) e perfis profissionais]], [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

### Administrador de Dados (AD)
* **Definição formal:** (*Data Administrator*) O profissional responsável pela governança estratégica da informação, definição do dicionário corporativo de dados, modelagem conceitual/lógica (DER) e alinhamento dos dados às regras de negócio e à conformidade legal (LGPD).
* **Modelo mental / Feynman:** É o arquiteto e urbanista que projeta o plano diretor e o zoneamento da cidade.
* **Artigo correspondente:** [[03. Linguagens de banco de dados (ddl e dml) e perfis profissionais]], [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

### Anomalia de modificação
* **Definição formal:** Inconsistências indesejadas que ocorrem em tabelas mal projetadas ou não normalizadas durante operações de inserção, alteração ou exclusão de registros.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

### Arquitetura ANSI/SPARC
* **Definição formal:** Padrão arquitetural tripartite para sistemas de bancos de dados proposto pelo comitê ANSI/X3/SPARC em 1975, que divide o sistema em três níveis de esquemas: externo (visões do usuário), conceitual (estrutura lógica global e regras de negócio) e interno/físico (alocação e estruturas de arquivos).
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

### Atores do banco de dados
* **Definição formal:** A comunidade de pessoas e papéis que interagem direta ou indiretamente com o banco de dados: Administrador de Banco de Dados (DBA), Administrador de Dados (AD), Projetistas, Desenvolvedores de Software e Usuários Finais (operacionais e gerenciais).
* **Artigo correspondente:** [[02. Abordagem de arquivos vs. abordagem de banco de dados]], [[03. Linguagens de banco de dados (ddl e dml) e perfis profissionais]], [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

### Atributo
* **Definição formal:** Propriedade, característica ou elemento descritivo associado a uma entidade ou a um relacionamento.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[05. Modelagem de entidades e tipos de atributos]]

### Atributo Armazenado (Base)
* **Definição formal:** Atributo cujo valor é gravado fisicamente nas tabelas do banco de dados, pois não pode ser deduzido a partir de nenhuma outra informação existente.
* **Artigo correspondente:** [[05. Modelagem de entidades e tipos de atributos]]

### Atributo Chave (Identificador)
* **Definição formal:** Atributo (ou conjunto de atributos) cujos valores são únicos para cada entidade dentro do conjunto, permitindo individualizar cada instância no banco.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[05. Modelagem de entidades e tipos de atributos]]

### Atributo Complexo
* **Definição formal:** Composição aninhada de atributos compostos contendo atributos multivalorados, ou atributos multivalorados cujos elementos são compostos.
* **Artigo correspondente:** [[05. Modelagem de entidades e tipos de atributos]]

### Atributo Composto
* **Definição formal:** Atributo formado pela união hierárquica de múltiplos atributos menores e mais simples (ex.: endereço formado por logradouro, número, bairro e CEP).
* **Artigo correspondente:** [[05. Modelagem de entidades e tipos de atributos]]

### Atributo Derivado (Calculado)
* **Definição formal:** Atributo cujo valor não é persistido fisicamente no disco, mas calculado dinamicamente pelo sistema a partir de atributos armazenados ou funções de sistema (ex.: idade calculada a partir da data de nascimento).
* **Artigo correspondente:** [[05. Modelagem de entidades e tipos de atributos]]

### Atributo Monovalorado (Univalorado)
* **Definição formal:** Atributo que armazena um único valor para cada entidade específica em um determinado momento (ex.: CPF, data de admissão).
* **Artigo correspondente:** [[05. Modelagem de entidades e tipos de atributos]]

### Atributo Multivalorado
* **Definição formal:** Atributo que pode assumir múltiplos valores para a mesma entidade (ex.: múltiplos telefones de contato de um cliente).
* **Artigo correspondente:** [[05. Modelagem de entidades e tipos de atributos]]

### Atributo Nulo (Opcional)
* **Definição formal:** Atributo que aceita a ausência de valor (`NULL`) quando a informação for desconhecida, inexistente ou não aplicável para determinada instância.
* **Artigo correspondente:** [[05. Modelagem de entidades e tipos de atributos]]

### Atributo Obrigatório
* **Definição formal:** Atributo cujo preenchimento de um valor válido é compulsório na inserção da entidade no banco (`NOT NULL`).
* **Artigo correspondente:** [[05. Modelagem de entidades e tipos de atributos]]

### Atributo Simples (Atômico)
* **Definição formal:** Atributo indivisível que não pode ser decomposto em partes menores sem perder sua semântica fundamental (ex.: salário, sexo).
* **Artigo correspondente:** [[05. Modelagem de entidades e tipos de atributos]]

### Autorrelacionamento
* **Definição formal:** Relacionamento de grau unário no qual instâncias da mesma entidade se associam entre si desempenhando papéis distintos (ex.: funcionário atua como supervisor de outros funcionários).
* **Artigo correspondente:** [[06. Modelagem de relacionamentos, cardinalidade e restrições de participação]]

---

## B

### Banco de Dados (BD) / Base de dados
* **Definição formal:** (*Database*) Coleção estruturada, integrada e logicamente coerente de dados correlacionados e persistentes que modelam e representam entidades e eventos de um domínio do mundo real (*mini-mundo*).
* **Artigo correspondente:** [[02. Abordagem de arquivos vs. abordagem de banco de dados]]

---

## C

### Cardinalidade Máxima
* **Definição formal:** O limite superior de ocorrências de uma entidade que podem estar associadas a uma única ocorrência de outra entidade através de um relacionamento ($1:1$, $1:N$, $N:M$).
* **Artigo correspondente:** [[06. Modelagem de relacionamentos, cardinalidade e restrições de participação]]

### Cardinalidade Mínima
* **Definição formal:** O limite inferior de ocorrências de uma entidade que devem participar de um relacionamento ($0$ para opcional/parcial, $\ge 1$ para obrigatória/total).
* **Artigo correspondente:** [[06. Modelagem de relacionamentos, cardinalidade e restrições de participação]]

### Catálogo do sistema (Dicionário de dados)
* **Definição formal:** Repositório interno e autocontido do SGBD que armazena os metadados — a descrição formal da estrutura, tabelas, colunas, tipos de dados, restrições de integridade e permissões de segurança de todo o banco de dados.
* **Artigo correspondente:** [[02. Abordagem de arquivos vs. abordagem de banco de dados]]

### Chave estrangeira (FK)
* **Definição formal:** (*Foreign Key*) Um atributo ou conjunto de atributos em uma tabela que faz referência direta à chave primária (PK) de outra tabela, estabelecendo e assegurando um vínculo relacional entre os registros.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

### Chave parcial (Discriminador)
* **Definição formal:** Atributo de uma entidade fraca que, isoladamente, não garante unicidade global, mas permite distinguir de forma única as instâncias subordinadas à mesma entidade forte. Representado por sublinhado tracejado no DER de Chen.
* **Artigo correspondente:** [[07. Modelo de entidades e relacionamentos estendido]]

### Chave primária (PK)
* **Definição formal:** (*Primary Key*) Um identificador único e irredutível escolhido para individualizar de forma inequívoca cada tupla dentro de uma tabela relacional (`NOT NULL` e `UNIQUE`).
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[05. Modelagem de entidades e tipos de atributos]]

### Conhecimento
* **Definição formal:** A integração de informações contextualizadas com regras de negócio, experiência humana e heurísticas, capacitando a tomada de decisões estratégicas.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

### Conjunto de Entidades (Entity Set)
* **Definição formal:** A coleção factual de todas as instâncias ou ocorrências de um determinado tipo de entidade armazenadas no banco de dados em um momento específico no tempo.
* **Artigo correspondente:** [[05. Modelagem de entidades e tipos de atributos]]

---

## D

### Dado
* **Definição formal:** Um valor ou registro atômico e bruto, desprovido de contexto, semântica ou interpretação inerente.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

### DCL (Data Control Language)
* **Definição formal:** Subconjunto da linguagem SQL voltado para o gerenciamento de permissões, direitos de acesso e privilégios de segurança aos usuários (`GRANT`, `REVOKE`).
* **Artigo correspondente:** [[03. Linguagens de banco de dados (ddl e dml) e perfis profissionais]]

### DDL (Data Definition Language)
* **Definição formal:** Subconjunto da linguagem SQL utilizado para definir, alterar e remover esquemas, tabelas, visões, índices e restrições estruturais no catálogo do banco de dados (`CREATE`, `ALTER`, `DROP`, `TRUNCATE`).
* **Modelo mental:** A equipe de cenografia que constrói a estrutura física do palco do teatro.
* **Artigo correspondente:** [[03. Linguagens de banco de dados (ddl e dml) e perfis profissionais]]

### Dependência lógica e física
* **Definição formal:** Acoplamento indesejável presente nos sistemas de arquivos legados, onde qualquer alteração no formato de gravação exigia a reescrita de todos os programas consumidores.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[02. Abordagem de arquivos vs. abordagem de banco de dados]]

### Diagrama Entidade-Relacionamento (DER)
* **Definição formal:** Notação gráfica e formal criada por Peter Chen em 1976 para representar o modelo conceitual de dados por meio de entidades, relacionamentos e atributos.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[04. Níveis do sgbd e etapas do projeto de banco de dados]], [[05. Modelagem de entidades e tipos de atributos]], [[06. Modelagem de relacionamentos, cardinalidade e restrições de participação]], [[07. Modelo de entidades e relacionamentos estendido]]

### Disjunção (Disjointness)
* **Definição formal:** Restrição em especializações do MER Estendido que define se uma entidade genérica pode pertencer a apenas uma subclasse (`d` - disjunta) ou a várias simultaneamente (`o` - sobreposição).
* **Artigo correspondente:** [[07. Modelo de entidades e relacionamentos estendido]]

### DML (Data Manipulation Language)
* **Definição formal:** Subconjunto da linguagem SQL utilizado para manipular e operar as instâncias de dados dentro das tabelas existentes (`INSERT`, `UPDATE`, `DELETE`, `SELECT`).
* **Modelo mental:** Os atores que entram, contracenam, mudam de posição e saem do palco do teatro.
* **Artigo correspondente:** [[03. Linguagens de banco de dados (ddl e dml) e perfis profissionais]]

### DML Não Procedural (Declarativa)
* **Definição formal:** Categoria de linguagem de manipulação (como o SQL padrão) em que o usuário especifica apenas *o que* deseja obter, cabendo ao otimizador do SGBD decidir a estratégia algorítmica e o plano de acesso físico aos dados.
* **Artigo correspondente:** [[03. Linguagens de banco de dados (ddl e dml) e perfis profissionais]]

### DML Procedural (Navegacional)
* **Definição formal:** Categoria de linguagem de manipulação (como PL/SQL e linguagens legadas) em que o usuário precisa instruir o computador com comandos explícitos de laços, ponteiros e algoritmos de navegação passo a passo pelos registros.
* **Artigo correspondente:** [[03. Linguagens de banco de dados (ddl e dml) e perfis profissionais]]

---

## E

### Entidade
* **Definição formal:** Qualquer objeto, ser, conceito ou evento do mundo real com existência distinta e sobre o qual o sistema necessita armazenar dados.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[05. Modelagem de entidades e tipos de atributos]]

### Entidade Fraca (Dependente)
* **Definição formal:** Entidade que não possui atributos suficientes para formar uma chave primária própria e cuja identificação depende compulsoriamente da chave primária de uma entidade forte proprietária através de um relacionamento identificador. Representada por retângulo duplo no DER de Chen.
* **Artigo correspondente:** [[07. Modelo de entidades e relacionamentos estendido]]

### Entidade Forte (Regular)
* **Definição formal:** Entidade autossuficiente que possui chave primária própria e existe independentemente de qualquer outra entidade no modelo de dados. Representada por retângulo simples.
* **Artigo correspondente:** [[05. Modelagem de entidades e tipos de atributos]], [[07. Modelo de entidades e relacionamentos estendido]]

### Especialização
* **Definição formal:** O processo de definir um conjunto de subclasses a partir de uma entidade genérica (superclasse), estabelecendo atributos e relacionamentos específicos para cada subgrupo.
* **Artigo correspondente:** [[07. Modelo de entidades e relacionamentos estendido]]

### Esquema (Schema / Intensão)
* **Definição formal:** A descrição ou projeto estrutural global do banco de dados, incluindo definições de tabelas, colunas, tipos e restrições. É estável e raramente sofre alterações ao longo do tempo.
* **Artigo correspondente:** [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

### Esquema conceitual
* **Definição formal:** O esquema intermediário global da arquitetura ANSI/SPARC que descreve a estrutura lógica completa de todos os dados da organização, independente de detalhes físicos de armazenamento.
* **Artigo correspondente:** [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

### Esquema externo (Visão)
* **Definição formal:** O esquema da arquitetura ANSI/SPARC mais próximo do usuário, descrevendo apenas a porção do banco de dados relevante para um determinado grupo ou perfil de acesso.
* **Artigo correspondente:** [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

### Esquema interno (Físico)
* **Definição formal:** O esquema de mais baixo nível da arquitetura ANSI/SPARC que descreve como os dados estão fisicamente alocados no hardware, incluindo arquivos, blocos e índices.
* **Artigo correspondente:** [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

---

## G

### Generalização
* **Definição formal:** O processo de abstração que unifica entidades com características em comum em uma superclasse genérica de mais alto nível.
* **Artigo correspondente:** [[07. Modelo de entidades e relacionamentos estendido]]

### Grau de Relacionamento
* **Definição formal:** O número de tipos de entidades participantes em um determinado relacionamento (unário = 1, binário = 2, ternário = 3, N-ário = N).
* **Artigo correspondente:** [[06. Modelagem de relacionamentos, cardinalidade e restrições de participação]], [[07. Modelo de entidades e relacionamentos estendido]]

---

## H

### Herança de Atributos
* **Definição formal:** Propriedade do MER Estendido pela qual as subclasses especializadas herdam automaticamente todos os atributos e relacionamentos definidos em sua superclasse genérica.
* **Artigo correspondente:** [[07. Modelo de entidades e relacionamentos estendido]]

---

## I

### Independência física de dados
* **Definição formal:** Capacidade de modificar as estruturas do nível interno/físico (discos, índices, partições) sem alterar o nível conceitual ou o código SQL das aplicações.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

### Independência lógica de dados
* **Definição formal:** Capacidade de alterar o nível conceitual/lógico (adicionar novas entidades ou colunas) sem que as aplicações e visões externas que não utilizam esses novos dados precisem ser alteradas.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

### Informação
* **Definição formal:** O dado bruto estruturado, processado, rotulado e associado a um significado e contexto claro.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

### Instância (Instance / Estado / Extensão)
* **Definição formal:** O conjunto real e factual de dados armazenados no banco de dados em um momento específico no tempo. Muda dinamicamente a cada transação DML.
* **Artigo correspondente:** [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

### Integridade referencial
* **Definição formal:** Regra fundamental de consistência relacional que estabelece que o valor de uma chave estrangeira em uma tabela deve corresponder a uma chave primária válida existente na tabela pai.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[02. Abordagem de arquivos vs. abordagem de banco de dados]]

---

## L

### Levantamento de Requisitos de Dados
* **Definição formal:** A etapa inicial do ciclo de vida de desenvolvimento de banco de dados na qual analistas e projetistas coletam, filtram e documentam as necessidades de informação e processos dos diferentes perfis de usuários (operacionais, analistas e gestores).
* **Artigo correspondente:** [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

---

## M

### Mapeamento entre níveis
* **Definição formal:** As transformações automáticas executadas pelo SGBD para converter solicitações expressas em esquemas externos para comandos no esquema conceitual e, finalmente, em leituras/escritas físicas no esquema interno.
* **Artigo correspondente:** [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

### MER Estendido (EER)
* **Definição formal:** Extensão do modelo entidade-relacionamento tradicional que incorpora abstrações avançadas como subclasses/superclasses, especialização, generalização, herança de atributos, entidades fracas e uniões de categorias.
* **Artigo correspondente:** [[07. Modelo de entidades e relacionamentos estendido]]

### Mini-mundo (Universo de discurso)
* **Definição formal:** A parte ou recorte específico do mundo real cujos dados e processos são de interesse direto para uma organização e que serão modelados e gerenciados pelo Sistema de Banco de Dados.
* **Artigo correspondente:** [[02. Abordagem de arquivos vs. abordagem de banco de dados]]

### Modelagem de dados
* **Definição formal:** O conjunto sistemático de conceitos, técnicas, processos e notações gráficas utilizados para abstrair, estruturar, definir e documentar os requisitos de dados e as regras de negócio de um domínio.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

### Modelo conceitual
* **Definição formal:** A representação abstrata de mais alto nível dos dados de um sistema, focada exclusivamente nas regras de negócio e no que existe no mundo real.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[04. Níveis do sgbd e etapas do projeto de banco de dados]], [[05. Modelagem de entidades e tipos de atributos]], [[07. Modelo de entidades e relacionamentos estendido]]

### Modelo físico
* **Definição formal:** A especificação técnica de mais baixo nível, detalhando como os dados são implementados e alocados no hardware e no SGBD específico.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

### Modelo lógico
* **Definição formal:** A representação intermediária dos dados adaptada a um paradigma de banco de dados específico (geralmente o modelo relacional).
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

### Modelo relacional
* **Definição formal:** Modelo formal de banco de dados introduzido por Edgar F. Codd em 1970, baseado na teoria matemática dos conjuntos, onde todos os dados são representados na forma de relações (tabelas).
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

---

## N

### Nível de Visão (Externo)
* **Definição formal:** O nível de abstração do SGBD voltado para atender às necessidades individuais de diferentes usuários e aplicações, disponibilizando janelas customizadas (*views*) e ocultando dados irrelevantes ou sensíveis.
* **Artigo correspondente:** [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

### Nível Físico (Interno)
* **Definição formal:** O nível de abstração do SGBD que gerencia o armazenamento real no hardware, lidando com alocação de blocos, particionamento e índices B-Tree/Hash.
* **Artigo correspondente:** [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

### Nível Lógico (Conceitual)
* **Definição formal:** O nível de abstração do SGBD que representa a estrutura completa e integrada de todo o banco de dados corporativo, contendo tabelas, chaves e restrições de integridade.
* **Artigo correspondente:** [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

---

## P

### Participação Parcial
* **Definição formal:** Restrição estrutural que indica que nem todas as instâncias de uma entidade precisam participar de um relacionamento (cardinalidade mínima = 0, representada por linha simples no DER de Chen).
* **Artigo correspondente:** [[06. Modelagem de relacionamentos, cardinalidade e restrições de participação]]

### Participação Total (Restrição de Existência)
* **Definição formal:** Restrição estrutural que estabelece que toda instância de uma entidade depende obrigatoriamente de sua participação no relacionamento para existir (cardinalidade mínima = 1, representada por linha dupla no DER de Chen).
* **Artigo correspondente:** [[06. Modelagem de relacionamentos, cardinalidade e restrições de participação]], [[07. Modelo de entidades e relacionamentos estendido]]

### Perda de atualização (Lost update)
* **Definição formal:** Falha crítica de concorrência que ocorre quando duas transações leem o mesmo registro simultaneamente e ambas gravam alterações, fazendo com que a última sobrescreva a primeira.
* **Artigo correspondente:** [[02. Abordagem de arquivos vs. abordagem de banco de dados]]

### Projeto Conceitual
* **Definição formal:** A primeira etapa do projeto de banco de dados, responsável por produzir um esquema semântico abstrato (MER/DER) a partir dos requisitos do mini-mundo, com independência total de SGBD.
* **Participantes:** Usuários de negócio, Analistas de Sistemas e Administrador de Dados (AD).
* **Artigo correspondente:** [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

### Projeto Físico
* **Definição formal:** A terceira etapa do projeto de banco de dados, responsável por implementar o esquema lógico em um SGBD específico por meio de scripts DDL, definindo tipos nativos, índices e estratégias de armazenamento.
* **Participantes:** Administrador de Banco de Dados (DBA) e Engenheiros de Infraestrutura.
* **Artigo correspondente:** [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

### Projeto Lógico
* **Definição formal:** A segunda etapa do projeto de banco de dados, responsável por transformar o modelo conceitual em um esquema relacional estruturado (tabelas, colunas, PKs, FKs) e aplicar regras de normalização.
* **Participantes:** Projetistas de Banco de Dados, Arquitetos de Software e Desenvolvedores.
* **Artigo correspondente:** [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

### Propriedades ACID
* **Definição formal:** Conjunto de quatro propriedades fundamentais que garantem a confiabilidade de transações em um SGBD: Atomicidade, Consistência, Isolamento e Durabilidade.
* **Artigo correspondente:** [[02. Abordagem de arquivos vs. abordagem de banco de dados]]

---

## R

### Redundância de dados
* **Definição formal:** A repetição desnecessária do mesmo dado em múltiplos locais da base de dados, gerando desperdício de espaço e risco de inconsistência.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[02. Abordagem de arquivos vs. abordagem de banco de dados]]

### Relacionamento
* **Definição formal:** Associação semântica e lógica entre duas ou mais entidades do modelo de dados.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[06. Modelagem de relacionamentos, cardinalidade e restrições de participação]]

### Relacionamento Binário
* **Definição formal:** Relacionamento que conecta exatamente duas entidades distintas do modelo conceitual.
* **Artigo correspondente:** [[06. Modelagem de relacionamentos, cardinalidade e restrições de participação]], [[07. Modelo de entidades e relacionamentos estendido]]

### Relacionamento Identificador
* **Definição formal:** Relacionamento especial no qual uma entidade fraca se associa à sua entidade forte proprietária para obter a chave de identificação. Representado por um losango duplo no DER de Chen.
* **Artigo correspondente:** [[07. Modelo de entidades e relacionamentos estendido]]

### Relacionamento Muitos para Muitos (N:M)
* **Definição formal:** Mapeamento de cardinalidade máxima no qual uma ocorrência da entidade A pode associar-se a várias ocorrências da entidade B, e vice-versa.
* **Artigo correspondente:** [[06. Modelagem de relacionamentos, cardinalidade e restrições de participação]]

### Relacionamento Ternário
* **Definição formal:** Relacionamento que conecta simultaneamente três entidades distintas para completar a semântica da associação de forma atômica.
* **Artigo correspondente:** [[06. Modelagem de relacionamentos, cardinalidade e restrições de participação]], [[07. Modelo de entidades e relacionamentos estendido]]

### Relacionamento Um para Muitos (1:N)
* **Definição formal:** Mapeamento de cardinalidade máxima no qual uma ocorrência da entidade A pode associar-se a várias da entidade B, mas cada ocorrência de B associa-se a no máximo uma de A.
* **Artigo correspondente:** [[06. Modelagem de relacionamentos, cardinalidade e restrições de participação]]

### Relacionamento Um para Um (1:1)
* **Definição formal:** Mapeamento de cardinalidade máxima no qual cada ocorrência da entidade A associa-se a no máximo uma ocorrência de B, e vice-versa.
* **Artigo correspondente:** [[06. Modelagem de relacionamentos, cardinalidade e restrições de participação]]

---

## S

### Sistema de Banco de Dados (SBD)
* **Definição formal:** O ecossistema integrado completo composto pelo Banco de Dados, o SGBD, as aplicações clientes, o hardware e a comunidade de usuários.
* **Artigo correspondente:** [[02. Abordagem de arquivos vs. abordagem de banco de dados]]

### Sistema Gerenciador de Banco de Dados (SGBD)
* **Definição formal:** (*DBMS*) O software de sistema responsável por gerenciar, controlar, proteger, consultar e manter bancos de dados.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[02. Abordagem de arquivos vs. abordagem de banco de dados]]

### Sobreposição (Overlap)
* **Definição formal:** Restrição em especializações do MER Estendido que permite que uma mesma ocorrência da superclasse pertença a múltiplas subclasses simultaneamente (`o`).
* **Artigo correspondente:** [[07. Modelo de entidades e relacionamentos estendido]]

---

## T

### TCL (Transaction Control Language)
* **Definição formal:** Subconjunto da linguagem SQL utilizado para gerenciar a execução atômica e consistente de transações no banco de dados (`COMMIT`, `ROLLBACK`, `SAVEPOINT`).
* **Artigo correspondente:** [[03. Linguagens de banco de dados (ddl e dml) e perfis profissionais]]

### Tipo de Entidade (Entity Type)
* **Definição formal:** O esquema descritivo formal que define a estrutura e o conjunto de atributos comuns compartilhados por um grupo de entidades similares (análogo a uma Classe na POO).
* **Artigo correspondente:** [[05. Modelagem de entidades e tipos de atributos]]

### Transação
* **Definição formal:** Uma unidade lógica de processamento que inclui uma ou mais operações de acesso ao banco de dados executadas sob as garantias ACID.
* **Artigo correspondente:** [[02. Abordagem de arquivos vs. abordagem de banco de dados]]

---

## V

### Visão (View)
* **Definição formal:** Uma tabela virtual baseada no resultado de uma consulta SQL pré-definida, utilizada para simplificar consultas e proteger colunas sensíveis.
* **Artigo correspondente:** [[02. Abordagem de arquivos vs. abordagem de banco de dados]], [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

---

## Artigos relacionados e navegação

* **Voltar ao artigo 01:** [[01. Introdução à modelagem de dados e sua importância]]
* **Voltar ao artigo 02:** [[02. Abordagem de arquivos vs. abordagem de banco de dados]]
* **Voltar ao artigo 03:** [[03. Linguagens de banco de dados (ddl e dml) e perfis profissionais]]
* **Voltar ao artigo 04:** [[04. Níveis do sgbd e etapas do projeto de banco de dados]]
* **Voltar ao artigo 05:** [[05. Modelagem de entidades e tipos de atributos]]
* **Voltar ao artigo 06:** [[06. Modelagem de relacionamentos, cardinalidade e restrições de participação]]
* **Voltar ao artigo 07:** [[07. Modelo de entidades e relacionamentos estendido]]
* **Resumo da disciplina:** [[00. Modelagem de Dados - Resumo]]
* **Índice geral do vault:** [[index.md|Página Inicial do Vault]]
