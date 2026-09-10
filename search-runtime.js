(function () {
    "use strict";

    var buscaMain = document.getElementById("main-search-input");
    var buscaNav = document.getElementById("nav-search-input");
    var fetchNativo = window.fetch ? window.fetch.bind(window) : null;
    var bypassBuscaUmaVez = false;
    var indice = null;

    var gruposDeAliases = [
        ["poo", "programacao orientada a objetos", "orientacao a objetos"],
        ["fk", "chave estrangeira", "foreign key"],
        ["pk", "chave primaria", "primary key"],
        ["ihc", "interacao humano computador", "interacao humano-computador"],
        ["sgbd", "sistema gerenciador de banco de dados", "sistema de gerenciamento de banco de dados"],
        ["mer", "modelo entidade relacionamento", "modelo entidade-relacionamento"],
        ["der", "diagrama entidade relacionamento", "diagrama entidade-relacionamento"],
        ["sobrescrita", "sobreposicao", "override"],
        ["llm", "large language model", "modelo de linguagem"],
        ["rag", "retrieval augmented generation", "geracao aumentada por recuperacao"],
        ["crud", "create read update delete"],
        ["rest", "representational state transfer"]
    ];

    function normalizar(valor) {
        var texto = String(valor || "").toLowerCase();
        if (texto.normalize) texto = texto.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
        return texto.replace(/\s+/g, " ").trim();
    }

    function termosDaConsulta(consulta) {
        return normalizar(consulta)
            .replace(/[^a-z0-9#]+/g, " ")
            .trim()
            .split(/\s+/)
            .filter(function (termo) { return termo.length > 0; });
    }

    function unicos(lista) {
        var vistos = {};
        return lista.filter(function (item) {
            var chave = normalizar(item);
            if (!chave || vistos[chave]) return false;
            vistos[chave] = true;
            return true;
        });
    }

    function expansoesParaConsulta(consulta, termos) {
        var expansoes = [];
        var consultaNormalizada = normalizar(consulta);
        gruposDeAliases.forEach(function (grupo) {
            var grupoNormalizado = grupo.map(normalizar);
            var bateConsulta = grupoNormalizado.indexOf(consultaNormalizada) !== -1;
            var bateTermo = termos.some(function (termo) { return grupoNormalizado.indexOf(termo) !== -1; });
            if (bateConsulta || bateTermo) expansoes = expansoes.concat(grupoNormalizado);
        });
        return unicos(expansoes);
    }

    function contem(texto, termo) {
        return termo && normalizar(texto).indexOf(termo) !== -1;
    }

    function prepararArtigo(artigo) {
        artigo._busca = artigo._busca || {
            title: normalizar(artigo.title || artigo.fileTitle),
            category: normalizar(artigo.category),
            tags: normalizar((artigo.tags || []).join(" ")),
            aliases: normalizar((artigo.aliases || []).join(" ")),
            headings: normalizar((artigo.headings || []).join(" ")),
            body: normalizar(artigo.plainText || "")
        };
        return artigo._busca;
    }

    function pontuarArtigo(artigo, consulta) {
        var campos = prepararArtigo(artigo);
        var frase = normalizar(consulta);
        var termos = termosDaConsulta(consulta);
        var expansoes = expansoesParaConsulta(consulta, termos);
        var score = 0;
        var razoes = {};
        var termosEncontrados = 0;

        function registrar(campo, pontos, razao) {
            if (campo) {
                score += pontos;
                razoes[razao] = true;
                return true;
            }
            return false;
        }

        registrar(campos.title === frase, 180, "título");
        registrar(frase.length > 1 && campos.title.indexOf(frase) !== -1, 120, "título");
        registrar(frase.length > 1 && campos.tags.indexOf(frase) !== -1, 85, "tag");
        registrar(frase.length > 1 && campos.aliases.indexOf(frase) !== -1, 80, "alias");
        registrar(frase.length > 1 && campos.headings.indexOf(frase) !== -1, 70, "seção");
        registrar(frase.length > 1 && campos.category.indexOf(frase) !== -1, 50, "matéria");
        registrar(frase.length > 2 && campos.body.indexOf(frase) !== -1, 35, "conteúdo");

        termos.forEach(function (termo) {
            var achou = false;
            if (registrar(campos.title.indexOf(termo) !== -1, 35, "título")) achou = true;
            if (registrar(campos.tags.indexOf(termo) !== -1, 28, "tag")) achou = true;
            if (registrar(campos.aliases.indexOf(termo) !== -1, 26, "alias")) achou = true;
            if (registrar(campos.headings.indexOf(termo) !== -1, 22, "seção")) achou = true;
            if (registrar(campos.category.indexOf(termo) !== -1, 12, "matéria")) achou = true;
            if (registrar(campos.body.indexOf(termo) !== -1, 6, "conteúdo")) achou = true;
            if (achou) termosEncontrados += 1;
        });

        expansoes.forEach(function (termo) {
            if (termos.indexOf(termo) !== -1 || termo === frase) return;
            if (registrar(campos.title.indexOf(termo) !== -1, 24, "conceito relacionado")) return;
            if (registrar(campos.tags.indexOf(termo) !== -1, 20, "conceito relacionado")) return;
            if (registrar(campos.aliases.indexOf(termo) !== -1, 18, "conceito relacionado")) return;
            if (registrar(campos.headings.indexOf(termo) !== -1, 15, "conceito relacionado")) return;
            registrar(campos.body.indexOf(termo) !== -1, 4, "conceito relacionado");
        });

        var cobertura = termos.length ? termosEncontrados / termos.length : 0;
        score += cobertura * 40;
        if (termos.length > 1 && cobertura < 1) score *= 0.55 + (0.45 * cobertura);

        return {
            article: artigo,
            score: score,
            coverage: cobertura,
            reasons: Object.keys(razoes)
        };
    }

    function ranquear(consulta) {
        if (!indice || !indice.articles) return [];
        return indice.articles
            .map(function (artigo) { return pontuarArtigo(artigo, consulta); })
            .filter(function (resultado) { return resultado.score >= 8; })
            .sort(function (a, b) {
                if (b.score !== a.score) return b.score - a.score;
                if (b.coverage !== a.coverage) return b.coverage - a.coverage;
                return String(a.article.title || a.article.fileTitle).localeCompare(String(b.article.title || b.article.fileTitle), "pt-BR", { numeric: true });
            });
    }

    function escaparHtml(valor) {
        return String(valor || "")
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#39;");
    }

    function nomeLimpo(valor) {
        return String(valor || "").replace(/^\d+\.\s*/, "");
    }

    function trechoRelevante(artigo, consulta) {
        var texto = String(artigo.plainText || "");
        var textoNormalizado = normalizar(texto);
        var candidatos = termosDaConsulta(consulta).concat(expansoesParaConsulta(consulta, termosDaConsulta(consulta)));
        var posicao = -1;
        var termoAchado = "";

        candidatos.some(function (termo) {
            var encontrado = textoNormalizado.indexOf(termo);
            if (encontrado >= 0) {
                posicao = encontrado;
                termoAchado = termo;
                return true;
            }
            return false;
        });

        if (posicao < 0) return texto.slice(0, 180) + (texto.length > 180 ? "..." : "");
        var inicio = Math.max(0, posicao - 70);
        var fim = Math.min(texto.length, posicao + Math.max(termoAchado.length, 20) + 110);
        return (inicio > 0 ? "..." : "") + texto.slice(inicio, fim) + (fim < texto.length ? "..." : "");
    }

    function garantirContainer() {
        var resultados = document.getElementById("resultados");
        var container = resultados ? resultados.querySelector(".cards-container") : null;
        if (!resultados) return null;
        if (!container) {
            resultados.innerHTML = '<div class="cards-container"></div>';
            container = resultados.querySelector(".cards-container");
        }
        return container;
    }

    function sincronizarCampos(valor, origem) {
        [buscaMain, buscaNav].forEach(function (campo) {
            if (campo && campo !== origem && campo.value !== valor) campo.value = valor;
        });
    }

    function mostrarHome() {
        var resultados = document.getElementById("resultados");
        var container = garantirContainer();
        if (container) container.innerHTML = "";
        if (resultados) resultados.classList.add("escondido");
        var disciplina = document.getElementById("disciplina-leitor");
        var artigo = document.getElementById("leitor-artigo");
        var orientacoes = document.getElementById("orientacoes-iniciais");
        var explorar = document.getElementById("explorar-disciplinas");
        if (disciplina) disciplina.classList.add("escondido");
        if (artigo) artigo.classList.add("escondido");
        if (orientacoes) orientacoes.classList.remove("escondido");
        if (explorar) explorar.classList.remove("escondido");
    }

    function abrirResultado(artigo) {
        var moderno = suportaLeitorModerno();
        if (moderno) {
            var rota = "#/" + encodeURIComponent(artigo.category) + "/" + encodeURIComponent(artigo.fileTitle || artigo.title);
            history.pushState(null, "", rota);
            try {
                window.dispatchEvent(new PopStateEvent("popstate"));
            } catch (erro) {
                var evento = document.createEvent("Event");
                evento.initEvent("popstate", true, true);
                window.dispatchEvent(evento);
            }
            return;
        }

        var campo = buscaMain || buscaNav;
        if (!campo) return;
        bypassBuscaUmaVez = true;
        campo.value = artigo.fileTitle || artigo.title;
        var eventoInput = document.createEvent("HTMLEvents");
        eventoInput.initEvent("input", true, false);
        campo.dispatchEvent(eventoInput);

        var botoes = document.querySelectorAll('#resultados button[data-caminho]');
        for (var i = 0; i < botoes.length; i += 1) {
            if (botoes[i].getAttribute("data-caminho") === artigo.sourcePath) {
                botoes[i].click();
                break;
            }
        }
    }

    function renderizarBusca(consulta) {
        var termo = String(consulta || "").trim();
        var resultadosEl = document.getElementById("resultados");
        var container = garantirContainer();
        if (!container || !resultadosEl) return;

        if (!termo) {
            mostrarHome();
            return;
        }

        var orientacoes = document.getElementById("orientacoes-iniciais");
        var explorar = document.getElementById("explorar-disciplinas");
        var disciplina = document.getElementById("disciplina-leitor");
        var leitor = document.getElementById("leitor-artigo");
        if (orientacoes) orientacoes.classList.add("escondido");
        if (explorar) explorar.classList.add("escondido");
        if (disciplina) disciplina.classList.add("escondido");
        if (leitor) leitor.classList.add("escondido");
        resultadosEl.classList.remove("escondido");

        if (normalizar(termo).length < 2) {
            container.innerHTML = '<p class="mensagem-busca">digite ao menos <strong>duas letras</strong> para pesquisar.</p>';
            return;
        }

        if (!indice) {
            container.innerHTML = '<p class="mensagem-busca">preparando o índice de pesquisa...</p>';
            return;
        }

        var ranqueados = ranquear(termo).slice(0, 60);
        container.innerHTML = "";

        if (!ranqueados.length) {
            container.innerHTML = '<p class="mensagem-busca">nenhum resultado relevante para <strong>“' + escaparHtml(termo) + '”</strong>.</p>';
            return;
        }

        var resumo = document.createElement("p");
        resumo.className = "resumo-busca";
        resumo.textContent = ranqueados.length + (ranqueados.length === 1 ? " resultado relevante" : " resultados relevantes") + " para “" + termo + "”";
        container.appendChild(resumo);

        var lista = document.createElement("div");
        lista.className = "resultados-lista busca-ranqueada-lista";

        ranqueados.forEach(function (resultado, indiceResultado) {
            var artigo = resultado.article;
            var card = document.createElement("a");
            card.className = "resultado-item busca-ranqueada-item";
            card.href = "#/" + encodeURIComponent(artigo.category) + "/" + encodeURIComponent(artigo.fileTitle || artigo.title);

            var numero = document.createElement("span");
            numero.className = "resultado-numero";
            numero.textContent = String(indiceResultado + 1).padStart ? String(indiceResultado + 1).padStart(2, "0") : (indiceResultado + 1 < 10 ? "0" : "") + String(indiceResultado + 1);

            var conteudo = document.createElement("span");
            conteudo.className = "resultado-conteudo";

            var meta = document.createElement("span");
            meta.className = "busca-ranqueada-meta";
            meta.textContent = nomeLimpo(artigo.category);

            var titulo = document.createElement("strong");
            titulo.textContent = nomeLimpo(artigo.fileTitle || artigo.title);

            var trecho = document.createElement("span");
            trecho.className = "resultado-trecho";
            trecho.textContent = trechoRelevante(artigo, termo);

            var motivos = document.createElement("span");
            motivos.className = "busca-ranqueada-motivos";
            resultado.reasons.slice(0, 4).forEach(function (razao) {
                var badge = document.createElement("span");
                badge.className = "busca-ranqueada-badge";
                badge.textContent = razao;
                motivos.appendChild(badge);
            });

            conteudo.appendChild(meta);
            conteudo.appendChild(titulo);
            conteudo.appendChild(trecho);
            conteudo.appendChild(motivos);
            card.appendChild(numero);
            card.appendChild(conteudo);

            card.addEventListener("click", function (evento) {
                if (evento.metaKey || evento.ctrlKey || evento.shiftKey || evento.button === 1) return;
                evento.preventDefault();
                abrirResultado(artigo);
            });
            lista.appendChild(card);
        });

        container.appendChild(lista);
    }

    function suportaLeitorModerno() {
        try {
            new Function("var item = { filho: { valor: 1 } }; return item?.filho?.valor;");
            new Function("return /(?<!a)b/.test('b');");
            return true;
        } catch (erro) {
            return false;
        }
    }

    function aoDigitar(evento) {
        if (bypassBuscaUmaVez) {
            bypassBuscaUmaVez = false;
            return;
        }
        evento.stopImmediatePropagation();
        var valor = evento.target.value;
        sincronizarCampos(valor, evento.target);
        renderizarBusca(valor);
    }

    if (buscaMain) buscaMain.addEventListener("input", aoDigitar, true);
    if (buscaNav) buscaNav.addEventListener("input", aoDigitar, true);

    function mapaPorCaminho(artigos) {
        var mapa = {};
        artigos.forEach(function (artigo) { mapa[normalizar(artigo.sourcePath)] = artigo; });
        return mapa;
    }

    var promessaIndice = fetchNativo
        ? fetchNativo("search-index.json?v=search-v2", { cache: "no-cache" })
            .then(function (resposta) {
                if (!resposta.ok) throw new Error("Índice indisponível");
                return resposta.json();
            })
            .then(function (dados) {
                indice = dados;
                window.PUC_SEARCH_INDEX = dados;
                return dados;
            })
            .catch(function (erro) {
                console.warn("Busca avançada indisponível; usando fallback do leitor.", erro);
                return null;
            })
        : Promise.resolve(null);

    window.PUC_SEARCH_INDEX_PROMISE = promessaIndice;
    window.PUC_SEARCH = { rank: ranquear, normalize: normalizar };

    if (fetchNativo && window.Response) {
        window.fetch = function (entrada, opcoes) {
            var url = typeof entrada === "string" ? entrada : (entrada && entrada.url ? entrada.url : "");
            var ehArvore = /api\.github\.com\/repos\/leorruas\/puc\/git\/trees\/main\?recursive=1/.test(url);
            var prefixoRaw = "https://raw.githubusercontent.com/leorruas/puc/main/";
            var ehMarkdownRaw = url.indexOf(prefixoRaw) === 0 && /\.md(?:\?|$)/i.test(url);

            if (!ehArvore && !ehMarkdownRaw) return fetchNativo(entrada, opcoes);

            return promessaIndice.then(function (dados) {
                if (!dados || !dados.articles) return fetchNativo(entrada, opcoes);

                if (ehArvore) {
                    var arvore = dados.articles.map(function (artigo) {
                        return { path: artigo.sourcePath, type: "blob" };
                    });
                    return new Response(JSON.stringify({ tree: arvore }), {
                        status: 200,
                        headers: { "Content-Type": "application/json" }
                    });
                }

                var caminhoCodificado = url.slice(prefixoRaw.length).split("?")[0];
                var caminho;
                try {
                    caminho = caminhoCodificado.split("/").map(decodeURIComponent).join("/");
                } catch (erro) {
                    caminho = caminhoCodificado;
                }
                var mapa = mapaPorCaminho(dados.articles);
                var artigo = mapa[normalizar(caminho)];
                if (!artigo) return fetchNativo(entrada, opcoes);
                return new Response(artigo.markdown || "", {
                    status: 200,
                    headers: { "Content-Type": "text/markdown; charset=utf-8" }
                });
            }).catch(function () {
                return fetchNativo(entrada, opcoes);
            });
        };
    }
}());
