---
title: "Pipelines autónomos que se auto-reparan"
date: 2026-02-13
type: til
---

Anoche corrimos un pipeline de 9 moonshots para el Pedagogical Engine: 4.5 horas autónomas (10pm → 2:42am). El script lanzaba Claude Code para cada feature, mergeaba a main, y seguía.

 **Se crasheó dos veces.** Claude Code terminaba su trabajo y hacía commit, pero el bash script moría antes del merge step. Sin safety net, esas features se perdían.

 **Fix:** Agregar lógica de skip-already-merged — antes de cada moonshot, checar `git log --oneline main | grep "Moonshot N:"`. Si ya está, skip. Si el commit existe en un branch pero no en main, merge y skip. Así el pipeline es *idempotente* — puedes re-ejecutarlo sin miedo.

 **Resultado:** 28 MCP tools, 21 rutas frontend, ~10K líneas. Todo en main. Todo limpio.

 **Lección:** Los pipelines de AI agents van a fallar. Diseña para re-ejecución, no para perfección. Idempotencia > robustez.
