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
                return {
                    titulo: nomeSemExtensao,
                    path: encodeURI(`./${item.path}`) // Usa encodeURI para preservar barras de subpastas
                };
            });
    } catch (erro) {
        console.warn("Não foi possível listar via GitHub, usando lista padrão completa:", erro);
        // Fallback local completo com todos os arquivos do vault puc
        return [
            { titulo: "Aula Inaugural - Resumo", path: "./00. Geral/Aula Inaugural - Resumo.md" },
            { titulo: "Aula Inaugural - Transcrição", path: "./00. Geral/Aula Inaugural - Transcrição.md" },
            { titulo: "01. Programacao Modular - Resumo", path: "./01. Programacao Modular/01. Programacao Modular - Resumo.md" },
            { titulo: "Prompts de Estudo (LLM) - Programacao Modular", path: "./01. Programacao Modular/Prompts de Estudo (LLM).md" },
            { titulo: "02. Modelagem de Dados - Resumo", path: "./02. Modelagem de Dados/02. Modelagem de Dados - Resumo.md" },
            { titulo: "Prompts de Estudo (LLM) - Modelagem de Dados", path: "./02. Modelagem de Dados/Prompts de Estudo (LLM).md" },
            { titulo: "03. Manipulacao de Dados SQL - Resumo", path: "./03. Manipulacao de Dados SQL/03. Manipulacao de Dados SQL - Resumo.md" },
            { titulo: "Prompts de Estudo (LLM) - Manipulacao de Dados SQL", path: "./03. Manipulacao de Dados SQL/Prompts de Estudo (LLM).md" },
            { titulo: "04. Algoritmos e Estruturas de Dados - Resumo", path: "./04. Algoritmos e Estruturas de Dados/04. Algoritmos e Estruturas de Dados - Resumo.md" },
            { titulo: "Recordando C# e arrays", path: "./04. Algoritmos e Estruturas de Dados/Recordando C# e arrays.md" },
            { titulo: "Prompts de Estudo (LLM) - Algoritmos e Estruturas de Dados", path: "./04. Algoritmos e Estruturas de Dados/Prompts de Estudo (LLM).md" },
            { titulo: "05. Desenvolvimento Web Back-End - Resumo", path: "./05. Desenvolvimento Web Back-End/05. Desenvolvimento Web Back-End - Resumo.md" },
            { titulo: "Prompts de Estudo (LLM) - Desenvolvimento Web Back-End", path: "./05. Desenvolvimento Web Back-End/Prompts de Estudo (LLM).md" },
            { titulo: "06. Projeto - Aplicacao Interativa - Resumo", path: "./06. Projeto - Aplicacao Interativa/06. Projeto - Aplicacao Interativa - Resumo.md" },
            { titulo: "Ods 4 educação de qualidade", path: "./06. Projeto - Aplicacao Interativa/01. Ods 4 educação de qualidade - conceito, metas e fundamentação.md" },
            { titulo: "Requisitos e diretrizes de escopo do projeto", path: "./06. Projeto - Aplicacao Interativa/02. Requisitos e diretrizes de escopo do projeto.md" },
            { titulo: "Cronograma semanal e entregas de etapas", path: "./06. Projeto - Aplicacao Interativa/03. Cronograma semanal e entregas de etapas.md" },
            { titulo: "Reunião inicial da turma 5", path: "./06. Projeto - Aplicacao Interativa/04. Reunião inicial da turma 5 - resumo e transcrição integral.md" },
            { titulo: "Prompts de Estudo (LLM) - Projeto Interativo", path: "./06. Projeto - Aplicacao Interativa/Prompts de Estudo (LLM).md" },
            { titulo: "07. Engenharia de Requisitos - Resumo", path: "./07. Engenharia de Requisitos/07. Engenharia de Requisitos - Resumo.md" },
            { titulo: "O que é, afinal, engenharia de requisitos", path: "./07. Engenharia de Requisitos/01. O que é, afinal, engenharia de requisitos.md" },
            { titulo: "Engenharia de requisitos e negócios", path: "./07. Engenharia de Requisitos/02. Engenharia de requisitos e negócios - o alinhamento estratégico.md" },
            { titulo: "O conceito de requisito de software", path: "./07. Engenharia de Requisitos/03. O conceito de requisito de software - definição, níveis e características.md" },
            { titulo: "Requisitos funcionais e não-funcionais", path: "./07. Engenharia de Requisitos/04. Requisitos funcionais e não-funcionais.md" },
            { titulo: "Como escrever requisitos de qualidade", path: "./07. Engenharia de Requisitos/05. Como escrever requisitos de qualidade - critérios, padrões e boas práticas.md" },
            { titulo: "Técnicas de elicitação de requisitos", path: "./07. Engenharia de Requisitos/06. Técnicas de elicitação de requisitos.md" },
            { titulo: "Visão geral da uml e tipos de diagramas", path: "./07. Engenharia de Requisitos/07. Visão geral da uml e tipos de diagramas na modelagem de requisitos.md" },
            { titulo: "Modelagem de requisitos com casos de uso", path: "./07. Engenharia de Requisitos/08. Modelagem de requisitos com casos de uso e especificações textuais.md" },
            { titulo: "Modelagem estrutural com diagrama de classes", path: "./07. Engenharia de Requisitos/09. Modelagem estrutural com diagrama de classes da uml.md" },
            { titulo: "Modelagem estrutural e modularização", path: "./07. Engenharia de Requisitos/10. Modelagem estrutural e modularização com diagrama de pacotes da uml.md" },
            { titulo: "Verificação e validação de requisitos", path: "./07. Engenharia de Requisitos/11. Verificação e validação de requisitos - técnicas, revisões e qualidade.md" },
            { titulo: "Prompts de Estudo (LLM) - Engenharia de Requisitos", path: "./07. Engenharia de Requisitos/Prompts de Estudo (LLM).md" },
            { titulo: "12. Design de Interacao - Resumo", path: "./08. Design de Interacao/12. Design de Interacao - Resumo.md" },
            { titulo: "O que é interação humano-computador", path: "./08. Design de Interacao/01. O que é interação humano-computador e a visão teórica do ser humano.md" },
            { titulo: "Construções teóricas da interação humano-computador", path: "./08. Design de Interacao/02. Construções teóricas da interação humano-computador.md" },
            { titulo: "O papel dos sistemas interativos na atividade humana", path: "./08. Design de Interacao/03. O papel dos sistemas interativos na atividade humana.md" },
            { titulo: "Perspectivas de interação usuário-sistema", path: "./08. Design de Interacao/04. Perspectivas de interação usuário-sistema - interagir com o sistema vs. por meio do sistema.md" },
            { titulo: "Por que a perspectiva da interação importa", path: "./08. Design de Interacao/05. Por que a perspectiva da interação importa.md" },
            { titulo: "Contexto de uso, interface, interação e papéis", path: "./08. Design de Interacao/06. Contexto de uso, interface, interação e papéis do design.md" },
            { titulo: "Atributos de qualidade em sistemas interativos", path: "./08. Design de Interacao/07. Atributos de qualidade em sistemas interativos - usabilidade, comunicabilidade, acessibilidade e experiência de uso.md" },
            { titulo: "Engenharia cognitiva e os problemas da interação", path: "./08. Design de Interacao/08. Engenharia cognitiva e os problemas da interação usuário-sistema.md" },
            { titulo: "Engenharia semiótica", path: "./08. Design de Interacao/09. Engenharia semiótica - comunicação usuário-sistema e metacomunicação usuário-designer.md" },
            { titulo: "Envolvimento do usuário no design", path: "./08. Design de Interacao/10. Envolvimento do usuário no design - projetar de modo independente, centrado ou participativo.md" },
            { titulo: "Racionalismo técnico e reflexão em ação", path: "./08. Design de Interacao/11. Racionalismo técnico e reflexão em ação - o papel da técnica e da criatividade no design.md" },
            { titulo: "Prompts de Estudo (LLM) - Design de Interacao", path: "./08. Design de Interacao/Prompts de Estudo (LLM).md" },
            { titulo: "09. Redes de Computadores - Resumo", path: "./09. Redes de Computadores/09. Redes de Computadores - Resumo.md" },
            { titulo: "Prompts de Estudo (LLM) - Redes de Computadores", path: "./09. Redes de Computadores/Prompts de Estudo (LLM).md" },
            { titulo: "10. Lideranca e Competencias - Resumo", path: "./10. Lideranca e Competencias/10. Lideranca e Competencias - Resumo.md" },
            { titulo: "Prompts de Estudo (LLM) - Lideranca e Competencias", path: "./10. Lideranca e Competencias/Prompts de Estudo (LLM).md" },
            { titulo: "11. Desafios Contemporaneos - Resumo", path: "./11. Desafios Contemporaneos/11. Desafios Contemporaneos - Resumo.md" },
            { titulo: "Prompts de Estudo (LLM) - Desafios Contemporaneos", path: "./11. Desafios Contemporaneos/Prompts de Estudo (LLM).md" }
        ];
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

    // Renderiza a estrutura de pastas na página inicial
    renderizarPastas();
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
        const protegido = conteudoInterno.replace(/\\?\|/g, "___OBSIDIAN_PIPE___");
        return "[[" + protegido + "]]";
    });
}

function abrirArtigo(titulo, conteudoMarkdown) {
    divResultados.classList.add("escondido");
    const pastasContainer = document.getElementById("pastas-container");
    if (pastasContainer) pastasContainer.classList.add("escondido");

    artigoTitulo.textContent = titulo;
    
    // Filtra e remove o bloco de metadados/atributos (YAML Frontmatter --- ... ---)
    const markdownLimpo = removerFrontmatter(conteudoMarkdown);

    // Converte a sintaxe de highlight do Obsidian ==texto== para <mark class="obsidian-highlight">texto</mark>
    const markdownComHighlight = markdownLimpo.replace(/==([^=]+)==/g, '<mark class="obsidian-highlight">$1</mark>');

    // Protege caracteres '|' em links do Obsidian [[Link|Texto]] para não quebrarem tabelas no marked.parse
    const markdownProtegido = protegerPipesObsidian(markdownComHighlight);

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

    leitorDeArtigo.classList.remove("escondido");
    window.scrollTo({ top: 0, behavior: "smooth" });
}

function processarLinksObsidian() {
    const htmlAtual = artigoCorpo.innerHTML;
    const regexObsidian = /\[\[([^\n\]]+)\]\]/g;

    artigoCorpo.innerHTML = htmlAtual.replace(regexObsidian, (match, conteudo) => {
        let caminho = "";
        let textoExibicao = "";

        if (conteudo.includes("___OBSIDIAN_PIPE___")) {
            const partes = conteudo.split("___OBSIDIAN_PIPE___");
            caminho = partes[0].trim();
            textoExibicao = partes[1].trim();
        } else {
            caminho = conteudo.trim();
            textoExibicao = conteudo.trim();
        }

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

function navegarParaLinkObsidian(nomeOuCaminho) {
    if (!nomeOuCaminho) return;

    const normalizar = (str) => decodeURIComponent(decodeURI(str))
        .replace(/^\.\//, "")
        .trim()
        .toLowerCase()
        .replace(/\.md$/i, "")
        .replace(/:/g, " -")
        .replace(/\s+/g, " ");

    const limpo = normalizar(nomeOuCaminho);
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
        abrirArtigo(encontrado.titulo, encontrado.conteudo);
    } else {
        console.warn("Artigo não encontrado para o link Obsidian:", nomeOuCaminho);
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
                abrirArtigo(arquivo.titulo, arquivo.conteudo);
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
    btnVoltar.addEventListener("click", voltarParaHome);
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

function voltarParaHome() {
    leitorDeArtigo.classList.add("escondido");
    divResultados.classList.remove("escondido");
    const pastasContainer = document.getElementById("pastas-container");
    if (pastasContainer) {
        pastasContainer.classList.remove("escondido");
    }
    if (campoTexto) campoTexto.value = "";
    if (campoTextoNav) campoTextoNav.value = "";
    containerResultados.innerHTML = "";
    window.scrollTo({ top: 0, behavior: "smooth" });
}

const navLogo = document.getElementById("nav-logo");
if (navLogo) {
    navLogo.addEventListener("click", voltarParaHome);
}

const mainTitle = document.querySelector("header h1");
if (mainTitle) {
    mainTitle.addEventListener("click", voltarParaHome);
}

const navLinkPastas = document.getElementById("nav-link-pastas");
if (navLinkPastas) {
    navLinkPastas.addEventListener("click", (e) => {
        e.preventDefault();
        leitorDeArtigo.classList.add("escondido");
        divResultados.classList.remove("escondido");
        const pastasContainer = document.getElementById("pastas-container");
        if (pastasContainer) {
            pastasContainer.classList.remove("escondido");
            pastasContainer.scrollIntoView({ behavior: "smooth", block: "start" });
        }
    });
}

// Inicializar na carga da página
carregarTodosOsArtigos();
