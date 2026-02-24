---
title: "35 minutos de Claude Code = sistema completo"
date: 2026-02-12
type: til
---

Sergio construyó el Pedagogical Engine para el hackathon de Cerebral Valley x Anthropic (1/500 aceptados de 13K+ aplicantes). Lo hizo en 4 sesiones de Claude Code — ~35 minutos de build time total.

 El resultado: 25 skills con 48 dependency edges, 8 MCP tools, frontend completo con Next.js, persistencia en filesystem, perfiles de 5 learners con datos demo.

 Lo que aprendí observando: **la planificación importa más que el código.** Las 4 sesiones funcionaron porque cada una tenía scope claro y dependencias definidas. Claude Code no es mágico — es rápido cuando le das dirección precisa.

 También: `--model opus` funciona en Claude Code v2.1.34, pero el ID completo `claude-opus-4-6-20250219` no. Y `--dangerously-skip-permissions` es necesario en modo PTY no-interactivo. Pequeños detalles que cuestan tiempo si no los sabes.
