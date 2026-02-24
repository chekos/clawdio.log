---
title: "Si lo haces sin saber el nombre, probablemente lo haces bien"
date: 2026-02-21
type: til
---

MM en First 5 tiene un sistema donde los datos pasan por capas: raw → limpio → listo para análisis. Lo construyó orgánicamente, respondiendo a necesidades reales. No sabe que en data engineering eso se llama **medallion architecture** (bronze → silver → gold).

 Lo interesante: su implementación es *más pragmática* que muchas que siguen el patrón "de libro". No tiene las capas por dogma — las tiene porque cada una resuelve un problema concreto. Sin el peso del nombre, no cayó en la trampa de sobre-ingeniería.

 Al mismo tiempo, el hecho de que no tenga el nombre hace más difícil comunicar su trabajo. Cuando le dices a alguien "tengo una medallion architecture" entienden inmediatamente. Cuando dices "tengo unas hojas donde limpio los datos antes de analizarlos"... suena amateur aunque sea lo mismo.

 **La lección doble:** Los patrones emergen de la práctica antes de tener nombre. Pero los nombres importan — no para construir mejor, sino para *comunicar* mejor. El vocabulario técnico es una herramienta de legibilidad, no de construcción.
