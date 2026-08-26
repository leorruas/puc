# Design QA — 2026-08-26

## Escopo

- Página inicial organizada por matérias, com “geral” e “sintaxe multilinguagem” como entrada.
- Busca, listas de artigos, navegação sequencial e retorno à matéria preservados.
- Direção visual alinhada ao Guia do Portal IFMG: tipografia e números como índice editorial, filetes, pouco preenchimento e fundo contínuo.
- Na capa, “ads” é o elemento tipográfico dominante; “puc minas” atua como assinatura menor.
- As notas são carregadas pela cópia pública do repositório para que a página aberta diretamente no vault também preencha as matérias.
- Diagramas Mermaid usam paletas contrastadas por tema e são redesenhados quando o tema muda.
- Diagramas usam geometria reta e filetes finos para acompanhar a linguagem editorial do leitor.
- Rótulos internos usam 16 px no desktop e 14 px em telas compactas, com espaçamento padronizado entre nós.
- Glossários extraem o índice temático do Markdown e o exibem como navegação por grupos; a barra lateral mostra apenas esses grupos e as seções editoriais, não cada verbete.

## Resultado

**passed** — A alteração foi conferida por revisão de estrutura e estilos: o índice do glossário não vaza sintaxe Markdown, mantém os atalhos para os verbetes e reduz a navegação lateral a uma escala legível.
