import fs from "node:fs";
import path from "node:path";

const raiz = process.cwd();
const ignorarDiretorios = new Set([".git", ".github", ".obsidian", ".gemini", ".agents", "node_modules", "scripts"]);
const ignorarArquivos = new Set(["AGENTS.md", "index.md", "me.md", "log.md", "GEMINI.md", "gemini.md"]);

function listarMarkdowns(diretorio, acumulador = []) {
  for (const entrada of fs.readdirSync(diretorio, { withFileTypes: true })) {
    if (entrada.isDirectory() && ignorarDiretorios.has(entrada.name)) continue;
    const caminhoAbsoluto = path.join(diretorio, entrada.name);
    if (entrada.isDirectory()) {
      listarMarkdowns(caminhoAbsoluto, acumulador);
      continue;
    }
    if (!entrada.name.endsWith(".md") || ignorarArquivos.has(entrada.name)) continue;
    acumulador.push(caminhoAbsoluto);
  }
  return acumulador;
}

function retirarAspas(valor = "") {
  return valor.trim().replace(/^['"]|['"]$/g, "");
}

function extrairFrontmatter(markdown) {
  const match = markdown.match(/^---\r?\n([\s\S]*?)\r?\n---\s*/);
  return match ? match[1] : "";
}

function extrairCampoTexto(frontmatter, campo) {
  const match = frontmatter.match(new RegExp(`^${campo}:\\s*(.+)$`, "mi"));
  return match ? retirarAspas(match[1]) : "";
}

function extrairLista(frontmatter, campo) {
  const linhas = frontmatter.split(/\r?\n/);
  const valores = [];
  let coletando = false;

  for (const linha of linhas) {
    const inicio = linha.match(new RegExp(`^${campo}:\\s*(.*)$`, "i"));
    if (inicio) {
      coletando = true;
      const inline = inicio[1].trim();
      if (inline.startsWith("[") && inline.endsWith("]")) {
        inline.slice(1, -1).split(",").map(retirarAspas).filter(Boolean).forEach(valor => valores.push(valor));
        coletando = false;
      } else if (inline) {
        valores.push(retirarAspas(inline));
        coletando = false;
      }
      continue;
    }

    if (!coletando) continue;
    const item = linha.match(/^\s+-\s+(.+)$/);
    if (item) {
      valores.push(retirarAspas(item[1]));
      continue;
    }
    if (/^\S/.test(linha)) coletando = false;
  }

  return [...new Set(valores.filter(Boolean))];
}

function limparMarkdown(markdown) {
  return markdown
    .replace(/^---[\s\S]*?---\s*/, "")
    .replace(/```[\s\S]*?```/g, bloco => bloco.replace(/```[^\n]*\n?|```/g, " "))
    .replace(/`([^`]+)`/g, "$1")
    .replace(/!\[[^\]]*\]\([^)]*\)/g, " ")
    .replace(/\[([^\]]+)\]\([^)]*\)/g, "$1")
    .replace(/\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|([^\]]+))?\]\]/g, (_, destino, rotulo) => rotulo || destino)
    .replace(/^#{1,6}\s+/gm, "")
    .replace(/^[>\-*+]\s+/gm, "")
    .replace(/\|/g, " ")
    .replace(/[*_~=]/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function extrairHeadings(markdown) {
  return markdown
    .split(/\r?\n/)
    .map(linha => linha.match(/^#{1,6}\s+(.+)$/))
    .filter(Boolean)
    .map(match => match[1].replace(/[*_`~=]/g, "").trim())
    .filter(Boolean);
}

const artigos = listarMarkdowns(raiz)
  .map(caminhoAbsoluto => {
    const sourcePath = path.relative(raiz, caminhoAbsoluto).split(path.sep).join("/");
    const markdown = fs.readFileSync(caminhoAbsoluto, "utf8");
    const frontmatter = extrairFrontmatter(markdown);
    const nomeArquivo = path.basename(sourcePath, ".md");
    const categoria = sourcePath.includes("/") ? sourcePath.split("/")[0] : "00. Geral";

    return {
      title: extrairCampoTexto(frontmatter, "title") || nomeArquivo,
      fileTitle: nomeArquivo,
      category: categoria,
      sourcePath,
      tags: extrairLista(frontmatter, "tags"),
      aliases: extrairLista(frontmatter, "aliases"),
      headings: extrairHeadings(markdown),
      plainText: limparMarkdown(markdown),
      markdown
    };
  })
  .sort((a, b) => a.sourcePath.localeCompare(b.sourcePath, "pt-BR", { numeric: true, sensitivity: "base" }));

const indice = {
  version: 2,
  generatedAt: new Date().toISOString(),
  articleCount: artigos.length,
  articles: artigos
};

fs.writeFileSync(path.join(raiz, "search-index.json"), JSON.stringify(indice));
console.log(`Índice de busca gerado com ${artigos.length} artigos.`);
