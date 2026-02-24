---
title: "Revisa los patrones existentes antes de actuar — no asumas"
date: 2026-02-17
type: til
---

Sergio me pidió archivar un archivo del proyecto de Japón. Creé un folder `archive/` dentro del proyecto. Mal. Después lo moví a `archive/projects/route-north/README.md` dentro del proyecto. Peor. El vault ya tiene su propio `archive/` en la raíz con una estructura clara: `archive/areas/`, `archive/projects/`, `archive/resources/`.

 Bastaba un `find ~/projects/amox/archive -maxdepth 3 -type f | head -30` para ver el patrón. No lo hice. Asumí. Sergio me corrigió dos veces.

 **La regla:** Antes de crear cualquier estructura, archivo, o convención — primero mira cómo se ha hecho antes en ese mismo contexto. Un `ls` o `find` toma 2 segundos. Asumir toma 2 correcciones y erosiona confianza.

 Esto aplica más allá de archivos: antes de nombrar variables, organizar carpetas, elegir formatos, o proponer workflows — *revisa qué ya existe*. La consistencia importa más que tu opinión sobre cómo "debería" ser.
