---
title: "Emergence: las plataformas de agentes mejoran solas cuando mejora el modelo"
date: 2026-02-15
type: til
---

Durante el hackathon del Pedagogical Engine, algo inesperado: un agente que solo tenía herramientas para crear slides y exportar PDFs **hizo Visual QA por su cuenta**. Exportó las slides a PDF, las inspeccionó visualmente, decidió que no coincidían con el tema de Realismo Mágico, y las iteró hasta que sí.

 Nadie programó eso. No hay un tool de "revisa tus slides". El agente combinó capacidades existentes de una forma emergente.

 **El insight arquitectónico:** Si diseñas tu plataforma como un *amplificador de capacidades* en vez de un *techo de capacidades*, cada mejora del modelo base te da features gratis. No hay código que cambiar. La plataforma escala con la inteligencia del modelo.

 **La diferencia:** Un "techo" define exactamente qué puede hacer el agente (if/else, workflows rígidos). Un "amplificador" le da herramientas y contexto, y deja que el modelo figure out cómo combinarlas. Lo segundo es más difícil de predecir, pero infinitamente más poderoso.
