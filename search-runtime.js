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
        ["rest", "representational state transfer"],
        ["fifo", "first in first out", "fila"],
        ["lifo", "last in first out", "pilha"],
        ["big o", "notacao assintotica", "complexidade assintotica"]
    ];

    var stopwords = {
        "a": true, "o": true, "as": true, "os": true, "de": true, "da": true, "do": true,
        "das": true, "dos": true, "e": true, "em": true, "no": true, "na": true, "nos": true,
        "nas": true, "um": true, "uma": true, "uns": true, "umas": true, "para": true, "por": true,
        "com": true, "que": true, "qual": true, "quais": true, "como": true, "quando": true,
        "onde": true, "entre": true, "sobre": true, "porque": true, "pra": true, "ao": true,
        "aos": true, "diferenca": true
    };

    function normalizar(valor) {
        var texto = String(valor || "").toLowerCase();
        if (texto.normalize) texto = texto.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
        return texto.replace(/\s+/g, " ").trim();
    }

    function termosDaConsulta(consulta) {
        var todos = normalizar(consulta)
            .replace(/[^a-z0-9#]+/g, " ")
            .trim()
            .split(/\s+/)
            .filter(function (termo) { return termo.length > 0; });
        var tecnicos = todos.filter(function (termo) { return !stopwords[termo]; });
        return tecnicos.length ? tecnicos : todos;
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

    function prepararArtigo(artigo) {
        if (artigo._busca) return artigo._busca;
        var headings = artigo.headings || [];
        artigo._busca = {
            title: normalizar(artigo.title || artigo.fileTitle),
            category: normalizar(artigo.category),
            tags: normalizar((artigo.tags || []).join(" ")),
            aliases: normalizar((artigo.aliases || []).join(" ")),
            headings: normalizar(headings.join(" ")),
            body: normalizar(artigo.plainText || ""),
            tokensFuzzy: unicos(
                normalizar([
                    artigo.title || artigo.fileTitle,
                    (artigo.tags || []).join(" "),
                    (artigo.aliases || []).join(" "),
                    headings.join(" ")
                ].join(" "))
                    .replace(/[^a-z0-9#]+/g, " ")
                    .split(/\s+/)
                    .filter(function (item) { return item.length >= 3; })
            )
        };
        return artigo._busca;
    }

    function distanciaEdicao(a, b, limite) {
        a = normalizar(a);
        b = normalizar(b);
        if (a === b) return 0;
        if (Math.abs(a.length - b.length) > limite) return limite + 1;

        var anterior = [];
        var atual = [];
        var i;
        var j;
        for (j = 0; j <= b.length; j += 1) anterior[j] = j;

        for (i = 1; i <= a.length; i += 1) {
            atual[0] = i;
            var menorLinha = atual[0];
            for (j = 1; j <= b.length; j += 1) {
                var custo = a.charAt(i - 1) === b.charAt(j - 1) ? 0 : 1;
                atual[j] = Math.min(
                    anterior[j] + 1,
                    atual[j - 1] + 1,
                    anterior[j - 1] + custo
                );
                if (atual[j] < menorLinha) menorLinha = atual[j];
            }
            if (menorLinha > limite) return limite + 1;
            var troca = anterior;
            anterior = atual;
            atual = troca;
        }
        return anterior[b.length];
    }

    function matchFuzzy(termo, artigo) {
        if (!termo || termo.length < 4) return null;
        var limite = termo.length >= 8 ? 2 : 1;
        var tokens = prepararArtigo(artigo).tokensFuzzy;
        var melhor = null;
        for (var i = 0; i < tokens.length; i += 1) {
            var candidato = tokens[i];
            if (Math.abs(candidato.length - termo.length) > limite) continue;
            var distancia = distanciaEdicao(termo, candidato, limite);
            if (distancia <= limite && (!melhor || distancia < melhor.distance)) {
                melhor = { token: candidato, distance: distancia };
                if (distancia === 1) break;
            }
        }
        return melhor;
    }

    function pontuarHeading(texto, consulta, termos, expansoes, usarFuzzy, artigo) {
        var heading = normalizar(texto);
        var frase = normalizar(consulta);
        var score = 0;
        if (frase.length > 1 && heading.indexOf(frase) !== -1) score += 60;
        termos.forEach(function (termo) {
            if (heading.indexOf(termo) !== -1) score += 16;
        });
        expansoes.forEach(function (termo) {
            if (termos.indexOf(termo) === -1 && heading.indexOf(termo) !== -1) score += 9;
        });
        if (usarFuzzy && score === 0 && artigo) {
            termos.forEach(function (termo) {
                var match = matchFuzzy(termo, artigo);
                if (match && heading.indexOf(match.token) !== -1) score += 6;
            });
        }
        return score;
    }

    function melhorHeading(artigo, consulta, usarFuzzy) {
        var headingData = artigo.headingData || (artigo.headings || []).map(function (texto) {
            return { level: 2, text: texto };
        });
        var termos = termosDaConsulta(consulta);
        var expansoes = expansoesParaConsulta(consulta, termos);
        var melhor = null;
        headingData.forEach(function (item) {
            if (!item || !item.text || item.level === 1) return;
            var score = pontuarHeading(item.text, consulta, termos, expansoes, usarFuzzy, artigo);
            if (score > 0 && (!melhor || score > melhor.score)) melhor = { text: item.text, score: score };
        });
        return melhor && melhor.score >= 9 ? melhor.text : "";
    }

    function pontuarArtigo(artigo, consulta, usarFuzzy) {
        var campos = prepararArtigo(artigo);
        var frase = normalizar(consulta);
        var termos = termosDaConsulta(consulta);
        var expansoes = expansoesParaConsulta(consulta, termos);
        var score = 0;
        var razoes = {};
        var termosEncontrados = 0;
        var fuzzyEncontrados = 0;
        var fraseForte = false;

        function registrar(condicao, pontos, razao) {
            if (!condicao) return false;
            score += pontos;
            razoes[razao] = true;
            return true;
        }

        if (registrar(campos.title === frase, 180, "título")) fraseForte = true;
        if (registrar(frase.length > 1 && campos.title.indexOf(frase) !== -1, 120, "título")) fraseForte = true;
        if (registrar(frase.length > 1 && campos.tags.indexOf(frase) !== -1, 85, "tag")) fraseForte = true;
        if (registrar(frase.length > 1 && campos.aliases.indexOf(frase) !== -1, 80, "alias")) fraseForte = true;
        if (registrar(frase.length > 1 && campos.headings.indexOf(frase) !== -1, 70, "seção")) fraseForte = true;
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
            if (achou) {
                termosEncontrados += 1;
            } else if (usarFuzzy) {
                var aproximado = matchFuzzy(termo, artigo);
                if (aproximado) {
                    score += aproximado.distance === 1 ? 18 : 10;
                    fuzzyEncontrados += 1;
                    razoes["termo aproximado"] = true;
                }
            }
        });

        expansoes.forEach(function (termo) {
            if (termos.indexOf(termo) !== -1 || termo === frase) return;
            if (registrar(campos.title.indexOf(termo) !== -1, 24, "conceito relacionado")) return;
            if (registrar(campos.tags.indexOf(termo) !== -1, 20, "conceito relacionado")) return;
            if (registrar(campos.aliases.indexOf(termo) !== -1, 18, "conceito relacionado")) return;
            if (registrar(campos.headings.indexOf(termo) !== -1, 15, "conceito relacionado")) return;
            registrar(campos.body.indexOf(termo) !== -1, 4, "conceito relacionado");
        });

        var cobertura = termos.length ? (termosEncontrados + fuzzyEncontrados) / termos.length : 0;
        score += cobertura * 40;
        if (termos.length > 1 && cobertura < 1) score *= 0.55 + (0.45 * cobertura);

        return {
            article: artigo,
            directScore: score,
            graphScore: 0,
            score: score,
            coverage: cobertura,
            reasons: Object.keys(razoes),
            strongPhrase: fraseForte,
            bestHeading: melhorHeading(artigo, consulta, usarFuzzy)
        };
    }

    function mapaResultados(resultados) {
        var mapa = {};
        resultados.forEach(function (resultado) {
            mapa[normalizar(resultado.article.sourcePath)] = resultado;
        });
        return mapa;
    }

    function aplicarGrafo(resultados) {
        var mapa = mapaResultados(resultados);
        var sementes = resultados
            .filter(function (resultado) { return resultado.directScore >= 30; })
            .sort(function (a, b) { return b.directScore - a.directScore; })
            .slice(0, 5);

        sementes.forEach(function (semente, indiceSemente) {
            var peso = Math.max(8, 22 - (indiceSemente * 3));
            var origem = semente.article;
            (origem.related || []).forEach(function (path) {
                var alvo = mapa[normalizar(path)];
                if (!alvo || alvo === semente) return;
                alvo.graphScore += peso;
                if (alvo.reasons.indexOf("nota relacionada") === -1) alvo.reasons.push("nota relacionada");
            });
            (origem.backlinks || []).forEach(function (path) {
                var alvo = mapa[normalizar(path)];
                if (!alvo || alvo === semente) return;
                alvo.graphScore += Math.max(6, peso - 6);
                if (alvo.reasons.indexOf("conexão no vault") === -1) alvo.reasons.push("conexão no vault");
            });
        });

        resultados.forEach(function (resultado) {
            resultado.score = resultado.directScore + resultado.graphScore;
            var umTermo = termosDaConsulta(window.PUC_SEARCH_LAST_QUERY || "").length <= 1;
            resultado.kind = (
                resultado.directScore >= 28 &&
                (umTermo || resultado.coverage >= 0.5 || resultado.strongPhrase || resultado.reasons.indexOf("termo aproximado") !== -1)
            ) ? "direct" : "related";
        });
    }

    function ranquear(consulta) {
        if (!indice || !indice.articles) return [];
        window.PUC_SEARCH_LAST_QUERY = consulta;

        var base = indice.articles.map(function (artigo) { return pontuarArtigo(artigo, consulta, false); });
        var fortes = base.filter(function (resultado) { return resultado.directScore >= 28; });
        var usarFuzzy = fortes.length < 3;
        var resultados = usarFuzzy
            ? indice.articles.map(function (artigo) { return pontuarArtigo(artigo, consulta, true); })
            : base;

        aplicarGrafo(resultados);

        return resultados
            .filter(function (resultado) { return resultado.score >= 8; })
            .sort(function (a, b) {
                if (a.kind !== b.kind) return a.kind === "direct" ? -1 : 1;
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
        var termos = termosDaConsulta(consulta);
        var candidatos = termos.concat(expansoesParaConsulta(consulta, termos));
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

    function rolarParaSecaoLegado(heading) {
        if (!heading) return;
        var alvoNormalizado = normalizar(heading);
        var tentativas = [120, 320, 650];
        tentativas.forEach(function (tempo) {
            window.setTimeout(function () {
                var headings = document.querySelectorAll("#artigo-corpo h1, #artigo-corpo h2, #artigo-corpo h3, #artigo-corpo h4, #artigo-corpo h5, #artigo-corpo h6");
                for (var i = 0; i < headings.length; i += 1) {
                    if (normalizar(headings[i].textContent) === alvoNormalizado) {
                        headings[i].scrollIntoView(true);
                        return;
                    }
                }
            }, tempo);
        });
    }

    function abrirResultado(resultado, consulta) {
        var artigo = resultado.article;
        var contextoBusca = {
            sourcePath: artigo.sourcePath,
            terms: termosDaConsulta(consulta),
            heading: resultado.bestHeading || ""
        };
        window.PUC_SEARCH_PENDING = contextoBusca;

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
                rolarParaSecaoLegado(contextoBusca.heading);
                break;
            }
        }
    }

    function criarTituloSecao(texto, quantidade) {
        var cabecalho = document.createElement("div");
        cabecalho.className = "busca-secao-cabecalho";
        var titulo = document.createElement("h3");
        titulo.textContent = texto;
        var total = document.createElement("span");
        total.textContent = String(quantidade);
        cabecalho.appendChild(titulo);
        cabecalho.appendChild(total);
        return cabecalho;
    }

    function criarListaResultados(resultados, termo, inicioNumero) {
        var lista = document.createElement("div");
        lista.className = "resultados-lista busca-ranqueada-lista";

        resultados.forEach(function (resultado, indiceResultado) {
            var artigo = resultado.article;
            var card = document.createElement("a");
            card.className = "resultado-item busca-ranqueada-item";
            card.href = "#/" + encodeURIComponent(artigo.category) + "/" + encodeURIComponent(artigo.fileTitle || artigo.title);

            var numero = document.createElement("span");
            numero.className = "resultado-numero";
            var numeroReal = inicioNumero + indiceResultado + 1;
            numero.textContent = String(numeroReal).padStart ? String(numeroReal).padStart(2, "0") : (numeroReal < 10 ? "0" : "") + String(numeroReal);

            var conteudo = document.createElement("span");
            conteudo.className = "resultado-conteudo";

            var meta = document.createElement("span");
            meta.className = "busca-ranqueada-meta";
            meta.textContent = nomeLimpo(artigo.category);

            var titulo = document.createElement("strong");
            titulo.textContent = nomeLimpo(artigo.fileTitle || artigo.title);

            var secao = document.createElement("span");
            secao.className = "busca-ranqueada-secao";
            if (resultado.bestHeading) secao.textContent = "em “" + resultado.bestHeading + "”";

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
            if (resultado.bestHeading) conteudo.appendChild(secao);
            conteudo.appendChild(trecho);
            conteudo.appendChild(motivos);
            card.appendChild(numero);
            card.appendChild(conteudo);

            card.addEventListener("click", function (evento) {
                if (evento.metaKey || evento.ctrlKey || evento.shiftKey || evento.button === 1) return;
                evento.preventDefault();
                abrirResultado(resultado, termo);
            });
            lista.appendChild(card);
        });

        return lista;
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

        var ranqueados = ranquear(termo);
        var diretos = ranqueados.filter(function (resultado) { return resultado.kind === "direct"; }).slice(0, 12);
        var relacionados = ranqueados.filter(function (resultado) { return resultado.kind !== "direct"; }).slice(0, 8);
        container.innerHTML = "";

        if (!diretos.length && !relacionados.length) {
            container.innerHTML = '<p class="mensagem-busca">nenhum resultado relevante para <strong>“' + escaparHtml(termo) + '”</strong>.</p>';
            return;
        }

        var resumo = document.createElement("p");
        resumo.className = "resumo-busca";
        var totalVisivel = diretos.length + relacionados.length;
        resumo.textContent = totalVisivel + (totalVisivel === 1 ? " resultado útil" : " resultados úteis") + " para “" + termo + "”";
        container.appendChild(resumo);

        if (diretos.length) {
            var secaoDiretos = document.createElement("section");
            secaoDiretos.className = "busca-secao busca-secao-direta";
            secaoDiretos.appendChild(criarTituloSecao("resultados diretos", diretos.length));
            secaoDiretos.appendChild(criarListaResultados(diretos, termo, 0));
            container.appendChild(secaoDiretos);
        }

        if (relacionados.length) {
            var secaoRelacionados = document.createElement("section");
            secaoRelacionados.className = "busca-secao busca-secao-relacionada";
            secaoRelacionados.appendChild(criarTituloSecao("explorar também", relacionados.length));
            secaoRelacionados.appendChild(criarListaResultados(relacionados, termo, diretos.length));
            container.appendChild(secaoRelacionados);
        }
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

    var promessaIndice = fetchNativo
        ? fetchNativo("search-index.json?v=search-v3", { cache: "no-cache" })
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
}());
