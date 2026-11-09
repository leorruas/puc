import json
import os

base_ref = '05. Desenvolvimento Web Back-End/'
puc_questions = []

def add_q(id_num, art, topico, dif, enunc, a_txt, b_txt, c_txt, d_txt, corr_idx, da, db, dc, dd, feynman, analise):
    letters = ['A', 'B', 'C', 'D']
    texts = [a_txt, b_txt, c_txt, d_txt]
    diags = [da, db, dc, dd]
    alts = []
    distrators = {}
    for i in range(4):
        is_corr = (i == corr_idx)
        alts.append({
            'letra': letters[i],
            'texto': texts[i],
            'correta': is_corr,
            'diagnostico': diags[i]
        })
        if not is_corr:
            distrators[letters[i]] = diags[i]
            
    puc_questions.append({
        'id': f'WEB-REV-{id_num:03d}',
        'disciplina_id': '05',
        'disciplina': 'Desenvolvimento Web Back-End',
        'topico': topico,
        'artigo_origem': art,
        'dificuldade': dif,
        'prioritaria': True,
        'origem': 'revisao_oficial_puc',
        'enunciado': enunc,
        'alternativas': alts,
        'explicacao': {
            'modelo_mental': feynman,
            'analise_correta': analise,
            'distratores': distrators,
            'referencia_vault': base_ref + art
        }
    })

raw = [
  # Questão 01
  (1, '01. Arquitetura de software e cliente-servidor.md',
   'Separação de responsabilidades e arquitetura em camadas', 'medio',
   'Uma equipe está modernizando um portal de consumo de veículos. Atualmente, a mesma classe recebe requisições HTTP, monta o HTML e executa consultas ao banco, dificultando os testes e a manutenção.\n\nQual decisão arquitetural enfrenta diretamente esse problema?',
   'Concentrar todas as funções em um controlador maior.',
   'Separar apresentação, processamento de requisições e responsabilidades de dados.',
   'Eliminar as classes de domínio para reduzir arquivos.',
   'Gerar todo o HTML diretamente em comandos SQL.',
   1,
   'Incorreto: aumentar a concentração criaria uma classe deus (God Class), piorando o acoplamento.',
   'Correto: separar a apresentação (View/UI), o controle de requisições (Controller) e o acesso aos dados (Model/Repository) aplica o princípio de responsabilidade única (SRP) e a arquitetura em camadas.',
   'Incorreto: eliminar classes de domínio destrói a representação do negócio.',
   'Incorreto: misturar SQL com HTML viola gravemente a separação de camadas e a segurança.',
   'Pense em um restaurante organizado: o garçom recebe os pedidos dos clientes (Controller), os cozinheiros preparam o prato seguindo receitas padronizadas (Model) e o prato é servido com uma apresentação bonita à mesa (View). Se o garçom tivesse que cozinhar, lavar e cobrar tudo ao mesmo tempo, a cozinha entraria em colapso.',
   'A separação de responsabilidades desacopla os componentes do sistema, facilitando testes unitários isolados, manutenção evolutiva e reuso de lógica de negócio.'),

  # Questão 02
  (2, '02. Estilos arquiteturais - camadas, monolítico e cliente-servidor.md',
   'Fluxo entre camadas no padrão MVC', 'medio',
   'Uma aplicação MVC registra o consumo de combustível de veículos. Um estudante desenhou o fluxo abaixo para explicar como uma solicitação de cadastro é processada.\n\nFluxo simplificado: Navegador -> Controller -> Model/dados -> View\n\nAo observar o fluxo, qual componente recebe a requisição e coordena a resposta no padrão MVC?',
   'Model, por ser responsável pelo HTML.',
   'View, por executar diretamente a persistência.',
   'Controller, por receber a solicitação e coordenar a interação com modelo e visualização.',
   'Banco SQL, por decidir a rota HTTP.',
   2,
   'Incorreto: o Model encapsula regras e dados de negócio, não o HTML.',
   'Incorreto: a View é puramente responsável pela apresentação visual, sem acesso direto a banco de dados.',
   'Correto: no padrão MVC, o Controller é o intermediário que intercepta a requisição HTTP enviada pelo navegador, aciona os Models para processar dados/regras e escolhe a View adequada para renderizar a resposta.',
   'Incorreto: o roteamento HTTP é responsabilidade do framework web e do servidor de aplicação, não do SGBD.',
   'O Controller é o maestro da orquestra: ele não toca todos os instrumentos sozinho nem senta na plateia; ele recebe a partitura (requisição HTTP), avisa aos músicos quando entrar (Model) e direciona o som harmonioso para o público (View).',
   'O ciclo de vida de uma requisição em ASP.NET Core MVC sempre atinge o Controller via middleware de roteamento antes de despachar dados para a View.'),

  # Questão 03
  (3, '03. Tipos de aplicações Web e estratégias de renderização.md',
   'Atualização de páginas em Multi-Page Applications (MPA)', 'facil',
   'A intranet de uma instituição usa uma aplicação tradicional: ao abrir um cadastro diferente, o navegador solicita outra página ao servidor e recebe um novo documento HTML.\n\nQual característica descreve a abordagem utilizada?',
   'MPA, com navegação baseada em solicitações e respostas de páginas.',
   'SPA, pois toda navegação sempre carrega novo HTML do servidor.',
   'Aplicação desktop sem comunicação HTTP.',
   'Serviço de banco de dados sem interface Web.',
   0,
   'Correto: em uma Multi-Page Application (MPA), cada transição de tela ou ação resulta em uma nova requisição HTTP ao servidor, que devolve um documento HTML completo renderizado no back-end (SSR).',
   'Incorreto: SPAs (Single-Page Applications) carregam uma única casca HTML inicial e atualizam o conteúdo dinamicamente via JavaScript e APIs JSON, sem recarregar a página inteira.',
   'Incorreto: a aplicação opera sobre o navegador e responde via requisições HTTP na intranet.',
   'Incorreto: trata-se de um sistema web com interface HTML para o usuário.',
   'Uma MPA é como virar as páginas de um livro físico impresso: para ler o próximo capítulo, você vira a página inteira. Já uma SPA é como uma lousa mágica digital onde você apaga e redesenha só um pedacinho sem trocar o quadro.',
   'Aplicações tradicionais em ASP.NET Core MVC operam tipicamente como MPAs com renderização no servidor (Server-Side Rendering), ideais para SEO e compatibilidade universal.'),

  # Questão 04
  (4, '04. Linguagens de programação back-end e PHP.md',
   'Geração de resposta HTTP e processamento no servidor', 'facil',
   'Um sistema de reservas precisa mostrar ao navegador o nome de um cliente que foi recuperado no servidor. O desenvolvedor está escolhendo onde executar a lógica de consulta e preparação dos dados.\n\nEm uma aplicação Web back-end, qual responsabilidade pertence ao processamento no servidor?',
   'Interpretar a requisição e produzir os dados ou conteúdo de resposta.',
   'Definir exclusivamente a resolução física da tela do usuário.',
   'Dispensar o protocolo HTTP na comunicação Web.',
   'Executar apenas arquivos de imagem sem lógica de aplicação.',
   0,
   'Correto: o servidor back-end processa a requisição do cliente, aplica regras de negócio, consulta bases de dados protegidas e constrói a resposta (em HTML, JSON, etc.) enviada de volta ao navegador.',
   'Incorreto: a resolução física da tela depende do hardware e do monitor do cliente.',
   'Incorreto: o protocolo HTTP é a espinha dorsal de toda a comunicação entre cliente e servidor web.',
   'Incorreto: o back-end executa lógica complexa de processamento, regras de negócio e persistência.',
   'O servidor é o cofre da agência bancária: quando você chega na boca do caixa (navegador) pedindo seu saldo, é lá dentro do cofre protegido que o bancário confere sua conta e entrega o extrato impresso.',
   'A arquitetura cliente-servidor distribui o trabalho: o cliente cuida da exibição e interação local; o back-end centraliza a lógica de negócios, a segurança e a integridade dos dados.'),

  # Questão 05
  (5, '05. Frameworks Web, MVC e mapeamento objeto-relacional.md',
   'Papel do ORM (Object-Relational Mapping)', 'medio',
   'Ao desenvolver a persistência de registros de abastecimento, uma equipe quer evitar escrever manualmente todo o mapeamento entre classes C# e tabelas relacionais.\n\nQue recurso de um framework atende a essa necessidade?',
   'Um editor de imagens.',
   'Um ORM, que faz o mapeamento objeto-relacional.',
   'Um gerenciador de estilos CSS.',
   'Um mecanismo que substitui completamente o banco de dados.',
   1,
   'Incorreto: editores de imagem tratam de assets visuais estáticos.',
   'Correto: um ORM (Object-Relational Mapper, como o Entity Framework Core) mapeia classes e propriedades orientadas a objetos diretamente para tabelas e colunas relacionais, gerando comandos SQL automaticamente.',
   'Incorreto: gerenciadores de CSS cuidam da apresentação e layout front-end.',
   'Incorreto: o ORM não substitui o banco de dados; ele atua como uma ponte de tradução entre o código da aplicação e o SGBD relacional (ex.: SQL Server).',
   'O ORM é um intérprete juramentado entre dois mundos: no C# você conversa com objetos e listas (`veiculo.Modelo`); no SQL Server o banco conversa com tabelas e colunas relacionais (`INSERT INTO Veiculos`). O ORM traduz um para o outro em tempo real sem você precisar escrever SQL na mão.',
   'O Entity Framework Core é o ORM oficial do ecossistema .NET, permitindo consultas fortemente tipadas via LINQ e controle de esquema por Migrations.'),

  # Questão 06
  (6, '05. Frameworks Web, MVC e mapeamento objeto-relacional.md',
   'Injeção de dependência por construtor em ASP.NET Core', 'dificil',
   'No sistema de consumo de veículos, um controlador precisa consultar serviços de negócio. A equipe quer diminuir o acoplamento e facilitar testes com implementações alternativas.\n\n```csharp\npublic class VeiculosController : Controller\n{\n    private readonly IVeiculoServico _servico;\n\n    public VeiculosController(IVeiculoServico servico)\n    {\n        _servico = servico;\n    }\n}\n```\n\nQual conceito é evidenciado pelo recebimento de `IVeiculoServico` no construtor?',
   'Herança múltipla entre controladores.',
   'Injeção de dependência por construtor.',
   'Renderização da View no servidor.',
   'Criação obrigatória do serviço com new dentro do Controller.',
   1,
   'Incorreto: C# não suporta herança múltipla de classes e a classe apenas herda de Controller.',
   'Correto: a dependência é declarada como uma interface no construtor e injetada pelo container de Inversão de Controle (IoC) do ASP.NET Core, promovendo baixo acoplamento e permitindo mocks em testes unitários.',
   'Incorreto: a injeção de dependência trata do ciclo de vida e instanciação de serviços, não da renderização visual.',
   'Incorreto: instanciar dependências diretamente com `new` gera acoplamento rígido, violando a inversão de dependência (DIP).',
   'Em vez de o controlador construir sua própria fábrica de peças dentro da sala (`new`), ele apenas estende a mão e recebe a ferramenta pronta que o container da empresa entrega no início do expediente.',
   'No ASP.NET Core, os serviços são registrados no `Program.cs` com tempos de vida `Transient`, `Scoped` ou `Singleton` e resolvidos automaticamente nos construtores dos controllers.'),

  # Questão 07
  (7, '07. Ambiente de desenvolvimento, Visual Studio e controle de versão no ASP.NET Core MVC.md',
   'Controle de versão com Git e GitHub', 'facil',
   'Três integrantes implementam partes do sistema no Visual Studio Community. Eles precisam registrar alterações e recuperar versões anteriores quando uma modificação provocar regressão.\n\nQual prática prevista no microfundamento atende diretamente a essa necessidade?',
   'Manter apenas uma cópia local do projeto.',
   'Usar Git e hospedar o repositório no GitHub.',
   'Salvar imagens das telas no banco SQL.',
   'Desativar o histórico de alterações para reduzir conflitos.',
   1,
   'Incorreto: cópias locais isoladas não oferecem histórico compartilhado nem rastreabilidade.',
   'Correto: o Git é o sistema de controle de versão distribuído que registra cada commit de alteração, e o GitHub centraliza o repositório em nuvem para colaboração em equipe.',
   'Incorreto: capturas de tela não gravam código-fonte nem permitem reversão funcional.',
   'Incorreto: o histórico é a ferramenta primordial para diagnosticar falhas e reverter regressões.',
   'O Git é uma máquina do tempo do seu código: a cada commit você salva um ponto de restauração confiável; se algo quebrar amanhã, você volta para a versão que funcionava com um simples comando.',
   'O uso de Git com branches e commits semânticos no GitHub é uma competência fundamental de engenharia exigida em todas as etapas práticas da PUC Minas.'),

  # Questão 08
  (8, '06. Model, validação e persistência no ASP.NET Core MVC.md',
   'Modelo de dados (Model) e propriedades em C#', 'medio',
   'Uma aplicação MVC precisa representar veículos cadastrados e guardar seus identificadores e modelos. O estudante deve escolher uma definição adequada para a classe de domínio.\n\n```csharp\npublic class Veiculo\n{\n    public int Id { get; set; }\n    public string Modelo { get; set; } = "";\n}\n```\n\nConsiderando o trecho, qual interpretação é correta?',
   'Id e Modelo são propriedades do modelo Veiculo.',
   'O código define diretamente uma tabela SQL por meio de CREATE TABLE.',
   'O código cria uma View Razor para listar veículos.',
   'A classe contém uma action de Controller que recebe HTTP.',
   0,
   'Correto: Id e Modelo são propriedades automáticas públicas da classe C# `Veiculo`, que atua como modelo de dados (Model) da aplicação.',
   'Incorreto: o código é C# puro; a tabela SQL é gerada posteriormente pelo ORM por meio de Migrations.',
   'Incorreto: Views Razor possuem extensão `.cshtml` e combinam HTML com sintaxe Razor.',
   'Incorreto: actions de controller são métodos públicos que retornam `IActionResult` dentro de classes derivadas de `Controller`.',
   'Uma classe Model é como a ficha cadastral em papel da concessionária: ela lista quais campos existem (número de série e modelo do carro) para que o sistema saiba como organizar essas informações.',
   'No Entity Framework Core, uma propriedade chamada `Id` ou `<NomeClasse>Id` é reconhecida automaticamente por convenção como chave primária da entidade.'),

  # Questão 09
  (9, '08. Implementação prática do CRUD de veículos no ASP.NET Core MVC.md',
   'Retorno de View com passagem de Model na action', 'medio',
   'Uma equipe precisa exibir a página de listagem de veículos. O controller recupera os registros do contexto e deve passá-los à View correspondente.\n\n```csharp\npublic IActionResult Index()\n{\n    var lista = _context.Veiculos.ToList();\n    return ______;\n}\n```\n\nQual expressão completa corretamente a action para renderizar a View com a lista?',
   'RedirectToAction("Index");',
   'View(lista);',
   'NotFound();',
   'Content("Lista não disponível");',
   1,
   'Incorreto: RedirectToAction causaria um redirecionamento HTTP que chamaria a action novamente, gerando loop infinito.',
   'Correto: `return View(lista);` renderiza a View associada à action (Views/Veiculos/Index.cshtml) passando a coleção de veículos como modelo tipado (`@model IEnumerable<Veiculo>`).',
   'Incorreto: NotFound retorna o status HTTP 404 de recurso não encontrado.',
   'Incorreto: Content retorna texto simples puro sem renderizar o template HTML da View.',
   'Executar `return View(lista);` é como o garçom pegar a bandeja montada na cozinha com todos os pratos (`lista`) e levar até a mesa decorada (`View`) para o cliente saborear.',
   'O método auxiliar `View(model)` do Controller empacota os dados no `ViewData.Model`, permitindo que a View Razor itere sobre os dados via `@foreach`.'),

  # Questão 10
  (10, '08. Implementação prática do CRUD de veículos no ASP.NET Core MVC.md',
   'Consulta de registros com LINQ (FirstOrDefault)', 'medio',
   'Na tela de detalhes de um veículo, o usuário informa um identificador. A action precisa recuperar o registro correspondente, ou obter null quando ele não existir.\n\n```csharp\npublic IActionResult Detalhes(int id)\n{\n    var veiculo = _context.Veiculos\n        .________(v => v.Id == id);\n    if (veiculo == null) return NotFound();\n    return View(veiculo);\n}\n```\n\nQual método completa a consulta conforme o comportamento desejado?',
   'Add',
   'FirstOrDefault',
   'SaveChanges',
   'Remove',
   1,
   'Incorreto: Add adiciona uma nova entidade ao contexto para inserção.',
   'Correto: `FirstOrDefault(v => v.Id == id)` executa a consulta LINQ retornando o primeiro elemento que satisfaz a condição lambda ou `null` caso nenhum registro seja encontrado.',
   'Incorreto: SaveChanges grava alterações pendentes no banco de dados.',
   'Incorreto: Remove marca a entidade para exclusão no banco.',
   'FirstOrDefault é como pedir para a recepcionista procurar no fichário o primeiro prontuário com aquele número: se encontrar, ela entrega a pasta; se não existir nenhum, ela volta de mãos vazias (`null`).',
   'No Entity Framework Core, métodos LINQ como `FirstOrDefault()` ou `FirstOrDefaultAsync()` traduzem a expressão lambda para uma cláusula SQL com `TOP(1)` e `WHERE`.'),

  # Questão 11
  (11, '06. Model, validação e persistência no ASP.NET Core MVC.md',
   'Persistência transacional com DbContext.SaveChanges()', 'medio',
   'Na funcionalidade de cadastro, o programador adiciona um objeto Veiculo ao contexto do banco, mas percebe que a informação ainda não foi efetivamente gravada.\n\n```csharp\nvar veiculo = new Veiculo { Modelo = "Sedan" };\n_context.Veiculos.Add(veiculo);\n// Falta persistir a alteração\n```\n\nQual chamada deve ser executada para gravar a inclusão no banco usando o contexto?',
   '_context.SaveChanges();',
   '_context.Veiculos.ToList();',
   'return View();',
   '_context.Veiculos.Find(veiculo.Id);',
   0,
   'Correto: o método `_context.SaveChanges()` aplica o padrão Unit of Work, abrindo a transação no banco, executando os comandos SQL gerados (`INSERT`) e persistindo as alterações no banco de dados.',
   'Incorreto: ToList() apenas executa uma consulta de leitura SELECT no banco.',
   'Incorreto: return View() renderiza uma tela no navegador sem interagir com a persistência do banco.',
   'Incorreto: Find() realiza uma busca por chave primária.',
   'Chamar `Add(veiculo)` é como colocar uma carta dentro do envelope e fechar; chamar `SaveChanges()` é como jogar a carta na caixa dos correios para ser enviada de verdade.',
   'O Entity Framework rastreia os estados das entidades (Added, Modified, Deleted) e só efetiva as alterações no banco ao chamar `SaveChanges()` ou `SaveChangesAsync()`.'),

  # Questão 12
  (12, '08. Implementação prática do CRUD de veículos no ASP.NET Core MVC.md',
   'Exclusão de registros com DbContext.Remove() e SaveChanges()', 'dificil',
   'Um desenvolvedor implementa a exclusão de veículos, mas, após localizar o registro, só chama SaveChanges. O item continua na tabela porque não foi marcado para remoção.\n\n```csharp\nvar veiculo = _context.Veiculos.Find(id);\nif (veiculo == null) return NotFound();\n\n// Uma instrução é necessária aqui\n_context.SaveChanges();\n```\n\nQual instrução deve ser inserida antes de SaveChanges para efetivar a exclusão?',
   '_context.Veiculos.Add(veiculo);',
   '_context.Veiculos.Remove(veiculo);',
   '_context.Veiculos.ToList();',
   'return View(veiculo);',
   1,
   'Incorreto: Add tentaria reinserir a entidade já existente.',
   'Correto: `_context.Veiculos.Remove(veiculo);` altera o estado da entidade no Change Tracker para `EntityState.Deleted`, permitindo que o `SaveChanges()` gere e execute o comando `DELETE FROM Veiculos WHERE Id = @id`.',
   'Incorreto: ToList() apenas lê dados sem alterar o estado da entidade rastreada.',
   'Incorreto: return View(veiculo) cancelaria a exclusão e apenas renderizaria a página.',
   'Se você quer jogar um arquivo fora, primeiro precisa arrastar o arquivo para a lixeira (`Remove`) e depois esvaziar a lixeira (`SaveChanges`). Se você só esvaziar a lixeira sem colocar o arquivo lá dentro, nada é apagado.',
   'O Entity Framework exige explicitamente a transição de estado da entidade antes de persistir a remoção no banco relacional.'),

  # Questão 13
  (13, '09. Relacionamentos entre modelos e novas funcionalidades no ASP.NET Core MVC.md',
   'Relacionamentos entre modelos: chave estrangeira e propriedade de navegação', 'dificil',
   'A aplicação, inicialmente limitada ao cadastro de veículos, passou a registrar vários abastecimentos para cada veículo. O programador precisa representar o vínculo entre Abastecimento e Veiculo.\n\n```csharp\npublic class Abastecimento\n{\n    public int Id { get; set; }\n    public int VeiculoId { get; set; }\n    public Veiculo Veiculo { get; set; }\n}\n```\n\nQual interpretação melhor descreve os dois últimos membros da classe?',
   'Ambos são controladores para o mesmo endpoint.',
   'VeiculoId pode representar a chave estrangeira e Veiculo a propriedade de navegação.',
   'VeiculoId necessariamente guarda o nome textual do veículo.',
   'Veiculo representa uma View Razor, não um objeto relacionado.',
   1,
   'Incorreto: propriedades de modelos não são controladores web.',
   'Correto: em modelos do Entity Framework Core, `VeiculoId` é a propriedade escalar de chave estrangeira (FK) que se conecta à tabela referenciada, enquanto `Veiculo` é a propriedade de navegação orientada a objetos que permite carregar os dados do veículo associado.',
   'Incorreto: VeiculoId é um inteiro (`int`) que armazena a chave primária numérica do veículo.',
   'Incorreto: Veiculo é uma referência de classe de domínio C#, não um arquivo de visualização.',
   'Em uma certidão de casamento: o número do documento da pessoa é a chave estrangeira (`VeiculoId`), enquanto a própria pessoa ao seu lado de carne e osso é a propriedade de navegação (`Veiculo`). Com o número você acha no arquivo; com a pessoa você conversa diretamente.',
   'As propriedades de navegação viabilizam o carregamento adiantado (Eager Loading) de dados relacionados utilizando o método `.Include(a => a.Veiculo)`.'),

  # Questão 14
  (14, '08. Implementação prática do CRUD de veículos no ASP.NET Core MVC.md',
   'Mapeamento de rotas convencionais no ASP.NET Core MVC', 'medio',
   'Um usuário acessa a URL `/Veiculos/Detalhes/8` em uma aplicação ASP.NET Core MVC com roteamento convencional por controller, action e id.\n\n```csharp\npublic IActionResult Detalhes(int id)\n{\n    return View();\n}\n```\n\nConsiderando a rota indicada, que valor deve ser associado ao parâmetro id da action?',
   '0',
   '8',
   '"Detalhes"',
   '"Veiculos"',
   1,
   'Incorreto: 0 seria o valor padrão caso o parâmetro não fosse localizado.',
   'Correto: no padrão de rota convencional `{controller=Home}/{action=Index}/{id?}`, o primeiro segmento (`Veiculos`) mapeia o `VeiculosController`, o segundo (`Detalhes`) a action `Detalhes()`, e o terceiro (`8`) é automaticamente convertido para o parâmetro inteiro `id = 8`.',
   'Incorreto: "Detalhes" é o nome da action no segundo segmento.',
   'Incorreto: "Veiculos" é o nome do controller no primeiro segmento.',
   'A rota convencional é como o endereço de uma carta: "Rua Veículos (Controller), Casa Detalhes (Action), Número 8 (id)". O carteiro entrega a correspondência diretamente na porta do morador número 8.',
   'O mecanismo de Model Binding do ASP.NET Core extrai automaticamente valores da rota, query string e corpo da requisição para injetar nos parâmetros das actions.'),

  # Questão 15
  (15, '05. Frameworks Web, MVC e mapeamento objeto-relacional.md',
   'Separação entre View e Controller (refatoração arquitetural)', 'medio',
   'Em uma revisão de código, a equipe encontra a lógica de persistência SQL diretamente na marcação HTML de uma View. O projeto se tornou difícil de testar e alterar.\n\nQual refatoração está mais alinhada à organização MVC estudada?',
   'Manter toda a persistência na View para reduzir arquivos.',
   'Transferir a lógica de processamento para componentes apropriados, preservando a View para apresentação.',
   'Mover a marcação visual para as tabelas do banco.',
   'Substituir o Controller por um arquivo CSS.',
   1,
   'Incorreto: misturar SQL com visualização viola o padrão MVC e compromete segurança e manutenção.',
   'Correto: o padrão MVC exige que a View limite-se à exibição e formatação dos dados recebidos, transferindo o processamento, persistência e regras para Controllers, Services e Repositórios.',
   'Incorreto: bancos relacionais armazenam dados, não templates de renderização visual.',
   'Incorreto: CSS é folha de estilos de apresentação, incapaz de controlar requisições de aplicação.',
   'Colocar consultas SQL dentro do HTML é como guardar a caixa de ferramentas pesada e graxa de motor dentro da vitrine de doces da confeitaria: a vitrine (View) deve exibir apenas os doces prontos; a graxa e as máquinas ficam isoladas na oficina (Back-End).',
   'Uma View desprovida de lógica de acesso a dados torna-se leve, segura contra injeções SQL acidentais e passível de redesign sem afetar as regras de negócio.'),

  # Questão 16
  (16, '10. Controle de usuários e criptografia de senhas no ASP.NET Core MVC.md',
   'Armazenamento seguro de senhas e funções de hash criptográfico', 'medio',
   'Ao construir o módulo de contas, um estudante propõe gravar as senhas digitadas exatamente como foram recebidas. Outro integrante alerta para os riscos caso o banco seja exposto.\n\nQual alteração melhora a proteção das credenciais armazenadas?',
   'Salvar senha em texto puro para facilitar recuperação.',
   'Aplicar mecanismo apropriado de hash de senhas no gerenciamento de usuários.',
   'Mostrar a senha no HTML para permitir conferência.',
   'Enviar a senha pela URL em toda requisição.',
   1,
   'Incorreto: texto puro expõe imediatamente todas as senhas dos usuários caso haja vazamento do banco.',
   'Correto: senhas nunca devem ser salvas em texto puro; deve-se aplicar uma função de hash criptográfico irreversível e lenta (como PBKDF2 ou BCrypt) com salt aleatório, garantindo que mesmo com o banco exposto a senha original não seja revelada.',
   'Incorreto: exibir senhas na interface visual expõe as credenciais a terceiros.',
   'Incorreto: enviar senhas por query string na URL grava as credenciais em logs de servidores e histórico do navegador.',
   'O hash de senha é como um triturador de carne de via única: você coloca um bife (senha) e sai carne moída (hash). Quando a pessoa digita a senha no login, você mói de novo e confere se a carne moída é idêntica; mas se um ladrão roubar o banco, ele só encontra carne moída e não consegue reconstruir o bife original.',
   'O ASP.NET Core Identity implementa por padrão o `PasswordHasher<TUser>` com PBKDF2 e derivação HMAC-SHA256 com salt individual de 128 bits.'),

  # Questão 17
  (17, '11. Autenticação baseada em cookies, claims e login no ASP.NET Core MVC.md',
   'Segurança e gerenciamento de usuários com ASP.NET Core Identity', 'medio',
   'Uma aplicação de gestão de consumo precisa registrar usuários, permitir login e manter informações de autenticação durante a navegação. A equipe considera o uso de recursos integrados do ASP.NET Core.\n\nQual componente atende diretamente a essas necessidades?',
   'ASP.NET Core Identity.',
   'Uma View apenas com CSS.',
   'A classe StringBuilder.',
   'A instrução SQL ORDER BY.',
   0,
   'Correto: o ASP.NET Core Identity é a biblioteca oficial e integrada de segurança que fornece gerenciamento completo de usuários, senhas com hash, autenticação baseada em cookies, claims, recuperação de conta e controle de perfis.',
   'Incorreto: arquivos CSS cuidam exclusivamente de estilo e layout visual.',
   'Incorreto: StringBuilder é um utilitário de manipulação de cadeias de caracteres em memória.',
   'Incorreto: ORDER BY é uma cláusula SQL de ordenação de consultas em tabelas.',
   'O ASP.NET Core Identity é a portaria eletrônica completa de um condomínio fechado: ele cadastra moradores, emite crachás codificados (cookies), confere a impressão digital no portão e sabe exatamente quem pode entrar em qual bloco.',
   'O Identity integra-se nativamente com o Entity Framework Core via `IdentityDbContext`, gerando automaticamente as tabelas `AspNetUsers`, `AspNetRoles` e afins.'),

  # Questão 18
  (18, '12. Autorização de acesso baseada em perfis no ASP.NET Core MVC.md',
   'Distinção fundamental entre Autenticação e Autorização', 'facil',
   'No portal de veículos, Carla entra com credenciais válidas. Ao tentar acessar um relatório restrito a administradores, recebe uma resposta de acesso negado.\n\nQual explicação diferencia corretamente as duas verificações?',
   'Carla não foi autenticada, mas foi autorizada para o relatório.',
   'Autenticação verificou sua identidade; autorização negou uma operação sem permissão.',
   'Autorização valida somente o formato da senha, não permissões.',
   'Autenticação e autorização são necessariamente o mesmo procedimento.',
   1,
   'Incorreto: Carla foi autenticada com sucesso (suas credenciais eram válidas), mas sua conta não possuía a autorização exigida.',
   'Correto: **Autenticação** responde *"Quem é você?"* (verificação de identidade via login e senha); **Autorização** responde *"O que você tem permissão para fazer?"* (verificação de papéis, perfis ou direitos sobre um recurso específico).',
   'Incorreto: formato de senha é validação cadastral, não autorização de acesso a recursos.',
   'Incorreto: são etapas de segurança distintas e consecutivas (primeiro autentica-se, depois autoriza-se).',
   'Pense em um aeroporto: conferir seu passaporte no guichê de entrada para provar quem você é é **Autenticação**; conferir se sua passagem permite entrar na cabine do piloto ou na sala VIP é **Autorização**. Ter o passaporte válido não dá permissão para pilotar o avião!',
   'No ASP.NET Core, a autenticação produz uma `ClaimsPrincipal` (`User`), enquanto a autorização inspeciona os atributos `[Authorize]` e as regras de roles e policies.'),

  # Questão 19
  (19, '12. Autorização de acesso baseada em perfis no ASP.NET Core MVC.md',
   'Proteção de actions e controladores com o atributo [Authorize]', 'dificil',
   'A equipe deseja impedir que pessoas não autenticadas acessem a lista de veículos. O projeto usa autenticação configurada com ASP.NET Core Identity.\n\n```csharp\npublic class VeiculosController : Controller\n{\n    [________]\n    public IActionResult Index()\n    {\n        return View();\n    }\n}\n```\n\nQual atributo deve substituir a lacuna para exigir autenticação na action?',
   'AllowAnonymous',
   'Authorize',
   'HttpGet("publico")',
   'ValidateAntiForgeryToken',
   1,
   'Incorreto: `[AllowAnonymous]` libera o acesso público anônimo, desativando restrições de autorização.',
   'Correto: o atributo `[Authorize]` exige que a requisição seja realizada por um usuário autenticado; caso contrário, o middleware redireciona automaticamente o visitante para a tela de login.',
   'Incorreto: HttpGet apenas restringe o método HTTP da rota.',
   'Incorreto: ValidateAntiForgeryToken protege contra ataques de falsificação de requisição entre sites (CSRF), mas não exige autenticação de usuário por si só.',
   'O atributo `[Authorize]` é a fechadura eletrônica da porta da sala: sem o crachá de login autenticado, a porta não abre e o sistema te manda direto para a recepção (tela de login) para se identificar.',
   'O atributo `[Authorize]` pode ser aplicado em nível de action individual ou em nível de classe controladora inteira, e suporta restrição por papéis como `[Authorize(Roles = "Admin")]`.'),

  # Questão 20
  (20, '11. Autenticação baseada em cookies, claims e login no ASP.NET Core MVC.md',
   'Acesso aos dados do usuário autenticado via HttpContext.User.Identity', 'medio',
   'Uma funcionalidade precisa exibir uma mensagem de boas-vindas ao usuário que já realizou login na aplicação MVC. O controller deve consultar informações da identidade atual.\n\n```csharp\npublic IActionResult Inicio()\n{\n    var nome = User.Identity?.Name;\n    return View(model: nome);\n}\n```\n\nQual interpretação é compatível com esse trecho?',
   'A propriedade consulta o usuário associado à requisição atual.',
   'A propriedade cria automaticamente um novo usuário no banco.',
   'A propriedade exclui todas as sessões da aplicação.',
   'O código determina o identificador de cada veículo cadastrado.',
   0,
   'Correto: a propriedade `User` (do tipo ClaimsPrincipal herdada da classe Controller) representa a identidade criptograficamente verificada vinculada à requisição HTTP atual, permitindo ler o nome do usuário logado via `User.Identity?.Name`.',
   'Incorreto: ler a propriedade de identidade é uma operação de consulta em memória, sem criação de registros no banco de dados.',
   'Incorreto: não encerra sessões nem afeta outros usuários.',
   'Incorreto: a propriedade trata da identidade do usuário logado, não dos veículos.',
   '`User.Identity.Name` é como o crachá pendurado no peito do visitante que acabou de passar pela catraca: o recepcionista só bate o olho no crachá e diz *"Bom dia, Leonardo!"*, sem precisar fazer uma nova entrevista cadastral do zero.',
   'Os dados de `User.Identity` são preenchidos pelo middleware de autenticação a partir do ticket descriptografado do cookie de autenticação enviado no cabeçalho HTTP.')
]

for item in raw:
    add_q(*item)

print(f"Generated {len(puc_questions)} official PUC revision questions for Web Back-End.")

# Load existing Web Back-End file
web_path = os.path.join('/home/antigravity/leorruas/puc/banco-de-questoes', '05.desenvolvimento-web-back-end.json')
with open(web_path, 'r', encoding='utf-8') as f:
    existing_web = json.load(f)

print(f"Existing Web Back-End questions: {len(existing_web)}")

for eq in existing_web:
    if 'prioritaria' not in eq:
        eq['prioritaria'] = False
    if 'origem' not in eq:
        eq['origem'] = 'banco_sintetico_vault'

existing_ids = {q['id'] for q in existing_web}
new_to_add = [q for q in puc_questions if q['id'] not in existing_ids]

merged_web = puc_questions + [q for q in existing_web if not q['id'].startswith('WEB-REV-')]

with open(web_path, 'w', encoding='utf-8') as f:
    json.dump(merged_web, f, ensure_ascii=False, indent=2)

print(f"Total questions in {web_path} after prepend: {len(merged_web)}")
