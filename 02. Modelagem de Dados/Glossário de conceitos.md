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
  - "[[08. Conceitos do modelo relacional e chave primária]]"
  - "[[09. Integridade referencial e chave estrangeira]]"
  - "[[10. Mapeamento de entidades e atributos]]"
  - "[[11. Mapeamento de relacionamentos]]"
  - "[[12. 1ª, 2ª e 3ª formas normais]]"
  - "[[13. Bancos de dados não-relacionais]]"
  - "[[14. Segurança de banco de dados]]"
---

# Glossário de conceitos: modelagem e projeto de bancos de dados

> **Contexto:** Dicionário terminológico e conceitual consolidado da disciplina de Modelagem de Dados, reunindo definições formais, modelos mentais, papéis arquiteturais e analogias didáticas.

---

## Índice alfabético

* [[#A|A]]: [[#Abstração de dados|Abstração de dados]], [[#Autenticação|Autenticação]], [[#Autorização|Autorização]], [[#Ações referenciais|Ações referenciais]], [[#Atributo primo|Atributo primo]], [[#Administrador de Banco de Dados (DBA)|Administrador de Banco de Dados (DBA)]], [[#Administrador de Dados (AD)|Administrador de Dados (AD)]], [[#Anomalia de modificação|Anomalia de modificação]], [[#Arquitetura ANSI/SPARC|Arquitetura ANSI/SPARC]], [[#Atores do banco de dados|Atores do banco de dados]], [[#Atributo|Atributo]], [[#Atributo Armazenado (Base)|Atributo Armazenado (Base)]], [[#Atributo Chave (Identificador)|Atributo Chave (Identificador)]], [[#Atributo Complexo|Atributo Complexo]], [[#Atributo Composto|Atributo Composto]], [[#Atributo Derivado (Calculado)|Atributo Derivado (Calculado)]], [[#Atributo Monovalorado (Univalorado)|Atributo Monovalorado (Univalorado)]], [[#Atributo Multivalorado|Atributo Multivalorado]], [[#Atributo Nulo (Opcional)|Atributo Nulo (Opcional)]], [[#Atributo Obrigatório|Atributo Obrigatório]], [[#Atributo Simples (Atômico)|Atributo Simples (Atômico)]], [[#Autorrelacionamento|Autorrelacionamento]]
* [[#B|B]]: [[#Banco de Dados (BD) / Base de dados|Banco de Dados (BD) / Base de dados]], [[#Banco de dados orientado a objetos|Banco de dados orientado a objetos]]
* [[#C|C]]: [[#Confidencialidade|Confidencialidade]], [[#Controle de acesso discricionário (DAC)|Controle de acesso discricionário (DAC)]], [[#Controle de acesso obrigatório (MAC)|Controle de acesso obrigatório (MAC)]], [[#Cardinalidade Máxima|Cardinalidade Máxima]], [[#Cardinalidade Mínima|Cardinalidade Mínima]], [[#Catálogo do sistema (Dicionário de dados)|Catálogo do sistema (Dicionário de dados)]], [[#Chave estrangeira (FK)|Chave estrangeira (FK)]], [[#Chave parcial (Discriminador)|Chave parcial (Discriminador)]], [[#Chave primária (PK)|Chave primária (PK)]], [[#Conhecimento|Conhecimento]], [[#Conjunto de Entidades (Entity Set)|Conjunto de Entidades (Entity Set)]]
* [[#D|D]]: [[#Disponibilidade|Disponibilidade]], [[#Dado|Dado]], [[#DCL (Data Control Language)|DCL (Data Control Language)]], [[#DDL (Data Definition Language)|DDL (Data Definition Language)]], [[#Dependência funcional|Dependência funcional]], [[#Dependência parcial|Dependência parcial]], [[#Dependência transitiva|Dependência transitiva]], [[#Dependência lógica e física|Dependência lógica e física]], [[#Diagrama Entidade-Relacionamento (DER)|Diagrama Entidade-Relacionamento (DER)]], [[#Disjunção (Disjointness)|Disjunção (Disjointness)]], [[#DML (Data Manipulation Language)|DML (Data Manipulation Language)]], [[#DML Não Procedural (Declarativa)|DML Não Procedural (Declarativa)]], [[#DML Procedural (Navegacional)|DML Procedural (Navegacional)]]
* [[#E|E]]: [[#Entidade|Entidade]], [[#Entidade Fraca (Dependente)|Entidade Fraca (Dependente)]], [[#Entidade Forte (Regular)|Entidade Forte (Regular)]], [[#Especialização|Especialização]], [[#Esquema (Schema / Intensão)|Esquema (Schema / Intensão)]], [[#Esquema conceitual|Esquema conceitual]], [[#Esquema externo (Visão)|Esquema externo (Visão)]], [[#Esquema interno (Físico)|Esquema interno (Físico)]]
* [[#G|G]]: [[#Generalização|Generalização]], [[#Grau de Relacionamento|Grau de Relacionamento]]
* [[#H|H]]: [[#Herança de atributos e relacionamentos|Herança de atributos e relacionamentos]]
* [[#I|I]]: [[#Integridade em segurança|Integridade em segurança]], [[#Identificador de objeto (OID)|Identificador de objeto (OID)]], [[#Independência física de dados|Independência física de dados]], [[#Independência lógica de dados|Independência lógica de dados]], [[#Informação|Informação]], [[#Instância (Instance / Estado / Extensão)|Instância (Instance / Estado / Extensão)]], [[#Integridade de chave|Integridade de chave]], [[#Integridade de domínio|Integridade de domínio]], [[#Integridade de entidade|Integridade de entidade]], [[#Integridade referencial|Integridade referencial]]
* [[#L|L]]: [[#LGPD|LGPD]], [[#Levantamento de Requisitos de Dados|Levantamento de Requisitos de Dados]]
* [[#M|M]]: [[#Mapeamento entre níveis|Mapeamento entre níveis]], [[#Modelo de rede|Modelo de rede]], [[#Modelo hierárquico|Modelo hierárquico]], [[#Mapeamento relacional|Mapeamento relacional]], [[#MER Estendido (EER)|MER Estendido (EER)]], [[#Mini-mundo (Universo de discurso)|Mini-mundo (Universo de discurso)]], [[#Modelagem de dados|Modelagem de dados]], [[#Modelo conceitual|Modelo conceitual]], [[#Modelo físico|Modelo físico]], [[#Modelo lógico|Modelo lógico]], [[#Modelo relacional|Modelo relacional]]
* [[#N|N]]: [[#NoSQL|NoSQL]], [[#Normalização|Normalização]], [[#Nível de Visão (Externo)|Nível de Visão (Externo)]], [[#Nível Físico (Interno)|Nível Físico (Interno)]], [[#Nível Lógico (Conceitual)|Nível Lógico (Conceitual)]]
* [[#P|P]]: [[#Princípio do menor privilégio|Princípio do menor privilégio]], [[#Parcialidade em especializações|Parcialidade em especializações]], [[#Primeira Forma Normal (1FN)|Primeira Forma Normal (1FN)]], [[#Participação Parcial|Participação Parcial]], [[#Participação Total (Restrição de Existência)|Participação Total (Restrição de Existência)]], [[#Perda de atualização (Lost update)|Perda de atualização (Lost update)]], [[#Projeto Conceitual|Projeto Conceitual]], [[#Projeto Físico|Projeto Físico]], [[#Projeto Lógico|Projeto Lógico]], [[#Propriedades ACID|Propriedades ACID]]
* [[#R|R]]: [[#Redundância de dados|Redundância de dados]], [[#Relacionamento|Relacionamento]], [[#Relacionamento Binário|Relacionamento Binário]], [[#Relacionamento Identificador|Relacionamento Identificador]], [[#Relacionamento Muitos para Muitos (N:M)|Relacionamento Muitos para Muitos (N:M)]], [[#Relacionamento Ternário|Relacionamento Ternário]], [[#Relacionamento Um para Muitos (1:N)|Relacionamento Um para Muitos (1:N)]], [[#Relacionamento Um para Um (1:1)|Relacionamento Um para Um (1:1)]]
* [[#S|S]]: [[#Segunda Forma Normal (2FN)|Segunda Forma Normal (2FN)]], [[#SQL|SQL]], [[#Sistema de Banco de Dados (SBD)|Sistema de Banco de Dados (SBD)]], [[#Sistema Gerenciador de Banco de Dados (SGBD)|Sistema Gerenciador de Banco de Dados (SGBD)]], [[#Subtipo|Subtipo]], [[#Supertipo|Supertipo]], [[#Sobreposição (Overlap)|Sobreposição (Overlap)]]
* [[#T|T]]: [[#Trilha de auditoria|Trilha de auditoria]], [[#Tabela associativa|Tabela associativa]], [[#Tipo chave-valor|Tipo chave-valor]], [[#Tipo documento|Tipo documento]], [[#Tipo grafo|Tipo grafo]], [[#Tipo wide-column|Tipo wide-column]], [[#TCL (Transaction Control Language)|TCL (Transaction Control Language)]], [[#Terceira Forma Normal (3FN)|Terceira Forma Normal (3FN)]], [[#Tipo de Entidade (Entity Type)|Tipo de Entidade (Entity Type)]], [[#Totalidade em especializações|Totalidade em especializações]], [[#Transação|Transação]]
* [[#V|V]]: [[#Visão (View)|Visão (View)]]

---

## A

### Abstração de dados
* **Definição formal:** O processo de ocultar detalhes operacionais e físicos de baixo nível sobre como os dados são armazenados na máquina, expondo apenas as estruturas essenciais e a semântica necessária para usuários e aplicações.
* **Modelo mental / Feynman:** É como o painel de um automóvel. O motorista só precisa enxergar o velocímetro, o marcador de combustível e os pedais, sem precisar saber a quantidade de injeção eletrônica de combustível ocorrendo no motor a cada segundo.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

### Ações referenciais
* **Definição formal:** Comportamentos definidos para preservar a integridade referencial quando uma chave referenciada é alterada ou excluída, como `RESTRICT`/`NO ACTION`, `CASCADE`, `SET NULL` e `SET DEFAULT`.
* **Modelo mental:** Respondem à pergunta: "o que deve acontecer com as tuplas filhas se a chave pai mudar ou desaparecer?"
* **Artigo correspondente:** [[09. Integridade referencial e chave estrangeira]]

### Administrador de Banco de Dados (DBA)
* **Definição formal:** (*Database Administrator*) O profissional responsável pela infraestrutura técnica, desempenho físico (*tuning*), segurança operacional, políticas de backup/restore, alta disponibilidade e integridade física do SGBD e servidores.
* **Modelo mental / Feynman:** É o engenheiro de tráfego, saneamento e manutenção pesada de uma grande cidade.
* **Artigo correspondente:** [[03. Linguagens de banco de dados (ddl e dml) e perfis profissionais]], [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

### Administrador de Dados (AD)
* **Definição formal:** (*Data Administrator*) O profissional responsável pela governança estratégica da informação, definição do dicionário corporativo de dados, modelagem conceitual/lógica (DER) e alinhamento dos dados às regras de negócio e à conformidade legal (LGPD).
* **Modelo mental / Feynman:** É o arquiteto e urbanista que projeta o plano diretor e o zoneamento da cidade.
* **Artigo correspondente:** [[03. Linguagens de banco de dados (ddl e dml) e perfis profissionais]], [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

### Anomalia de modificação
* **Definição formal:** Problema decorrente de redundância ou dependências inadequadas em relações mal projetadas, manifestando-se como anomalias de inserção, atualização ou exclusão.
* **Modelo mental:** Uma operação sobre um fato obriga a alterar, criar ou apagar indevidamente outro fato.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[12. 1ª, 2ª e 3ª formas normais]]

### Arquitetura ANSI/SPARC
* **Definição formal:** Padrão arquitetural tripartite para sistemas de bancos de dados proposto pelo comitê ANSI/X3/SPARC em 1975, que divide o sistema em três níveis de esquemas: externo (visões do usuário), conceitual (estrutura lógica global e regras de negócio) e interno/físico (alocação e estruturas de arquivos).
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

### Atores do banco de dados
* **Definição formal:** A comunidade de pessoas e papéis que interagem direta ou indiretamente com o banco de dados: Administrador de Banco de Dados (DBA), Administrador de Dados (AD), Projetistas, Desenvolvedores de Software e Usuários Finais (operacionais e gerenciais).
* **Artigo correspondente:** [[02. Abordagem de arquivos vs. abordagem de banco de dados]], [[03. Linguagens de banco de dados (ddl e dml) e perfis profissionais]], [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

### Autenticação
* **Definição formal:** Processo de verificar a identidade apresentada por um usuário, serviço ou processo.
* **Modelo mental:** Responde à pergunta "quem é você?".
* **Artigo correspondente:** [[14. Segurança de banco de dados]]

### Autorização
* **Definição formal:** Processo de determinar quais recursos e operações uma identidade autenticada pode acessar ou executar.
* **Modelo mental:** Responde à pergunta "o que você pode fazer?".
* **Artigo correspondente:** [[14. Segurança de banco de dados]]

### Atributo
* **Definição formal:** Propriedade, característica ou elemento descritivo associado a uma entidade ou a um relacionamento.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[05. Modelagem de entidades e tipos de atributos]]

### Atributo primo
* **Definição formal:** Atributo que participa de pelo menos uma chave candidata de uma relação. O conceito é importante na formulação formal das formas normais.
* **Artigo correspondente:** [[12. 1ª, 2ª e 3ª formas normais]]

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
* **Artigo correspondente:** [[05. Modelagem de entidades e tipos de atributos]], [[10. Mapeamento de entidades e atributos]]

### Atributo Derivado (Calculado)
* **Definição formal:** Atributo cujo valor não é persistido fisicamente no disco, mas calculado dinamicamente pelo sistema a partir de atributos armazenados ou funções de sistema (ex.: idade calculada a partir da data de nascimento).
* **Artigo correspondente:** [[05. Modelagem de entidades e tipos de atributos]]

### Atributo Monovalorado (Univalorado)
* **Definição formal:** Atributo que armazena um único valor para cada entidade específica em um determinado momento (ex.: CPF, data de admissão).
* **Artigo correspondente:** [[05. Modelagem de entidades e tipos de atributos]]

### Atributo Multivalorado
* **Definição formal:** Atributo que pode assumir múltiplos valores para a mesma entidade (ex.: múltiplos telefones de contato de um cliente). No mapeamento relacional, normalmente origina uma relação própria ligada à entidade proprietária por chave estrangeira.
* **Artigo correspondente:** [[05. Modelagem de entidades e tipos de atributos]], [[10. Mapeamento de entidades e atributos]]

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

### Banco de dados orientado a objetos
* **Definição formal:** SGBD cujo modelo principal representa dados como objetos com identidade própria, tipos/classes, atributos complexos, referências e, conforme o produto, herança e encapsulamento.
* **Modelo mental:** Em vez de converter necessariamente objetos em linhas e FKs, o banco pode persistir diretamente a estrutura de objetos e suas referências.
* **Artigo correspondente:** [[13. Bancos de dados não-relacionais]]

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
* **Definição formal:** (*Foreign Key*) Atributo ou conjunto de atributos de uma relação cujos valores referenciam uma chave identificadora de outra relação (ou da própria relação). Quando não nula, a FK deve corresponder a um valor válido da chave referenciada.
* **Modelo mental:** A PK identifica "quem é" a tupla na relação de origem; a FK leva esse identificador para outra relação para dizer "a quem esta tupla se refere".
* **Artigo correspondente:** [[09. Integridade referencial e chave estrangeira]]

### Chave parcial (Discriminador)
* **Definição formal:** Atributo de uma entidade fraca que, isoladamente, não garante unicidade global, mas permite distinguir de forma única as instâncias subordinadas à mesma entidade forte. Representado por sublinhado tracejado no DER de Chen. No mapeamento relacional, combina-se com a PK da entidade proprietária para formar a PK da relação fraca.
* **Artigo correspondente:** [[07. Modelo de entidades e relacionamentos estendido]], [[10. Mapeamento de entidades e atributos]]

### Chave primária (PK)
* **Definição formal:** (*Primary Key*) Um identificador único e irredutível escolhido para individualizar de forma inequívoca cada tupla dentro de uma tabela relacional (`NOT NULL` e `UNIQUE`).
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[05. Modelagem de entidades e tipos de atributos]]

### Confidencialidade
* **Definição formal:** Objetivo de segurança que restringe a revelação de informações a pessoas, sistemas e processos autorizados.
* **Modelo mental:** Quem pode ver este dado?
* **Artigo correspondente:** [[14. Segurança de banco de dados]]

### Controle de acesso discricionário (DAC)
* **Definição formal:** Modelo em que privilégios podem ser concedidos e revogados por sujeitos autorizados conforme regras do sistema.
* **Artigo correspondente:** [[14. Segurança de banco de dados]]

### Controle de acesso obrigatório (MAC)
* **Definição formal:** Modelo em que o acesso é determinado por uma política central e classificações que usuários individuais não podem simplesmente alterar.
* **Artigo correspondente:** [[14. Segurança de banco de dados]]

### Conhecimento
* **Definição formal:** A integração de informações contextualizadas com regras de negócio, experiência humana e heurísticas, capacitando a tomada de decisões estratégicas.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

### Conjunto de Entidades (Entity Set)
* **Definição formal:** A coleção factual de todas as instâncias ou ocorrências de um determinado tipo de entidade armazenadas no banco de dados em um momento específico no tempo.
* **Artigo correspondente:** [[05. Modelagem de entidades e tipos de atributos]]

---

## D

### Disponibilidade
* **Definição formal:** Objetivo de segurança que garante acesso a dados e serviços por usuários e sistemas autorizados quando necessário.
* **Modelo mental:** Quem tem autorização consegue acessar quando precisa?
* **Artigo correspondente:** [[14. Segurança de banco de dados]]

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

### Dependência funcional
* **Definição formal:** Relação lógica entre conjuntos de atributos representada por `X → Y`, indicando que cada valor de X determina no máximo um valor correspondente de Y em uma relação válida.
* **Modelo mental:** Se conheço X, a regra do domínio permite determinar univocamente Y.
* **Artigo correspondente:** [[12. 1ª, 2ª e 3ª formas normais]]

### Dependência parcial
* **Definição formal:** Dependência funcional em que um atributo não-primo depende apenas de um subconjunto próprio de uma chave candidata composta, e não da chave inteira.
* **Modelo mental:** O atributo está "pendurado" em apenas uma parte da chave composta.
* **Artigo correspondente:** [[12. 1ª, 2ª e 3ª formas normais]]

### Dependência transitiva
* **Definição formal:** Dependência em cadeia na qual uma chave determina um atributo intermediário e esse atributo determina outro, como `CPF → Dept_Cod → Dept_Nome`.
* **Modelo mental:** O atributo final depende da chave "por intermédio" de outro atributo.
* **Artigo correspondente:** [[12. 1ª, 2ª e 3ª formas normais]]

### Dependência lógica e física
* **Definição formal:** Acoplamento indesejável presente nos sistemas de arquivos legados, onde qualquer alteração no formato de gravação exigia a reescrita de todos os programas consumidores.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[02. Abordagem de arquivos vs. abordagem de banco de dados]]

### Diagrama Entidade-Relacionamento (DER)
* **Definição formal:** Notação gráfica e formal criada por Peter Chen em 1976 para representar o modelo conceitual de dados por meio de entidades, relacionamentos e atributos.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[04. Níveis do sgbd e etapas do projeto de banco de dados]], [[05. Modelagem de entidades e tipos de atributos]], [[06. Modelagem de relacionamentos, cardinalidade e restrições de participação]], [[07. Modelo de entidades e relacionamentos estendido]]

### Disjunção (Disjointness)
* **Definição formal:** Restrição de uma especialização do MER Estendido em que uma ocorrência do supertipo pode pertencer a no máximo um dos subtipos daquela especialização. É representada por `d`.
* **Modelo mental:** Responde à pergunta: "pode estar em mais de um subtipo ao mesmo tempo?" Na disjunção, não.
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
* **Definição formal:** Entidade que não possui atributos suficientes para formar uma chave primária completa e independente e cuja identificação depende da chave primária de uma entidade forte proprietária através de um relacionamento identificador. Representada por retângulo duplo no DER de Chen. No modelo relacional, a PK da proprietária entra como FK e participa da PK composta da relação fraca.
* **Artigo correspondente:** [[07. Modelo de entidades e relacionamentos estendido]], [[10. Mapeamento de entidades e atributos]]

### Entidade Forte (Regular)
* **Definição formal:** Entidade cuja identificação pode ser estabelecida por uma chave própria, sem depender da chave de outra entidade para completar sua identidade. Representada por retângulo simples.
* **Artigo correspondente:** [[05. Modelagem de entidades e tipos de atributos]], [[07. Modelo de entidades e relacionamentos estendido]], [[10. Mapeamento de entidades e atributos]]

### Especialização
* **Definição formal:** Processo que parte de um supertipo e define subtipos mais específicos, capazes de herdar atributos e relacionamentos gerais e acrescentar propriedades próprias.
* **Modelo mental:** Movimento do geral para o específico: `VEÍCULO` → `CARRO` e `CAMINHÃO`.
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
* **Definição formal:** Processo de abstração que identifica características comuns em tipos específicos e as reúne em um supertipo mais geral.
* **Modelo mental:** Movimento do específico para o geral: `CARRO` + `CAMINHÃO` → `VEÍCULO`.
* **Artigo correspondente:** [[07. Modelo de entidades e relacionamentos estendido]]

### Grau de Relacionamento
* **Definição formal:** O número de tipos de entidades participantes em um determinado relacionamento (unário = 1, binário = 2, ternário = 3, N-ário = N).
* **Artigo correspondente:** [[06. Modelagem de relacionamentos, cardinalidade e restrições de participação]], [[07. Modelo de entidades e relacionamentos estendido]]

---

## H

### Herança de atributos e relacionamentos
* **Definição formal:** Propriedade do MER Estendido pela qual uma ocorrência de um subtipo recebe os atributos e relacionamentos definidos no supertipo e pode acrescentar propriedades específicas.
* **Artigo correspondente:** [[07. Modelo de entidades e relacionamentos estendido]]

---

## I

### Identificador de objeto (OID)
* **Definição formal:** Identificador fornecido pelo sistema para preservar a identidade de um objeto independentemente dos valores de seus atributos.
* **Modelo mental:** O objeto continua sendo o mesmo mesmo que seus dados mudem.
* **Artigo correspondente:** [[13. Bancos de dados não-relacionais]]

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

### Integridade em segurança
* **Definição formal:** Objetivo de segurança voltado a preservar correção, consistência e legitimidade dos dados, impedindo ou detectando modificações indevidas.
* **Modelo mental:** Quem pode alterar e como sabemos que a informação continua confiável?
* **Artigo correspondente:** [[14. Segurança de banco de dados]]

### Integridade de chave
* **Definição formal:** Restrição que exige unicidade dos valores de uma chave candidata; duas tuplas distintas não podem compartilhar a mesma combinação de valores de uma chave.
* **Artigo correspondente:** [[08. Conceitos do modelo relacional e chave primária]], [[09. Integridade referencial e chave estrangeira]]

### Integridade de domínio
* **Definição formal:** Restrição que exige que cada valor armazenado pertença ao domínio admitido pelo atributo, incluindo tipo, formato, faixa e demais regras lógicas aplicáveis.
* **Artigo correspondente:** [[08. Conceitos do modelo relacional e chave primária]], [[09. Integridade referencial e chave estrangeira]]

### Integridade de entidade
* **Definição formal:** Regra segundo a qual nenhum componente da chave primária de uma relação pode ser nulo, pois cada tupla precisa possuir identidade definida.
* **Artigo correspondente:** [[09. Integridade referencial e chave estrangeira]]

### Integridade referencial
* **Definição formal:** Regra de consistência segundo a qual cada valor não nulo de uma chave estrangeira deve corresponder a um valor existente da chave referenciada.
* **Modelo mental:** Uma referência não pode apontar para uma tupla que não existe.
* **Artigo correspondente:** [[09. Integridade referencial e chave estrangeira]]

---

## L

### LGPD
* **Definição formal:** Lei nº 13.709/2018, que regula o tratamento de dados pessoais no Brasil e protege direitos fundamentais de liberdade, privacidade e livre desenvolvimento da personalidade.
* **Artigo correspondente:** [[14. Segurança de banco de dados]]

### Levantamento de Requisitos de Dados
* **Definição formal:** A etapa inicial do ciclo de vida de desenvolvimento de banco de dados na qual analistas e projetistas coletam, filtram e documentam as necessidades de informação e processos dos diferentes perfis de usuários (operacionais, analistas e gestores).
* **Artigo correspondente:** [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

---

## M

### Mapeamento entre níveis
* **Definição formal:** As transformações automáticas executadas pelo SGBD para converter solicitações expressas em esquemas externos para comandos no esquema conceitual e, finalmente, em leituras/escritas físicas no esquema interno.
* **Artigo correspondente:** [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

### Mapeamento relacional
* **Definição formal:** Conjunto de regras de projeto lógico que transforma elementos do MER/DER em relações, atributos, chaves primárias e chaves estrangeiras, preservando no modelo relacional a semântica definida no modelo conceitual.
* **Modelo mental:** É a tradução entre duas linguagens de representação: do desenho conceitual do domínio para a estrutura formal de relações e chaves.
* **Artigo correspondente:** [[10. Mapeamento de entidades e atributos]], [[11. Mapeamento de relacionamentos]]

### MER Estendido (EER)
* **Definição formal:** Extensão do modelo entidade-relacionamento tradicional que incorpora abstrações avançadas como subclasses/superclasses, especialização, generalização, herança de atributos, entidades fracas e uniões de categorias.
* **Artigo correspondente:** [[07. Modelo de entidades e relacionamentos estendido]]

### Mini-mundo (Universo de discurso)
* **Definição formal:** A parte ou recorte específico do mundo real cujos dados e processos são de interesse direto para uma organização e que serão modelados e gerenciados pelo Sistema de Banco de Dados.
* **Artigo correspondente:** [[02. Abordagem de arquivos vs. abordagem de banco de dados]]

### Modelagem de dados
* **Definição formal:** O conjunto sistemático de conceitos, técnicas, processos e notações gráficas utilizados para abstrair, estruturar, definir e documentar os requisitos de dados e as regras de negócio de um domínio.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

### Modelo hierárquico
* **Definição formal:** Modelo de dados que organiza registros em uma estrutura de árvore, na qual cada filho possui no máximo um pai e relações 1:N são representadas naturalmente.
* **Artigo correspondente:** [[13. Bancos de dados não-relacionais]]

### Modelo de rede
* **Definição formal:** Modelo de dados navegacional em que registros podem participar de múltiplas ligações, historicamente associado ao CODASYL e a conjuntos proprietário-membro.
* **Artigo correspondente:** [[13. Bancos de dados não-relacionais]]

### Modelo conceitual
* **Definição formal:** A representação abstrata de mais alto nível dos dados de um sistema, focada exclusivamente nas regras de negócio e no que existe no mundo real.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[04. Níveis do sgbd e etapas do projeto de banco de dados]], [[05. Modelagem de entidades e tipos de atributos]], [[07. Modelo de entidades e relacionamentos estendido]]

### Modelo físico
* **Definição formal:** A especificação técnica de mais baixo nível, detalhando como os dados são implementados e alocados no hardware e no SGBD específico.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

### Modelo lógico
* **Definição formal:** A representação intermediária dos dados adaptada a um paradigma de banco de dados específico, como o modelo relacional, ainda antes das decisões próprias de um produto de SGBD.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[04. Níveis do sgbd e etapas do projeto de banco de dados]], [[10. Mapeamento de entidades e atributos]]

### Modelo relacional
* **Definição formal:** Modelo formal de banco de dados introduzido por Edgar F. Codd em 1970, baseado na teoria matemática dos conjuntos, onde todos os dados são representados na forma de relações (tabelas).
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]]

---

## N

### NoSQL
* **Definição formal:** Rótulo amplo para famílias de bancos que não usam o modelo relacional clássico como único paradigma principal, incluindo chave-valor, documentos, wide-column e grafos.
* **Modelo mental:** Não é um único modelo concorrente do relacional, mas um conjunto de modelos especializados.
* **Artigo correspondente:** [[13. Bancos de dados não-relacionais]]

### Normalização
* **Definição formal:** Processo sistemático de análise e decomposição de relações com base em chaves e dependências funcionais para reduzir redundância estrutural e anomalias de inserção, atualização e exclusão.
* **Modelo mental:** Um teste de qualidade do esquema que pergunta se cada fato está armazenado na relação determinada pela chave da qual ele realmente depende.
* **Artigo correspondente:** [[12. 1ª, 2ª e 3ª formas normais]]

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

### Princípio do menor privilégio
* **Definição formal:** Regra de segurança segundo a qual cada usuário, serviço ou processo deve receber apenas os privilégios necessários para sua função.
* **Artigo correspondente:** [[14. Segurança de banco de dados]]

### Parcialidade em especializações
* **Definição formal:** Restrição de completude em que podem existir ocorrências do supertipo que não pertencem a nenhum dos subtipos apresentados. Na notação estudada, é indicada por linha simples.
* **Modelo mental:** Responde à pergunta: "toda ocorrência precisa entrar em alguma das categorias?" Na parcialidade, não.
* **Artigo correspondente:** [[07. Modelo de entidades e relacionamentos estendido]]

### Participação Parcial
* **Definição formal:** Restrição estrutural que indica que nem todas as instâncias de uma entidade precisam participar de um relacionamento (cardinalidade mínima = 0, representada por linha simples no DER de Chen).
* **Artigo correspondente:** [[06. Modelagem de relacionamentos, cardinalidade e restrições de participação]]

### Participação Total (Restrição de Existência)
* **Definição formal:** Restrição estrutural que estabelece que toda instância de uma entidade depende obrigatoriamente de sua participação no relacionamento para existir (cardinalidade mínima = 1, representada por linha dupla no DER de Chen).
* **Artigo correspondente:** [[06. Modelagem de relacionamentos, cardinalidade e restrições de participação]], [[07. Modelo de entidades e relacionamentos estendido]]

### Perda de atualização (Lost update)
* **Definição formal:** Falha crítica de concorrência que ocorre quando duas transações leem o mesmo registro simultaneamente e ambas gravam alterações, fazendo com que a última sobrescreva a primeira.
* **Artigo correspondente:** [[02. Abordagem de arquivos vs. abordagem de banco de dados]]

### Primeira Forma Normal (1FN)
* **Definição formal:** Forma normal que, na abordagem didática da disciplina, exige valores atômicos em cada posição da relação e ausência de grupos repetitivos ou atributos multivalorados armazenados em uma única célula.
* **Modelo mental:** Uma posição da tabela deve representar um único valor do domínio.
* **Artigo correspondente:** [[12. 1ª, 2ª e 3ª formas normais]]

### Projeto Conceitual
* **Definição formal:** A primeira etapa do projeto de banco de dados, responsável por produzir um esquema semântico abstrato (MER/DER) a partir dos requisitos do mini-mundo, com independência total de SGBD.
* **Participantes:** Usuários de negócio, Analistas de Sistemas e Administrador de Dados (AD).
* **Artigo correspondente:** [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

### Projeto Físico
* **Definição formal:** A terceira etapa do projeto de banco de dados, responsável por implementar o esquema lógico em um SGBD específico por meio de scripts DDL, definindo tipos nativos, índices e estratégias de armazenamento.
* **Participantes:** Administrador de Banco de Dados (DBA) e Engenheiros de Infraestrutura.
* **Artigo correspondente:** [[04. Níveis do sgbd e etapas do projeto de banco de dados]]

### Projeto Lógico
* **Definição formal:** A segunda etapa do projeto de banco de dados, responsável por transformar o modelo conceitual em um esquema adaptado ao paradigma escolhido, como um esquema relacional estruturado em relações, atributos, PKs e FKs, além de aplicar regras de normalização.
* **Participantes:** Projetistas de Banco de Dados, Arquitetos de Software e Desenvolvedores.
* **Artigo correspondente:** [[04. Níveis do sgbd e etapas do projeto de banco de dados]], [[10. Mapeamento de entidades e atributos]]

### Propriedades ACID
* **Definição formal:** Conjunto de quatro propriedades fundamentais que garantem a confiabilidade de transações em um SGBD: Atomicidade, Consistência, Isolamento e Durabilidade.
* **Artigo correspondente:** [[02. Abordagem de arquivos vs. abordagem de banco de dados]]

---

## R

### Redundância de dados
* **Definição formal:** A repetição desnecessária do mesmo fato em múltiplas tuplas ou relações, aumentando o risco de inconsistência e de anomalias de atualização.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[02. Abordagem de arquivos vs. abordagem de banco de dados]], [[12. 1ª, 2ª e 3ª formas normais]]

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
* **Artigo correspondente:** [[06. Modelagem de relacionamentos, cardinalidade e restrições de participação]], [[11. Mapeamento de relacionamentos]]

### Relacionamento Ternário
* **Definição formal:** Relacionamento que conecta simultaneamente três entidades distintas para completar a semântica da associação de forma atômica.
* **Artigo correspondente:** [[06. Modelagem de relacionamentos, cardinalidade e restrições de participação]], [[07. Modelo de entidades e relacionamentos estendido]], [[11. Mapeamento de relacionamentos]]

### Relacionamento Um para Muitos (1:N)
* **Definição formal:** Mapeamento de cardinalidade máxima no qual uma ocorrência da entidade A pode associar-se a várias da entidade B, mas cada ocorrência de B associa-se a no máximo uma de A.
* **Artigo correspondente:** [[06. Modelagem de relacionamentos, cardinalidade e restrições de participação]], [[11. Mapeamento de relacionamentos]]

### Relacionamento Um para Um (1:1)
* **Definição formal:** Mapeamento de cardinalidade máxima no qual cada ocorrência da entidade A associa-se a no máximo uma ocorrência de B, e vice-versa.
* **Artigo correspondente:** [[06. Modelagem de relacionamentos, cardinalidade e restrições de participação]], [[11. Mapeamento de relacionamentos]]

---

## S

### Segunda Forma Normal (2FN)
* **Definição formal:** Uma relação está na 2FN quando está na 1FN e todo atributo não-primo depende funcionalmente da chave candidata inteira, sem dependências parciais de subconjuntos próprios de chaves compostas.
* **Modelo mental:** Se a chave é composta, nenhum atributo não-chave deve depender só de um pedaço dela.
* **Artigo correspondente:** [[12. 1ª, 2ª e 3ª formas normais]]

### SQL
* **Definição formal:** (*Structured Query Language*) Linguagem padronizada e predominantemente declarativa para definição, consulta, manipulação e controle de dados em SGBDs relacionais.
* **Modelo mental:** Dizemos ao SGBD qual resultado queremos; o otimizador escolhe como executar a consulta.
* **Artigo correspondente:** [[03. Linguagens de banco de dados (ddl e dml) e perfis profissionais]], [[13. Bancos de dados não-relacionais]]

### Sistema de Banco de Dados (SBD)
* **Definição formal:** O ecossistema integrado completo composto pelo Banco de Dados, o SGBD, as aplicações clientes, o hardware e a comunidade de usuários.
* **Artigo correspondente:** [[02. Abordagem de arquivos vs. abordagem de banco de dados]]

### Sistema Gerenciador de Banco de Dados (SGBD)
* **Definição formal:** (*DBMS*) O software de sistema responsável por gerenciar, controlar, proteger, consultar e manter bancos de dados.
* **Artigo correspondente:** [[01. Introdução à modelagem de dados e sua importância]], [[02. Abordagem de arquivos vs. abordagem de banco de dados]]

### Subtipo
* **Definição formal:** Tipo de entidade mais específico que representa um subconjunto das ocorrências de um supertipo, herdando sua estrutura geral e podendo acrescentar atributos e relacionamentos próprios.
* **Artigo correspondente:** [[07. Modelo de entidades e relacionamentos estendido]]

### Supertipo
* **Definição formal:** Tipo de entidade mais geral que concentra atributos e relacionamentos compartilhados por dois ou mais subtipos.
* **Artigo correspondente:** [[07. Modelo de entidades e relacionamentos estendido]]

### Sobreposição (Overlap)
* **Definição formal:** Restrição de uma especialização do MER Estendido que permite que uma mesma ocorrência do supertipo pertença simultaneamente a vários subtipos. É representada por `o`.
* **Modelo mental:** Responde à pergunta: "pode estar em mais de um subtipo ao mesmo tempo?" Na sobreposição, sim.
* **Artigo correspondente:** [[07. Modelo de entidades e relacionamentos estendido]]

---

## T

### Trilha de auditoria
* **Definição formal:** Registro de eventos relevantes para reconstruir ações realizadas no sistema, como usuário, horário, operação e objeto afetado.
* **Modelo mental:** Quem fez o quê e quando?
* **Artigo correspondente:** [[14. Segurança de banco de dados]]

### Tabela associativa
* **Definição formal:** Relação criada no mapeamento de um relacionamento N:N ou N-ário para armazenar as chaves estrangeiras das entidades participantes e os atributos próprios do relacionamento.
* **Modelo mental:** O relacionamento deixa de ser apenas uma linha no DER e ganha uma tabela capaz de registrar cada combinação válida entre os participantes.
* **Artigo correspondente:** [[11. Mapeamento de relacionamentos]]

### TCL (Transaction Control Language)
* **Definição formal:** Subconjunto da linguagem SQL utilizado para gerenciar a execução atômica e consistente de transações no banco de dados (`COMMIT`, `ROLLBACK`, `SAVEPOINT`).
* **Artigo correspondente:** [[03. Linguagens de banco de dados (ddl e dml) e perfis profissionais]]

### Terceira Forma Normal (3FN)
* **Definição formal:** Forma normal em que, além de satisfazer a 2FN, as dependências funcionais não triviais não deixam atributos não-primos transitivamente dependentes de chaves candidatas. Na formulação formal, para toda dependência `X → A`, X deve ser superchave ou A deve ser atributo primo.
* **Modelo mental:** Depois de garantir que os atributos dependem da chave inteira, verificamos se algum atributo não-chave depende de outro atributo não-chave.
* **Artigo correspondente:** [[12. 1ª, 2ª e 3ª formas normais]]

### Tipo chave-valor
* **Definição formal:** Modelo NoSQL em que cada valor é armazenado e recuperado por uma chave associada.
* **Artigo correspondente:** [[13. Bancos de dados não-relacionais]]

### Tipo documento
* **Definição formal:** Modelo NoSQL que armazena registros em documentos autocontidos, frequentemente semelhantes a JSON, com estrutura flexível, arrays e objetos aninhados.
* **Artigo correspondente:** [[13. Bancos de dados não-relacionais]]

### Tipo grafo
* **Definição formal:** Modelo de banco que representa dados por nós e relacionamentos por arestas, podendo ambos possuir propriedades.
* **Artigo correspondente:** [[13. Bancos de dados não-relacionais]]

### Tipo wide-column
* **Definição formal:** Modelo NoSQL baseado em linhas esparsas e famílias de colunas, frequentemente projetado para distribuição horizontal em grande escala.
* **Artigo correspondente:** [[13. Bancos de dados não-relacionais]]

### Tipo de Entidade (Entity Type)
* **Definição formal:** O esquema descritivo formal que define a estrutura e o conjunto de atributos comuns compartilhados por um grupo de entidades similares (análogo a uma Classe na POO).
* **Artigo correspondente:** [[05. Modelagem de entidades e tipos de atributos]]

### Totalidade em especializações
* **Definição formal:** Restrição de completude em que toda ocorrência do supertipo precisa pertencer a pelo menos um dos subtipos da especialização. Na notação estudada, é indicada por linha dupla.
* **Modelo mental:** Responde à pergunta: "toda ocorrência precisa entrar em alguma das categorias?" Na totalidade, sim.
* **Artigo correspondente:** [[07. Modelo de entidades e relacionamentos estendido]]

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
* **Voltar ao artigo 08:** [[08. Conceitos do modelo relacional e chave primária]]
* **Voltar ao artigo 09:** [[09. Integridade referencial e chave estrangeira]]
* **Voltar ao artigo 10:** [[10. Mapeamento de entidades e atributos]]
* **Voltar ao artigo 11:** [[11. Mapeamento de relacionamentos]]
* **Voltar ao artigo 12:** [[12. 1ª, 2ª e 3ª formas normais]]
* **Voltar ao artigo 13:** [[13. Bancos de dados não-relacionais]]
* **Voltar ao artigo 14:** [[14. Segurança de banco de dados]]
* **Resumo da disciplina:** [[00. Modelagem de Dados - Resumo]]
* **Índice geral do vault:** [[index.md|Página Inicial do Vault]]
