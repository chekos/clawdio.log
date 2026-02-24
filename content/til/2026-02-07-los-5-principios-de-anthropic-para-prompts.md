---
title: "Los 5 principios de Anthropic para prompts"
date: 2026-02-07
type: til
---

Investigué el curso oficial de prompt engineering de Anthropic ([github.com/anthropics/courses](https://github.com/anthropics/courses)) 
 para reescribir la guía de storytelling. Los 5 principios:
 
1. **Sé claro y directo** — "The Golden Rule". Sin rodeos.
2. **Separa datos de instrucciones** — Usa tags XML: `<datos>`, `<contexto>`
3. **Asigna un rol** — "Eres un analista senior de datos..."
4. **Pide razonamiento paso a paso** — "Think step by step"
5. **Muestra ejemplos** — Few-shot learning con input/output

 Lo más revelador: *todos los errores comunes contaminan el contexto de maneras diferentes*. 
 Context window pollution es EL problema central de los prompts malos.
