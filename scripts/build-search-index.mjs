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

function normalizar(valor = "") {
  return String(valor)
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/\\/g, "/")
    .replace(/\.md$/i, "")
    .replace(/\s+/g, " ")
    .trim();
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

function limparHeading(texto) {
  return texto
    .replace(/\s+#+\s*$/, "")
    .replace(/[*_`~=]/g, "")
    .trim();
}

function extrairHeadingData(markdown) {
  return markdown
    .split(/\r?\n/)
    .map(linha => linha.match(/^(#{1,6})\s+(.+)$/))
    .filter(Boolean)
    .map(match => ({ level: match[1].length, text: limparHeading(match[2]) }))
    .filter(item => item.text);
}

function limparReferenciaWiki(valor) {
  let referencia = String(valor || "").trim();
  const wiki = referencia.match(/^\[\[([\s\S]+)\]\]$/);
  if (wiki) referencia = wiki[1];
  referencia = referencia.split("|")[0].split("#")[0].trim();
  return referencia.replace(/^\.\//, "").replace(/\.md$/i, "").trim();
}

const artigos = listarMarkdowns(raiz)
  .map(caminhoAbsoluto => {
    const sourcePath = path.relative(raiz, caminhoAbsoluto).split(path.sep).join("/");
    const markdown = fs.readFileSync(caminhoAbsoluto, "utf8");
    const frontmatter = extrairFrontmatter(markdown);
    const nomeArquivo = path.basename(sourcePath, ".md");
    const categoria = sourcePath.includes("/") ? sourcePath.split("/")[0] : "00. Geral";
    const headingData = extrairHeadingData(markdown);

    return {
      title: extrairCampoTexto(frontmatter, "title") || nomeArquivo,
      fileTitle: nomeArquivo,
      category: categoria,
      sourcePath,
      tags: extrairLista(frontmatter, "tags"),
      aliases: extrairLista(frontmatter, "aliases"),
      headings: headingData.map(item => item.text),
      headingData,
      relatedRaw: extrairLista(frontmatter, "relacionados"),
      plainText: limparMarkdown(markdown)
    };
  })
  .sort((a, b) => a.sourcePath.localeCompare(b.sourcePath, "pt-BR", { numeric: true, sensitivity: "base" }));

const porCaminho = new Map();
const porNome = new Map();

for (const artigo of artigos) {
  porCaminho.set(normalizar(artigo.sourcePath), artigo);
  porCaminho.set(normalizar(artigo.sourcePath.replace(/\.md$/i, "")), artigo);

  const chavesNome = [artigo.fileTitle, artigo.title].map(normalizar).filter(Boolean);
  for (const chave of chavesNome) {
    if (!porNome.has(chave)) porNome.set(chave, []);
    porNome.get(chave).push(artigo);
  }
}

function resolverRelacionado(origem, referenciaBruta) {
  const referencia = limparReferenciaWiki(referenciaBruta);
  if (!referencia) return null;

  const porPath = porCaminho.get(normalizar(referencia));
  if (porPath) return porPath;

  const nome = normalizar(referencia.split("/").pop());
  const candidatos = porNome.get(nome) || [];
  if (candidatos.length === 1) return candidatos[0];

  const mesmaCategoria = candidatos.find(item => item.category === origem.category);
  return mesmaCategoria || candidatos[0] || null;
}

for (const artigo of artigos) {
  artigo.related = [...new Set(
    artigo.relatedRaw
      .map(referencia => resolverRelacionado(artigo, referencia))
      .filter(Boolean)
      .map(item => item.sourcePath)
  )];
  artigo.backlinks = [];
  delete artigo.relatedRaw;
}

const porSourcePath = new Map(artigos.map(artigo => [artigo.sourcePath, artigo]));
for (const artigo of artigos) {
  for (const destino of artigo.related) {
    const relacionado = porSourcePath.get(destino);
    if (relacionado && !relacionado.backlinks.includes(artigo.sourcePath)) {
      relacionado.backlinks.push(artigo.sourcePath);
    }
  }
}

const indice = {
  version: 3,
  articleCount: artigos.length,
  articles: artigos
};

fs.writeFileSync(path.join(raiz, "search-index.json"), JSON.stringify(indice));
console.log(`Índice de busca v3 gerado com ${artigos.length} artigos.`);
