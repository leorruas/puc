import fs from "node:fs";

function substituirEntre(texto, inicio, fim, novoBloco) {
  const posInicio = texto.indexOf(inicio);
  const posFim = texto.indexOf(fim, posInicio + inicio.length);
  if (posInicio < 0 || posFim < 0) throw new Error(`Marcadores não encontrados: ${inicio} / ${fim}`);
  return texto.slice(0, posInicio) + novoBloco + "\n\n" + texto.slice(posFim);
}

function substituirUma(texto, antigo, novo, rotulo) {
  const ocorrencias = texto.split(antigo).length - 1;
  if (ocorrencias !== 1) throw new Error(`${rotulo}: esperava 1 ocorrência, encontrei ${ocorrencias}`);
  return texto.replace(antigo, novo);
}

let script = fs.readFileSync("script.js", "utf8");

const blocoCarga = `// Carrega o catálogo pelo índice e o conteúdo das notas sob demanda
function caminhoRawDoArtigo(sourcePath) {
    const caminhoCodificado = String(sourcePath || "")
        .split("/")
        .map(segmento => encodeURIComponent(segmento))
        .join("/");
    return \`https://raw.githubusercontent.com/leorruas/puc/main/\${caminhoCodificado}\`;
}

async function carregarTodosOsArtigos() {
    inicializarTema();
    let indiceBusca = null;

    try {
        if (window.PUC_SEARCH_INDEX_PROMISE) {
            indiceBusca = await window.PUC_SEARCH_INDEX_PROMISE;
        }
    } catch (erro) {
        console.warn("Índice otimizado indisponível; carregando catálogo pelo fallback.", erro);
    }

    if (indiceBusca?.articles?.length) {
        todosOsArtigos = indiceBusca.articles.map(item => ({
            titulo: item.fileTitle || item.title,
            path: caminhoRawDoArtigo(item.sourcePath),
            sourcePath: item.sourcePath,
            categoria: item.category,
            conteudo: null
        }));
    } else {
        const lista = await obterListaDeArquivos();
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
                    categoria,
                    conteudo: texto
                };
            } catch (e) {
                console.error(\`Erro ao carregar \${item.path}:\`, e);
                return null;
            }
        });
        const resultados = await Promise.all(promessas);
        todosOsArtigos = resultados.filter(artigo => artigo !== null);
    }

    indiceDeBuscaPronto = true;
    todasAsPastas = {};
    todosOsArtigos.forEach(artigo => {
        if (!todasAsPastas[artigo.categoria]) todasAsPastas[artigo.categoria] = [];
        todasAsPastas[artigo.categoria].push(artigo);
    });

    Object.values(todasAsPastas).forEach(artigos => {
        artigos.sort((a, b) => {
            return (a.sourcePath || a.path).localeCompare(b.sourcePath || b.path, "pt-BR", { numeric: true, sensitivity: "base" });
        });
    });

    renderizarPastas();
    if (window.location.hash) tratarHashNavegacao();
}`;

script = substituirEntre(
  script,
  "// Carrega os arquivos e busca o conteúdo de cada um",
  "// Renderiza a Grade Suíça de Matérias na Home",
  blocoCarga
);

script = substituirUma(
  script,
  "function abrirArtigo(titulo, conteudoMarkdown, atualizarHash = true, termosBusca = []) {",
  "async function abrirArtigo(titulo, conteudoMarkdown, atualizarHash = true, termosBusca = [], secaoBusca = \"\") {",
  "assinatura de abrirArtigo"
);

const artigoAtualAntigo = `    artigoAtual = todosOsArtigos.find(a => a.titulo === titulo && a.conteudo === conteudoMarkdown) ||
                  todosOsArtigos.find(a => a.titulo === titulo) || {
                      titulo: titulo,
                      path: \`./\${titulo}.md\`,
                      categoria: "00. Geral",
                      conteudo: conteudoMarkdown
                  };

    artigoTitulo.textContent = limparNomeTitulo(artigoAtual.titulo);`;

const artigoAtualNovo = `    artigoAtual = todosOsArtigos.find(a => a.titulo === titulo && a.conteudo === conteudoMarkdown) ||
                  todosOsArtigos.find(a => a.titulo === titulo) || {
                      titulo: titulo,
                      path: \`./\${titulo}.md\`,
                      categoria: "00. Geral",
                      conteudo: conteudoMarkdown
                  };

    if (!conteudoMarkdown && artigoAtual.path) {
        try {
            const resposta = await fetch(artigoAtual.path, { cache: "no-cache" });
            if (!resposta.ok) throw new Error(\`HTTP \${resposta.status}\`);
            conteudoMarkdown = await resposta.text();
            artigoAtual.conteudo = conteudoMarkdown;
        } catch (erro) {
            console.error(\`Erro ao carregar \${artigoAtual.sourcePath || artigoAtual.path}:\`, erro);
            conteudoMarkdown = "# Conteúdo indisponível\\n\\nNão foi possível carregar esta nota agora.";
        }
    }

    artigoTitulo.textContent = limparNomeTitulo(artigoAtual.titulo);`;

script = substituirUma(script, artigoAtualAntigo, artigoAtualNovo, "lazy load em abrirArtigo");

const scrollAntigo = `    const alvoDaBusca = encontrarAlvoDaBuscaNoArtigo(termosBusca);
    if (alvoDaBusca) {
        window.setTimeout(() => alvoDaBusca.scrollIntoView({ behavior: "smooth", block: "start" }), 80);
    } else {
        rolarAoTopo();
        requestAnimationFrame(() => rolarAoTopo());
        setTimeout(rolarAoTopo, 50);
        setTimeout(rolarAoTopo, 150);
    }`;

const scrollNovo = `    const alvoDaBusca = encontrarAlvoDaBuscaNoArtigo(termosBusca);
    if (secaoBusca) {
        window.setTimeout(() => scrollParaHeading(secaoBusca), 80);
        window.setTimeout(() => scrollParaHeading(secaoBusca), 220);
    } else if (alvoDaBusca) {
        window.setTimeout(() => alvoDaBusca.scrollIntoView({ behavior: "smooth", block: "start" }), 80);
    } else {
        rolarAoTopo();
        requestAnimationFrame(() => rolarAoTopo());
        setTimeout(rolarAoTopo, 50);
        setTimeout(rolarAoTopo, 150);
    }`;

script = substituirUma(script, scrollAntigo, scrollNovo, "rolagem para seção da busca");

const navegacaoAntiga = `    if (encontrado) {
        abrirArtigo(encontrado.titulo, encontrado.conteudo, atualizarHash);
        if (hashSecao) {
            setTimeout(() => {
                scrollParaHeading(hashSecao);
            }, 250);
            setTimeout(() => {
                scrollParaHeading(hashSecao);
            }, 500);
        }
    }`;

const navegacaoNova = `    if (encontrado) {
        abrirArtigo(encontrado.titulo, encontrado.conteudo, atualizarHash, [], hashSecao).then(() => {
            if (!hashSecao) return;
            setTimeout(() => scrollParaHeading(hashSecao), 120);
            setTimeout(() => scrollParaHeading(hashSecao), 320);
        });
    }`;

script = substituirUma(script, navegacaoAntiga, navegacaoNova, "links internos com lazy load");

const rotaAntiga = `        if (artigo) {
            abrirArtigo(artigo.titulo, artigo.conteudo, false);
            return;
        }`;

const rotaNova = `        if (artigo) {
            const contextoBusca = window.PUC_SEARCH_PENDING;
            window.PUC_SEARCH_PENDING = null;
            abrirArtigo(
                artigo.titulo,
                artigo.conteudo,
                false,
                contextoBusca?.terms || [],
                contextoBusca?.heading || ""
            );
            return;
        }`;

script = substituirUma(script, rotaAntiga, rotaNova, "contexto da busca na rota");
fs.writeFileSync("script.js", script);

let index = fs.readFileSync("index.html", "utf8");
index = index.replace("search-runtime.css?v=search-v2", "search-runtime.css?v=search-v3");
index = index.replace("search-runtime.js?v=search-v2", "search-runtime.js?v=search-v3");
index = index.replace("script.js?v=ipad-mini-v1", "script.js?v=search-v3");
fs.writeFileSync("index.html", index);

console.log("Migração search-v3 aplicada ao leitor e ao index.html.");
