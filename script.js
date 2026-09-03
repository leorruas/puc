// script.js - Coordenador Principal da Aplicação
import { informacoesDisciplinas, obterListaDeArquivos } from "./js/vault.js";
import { renderizarDiagramasMermaid } from "./js/mermaid.js?v=mermaid-style-v6";

// Variáveis globais
let todosOsArtigos = [];
let todasAsPastas = {};
let artigoAtual = null;
let indiceDeBuscaPronto = false;

const campoTexto = document.getElementById("main-search-input");
const campoTextoNav = document.getElementById("nav-search-input");
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
        renderizarDiagramasMermaid(artigoCorpo);
    });
}

function limparNomeCategoria(categoria) {
    return categoria.replace(/^\d+\.\s*/, "").toLowerCase();
}

function limparNomeTitulo(titulo) {
    if (!titulo) return "";
    return titulo.replace(/^\d+\.\s*/, "");
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
            const res = await fetch(item.path, { cache: "no-cache" });
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
    indiceDeBuscaPronto = true;

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
        acao.setAttribute("aria-label", limparNomeTitulo(artigo.titulo));

        const numeroFormatado = String(idx + 1).padStart(2, "0");

        acao.innerHTML = `
            <span class="disciplina-acao-numero">${numeroFormatado}</span>
            <span class="disciplina-acao-conteudo">
                <strong>${limparNomeTitulo(artigo.titulo)}</strong>
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

function normalizarTextoParaBusca(texto = "") {
    return String(texto)
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
        .toLocaleLowerCase("pt-BR");
}

function termosDaBusca(termoBusca) {
    return normalizarTextoParaBusca(termoBusca)
        .replace(/[^\p{L}\p{N}]+/gu, " ")
        .trim()
        .split(/\s+/)
        .filter(Boolean);
}

function contemTodosOsTermos(texto, termos) {
    const textoNormalizado = normalizarTextoParaBusca(texto);
    return termos.every(termo => textoNormalizado.includes(termo));
}

function criarIndiceNormalizado(texto = "") {
    const caracteres = Array.from(String(texto));
    const origens = [];
    let normalizado = "";

    caracteres.forEach((caractere, indiceOriginal) => {
        const trechoNormalizado = normalizarTextoParaBusca(caractere);
        for (const caractereNormalizado of trechoNormalizado) {
            normalizado += caractereNormalizado;
            origens.push(indiceOriginal);
        }
    });

    return { caracteres, normalizado, origens };
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

    document.getElementById("orientacoes-iniciais")?.classList.add("escondido");
    document.getElementById("explorar-disciplinas")?.classList.add("escondido");

    if (!indiceDeBuscaPronto) {
        divResultados.classList.remove("escondido");
        containerResultados.innerHTML = `<p class="mensagem-busca">preparando a pesquisa dos artigos… tente novamente em instantes.</p>`;
        return;
    }

    const termo = termoBusca.trim();
    const termos = termosDaBusca(termo);

    if (normalizarTextoParaBusca(termo).length < 2) {
        divResultados.classList.remove("escondido");
        containerResultados.innerHTML = `<p class="mensagem-busca">digite ao menos <strong>duas letras</strong> para pesquisar nos tópicos e artigos.</p>`;
        return;
    }

    const filtrados = todosOsArtigos
        .filter(artigo => contemTodosOsTermos(`${artigo.titulo} ${artigo.categoria} ${artigo.conteudo}`, termos))
        .sort((a, b) => {
            const prioridade = (artigo) => {
                const titulo = normalizarTextoParaBusca(artigo.titulo);
                const categoria = normalizarTextoParaBusca(artigo.categoria);
                const consulta = normalizarTextoParaBusca(termo);
                if (titulo === consulta) return 0;
                if (titulo.includes(consulta)) return 1;
                if (contemTodosOsTermos(artigo.titulo, termos)) return 2;
                if (contemTodosOsTermos(categoria, termos)) return 3;
                return 4;
            };
            const prioridadeA = prioridade(a);
            const prioridadeB = prioridade(b);
            return prioridadeA - prioridadeB || a.titulo.localeCompare(b.titulo, "pt-BR", { numeric: true });
        });

    exibirResultados(filtrados, termo, termos);
}

function destacarTexto(texto, termo) {
    const termos = termosDaBusca(termo);
    if (!termos.length) return escaparHtml(texto);

    const indice = criarIndiceNormalizado(texto);
    const intervalos = [];
    termos.forEach(termoNormalizado => {
        let posicao = indice.normalizado.indexOf(termoNormalizado);
        while (posicao !== -1) {
            const inicio = indice.origens[posicao];
            const fim = indice.origens[posicao + termoNormalizado.length - 1] + 1;
            intervalos.push([inicio, fim]);
            posicao = indice.normalizado.indexOf(termoNormalizado, posicao + termoNormalizado.length);
        }
    });

    const mesclados = intervalos
        .sort((a, b) => a[0] - b[0])
        .reduce((resultado, intervalo) => {
            const ultimo = resultado.at(-1);
            if (ultimo && intervalo[0] <= ultimo[1]) ultimo[1] = Math.max(ultimo[1], intervalo[1]);
            else resultado.push([...intervalo]);
            return resultado;
        }, []);

    let cursor = 0;
    return mesclados.map(([inicio, fim]) => {
        const antes = escaparHtml(indice.caracteres.slice(cursor, inicio).join(""));
        const marcado = escaparHtml(indice.caracteres.slice(inicio, fim).join(""));
        cursor = fim;
        return `${antes}<mark class="highlight">${marcado}</mark>`;
    }).join("") + escaparHtml(indice.caracteres.slice(cursor).join(""));
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
    const indice = criarIndiceNormalizado(textoLimpo);
    const posicaoNormalizada = Math.min(...termosDaBusca(termo)
        .map(termoNormalizado => indice.normalizado.indexOf(termoNormalizado))
        .filter(posicao => posicao >= 0));
    const pos = Number.isFinite(posicaoNormalizada)
        ? indice.caracteres.slice(0, indice.origens[posicaoNormalizada]).join("").length
        : -1;
    
    if (pos === -1) {
        return textoLimpo.substring(0, 140) + "...";
    }
    
    const inicio = Math.max(0, pos - 50);
    const fim = Math.min(textoLimpo.length, pos + 90);
    let trecho = textoLimpo.substring(inicio, fim);
    
    if (inicio > 0) trecho = "..." + trecho;
    if (fim < textoLimpo.length) trecho = trecho + "...";
    
    return trecho;
}

function exibirResultados(artigos, termo = "", termos = []) {
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

    const listaTermos = termos.length ? termos : termosDaBusca(termo);

    Object.keys(grupos)
        .sort((a, b) => {
            const tituloEmA = grupos[a].some(artigo => contemTodosOsTermos(artigo.titulo, listaTermos));
            const tituloEmB = grupos[b].some(artigo => contemTodosOsTermos(artigo.titulo, listaTermos));
            const diffTitulo = Number(tituloEmB) - Number(tituloEmA);
            return diffTitulo !== 0 ? diffTitulo : a.localeCompare(b, "pt-BR", { numeric: true });
        })
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
                titulo.innerHTML = destacarTexto(limparNomeTitulo(artigo.titulo), termo);

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
                    const abrirNaOcorrencia = !contemTodosOsTermos(artigo.titulo, listaTermos);
                    abrirArtigo(artigo.titulo, artigo.conteudo, true, abrirNaOcorrencia ? listaTermos : []);
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

function protegerLinksObsidian(md, storage = []) {
    if (!md) return md;
    return md.replace(/\[\[([^\]]+)\]\]/g, (match, conteudoInterno) => {
        const protegido = conteudoInterno.replace(/\\?\|/g, "%%OBSIDIANPIPE%%");
        storage.push(protegido);
        return `@@OBSIDIAN_LINK_${storage.length - 1}@@`;
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

function encontrarAlvoDaBuscaNoArtigo(termos) {
    if (!termos?.length || !artigoCorpo) return null;

    const secoes = Array.from(artigoCorpo.querySelectorAll("h2, h3, h4"));
    for (const secao of secoes) {
        let textoDaSecao = secao.textContent || "";
        for (let no = secao.nextElementSibling; no && !["H2", "H3", "H4"].includes(no.tagName); no = no.nextElementSibling) {
            textoDaSecao += ` ${no.textContent || ""}`;
        }
        if (contemTodosOsTermos(textoDaSecao, termos)) return secao;
    }

    return Array.from(artigoCorpo.querySelectorAll("p, li, blockquote, td"))
        .find(elemento => contemTodosOsTermos(elemento.textContent, termos)) || null;
}

// Leitor de Artigos com Suporte Suíço
function abrirArtigo(titulo, conteudoMarkdown, atualizarHash = true, termosBusca = []) {
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

    artigoTitulo.textContent = limparNomeTitulo(artigoAtual.titulo);

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
    const linksObsidianStorage = [];
    const markdownProtegido = protegerLinksObsidian(markdownComSetas, linksObsidianStorage);
    const markdownNormalizado = normalizarListasObsidian(markdownProtegido);

    if (typeof marked !== 'undefined') {
        let htmlRenderizado = marked.parse(markdownNormalizado);
        htmlRenderizado = htmlRenderizado.replace(/@@OBSIDIAN_LINK_(\d+)@@/g, (match, index) => {
            const raw = linksObsidianStorage[parseInt(index, 10)];
            return raw ? `[[${raw}]]` : match;
        });
        artigoCorpo.innerHTML = htmlRenderizado;
    } else {
        let textoRenderizado = markdownNormalizado;
        textoRenderizado = textoRenderizado.replace(/@@OBSIDIAN_LINK_(\d+)@@/g, (match, index) => {
            const raw = linksObsidianStorage[parseInt(index, 10)];
            return raw ? `[[${raw}]]` : match;
        });
        artigoCorpo.innerText = textoRenderizado;
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
        setTimeout(() => renderizarDiagramasMermaid(artigoCorpo), 50);
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

    const alvoDaBusca = encontrarAlvoDaBuscaNoArtigo(termosBusca);
    if (alvoDaBusca) {
        window.setTimeout(() => alvoDaBusca.scrollIntoView({ behavior: "smooth", block: "start" }), 80);
    } else {
        rolarAoTopo();
        requestAnimationFrame(() => rolarAoTopo());
        setTimeout(rolarAoTopo, 50);
        setTimeout(rolarAoTopo, 150);
    }
}

function processarContextoArtigo(conteudoMarkdown) {
    const contextoEl = document.getElementById("artigo-contexto");
    if (!contextoEl) return;

    const matchContexto = conteudoMarkdown.match(/^>\s*\*\*Contexto:\*\*\s*([^\n\r]+(?:\n>[^\n\r]+)*)/m) ||
                          conteudoMarkdown.match(/^>\s*([^\n\r]+(?:\n>[^\n\r]+)*)/m);

    if (matchContexto && matchContexto[1]) {
        let textoContexto = matchContexto[1].replace(/\n>/g, ' ').trim();
        textoContexto = textoContexto.replace(/^(?:\*\*Contexto:\*\*|Contexto:)\s*/i, '');
        textoContexto = textoContexto.replace(/\[\[(?:[^|\]]*\|)?([^\]]+)\]\]/g, '$1');
        textoContexto = textoContexto.replace(/==([^=]+)==/g, '<mark class="obsidian-highlight">$1</mark>');

        const htmlContexto = typeof marked !== 'undefined'
            ? marked.parseInline(textoContexto)
            : textoContexto;

        contextoEl.innerHTML = `
            <div class="contexto-icone">
                <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">
                    <circle cx="12" cy="12" r="8"></circle>
                    <path d="m14.8 9.2-2.1 4.3-4.3 2.1 2.1-4.3z"></path>
                </svg>
            </div>
            <p><strong>Contexto:</strong> ${htmlContexto}</p>
        `;
        contextoEl.hidden = false;
        contextoEl.classList.remove("escondido");
    } else {
        contextoEl.innerHTML = "";
        contextoEl.hidden = true;
        contextoEl.classList.add("escondido");
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

        const codeEl = pre.querySelector('code');
        if (codeEl && !pre.classList.contains('has-line-numbers')) {
            const rawCode = codeEl.textContent.replace(/\r\n/g, '\n').replace(/\r/g, '\n');
            const lines = rawCode.split('\n');
            if (lines.length > 0 && lines[lines.length - 1] === '') {
                lines.pop();
            }

            if (lines.length > 0) {
                codeEl.innerHTML = '';
                lines.forEach((linhaTexto) => {
                    const lineSpan = document.createElement('span');
                    lineSpan.className = 'code-line';
                    
                    if (!linhaTexto) {
                        lineSpan.textContent = ' ';
                    } else {
                        // Detecta comentários de linha inteira ou inline (//, #, --, /* */, <!-- -->)
                        // Preserva strings literais simples antes do comentário se houver
                        const matchComentario = linhaTexto.match(/^(\s*)(\/\/.*|\/\*.*?\*\/|#.*|--.*|<!--.*?-->)$/) ||
                                                linhaTexto.match(/^([^"'\n]*?)(\/\/.*|#.*|--.*)$/);

                        if (matchComentario) {
                            const prefixo = matchComentario[1];
                            const comentario = matchComentario[2];
                            if (prefixo) {
                                lineSpan.appendChild(document.createTextNode(prefixo));
                            }
                            const commentSpan = document.createElement('span');
                            commentSpan.className = 'code-comment';
                            commentSpan.textContent = comentario;
                            lineSpan.appendChild(commentSpan);
                        } else {
                            lineSpan.textContent = linhaTexto;
                        }
                    }
                    codeEl.appendChild(lineSpan);
                });
                pre.classList.add('has-line-numbers');
            }
        }

        const btnCopiar = document.createElement('button');
        btnCopiar.className = 'btn-copiar-codigo';
        btnCopiar.type = 'button';
        btnCopiar.setAttribute('aria-label', 'copiar código');
        btnCopiar.textContent = 'copiar';

        btnCopiar.addEventListener('click', async (e) => {
            e.stopPropagation();
            let textoParaCopiar = "";
            if (codeEl) {
                const lineSpans = codeEl.querySelectorAll('.code-line');
                if (lineSpans.length > 0) {
                    textoParaCopiar = Array.from(lineSpans).map(s => s.textContent === ' ' ? '' : s.textContent).join('\n');
                } else {
                    textoParaCopiar = codeEl.innerText.replace(/copiar|copiado!/g, '').trim();
                }
            } else {
                textoParaCopiar = pre.innerText.replace(/copiar|copiado!/g, '').trim();
            }

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
                    btnCopiar.classList.remove('copiado');
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
            <span class="nav-card-title">${limparNomeTitulo(artigoAnterior.titulo)}</span>
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
            <span class="nav-card-title">${limparNomeTitulo(artigoProximo.titulo)}</span>
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
    spanArtigo.textContent = limparNomeTitulo(artigo.titulo);

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

function separarDestinoEHash(destino) {
    if (!destino) return { nomeArtigo: "", hashSecao: "" };

    let destinoDecodificado = destino.trim();
    try {
        destinoDecodificado = decodeURIComponent(decodeURI(destinoDecodificado));
    } catch (e) {}

    if (destinoDecodificado.startsWith("#")) {
        return { nomeArtigo: "", hashSecao: destinoDecodificado.replace(/^#/, "").trim() };
    }

    // Se tiver '#' que não seja parte do nome de linguagem como 'C#' ou 'c#'
    const partes = destinoDecodificado.split(/(?<![cC])#/);
    if (partes.length > 1) {
        const candidatoNome = partes[0].trim();
        const candidatoSecao = partes.slice(1).join("#").trim();
        if (buscarArtigoPorCaminho(candidatoNome)) {
            return { nomeArtigo: candidatoNome, hashSecao: candidatoSecao };
        }
    }

    // Se o destino completo já é um artigo existente (ex.: arquivo contendo C# no título e sem âncora)
    if (buscarArtigoPorCaminho(destinoDecodificado)) {
        return { nomeArtigo: destinoDecodificado, hashSecao: "" };
    }

    // Fallback: se houver qualquer '#' que divida em um artigo válido
    const ultimoHash = destinoDecodificado.lastIndexOf("#");
    if (ultimoHash > 0) {
        const candidatoNome = destinoDecodificado.substring(0, ultimoHash).trim();
        const candidatoSecao = destinoDecodificado.substring(ultimoHash + 1).trim();
        if (buscarArtigoPorCaminho(candidatoNome)) {
            return { nomeArtigo: candidatoNome, hashSecao: candidatoSecao };
        }
    }

    return { nomeArtigo: destinoDecodificado, hashSecao: "" };
}

function navegarParaLinkObsidian(destino, atualizarHash = true) {
    if (!destino) return;

    const { nomeArtigo, hashSecao } = separarDestinoEHash(destino);

    if (!nomeArtigo && hashSecao) {
        scrollParaHeading(hashSecao);
        return;
    }

    const encontrado = buscarArtigoPorCaminho(nomeArtigo);

    if (encontrado) {
        abrirArtigo(encontrado.titulo, encontrado.conteudo, atualizarHash);
        if (hashSecao) {
            setTimeout(() => {
                scrollParaHeading(hashSecao);
            }, 250);
            setTimeout(() => {
                scrollParaHeading(hashSecao);
            }, 500);
        }
    }
}

function buscarArtigoPorCaminho(nomeOuCaminho) {
    if (!nomeOuCaminho) return null;
    
    const normalizar = (str) => {
        try {
            str = decodeURIComponent(decodeURI(str));
        } catch (e) {}
        return str
            .replace(/^\.\//, "")
            .trim()
            .toLowerCase()
            .normalize("NFD").replace(/[\u0300-\u036f]/g, "") // Remove acentos
            .replace(/\.md$/i, "")
            .replace(/[(),:;+]/g, " ")
            .replace(/\s+/g, " ")
            .trim();
    };

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
    const { nomeArtigo, hashSecao } = separarDestinoEHash(destino);
    if (!nomeArtigo && hashSecao) return `#${encodeURIComponent(hashSecao)}`;

    const artigo = buscarArtigoPorCaminho(nomeArtigo);
    if (artigo) {
        const rotaBase = rotaDoArtigo(artigo);
        return hashSecao ? `${rotaBase}#${encodeURIComponent(hashSecao)}` : rotaBase;
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
function executarBuscaGlobal(termo, campoDeOrigem) {
    [campoTexto, campoTextoNav].forEach(campo => {
        if (campo && campo !== campoDeOrigem) campo.value = termo;
    });
    filtrarArtigos(termo);
}

function limparBuscaGlobal() {
    [campoTexto, campoTextoNav].forEach(campo => {
        if (campo) campo.value = "";
    });
    filtrarArtigos("");
}

if (campoTexto) {
    campoTexto.addEventListener("input", (e) => {
        executarBuscaGlobal(e.target.value, e.currentTarget);
    });
}

if (campoTextoNav) {
    campoTextoNav.addEventListener("input", (e) => {
        executarBuscaGlobal(e.target.value, e.currentTarget);
    });
}

document.addEventListener("keydown", (event) => {
    const comandoDeBusca = (event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k";
    if (comandoDeBusca) {
        event.preventDefault();
        const campoVisivel = campoTextoNav?.offsetParent !== null ? campoTextoNav : campoTexto;
        campoVisivel?.focus();
        campoVisivel?.select();
        return;
    }

    if (event.key === "Escape" && [campoTexto, campoTextoNav].includes(document.activeElement)) {
        limparBuscaGlobal();
        document.activeElement?.blur();
    }
});

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

const navLinkMapa = document.getElementById("nav-link-mapa");
if (navLinkMapa) {
    navLinkMapa.addEventListener("click", (e) => {
        if (e.metaKey || e.ctrlKey || e.shiftKey || e.button === 1) return;
        e.preventDefault();
        navegarParaLinkObsidian("00. Geral/Mapa de aprendizagem do semestre", true);
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
