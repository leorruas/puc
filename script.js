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
                const pathCodificado = item.path.split("/").map(seg => encodeURIComponent(seg)).join("/");
                return {
                    titulo: nomeSemExtensao,
                    path: `./${pathCodificado}`
                };
            });
    } catch (erro) {
        console.warn("Não foi possível listar via GitHub, usando lista padrão completa:", erro);
        // Fallback local completo com todos os arquivos do vault puc
        const arquivosFallback = [
            "00. Geral/Aula Inaugural - Resumo.md",
            "00. Geral/Aula Inaugural - Transcrição.md",
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
            "06. Projeto - Aplicacao Interativa/06. Projeto - Aplicacao Interativa - Resumo.md",
            "06. Projeto - Aplicacao Interativa/01. Ods 4 educação de qualidade - conceito, metas e fundamentação.md",
            "06. Projeto - Aplicacao Interativa/02. Requisitos e diretrizes de escopo do projeto.md",
            "06. Projeto - Aplicacao Interativa/03. Cronograma semanal e entregas de etapas.md",
            "06. Projeto - Aplicacao Interativa/04. Reunião inicial da turma 5 - resumo e transcrição integral.md",
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
            const pathCodificado = p.split("/").map(seg => encodeURIComponent(seg)).join("/");
            return {
                titulo: nomeSemExtensao,
                path: `./${pathCodificado}`
            };
        });
    }
}

// Variáveis globais
let todosOsArtigos = [];
let todasAsPastas = {};

const campoTexto = document.getElementById("main-search-input");
const campoTextoNav = document.getElementById("nav-search-input");
const btnPesquisar = document.querySelector("main button");
const containerResultados = document.querySelector(".cards-container");
const divResultados = document.querySelector(".resultados");
const leitorDeArtigo = document.getElementById("leitor-artigo");
const artigoTitulo = document.getElementById("artigo-titulo");
const artigoCorpo = document.getElementById("artigo-corpo");
const btnVoltar = document.getElementById("btn-voltar");

// Carrega os arquivos e busca o conteúdo de cada um
async function carregarTodosOsArtigos() {
    const lista = await obterListaDeArquivos();

    // Promessas paralelas para ler o conteúdo Markdown de cada arquivo
    const promessas = lista.map(async (item) => {
        try {
            const res = await fetch(item.path);
            if (!res.ok) return null;
            const texto = await res.text();
            
            // Extrai pasta/categoria se houver subpasta
            const caminhoDecodificado = decodeURI(item.path);
            const partes = caminhoDecodificado.replace("./", "").split("/");
            const categoria = partes.length > 1 ? partes[0] : "Geral";

            return {
                titulo: item.titulo,
                path: item.path,
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

    // Organiza artigos em estrutura de pasta para o accordion
    todasAsPastas = {};
    todosOsArtigos.forEach(artigo => {
        if (!todasAsPastas[artigo.categoria]) {
            todasAsPastas[artigo.categoria] = [];
        }
        todasAsPastas[artigo.categoria].push(artigo);
    });

    // Ordena os artigos dentro de cada pasta pelo nome e número
    Object.keys(todasAsPastas).forEach(cat => {
        todasAsPastas[cat].sort((a, b) => {
            return a.path.localeCompare(b.path, undefined, { numeric: true, sensitivity: 'base' });
        });
    });

    // Renderiza a estrutura de pastas na página inicial
    renderizarPastas();

    // Se a página for carregada com uma rota no Hash da URL, abre o artigo correspondente
    if (window.location.hash) {
        tratarHashNavegacao();
    }
}

function filtrarArtigos(termoBusca) {
    if (!termoBusca || termoBusca.trim() === "") {
        containerResultados.innerHTML = "";
        const pastasContainer = document.getElementById("pastas-container");
        if (pastasContainer) pastasContainer.classList.remove("escondido");
        return;
    }

    const termo = termoBusca.toLowerCase().trim();
    
    // Oculta container de pastas ao fazer busca
    const pastasContainer = document.getElementById("pastas-container");
    if (pastasContainer) pastasContainer.classList.add("escondido");

    const filtrados = todosOsArtigos.filter(artigo => {
        const tituloMatch = artigo.titulo.toLowerCase().includes(termo);
        const conteudoMatch = artigo.conteudo.toLowerCase().includes(termo);
        return tituloMatch || conteudoMatch;
    });

    exibirResultados(filtrados, termo);
}

function destacarTexto(texto, termo) {
    if (!termo) return texto;
    const regex = new RegExp(`(${termo.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'gi');
    return texto.replace(regex, '<mark class="highlight">$1</mark>');
}

function removerFrontmatter(markdown) {
    if (!markdown) return "";
    // Remove cabeçalho YAML entre --- e --- no início do arquivo
    return markdown.replace(/^---[\s\S]*?---\s*/, "");
}

function removerPrimeiroH1(markdown) {
    if (!markdown) return "";
    // Remove o primeiro título H1 (# Título...) se houver, para evitar duplicação com o título do leitor
    return markdown.replace(/^\s*#\s+[^\n]+(?:\r?\n)*/, "");
}

function processarLaTeXSetas(markdown) {
    if (!markdown) return "";
    return markdown
        .replace(/\$\s*\\rightarrow\s*\$/g, "→")
        .replace(/\$\s*\\leftarrow\s*\$/g, "←")
        .replace(/\$\s*\\leftrightarrow\s*\$/g, "↔")
        .replace(/\$\s*\\Rightarrow\s*\$/g, "⇒")
        .replace(/\$\s*\\Leftarrow\s*\$/g, "⇐")
        .replace(/\$\s*\\Leftrightarrow\s*\$/g, "⇔")
        .replace(/\\rightarrow/g, "→")
        .replace(/\\leftarrow/g, "←")
        .replace(/\\leftrightarrow/g, "↔")
        .replace(/\\Rightarrow/g, "⇒")
        .replace(/\\Leftarrow/g, "⇐")
        .replace(/\\Leftrightarrow/g, "⇔")
        .replace(/\$\s*→\s*\$/g, "→")
        .replace(/\$\s*←\s*\$/g, "←")
        .replace(/\$\s*↔\s*\$/g, "↔")
        .replace(/\$\s*⇒\s*\$/g, "⇒")
        .replace(/\$\s*⇐\s*\$/g, "⇐")
        .replace(/\$\s*⇔\s*\$/g, "⇔");
}

function extrairTrechoRelevante(conteudo, termo) {
    const conteudoSemFrontmatter = removerFrontmatter(conteudo);
    const textoLimpo = conteudoSemFrontmatter.replace(/==/g, '').replace(/[#*`_~\[\]]/g, ' ');
    const pos = textoLimpo.toLowerCase().indexOf(termo.toLowerCase());
    
    if (pos === -1) {
        return textoLimpo.substring(0, 150) + "...";
    }

    const inicio = Math.max(0, pos - 40);
    const fim = Math.min(textoLimpo.length, pos + 110);
    let trecho = textoLimpo.substring(inicio, fim);
    
    if (inicio > 0) trecho = "..." + trecho;
    if (fim < textoLimpo.length) trecho = trecho + "...";
    
    return trecho;
}

function exibirResultados(artigos, termo = "") {
    containerResultados.innerHTML = "";
    leitorDeArtigo.classList.add("escondido");
    divResultados.classList.remove("escondido");

    if (artigos.length === 0) {
        containerResultados.innerHTML = "<p class='sem-resultados'>Nenhum resultado encontrado.</p>";
        return;
    }

    // Agrupa resultados por categoria (pasta)
    const grupos = {};
    artigos.forEach(artigo => {
        if (!grupos[artigo.categoria]) grupos[artigo.categoria] = [];
        grupos[artigo.categoria].push(artigo);
    });

    Object.keys(grupos).sort().forEach(categoria => {
        const grupoDiv = document.createElement("div");
        grupoDiv.className = "busca-grupo-assunto";

        const tituloGrupo = document.createElement("h3");
        tituloGrupo.className = "busca-assunto-titulo";
        tituloGrupo.textContent = categoria;
        grupoDiv.appendChild(tituloGrupo);

        const subCardsContainer = document.createElement("div");
        subCardsContainer.className = "cards-container";

        grupos[categoria].forEach(artigo => {
            const card = document.createElement("div");
            card.className = "card";

            const tag = document.createElement("span");
            tag.className = "card-tag";
            tag.textContent = artigo.categoria;

            const h2 = document.createElement("h2");
            h2.innerHTML = destacarTexto(artigo.titulo, termo);

            const p = document.createElement("p");
            p.className = "conteudo";
            const trecho = extrairTrechoRelevante(artigo.conteudo, termo);
            p.innerHTML = destacarTexto(trecho, termo);

            card.appendChild(tag);
            card.appendChild(h2);
            card.appendChild(p);

            card.addEventListener("click", () => {
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

function abrirArtigo(titulo, conteudoMarkdown, atualizarHash = true) {
    rolarAoTopo();
    divResultados.classList.add("escondido");
    const pastasContainer = document.getElementById("pastas-container");
    if (pastasContainer) pastasContainer.classList.add("escondido");

    artigoTitulo.textContent = titulo;

    // Localiza os metadados do artigo na base carregada
    const artigoAtual = todosOsArtigos.find(a => a.titulo === titulo || a.conteudo === conteudoMarkdown) || {
        titulo: titulo,
        path: `./${titulo}.md`,
        categoria: "Geral",
        conteudo: conteudoMarkdown
    };

    // Atualiza a URL / Rota no navegador para permitir histórico e botões de voltar/avançar
    if (atualizarHash) {
        const rotaHash = "#/" + encodeURIComponent(artigoAtual.categoria) + "/" + encodeURIComponent(artigoAtual.titulo);
        if (window.location.hash !== rotaHash) {
            history.pushState({ path: artigoAtual.path, titulo: artigoAtual.titulo }, artigoAtual.titulo, rotaHash);
        }
    }

    // Renderiza a trilha de navegação (breadcrumbs) e a barra de botões sequenciais
    renderizarBreadcrumbs(artigoAtual);
    renderizarBotoesNavegacao(artigoAtual);
    
    // Filtra e remove o bloco de metadados/atributos (YAML Frontmatter) e o primeiro H1 duplicado
    const markdownSemFrontmatter = removerFrontmatter(conteudoMarkdown);
    const markdownLimpo = removerPrimeiroH1(markdownSemFrontmatter);

    // Protege blocos de código (``` e `) para não corromper divisores como // =====...===== com a regex de highlight ==texto==
    const blocosCodigo = [];
    const markdownSemCodigo = markdownLimpo.replace(/(```[\s\S]*?```|`[^`\n]+`)/g, (match) => {
        blocosCodigo.push(match);
        return `@@CODE_BLOCK_${blocosCodigo.length - 1}@@`;
    });

    // Converte a sintaxe de highlight do Obsidian ==texto== para <mark class="obsidian-highlight">texto</mark>
    const markdownComHighlight = markdownSemCodigo.replace(/==([^=]+)==/g, '<mark class="obsidian-highlight">$1</mark>');

    // Restaura os blocos de código intactos
    const markdownComCodigoRestaurado = markdownComHighlight.replace(/@@CODE_BLOCK_(\d+)@@/g, (match, index) => {
        return blocosCodigo[parseInt(index, 10)] || match;
    });

    // Converte notações LaTeX de setas (ex: $\rightarrow$, $\leftrightarrow$) para caracteres Unicode reais (→, ↔)
    const markdownComSetas = processarLaTeXSetas(markdownComCodigoRestaurado);

    // Protege caracteres '|' em links do Obsidian [[Link|Texto]] para não quebrarem tabelas no marked.parse
    const markdownProtegido = protegerPipesObsidian(markdownComSetas);

    // Normaliza identação de listas do Obsidian (1-3 espaços -> 4 espaços) para o marked.parse
    const markdownNormalizado = normalizarListasObsidian(markdownProtegido);

    // Converte Markdown para HTML com marked
    if (typeof marked !== 'undefined') {
        artigoCorpo.innerHTML = marked.parse(markdownNormalizado);
    } else {
        artigoCorpo.innerText = markdownNormalizado;
    }

    // Processa os links do Obsidian [[Nome do Artigo]] e restaura os pipes dos links
    processarLinksObsidian();

    // Processa callouts / caixas de aviso do Obsidian ([!IMPORTANT], [!NOTE], [!TIP], etc.)
    processarCalloutsObsidian();

    // Formata itens de lista de tarefas (Checkboxes / Study Roadmap)
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

    // Processa blocos Mermaid se houver
    if (typeof mermaid !== 'undefined') {
        mermaid.initialize({
            startOnLoad: false,
            theme: 'dark',
            fontFamily: 'Archivo, sans-serif',
            flowchart: {
                curve: 'linear',
                defaultRenderer: 'dagre-wrapper'
            },
            themeVariables: {
                fontFamily: 'Archivo, sans-serif',
                darkMode: true,
                background: '#0d0d0d',
                primaryColor: '#007aff',
                primaryTextColor: '#ffffff',
                primaryBorderColor: '#007aff',
                lineColor: '#007aff',
                secondaryColor: '#1a1a1a',
                tertiaryColor: '#222222'
            }
        });
        const blocosMermaid = artigoCorpo.querySelectorAll('pre code.language-mermaid, pre.language-mermaid');
        blocosMermaid.forEach((bloco, idx) => {
            const containerPre = bloco.tagName.toLowerCase() === 'pre' ? bloco : bloco.parentElement;
            const codigoMermaid = bloco.textContent;
            const divMermaid = document.createElement('div');
            divMermaid.className = 'mermaid';
            divMermaid.textContent = codigoMermaid;
            containerPre.replaceWith(divMermaid);
        });
        setTimeout(() => {
            try {
                mermaid.run({ nodes: artigoCorpo.querySelectorAll('.mermaid') });
            } catch (err) {
                console.error("Erro ao renderizar Mermaid:", err);
            }
        }, 50);
    }

    // Gera a Table of Contents (TOC) a partir dos cabeçalhos h2, h3, h4 do artigo
    gerarTableOfContents();

    leitorDeArtigo.classList.remove("escondido");
    
    // Atualiza visibilidade dos controles de TOC
    atualizarControlesTOC(true);

    // Garante que a transição reposicione a leitura no topo exato da tela (scroll 0, 0)
    rolarAoTopo();
    requestAnimationFrame(() => rolarAoTopo());
    setTimeout(rolarAoTopo, 50);
    setTimeout(rolarAoTopo, 150);
}

function rolarAoTopo() {
    window.scrollTo(0, 0);
    window.scrollTo({ top: 0, left: 0, behavior: "instant" });
    document.documentElement.scrollTop = 0;
    document.body.scrollTop = 0;
}

function gerarTableOfContents() {
    const tocNavDesktop = document.getElementById("toc-nav");
    const tocSidebar = document.getElementById("artigo-toc-sidebar");

    if (!tocNavDesktop) return;

    tocNavDesktop.innerHTML = "";

    // Pega exclusivamente os títulos principais (H2) do artigo
    const headings = artigoCorpo.querySelectorAll("h2");

    if (headings.length === 0) {
        if (tocSidebar) tocSidebar.style.display = "none";
        return;
    }

    if (tocSidebar) tocSidebar.style.display = "";

    const ulDesktop = document.createElement("ul");
    ulDesktop.className = "toc-list";

    headings.forEach((heading, index) => {
        // Cria um ID amigável se o elemento não possuir
        if (!heading.id) {
            const slug = heading.textContent
                .toLowerCase()
                .replace(/[^\w\s-]/g, "")
                .replace(/\s+/g, "-") || `secao-${index}`;
            heading.id = slug;
        }

        const texto = heading.textContent.trim();

        // Item Desktop
        const liDesktop = document.createElement("li");
        liDesktop.className = "toc-item";
        const aDesktop = document.createElement("a");
        aDesktop.href = `#${heading.id}`;
        aDesktop.textContent = texto;
        aDesktop.setAttribute("data-heading-id", heading.id);
        aDesktop.addEventListener("click", (e) => {
            e.preventDefault();
            scrollParaHeading(heading.id);
        });
        liDesktop.appendChild(aDesktop);
        ulDesktop.appendChild(liDesktop);
    });

    tocNavDesktop.appendChild(ulDesktop);

    // Configura o filtro em tempo real do sumário lateral
    const tocFilterContainer = document.getElementById("toc-filter-container");
    const tocFilterInput = document.getElementById("toc-filter-input");

    if (tocFilterContainer && tocFilterInput) {
        // Se o artigo tiver mais de 4 seções, exibe a caixinha de filtro rápido
        if (headings.length >= 4) {
            tocFilterContainer.style.display = "";
            tocFilterInput.value = "";
            tocFilterInput.oninput = (e) => {
                const termo = e.target.value.toLowerCase().trim();
                const itens = ulDesktop.querySelectorAll(".toc-item");
                itens.forEach(item => {
                    const texto = item.textContent.toLowerCase();
                    if (!termo || texto.includes(termo)) {
                        item.style.display = "";
                    } else {
                        item.style.display = "none";
                    }
                });
            };
        } else {
            tocFilterContainer.style.display = "none";
        }
    }

    // Inicializa o ScrollSpy para destacar o item ativo enquanto o usuário rola a página
    iniciarScrollSpy();
}

function scrollParaHeading(idOuTexto) {
    if (!idOuTexto) return;
    
    const normalizar = (s) => s.toLowerCase()
        .normalize("NFD").replace(/[\u0300-\u036f]/g, "")
        .replace(/[^\w\s-]/g, "")
        .replace(/\s+/g, "-")
        .trim();

    const slug = normalizar(idOuTexto);
    
    // 1. Tenta buscar direto por ID exato ou ID em slug
    let el = document.getElementById(idOuTexto) || document.getElementById(slug);
    
    // 2. Se não achar, procura entre todos os títulos do artigoCorpo
    if (!el && artigoCorpo) {
        const headings = artigoCorpo.querySelectorAll("h1, h2, h3, h4, h5, h6");
        for (const h of headings) {
            const hSlug = normalizar(h.textContent);
            const hIdSlug = h.id ? normalizar(h.id) : "";
            if (h.id === idOuTexto || h.id === slug || hSlug === slug || hIdSlug === slug || hSlug.includes(slug) || slug.includes(hSlug)) {
                el = h;
                break;
            }
        }
    }

    if (!el) {
        console.warn("Seção não encontrada para rolagem:", idOuTexto);
        return;
    }

    // Altura do sticky nav compensada no scroll
    const stickyNav = document.getElementById("sticky-nav");
    const navOffset = stickyNav ? stickyNav.offsetHeight + 20 : 80;

    const elementPosition = el.getBoundingClientRect().top;
    const offsetPosition = elementPosition + window.pageYOffset - navOffset;

    window.scrollTo({
        top: offsetPosition,
        behavior: "smooth"
    });
}

let scrollSpyObserver = null;
function iniciarScrollSpy() {
    if (scrollSpyObserver) {
        scrollSpyObserver.disconnect();
    }

    const headings = artigoCorpo.querySelectorAll("h2");
    if (headings.length === 0) return;

    const callback = (entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.id;
                document.querySelectorAll(".toc-nav a").forEach(link => {
                    if (link.getAttribute("data-heading-id") === id) {
                        link.classList.add("toc-active");
                    } else {
                        link.classList.remove("toc-active");
                    }
                });
            }
        });
    };

    scrollSpyObserver = new IntersectionObserver(callback, {
        rootMargin: "-80px 0px -70% 0px",
        threshold: 0.1
    });

    headings.forEach(h => scrollSpyObserver.observe(h));
}

function processarLinksObsidian() {
    const htmlAtual = artigoCorpo.innerHTML;
    const regexObsidian = /\[\[([^\n\]]+)\]\]/g;

    artigoCorpo.innerHTML = htmlAtual.replace(regexObsidian, (match, conteudoBruto) => {
        // Normaliza qualquer resquício de placeholders ou tags intermediárias
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

        // Remove tags HTML indesejadas do caminho de destino
        caminho = caminho.replace(/<[^>]+>/g, "").trim();

        return `<a class="obsidian-link" data-destino="${caminho}">${textoExibicao}</a>`;
    });

    artigoCorpo.querySelectorAll(".obsidian-link").forEach(link => {
        link.addEventListener("click", (e) => {
            e.preventDefault();
            const destino = link.getAttribute("data-destino");
            navegarParaLinkObsidian(destino);
        });
    });
}

function processarCalloutsObsidian() {
    const blockquotes = artigoCorpo.querySelectorAll('blockquote');
    blockquotes.forEach(bq => {
        const conteudo = bq.innerHTML;
        const match = conteudo.match(/\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\](?:\s*([^\n<]+))?/i);
        if (match) {
            const tipo = match[1].toUpperCase();
            const tituloCustomizado = match[2] ? match[2].trim() : '';
            
            // Remove a tag [!TIPO] e o título do conteúdo do parágrafo
            let htmlLimpo = conteudo.replace(/\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\](?:\s*[^\n<]+)?/i, '');
            
            // Remove parágrafos vazios gerados na conversão
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

    const linkHome = document.createElement("span");
    linkHome.className = "breadcrumb-link";
    linkHome.textContent = "início";
    linkHome.addEventListener("click", () => voltarParaHome(true));

    const sep1 = document.createElement("span");
    sep1.className = "breadcrumb-separator";
    sep1.textContent = "/";

    const linkCategoria = document.createElement("span");
    linkCategoria.className = "breadcrumb-link";
    linkCategoria.textContent = artigo.categoria;
    linkCategoria.addEventListener("click", () => {
        voltarParaHome(true);
        setTimeout(() => {
            abrirPastaPorNome(artigo.categoria);
        }, 120);
    });

    breadcrumbsNav.appendChild(linkHome);
    breadcrumbsNav.appendChild(sep1);
    breadcrumbsNav.appendChild(linkCategoria);
}

function renderizarBotoesNavegacao(artigo) {
    const navRodape = document.getElementById("artigo-nav-rodape");
    if (!navRodape) return;

    navRodape.innerHTML = "";

    const listaCategoria = todasAsPastas[artigo.categoria] || [];
    const indexAtual = listaCategoria.findIndex(a => a.path === artigo.path || a.titulo === artigo.titulo);

    const artigoAnterior = indexAtual > 0 ? listaCategoria[indexAtual - 1] : null;
    const artigoProximo = (indexAtual >= 0 && indexAtual < listaCategoria.length - 1) ? listaCategoria[indexAtual + 1] : null;
    const artigoResumo = listaCategoria.find(a => a.path.includes("00.") || a.titulo.toLowerCase().includes("resumo"));

    if (!artigoAnterior && !artigoProximo && !artigoResumo) return;

    const cardsGrid = document.createElement("div");
    cardsGrid.className = "artigo-nav-cards-grid";

    if (artigoAnterior) {
        const cardPrev = document.createElement("div");
        cardPrev.className = "nav-card nav-card-prev";
        cardPrev.innerHTML = `
            <span class="nav-card-label">&larr; artigo anterior</span>
            <span class="nav-card-title">${artigoAnterior.titulo}</span>
        `;
        cardPrev.addEventListener("click", () => {
            abrirArtigo(artigoAnterior.titulo, artigoAnterior.conteudo, true);
        });
        cardsGrid.appendChild(cardPrev);
    } else {
        const placeholder = document.createElement("div");
        placeholder.className = "nav-card-placeholder";
        cardsGrid.appendChild(placeholder);
    }

    if (artigoProximo) {
        const cardNext = document.createElement("div");
        cardNext.className = "nav-card nav-card-next";
        cardNext.innerHTML = `
            <span class="nav-card-label">próximo artigo &rarr;</span>
            <span class="nav-card-title">${artigoProximo.titulo}</span>
        `;
        cardNext.addEventListener("click", () => {
            abrirArtigo(artigoProximo.titulo, artigoProximo.conteudo, true);
        });
        cardsGrid.appendChild(cardNext);
    } else if (artigoResumo && artigoResumo.titulo !== artigo.titulo) {
        const cardResumo = document.createElement("div");
        cardResumo.className = "nav-card nav-card-next nav-card-resumo";
        cardResumo.innerHTML = `
            <span class="nav-card-label">resumo da matéria &rarr;</span>
            <span class="nav-card-title">${artigoResumo.titulo}</span>
        `;
        cardResumo.addEventListener("click", () => {
            abrirArtigo(artigoResumo.titulo, artigoResumo.conteudo, true);
        });
        cardsGrid.appendChild(cardResumo);
    }

    navRodape.appendChild(cardsGrid);
}

function abrirPastaPorNome(nomeCategoria) {
    const pastasContainer = document.getElementById("pastas-container");
    if (!pastasContainer) return;

    pastasContainer.querySelectorAll(".pasta-item").forEach(item => {
        const header = item.querySelector(".pasta-nome");
        if (header && header.textContent.trim() === nomeCategoria.trim()) {
            item.classList.add("aberta");
            item.scrollIntoView({ behavior: "smooth", block: "center" });
        } else {
            item.classList.remove("aberta");
        }
    });
}

function navegarParaLinkObsidian(nomeOuCaminho, atualizarHash = true) {
    if (!nomeOuCaminho) return;

    // Caso 1: Link interno para uma seção da página atual (ex.: [[#1. Tipo (Type)]] ou #secao)
    if (nomeOuCaminho.startsWith("#")) {
        const hashSecao = nomeOuCaminho.replace(/^#/, "").trim();
        scrollParaHeading(hashSecao);
        return;
    }

    // Caso 2: Link para outro artigo ou outro artigo com seção (ex.: [[OutroArtigo#Secao]])
    const [caminhoSemHash, hashSecao] = nomeOuCaminho.split("#");

    // Se o caminho antes do # for vazio, é link de âncora interno
    if (!caminhoSemHash || caminhoSemHash.trim() === "") {
        if (hashSecao) scrollParaHeading(hashSecao.trim());
        return;
    }

    const normalizar = (str) => decodeURIComponent(decodeURI(str))
        .replace(/^\.\//, "")
        .trim()
        .toLowerCase()
        .normalize("NFD").replace(/[\u0300-\u036f]/g, "") // Remove acentos
        .replace(/\.md$/i, "")
        .replace(/[(),:;+]/g, " ") // Remove parênteses, vírgulas, dois-pontos, mais
        .replace(/#/g, " ")
        .replace(/\s+/g, " ")
        .trim();

    const limpo = normalizar(caminhoSemHash);
    const limpoApenasNome = limpo.split("/").pop();

    // Procura o artigo por correspondência exata de caminho, nome do arquivo ou título
    const encontrado = todosOsArtigos.find(a => {
        const caminhoSemExtensao = normalizar(a.path);
        const nomeArquivo = normalizar(a.path.split("/").pop());
        const tituloNorm = normalizar(a.titulo);

        return caminhoSemExtensao === limpo ||
               nomeArquivo === limpo ||
               nomeArquivo === limpoApenasNome ||
               tituloNorm === limpo ||
               tituloNorm === limpoApenasNome;
    }) || todosOsArtigos.find(a => {
        // Fallback: correspondência parcial se não achou exato
        const nomeArquivo = normalizar(a.path.split("/").pop());
        const tituloNorm = normalizar(a.titulo);
        return nomeArquivo.includes(limpoApenasNome) || limpoApenasNome.includes(nomeArquivo) || tituloNorm.includes(limpoApenasNome);
    });

    if (encontrado) {
        abrirArtigo(encontrado.titulo, encontrado.conteudo, atualizarHash);
        if (hashSecao) {
            setTimeout(() => {
                scrollParaHeading(hashSecao.trim());
            }, 120);
        }
    } else {
        // Se não encontrou outro arquivo com esse nome, tenta rolar até a seção no artigo atual
        if (hashSecao) {
            scrollParaHeading(hashSecao.trim());
        } else {
            scrollParaHeading(nomeOuCaminho);
        }
    }
}

function renderizarPastas() {
    const pastasContainer = document.getElementById("pastas-container");
    if (!pastasContainer) return;

    pastasContainer.innerHTML = "";

    const categoriasOrdenadas = Object.keys(todasAsPastas).sort();

    categoriasOrdenadas.forEach(categoria => {
        const pastaItem = document.createElement("div");
        pastaItem.className = "pasta-item";

        const header = document.createElement("div");
        header.className = "pasta-header";

        const nome = document.createElement("span");
        nome.className = "pasta-nome";
        nome.textContent = categoria;

        const icone = document.createElement("span");
        icone.className = "pasta-icone";
        icone.textContent = "+";

        header.appendChild(nome);
        header.appendChild(icone);

        const conteudo = document.createElement("div");
        conteudo.className = "pasta-conteudo";

        todasAsPastas[categoria].forEach(arquivo => {
            const linkArtigo = document.createElement("a");
            linkArtigo.className = "artigo-lista-link";
            linkArtigo.textContent = arquivo.titulo;
            
            linkArtigo.addEventListener("click", async (e) => {
                e.preventDefault();
                e.stopPropagation();
                abrirArtigo(arquivo.titulo, arquivo.conteudo, true);
            });
            
            conteudo.appendChild(linkArtigo);
        });

        pastaItem.appendChild(header);
        pastaItem.appendChild(conteudo);

        header.addEventListener("click", () => {
            const jaAberta = pastaItem.classList.contains("aberta");
            
            document.querySelectorAll(".pasta-item").forEach(item => {
                item.classList.remove("aberta");
            });

            if (!jaAberta) {
                pastaItem.classList.add("aberta");
            }
        });

        pastasContainer.appendChild(pastaItem);
    });
}

// Event Listeners para buscas
if (campoTexto) {
    campoTexto.addEventListener("input", (e) => {
        filtrarArtigos(e.target.value);
    });
}

if (campoTextoNav) {
    campoTextoNav.addEventListener("input", (e) => {
        filtrarArtigos(e.target.value);
    });
}

if (btnPesquisar) {
    btnPesquisar.addEventListener("click", () => {
        if (campoTexto) filtrarArtigos(campoTexto.value);
    });
}

if (btnVoltar) {
    btnVoltar.addEventListener("click", () => voltarParaHome(true));
}

// Configuração do Sticky Navbar baseada no scroll
const headerEl = document.querySelector("header");
const stickyNav = document.getElementById("sticky-nav");

window.addEventListener("scroll", () => {
    if (!headerEl || !stickyNav) return;
    const headerHeight = headerEl.offsetHeight;
    if (window.scrollY > headerHeight) {
        stickyNav.classList.add("visible");
    } else {
        stickyNav.classList.remove("visible");
    }
});

function voltarParaHome(atualizarHash = true) {
    leitorDeArtigo.classList.add("escondido");
    divResultados.classList.remove("escondido");
    const pastasContainer = document.getElementById("pastas-container");
    if (pastasContainer) {
        pastasContainer.classList.remove("escondido");
    }
    if (campoTexto) campoTexto.value = "";
    if (campoTextoNav) campoTextoNav.value = "";
    containerResultados.innerHTML = "";

    if (atualizarHash && window.location.hash) {
        history.pushState(null, "", window.location.pathname);
    }

    window.scrollTo({ top: 0, behavior: "smooth" });
}

const navLogo = document.getElementById("nav-logo");
if (navLogo) {
    navLogo.addEventListener("click", () => voltarParaHome(true));
}

const mainTitle = document.querySelector("header h1");
if (mainTitle) {
    mainTitle.addEventListener("click", () => voltarParaHome(true));
}

const navLinkPastas = document.getElementById("nav-link-pastas");
if (navLinkPastas) {
    navLinkPastas.addEventListener("click", (e) => {
        e.preventDefault();
        voltarParaHome(true);
        const pastasContainer = document.getElementById("pastas-container");
        if (pastasContainer) {
            pastasContainer.scrollIntoView({ behavior: "smooth", block: "start" });
        }
    });
}

// Tratamento de Histórico e Rotas do Navegador (Popstate e Hashchange)
function tratarHashNavegacao() {
    const hash = window.location.hash;
    if (!hash || hash === "#" || hash === "#/") {
        if (!leitorDeArtigo.classList.contains("escondido")) {
            voltarParaHome(false);
        }
        return;
    }

    const rotaLimpa = decodeURIComponent(hash.replace(/^#\/?/, "").trim());
    if (rotaLimpa) {
        navegarParaLinkObsidian(rotaLimpa, false);
    }
}

window.addEventListener("popstate", () => {
    tratarHashNavegacao();
});

// Inicializar na carga da página
carregarTodosOsArtigos();

