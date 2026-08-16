---
title: "Guia multilinguagem de sintaxe, estruturas e práticas"
disciplina: "00. Geral"
modulo: "Referência Transversal de Programação"
tags:
  - sintaxe
  - multilinguagem
  - algoritmo
  - csharp
  - java
  - python
  - javascript
relacionados:
  - "[[01. Programacao Modular/00. Programação modular - Resumo]]"
  - "[[01. Programacao Modular/01. Introdução à programação modular]]"
  - "[[01. Programacao Modular/02. Funções e procedimentos]]"
---

# Guia multilinguagem de sintaxe, estruturas e práticas

> **Contexto:** Referência transversal para o aprendizado prático de estruturas de controle, tipos de dados, abstrações de sub-rotinas e elementos modulares em múltiplas linguagens (C#, Java, Python e JavaScript/TypeScript). Inclui explicação teórica de funcionamento, equivalência sintática, armadilhas comuns e exercícios de fixação.

---

## Como utilizar este guia

Este documento funciona como um **hub central de sintaxe e prática**. Cada seção aborda um conceito fundamental de construção de software dividido em quatro partes:

1. **Como funciona (Teoria e Mecânica):** Explicação conceitual de como a CPU/linguagem executa a instrução.
2. **Comparativo Multilinguagem:** Exemplos lado a lado em C#, Java, Python e JavaScript.
3. **Armadilhas Comuns:** Erros frequentes de iniciantes (ex.: laço infinito, escopo de variável, comparação de igualdade).
4. **Exercício de Prática:** Desafio prático com requisitos claros para implementação.

---

## 1. Comandos sequenciais e atribuição de variáveis

### Como funciona
A execução sequencial é o fluxo padrão de um algoritmo: as instruções são executadas uma após a outra, de cima para baixo, na ordem em que foram escritas. A atribuição armazena o resultado de uma expressão em uma região de memória rotulada por um nome (variável).

### Comparativo de sintaxe

| Linguagem | Tipagem | Exemplo de código |
| --- | --- | --- |
| **C#** | Estática / Forte | `int idade = 25; string nome = "Ana";` |
| **Java** | Estática / Forte | `int idade = 25; String nome = "Ana";` |
| **Python** | Dinâmica / Forte | `idade = 25; nome = "Ana"` |
| **JavaScript** | Dinâmica / Fraca | `let idade = 25; const nome = "Ana";` |

### Armadilhas comuns
* **Diferença entre `=` e `==`:** `=` atribui valor; `==` compara igualdade.
* **Escopo de variáveis:** Declarar uma variável dentro de um bloco e tentar acessá-la fora gera erro de compilação em C#/Java/JS (`let`).

### Exercício de prática
* **Desafio:** Crie um algoritmo que leia a temperatura em Celsius, converta para Fahrenheit ($F = C \times 1.8 + 32$) e exiba o resultado formatado.

---

## 2. Comandos de seleção simples e composta (`if`, `else if`, `else`)

### Como funciona
Avalia uma expressão booleana (verdadeira ou falsa). Se a condição for verdadeira (`true`), o bloco associado é executado. Se for falsa (`false`), o fluxo salta para a próxima condição (`else if`) ou para o bloco alternativo (`else`).

### Comparativo de sintaxe

==== C# / Java / JavaScript
```csharp
int nota = 85;

if (nota >= 90) {
    Console.WriteLine("Aprovado com distinção");
} else if (nota >= 60) {
    Console.WriteLine("Aprovado");
} else {
    Console.WriteLine("Reprovado");
}
```

==== Python
```python
nota = 85

if nota >= 90:
    print("Aprovado com distinção")
elif nota >= 60:
    print("Aprovado")
else:
    print("Reprovado")
```

### Armadilhas comuns
* **Ordem das condições:** Colocar uma condição genérica antes de uma específica impede que a específica seja testada.
* **Indentação em Python:** A ausência de chaves `{}` torna a indentação (espaçamento) parte da sintaxe obrigatória.

---

## 3. Comandos de seleção múltipla (`switch` / `match`)

### Como funciona
Avalia o valor de uma única variável contra múltiplos casos possíveis (*cases*). É mais legível e eficiente do que encadear dezenas de `if / else if`.

### Comparativo de sintaxe

==== C#
```csharp
int dia = 2;
switch (dia) {
    case 1: Console.WriteLine("Domingo"); break;
    case 2: Console.WriteLine("Segunda"); break;
    default: Console.WriteLine("Dia inválido"); break;
}
```

==== Java
```java
int dia = 2;
switch (dia) {
    case 1 -> System.out.println("Domingo");
    case 2 -> System.out.println("Segunda");
    default -> System.out.println("Dia inválido");
}
```

==== Python (3.10+)
```python
dia = 2
match dia:
    case 1: print("Domingo")
    case 2: print("Segunda")
    case _: print("Dia inválido")
```

==== JavaScript
```javascript
let dia = 2;
switch (dia) {
    case 1: console.log("Domingo"); break;
    case 2: console.log("Segunda"); break;
    default: console.log("Dia inválido"); break;
}
```

### Armadilhas comuns
* **Esquecer o `break` (Fallthrough):** Sem `break` em C#/JS, a execução "cai" nos casos seguintes mesmo que a condição não seja verdadeira.

---

## 4. Comandos de repetição pré-testados (`while`)

### Como funciona
Avalia uma condição booleana **antes** de cada iteração. Enquanto a condição for verdadeira, o bloco de código dentro do laço é repetido. Se a condição for falsa na primeira avaliação, o bloco nunca é executado.

### Comparativo de sintaxe

==== C# / Java
```csharp
int contador = 1;
while (contador <= 5) {
    Console.WriteLine($"Contagem: {contador}");
    contador++;
}
```

==== Python
```python
contador = 1
while contador <= 5:
    print(f"Contagem: {contador}")
    contador += 1
```

==== JavaScript
```javascript
let contador = 1;
while (contador <= 5) {
    console.log(`Contagem: ${contador}`);
    contador++;
}
```

### Armadilhas comuns
* **Laço infinito:** Esquecer de atualizar a variável de controle (`contador++` ou `contador += 1`) dentro do corpo do laço.

---

## 5. Comandos de repetição contados (`for`)

### Como funciona
Utilizado quando se sabe previamente o número de iterações. Combina em uma única linha a inicialização de uma variável contadora, a condição de parada e o incremento.

### Comparativo de sintaxe

==== C# / Java / JavaScript
```csharp
for (int i = 0; i < 5; i++) {
    Console.WriteLine($"Índice: {i}");
}
```

==== Python
```python
for i in range(5):
    print(f"Índice: {i}")
```

### Armadilhas comuns
* **Erro Off-by-One (Estouro de limite):** Iterar até `i <= lista.Length` em vez de `i < lista.Length` causa erro de índice fora dos limites.

---

## 6. Comandos de repetição pós-testados (`do-while`)

### Como funciona
Executa o bloco de código **pelo menos uma vez** antes de testar a condição no final. É ideal para menus interativos e validação de entrada de dados do usuário.

### Comparativo de sintaxe

==== C# / Java / JavaScript
```csharp
int opcao;
do {
    opcao = LerOpcao();
} while (opcao != 0);
```

==== Python (Emulação do `do-while`)
```python
# Python não possui a palavra-chave 'do-while' nativa; emula-se com while True e break
while True:
    opcao = ler_opcao()
    if opcao == 0:
        break
```

---

## 7. Sub-rotinas: Funções vs. Procedimentos

### Como funciona
* **Função (Abstração de Expressão):** Recebe parâmetros de entrada, processa e **retorna obrigatoriamente um valor**. É usada em atribuições (`x = calcular()`).
* **Procedimento (Abstração de Comandos):** Executa uma sequência de instruções de ação (E/S, telas, gravações) e **não retorna valor** (`void` em C#/Java).

### Comparativo de sintaxe

==== C#
```csharp
// Procedimento (void)
public static void ExibirMensagem(string texto) {
    Console.WriteLine(texto);
}

// Função (retorna int)
public static int Somar(int a, int b) {
    return a + b;
}
```

==== Java
```java
// Procedimento
public static void exibirMensagem(String texto) {
    System.out.println(texto);
}

// Função
public static int somar(int a, int b) {
    return a + b;
}
```

==== Python
```python
# Procedimento (retorna None implicitamente)
def exibir_mensagem(texto):
    print(texto)

# Função (retorna valor explicitamente)
def somar(a, b):
    return a + b
```

==== JavaScript
```javascript
// Procedimento
function exibirMensagem(texto) {
    console.log(texto);
}

// Função
function somar(a, b) {
    return a + b;
}
```

---

## 8. Abstração e Encapsulamento com Classes (TADs)

### Como funciona
Unifica estado (atributos privados) e comportamento (métodos públicos) em uma classe. Garante que os dados internos não sejam corrompidos por acesso direto não autorizado.

### Comparativo de sintaxe

==== C#
```csharp
public class ContaBancaria {
    private double _saldo;

    public ContaBancaria(double saldoInicial) {
        _saldo = saldoInicial;
    }

    public void Depositar(double quantia) {
        if (quantia > 0) _saldo += quantia;
    }

    public double GetSaldo() => _saldo;
}
```

==== Java
```java
public class ContaBancaria {
    private double saldo;

    public ContaBancaria(double saldoInicial) {
        this.saldo = saldoInicial;
    }

    public void depositar(double quantia) {
        if (quantia > 0) this.saldo += quantia;
    }

    public double getSaldo() {
        return this.saldo;
    }
}
```

==== Python
```python
class ContaBancaria:
    def __init__(self, saldo_inicial):
        self._saldo = saldo_inicial # Prefixo _ indica atributo privado por convenção

    def depositar(self, quantia):
        if quantia > 0:
            self._saldo += quantia

    def get_saldo(self):
        return self._saldo
```

---

## Plano de prática e exercícios recomendados

Para consolidar o aprendizado em cada linguagem:

1. **Nível 1 (Lógica Básica):** Escreva um algoritmo de validação de idade (maioridade) em C# e Python.
2. **Nível 2 (Repetição e Funções):** Implemente a função de cálculo do Dígito Verificador do CPF em C# e JavaScript.
3. **Nível 3 (Encapsulamento e TAD):** Crie uma classe `Retangulo` com atributos privados `largura` e `altura` e métodos públicos para calcular área e perímetro em C# e Java.

---

## Referências bibliográficas

* SEBESTA, Robert W. **Conceitos de Linguagens de Programação**. 11. ed. Porto Alegre: Bookman, 2018.
* WIRTH, Niklaus. **Algorithms + Data Structures = Programs**. Prentice-Hall, 1976.

---

## Artigos relacionados e navegação

* **Resumo de Programação Modular:** [[01. Programacao Modular/00. Programação modular - Resumo]]
* **Voltar para o Glossário:** [[01. Programacao Modular/Glossário de conceitos]]
* **Página Inicial do Vault:** [[index.md|Página Inicial do Vault]]
