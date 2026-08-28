// Função para buscar automaticamente todos os arquivos .md do seu GitHub (sem precisar de token)
async function obterListaDeArquivos() {
    try {
        const resposta = await fetch("https://api.github.com/repos/leorruas/puc/git/trees/main?recursive=1");
        if (!resposta.ok) throw new Error("Erro na API do GitHub");

        const dados = await resposta.json();

        // Filtra apenas os arquivos Markdown (.md), ignorando arquivos de sistema, index raiz e regras de agentes
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
                return {
                    titulo: nomeSemExtensao,
                    // Usa a cópia pública para funcionar também quando o leitor é aberto via file:// pelo Obsidian.
                    path: encodeURI(`https://raw.githubusercontent.com/leorruas/puc/main/${item.path}`),
                    sourcePath: item.path,
                    categoria: categoria
                };
            });
    } catch (erro) {
        console.warn("Não foi possível listar via GitHub, usando lista padrão completa:", erro);
        const arquivosFallback = [
            "00. Geral/Aula Inaugural (04-08-2026) - Resumo.md",
            "00. Geral/Aula Inaugural (04-08-2026) - Transcrição.md",
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
            "01. Programacao Modular/Glossário de conceitos.md",
            "01. Programacao Modular/Prompts de Estudo (LLM).md",
            "02. Modelagem de Dados/02. Modelagem de Dados - Resumo.md",
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

        return arquivosFallback.map(p => {
            const nomeSemExtensao = p.split("/").pop().replace(".md", "");
            const partes = p.split("/");
            const categoria = partes.length > 1 ? partes[0] : "00. Geral";
            return {
                titulo: nomeSemExtensao,
                path: encodeURI(`https://raw.githubusercontent.com/leorruas/puc/main/${p}`),
                sourcePath: p,
                categoria: categoria
            };
        });
    }
}

// Descrições e Metadados das Matérias para o Design Suíço
const informacoesDisciplinas = {
    "00. Geral": { numero: "01", resumo: "aula inaugural e introdução ao curso de ads" },
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

// Variáveis globais
let todosOsArtigos = [];
let todasAsPastas = {};
let artigoAtual = null;

const campoTexto = document.getElementById("main-search-input");
const containerResultados = document.querySelector(".cards-container");
const divResultados = document.getElementById("resultados");
const leitorDeArtigo = document.getElementById("leitor-artigo");
const leitorDeDisciplina = document.getElementById("disciplina-leitor");
const disciplinaCabecalho = document.getElementById("disciplina-cabecalho");
const disciplinaAcoes = document.getElementById("disciplina-acoes");
const artigoTitulo = document.getElementById("artigo-titulo");
const artigoCorpo = document.getElementById("artigo-corpo");
const btnVoltar = document.getElementById("btn-voltar");
const btnVoltarDisciplina = document.getElementById("btn-voltar-disciplina");
const retornoArtigoTexto = document.getElementById("retorno-artigo-texto");
const btnTema = document.getElementById("theme-toggle");

// Controle de Tema (Claro / Escuro)
function aplicarTema(tema, persistir = true) {
    document.documentElement.dataset.theme = tema;
    if (persistir) localStorage.setItem("tema-puc-ads", tema);
    if (btnTema) {
        const proximoTema = tema === "dark" ? "modo claro" : "modo escuro";
        btnTema.textContent = proximoTema;
        btnTema.setAttribute("aria-label", `Alternar para ${proximoTema}`);
    }
}

function configurarMermaid() {
    if (typeof mermaid === "undefined") return;

    const temaEscuro = document.documentElement.dataset.theme !== "light";
    mermaid.initialize({
        startOnLoad: false,
        theme: "base",
        fontFamily: "Archivo, sans-serif",
        fontSize: 16,
        flowchart: {
            curve: "linear",
            defaultRenderer: "dagre-wrapper",
            nodeSpacing: 42,
            rankSpacing: 56,
            padding: 16
        },
        themeVariables: temaEscuro ? {
            fontFamily: "Archivo, sans-serif",
            fontSize: "16px",
            darkMode: true,
            background: "#101010",
            primaryColor: "#182431",
            primaryTextColor: "#f1f0eb",
            primaryBorderColor: "#6fa8e8",
            lineColor: "#9ab0c5",
            secondaryColor: "#15191d",
            tertiaryColor: "#20262d"
        } : {
            fontFamily: "Archivo, sans-serif",
            fontSize: "16px",
            darkMode: false,
            background: "#ffffff",
            primaryColor: "#eef5fc",
            primaryTextColor: "#151515",
            primaryBorderColor: "#1c5f9f",
            lineColor: "#3f6282",
            secondaryColor: "#f7f9fc",
            tertiaryColor: "#e8f0f8"
        }
    });
}

function renderizarDiagramasMermaid() {
    if (typeof mermaid === "undefined" || !artigoCorpo) return;
    configurarMermaid();

    const diagramas = artigoCorpo.querySelectorAll(".mermaid");
    diagramas.forEach(diagrama => {
        const codigo = diagrama.dataset.mermaidSource || diagrama.textContent;
        diagrama.dataset.mermaidSource = codigo;
        diagrama.removeAttribute("data-processed");
        diagrama.textContent = codigo;
    });

    mermaid.run({ nodes: diagramas }).catch(err => {
        console.error("Erro ao renderizar Mermaid:", err);
    });
}

function inicializarTema() {
    const temaSalvo = localStorage.getItem("tema-puc-ads");
    const temaDoSistema = window.matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark";
    aplicarTema(temaSalvo || temaDoSistema, false);
}

if (btnTema) {
    btnTema.addEventListener("click", () => {
        const temaAtual = document.documentElement.dataset.theme === "light" ? "light" : "dark";
        const novoTema = temaAtual === "dark" ? "light" : "dark";
        aplicarTema(novoTema, true);
        renderizarDiagramasMermaid();
    });
}

function limparNomeCategoria(categoria) {
    return categoria.replace(/^\d+\.\s*/, "").toLowerCase();
}

function obterRotaCategoria(categoria) {
    return `#/disciplina/${encodeURIComponent(categoria)}`;
}

function rotaDoArtigo(artigo) {
    return `#/${encodeURIComponent(artigo.categoria)}/${encodeURIComponent(artigo.titulo)}`;
}

// Carrega os arquivos e busca o conteúdo de cada um
async function carregarTodosOsArtigos() {
    inicializarTema();
    const lista = await obterListaDeArquivos();

    // Promessas paralelas para ler o conteúdo Markdown de cada arquivo
    const promessas = lista.map(async (item) => {
        try {
            const res = await fetch(item.path);
            if (!res.ok) return null;
            const texto = await res.text();
            
            const caminhoDecodificado = decodeURI(item.path);
            const partes = caminhoDecodificado.replace("./", "").split("/");
            const categoria = item.categoria || (partes.length > 1 ? partes[0] : "00. Geral");

            return {
                titulo: item.titulo,
                path: item.path,
                sourcePath: item.sourcePath || item.path,
                categoria: categoria,
                conteudo: texto
            };
        } catch (e) {
            console.error(`Erro ao carregar ${item.path}:`, e);
            return null;
        }
    });

    const resultados = await Promise.all(promessas);
    todosOsArtigos = resultados.filter(artigo => artigo !== null);

    // Organiza artigos em estrutura de pasta para as matérias
    todasAsPastas = {};
    todosOsArtigos.forEach(artigo => {
        if (!todasAsPastas[artigo.categoria]) {
            todasAsPastas[artigo.categoria] = [];
        }
        todasAsPastas[artigo.categoria].push(artigo);
    });

    // Ordena os artigos dentro de cada matéria pelo caminho e numeração real
    Object.values(todasAsPastas).forEach(artigos => {
        artigos.sort((a, b) => {
            return (a.sourcePath || a.path).localeCompare(b.sourcePath || b.path, "pt-BR", { numeric: true, sensitivity: 'base' });
        });
    });

    // Renderiza a grade suíça de matérias na página inicial
    renderizarPastas();

    // Se a página for carregada com rota no Hash, abre a rota correspondente
    if (window.location.hash) {
        tratarHashNavegacao();
    }
}

// Renderiza a Grade Suíça de Matérias na Home
function renderizarPastas() {
    const orientacoesContainer = document.getElementById("orientacoes-container");
    const pastasContainer = document.getElementById("pastas-container");
    if (!pastasContainer || !orientacoesContainer) return;

    pastasContainer.innerHTML = "";
    orientacoesContainer.innerHTML = "";

    const todasCategorias = Object.keys(todasAsPastas).sort((a, b) => a.localeCompare(b, "pt-BR", { numeric: true }));

    const categoriasOrientacao = ["00. Geral", "00. Sintaxe Multilinguagem"];

    todasCategorias.forEach(categoria => {
        const info = informacoesDisciplinas[categoria] || {
            numero: categoria.match(/^\d+/)?.[0] || "•",
            resumo: `${todasAsPastas[categoria].length} artigos disponíveis`
        };

        const card = document.createElement("a");
        card.className = "disciplina-card";
        card.href = obterRotaCategoria(categoria);
        card.setAttribute("aria-label", `Abrir disciplina ${limparNomeCategoria(categoria)}`);

        card.innerHTML = `
            <span class="indice-numero">${info.numero}</span>
            <span class="disciplina-card-conteudo">
                <strong>${limparNomeCategoria(categoria)}</strong>
                <span class="indice-resumo">${info.resumo}</span>
            </span>
        `;

        card.addEventListener("click", (e) => {
            if (e.metaKey || e.ctrlKey || e.shiftKey || e.button === 1) return;
            e.preventDefault();
            abrirDisciplina(categoria);
        });

        if (categoriasOrientacao.includes(categoria)) {
            orientacoesContainer.appendChild(card);
        } else {
            pastasContainer.appendChild(card);
        }
    });
}

// Visualizador da Matéria (Lista Suíça de Artigos da Disciplina)
function abrirDisciplina(categoria, atualizarRota = true) {
    const artigos = todasAsPastas[categoria] || [];
    if (artigos.length === 0) return;

    leitorDeArtigo.classList.add("escondido");
    divResultados.classList.add("escondido");
    document.getElementById("orientacoes-iniciais")?.classList.add("escondido");
    document.getElementById("explorar-disciplinas")?.classList.add("escondido");
    artigoAtual = null;

    if (atualizarRota && window.location.hash !== obterRotaCategoria(categoria)) {
        history.pushState({ categoria: categoria }, "", obterRotaCategoria(categoria));
    }

    const breadcrumbs = document.getElementById("disciplina-breadcrumbs");
    breadcrumbs.innerHTML = "";
    const inicio = document.createElement("button");
    inicio.type = "button";
    inicio.className = "breadcrumb-link";
    inicio.textContent = "início";
    inicio.addEventListener("click", () => voltarParaHome(true));

    const separador = document.createElement("span");
    separador.className = "breadcrumb-separator";
    separador.textContent = "/";

    const atual = document.createElement("span");
    atual.textContent = limparNomeCategoria(categoria);

    breadcrumbs.append(inicio, separador, atual);

    disciplinaCabecalho.innerHTML = `
        <p class="disciplina-rotulo">matéria • ${artigos.length} artigos</p>
        <h2>${limparNomeCategoria(categoria)}</h2>
    `;

    disciplinaAcoes.innerHTML = "";
    artigos.forEach((artigo, idx) => {
        const acao = document.createElement("a");
        acao.className = "disciplina-acao";
        acao.href = rotaDoArtigo(artigo);
        acao.setAttribute("aria-label", artigo.titulo);

        const numeroFormatado = String(idx + 1).padStart(2, "0");

        acao.innerHTML = `
            <span class="disciplina-acao-numero">${numeroFormatado}</span>
            <span class="disciplina-acao-conteudo">
                <strong>${artigo.titulo}</strong>
            </span>
        `;

        acao.addEventListener("click", (event) => {
            if (event.metaKey || event.ctrlKey || event.shiftKey || event.button === 1) return;
            event.preventDefault();
            abrirArtigo(artigo.titulo, artigo.conteudo);
        });

        disciplinaAcoes.appendChild(acao);
    });

    leitorDeDisciplina.classList.remove("escondido");
    window.scrollTo({ top: 0, behavior: "instant" });
}

// Filtro de Busca Suíça em Tempo Real
function filtrarArtigos(termoBusca) {
    leitorDeDisciplina.classList.add("escondido");
    leitorDeArtigo.classList.add("escondido");

    if (!termoBusca || termoBusca.trim() === "") {
        divResultados.classList.add("escondido");
        containerResultados.innerHTML = "";
        document.getElementById("orientacoes-iniciais")?.classList.remove("escondido");
        document.getElementById("explorar-disciplinas")?.classList.remove("escondido");
        return;
    }

    const termo = termoBusca.toLowerCase().trim();

    document.getElementById("orientacoes-iniciais")?.classList.add("escondido");
    document.getElementById("explorar-disciplinas")?.classList.add("escondido");
    divResultados.classList.remove("escondido");

    if (termo.length < 2) {
        containerResultados.innerHTML = `<p class="mensagem-busca">digite ao menos <strong>duas letras</strong> para pesquisar nos tópicos e artigos.</p>`;
        return;
    }

    const filtrados = todosOsArtigos
        .filter(artigo => artigo.titulo.toLowerCase().includes(termo) || artigo.conteudo.toLowerCase().includes(termo))
        .sort((a, b) => {
            const prioridadeA = a.titulo.toLowerCase().includes(termo) ? 0 : 1;
            const prioridadeB = b.titulo.toLowerCase().includes(termo) ? 0 : 1;
            return prioridadeA - prioridadeB || a.titulo.localeCompare(b.titulo, "pt-BR", { numeric: true });
        });

    exibirResultados(filtrados, termo);
}

function destacarTexto(texto, termo) {
    if (!termo) return texto;
    const regex = new RegExp(`(${termo.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'gi');
    return texto.replace(regex, '<mark class="highlight">$1</mark>');
}

function escaparHtml(texto) {
    const elemento = document.createElement("span");
    elemento.textContent = texto;
    return elemento.innerHTML;
}

function removerFrontmatter(markdown) {
    if (!markdown) return "";
    return markdown.replace(/^---[\s\S]*?---\s*/, "");
}

function removerPrimeiroH1(markdown) {
    if (!markdown) return "";
    return markdown.replace(/^\s*#\s+[^\n\r]+(\r?\n|$)/, "");
}

function extrairTrechoRelevante(conteudo, termo) {
    const conteudoSemFrontmatter = removerFrontmatter(conteudo);
    const textoLimpo = conteudoSemFrontmatter.replace(/==/g, '').replace(/[#*`_~\[\]]/g, ' ');
    const pos = textoLimpo.toLowerCase().indexOf(termo.toLowerCase());
    
    if (pos === -1) {
        return textoLimpo.substring(0, 140) + "...";
    }
    
    const inicio = Math.max(0, pos - 50);
    const fim = Math.min(textoLimpo.length, pos + termo.length + 80);
    let trecho = textoLimpo.substring(inicio, fim);
    
    if (inicio > 0) trecho = "..." + trecho;
    if (fim < textoLimpo.length) trecho = trecho + "...";
    
    return trecho;
}

function exibirResultados(artigos, termo = "") {
    containerResultados.innerHTML = "";
    leitorDeArtigo.classList.add("escondido");
    leitorDeDisciplina.classList.add("escondido");
    divResultados.classList.remove("escondido");

    if (artigos.length === 0) {
        containerResultados.innerHTML = `<p class="mensagem-busca">nenhum artigo ou tópico encontrado para <strong>“${escaparHtml(termo)}”</strong>.</p>`;
        return;
    }

    const resumoBusca = document.createElement("p");
    resumoBusca.className = "resumo-busca";
    resumoBusca.textContent = `${artigos.length} ${artigos.length === 1 ? "artigo encontrado" : "artigos encontrados"} para “${termo}”`;
    containerResultados.appendChild(resumoBusca);

    // Agrupa resultados por matéria
    const grupos = {};
    artigos.forEach(artigo => {
        if (!grupos[artigo.categoria]) grupos[artigo.categoria] = [];
        grupos[artigo.categoria].push(artigo);
    });

    Object.keys(grupos)
        .sort((a, b) => a.localeCompare(b, "pt-BR", { numeric: true }))
        .forEach(categoria => {
            const grupoDiv = document.createElement("div");
            grupoDiv.className = "busca-grupo-assunto";

            const tituloGrupo = document.createElement("h3");
            tituloGrupo.className = "busca-assunto-titulo";
            tituloGrupo.textContent = limparNomeCategoria(categoria);
            grupoDiv.appendChild(tituloGrupo);

            const subCardsContainer = document.createElement("div");
            subCardsContainer.className = "resultados-lista";

            grupos[categoria].forEach((artigo, indice) => {
                const card = document.createElement("a");
                card.className = "resultado-item";
                card.href = rotaDoArtigo(artigo);

                const numero = document.createElement("span");
                numero.className = "resultado-numero";
                numero.textContent = String(indice + 1).padStart(2, "0");

                const conteudoResultado = document.createElement("span");
                conteudoResultado.className = "resultado-conteudo";

                const titulo = document.createElement("strong");
                titulo.innerHTML = destacarTexto(artigo.titulo, termo);

                const trecho = document.createElement("span");
                trecho.className = "resultado-trecho";
                const textoTrecho = extrairTrechoRelevante(artigo.conteudo, termo);
                trecho.innerHTML = destacarTexto(textoTrecho, termo);

                conteudoResultado.appendChild(titulo);
                conteudoResultado.appendChild(trecho);
                card.appendChild(numero);
                card.appendChild(conteudoResultado);

                card.addEventListener("click", (event) => {
                    if (event.metaKey || event.ctrlKey || event.shiftKey || event.button === 1) return;
                    event.preventDefault();
                    abrirArtigo(artigo.titulo, artigo.conteudo);
                });

                subCardsContainer.appendChild(card);
            });

            grupoDiv.appendChild(subCardsContainer);
            containerResultados.appendChild(grupoDiv);
        });
}

function normalizarListasObsidian(md) {
    if (!md) return "";
    const linhas = md.split("\n");
    let dentroDeBlocoDeCodigo = false;

    return linhas.map(linha => {
        const linhaTrim = linha.trim();
        if (linhaTrim.startsWith("```")) {
            dentroDeBlocoDeCodigo = !dentroDeBlocoDeCodigo;
            return linha;
        }

        if (dentroDeBlocoDeCodigo) {
            return linha;
        }

        const match = linha.match(/^(\s+)([\*\-\+]|\d+\.|\w)/);
        if (match) {
            const spaces = match[1].length;
            const rest = linha.substring(spaces);
            const targetSpaces = Math.ceil(spaces / 4) * 4;
            return " ".repeat(targetSpaces) + rest;
        }
        return linha;
    }).join("\n");
}

function protegerPipesObsidian(md) {
    if (!md) return "";
    return md.replace(/\[\[([^\]]+)\]\]/g, (match, conteudoInterno) => {
        const protegido = conteudoInterno.replace(/\\?\|/g, "%%OBSIDIANPIPE%%");
        return "[[" + protegido + "]]";
    });
}

function processarLaTeXSetas(md) {
    if (!md) return "";
    return md
        .replace(/\$\s*\\rightarrow\s*\$/gi, "→")
        .replace(/\$\s*\\to\s*\$/gi, "→")
        .replace(/\$\s*\\leftarrow\s*\$/gi, "←")
        .replace(/\$\s*\\leftrightarrow\s*\$/gi, "↔")
        .replace(/\$\s*\\Rightarrow\s*\$/gi, "⇒")
        .replace(/\$\s*\\Leftarrow\s*\$/gi, "⇐")
        .replace(/\$\s*\\Leftrightarrow\s*\$/gi, "⇔")
        .replace(/\\rightarrow(?![a-zA-Z])/gi, "→")
        .replace(/\\leftarrow(?![a-zA-Z])/gi, "←")
        .replace(/\\leftrightarrow(?![a-zA-Z])/gi, "↔");
}

function extrairIndiceGlossario(md) {
    const inicio = md.match(/^##\s+Índice temático\s*$(?:\r?\n)?/im);
    if (!inicio || inicio.index === undefined) return null;

    const antes = md.slice(0, inicio.index);
    const depoisDoTitulo = md.slice(inicio.index + inicio[0].length);
    const fim = depoisDoTitulo.search(/^---\s*$\r?\n\r?\n^##\s+/m);
    if (fim === -1) return null;

    const indiceMarkdown = depoisDoTitulo.slice(0, fim);
    const depois = depoisDoTitulo.slice(fim);
    const grupos = [];
    let grupoAtual = null;

    indiceMarkdown.split(/\r?\n/).forEach(linha => {
        const tituloGrupo = linha.match(/^###\s+(.+)$/);
        if (tituloGrupo) {
            grupoAtual = { titulo: tituloGrupo[1].trim(), termos: [] };
            grupos.push(grupoAtual);
            return;
        }

        if (!grupoAtual) return;
        const regexLink = /\[\[([^|\]]+)\|([^\]]+)\]\]/g;
        let link;
        while ((link = regexLink.exec(linha)) !== null) {
            grupoAtual.termos.push({ destino: link[1].trim(), rotulo: link[2].trim() });
        }
    });

    if (!grupos.length) return null;
    return { markdown: antes + depois, grupos };
}

function removerContextoDoCorpo(md) {
    return md.replace(/^>\s*(?:\*\*Contexto:\*\*\s*)?[^\n\r]+(?:\r?\n>[^\n\r]+)*(?:\r?\n){1,2}/m, "");
}

function renderizarNavegacaoGlossario(grupos) {
    if (!grupos?.length || !artigoCorpo) return;

    const navegacao = document.createElement("nav");
    navegacao.className = "glossario-navegacao";
    navegacao.setAttribute("aria-label", "Índice temático do glossário");
    navegacao.innerHTML = '<p class="glossario-navegacao-rotulo">índice temático</p>';

    const listaGrupos = document.createElement("div");
    listaGrupos.className = "glossario-grupos";

    grupos.forEach((grupo, indice) => {
        const secao = document.createElement("section");
        secao.className = "glossario-grupo";
        secao.id = `glossario-grupo-${indice + 1}`;

        const titulo = document.createElement("h2");
        titulo.textContent = grupo.titulo;
        secao.appendChild(titulo);

        const termos = document.createElement("div");
        termos.className = "glossario-termos";

        grupo.termos.forEach(termo => {
            const botao = document.createElement("button");
            botao.type = "button";
            botao.className = "glossario-termo";
            botao.dataset.destino = termo.destino;
            botao.innerHTML = typeof marked !== "undefined" ? marked.parseInline(termo.rotulo) : termo.rotulo;
            botao.addEventListener("click", () => navegarParaLinkObsidian(termo.destino));
            termos.appendChild(botao);
        });

        secao.appendChild(termos);
        listaGrupos.appendChild(secao);
    });

    navegacao.appendChild(listaGrupos);
    artigoCorpo.prepend(navegacao);
}

// Leitor de Artigos com Suporte Suíço
function abrirArtigo(titulo, conteudoMarkdown, atualizarHash = true) {
    rolarAoTopo();
    divResultados.classList.add("escondido");
    leitorDeDisciplina.classList.add("escondido");
    document.getElementById("orientacoes-iniciais")?.classList.add("escondido");
    document.getElementById("explorar-disciplinas")?.classList.add("escondido");

    artigoAtual = todosOsArtigos.find(a => a.titulo === titulo && a.conteudo === conteudoMarkdown) ||
                  todosOsArtigos.find(a => a.titulo === titulo) || {
                      titulo: titulo,
                      path: `./${titulo}.md`,
                      categoria: "00. Geral",
                      conteudo: conteudoMarkdown
                  };

    artigoTitulo.textContent = artigoAtual.titulo;

    if (atualizarHash) {
        const rotaHash = rotaDoArtigo(artigoAtual);
        if (window.location.hash !== rotaHash) {
            history.pushState({ path: artigoAtual.path, titulo: artigoAtual.titulo }, artigoAtual.titulo, rotaHash);
        }
    }

    renderizarBreadcrumbs(artigoAtual);
    renderizarBotoesNavegacao(artigoAtual);
    processarContextoArtigo(conteudoMarkdown);

    btnVoltar.textContent = `← voltar para ${limparNomeCategoria(artigoAtual.categoria)}`;
    btnVoltar.setAttribute("aria-label", `Voltar para ${limparNomeCategoria(artigoAtual.categoria)}`);
    if (retornoArtigoTexto) {
        retornoArtigoTexto.innerHTML = `terminou este artigo? <strong>continue pelas outras notas de ${limparNomeCategoria(artigoAtual.categoria)}.</strong>`;
    }

    const markdownSemFrontmatter = removerFrontmatter(conteudoMarkdown);
    const markdownLimpo = removerContextoDoCorpo(removerPrimeiroH1(markdownSemFrontmatter));
    const indiceGlossario = extrairIndiceGlossario(markdownLimpo);
    const markdownParaRenderizar = indiceGlossario ? indiceGlossario.markdown : markdownLimpo;

    const blocosCodigo = [];
    const markdownSemCodigo = markdownParaRenderizar.replace(/(```[\s\S]*?```|`[^`\n]+`)/g, (match) => {
        blocosCodigo.push(match);
        return `@@CODE_BLOCK_${blocosCodigo.length - 1}@@`;
    });

    const markdownComHighlight = markdownSemCodigo.replace(/==([^=]+)==/g, '<mark class="obsidian-highlight">$1</mark>');

    const markdownComCodigoRestaurado = markdownComHighlight.replace(/@@CODE_BLOCK_(\d+)@@/g, (match, index) => {
        return blocosCodigo[parseInt(index, 10)] || match;
    });

    const markdownComSetas = processarLaTeXSetas(markdownComCodigoRestaurado);
    const markdownProtegido = protegerPipesObsidian(markdownComSetas);
    const markdownNormalizado = normalizarListasObsidian(markdownProtegido);

    if (typeof marked !== 'undefined') {
        artigoCorpo.innerHTML = marked.parse(markdownNormalizado);
    } else {
        artigoCorpo.innerText = markdownNormalizado;
    }

    processarLinksObsidian();
    processarCalloutsObsidian();
    renderizarNavegacaoGlossario(indiceGlossario?.grupos);

    artigoCorpo.querySelectorAll('li input[type="checkbox"]').forEach(checkbox => {
        const li = checkbox.parentElement;
        if (li) {
            li.classList.add('task-list-item');
            const textNodes = Array.from(li.childNodes).filter(node => node !== checkbox);
            const wrapper = document.createElement('span');
            wrapper.className = 'task-item-content';
            textNodes.forEach(node => wrapper.appendChild(node));
            li.appendChild(wrapper);
        }
    });

    if (typeof mermaid !== 'undefined') {
        const blocosMermaid = artigoCorpo.querySelectorAll('pre code.language-mermaid, pre.language-mermaid');
        blocosMermaid.forEach((bloco) => {
            const containerPre = bloco.tagName.toLowerCase() === 'pre' ? bloco : bloco.parentElement;
            const codigoMermaid = bloco.textContent;
            const divMermaid = document.createElement('div');
            divMermaid.className = 'mermaid';
            divMermaid.dataset.mermaidSource = codigoMermaid;
            divMermaid.textContent = codigoMermaid;
            containerPre.replaceWith(divMermaid);
        });
        setTimeout(renderizarDiagramasMermaid, 50);
    }

    if (typeof renderMathInElement !== 'undefined') {
        try {
            renderMathInElement(artigoCorpo, {
                delimiters: [
                    { left: '$$', right: '$$', display: true },
                    { left: '$', right: '$', display: false },
                    { left: '\\(', right: '\\)', display: false },
                    { left: '\\[', right: '\\]', display: true }
                ],
                throwOnError: false,
                ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
            });
        } catch (eMath) {
            console.warn("Erro ao renderizar KaTeX:", eMath);
        }
    }

    configurarCopiaDeCodigo();
    configurarZoomImagens();
    gerarTableOfContents();

    leitorDeArtigo.classList.remove("escondido");

    rolarAoTopo();
    requestAnimationFrame(() => rolarAoTopo());
    setTimeout(rolarAoTopo, 50);
    setTimeout(rolarAoTopo, 150);
}

function processarContextoArtigo(conteudoMarkdown) {
    const contextoEl = document.getElementById("artigo-contexto");
    if (!contextoEl) return;

    const matchContexto = conteudoMarkdown.match(/^>\s*\*\*Contexto:\*\*\s*([^\n\r]+(?:\n>[^\n\r]+)*)/m) ||
                          conteudoMarkdown.match(/^>\s*([^\n\r]+(?:\n>[^\n\r]+)*)/m);

    if (matchContexto && matchContexto[1]) {
        const textoContexto = matchContexto[1].replace(/\n>/g, ' ').replace(/\*\*/g, '').trim();
        const textoLimpo = textoContexto.replace(/\[\[(?:[^|\]]*\|)?([^\]]+)\]\]/g, '$1');
        contextoEl.innerHTML = `
            <div class="contexto-icone">
                <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">
                    <circle cx="12" cy="12" r="8"></circle>
                    <path d="m14.8 9.2-2.1 4.3-4.3 2.1 2.1-4.3z"></path>
                </svg>
            </div>
            <p><strong>Contexto:</strong> ${textoLimpo}</p>
        `;
        contextoEl.hidden = false;
    } else {
        contextoEl.innerHTML = "";
        contextoEl.hidden = true;
    }
}

function configurarZoomImagens() {
    const imagens = artigoCorpo.querySelectorAll('img');
    imagens.forEach(img => {
        img.addEventListener('click', () => {
            const modalExistente = document.querySelector('.imagem-modal');
            if (modalExistente) modalExistente.remove();

            const modal = document.createElement('div');
            modal.className = 'imagem-modal';
            modal.innerHTML = `
                <button class="imagem-modal-fechar" aria-label="Fechar">&times;</button>
                <img src="${img.src}" alt="${img.alt || 'Imagem ampliada'}">
            `;

            modal.addEventListener('click', (e) => {
                if (e.target === modal || e.target.classList.contains('imagem-modal-fechar')) {
                    modal.remove();
                }
            });

            document.body.appendChild(modal);
        });
    });
}

function configurarCopiaDeCodigo() {
    const inlineCodes = artigoCorpo.querySelectorAll('code');
    inlineCodes.forEach(code => {
        if (code.closest('pre')) return;

        code.setAttribute('title', 'clique para copiar');
        code.classList.add('code-copiavel');

        code.addEventListener('click', async (e) => {
            e.stopPropagation();
            const texto = code.innerText.trim();
            if (!texto) return;

            try {
                if (navigator.clipboard && window.isSecureContext) {
                    await navigator.clipboard.writeText(texto);
                } else {
                    const textArea = document.createElement('textarea');
                    textArea.value = texto;
                    textArea.style.position = 'fixed';
                    textArea.style.opacity = '0';
                    document.body.appendChild(textArea);
                    textArea.focus();
                    textArea.select();
                    document.execCommand('copy');
                    document.body.removeChild(textArea);
                }

                code.classList.add('code-copiado');
                setTimeout(() => {
                    code.classList.remove('code-copiado');
                }, 1400);
            } catch (err) {
                console.error('Falha ao copiar texto do code:', err);
            }
        });
    });

    const blocosPre = artigoCorpo.querySelectorAll('pre');
    blocosPre.forEach(pre => {
        if (pre.classList.contains('mermaid') || pre.querySelector('.btn-copiar-codigo')) return;

        const btnCopiar = document.createElement('button');
        btnCopiar.className = 'btn-copiar-codigo';
        btnCopiar.type = 'button';
        btnCopiar.setAttribute('aria-label', 'copiar código');
        btnCopiar.textContent = 'copiar';

        btnCopiar.addEventListener('click', async (e) => {
            e.stopPropagation();
            const codeEl = pre.querySelector('code');
            const textoParaCopiar = (codeEl ? codeEl.innerText : pre.innerText).replace(/copiar|copiado!/g, '').trim();

            try {
                if (navigator.clipboard && window.isSecureContext) {
                    await navigator.clipboard.writeText(textoParaCopiar);
                } else {
                    const textArea = document.createElement('textarea');
                    textArea.value = textoParaCopiar;
                    textArea.style.position = 'fixed';
                    textArea.style.opacity = '0';
                    document.body.appendChild(textArea);
                    textArea.focus();
                    textArea.select();
                    document.execCommand('copy');
                    document.body.removeChild(textArea);
                }

                btnCopiar.textContent = 'copiado!';
                btnCopiar.classList.add('copiado');
                setTimeout(() => {
                    btnCopiar.textContent = 'copiar';
                    btnCopiar.classList.remove('copiado');
                }, 2000);
            } catch (err) {
                console.error('Falha ao copiar código:', err);
                btnCopiar.textContent = 'erro';
                setTimeout(() => {
                    btnCopiar.textContent = 'copiar';
                }, 2000);
            }
        });

        pre.appendChild(btnCopiar);
    });
}

function rolarAoTopo() {
    window.scrollTo(0, 0);
    window.scrollTo({ top: 0, left: 0, behavior: "instant" });
    document.documentElement.scrollTop = 0;
    document.body.scrollTop = 0;
}

// Table of Contents (TOC) com Scrollspy e Filtro em Tempo Real
let scrollSpyObserver = null;
let headingsTOC = [];

function gerarTableOfContents() {
    const tocNavDesktop = document.getElementById("toc-nav");
    const tocSidebar = document.getElementById("artigo-toc-sidebar");

    if (!tocNavDesktop) return;

    tocNavDesktop.innerHTML = "";

    const headings = Array.from(artigoCorpo.querySelectorAll("h2"));

    if (headings.length === 0) {
        if (tocSidebar) tocSidebar.style.display = "none";
        return;
    }

    if (tocSidebar) tocSidebar.style.display = "block";

    const listaDesktop = document.createElement("ul");
    listaDesktop.className = "toc-list";

    headings.forEach((heading, index) => {
        if (!heading.id) {
            heading.id = `heading-toc-${index}`;
        }

        const liDesktop = document.createElement("li");
        liDesktop.className = "toc-item";
        const linkDesktop = document.createElement("a");
        linkDesktop.textContent = heading.textContent.toLowerCase();
        linkDesktop.href = `#${heading.id}`;
        linkDesktop.setAttribute("data-target", heading.id);

        linkDesktop.addEventListener("click", (e) => {
            e.preventDefault();
            scrollParaHeading(heading);
        });

        liDesktop.appendChild(linkDesktop);
        listaDesktop.appendChild(liDesktop);
    });

    tocNavDesktop.appendChild(listaDesktop);

    const tocFilterInput = document.getElementById("toc-filter-input");
    if (tocFilterInput) {
        tocFilterInput.value = "";
        tocFilterInput.oninput = (e) => {
            const query = e.target.value.toLowerCase().trim();
            const items = listaDesktop.querySelectorAll(".toc-item");
            items.forEach(item => {
                const link = item.querySelector("a");
                if (!link) return;
                const match = link.textContent.toLowerCase().includes(query);
                item.style.display = match ? "block" : "none";
            });
        };
    }

    inicializarScrollspyTOC(headings);
}

function inicializarScrollspyTOC(headings) {
    if (scrollSpyObserver) {
        scrollSpyObserver.disconnect();
    }

    headingsTOC = headings;

    scrollSpyObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.id;
                const links = document.querySelectorAll(`.toc-list a[data-target="${id}"]`);
                document.querySelectorAll(".toc-list a").forEach(a => a.classList.remove("toc-active"));
                links.forEach(a => a.classList.add("toc-active"));
            }
        });
    }, {
        rootMargin: "-80px 0px -70% 0px",
        threshold: 0.1
    });

    headings.forEach(heading => scrollSpyObserver.observe(heading));
}

function extrairNomeLimpo(nomeComPrefixo) {
    if (!nomeComPrefixo) return "";
    return nomeComPrefixo.replace(/^\d+\s*[-.]\s*/, "").replace(/\.md$/i, "").trim();
}

function obterRotaArtigo(artigo) {
    if (!artigo) return "#";
    return rotaDoArtigo(artigo);
}

function obterHrefParaLinkObsidian(destino) {
    if (!destino) return "#";
    if (destino.startsWith("#")) return destino;

    const [nomeArtigo, hashSecao] = destino.split("#");
    const artigo = buscarArtigoPorCaminho(nomeArtigo.trim());
    if (artigo) {
        const rotaBase = obterRotaArtigo(artigo);
        return hashSecao ? `${rotaBase}#${encodeURIComponent(hashSecao.trim())}` : rotaBase;
    }
    return "#";
}

function renderizarBotoesNavegacao(artigoAtual) {
    const rodapeNavContainer = document.getElementById("artigo-nav-rodape");
    if (!rodapeNavContainer) return;

    rodapeNavContainer.innerHTML = "";

    const artigosDaCategoria = todasAsPastas[artigoAtual.categoria] || [];
    if (artigosDaCategoria.length <= 1) return;

    const indiceAtual = artigosDaCategoria.findIndex(a => a.titulo === artigoAtual.titulo);
    if (indiceAtual === -1) return;

    const artigoAnterior = indiceAtual > 0 ? artigosDaCategoria[indiceAtual - 1] : null;
    const artigoProximo = indiceAtual < artigosDaCategoria.length - 1 ? artigosDaCategoria[indiceAtual + 1] : null;

    if (!artigoAnterior && !artigoProximo) return;

    const grid = document.createElement("div");
    grid.className = "artigo-nav-cards-grid";

    if (artigoAnterior) {
        const cardPrev = document.createElement("a");
        cardPrev.className = "nav-card nav-card-prev";
        cardPrev.href = obterRotaArtigo(artigoAnterior);
        cardPrev.innerHTML = `
            <span class="nav-card-label">← anterior</span>
            <span class="nav-card-title">${artigoAnterior.titulo}</span>
        `;
        cardPrev.addEventListener("click", (e) => {
            if (e.metaKey || e.ctrlKey || e.shiftKey || e.button === 1) return;
            e.preventDefault();
            abrirArtigo(artigoAnterior.titulo, artigoAnterior.conteudo);
        });
        grid.appendChild(cardPrev);
    } else {
        const placeholder = document.createElement("div");
        placeholder.className = "nav-card nav-card-placeholder";
        grid.appendChild(placeholder);
    }

    if (artigoProximo) {
        const cardNext = document.createElement("a");
        cardNext.className = "nav-card nav-card-next";
        cardNext.href = obterRotaArtigo(artigoProximo);
        cardNext.innerHTML = `
            <span class="nav-card-label">próximo →</span>
            <span class="nav-card-title">${artigoProximo.titulo}</span>
        `;
        cardNext.addEventListener("click", (e) => {
            if (e.metaKey || e.ctrlKey || e.shiftKey || e.button === 1) return;
            e.preventDefault();
            abrirArtigo(artigoProximo.titulo, artigoProximo.conteudo);
        });
        grid.appendChild(cardNext);
    } else {
        const placeholder = document.createElement("div");
        placeholder.className = "nav-card nav-card-placeholder";
        grid.appendChild(placeholder);
    }

    rodapeNavContainer.appendChild(grid);
}

function processarCalloutsObsidian() {
    const blockquotes = artigoCorpo.querySelectorAll('blockquote');
    blockquotes.forEach(bq => {
        const conteudo = bq.innerHTML;
        const match = conteudo.match(/\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\](?:[ \t]+([^\n<]+))?/i);
        if (match) {
            const tipo = match[1].toUpperCase();
            const tituloCustomizado = match[2] ? match[2].trim() : '';
            
            let htmlLimpo = conteudo.replace(/\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\](?:[ \t]+[^\n<]+)?/i, '');
            htmlLimpo = htmlLimpo.replace(/<p>\s*<\/p>/g, '');

            const rotulos = {
                'NOTE': 'NOTA',
                'TIP': 'DICA',
                'IMPORTANT': 'IMPORTANTE',
                'WARNING': 'AVISO',
                'CAUTION': 'ATENÇÃO'
            };

            const tituloExibicao = tituloCustomizado || rotulos[tipo] || tipo;

            const divCallout = document.createElement('div');
            divCallout.className = `obsidian-callout callout-${tipo.toLowerCase()}`;

            divCallout.innerHTML = `
                <div class="callout-header">
                    <span class="callout-title">${tituloExibicao}</span>
                </div>
                <div class="callout-content">
                    ${htmlLimpo}
                </div>
            `;

            bq.replaceWith(divCallout);
        }
    });
}

function renderizarBreadcrumbs(artigo) {
    const breadcrumbsNav = document.getElementById("artigo-breadcrumbs");
    if (!breadcrumbsNav) return;

    breadcrumbsNav.innerHTML = "";

    const linkHome = document.createElement("a");
    linkHome.className = "breadcrumb-link";
    linkHome.href = "#";
    linkHome.textContent = "início";
    linkHome.addEventListener("click", (e) => {
        if (e.metaKey || e.ctrlKey || e.shiftKey || e.button === 1) return;
        e.preventDefault();
        voltarParaHome(true);
    });

    const separador1 = document.createElement("span");
    separador1.className = "breadcrumb-separator";
    separador1.textContent = "/";

    const linkCategoria = document.createElement("a");
    linkCategoria.className = "breadcrumb-link";
    linkCategoria.href = obterRotaCategoria(artigo.categoria);
    linkCategoria.textContent = limparNomeCategoria(artigo.categoria);
    linkCategoria.addEventListener("click", (e) => {
        if (e.metaKey || e.ctrlKey || e.shiftKey || e.button === 1) return;
        e.preventDefault();
        abrirDisciplina(artigo.categoria);
    });

    const separador2 = document.createElement("span");
    separador2.className = "breadcrumb-separator";
    separador2.textContent = "/";

    const spanArtigo = document.createElement("span");
    spanArtigo.textContent = artigo.titulo;

    breadcrumbsNav.append(linkHome, separador1, linkCategoria, separador2, spanArtigo);
}

function scrollParaHeading(idOuTexto) {
    if (!idOuTexto) return;
    
    // Se for um elemento DOM direto
    if (idOuTexto instanceof HTMLElement) {
        const stickyNav = document.getElementById("sticky-nav");
        const offset = (stickyNav ? stickyNav.offsetHeight : 60) + 20;
        const elementPosition = idOuTexto.getBoundingClientRect().top + window.scrollY;
        window.scrollTo({
            top: Math.max(0, elementPosition - offset),
            behavior: "smooth"
        });
        return;
    }

    const decodificado = decodeURIComponent(idOuTexto).trim();

    const normalizar = (s) => (s || "").toLowerCase()
        .normalize("NFD").replace(/[\u0300-\u036f]/g, "")
        .replace(/[^\w\s-]/g, "")
        .replace(/\s+/g, " ")
        .trim();

    const slug = normalizar(decodificado).replace(/\s+/g, "-");
    const termoLimpo = normalizar(decodificado);

    const matchNumero = decodificado.match(/^(\d+)\./);
    const numeroItem = matchNumero ? matchNumero[1] : null;
    
    let el = document.getElementById(decodificado) || 
             document.getElementById(idOuTexto) || 
             document.getElementById(slug);
    
    if (!el && artigoCorpo) {
        const headings = Array.from(artigoCorpo.querySelectorAll("h1, h2, h3, h4, h5, h6"));
        
        el = headings.find(h => {
            const hNorm = normalizar(h.textContent);
            const hSlug = hNorm.replace(/\s+/g, "-");
            const hId = h.id ? h.id.toLowerCase() : "";
            return h.id === decodificado || h.id === slug || hId === slug || hNorm === termoLimpo || hSlug === slug;
        });

        if (!el && numeroItem) {
            el = headings.find(h => {
                const texto = h.textContent.trim();
                return texto.startsWith(`${numeroItem}.`) || texto.startsWith(`${numeroItem} `) || h.id.startsWith(`${numeroItem}-`);
            });
        }

        if (!el) {
            el = headings.find(h => {
                const hNorm = normalizar(h.textContent);
                return (termoLimpo.length > 4 && hNorm.includes(termoLimpo)) || (hNorm.length > 4 && termoLimpo.includes(hNorm));
            });
        }
    }

    if (el) {
        const stickyNav = document.getElementById("sticky-nav");
        const offset = (stickyNav ? stickyNav.offsetHeight : 60) + 20;
        const elementPosition = el.getBoundingClientRect().top + window.scrollY;
        window.scrollTo({
            top: Math.max(0, elementPosition - offset),
            behavior: "smooth"
        });
    }
}

function navegarParaLinkObsidian(destino, atualizarHash = true) {
    if (!destino) return;

    if (destino.startsWith("#")) {
        const secaoTexto = destino.substring(1).trim();
        scrollParaHeading(secaoTexto);
        return;
    }

    const [nomeArtigo, hashSecao] = destino.split("#");
    const encontrado = buscarArtigoPorCaminho(nomeArtigo.trim());

    if (encontrado) {
        abrirArtigo(encontrado.titulo, encontrado.conteudo, atualizarHash);
        if (hashSecao) {
            setTimeout(() => {
                scrollParaHeading(hashSecao.trim());
            }, 250);
            setTimeout(() => {
                scrollParaHeading(hashSecao.trim());
            }, 500);
        }
    }
}

function buscarArtigoPorCaminho(nomeOuCaminho) {
    if (!nomeOuCaminho) return null;
    
    const normalizar = (str) => decodeURIComponent(decodeURI(str))
        .replace(/^\.\//, "")
        .trim()
        .toLowerCase()
        .normalize("NFD").replace(/[\u0300-\u036f]/g, "") // Remove acentos
        .replace(/\.md$/i, "")
        .replace(/[(),:;+]/g, " ")
        .replace(/\s+/g, " ")
        .trim();

    const limpo = normalizar(nomeOuCaminho);
    const limpoApenasNome = limpo.split("/").pop().trim();

    return todosOsArtigos.find(a => {
        const caminhoSemExtensao = normalizar(a.sourcePath || a.path);
        const nomeArquivo = normalizar((a.sourcePath || a.path).split("/").pop());
        const tituloNorm = normalizar(a.titulo);

        return caminhoSemExtensao === limpo ||
               nomeArquivo === limpo ||
               nomeArquivo === limpoApenasNome ||
               tituloNorm === limpo ||
               tituloNorm === limpoApenasNome;
    }) || todosOsArtigos.find(a => {
        const nomeArquivo = normalizar((a.sourcePath || a.path).split("/").pop());
        const tituloNorm = normalizar(a.titulo);
        return (limpoApenasNome.length > 3 && (nomeArquivo.includes(limpoApenasNome) || limpoApenasNome.includes(nomeArquivo) || tituloNorm.includes(limpoApenasNome)));
    }) || null;
}

function obterHrefParaLinkObsidian(destino) {
    if (!destino) return "#";
    if (destino.startsWith("#")) return destino;

    const [nomeArtigo, hashSecao] = destino.split("#");
    const artigo = buscarArtigoPorCaminho(nomeArtigo.trim());
    if (artigo) {
        const rotaBase = rotaDoArtigo(artigo);
        return hashSecao ? `${rotaBase}#${encodeURIComponent(hashSecao.trim())}` : rotaBase;
    }
    return "#";
}

function processarLinksObsidian() {
    const htmlAtual = artigoCorpo.innerHTML;
    // Regex flexível que aceita tanto %%OBSIDIANPIPE%% quanto pipes puros |
    const regexObsidian = /\[\[([^\n\]]+)\]\]/g;

    artigoCorpo.innerHTML = htmlAtual.replace(regexObsidian, (match, conteudoBruto) => {
        let conteudo = conteudoBruto
            .replace(/<[^>]+>OBSIDIAN_PIPE<[^>]+>/g, "%%OBSIDIANPIPE%%")
            .replace(/___OBSIDIAN_PIPE___/g, "%%OBSIDIANPIPE%%");

        let caminho = "";
        let textoExibicao = "";

        if (conteudo.includes("%%OBSIDIANPIPE%%")) {
            const partes = conteudo.split("%%OBSIDIANPIPE%%");
            caminho = partes[0].trim();
            textoExibicao = partes[1].trim();
        } else if (conteudo.includes("|")) {
            const partes = conteudo.split("|");
            caminho = partes[0].trim();
            textoExibicao = partes[1].trim();
        } else {
            caminho = conteudo.trim();
            textoExibicao = conteudo.trim();
        }

        caminho = caminho.replace(/<[^>]+>/g, "").trim();
        const href = obterHrefParaLinkObsidian(caminho);

        return `<a href="${href}" class="obsidian-link" data-destino="${caminho}">${textoExibicao}</a>`;
    });

    artigoCorpo.querySelectorAll(".obsidian-link").forEach(link => {
        link.addEventListener("click", (e) => {
            if (e.metaKey || e.ctrlKey || e.shiftKey || e.button === 1) return;
            e.preventDefault();
            const destino = link.getAttribute("data-destino");
            navegarParaLinkObsidian(destino);
        });
    });
}

function voltarParaHome(atualizarHash = true) {
    leitorDeArtigo.classList.add("escondido");
    leitorDeDisciplina.classList.add("escondido");
    divResultados.classList.add("escondido");
    document.getElementById("orientacoes-iniciais")?.classList.remove("escondido");
    document.getElementById("explorar-disciplinas")?.classList.remove("escondido");

    if (campoTexto) campoTexto.value = "";
    containerResultados.innerHTML = "";

    if (atualizarHash && window.location.hash) {
        history.pushState(null, "", window.location.pathname);
    }

    window.scrollTo({ top: 0, behavior: "smooth" });
}

// Event Listeners
if (campoTexto) {
    campoTexto.addEventListener("input", (e) => {
        filtrarArtigos(e.target.value);
    });
}

if (btnVoltar) {
    btnVoltar.addEventListener("click", () => {
        if (artigoAtual && artigoAtual.categoria) {
            abrirDisciplina(artigoAtual.categoria, true);
        } else {
            voltarParaHome(true);
        }
    });
}

if (btnVoltarDisciplina) {
    btnVoltarDisciplina.addEventListener("click", () => voltarParaHome(true));
}

const stickyNav = document.getElementById("sticky-nav");
window.addEventListener("scroll", () => {
    if (!stickyNav) return;
    if (window.scrollY > 80) {
        stickyNav.classList.add("visible");
    } else {
        stickyNav.classList.remove("visible");
    }
});

const navLogo = document.getElementById("nav-logo");
if (navLogo) {
    navLogo.addEventListener("click", () => voltarParaHome(true));
}

const mainTitle = document.getElementById("home-title");
if (mainTitle) {
    mainTitle.addEventListener("click", () => voltarParaHome(true));
}

const navLinkPastas = document.getElementById("nav-link-pastas");
if (navLinkPastas) {
    navLinkPastas.addEventListener("click", (e) => {
        e.preventDefault();
        voltarParaHome(true);
        const pastasContainer = document.getElementById("explorar-disciplinas");
        if (pastasContainer) {
            pastasContainer.scrollIntoView({ behavior: "smooth", block: "start" });
        }
    });
}

// Tratamento de Rotas no Hash
function tratarHashNavegacao() {
    const hash = window.location.hash;
    if (!hash || hash === "#" || hash === "#/") {
        voltarParaHome(false);
        return;
    }

    const rotaLimpa = decodeURIComponent(hash.replace(/^#\/?/, "").trim());
    
    if (rotaLimpa.startsWith("disciplina/")) {
        const categoria = rotaLimpa.replace("disciplina/", "").trim();
        abrirDisciplina(categoria, false);
        return;
    }

    const partes = rotaLimpa.split("/");
    if (partes.length >= 2) {
        const [categoria, ...resto] = partes;
        const nomeArtigo = resto.join("/");
        const artigo = todosOsArtigos.find(a => 
            a.categoria.toLowerCase() === categoria.toLowerCase() && 
            a.titulo.toLowerCase() === nomeArtigo.toLowerCase()
        );
        if (artigo) {
            abrirArtigo(artigo.titulo, artigo.conteudo, false);
            return;
        }
    }

    navegarParaLinkObsidian(rotaLimpa, false);
}

window.addEventListener("popstate", () => {
    tratarHashNavegacao();
});

// Inicialização
carregarTodosOsArtigos();
