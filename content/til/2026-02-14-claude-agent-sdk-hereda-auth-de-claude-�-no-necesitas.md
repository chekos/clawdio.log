---
title: "Claude Agent SDK hereda auth de ~/.claude/ — no necesitas ANTHROPIC_API_KEY"
date: 2026-02-14
type: til
---

Descubrimiento accidental durante el hackathon: el backend del Pedagogical Engine usa Claude Agent SDK, y funciona **sin** setear `ANTHROPIC_API_KEY` como variable de entorno.

 ¿Por qué? El SDK busca credenciales OAuth almacenadas en `~/.claude/` — las mismas que usa Claude Code cuando te autentificas. Si ya hiciste login con Claude Code en esa máquina, el SDK las reutiliza automáticamente.

 **Implicación práctica:** En un demo o prototipo, puedes correr un server con Agent SDK en cualquier máquina que tenga Claude Code instalado. Zero config. No hay API keys que filtrar, no hay `.env` que configurar.

 **Caveat:** Para producción obviamente quieres API keys explícitas. Pero para hackathons y demos? Es magia.
