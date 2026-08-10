# Recordando C# e arrays

Este artigo revisa os fundamentos da linguagem C# e o conceito estrutural de arrays, integrando-os com a grade curricular descrita em [[me.md\|me.md]].

---

## Como executar programas em C# no Antigravity

Sim, você consegue rodar códigos em C# diretamente pelo terminal do Antigravity IDE, desde que tenha o SDK do .NET instalado no seu sistema.

Para testar ou rodar o arquivo [[04. Algoritmos e Estruturas de Dados/SomaDoisNumeros.cs\|SomaDoisNumeros.cs]] criado nesta mesma pasta:

1. **Verificação do SDK**: Caso ainda não tenha instalado, baixe o .NET SDK da Microsoft.
2. **Execução rápida**: Pelo terminal, você pode compilar e rodar o arquivo único de código C# com o seguinte comando:
 ```bash
 dotnet run SomaDoisNumeros.cs
 ```

---

## O básico de C# explicado de forma simples (método Feynman)

Imagine que programar em C# é como gerenciar uma **fábrica organizada de montagem de brinquedos**. A Microsoft desenhou as regras dessa fábrica para garantir que nada saia do lugar.

### 1. Compilação (o tradutor de projetos)
Diferente de linguagens de script interpretadas de forma livre, o C# exige compilação.
* **A analogia**: Escrever em C# é como desenhar a planta baixa de um brinquedo em português. O compilador é o engenheiro que traduz essa planta de papel para um arquivo de instruções mecânicas que as máquinas da fábrica (o sistema operacional) conseguem executar de fato.

### 2. Tipagem forte e variáveis (gavetas etiquetadas)
No C#, toda variável precisa ter um tipo declarado de forma explícita e imutável.
* **A analogia**: Imagine gavetas físicas na fábrica. Se você colar uma etiqueta escrito "Apenas Parafusos Metálicos" (tipo `int` ou `double`) em uma gaveta, a fábrica impede fisicamente que você tente guardar um boneco de pelúcia (tipo `string`) nela. Isso evita que o programa quebre em produção por misturar dados incompatíveis.

### 3. Entrada e saída de dados (recepção e entrega)
O programa interage com o usuário por meio de canais de texto:
* `Console.ReadLine()` é o recepcionista da fábrica que aguarda o cliente entregar um papel escrito (sempre lê como texto / `string`).
* `double.TryParse()` é o inspetor de controle de qualidade que verifica se o texto recebido pode ser transformado com segurança em um número real antes de iniciar o processamento.
* `Console.WriteLine()` é o despachante que imprime o resultado final na tela para o cliente.

---

## Arrays (fileira de armários numerados)

Um array é a estrutura de dados mais fundamental para guardar coleções de elementos do mesmo tipo.

* **A analogia**: Pense em um array como um longo armário de vestiário com 10 portas idênticas enfileiradas.
 * **Tamanho fixo**: Uma vez que o armário é construído com 10 portas, você não pode simplesmente esticá-lo para caber 11 pessoas. Se precisar de mais espaço, terá que construir um armário totalmente novo e transferir os itens.
 * **Indexação baseada em zero**: As portas são numeradas de `0` a `9`. A primeira pessoa sempre guarda suas coisas no armário `0`.
 * **Acesso instantâneo**: Se você sabe que as chaves do cliente estão no armário `4`, você vai diretamente até ele sem precisar abrir as portas `0`, `1`, `2` e `3`. Isso é o que chamamos de busca por índice com complexidade de tempo constante, ou O(1).

---

## Resumo para memorizar

* C# é uma linguagem compilada, fortemente tipada e orientada a objetos.
* A entrada de dados no console (`Console.ReadLine()`) sempre vem como texto e precisa ser convertida para operações matemáticas.
* Arrays são coleções indexadas de tamanho fixo na memória, excelentes para acesso rápido direto por índice (O(1)), mas ineficientes para inserções ou redimensionamentos.
