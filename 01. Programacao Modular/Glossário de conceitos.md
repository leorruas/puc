---
title: "Glossário de conceitos em programação modular"
disciplina: "01. Programacao Modular"
modulo: "Módulo 1: Introdução e conceitos iniciais"
tags:
  - glossario
  - conceitos-fundamentais
  - tipos
  - operacoes
  - modulos
  - atributos
  - goto
  - programacao-modular
relacionados:
  - "[[01. Introdução à programação modular]]"
  - "[[03. Tipos abstratos de dados]]"
  - "[[00. Programação modular - Resumo]]"
---

# Glossário de conceitos em programação modular

> **Contexto:** Guia rápido e comparativo para diferenciar os termos fundamentais da engenharia de software e da programação modular: Tipos, Operações, Módulos, Atributos, Classes, Objetos, Interfaces e a instrução histórica GOTO.

---

## Diferenciação rápida entre os conceitos fundamentais

| Termo | Definição simplificada | O que representa? | Exemplo no código (C# / Teoria) |
| --- | --- | --- | --- |
| **Tipo (*Type*)** | Um conjunto de valores e o conjunto de regras/operações aplicáveis a eles. | O **conceito/definição** do dado | `int`, `string`, `class Conta` |
| **Operação (*Method/Function*)** | Ação, cálculo ou comportamento executado sobre dados. | O **comportamento / "o que faz"** | `Sacar()`, `Depositar()`, `CalcularDV()` |
| **Módulo (*Module*)** | Unidade de organização física ou lógica que agrupa códigos relacionados. | O **container de organização** | Um arquivo `.cs`, `class`, pacote ou biblioteca |
| **Atributo (*Field/Property*)** | Variável interna que guarda o valor do estado de uma entidade. | Os **dados / o estado interno** | `private double _saldo;` |
| **Classe (*Class*)** | O modelo/molde que junta Atributos e Operações para criar um Tipo. | A **planta estrutural** do TAD | `public class Conta { ... }` |
| **Objeto (*Instance*)** | Valor concreto criado na memória com base na especificação de uma Classe. | A **entidade real na memória** | `Conta contaDoZe = new Conta();` |
| **Interface (*Interface*)** | Contrato de operações expostas públicas sem expor a implementação. | O **ponto de comunicação** | `get { return _criacao; }` ou `IMetodo` |
| **Fatores Externos** | Qualidades perceptíveis diretamente pelos usuários na execução do software. | O **valor e utilidade para o usuário** | Corretude, Robustez, Usabilidade, Eficiência |
| **Fatores Internos** | Qualidades técnicas do código-fonte perceptíveis apenas pelos desenvolvedores. | A **sustentação arquitetural do código** | Modularidade, Baixo Acoplamento, Coesão |
| **Corretude / Correção (*Correctness*)** | Capacidade de executar exatamente aquilo que foi especificado nos requisitos sob condições normais. | A **precisão funcional primária** | $2 + 2 = 4$; calcular juros exatos |
| **Robustez (*Robustness*)** | Capacidade de reagir de forma segura diante de entradas anormais ou falhas sem travar (*crash*). | A **tolerância e segurança a imprevistos** | `try / catch`, validação de dados de entrada |
| **Degradação Graciosa (*Graceful Degradation*)** | Capacidade do sistema manter funções essenciais ativas reduzindo a sofisticação sob falhas parciais. | A **resiliência e continuidade de serviço** | Reduzir resolução de vídeo sob oscilação de rede |
| **`GOTO`** | Instrução de salto incondicional de fluxo obsoleta pela Programação Estruturada. | O **controle desestruturado (evitar)** | `goto Rótulo;` (gera *spaghetti code*) |

---

## 1. Tipo (*Type*)

Na Ciência da Computação (e na teoria dos conjuntos), um **Tipo** define o **espaço de valores permitidos** e quais regras/operações podem ser executadas sobre eles.

* **Função:** Impedir que o programa execute operações inválidas (como tentar multiplicar um texto por uma data).
* **Tipos nativos:** `int`, `double`, `bool`.
* **Tipos personalizados (TADs):** `Conta`, `Cliente`, `Pilha`.

---

## 2. Operação (*Operation / Method*)

Uma **Operação** é a abstração executável (uma função ou um procedimento) responsável por processar entradas, realizar cálculos ou modificar o estado dos dados.

* **Abstração de expressão (Função):** Mapeia entradas em um resultado de saída sem que o usuário precise se preocupar com como isso é feito (ex.: `GetSaldo()`, `CalcularPrimeiroDigito()`).
* **Abstração de comando (Procedimento):** Agrupa tarefas repetitivas em blocos de comando isolados sem obrigatoriedade de retorno de valor (ex.: `Depositar(200)`, `ExibirMenu()`).

---

## 3. Módulo (*Module*)

Um **Módulo** é a unidade de fronteira e organização do código. É o invólucro que agrupa funções, variáveis e tipos relacionados em uma entidade delimitada.

* **No nível de arquivo:** Um arquivo de código (ex.: `Validador.cs`).
* **No nível de linguagem:** Uma `class`, um `namespace` ou um módulo de compilação.
* **No nível de arquitetura:** Uma biblioteca (`.dll`), pacote ou microsserviço.

---

## 4. Atributo (*Attribute / Field*)

Um **Atributo** (também chamado de campo ou variável de instância) é onde o estado interno é efetivamente armazenado na memória.

* **Ocultamento da informação:** Em programação modular bem projetada, os atributos são mantidos **privados** (`private`) para que nenhuma parte externa do sistema possa alterá-los sem autorização.
* **Exemplo:** O atributo `_saldo` da conta bancária.

---

## 5. `GOTO` (Salto Incondicional)

A instrução **`GOTO`** é um comando primitivo de desvio incondicional no fluxo de execução que faz a CPU saltar diretamente para qualquer linha marcada por um rótulo no programa.

* **Problema histórico:** Seu uso desordenado originou o chamado *spaghetti code* ("código espaguete"), tornando imprevisível o rastreamento do estado das variáveis e a localização de bugs.
* **Substituição:** O Teorema de Böhm-Jacopini (1966) e o artigo de Dijkstra (1968) provaram que o `GOTO` é desnecessário e deve ser substituído por comandos estruturados (Sequência, Seleção e Repetição).

---

## Analogia do mundo real

Para fixar a diferença de forma intuitiva:

* **Tipo / Classe:** O projeto arquitetônico de um **Carro**.
* **Objeto / Instância:** O carro físico vermelho parado na sua garagem.
* **Atributos (Dados):** O nível de combustível no tanque e a velocidade atual no velocímetro.
* **Operações (Métodos):** Acelerador, freio e troca de marcha.
* **Módulo:** O sistema do motor completo encapsulado sob o capô (onde o motorista interage apenas com os pedais, sem tocar nos pistões).

---

## Referências bibliográficas

* SEBESTA, Robert W. **Conceitos de Linguagens de Programação**. 11. ed. Porto Alegre: Bookman, 2018.
* SOMMERVILLE, Ian. **Engenharia de Software**. 10. ed. São Paulo: Pearson, 2019.
* DIJKSTRA, Edsger W. **Go To Statement Considered Harmful**. Communications of the ACM, v. 11, n. 3, p. 147-148, 1968.

---

## Artigos relacionados e navegação

* **Resumo da disciplina:** [[00. Programação modular - Resumo]]
* **Ver Introdução e Böhm-Jacopini:** [[01. Introdução à programação modular]]
* **Ver Tipos Abstratos de Dados:** [[03. Tipos abstratos de dados]]
* **Índice geral do vault:** [[index.md|Página Inicial do Vault]]
