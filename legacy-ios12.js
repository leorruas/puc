(function () {
    "use strict";

    var artigos = [];
    var artigosPorCategoria = {};
    var categoriaAtual = null;
    var inicio = document.getElementById("page-masthead");
    var orientacoes = document.getElementById("orientacoes-iniciais");
    var explorar = document.getElementById("explorar-disciplinas");
    var pastas = document.getElementById("pastas-container");
    var resultados = document.getElementById("resultados");
    var leitorDisciplina = document.getElementById("disciplina-leitor");
    var disciplinaCabecalho = document.getElementById("disciplina-cabecalho");
    var disciplinaAcoes = document.getElementById("disciplina-acoes");
    var leitorArtigo = document.getElementById("leitor-artigo");
    var artigoTitulo = document.getElementById("artigo-titulo");
    var artigoCorpo = document.getElementById("artigo-corpo");
    var breadcrumbs = document.getElementById("artigo-breadcrumbs");
    var buscaMain = document.getElementById("main-search-input");
    var buscaNav = document.getElementById("nav-search-input");
    var temaBtn = document.getElementById("theme-toggle");

    function mostrar(elemento) { if (elemento) elemento.classList.remove("escondido"); }
    function esconder(elemento) { if (elemento) elemento.classList.add("escondido"); }
    function rolarTopo() { window.scrollTo(0, 0); }
    function nomeLimpo(valor) { return String(valor || "").replace(/^\d+[.\-_\s]+/, ""); }
    function categoriaDo(caminho) { return String(caminho || "").split("/")[0] || "00. Geral"; }
    function tituloDo(caminho) { return caminho.split("/").pop().replace(/\.md$/i, ""); }
    function urlDo(caminho) { return "https://raw.githubusercontent.com/leorruas/puc/main/" + caminho.split("/").map(encodeURIComponent).join("/"); }
    function escaparHtml(valor) { return String(valor || "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/\"/g, "&quot;").replace(/'/g, "&#39;"); }

    function aplicarTema(tema, salvar) {
        document.documentElement.setAttribute("data-theme", tema);
        if (salvar) { try { localStorage.setItem("tema-puc", tema); } catch (erro) {} }
        if (temaBtn) temaBtn.textContent = tema === "light" ? "modo escuro" : "modo claro";
    }

    function iniciarTema() {
        var salvo = null;
        try { salvo = localStorage.getItem("tema-puc"); } catch (erro) {}
        var claro = window.matchMedia && window.matchMedia("(prefers-color-scheme: light)").matches;
        aplicarTema(salvo || (claro ? "light" : "dark"), false);
    }

    function agruparArtigos() {
        var i, categoria;
        artigosPorCategoria = {};
        for (i = 0; i < artigos.length; i += 1) {
            categoria = artigos[i].categoria;
            if (!artigosPorCategoria[categoria]) artigosPorCategoria[categoria] = [];
            artigosPorCategoria[categoria].push(artigos[i]);
        }
    }

    function montarHome() {
        var categorias = Object.keys(artigosPorCategoria).sort();
        var i, categoria, botao;
        if (!pastas) return;
        pastas.innerHTML = "";
        for (i = 0; i < categorias.length; i += 1) {
            categoria = categorias[i];
            botao = document.createElement("button");
            botao.type = "button";
            botao.className = "legacy-area-link";
            botao.setAttribute("data-categoria", categoria);
            botao.textContent = nomeLimpo(categoria) + " · " + artigosPorCategoria[categoria].length + " notas";
            botao.onclick = function () { abrirCategoria(this.getAttribute("data-categoria")); };
            pastas.appendChild(botao);
        }
    }

    function abrirHome() {
        categoriaAtual = null;
        mostrar(inicio); mostrar(orientacoes); mostrar(explorar);
        esconder(resultados); esconder(leitorDisciplina); esconder(leitorArtigo);
        montarHome(); rolarTopo();
    }

    function abrirCategoria(categoria) {
        var lista = (artigosPorCategoria[categoria] || []).slice().sort(function (a, b) { return a.titulo.localeCompare(b.titulo); });
        var caixa = document.createElement("div"), i, botao;
        categoriaAtual = categoria;
        esconder(inicio); esconder(orientacoes); esconder(explorar); esconder(resultados); esconder(leitorArtigo); mostrar(leitorDisciplina);
        disciplinaCabecalho.innerHTML = "<h2>" + escaparHtml(nomeLimpo(categoria)) + "</h2>";
        disciplinaAcoes.innerHTML = "";
        caixa.className = "legacy-lista";
        for (i = 0; i < lista.length; i += 1) {
            botao = document.createElement("button");
            botao.type = "button"; botao.setAttribute("data-caminho", lista[i].caminho); botao.textContent = nomeLimpo(lista[i].titulo);
            botao.onclick = function () { abrirArtigo(this.getAttribute("data-caminho")); };
            caixa.appendChild(botao);
        }
        disciplinaAcoes.appendChild(caixa); rolarTopo();
    }

    function removerFrontmatter(markdown) { return String(markdown || "").replace(/^---[\s\S]*?---\s*/, ""); }
    function renderizarMarkdown(markdown) {
        var texto = removerFrontmatter(markdown);
        if (window.marked) {
            try { return typeof window.marked.parse === "function" ? window.marked.parse(texto) : window.marked(texto); } catch (erro) {}
        }
        return "<pre>" + escaparHtml(texto) + "</pre>";
    }

    function instalarLinks() {
        var links = artigoCorpo.querySelectorAll("a"), i;
        for (i = 0; i < links.length; i += 1) {
            if (links[i].getAttribute("href").indexOf("[[") !== -1) continue;
        }
        artigoCorpo.innerHTML = artigoCorpo.innerHTML.replace(/\[\[([^\]|]+)(?:\|([^\]]+))?\]\]/g, function (texto, destino, rotulo) {
            return '<a href="#wiki:" data-destino="' + escaparHtml(destino) + '">' + escaparHtml(rotulo || destino.split("/").pop()) + "</a>";
        });
        links = artigoCorpo.querySelectorAll("a[data-destino]");
        for (i = 0; i < links.length; i += 1) {
            links[i].onclick = function (evento) { evento.preventDefault(); abrirWiki(this.getAttribute("data-destino")); };
        }
    }

    function abrirWiki(destino) {
        var normal = String(destino || "").replace(/\.md$/i, "").toLowerCase();
        var candidato = null, i;
        for (i = 0; i < artigos.length; i += 1) {
            if (artigos[i].caminho.replace(/\.md$/i, "").toLowerCase() === normal) { candidato = artigos[i]; break; }
            if (!candidato && artigos[i].categoria === categoriaAtual && artigos[i].titulo.toLowerCase() === normal.split("/").pop()) candidato = artigos[i];
        }
        if (!candidato) for (i = 0; i < artigos.length; i += 1) if (artigos[i].titulo.toLowerCase() === normal.split("/").pop()) { candidato = artigos[i]; break; }
        if (candidato) abrirArtigo(candidato.caminho);
    }

    function marcarMermaidLegado() {
        var blocos = artigoCorpo.querySelectorAll("code.language-mermaid"), i;
        for (i = 0; i < blocos.length; i += 1) if (blocos[i].parentNode) blocos[i].parentNode.className += " legacy-mermaid-fallback";
    }

    function abrirArtigo(caminho) {
        var item = null, i;
        for (i = 0; i < artigos.length; i += 1) if (artigos[i].caminho === caminho) { item = artigos[i]; break; }
        if (!item) return;
        categoriaAtual = item.categoria;
        esconder(inicio); esconder(orientacoes); esconder(explorar); esconder(resultados); esconder(leitorDisciplina); mostrar(leitorArtigo);
        artigoTitulo.textContent = nomeLimpo(item.titulo);
        breadcrumbs.innerHTML = '<a href="#" id="legacy-inicio">início</a> / <a href="#" id="legacy-categoria">' + escaparHtml(nomeLimpo(item.categoria)) + "</a>";
        document.getElementById("legacy-inicio").onclick = function (evento) { evento.preventDefault(); abrirHome(); };
        document.getElementById("legacy-categoria").onclick = function (evento) { evento.preventDefault(); abrirCategoria(categoriaAtual); };
        artigoCorpo.innerHTML = '<p class="legacy-status">Carregando artigo...</p>';
        fetch(urlDo(item.caminho), { cache: "no-cache" }).then(function (resposta) {
            if (!resposta.ok) throw new Error("HTTP " + resposta.status);
            return resposta.text();
        }).then(function (markdown) {
            artigoCorpo.innerHTML = renderizarMarkdown(markdown);
            instalarLinks(); marcarMermaidLegado(); rolarTopo();
        }).catch(function () { artigoCorpo.innerHTML = '<p class="legacy-status">Não foi possível carregar este artigo neste navegador.</p>'; });
    }

    function buscar(termo) {
        var texto = String(termo || "").toLowerCase(), lista, i, botao;
        if (buscaMain && buscaMain.value !== termo) buscaMain.value = termo;
        if (buscaNav && buscaNav.value !== termo) buscaNav.value = termo;
        if (!texto) { abrirHome(); return; }
        lista = artigos.filter(function (artigo) { return (artigo.titulo + " " + artigo.categoria).toLowerCase().indexOf(texto) !== -1; });
        esconder(inicio); esconder(orientacoes); esconder(explorar); esconder(leitorDisciplina); esconder(leitorArtigo); mostrar(resultados);
        resultados.innerHTML = '<div class="legacy-lista"></div>';
        var caixa = resultados.firstChild;
        if (!lista.length) caixa.innerHTML = '<p class="legacy-status">Nenhuma nota encontrada. No modo de compatibilidade, a busca é por título e matéria.</p>';
        for (i = 0; i < lista.length; i += 1) {
            botao = document.createElement("button"); botao.type = "button"; botao.setAttribute("data-caminho", lista[i].caminho);
            botao.textContent = nomeLimpo(lista[i].categoria) + " · " + nomeLimpo(lista[i].titulo);
            botao.onclick = function () { abrirArtigo(this.getAttribute("data-caminho")); }; caixa.appendChild(botao);
        }
    }

    function carregarCatalogo() {
        fetch("./js/vault.js?v=ipad-mini-v1", { cache: "no-cache" }).then(function (resposta) { return resposta.text(); }).then(function (texto) {
            var correspondencias = texto.match(/^\s*"([^\"]+\.md)",?$/gm) || [], i, caminho;
            for (i = 0; i < correspondencias.length; i += 1) {
                caminho = correspondencias[i].replace(/^\s*"|",?$/g, "");
                artigos.push({ caminho: caminho, titulo: tituloDo(caminho), categoria: categoriaDo(caminho) });
            }
            agruparArtigos(); abrirHome();
        }).catch(function () { if (pastas) pastas.innerHTML = '<p class="legacy-status">Não foi possível carregar o catálogo compatível.</p>'; });
    }

    if (buscaMain) buscaMain.oninput = function () { buscar(this.value); };
    if (buscaNav) buscaNav.oninput = function () { buscar(this.value); };
    if (temaBtn) temaBtn.onclick = function () { var atual = document.documentElement.getAttribute("data-theme"); aplicarTema(atual === "light" ? "dark" : "light", true); };
    document.getElementById("btn-voltar").onclick = function () { abrirCategoria(categoriaAtual); };
    document.getElementById("btn-voltar-disciplina").onclick = abrirHome;
    document.getElementById("nav-logo").onclick = abrirHome;
    iniciarTema(); carregarCatalogo();
}());
