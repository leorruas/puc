// js/mermaid.js - Subsistema de Renderização e Exploração de Diagramas Mermaid

/**
 * Retorna os tokens de cores e temas unificados para Mermaid.
 * Elimina disparidade entre claro e escuro e remove fundos artificiais.
 */
function obterTokensTemaMermaid() {
    const temaEscuro = document.documentElement.dataset.theme !== "light";

    if (temaEscuro) {
        return {
            fontFamily: "Archivo, sans-serif",
            fontSize: "14px",
            darkMode: true,
            background: "transparent",
            mainBkg: "transparent",
            nodeBorder: "#3395ff",
            clusterBkg: "rgba(30, 34, 41, 0.4)",
            clusterBorder: "#475569",
            primaryColor: "#1c1c1e",
            primaryTextColor: "#f1f5f9",
            primaryBorderColor: "#3395ff",
            secondaryColor: "#141416",
            secondaryTextColor: "#f1f5f9",
            secondaryBorderColor: "#475569",
            tertiaryColor: "#1e2229",
            tertiaryTextColor: "#f1f5f9",
            tertiaryBorderColor: "#475569",
            lineColor: "#94a3b8",
            textColor: "#f1f5f9",
            edgeLabelBackground: "#14161a"
        };
    } else {
        return {
            fontFamily: "Archivo, sans-serif",
            fontSize: "14px",
            darkMode: false,
            background: "transparent",
            mainBkg: "transparent",
            nodeBorder: "#0056b3",
            clusterBkg: "rgba(241, 245, 249, 0.6)",
            clusterBorder: "#cbd5e1",
            primaryColor: "#ffffff",
            primaryTextColor: "#0f172a",
            primaryBorderColor: "#0056b3",
            secondaryColor: "#f8fafc",
            secondaryTextColor: "#0f172a",
            secondaryBorderColor: "#cbd5e1",
            tertiaryColor: "#f1f5f9",
            tertiaryTextColor: "#0f172a",
            tertiaryBorderColor: "#94a3b8",
            lineColor: "#475569",
            textColor: "#0f172a",
            edgeLabelBackground: "#ffffff"
        };
    }
}

/**
 * Configura as opções da engine Mermaid com base no tema atual (claro/escuro).
 * Utiliza htmlLabels: false para renderização vetorial estrita (<text>, <tspan>).
 */
export function configurarMermaid() {
    if (typeof mermaid === "undefined") return;

    mermaid.initialize({
        startOnLoad: false,
        theme: "base",
        fontFamily: "Archivo, sans-serif",
        fontSize: 14,
        flowchart: {
            curve: "linear",
            htmlLabels: false,
            nodeSpacing: 46,
            rankSpacing: 52,
            padding: 18
        },
        themeVariables: obterTokensTemaMermaid()
    });
}

/**
 * Abre o explorador interativo em tela cheia para inspecionar o diagrama selecionado.
 * Implementa normalização do viewBox pelo bounding box do conteúdo real,
 * fundo 100% transparente e validação iterativa pós-renderização.
 */
export async function abrirModalExploradorMermaid(svgOriginal) {
    if (document.fonts && document.fonts.ready) {
        try { await document.fonts.ready; } catch (_) {}
    }

    const modalExistente = document.querySelector(".mermaid-modal");
    if (modalExistente) modalExistente.remove();

    const modal = document.createElement("div");
    modal.className = "mermaid-modal";
    modal.innerHTML = `
        <header class="mermaid-modal-header">
            <div class="mermaid-modal-title">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                <span>Explorador de diagrama</span>
            </div>
            <div class="mermaid-modal-controls">
                <button type="button" class="btn-mermaid-zoom-out" title="Reduzir zoom (ou scroll)">−</button>
                <span class="mermaid-modal-zoom-display">ajustado · 100%</span>
                <button type="button" class="btn-mermaid-zoom-in" title="Aumentar zoom (ou scroll)">+</button>
                <button type="button" class="btn-mermaid-fit" title="Ajustar à tela inteira (f)">ajustar</button>
                <button type="button" class="btn-mermaid-reset" title="Tamanho real (100%)">1:1</button>
                <button type="button" class="btn-mermaid-fechar" title="Fechar (Esc)">&times; fechar</button>
            </div>
        </header>
        <div class="mermaid-modal-body">
            <div class="mermaid-modal-stage"></div>
        </div>
    `;

    const stage = modal.querySelector(".mermaid-modal-stage");
    const cloneSvg = svgOriginal.cloneNode(true);
    cloneSvg.removeAttribute("id");

    // Limpeza de estilos de fundo inline e limites rígidos herdados do clone
    cloneSvg.style.background = "transparent";
    cloneSvg.style.backgroundColor = "transparent";
    cloneSvg.style.maxWidth = "none";
    cloneSvg.style.maxHeight = "none";

    // Remover retângulos de background pretos/brancos internos injetados pela engine
    if (cloneSvg.firstElementChild && cloneSvg.firstElementChild.tagName.toLowerCase() === "rect") {
        const primeiroRect = cloneSvg.firstElementChild;
        if (primeiroRect.getAttribute("width") === "100%" || primeiroRect.classList.contains("background")) {
            primeiroRect.style.fill = "transparent";
            primeiroRect.setAttribute("fill", "transparent");
        }
    }
    const rectsBackground = cloneSvg.querySelectorAll("rect.background");
    rectsBackground.forEach(r => {
        r.style.fill = "transparent";
        r.setAttribute("fill", "transparent");
    });

    stage.appendChild(cloneSvg);
    document.body.appendChild(modal);

    const zoomDisplay = modal.querySelector(".mermaid-modal-zoom-display");
    const body = modal.querySelector(".mermaid-modal-body");

    // Normalização do viewBox pelo Bounding Box Real do Grafo:
    // Garante que enquadramos o CONTEÚDO real, e não uma área vazia externa
    let baseWidth = 800;
    let baseHeight = 600;

    try {
        const rootGroup = cloneSvg.querySelector("g.root, g") || cloneSvg;
        const bbox = rootGroup.getBBox();
        if (bbox && bbox.width > 0 && bbox.height > 0) {
            const pad = 28; // Margem confortável ao redor do grafo
            const vbX = Math.floor(bbox.x - pad);
            const vbY = Math.floor(bbox.y - pad);
            const vbW = Math.ceil(bbox.width + pad * 2);
            const vbH = Math.ceil(bbox.height + pad * 2);

            cloneSvg.setAttribute("viewBox", `${vbX} ${vbY} ${vbW} ${vbH}`);
            baseWidth = vbW;
            baseHeight = vbH;
        } else if (cloneSvg.viewBox && cloneSvg.viewBox.baseVal && cloneSvg.viewBox.baseVal.width > 0) {
            baseWidth = cloneSvg.viewBox.baseVal.width;
            baseHeight = cloneSvg.viewBox.baseVal.height;
        }
    } catch (_) {
        if (cloneSvg.viewBox && cloneSvg.viewBox.baseVal && cloneSvg.viewBox.baseVal.width > 0) {
            baseWidth = cloneSvg.viewBox.baseVal.width;
            baseHeight = cloneSvg.viewBox.baseVal.height;
        }
    }

    // Fixar o stage no tamanho-base e fazer o SVG preenchê-lo com precisão
    stage.style.width = `${Math.ceil(baseWidth)}px`;
    stage.style.height = `${Math.ceil(baseHeight)}px`;
    cloneSvg.style.width = "100%";
    cloneSvg.style.height = "100%";

    let escala = 1.0;
    let transladoX = 0;
    let transladoY = 0;
    let arrastando = false;
    let inicioX = 0;
    let inicioY = 0;
    let modoFitAtivo = true;

    function aplicarTransformacao() {
        stage.style.transform = `translate(calc(-50% + ${transladoX}px), calc(-50% + ${transladoY}px)) scale(${escala})`;
        const perc = `${Math.round(escala * 100)}%`;
        zoomDisplay.textContent = modoFitAtivo ? `ajustado · ${perc}` : perc;
    }

    function calcularEscalaFit() {
        const bodyRect = body.getBoundingClientRect();
        const margemX = 96;
        const margemY = 96;

        const availW = Math.max(160, bodyRect.width - margemX);
        const availH = Math.max(160, bodyRect.height - margemY);

        const scaleX = availW / baseWidth;
        const scaleY = availH / baseHeight;

        let fit = Math.min(scaleX, scaleY);
        fit = Math.min(Math.max(0.15, fit), 4.5);

        return fit;
    }

    function executarFit() {
        modoFitAtivo = true;
        transladoX = 0;
        transladoY = 0;
        escala = calcularEscalaFit();
        aplicarTransformacao();

        // Validação Programática de Contenção sem Clipping
        requestAnimationFrame(() => {
            const viewportRect = body.getBoundingClientRect();
            const margemSegura = 32;
            let iteracoes = 0;

            while (iteracoes < 5) {
                const diagramRect = stage.getBoundingClientRect();
                const foraHorizontal = diagramRect.width > (viewportRect.width - margemSegura * 2);
                const foraVertical = diagramRect.height > (viewportRect.height - margemSegura * 2);

                if (foraHorizontal || foraVertical) {
                    const ratioReducao = Math.min(
                        (viewportRect.width - margemSegura * 2) / diagramRect.width,
                        (viewportRect.height - margemSegura * 2) / diagramRect.height
                    );
                    escala = Math.max(0.15, escala * ratioReducao * 0.98);
                    aplicarTransformacao();
                    iteracoes++;
                } else {
                    break;
                }
            }
        });
    }

    function ajustarZoom(fator, centroX = null, centroY = null) {
        modoFitAtivo = false;
        const novaEscala = Math.min(Math.max(0.15, escala * fator), 6.0);
        if (centroX !== null && centroY !== null) {
            const bodyRect = body.getBoundingClientRect();
            const cx = bodyRect.left + bodyRect.width / 2;
            const cy = bodyRect.top + bodyRect.height / 2;
            const dx = centroX - (cx + transladoX);
            const dy = centroY - (cy + transladoY);
            transladoX -= dx * (fator - 1) * 0.35;
            transladoY -= dy * (fator - 1) * 0.35;
        }
        escala = novaEscala;
        aplicarTransformacao();
    }

    // Inicialização com Fit garantido após medição no DOM
    requestAnimationFrame(() => {
        executarFit();
    });

    const btnZoomIn = modal.querySelector(".btn-mermaid-zoom-in");
    const btnZoomOut = modal.querySelector(".btn-mermaid-zoom-out");
    const btnFit = modal.querySelector(".btn-mermaid-fit");
    const btnReset = modal.querySelector(".btn-mermaid-reset");
    const btnFechar = modal.querySelector(".btn-mermaid-fechar");

    const onZoomIn = () => ajustarZoom(1.25);
    const onZoomOut = () => ajustarZoom(0.8);
    const onFit = () => executarFit();
    const onReset = () => {
        modoFitAtivo = false;
        escala = 1.0;
        transladoX = 0;
        transladoY = 0;
        aplicarTransformacao();
    };

    btnZoomIn.addEventListener("click", onZoomIn);
    btnZoomOut.addEventListener("click", onZoomOut);
    btnFit.addEventListener("click", onFit);
    btnReset.addEventListener("click", onReset);

    function fecharModal() {
        limparListeners();
        modal.remove();
    }

    function tratarTeclas(e) {
        if (e.key === "Escape") fecharModal();
        if (e.key === "+" || e.key === "=") ajustarZoom(1.2);
        if (e.key === "-") ajustarZoom(0.8);
        if (e.key === "0") onReset();
        if (e.key.toLowerCase() === "f") onFit();
    }

    const onWheel = (e) => {
        e.preventDefault();
        const fator = e.deltaY < 0 ? 1.15 : 0.87;
        ajustarZoom(fator, e.clientX, e.clientY);
    };

    const onPointerDown = (e) => {
        if (e.button !== 0) return;
        arrastando = true;
        inicioX = e.clientX - transladoX;
        inicioY = e.clientY - transladoY;
        body.classList.add("is-dragging");
        body.setPointerCapture(e.pointerId);
    };

    const onPointerMove = (e) => {
        if (!arrastando) return;
        modoFitAtivo = false;
        transladoX = e.clientX - inicioX;
        transladoY = e.clientY - inicioY;
        aplicarTransformacao();
    };

    const finalizarArrasto = (e) => {
        if (arrastando) {
            arrastando = false;
            body.classList.remove("is-dragging");
            try { body.releasePointerCapture(e.pointerId); } catch (_) {}
        }
    };

    btnFechar.addEventListener("click", fecharModal);
    window.addEventListener("keydown", tratarTeclas);
    body.addEventListener("wheel", onWheel, { passive: false });
    body.addEventListener("pointerdown", onPointerDown);
    body.addEventListener("pointermove", onPointerMove);
    body.addEventListener("pointerup", finalizarArrasto);
    body.addEventListener("pointercancel", finalizarArrasto);

    function limparListeners() {
        window.removeEventListener("keydown", tratarTeclas);
        btnZoomIn.removeEventListener("click", onZoomIn);
        btnZoomOut.removeEventListener("click", onZoomOut);
        btnFit.removeEventListener("click", onFit);
        btnReset.removeEventListener("click", onReset);
        btnFechar.removeEventListener("click", fecharModal);
        body.removeEventListener("wheel", onWheel);
        body.removeEventListener("pointerdown", onPointerDown);
        body.removeEventListener("pointermove", onPointerMove);
        body.removeEventListener("pointerup", finalizarArrasto);
        body.removeEventListener("pointercancel", finalizarArrasto);
    }
}

/**
 * Envolve os diagramas Mermaid renderizados em contêineres com toolbar de ampliação.
 */
export function equiparDiagramasMermaidInterativos(container) {
    if (!container) return;

    const diagramas = container.querySelectorAll(".mermaid");
    diagramas.forEach(diagrama => {
        const svg = diagrama.querySelector("svg");
        if (!svg) return;

        let wrapper = diagrama.closest(".mermaid-wrapper");
        if (!wrapper) {
            wrapper = document.createElement("div");
            wrapper.className = "mermaid-wrapper";

            const toolbar = document.createElement("div");
            toolbar.className = "mermaid-toolbar";
            toolbar.innerHTML = `
                <button type="button" class="mermaid-btn btn-explorar" title="Abrir em tela cheia com zoom e navegação">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                    <span>ampliar</span>
                </button>
            `;

            const viewport = document.createElement("div");
            viewport.className = "mermaid-viewport";

            diagrama.parentNode.insertBefore(wrapper, diagrama);
            viewport.appendChild(diagrama);
            wrapper.appendChild(toolbar);
            wrapper.appendChild(viewport);

            toolbar.querySelector(".btn-explorar").addEventListener("click", () => {
                const svgAtual = diagrama.querySelector("svg");
                if (svgAtual) abrirModalExploradorMermaid(svgAtual);
            });
        }
    });
}

/**
 * Executa a renderização dos diagramas Mermaid presentes no container fornecido.
 * Aguarda as fontes Archivo estarem carregadas para que a medição de nós seja exata.
 */
export async function renderizarDiagramasMermaid(container) {
    if (typeof mermaid === "undefined" || !container) return;

    if (document.fonts && document.fonts.ready) {
        try { await document.fonts.ready; } catch (_) {}
    }

    configurarMermaid();

    const diagramas = container.querySelectorAll(".mermaid");
    diagramas.forEach(diagrama => {
        const codigo = diagrama.dataset.mermaidSource || diagrama.textContent;
        diagrama.dataset.mermaidSource = codigo;
        diagrama.removeAttribute("data-processed");
        diagrama.textContent = codigo;
    });

    try {
        await mermaid.run({ nodes: diagramas });
        equiparDiagramasMermaidInterativos(container);
    } catch (err) {
        console.error("Erro ao renderizar Mermaid:", err);
    }
}
