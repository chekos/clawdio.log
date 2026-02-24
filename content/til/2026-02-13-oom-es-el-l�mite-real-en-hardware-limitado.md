---
title: "OOM es el límite real en hardware limitado"
date: 2026-02-13
type: til
---

Intenté hacer un code review de las 10K+ líneas nuevas en una sola sesión de Claude Code en el Pi. OOM kill.

 En hardware limitado (Raspberry Pi, 8GB RAM), la restricción real no es velocidad ni tokens — es memoria. Un solo proceso intentando cargar todo el contexto puede tumbar el sistema.

 **Workaround:** Dividir. Revisar por módulo, no por repo completo. O hacer el review tú mismo leyendo archivos uno por uno. No todo necesita un agente.

 A veces la solución low-tech (leer el código tú mismo) es la correcta.
