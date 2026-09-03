# Prompts de Estudo (LLM) - Design de Interação

Use estes prompts e parâmetros estruturados para estudar, simular provas e receber explicações detalhadas de erros via LLM (ChatGPT, Gemini, Claude, etc.).

---

## 1. Simulador de Prova e Questões Avançadas (Alta Dificuldade)

Copie e cole este prompt para iniciar um simulado com questões no nível de prova universitária/concurso:

```text
Atue como um Professor Doutor em Interação Humano-Computador (IHC) e Design de Interação.

Gere um simulado de [NÚMERO, ex: 5] questões de múltipla escolha ou discursivas sobre os temas abaixo.

Regras de elaboração de questões:
1. Dificuldade Elevada: As perguntas e opções incorretas (distratores) devem exigir análise crítica profunda e distinção teórica rigorosa (ex: Engenharia Cognitiva de Norman vs Engenharia Semiótica de Clarisse de Souza; Golfo de Execução vs Golfo de Avaliação; Método MIS vs MAC; Inspeção Heurística vs Teste de Usabilidade; WCAG 2.1 A/AA/AAA).
2. Cenários Práticos Complexos: Crie cenários de interfaces reais com falhas de usabilidade, desafios de acessibilidade ou problemas de comunicação designer-usuário.
3. Respostas e Distratores Desafiadores: Evite alternativas óbvias ou ingênuas. Todos os distratores devem ser embasados em conceitos reais da área, exigindo que o aluno identifique nuances e ambiguidades sutis.

Tópicos para escolher:
- Engenharia Cognitiva (Norman, Golfos, Ação e Avaliação)
- Engenharia Semiótica (Clarisse de Souza, Signos, Metacomunicação e Preposto)
- Atributos de Qualidade (Usabilidade ISO 9241-11, Comunicabilidade, Acessibilidade WCAG, UX)
- Métodos de Avaliação por Inspeção (Heurísticas de Nielsen, Percurso Cognitivo, MIS)
- Métodos de Avaliação Empírica e Investigação (Teste de Usabilidade, MAC, SUS)
- Princípios e Regras de Design (Gestalt, Regras de Ouro de Shneiderman)

Aguarde minhas respostas antes de fornecer o gabarito.
```

---

## 2. Parâmetros de Feedback e Diagnóstico de Erros (Prompt de Correção)

Após responder ao simulado ou colar uma questão que você errou, use este prompt para a LLM explicar o erro em detalhes:

```text
Analise a resposta que eu forneci para a questão abaixo e diagnostique meus erros utilizando a seguinte estrutura obrigatória de feedback:

1. Diagnóstico do Erro:
   - Tipo de Erro: [Conceitual / Terminológico / Interpretação de Leitura / Aplicação (Heurística/Diretriz) / Confusão Teórica (Cognitiva vs Semiótica) / Distração]
   - Onde errei: Explique exatamente o ponto onde o raciocínio falhou.

2. Explicação da Resposta Correta:
   - Por que a alternativa correta está certa (fundamentação teórica com autores como Norman, Clarisse de Souza, Nielsen, Benyon, Shneiderman ou WCAG).
   - Por que a minha alternativa escolhida está incorreta (desmonte a pegadinha ou a falha do distrator).

3. Ponte Teórica e Revisão Rápida:
   - Apresente um resumo conciso da teoria ou método em questão.
   - Forneça uma dica prática ou macete acadêmico para não errar esse tipo de questão na prova.

Questão: [COLE A QUESTÃO AQUI]
Minha Resposta: [COLE SUA RESPOSTA AQUI]
```

---

## 3. Analisador Heurístico e Semiótico de Interface

```text
Analise o seguinte fluxo ou tela de sistema: [DESCREVA A TELA OU FLUXO].
1. Identifique 3 problemas de usabilidade com base nas 10 Heurísticas de Nielsen.
2. Identifique 1 falha de comunicabilidade sob a perspectiva da Engenharia Semiótica (ruptura na metacomunicação designer-usuário).
3. Proponha correções de design fundamentadas em princípios de Gestalt ou recomendações ergonômicas.
```

---

## 4. Planejador de Avaliação de Sistemas Interativos

```text
Para um sistema interativo do tipo [DESCREVA O SISTEMA], preciso planejar uma avaliação.
1. Qual método de inspeção (Heurística, Percurso Cognitivo ou MIS) é mais adequado para a fase inicial e por quê?
2. Qual método empírico ou por investigação (Teste de Usabilidade formal ou Escala SUS) deve ser aplicado na fase final e como recrutar os participantes?
3. Liste 3 critérios de acessibilidade da WCAG 2.1 (nível AA) essenciais para esse tipo de aplicação.
```
