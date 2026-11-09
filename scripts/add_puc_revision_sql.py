import json
import os

base_ref = '03. Manipulação de Dados SQL/'
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
        'id': f'SQL-REV-{id_num:03d}',
        'disciplina_id': '03',
        'disciplina': 'Manipulação de Dados SQL',
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
  # Questao 01
  (1, '04. Alteração e remoção de tabelas.md',
   'DDL: comando ALTER TABLE e adição de colunas', 'facil',
   'Uma empresa mantém a tabela Cliente em um banco de dados relacional. A equipe precisa acrescentar uma coluna telefone, do tipo VARCHAR(20), sem excluir registros nem modificar as demais colunas. Qual comando realiza a alteração?',
   'ALTER TABLE Cliente ADD telefone VARCHAR(20);',
   'TRUNCATE TABLE Cliente;',
   'CREATE TABLE Cliente (telefone VARCHAR(20));',
   'UPDATE Cliente SET telefone = NULL;',
   0,
   'Correto: o comando DDL ALTER TABLE ... ADD ... adiciona novas colunas a estrutura de uma tabela existente sem afetar os dados preexistentes nas demais colunas.',
   'Incorreto: TRUNCATE TABLE apaga todos os registros da tabela em disco.',
   'Incorreto: CREATE TABLE falhara se a tabela Cliente ja existir no catalogo do banco.',
   'Incorreto: UPDATE e comando DML que manipula valores de linhas existentes, nao modificando o esquema DDL.',
   'Pense em uma planilha com varias linhas preenchidas: em vez de apagar a folha ou criar outra do zero, voce apenas clica com o botao direito e adiciona uma nova coluna a direita de todas as linhas ja cadastradas.',
   'O comando ALTER TABLE table ADD coluna tipo altera os metadados do esquema relacional no catalogo do SGBD, preenchendo a nova coluna com NULL (ou valor padrao DEFAULT) para as tuplas preexistentes.'),

  # Questao 02
  (2, '05. Comandos INSERT, UPDATE e DELETE.md',
   'DML: comando UPDATE com condições compostas (AND) e reajuste percentual', 'medio',
   'A tabela Produto contém id, nome, categoria e preco. Uma loja precisa aumentar em 10% apenas o preço dos produtos da categoria Informatica cujo preço atual é inferior a R$ 200,00. Qual comando atende à solicitação?',
   "UPDATE Produto SET preco = preco * 1.10 WHERE categoria = 'Informatica' OR preco < 200;",
   "UPDATE Produto SET preco = preco * 1.10 WHERE categoria = 'Informatica';",
   "UPDATE Produto SET preco = preco * 1.10 WHERE categoria = 'Informatica' AND preco < 200;",
   "UPDATE Produto SET preco = preco + 10 WHERE categoria = 'Informatica' AND preco < 200;",
   2,
   'Incorreto: o operador OR reajustaria produtos de outras categorias que custam menos de 200 e itens caros de informatica.',
   'Incorreto: ignora a restricao de valor maximo de 200 reais.',
   'Correto: multiplica o preco atual por 1,10 (aumento de 10%) aplicando conjuncao logica AND para filtrar apenas itens simultaneamente da categoria "Informatica" e com preco estritamente menor que 200.',
   'Incorreto: somar 10 adiciona um valor absoluto fixo de R$ 10,00, nao um percentual de 10%.',
   'Se voce der um aumento percentual para um produto de R$ 100,00, ele passa a custar R$ 110,00 (100 * 1,10). Se voce fizesse + 10 para alguem que ganha R$ 1.000,00, seria irrelevante; o percentual exige multiplicacao pelo fator 1,10.',
   'O comando UPDATE atua sobre as tuplas que satisfazem a expressao booleana da clausula WHERE. A conjuncao AND exige verdade simultanea em ambos os predicados.'),

  # Questao 03
  (3, '08. Funções agregadas e cálculos em SQL.md',
   'Funções agregadas: COUNT(*), COUNT(coluna), AVG e tratamento de valores NULL', 'medio',
   'A tabela Funcionario contém cinco linhas, com estes valores da coluna bonus: 500, NULL, 300, 0 e NULL. Qual resultado, na ordem das colunas, será produzido por SELECT COUNT(*), COUNT(bonus), AVG(bonus) FROM Funcionario? Considere a média arredondada para duas casas decimais.',
   '5, 5, 160.00',
   '5, 3, 400.00',
   '3, 3, 400.00',
   '5, 3, 266.67',
   3,
   'Incorreto: trata NULLs como valores validos em COUNT(coluna) e na divisao da media por 5.',
   'Incorreto: ignora o zero no denominador da media, calculando 800 / 2 em vez de 800 / 3.',
   'Incorreto: COUNT(*) conta todas as linhas da tabela, totalizando 5 e nao 3.',
   'Correto: COUNT(*) conta todas as 5 tuplas da tabela; COUNT(bonus) ignora os dois valores NULL, contabilizando 3 tuplas (500, 300, 0); AVG(bonus) soma os nao-nulos (500 + 300 + 0 = 800) e divide pelo numero de nao-nulos (800 / 3 = 266,67).',
   'Imagine 5 fichas de funcionarios na mesa: 2 pessoas nao tem bonus cadastrado (esta em branco/NULL), 1 pessoa tem bonus R$ 0,00 e 2 tem bonus positivo. No censo total sao 5 pessoas; quem tem ficha preenchida sao 3; e a media de quem tem valor e (500 + 300 + 0) / 3 = 266,67.',
   'Segundo o padrao SQL ANSI, funcoes de agregacao que recebem expressoes de coluna (COUNT(col), AVG(col), SUM(col)) descartam automaticamente valores NULL antes de computar o calculo. O valor numerico zero (0) e um valor conhecido e participa da media.'),

  # Questao 04
  (4, '09. Cláusulas GROUP BY e HAVING.md',
   'Agrupamento e filtragem com WHERE, GROUP BY e HAVING', 'dificil',
   'A tabela Matricula contém id, aluno_id, curso_id e status. A coordenação quer os identificadores dos cursos com MAIS de cinco matrículas cujo status é Ativa, acompanhados da quantidade de matrículas ativas. Qual consulta atende ao pedido?',
   "SELECT curso_id, COUNT(*) FROM Matricula WHERE status = 'Ativa' GROUP BY curso_id HAVING COUNT(*) > 5;",
   "SELECT curso_id, COUNT(*) FROM Matricula WHERE status = 'Ativa' GROUP BY curso_id HAVING COUNT(*) >= 5;",
   "SELECT curso_id, COUNT(*) FROM Matricula WHERE status = 'Ativa' AND COUNT(*) > 5 GROUP BY curso_id;",
   "SELECT curso_id, COUNT(*) FROM Matricula GROUP BY curso_id HAVING COUNT(*) > 5;",
   0,
   'Correto: o WHERE filtra as linhas antes do agrupamento mantendo apenas as ativas; o GROUP BY curso_id agrupa por curso; e o HAVING COUNT(*) > 5 filtra os grupos pos-agregacao com mais de 5 matriculas ativas.',
   'Incorreto: o operador >= 5 incluiria cursos com exatamente 5 matriculas, violando o criterio "MAIS de cinco" (> 5).',
   'Incorreto: funcoes de agregacao como COUNT(*) nao podem ser usadas na clausula WHERE.',
   'Incorreto: agrupa todas as matriculas sem filtrar o status "Ativa" no WHERE, contando matriculas canceladas ou trancadas.',
   'Pense em um filtro de duas etapas: primeiro voce descarta todas as fichas de alunos que nao estao ativos (WHERE individual); depois empilha as fichas por turma (GROUP BY) e so entrega para a coordenacao as pilhas que tiverem mais de 5 fichas (HAVING do grupo).',
   'A ordem de processamento logico do SQL executa: FROM -> WHERE (filtra linhas individuais) -> GROUP BY (forma os grupos) -> HAVING (filtra os grupos formados) -> SELECT -> ORDER BY.'),

  # Questao 05
  (5, '12. Transações em banco de dados, COMMIT e ROLLBACK.md',
   'Controle de transações, atomicidade e ROLLBACK', 'medio',
   'Uma transferência bancária debita uma conta e credita outra na mesma transação ainda não confirmada. Uma falha ocorre após o débito, antes do crédito. Qual procedimento evita efetivar somente uma parte da transferência?',
   'Executar ROLLBACK apenas para a operação de crédito, mantendo o débito.',
   'Executar ROLLBACK para desfazer as alterações da transação incompleta.',
   'Executar COMMIT imediatamente após o débito.',
   'Executar COMMIT e deixar o crédito para outra transação eventual.',
   1,
   'Incorreto: o ROLLBACK atua sobre toda a transacao atomica, nao sendo possivel desfazer apenas o que nao ocorreu e manter o debito injusto.',
   'Correto: o comando ROLLBACK desfaz todas as alteracoes efetuadas desde o inicio da transacao nao confirmada, restaurando o estado anterior consistente do banco de dados (propriedade de atomicidade).',
   'Incorreto: executar COMMIT apos o debito tornaria permanente o desconto do saldo sem creditar a conta recebedora.',
   'Incorreto: fragmentar em outra transacao eventual viola a garantia ACID e a consistencia contabil.',
   'Atomicidade e a regra do "tudo ou nada": se voce foi pagar uma conta e o dinheiro saiu da sua carteira mas o caixa travou antes de emitir o comprovante, a transacao deve ser desfeita por completo e o dinheiro devolvido a sua mao.',
   'A atomicidade (o "A" do acronimo ACID) garante que a transacao e tratada como uma unidade indivisivel de trabalho: caso ocorra qualquer excecao ou falha antes do COMMIT, o SGBD realiza o ROLLBACK automatico ou explicito via log de transacoes (undo log).'),

  # Questao 06
  (6, '02. Bancos de dados relacionais e SGBDs.md',
   'Chaves primárias, chaves estrangeiras e integridade referencial 1:N', 'medio',
   'Uma instituição mantém Curso(id_curso, nome_curso) e Aluno(id_aluno, nome_aluno, id_curso). Cada aluno pertence a um curso, e cada curso pode ter vários alunos. Em Curso, id_curso identifica cada linha. Qual definição representa corretamente esse relacionamento?',
   'Manter apenas chaves primárias, pois nomes iguais de campos estabelecem integridade referencial.',
   'Definir Aluno.id_curso como chave estrangeira referenciando Curso.id_curso.',
   'Definir Aluno.id_curso como chave primária, impedindo repetição de curso.',
   'Usar Aluno.id_aluno como chave estrangeira na tabela Curso.',
   1,
   'Incorreto: o modelo relacional nao infere integridade referencial meramente por coincidencia de nomes de colunas sem a restricao FOREIGN KEY declarada.',
   'Correto: no relacionamento 1:N (um curso para muitos alunos), a chave primaria da tabela do lado 1 (Curso.id_curso) migra para a tabela do lado N (Aluno) como chave estrangeira (foreign key).',
   'Incorreto: se Aluno.id_curso fosse chave primaria, a tabela Aluno so permitiria um unico aluno cadastrado por curso.',
   'Incorreto: colocar Aluno.id_aluno em Curso inverteria a dependencia e impediria que um curso tivesse multiplos alunos.',
   'Pense no cracha do aluno: a faculdade e uma so, mas cada aluno carrega em seu cracha o codigo do curso em que estuda (chave estrangeira). A faculdade nao tem como colar no teto da sala o nome de cada aluno em uma unica placa.',
   'A restricao FOREIGN KEY (id_curso) REFERENCES Curso(id_curso) estabelece a integridade referencial, impedindo a insercao de alunos vinculados a cursos inexistentes e bloqueando a exclusao de cursos com alunos ativos sem regra de cascata.'),

  # Questao 07
  (7, '03. Comando CREATE TABLE.md',
   'DDL: CREATE TABLE, tipos INTEGER e VARCHAR e PRIMARY KEY', 'facil',
   'Uma loja precisa criar Categoria com id numérico único e nome com até 80 caracteres. Qual definição SQL atende a esses requisitos?',
   'CREATE TABLE Categoria (id INTEGER PRIMARY KEY, nome VARCHAR(80));',
   'CREATE TABLE Categoria (id INTEGER PRIMARY KEY, nome INTEGER);',
   'CREATE TABLE Categoria (id VARCHAR(80) PRIMARY KEY, nome VARCHAR(80));',
   'CREATE TABLE Categoria (id INTEGER, nome VARCHAR(80) PRIMARY KEY);',
   0,
   'Correto: define id com tipo numerico inteiro INTEGER e restricao de unicidade/obrigatoriedade PRIMARY KEY, e nome com tipo alfanumerico variavel VARCHAR(80).',
   'Incorreto: definiu a coluna nome como tipo numerico INTEGER.',
   'Incorreto: definiu id como texto VARCHAR(80) em vez de numerico inteiro.',
   'Incorreto: atribuiu a chave primaria incorretamente a coluna nome em vez da coluna id.',
   'E como criar uma ficha de gaveta onde o codigo numerico no topo da aba identifica a ficha de modo exclusivo (INTEGER PRIMARY KEY) e o campo do titulo aceita ate 80 letras escritas (VARCHAR(80)).',
   'O comando CREATE TABLE define o esquema fisico da relacao, associando tipos de dados ANSI e restricoes de integridade estrutural (constraints) a cada atributo.'),

  # Questao 08
  (8, '05. Comandos INSERT, UPDATE e DELETE.md',
   'DML: comandos INSERT INTO e DELETE FROM com WHERE', 'medio',
   'A tabela Tarefa tem id, descricao e status. É necessário inserir (25, Revisar cadastro, Pendente) e, depois, remover APENAS a tarefa de id 10. Qual sequência executa as operações?',
   "INSERT INTO Tarefa (id, descricao, status) VALUES (25, 'Revisar cadastro', 'Pendente'); UPDATE Tarefa SET status = 'Excluida' WHERE id = 10;",
   "INSERT INTO Tarefa (id, descricao, status) VALUES (25, 'Revisar cadastro', 'Pendente'); DELETE FROM Tarefa WHERE id = 25;",
   "INSERT INTO Tarefa (id, descricao, status) VALUES (25, 'Revisar cadastro', 'Pendente'); DELETE FROM Tarefa WHERE id = 10;",
   "INSERT INTO Tarefa (id, descricao, status) VALUES (25, 'Revisar cadastro', 'Pendente'); DELETE FROM Tarefa;",
   2,
   'Incorreto: realiza um UPDATE logico alterando o status, nao uma remocao real com DELETE.',
   'Incorreto: remove a tarefa recem-inserida de id 25, em vez de remover a tarefa de id 10.',
   'Correto: usa INSERT INTO Tarefa (...) VALUES (...) para criar o registro 25 e DELETE FROM Tarefa WHERE id = 10; com predicado exato para apagar unicamente a tarefa de identificador 10.',
   'Incorreto: um DELETE FROM Tarefa sem clausula WHERE apagaria todas as linhas da tabela.',
   'Inserir e colocar uma nova pasta no arquivo (INSERT); excluir com WHERE e pegar especificamente a pasta numero 10 e picotar no triturador de papel. Se voce esquecer o WHERE, tritura o armario inteiro.',
   'O DELETE FROM e uma operacao DML que remove tuplas fisicas. A omissao acidental da clausula WHERE constitui um dos erros operacionais mais perigosos em bancos de dados relacionais.'),

  # Questao 09
  (9, '07. Operadores e condições em consultas SQL.md',
   'Operadores LIKE, BETWEEN e AND em consultas SQL', 'medio',
   'Em Livro(id, titulo, autor, ano_publicacao), deseja-se localizar títulos que COMEÇAM com Banco e foram publicados entre 2020 e 2025, inclusive. Qual consulta produz esse resultado?',
   "SELECT * FROM Livro WHERE titulo = 'Banco%' AND ano_publicacao BETWEEN 2020 AND 2025;",
   "SELECT * FROM Livro WHERE titulo LIKE 'Banco%' AND ano_publicacao BETWEEN 2020 AND 2025;",
   "SELECT * FROM Livro WHERE titulo LIKE '%Banco' AND ano_publicacao BETWEEN 2020 AND 2025;",
   "SELECT * FROM Livro WHERE titulo LIKE 'Banco%' OR ano_publicacao BETWEEN 2020 AND 2025;",
   1,
   'Incorreto: o operador de igualdade = busca o texto literal "Banco%", desativando a interpretacao do caractere coringa %.',
   'Correto: o operador LIKE com padrao "Banco%" casa qualquer texto que inicie com a palavra "Banco", e BETWEEN 2020 AND 2025 e inclusivo em ambos os limites sob a conjuncao AND.',
   'Incorreto: o padrao "%Banco" filtraria livros que TERMINAM com a palavra "Banco".',
   'Incorreto: o operador OR retornaria livros fora da faixa de ano se comecassem com Banco, ou livros de outros assuntos publicados entre 2020 e 2025.',
   'Pense em um catalogo de biblioteca: o curinga % no final de "Banco%" significa "Banco seguido de qualquer coisa" (como "Banco de Dados", "Bancos Centrais"). E BETWEEN 2020 AND 2025 inclui os livros de 2020 ate 2025.',
   'No SQL padrao, o operador BETWEEN x AND y equivale semanticamente a expressao (coluna >= x AND coluna <= y), sendo estritamente inclusivo.'),

  # Questao 10
  (10, '10. Cláusula JOIN, junções e UNION.md',
   'Tipos de junção: LEFT JOIN e preservação de registros sem correspondência', 'medio',
   'Cliente(id, nome) e Pedido(id, cliente_id, valor_total) estão relacionadas por Pedido.cliente_id = Cliente.id. Deseja-se listar TODOS os clientes, mesmo sem pedidos, com valor_total igual a NULL quando não houver pedido. Qual consulta atende?',
   'SELECT Cliente.nome, Pedido.valor_total FROM Cliente RIGHT JOIN Pedido ON Cliente.id = Pedido.cliente_id;',
   'SELECT Cliente.nome, Pedido.valor_total FROM Cliente CROSS JOIN Pedido;',
   'SELECT Cliente.nome, Pedido.valor_total FROM Cliente INNER JOIN Pedido ON Cliente.id = Pedido.cliente_id;',
   'SELECT Cliente.nome, Pedido.valor_total FROM Cliente LEFT JOIN Pedido ON Cliente.id = Pedido.cliente_id;',
   3,
   'Incorreto: RIGHT JOIN preservaria todos os pedidos da direita, descartando clientes sem pedidos.',
   'Incorreto: CROSS JOIN calcula o produto cartesiano de todos os clientes com todos os pedidos.',
   'Incorreto: INNER JOIN descarta clientes que nao possuem correspondencia na tabela Pedido.',
   'Correto: o LEFT JOIN (ou LEFT OUTER JOIN) preserva todas as tuplas da tabela a esquerda (Cliente), preenchendo as colunas da tabela a direita (Pedido) com NULL quando nao houver casamento de chave.',
   'Imagine uma chamada em sala: o professor le o nome de todos os alunos da lista (tabela da esquerda). Se o aluno entregou o trabalho (tabela da direita), o professor anota a nota; se nao entregou, anota NULL (em branco), mas o nome do aluno continua na lista.',
   'A juncao externa a esquerda garante que nenhuma linha da entidade mandatoria seja perdida na projecao final, sendo indispensavel para relatorios de cobertura cadastral.'),

  # Questao 11
  (11, '11. Consultas aninhadas sem e com correlação.md',
   'Subconsultas não correlacionadas com funções agregadas', 'medio',
   'Funcionario(id, nome, salario, departamento) armazena salários. A empresa quer nomes e salários dos funcionários cujo salário é superior à média de TODOS os funcionários. Qual consulta atende?',
   'SELECT nome, salario FROM Funcionario WHERE salario > (SELECT MAX(salario) FROM Funcionario);',
   'SELECT nome, salario FROM Funcionario WHERE salario > (SELECT AVG(salario) FROM Funcionario);',
   "SELECT nome, salario FROM Funcionario WHERE salario > (SELECT AVG(salario) FROM Funcionario WHERE departamento = 'Vendas');",
   'SELECT nome, salario FROM Funcionario WHERE salario < (SELECT AVG(salario) FROM Funcionario);',
   1,
   'Incorreto: compara com o salario maximo MAX(salario), o que retornaria um conjunto vazio (ninguem ganha estritamente mais que o maior salario).',
   'Correto: a subconsulta (SELECT AVG(salario) FROM Funcionario) calcula a media geral de todos os colaboradores uma unica vez, e a consulta externa filtra os funcionarios com salario estritamente superior a esse valor.',
   'Incorreto: restringe a media apenas ao departamento de Vendas, e nao a todos os funcionarios.',
   'Incorreto: utiliza o operador < (menor que), retornando os salarios abaixo da media.',
   'Pense em um calculo de notas da turma: primeiro o professor calcula a media geral da sala inteira (subconsulta interna, que da 7,0); depois ele passa a lista olhando quem tirou nota acima de 7,0 (consulta externa).',
   'Por ser uma subconsulta nao correlacionada (uncorrelated subquery), a expressao interna nao depende de valores da consulta externa, sendo avaliada uma unica vez pelo otimizador do SGBD.'),

  # Questao 12
  (12, '11. Consultas aninhadas sem e com correlação.md',
   'Subconsultas correlacionadas com EXISTS e predicados compostos', 'dificil',
   'Aluno(id, nome) e Matricula(id, aluno_id, curso_id, status) estão relacionadas por Matricula.aluno_id = Aluno.id. A coordenação deseja listar uma vez cada aluno com pelo menos uma matrícula Ativa, usando EXISTS. Qual consulta atende?',
   'SELECT A.nome FROM Aluno A WHERE EXISTS (SELECT 1 FROM Matricula M WHERE M.aluno_id = A.id);',
   "SELECT A.nome FROM Aluno A WHERE EXISTS (SELECT 1 FROM Matricula M WHERE M.aluno_id = A.id AND M.status = 'Ativa');",
   "SELECT A.nome FROM Aluno A WHERE EXISTS (SELECT 1 FROM Matricula M WHERE M.status = 'Ativa');",
   "SELECT A.nome FROM Aluno A WHERE NOT EXISTS (SELECT 1 FROM Matricula M WHERE M.aluno_id = A.id AND M.status = 'Ativa');",
   1,
   'Incorreto: verifica apenas a existencia de qualquer matricula do aluno, independente do status ser Ativa ou Inativa/Cancelada.',
   'Correto: o predicado EXISTS avalia para cada linha de Aluno (A.id) se existe ao menos uma linha na tabela Matricula com o mesmo aluno_id e com status = "Ativa", retornando o aluno sem duplicatas.',
   'Incorreto: a subconsulta nao esta correlacionada com A.id; se houver qualquer matricula ativa na faculdade inteira, todos os alunos do banco serao retornados.',
   'Incorreto: NOT EXISTS retornaria os alunos que NAO possuem nenhuma matricula ativa.',
   'Pense no porteiro conferindo a lista de convidados: para cada pessoa que chega na porta (Aluno A), ele olha na planilha de credenciamento (Matricula M) para ver se ha pelo menos uma linha com o nome daquela pessoa e carimbo "Ativa". Achou a primeira, ja autoriza a entrada.',
   'O predicado correlacionado EXISTS interrompe a varredura da subconsulta assim que a primeira correspondencia e encontrada (short-circuit evaluation), tornando a execucao altamente eficiente sem gerar duplicatas no resultado.'),

  # Questao 13
  (13, '13. Comandos GRANT e REVOKE.md',
   'DCL: comando GRANT e concessão de privilégios específicos', 'facil',
   'Um usuário analista deverá consultar e atualizar a tabela Produto, mas não poderá inserir ou excluir dados. Considere que o administrador tem autorização para conceder permissões. Qual comando concede apenas os privilégios necessários?',
   'GRANT SELECT, UPDATE ON Produto TO analista;',
   'REVOKE SELECT, UPDATE ON Produto FROM analista;',
   'GRANT ALL ON Produto TO analista;',
   'GRANT INSERT, DELETE ON Produto TO analista;',
   0,
   'Correto: a sintaxe DCL GRANT SELECT, UPDATE ON Produto TO analista; concede exatamente os privilegios de leitura (SELECT) e modificacao (UPDATE) sobre a tabela especificada para o usuario indicado.',
   'Incorreto: REVOKE remove permissoes previamente concedidas, nao as concede.',
   'Incorreto: GRANT ALL concederia todos os privilegios, incluindo INSERT, DELETE e DROP, violando o principio do menor privilegio.',
   'Incorreto: concede privilegios de insercao e exclusao, exatamente os que foram proibidos.',
   'Pense em um cracha de visitante de um laboratorio: o seguranca carimba no cracha autorizacao para olhar as prateleiras (SELECT) e anotar no relatorio (UPDATE), mas nao autoriza trazer caixas novas (INSERT) nem jogar nada no lixo (DELETE).',
   'A DCL (Data Control Language) implementa o modelo de seguranca discricionario (DAC), assegurando o principio do privilegio minimo (least privilege) na governanca corporativa de dados.'),

  # Questao 14
  (14, '13. Comandos GRANT e REVOKE.md',
   'DCL: comando REVOKE e remoção de privilégios pontuais', 'medio',
   'O usuário assistente_rh tem privilégios SELECT e UPDATE concedidos diretamente sobre Funcionario. Deve manter SELECT, mas perder UPDATE. Não há outras concessões de UPDATE. Qual comando atende?',
   'GRANT SELECT ON Funcionario TO assistente_rh;',
   'REVOKE UPDATE ON Funcionario FROM assistente_rh;',
   'REVOKE ALL ON Funcionario FROM assistente_rh;',
   'REVOKE SELECT ON Funcionario FROM assistente_rh;',
   1,
   'Incorreto: tentar conceder novamente o SELECT nao revoga o UPDATE ja existente.',
   'Correto: o comando REVOKE UPDATE ON Funcionario FROM assistente_rh; remove cirurgicamente o privilegio de atualizacao mantendo intacto o privilegio de consulta (SELECT).',
   'Incorreto: REVOKE ALL removeria todos os privilegios, inclusive o SELECT que o usuario deveria manter.',
   'Incorreto: removeria a permissao de leitura (SELECT), mantendo a permissao de escrita (UPDATE).',
   'E como recolher uma das chaves do chaveiro do funcionario: ele tinha a chave da porta para entrar e ler os arquivos (SELECT) e a chave do armario de edicao (UPDATE). O administrador vai ate ele e recolhe apenas a chave do armario (REVOKE UPDATE).',
   'O comando REVOKE privilegio ON objeto FROM usuario atua diretamente nas tabelas de controle de acesso do dicionario de dados do SGBD, desautorizando comandos futuros do tipo revogado.'),

  # Questao 15
  (15, '12. Transações em banco de dados, COMMIT e ROLLBACK.md',
   'Propriedades ACID: isolamento e concorrência de transações', 'medio',
   'Em uma loja virtual, duas transações simultâneas acessam o estoque de um produto. O SGBD deve impedir interferências indevidas entre as operações concorrentes. Qual propriedade ACID está diretamente associada a esse controle?',
   'Consistência, que preserva regras e restrições de integridade.',
   'Atomicidade, que exige efetivar todas as operações de uma transação ou nenhuma.',
   'Isolamento, que controla interferências indevidas entre transações concorrentes.',
   'Durabilidade, que preserva as alterações confirmadas após falhas.',
   2,
   'Incorreto: a consistencia garante que o banco transite de um estado valido a outro em respeito as restricoes de integridade.',
   'Incorreto: a atomicidade assegura a indivisibilidade de uma transacao (tudo ou nada).',
   'Correto: o isolamento (o "I" do ACID) garante que a execucao concorrente de multiplas transacoes produza o mesmo resultado que se elas fossem executadas de maneira estritamente serial, impedindo problemas como leitura suja (dirty read) e perda de atualizacao (lost update).',
   'Incorreto: a durabilidade assegura a persistencia definitiva dos dados gravados em disco apos o COMMIT, mesmo diante de pane eletrica.',
   'Pense em duas pessoas tentando comprar a ultima poltrona do mesmo voo na internet ao mesmo tempo: o isolamento coloca uma cortina em volta da compra da primeira pessoa para que ela termine a reserva sem que a outra interfira no meio da transacao.',
   'O SGBD implementa o isolamento atraves de mecanismos de controle de concorrencia, como bloqueios de leitura/escrita (2PL - Two-Phase Locking) e controle de versao multiversao (MVCC), operando em niveis como Read Committed, Repeatable Read e Serializable.')
]

for idx, r in enumerate(raw):
    actual_id = idx + 1
    add_q(actual_id, r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12], r[13], r[14], r[15])

print(f"Geradas {len(puc_questions)} questoes de revisao oficial para SQL.")

sql_path = '/home/antigravity/leorruas/puc/banco-de-questoes/03.manipulacao-de-dados-sql.json'
with open(sql_path, 'r', encoding='utf-8') as f:
    existing_sql = json.load(f)

clean_base = [q for q in existing_sql if not q.get('id', '').startswith('SQL-REV-')]
print(f"Questoes base preservadas: {len(clean_base)}")

for q in clean_base:
    if 'prioritaria' not in q:
        q['prioritaria'] = False
    if 'origem' not in q:
        q['origem'] = 'banco_sintetico_vault'

merged = puc_questions + clean_base

with open(sql_path, 'w', encoding='utf-8') as f:
    json.dump(merged, f, ensure_ascii=False, indent=2)

print(f"Sucesso: {len(merged)} questoes salvas em {sql_path}.")
