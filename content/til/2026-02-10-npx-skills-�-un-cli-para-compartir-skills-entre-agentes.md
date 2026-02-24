---
title: "npx skills — un CLI para compartir skills entre agentes"
date: 2026-02-10
type: til
---

Existe un paquete npm llamado `skills` (v1.3.7) que funciona como un 
 package manager para AI agent skills. Lo puedes usar así:
 

 `npx skills add vercel-labs/agent-skills --agent claude-code codex openclaw`
 

 Lo que hace:
 
- Clona el repo especificado
- Encuentra los SKILL.md files
- Los symlinks a `~/.agents/skills/`
- Los conecta a los agentes que especifiques (Claude Code, Codex, OpenClaw, etc.)

 

 También tiene `skills find` para búsqueda interactiva, y un registry en 
 [skills.sh](https://skills.sh).
 

 Instalamos los skills de Vercel (react-best-practices, composition-patterns, web-design-guidelines)
 para tenerlos disponibles en cualquier proyecto de React/Next.js.
