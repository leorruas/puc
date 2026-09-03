// js/vault.js - Gerenciamento de Dados, Carregamento e Fallback do Vault

// Metadados e resumos de cada disciplina para o leitor e índice
export const informacoesDisciplinas = {
    "00. Geral": { numero: "01", resumo: "mapa de aprendizagem, aula inaugural e introdução ao curso" },
    "00. Sintaxe Multilinguagem": { numero: "02", resumo: "comparativo de sintaxe c#, java, python e javascript" },
    "01. Programacao Modular": { numero: "03", resumo: "classes, encapsulamento, herança e polimorfismo em c#" },
    "02. Modelagem de Dados": { numero: "04", resumo: "modelo relacional, entidades, relacionamentos e normalização" },
    "03. Manipulacao de Dados SQL": { numero: "05", resumo: "consultas dml, joins, agrupamentos, views e ddl" },
    "04. Algoritmos e Estruturas de Dados": { numero: "06", resumo: "arrays, listas, pilhas, filas e análise assintótica" },
    "05. Desenvolvimento Web Back-End": { numero: "07", resumo: "arquitetura mvc, apis rest, autenticação e rotas" },
    "06. Projeto - Aplicacao Interativa": { numero: "08", resumo: "projeto de extensão ods 4, requisitos e entregas" },
    "07. Engenharia de Requisitos": { numero: "09", resumo: "elicitação, especificação, casos de uso e modelagem uml" },
    "08. Design de Interacao": { numero: "10", resumo: "experiência do usuário, heurísticas de usabilidade e ihc" },
    "09. Redes de Computadores": { numero: "11", resumo: "arquitetura tcp/ip, camadas, roteamento e protocolos" },
    "10. Lideranca e Competencias": { numero: "12", resumo: "gestão de equipes ágeis, comunicação e liderança" },
    "11. Desafios Contemporaneos": { numero: "13", resumo: "ética na computação, inteligência artificial e sociedade" }
};

// Lista de arquivos Markdown estáticos para fallback de alta disponibilidade offline ou erro de API
const arquivosFallback = [
    "00. Geral/Aula Inaugural (04-08-2026) - Resumo.md",
    "00. Geral/Aula Inaugural (04-08-2026) - Transcrição.md",
    "00. Geral/Mapa de aprendizagem do semestre.md",
    "00. Sintaxe Multilinguagem/00. Guia multilinguagem de sintaxe e praticas - Índice.md",
    "00. Sintaxe Multilinguagem/00. Evolução das linguagens e genealogia do C (C, C++, Java, C#, JS, Python).md",
    "00. Sintaxe Multilinguagem/01. Variáveis, tipos e atribuição.md",
    "00. Sintaxe Multilinguagem/02. Estruturas condicionais (if, else, switch).md",
    "00. Sintaxe Multilinguagem/03. Estruturas de repetição (while, for, do-while).md",
    "00. Sintaxe Multilinguagem/04. Sub-rotinas (funções e procedimentos).md",
    "00. Sintaxe Multilinguagem/05. Abstração e encapsulamento com classes (TADs).md",
    "00. Sintaxe Multilinguagem/06. Modificadores de acesso, escopo e a palavra-chave static.md",
    "00. Sintaxe Multilinguagem/07. Getters, setters e propriedades (acesso e modificação de estado).md",
    "00. Sintaxe Multilinguagem/08. Estruturas de dados fundamentais (materialização de modelos mentais em código).md",
    "00. Sintaxe Multilinguagem/09. Tratamento de exceções e erros (try, catch, finally, throw).md",
    "00. Sintaxe Multilinguagem/10. Manipulação e representação de datas e horários (DateTime, fusos e formatos).md",
    "00. Sintaxe Multilinguagem/11. Herança, superclasses e subclasses (sintaxe comparada e extensibilidade).md",
    "00. Sintaxe Multilinguagem/12. Sobrescrita de métodos e representação textual (ToString, toString, __str__).md",
    "00. Sintaxe Multilinguagem/13. Igualdade de objetos, comparação e hashing (Equals, GetHashCode, hashCode, __eq__).md",
    "00. Sintaxe Multilinguagem/14. Tipos genéricos e polimorfismo paramétrico (Generics, TypeVar, Any, Templates).md",
    "00. Sintaxe Multilinguagem/15. Expressões lambda, delegates e funções de primeira classe (callbacks, arrow functions, closures).md",
    "01. Programacao Modular/00. Programação modular - Resumo.md",
    "01. Programacao Modular/01. Introdução à programação modular.md",
    "01. Programacao Modular/02. Funções e procedimentos.md",
    "01. Programacao Modular/03. Tipos abstratos de dados.md",
    "01. Programacao Modular/04. Programação orientada a objetos e acoplamento.md",
    "01. Programacao Modular/05. Fatores externos de qualidade de software.md",
    "01. Programacao Modular/06. Fatores internos de qualidade de software.md",
    "01. Programacao Modular/07. Atributos e métodos (classes, objetos e definição de membros).md",
    "01. Programacao Modular/08. Construtores (inicialização, sobrecarga e garantia de invariantes).md",
    "01. Programacao Modular/09. Atributos estáticos e propriedades (compartilhamento de estado e encapsulamento).md",
    "01. Programacao Modular/10. Destrutores e finalizadores (desalocação de memória e liberação de recursos).md",
    "01. Programacao Modular/11. Princípio da ocultação da informação (information hiding e encapsulamento).md",
    "01. Programacao Modular/12. Modificadores de acesso (visibilidade e níveis de proteção no encapsulamento).md",
    "01. Programacao Modular/13. Métodos de acesso e propriedades (publicação de contratos e garantia de invariantes).md",
    "01. Programacao Modular/14. Namespaces e partial classes (espaços de nomes e modularização em larga escala).md",
    "01. Programacao Modular/15. Herança (generalização, especialização e extensibilidade modular).md",
    "01. Programacao Modular/16. Construtores em classes filhas (ordem de inicialização e a cláusula base).md",
    "01. Programacao Modular/17. Sobreposição de métodos (virtual e override).md",
    "01. Programacao Modular/18. Classes abstratas e métodos abstratos (contratos de herança e polimorfismo puro).md",
    "01. Programacao Modular/19. Classes e membros selados (sealed).md",
    "01. Programacao Modular/20. Tipos genéricos (generics, type safety e coleções homogêneas).md",
    "01. Programacao Modular/21. Coleções genéricas em C# (estruturas de dados, propósitos e performance assintótica).md",
    "01. Programacao Modular/22. Delegates, funções anônimas, expressões lambda e eventos em C#.md",
    "01. Programacao Modular/23. Princípios SOLID de design orientado a objetos.md",
    "01. Programacao Modular/24. Padrões de projeto (design patterns) e o catálogo GoF.md",
    "01. Programacao Modular/Glossário de conceitos.md",
    "01. Programacao Modular/Prompts de Estudo (LLM).md",
    "02. Modelagem de Dados/00. Modelagem de Dados - Resumo.md",
    "02. Modelagem de Dados/01. Introdução à modelagem de dados e sua importância.md",
    "02. Modelagem de Dados/02. Abordagem de arquivos vs. abordagem de banco de dados.md",
    "02. Modelagem de Dados/03. Linguagens de banco de dados (ddl e dml) e perfis profissionais.md",
    "02. Modelagem de Dados/04. Níveis do sgbd e etapas do projeto de banco de dados.md",
    "02. Modelagem de Dados/05. Modelagem de entidades e tipos de atributos.md",
    "02. Modelagem de Dados/06. Modelagem de relacionamentos, cardinalidade e restrições de participação.md",
    "02. Modelagem de Dados/Glossário de conceitos.md",
    "02. Modelagem de Dados/Prompts de Estudo (LLM).md",
    "03. Manipulacao de Dados SQL/03. Manipulacao de Dados SQL - Resumo.md",
    "03. Manipulacao de Dados SQL/Prompts de Estudo (LLM).md",
    "04. Algoritmos e Estruturas de Dados/04. Algoritmos e Estruturas de Dados - Resumo.md",
    "04. Algoritmos e Estruturas de Dados/Recordando C# e arrays.md",
    "04. Algoritmos e Estruturas de Dados/Prompts de Estudo (LLM).md",
    "05. Desenvolvimento Web Back-End/05. Desenvolvimento Web Back-End - Resumo.md",
    "05. Desenvolvimento Web Back-End/Prompts de Estudo (LLM).md",
    "06. Projeto - Aplicacao Interativa/00. Projeto - Aplicacao Interativa - Resumo.md",
    "06. Projeto - Aplicacao Interativa/01. Ods 4 educação de qualidade - conceito, metas e fundamentação.md",
    "06. Projeto - Aplicacao Interativa/02. Requisitos e diretrizes de escopo do projeto.md",
    "06. Projeto - Aplicacao Interativa/03. Cronograma semanal e entregas de etapas.md",
    "06. Projeto - Aplicacao Interativa/04. Reunião inicial da turma 5 (08-08-2026) - resumo e transcrição integral.md",
    "06. Projeto - Aplicacao Interativa/05. Reunião de acompanhamento do grupo 4 (20-08-2026) - resumo e transcrição integral.md",
    "06. Projeto - Aplicacao Interativa/06. Reunião de acompanhamento do grupo 4 (27-08-2026) - resumo e transcrição integral.md",
    "06. Projeto - Aplicacao Interativa/Prompts de Estudo (LLM).md",
    "07. Engenharia de Requisitos/07. Engenharia de Requisitos - Resumo.md",
    "07. Engenharia de Requisitos/01. O que é, afinal, engenharia de requisitos.md",
    "07. Engenharia de Requisitos/02. Engenharia de requisitos e negócios - o alinhamento estratégico.md",
    "07. Engenharia de Requisitos/03. O conceito de requisito de software - definição, níveis e características.md",
    "07. Engenharia de Requisitos/04. Requisitos funcionais e não-funcionais.md",
    "07. Engenharia de Requisitos/05. Como escrever requisitos de qualidade - critérios, padrões e boas práticas.md",
    "07. Engenharia de Requisitos/06. Técnicas de elicitação de requisitos.md",
    "07. Engenharia de Requisitos/07. Visão geral da uml e tipos de diagramas na modelagem de requisitos.md",
    "07. Engenharia de Requisitos/08. Modelagem de requisitos com casos de uso e especificações textuais.md",
    "07. Engenharia de Requisitos/09. Modelagem estrutural com diagrama de classes da uml.md",
    "07. Engenharia de Requisitos/10. Modelagem estrutural e modularização com diagrama de pacotes da uml.md",
    "07. Engenharia de Requisitos/11. Verificação e validação de requisitos - técnicas, revisões e qualidade.md",
    "07. Engenharia de Requisitos/Prompts de Estudo (LLM).md",
    "08. Design de Interacao/12. Design de Interacao - Resumo.md",
    "08. Design de Interacao/01. O que é interação humano-computador e a visão teórica do ser humano.md",
    "08. Design de Interacao/02. Construções teóricas da interação humano-computador.md",
    "08. Design de Interacao/03. O papel dos sistemas interativos na atividade humana.md",
    "08. Design de Interacao/04. Perspectivas de interação usuário-sistema - interagir com o sistema vs. por meio do sistema.md",
    "08. Design de Interacao/05. Por que a perspectiva da interação importa.md",
    "08. Design de Interacao/06. Contexto de uso, interface, interação e papéis do design.md",
    "08. Design de Interacao/07. Atributos de qualidade em sistemas interativos - usabilidade, comunicabilidade, acessibilidade e experiência de uso.md",
    "08. Design de Interacao/08. Engenharia cognitiva e os problemas da interação usuário-sistema.md",
    "08. Design de Interacao/09. Engenharia semiótica - comunicação usuário-sistema e metacomunicação usuário-designer.md",
    "08. Design de Interacao/10. Envolvimento do usuário no design - projetar de modo independente, centrado ou participativo.md",
    "08. Design de Interacao/11. Racionalismo técnico e reflexão em ação - o papel da técnica e da criatividade no design.md",
    "08. Design de Interacao/Prompts de Estudo (LLM).md",
    "09. Redes de Computadores/09. Redes de Computadores - Resumo.md",
    "09. Redes de Computadores/Prompts de Estudo (LLM).md",
    "10. Lideranca e Competencias/10. Lideranca e Competencias - Resumo.md",
    "10. Lideranca e Competencias/Prompts de Estudo (LLM).md",
    "11. Desafios Contemporaneos/11. Desafios Contemporaneos - Resumo.md",
    "11. Desafios Contemporaneos/Prompts de Estudo (LLM).md"
];

/**
 * Consulta a árvore do repositório no GitHub ou retorna o catálogo de fallback normalizado.
 */
export async function obterListaDeArquivos() {
    try {
        const resposta = await fetch("https://api.github.com/repos/leorruas/puc/git/trees/main?recursive=1");
        if (!resposta.ok) throw new Error("Erro na API do GitHub");

        const dados = await resposta.json();

        return dados.tree
            .filter(item => {
                const pathLower = item.path.toLowerCase();
                const fileName = pathLower.split("/").pop();

                if (!item.path.endsWith(".md")) return false;
                if (item.path.includes(".obsidian") || item.path.includes(".git") || item.path.includes(".gemini") || item.path.includes(".agents")) return false;
                if (fileName === "agents.md" || fileName === "index.md" || fileName === "me.md" || fileName === "log.md" || fileName === "gemini.md") return false;

                return true;
            })
            .map(item => {
                const nomeSemExtensao = item.path.split("/").pop().replace(".md", "");
                const partes = item.path.split("/");
                const categoria = partes.length > 1 ? partes[0] : "00. Geral";
                const urlSegura = "https://raw.githubusercontent.com/leorruas/puc/main/" + item.path.split("/").map(encodeURIComponent).join("/");
                return {
                    titulo: nomeSemExtensao,
                    path: urlSegura,
                    sourcePath: item.path,
                    categoria: categoria
                };
            });
    } catch (erro) {
        console.warn("Não foi possível listar via GitHub, usando lista padrão completa:", erro);
        return arquivosFallback.map(p => {
            const nomeSemExtensao = p.split("/").pop().replace(".md", "");
            const partes = p.split("/");
            const categoria = partes.length > 1 ? partes[0] : "00. Geral";
            const urlSegura = "https://raw.githubusercontent.com/leorruas/puc/main/" + p.split("/").map(encodeURIComponent).join("/");
            return {
                titulo: nomeSemExtensao,
                path: urlSegura,
                sourcePath: p,
                categoria: categoria
            };
        });
    }
}
