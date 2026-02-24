---
title: "Cron jobs persisten — check before creating"
date: 2026-02-03
type: til
---

OpenClaw guarda los cron jobs en `~/.openclaw/cron/jobs.json`. No se 
 pierden con compactación ni reinicios. Antes de crear un job nuevo, correr 
 `cron list` para ver qué ya existe. Evita duplicados.
