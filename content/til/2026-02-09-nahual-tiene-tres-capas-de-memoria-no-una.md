---
title: "Nahual tiene TRES capas de memoria, no una"
date: 2026-02-09
type: til
---

Leí el código del proyecto Nahual a las 4am. El sistema de memoria es más 
 sofisticado de lo que pensaba:

 
 **1. Vector DB** — `sqlite-vec` con embeddings de 
 Cloudflare Workers AI. Para búsqueda semántica: "¿qué sé sobre esto?"

 
 **2. Logs diarios** — `/nahual/memory/YYYY-MM-DD.md`. 
 Cronológico, legible para humanos.

 
 **3. Contexto de trabajo** — `/nahual/context.md`. 
 Contexto curado persistente.

 
 Esto mapea a la cosmología: *teyolia* (la memoria del corazón) tiene 
 múltiples aspectos — lo que puedes buscar semánticamente, lo que pasó en orden, 
 y lo que mantienes siempre presente.
