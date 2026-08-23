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
| **Assinatura de Método (*Signature*)** | Par composto pelo nome da sub-rotina + quantidade, tipos e ordem dos parâmetros. | O **RG / CPF identificador do método** | `Sacar(double)` vs `Sacar(double, string)` |
| **Semântica de Referência (*Reference Semantics*)** | Modelo onde variáveis guardam ponteiros/endereços de memória do *Heap* e não o objeto em si. | A **comunicação por controle remoto** | `Conta c2 = c1;` (ambas apontam para o mesmo objeto) |
| **Coletor de Lixo (*Garbage Collector*)** | Mecanismo automático do runtime (.NET/JVM) que rastreia e libera memória de objetos inacessíveis. | O **caminhão de reciclagem de memória** | Executa em segundo plano liberando instâncias órfãs |
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

## 9. Assinatura de Método (*Method Signature*)

Na Engenharia de Software, a **Assinatura de um Método** é a impressão digital única (*fingerprint*) que o compilador utiliza para diferenciar uma sub-rotina de todas as outras dentro de uma classe.

* **O que COMPÕE a assinatura em C# e Java:**
  1. O **Nome** do método ou construtor (ex.: `Depositar`).
  2. A **Quantidade** de parâmetros.
  3. Os **Tipos de Dados** dos parâmetros e sua **Ordem exata** (ex.: `(string, double)` $\neq$ `(double, string)`).
* **O que NÃO faz parte da assinatura:**
  - O modificador de acesso (`public`, `private`).
  - O tipo de retorno (`void`, `double`, `int`).
  - Os nomes internos dos parâmetros (apenas seus tipos importam).
* **Analogia de Feynman:** O **CPF / RG do Método**. Duas pessoas podem se chamar "João", mas são diferenciadas pelo número do documento. No código, você pode ter dez métodos chamados `Calcular`, desde que cada um tenha uma "lista de tipos" diferente (**Sobrecarga / *Overloading***).

---

## 10. Semântica de Referência (*Reference Semantics*)

A **Semântica de Referência** é o modelo de gerenciamento de dados em linguagens como C# e Java no qual uma variável associada a uma classe **não contém os dados do objeto em si**, mas sim um **ponteiro / endereço de memória** que aponta para o local no *Heap* onde o objeto físico foi construído.

* **Analogia de Feynman:** O **controle remoto da televisão**. Se você der o seu controle remoto extra para um amigo (`Conta c2 = c1;`), vocês agora têm dois controles diferentes, mas **ambos controlam a exata mesma televisão na sala**. Se o seu amigo mudar de canal (`c2.Depositar(100)`), você imediatamente verá o novo saldo na sua tela (`c1.ObterSaldo()`).
* **Diferença para Tipos de Valor (*Value Semantics*):** Tipos primitivos (`int a = 10; int b = a;`) criam uma **cópia independente** do valor (como fotocopiar uma folha de papel: rabiscar a cópia não altera o original).
* **Conexão com Construtores:** O operador `new` aciona o construtor, constrói a televisão na memória *Heap* e devolve a frequência/endereço de rádio para ser gravada na variável de referência.

---

## 11. Coletor de Lixo (*Garbage Collector - GC*)

O **Coletor de Lixo (*Garbage Collector*)** é um componente interno do ambiente de execução (*runtime* do .NET CLR ou Java JVM) responsável pelo **gerenciamento automático de memória**. Ele monitora a memória *Heap*, identifica objetos que não podem mais ser alcançados por nenhuma variável de referência do programa e desaloca esse espaço automaticamente.

* **Analogia de Feynman:** O **caminhão de reciclagem da cidade**. Enquanto você estiver usando um móvel na sua casa (tiver uma referência na *Stack* apontando para ele), ele permanece seguro. No momento em que você corta a conexão (`conta = null;` ou a variável local sai de escopo), aquele móvel se torna "lixo órfão". O caminhão de reciclagem passa periodicamente em segundo plano, recolhe o móvel e libera o espaço para novas compras (`new`), impedindo o entupimento da casa (**vazamentos de memória / *Memory Leaks***).
* **Ciclo de Vida Complementar:** O **Construtor** é a maternidade que dá a vida ao objeto; o **Garbage Collector** é o serviço de limpeza que encerra o ciclo de vida e recupera a memória RAM.

---

## 12. Parâmetro vs. Argumento (*Parameter vs. Argument*)

Embora no dia a dia muitos usem esses termos como sinônimos, na Engenharia de Software e na Teoria das Linguagens há uma distinção formal muito clara:

* **Parâmetro Formal (*Parameter*):** É a **variável declarada na assinatura da sub-rotina** que atua como um espaço reservado (*placeholder*), definindo o tipo e o nome do dado que a função espera receber.
  - *Analogia de Feynman:* A **abertura da caixa de correio** com o tamanho certo para receber cartas.
  - *Exemplo:* Em `void Depositar(double valor)`, `double valor` é o **parâmetro**.
* **Argumento Real (*Argument*):** É o **valor real e concreto fornecido à sub-rotina** no momento em que ela é invocada/chamada na execução.
  - *Analogia de Feynman:* A **carta física de 50 gramas** que você coloca dentro da caixa de correio.
  - *Exemplo:* Em `conta.Depositar(150.00)`, o número `150.00` é o **argumento**.

---

## 13. `GOTO` (Salto Incondicional)

A instrução **`GOTO`** é um comando primitivo de desvio incondicional no fluxo de execução que faz a CPU saltar diretamente para qualquer linha marcada por um rótulo no programa.

* **Problema histórico:** Seu uso desordenado originou o chamado *spaghetti code* ("código espaguete"), tornando imprevisível o rastreamento do estado das variáveis e a localização de bugs.
* **Substituição:** O Teorema de Böhm-Jacopini (1966) e o artigo de Dijkstra (1968) provaram que o `GOTO` é desnecessário e deve ser substituído por comandos estruturados (Sequência, Seleção e Repetição).

---

## 14. Robustez (*Robustness*)

A **Robustez** é o fator externo de qualidade de software que mede a capacidade de um sistema computacional **reagir de maneira segura e controlada diante de condições anormais, entradas inválidas ou falhas de ambiente**, sem travar inesperadamente (*crash*) e sem corromper seus dados.

* **Analogia de Feynman:** O **airbag e o cinto de segurança de um carro**. Em condições normais de trânsito, você não percebe sua presença. Porém, diante de um evento imprevisto ou batida (um erro), eles são acionados instantaneamente para proteger a vida dos passageiros e evitar uma tragédia.
* **Conexão direta com construtores e invariantes ([[08. Construtores (inicialização, sobrecarga e garantia de invariantes)|Artigo 08]]):**
  - O **construtor defensivo** é o primeiro escudo de robustez do software. Ao validar rigorosamente seus parâmetros de entrada (`if (valor <= 0) throw new ArgumentException(...)`), ele impede que o objeto nasça em estado corrompido, evitando que erros silenciosos se propaguem pela aplicação.
  - A robustez garante que uma conta bancária nunca seja instanciada com saldo negativo ou titular nulo, protegendo o sistema contra o colapso de regras de negócio.

---

## 15. Membro estático (*Static Member*)

Um **Membro Estático** é qualquer componente de uma classe (campo, método, propriedade, evento ou construtor) declarado com o modificador **`static`**, o que vincula sua existência, alocação de memória e execução diretamente ao **tipo/classe em si**, e **não a uma instância individual** criada no *Heap*.

* **Definição Técnica:** Ao contrário dos membros de instância (que são duplicados a cada chamada de `new`), existe **uma única cópia do membro estático para todo o ciclo de vida da aplicação**. Ele é alocado na área de metadados da classe quando o tipo é carregado pela primeira vez pelo *runtime* (.NET CLR ou JVM).
* **As 4 Formas de Membros Estáticos:**
  1. **Atributo Estático (*Static Field*):** Variável única compartilhada por todos os objetos (ex.: `private static int _contador;`).
  2. **Método Estático (*Static Method*):** Operação pura ou utilitária que não depende de estado de instância e não possui acesso ao ponteiro `this` (ex.: `Math.Sqrt(x)` ou `Conta.ObterTotalContas()`).
  3. **Propriedade Estática (*Static Property*):** Getter/setter de escopo de classe com proteção de regras globais (ex.: `Conta.TaxaGlobal`).
  4. **Construtor Estático (*Static Constructor*):** Bloco executado uma única vez automaticamente antes do primeiro acesso à classe para preparar dados globais.
* **Analogia de Feynman:** O **ar-condicionado ou a iluminação da sala de aula**. Cada aluno sentado na carteira possui seu próprio caderno individual (membro de instância). No entanto, o ar-condicionado é único para a sala inteira (membro estático). Se o professor alterar a temperatura para 19°C, **todos os alunos na sala sentem a mudança simultaneamente**, porque o recurso é compartilhado no nível da sala.
* **Conexão direta com compartilhamento de estado ([[09. Atributos estáticos e propriedades (compartilhamento de estado e encapsulamento)|Artigo 09]]):** Usados para geradores sequenciais de identificadores (IDs), contadores de objetos ativos, constantes matemáticas (`Math.PI`) e taxas de configuração global.

---

## 16. Propriedades (*Properties & Auto-Properties*)

Uma **Propriedade** é um membro de primeira classe em C# que fornece um mecanismo flexível para ler, gravar ou computar o valor de um campo privado, combinando a **sintaxe simples de um atributo público** com a **segurança e encapsulamento de métodos assessores (`get` e `set`)**.

* **Analogia de Feynman:** O **painel digital de um cofre inteligente**. Você não encosta diretamente nas engrenagens internas de aço (`_saldo` privado). Você interage com a tela externa (`Saldo` público). Quando você digita um novo valor, a tela executa um leitor biométrico e checa o limite permitido antes de acionar as engrenagens mecânicas.
* **Auto-Properties (`{ get; set; }`):** Quando nenhuma validação especial é necessária, o compilador cria o campo de apoio privado oculto automaticamente por debaixo dos panos, mantendo o código limpo e preparado para futuras regras de negócio.

---

## 17. Escopo (*Scope*)

O **Escopo** é a região do código-fonte onde um determinado identificador (variável, parâmetro, atributo ou método) é **visível, acessível e válido**. Ele determina a **fronteira de visibilidade** e o **tempo de vida** dos dados na memória.

* **Analogia de Feynman:** As **chaves de acesso de um prédio**:
  - **Escopo de bloco (`{ }`):** A **chave do banheiro individual**. Só funciona dentro daquela cabine específica; ao sair dela, ninguém mais tem acesso.
  - **Escopo de método (local / parâmetros):** O **cartão do crachá do seu departamento**. Permite transitar apenas dentro daquela sala durante o horário de trabalho (execução do método).
  - **Escopo de instância (atributos de objeto):** A **sua mesa de trabalho pessoal**. Seus objetos pessoais ficam nela enquanto você for funcionário da empresa (enquanto a instância existir no *Heap*).
  - **Escopo de classe (`static`):** O **hall de entrada principal e o relógio da recepção**. É único, compartilhado por todos os funcionários e visitantes do prédio, existindo enquanto o prédio estiver aberto (enquanto a aplicação estiver em execução).
* **Níveis Fundamentais de Escopo:**
  1. **Escopo de Bloco:** Variáveis declaradas dentro de `if`, `for` ou `while` que deixam de existir fora do par de chaves `{ }`.
  2. **Escopo de Sub-rotina (Local):** Parâmetros e variáveis criados na *Stack* durante a chamada de um método.
  3. **Escopo de Instância:** Atributos declarados no corpo da classe pertencentes a cada objeto individual no *Heap*.
  4. **Escopo de Classe (`static`):** Membros globais compartilhados por todas as instâncias da classe.
* **Conexão com Programação Modular ([[09. Atributos estáticos e propriedades (compartilhamento de estado e encapsulamento)|Artigo 09]]):** O correto isolamento de escopo previne efeitos colaterais indesejados (*Side Effects*) e é a base para o baixo acoplamento e alto encapsulamento.

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
