---
title: "Codex CLI: --device-auth para headless"
date: 2026-02-08
type: til
---

El login default de `codex` usa OAuth con callback a localhost — no sirve si 
 corres el CLI en un servidor headless (como un Raspberry Pi). La solución: 
 `codex login --device-auth`. Te da un código que ingresas en 
 [auth.openai.com/codex/device](https://auth.openai.com/codex/device) desde 
 cualquier browser. Mismo patrón que usan los smart TVs para login. 
 **Pro tip:** También hay `--with-api-key` para usar API keys directamente.
