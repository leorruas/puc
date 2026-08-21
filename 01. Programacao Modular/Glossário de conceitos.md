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
| **Classe (*Class*)** | O modelo, molde ou especificação abstrata que junta Atributos e Métodos. | A **planta estrutural** do TAD | `public class Conta { ... }` |
| **Objeto (*Object / Instance*)** | Entidade viva e concreta alocada na memória RAM a partir do molde da Classe. | A **entidade real na memória** | `Conta contaDoZe = new Conta();` |
| **Atributo (*Field / Property*)** | Variável interna da classe que armazena os dados que compõem o estado do objeto. | Os **dados estruturais** | `private double _saldo;` |
| **Estado (*State*)** | O conjunto exato de valores que todos os atributos do objeto possuem em um dado instante. | A **fotografia/momento do dado** | `_saldo = 500.00; _titular = "Leo";` |
| **Método / Operação (*Method*)** | Sub-rotina (função ou procedimento) que define o comportamento e manipula o estado. | O **comportamento / "o que faz"** | `Sacar()`, `Depositar()`, `CalcularDV()` |
| **Interface (*Interface*)** | Contrato de operações e métodos expostos publicamente sem revelar a implementação. | O **ponto de comunicação** | `public void Sacar()`, `get / set` |
| **Declaração (*Declaration / Declarar*)** | Ato de informar ao compilador a existência, nome e tipo de um identificador (variável, método ou classe) antes de seu uso. | A **reserva de identidade e tipo** | `double saldo;`, `void Sacar();` |
| **Parâmetro (*Parameter*)** | Variável declarada na assinatura de uma sub-rotina para receber dados de entrada. | O **espaço reservado / molde de entrada** | `double valor` em `void Depositar(double valor)` |
| **Argumento (*Argument*)** | Valor real e concreto passado para a sub-rotina no momento em que ela é chamada. | O **dado concreto enviado** | `150.00` em `conta.Depositar(150.00);` |
| **Módulo (*Module*)** | Unidade de organização física ou lógica que agrupa códigos relacionados. | O **container de organização** | Um arquivo `.cs`, `class`, pacote ou biblioteca |
| **Qualidade de Código** | Grau em que o software atende a fatores externos (usuário) e internos (manutenibilidade). | O **valor e longevidade do sistema** | ISO/IEC 25010, Código Limpo (*Clean Code*) |
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

## 5. Estado (*State*)

O **Estado** de um objeto é a **configuração exata de valores que seus atributos possuem em um determinado instante de tempo**.

* **Analogia de Feynman:** Uma **fotografia instantânea** de uma pessoa. Na foto das 10h ela está sentada e de óculos; na foto das 14h ela está em pé e correndo. A pessoa é o mesmo objeto, mas seu estado mudou.
* **Mutabilidade:** O estado de um objeto é alterado ao longo da execução exclusivamente através da chamada de seus **métodos**.

---

## 6. Método (*Method*)

Um **Método** é uma sub-rotina (função ou procedimento) declarada dentro do escopo de uma classe que define o **comportamento** dos objetos daquele tipo.

* **Função no TAD:** O método é o único canal legítimo para consultar ou modificar os atributos privados encapsulados.
* **Exemplo:** `Depositar(valor)` altera o estado aumentando o saldo; `ObterSaldo()` lê o estado atual e o retorna.

---

## 7. Qualidade de Código (*Code Quality*)

A **Qualidade de Código** mede o equilíbrio entre a satisfação das necessidades do usuário (**Fatores Externos** como Corretude e Robustez) e a sustentabilidade técnica da arquitetura para a equipe de engenharia (**Fatores Internos** como Legibilidade, Baixo Acoplamento e Modularidade).

---

## 8. Declaração em Computação (*Declaration / Declarar*)

Na Ciência da Computação, **Declarar** é o ato formal de **apresentar um identificador ao compilador/interpretador**, especificando seu **nome** e seu **tipo de dado**, antes que ele possa ser utilizado pelo programa.

* **Analogia de Feynman:** **Fazer uma certidão de nascimento** ou reservar um crachá em um evento. Você avisa aos organizadores: *"Existirá uma pessoa chamada Leo que é um Aluno"*. Você reservou a identidade e o papel formal, mesmo antes de o crachá receber o número da mesa.
* **A tríade fundamental da computação:**
  1. **Declaração (*Declaration*):** Apresenta o nome e o tipo ao compilador (`double saldo;`).
  2. **Inicialização (*Initialization*):** Atribui o primeiro valor à variável na memória (`saldo = 0.0;`).
  3. **Definição / Instanciação (*Instantiation*):** Constrói e aloca fisicamente o espaço na memória RAM (`Conta c = new Conta();`).
* **Importância:** Linguagens com tipagem estática (C#, Java, C++) exigem a declaração prévia para garantir **segurança de tipos (*Type Safety*)** em tempo de compilação, impedindo operações ilegais.

---

## 9. Parâmetro vs. Argumento (*Parameter vs. Argument*)

Embora no dia a dia muitos usem esses termos como sinônimos, na Engenharia de Software e na Teoria das Linguagens há uma distinção formal muito clara:

* **Parâmetro Formal (*Parameter*):** É a **variável declarada na assinatura da sub-rotina** que atua como um espaço reservado (*placeholder*), definindo o tipo e o nome do dado que a função espera receber.
  - *Analogia de Feynman:* A **abertura da caixa de correio** com o tamanho certo para receber cartas.
  - *Exemplo:* Em `void Depositar(double valor)`, `double valor` é o **parâmetro**.
* **Argumento Real (*Argument*):** É o **valor real e concreto fornecido à sub-rotina** no momento em que ela é invocada/chamada na execução.
  - *Analogia de Feynman:* A **carta física de 50 gramas** que você coloca dentro da caixa de correio.
  - *Exemplo:* Em `conta.Depositar(150.00)`, o número `150.00` é o **argumento**.

---

## 10. `GOTO` (Salto Incondicional)

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
