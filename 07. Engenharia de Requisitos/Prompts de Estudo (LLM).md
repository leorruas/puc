# Prompts de Estudo (LLM) - Engenharia de Requisitos de Software

Use estes prompts e parâmetros estruturados para estudar, simular provas e receber explicações detalhadas de erros via LLM (ChatGPT, Gemini, Claude, etc.).

---

## 1. Simulador de Prova e Questões Avançadas (Alta Dificuldade)

Copie e cole este prompt para iniciar um simulado com questões no nível de prova universitária/concurso:

```text
Atue como um Professor Doutor em Engenharia de Software responsável pela disciplina de Engenharia de Requisitos.

Gere um simulado de [NÚMERO, ex: 5] questões de múltipla escolha ou discursivas sobre os temas abaixo.

Regras de elaboração de questões:
1. Dificuldade Elevada: As perguntas e opções incorretas (distratores) devem exigir análise crítica profunda, distinção de conceitos sutis (ex: Verificação vs Validação, Requisito Não-Funcional de Produto vs Organizacional, Agregação vs Composição na UML, RTM vs Matriz de Rastreabilidade).
2. Cenários Práticos Complexos: Crie cenários reais de projetos de software com ambiguidades, restrições e conflitos de negócio.
3. Respostas e Distratores Desafiadores: Não inclua alternativas absurdamente erradas ou fáceis. Todos os distratores devem parecer plausíveis para quem estudou superficialmente.

Tópicos para escolher:
- Elicitação de requisitos e suas 6 técnicas
- Requisitos funcionais, não-funcionais (categorias Sommerville) e níveis de abstração
- Escrita de requisitos de qualidade (ISO/IEEE 29148)
- Modelagem UML: Casos de Uso, Diagrama de Classes (multiplicidades e relacionamentos) e Diagrama de Pacotes (Layering, CCP, CRP, REP)
- Verificação, Validação e Inspeções Fagan

Aguarde minhas respostas antes de fornecer o gabarito.
```

---

## 2. Parâmetros de Feedback e Diagnóstico de Erros (Prompt de Correção)

Após responder ao simulado ou colar uma questão que você errou, use este prompt para a LLM explicar o erro em detalhes:

```text
Analise a resposta que eu forneci para a questão abaixo e diagnostique meus erros utilizando a seguinte estrutura obrigatória de feedback:

1. Diagnóstico do Erro:
   - Tipo de Erro: [Conceitual / Leitura de Cenário / Confusão de Nomenclatura / Aplicação Incorreta de Regra]
   - Onde errei: Explique exatamente o ponto onde o raciocínio falhou.

2. Explicação da Resposta Correta:
   - Por que a alternativa correta está certa (fundamentação teórica com autores como Sommerville, Bezerra, Pressman ou normas ISO/IEEE).
   - Por que a minha alternativa escolhida está incorreta (desmonte a pegadinha ou a falha do distrator).

3. Ponte Teórica e Revisão Rápida:
   - Apresente um resumo conciso do conceito que preciso revisar.
   - Forneça uma dica prática ou macete acadêmico para não errar esse tipo de questão na prova.

Questão: [COLE A QUESTÃO AQUI]
Minha Resposta: [COLE SUA RESPOSTA AQUI]
```

---

## 3. Gerador de Casos de Uso e User Stories Detalhadas

```text
Com base no seguinte contexto de sistema: [DESCREVA O SISTEMA], gere:
1. Uma Especificação Textual Completa de Caso de Uso (Fluxo Principal, Fluxos Alternativos e Exceções, Pré-condições e Pós-condições).
2. Duas Histórias de Usuário (User Stories) no padrão 'Como [papel], Eu quero [ação], Para que [valor]', com Critérios de Aceitação em formato Given/When/Then (Dado/Quando/Então).
3. Identifique 2 Requisitos Não-Funcionais associados a esse fluxo, classificando-os segundo Sommerville (Produto, Organizacional ou Externo).
```

---

## 4. Analisador de Diagramas UML (Classes, Pacotes e Casos de Uso)

```text
Dado o seguinte cenário de modelagem UML: [DESCREVA AS ENTIDADES OU REGRAS DE NEGÓCIO]
1. Explique como modelar a relação entre essas entidades usando o Diagrama de Classes (especifique se deve ser Associação, Agregação, Composição ou Herança e justifique a decisão com base na dependência do ciclo de vida).
2. Indique as multiplicidades em ambas as extremidades.
3. Se fôssemos organizar essas classes em pacotes, quais princípios de coesão (CCP, CRP ou REP) seriam aplicados?
```
