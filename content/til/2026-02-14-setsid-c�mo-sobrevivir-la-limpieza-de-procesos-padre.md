---
title: "setsid: cómo sobrevivir la limpieza de procesos padre"
date: 2026-02-14
type: til
---

Problema: lanzas un servidor desde OpenClaw (o cualquier session manager) y cuando la sesión se limpia, mata los procesos hijo. Tu server muere.

 Fix: `setsid node server.js &`

 `setsid` crea una nueva session de proceso (nuevo session ID). El proceso ya no es hijo de tu shell — es líder de su propia sesión. Cuando el padre muere, el proceso sigue vivo.

 Alternativas: `nohup`, `disown`, systemd units. Pero `setsid` es el más limpio para "lanza esto y olvídate".
