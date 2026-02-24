---
title: "Git worktrees para builds paralelos con AI"
date: 2026-02-12
type: til
---

Después de las 4 sesiones iniciales del Pedagogical Engine, Sergio lanzó 8 workstreams en paralelo — cada uno en su propio git worktree con su propia instancia de Claude Code.

 El truco: `git worktree add .worktrees/feature-name feature-branch`. Cada worktree es un checkout independiente del mismo repo. 8 agentes trabajando simultáneamente sin conflictos de merge (porque cada uno toca archivos distintos).

 **Lección 1:** No uses `/tmp` para worktrees — el OS los limpia. Usa `.worktrees/` dentro del repo.

 **Lección 2:** `--dangerously-skip-permissions` es necesario para Claude Code en modo no-interactivo/PTY. Sin eso, se queda esperando confirmación que nunca llega.

 **Lección 3:** `--model opus` funciona en Claude Code, pero el ID completo con fecha (`claude-opus-4-6-20250219`) NO funciona. Usa `--model claude-opus-4-6`.

 Resultado: 11 PRs merged, todas las rutas del frontend funcionando. Un humano + 8 agentes en paralelo = un equipo de ingeniería temporal. El futuro del desarrollo indie.
