// js/mermaid.js - Subsistema de Renderização e Exploração de Diagramas Mermaid

/**
 * Configura as opções da engine Mermaid com base no tema atual (claro/escuro).
 * Utiliza htmlLabels: false para garantir renderização puramente vetorial e evitar clipping de foreignObject.
 */
export function configurarMermaid() {
    if (typeof mermaid === "undefined") return;

    const temaEscuro = document.documentElement.dataset.theme !== "light";
    mermaid.initialize({
        startOnLoad: false,
        theme: "base",
        fontFamily: "Archivo, sans-serif",
        fontSize: 14,
        flowchart: {
            curve: "linear",
            defaultRenderer: "dagre-wrapper",
            htmlLabels: false,
            nodeSpacing: 46,
            rankSpacing: 52,
            padding: 18
        },
        themeVariables: temaEscuro ? {
            fontFamily: "Archivo, sans-serif",
            fontSize: "14px",
            darkMode: true,
            background: "#111111",
            primaryColor: "#1c1c1e",
            primaryTextColor: "#f5f5f7",
            primaryBorderColor: "#3395ff",
            lineColor: "#8e9bb0",
            secondaryColor: "#141416",
            tertiaryColor: "#1e2229"
        } : {
            fontFamily: "Archivo, sans-serif",
            fontSize: "14px",
            darkMode: false,
            background: "#ffffff",
            primaryColor: "#f1f5f9",
            primaryTextColor: "#0f172a",
            primaryBorderColor: "#0056b3",
            lineColor: "#475569",
            secondaryColor: "#f8fafc",
            tertiaryColor: "#e2e8f0"
        }
    });
}

/**
 * Abre o explorador interativo em tela cheia para inspecionar o diagrama selecionado.
 * Implementa sistema de coordenadas único, centralização geométrica e contenção estrita.
 * Remove todos os event listeners ao fechar para evitar memory leaks.
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
    stage.appendChild(cloneSvg);

    document.body.appendChild(modal);

    const zoomDisplay = modal.querySelector(".mermaid-modal-zoom-display");
    const body = modal.querySelector(".mermaid-modal-body");

    // 1. Sistema Único de Coordenadas:
    // Medir dimensões do SVG clonado já inserido na DOM após carregamento de fontes
    let baseWidth = 800;
    let baseHeight = 600;

    if (cloneSvg.viewBox && cloneSvg.viewBox.baseVal && cloneSvg.viewBox.baseVal.width > 0) {
        baseWidth = cloneSvg.viewBox.baseVal.width;
        baseHeight = cloneSvg.viewBox.baseVal.height;
    } else {
        try {
            const bbox = cloneSvg.getBBox();
            if (bbox.width > 0 && bbox.height > 0) {
                baseWidth = bbox.width;
                baseHeight = bbox.height;
            }
        } catch (_) {
            const rect = cloneSvg.getBoundingClientRect();
            if (rect.width > 0 && rect.height > 0) {
                baseWidth = rect.width;
                baseHeight = rect.height;
            }
        }
    }

    // Fixar o stage nas dimensões exatas de base e forçar SVG a preenchê-lo
    stage.style.width = `${Math.ceil(baseWidth)}px`;
    stage.style.height = `${Math.ceil(baseHeight)}px`;
    cloneSvg.style.width = "100%";
    cloneSvg.style.height = "100%";
    cloneSvg.style.maxWidth = "none";
    cloneSvg.style.maxHeight = "none";

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
        // Margem de segurança confortável de 48px por margem (96px total por eixo)
        const margemX = 96;
        const margemY = 96;

        const availW = Math.max(160, bodyRect.width - margemX);
        const availH = Math.max(160, bodyRect.height - margemY);

        const scaleX = availW / baseWidth;
        const scaleY = availH / baseHeight;

        let fit = Math.min(scaleX, scaleY);

        // Permitir que diagramas pequenos ocupem confortavelmente a viewport (até 4.5x)
        fit = Math.min(Math.max(0.15, fit), 4.5);

        return fit;
    }

    function executarFit() {
        modoFitAtivo = true;
        transladoX = 0;
        transladoY = 0;
        escala = calcularEscalaFit();
        aplicarTransformacao();

        // Validação Programática de Contenção (Garantia Estrita sem Clipping)
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

    // Limpeza rigorosa de todos os listeners para evitar acúmulo em memória
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
 */
export function renderizarDiagramasMermaid(container) {
    if (typeof mermaid === "undefined" || !container) return;
    configurarMermaid();

    const diagramas = container.querySelectorAll(".mermaid");
    diagramas.forEach(diagrama => {
        const codigo = diagrama.dataset.mermaidSource || diagrama.textContent;
        diagrama.dataset.mermaidSource = codigo;
        diagrama.removeAttribute("data-processed");
        diagrama.textContent = codigo;
    });

    mermaid.run({ nodes: diagramas }).then(() => {
        equiparDiagramasMermaidInterativos(container);
    }).catch(err => {
        console.error("Erro ao renderizar Mermaid:", err);
    });
}
