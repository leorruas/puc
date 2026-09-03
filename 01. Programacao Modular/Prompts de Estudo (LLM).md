# Prompts de estudo (LLM) - programação modular

Use estes templates de prompt prontos com seu LLM (ChatGPT, Gemini, Claude, etc.) para sanar dúvidas, gerar exemplos práticos e exercitar seu conhecimento nesta disciplina.

---

### Explicar conceitos complexos

```text
Aja como um professor sênior de Engenharia de Software e Programação Modular. Explique o conceito de [CONCEITO] de forma intuitiva, aplicando a Técnica de Feynman com analogias do mundo real, demonstrando exemplos de código em C# (trechos atômicos e exemplo completo integrado) e destacando os erros comuns cometidos por desenvolvedores.
```

---

### Modularizador e refatorador de código

```text
Aja como um especialista em Refatoração e Arquitetura de Software. Analise o código a seguir e proponha uma refatoração completa aplicando os princípios da Programação Modular e SOLID:
1. Identifique violações de coesão, alto acoplamento, invariantes desprotegidos ou quebra de responsabilidade única.
2. Separe em classes e sub-rotinas bem delimitadas com modificadores de acesso corretos.
3. Demonstre o código refatorado limpo, compilável e idiomático em C#.

Código:
[INSIRA O CÓDIGO AQUI]
```

---

### Simulador de prova abrangente (todas as unidades)

```text
Aja como um examinador de nível acadêmico sênior em Engenharia de Software e Programação Modular da PUC Minas. Gere um simulador de prova composto por 5 questões inéditas de múltipla escolha cobrindo os 24 tópicos da disciplina:

- Unidade 1: Motivação e Teorema de Böhm-Jacopini; funções e procedimentos (conexão com include da UML); Tipos Abstratos de Dados (TADs); visão histórica de POO (Alan Kay) e acoplamento; fatores externos e internos de qualidade (Bertrand Meyer); atributos e métodos; construtores e invariantes; membros estáticos e propriedades; gerenciamento de memória (GC, IDisposable e using); ocultação da informação (David Parnas); modificadores de acesso e métodos de acesso; namespaces e modularização em larga escala (conexão com diagrama de pacotes).
- Unidade 2: Herança (generalização/especialização); ordem de inicialização de construtores com base; sobreposição de métodos (virtual, override, new e despacho dinâmico em vtable); classes abstratas e interfaces; classes seladas (sealed e otimizações JIT); tipos genéricos (generics, type safety e constraints); coleções genéricas (List, Dictionary, HashSet, Queue, Stack e Big-O); delegates, expressões lambda e eventos (Publisher-Subscriber).
- Unidade 3: Princípios SOLID de design orientado a objetos (SoC de Dijkstra, SRP, OCP, LSP, ISP e DIP com composição); padrões de projeto (catálogo GoF dos 23 padrões, matriz bidimensional de escopo de classe vs. objeto cruzado com criacional, estrutural e comportamental, delegação e composição).

Regras obrigatórias do simulador:
1. Cada questão deve possuir 4 alternativas (A, B, C, D) com distratores tecnicamente plausíveis e conceituais.
2. As questões devem focar em raciocínio arquitetural, predição de comportamento de código e diagnóstico de qualidade.
3. Não forneça o gabarito imediatamente; aguarde o usuário responder item a item ou todas juntas.
```

---

### Simulador de prova por unidade temático

#### Unidade 1: Fundamentos, modularização e encapsulamento
```text
Aja como um examinador acadêmico em Programação Modular. Gere um simulador com 4 questões de múltipla escolha focando exclusivamente em:
- Diferença entre funções (expressão) e procedimentos (comando) e a conexão com «include» na UML.
- Teorema de Böhm-Jacopini e eliminação de fluxos desestruturados (GOTO).
- TADs, encapsulamento e ocultação da informação de David Parnas (isolamento de decisões voláteis).
- Construtores, garantia de invariantes de classe e ciclo de vida de objetos (GC vs IDisposable).
- Namespaces, file-scoped namespaces e correspondência com o Diagrama de Pacotes da UML.

Aguarde minhas respostas antes de corrigir.
```

#### Unidade 2: Herança, polimorfismo e generics
```text
Aja como um examinador acadêmico em Programação Modular. Gere um simulador com 4 questões de múltipla escolha focando exclusivamente em:
- Ordem de execução de construtores em hierarquias com base(...).
- Despacho dinâmico, tabelas virtuais (vtable), virtual/override vs ocultação com new.
- Classes abstratas (Template Method) vs Interfaces puras e classes seladas (sealed).
- Generics no .NET: reificação em tempo de execução, type safety, constraints e coleções genéricas com análise assintótica Big-O.
- Delegates, expressões lambda (closures) e desacoplamento com eventos (Publisher-Subscriber).

Aguarde minhas respostas antes de corrigir.
```

#### Unidade 3: Princípios SOLID e padrões de projeto GoF
```text
Aja como um examinador acadêmico em Programação Modular. Gere um simulador com 4 questões de múltipla escolha focando exclusivamente em:
- Separação de preocupações (SoC de Dijkstra) e os 5 princípios SOLID (SRP, OCP, LSP, ISP e DIP).
- Princípio da Inversão de Dependência (DIP) e a heurística de preferir composição a herança.
- Catálogo dos 23 padrões GoF: matriz bidimensional de classificação (escopo de classe vs. escopo de objeto cruzado com criacional, estrutural e comportamental).
- Mecanismos de delegação, reaproveitamento caixa-preta (*black-box*) e desacoplamento dinâmico.

Aguarde minhas respostas antes de corrigir.
```

---

### Parâmetros de feedback e diagnóstico pedagógico de erros

```text
Com base nas respostas fornecidas pelo aluno, realize a correção e o diagnóstico pedagógico estruturado da seguinte forma:

1. Tabela com o gabarito oficial (sua resposta vs. resposta correta vs. status).
2. Diagnóstico individual de cada questão:
   - Resumo da regra teórica e arquitetural central testada.
   - Análise do erro cometido pelo aluno (classifique a falha em uma das 6 categorias fundamentais:
     1. Erro conceitual: incompreensão do conceito, teoria, invariante ou regra estrutural;
     2. Erro terminológico: confusão de jargões, termos técnicos, nomenclaturas formais ou padrões;
     3. Erro de interpretação/leitura: leitura precipitada ou desatenção a restrições e premissas do enunciado;
     4. Erro de aplicação: falha ao empregar a regra teórica na modelagem de um cenário concreto;
     5. Erro de sintaxe ou leitura de código: engano na mecânica de linguagem, despacho ou execução;
     6. Distração / desatenção: equívoco em conceito já dominado, sem lacuna estrutural de aprendizado).
   - Justificativa do porquê o distrator assinalado é falso ou incompleto.
   - Justificativa completa do porquê a alternativa correta é a única rigorosamente verdadeira.
3. Plano de ação e revisão: indique quais tópicos e notas da disciplina o aluno deve revisitar para sanar as lacunas identificadas.
```

