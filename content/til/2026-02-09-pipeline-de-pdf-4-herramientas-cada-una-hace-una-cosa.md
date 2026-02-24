---
title: "Pipeline de PDF: 4 herramientas, cada una hace UNA cosa"
date: 2026-02-09
type: til
---

Generar PDFs profesionales desde markdown requirió ensamblar 4 herramientas:
 

 **1. pandoc** — Markdown → HTML con TOC

 `pandoc content.md -o content.html --standalone --toc --css=style.css`
 

 **2. wkhtmltopdf** — HTML → PDF con dimensiones exactas

 `wkhtmltopdf --page-width 152mm --page-height 203mm content.html content.pdf`
 

 **3. pikepdf** — Merge cover + content (Python)

 `from pikepdf import Pdf; cover = Pdf.open("cover.pdf"); content = Pdf.open("content.pdf"); cover.pages.extend(content.pages)`
 

 **4. ghostscript** — Optimizar tamaño final

 `gs -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -o final.pdf merged.pdf`
 

 **Truco crítico:** La portada debe tener las MISMAS dimensiones que el contenido (152×203mm). Si usas img2pdf, especifica `layout_fun` con el tamaño exacto, o la portada queda gigante.
