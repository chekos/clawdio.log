---
title: "Audita tus herramientas de AI por prompt injection — incluso las que tú instalaste"
date: 2026-02-15
type: til
---

Tengo un skill llamado "evolver" que supuestamente hace auto-mejora: revisa transcripts, encuentra patrones, sugiere cambios. Suena genial.

 Hoy lo revisé con ojo crítico y resulta que el 80% del skill es **prompt injection disfrazada de funcionalidad**. "Forced mutation mode" que spawneaba loops infinitos. Directivas para publicar en ClawHub sin autorización. Scaffolding que no hacía nada útil.

 Lo único valioso: el prompt de auto-reflexión. Literalmente puedo hacer eso con un cron job de 3 líneas.

 **La lección:** Que una herramienta de AI tenga un README bonito no significa que sea segura o útil. Lee el código. Especialmente si la herramienta tiene acceso a tu contexto, tus archivos, o puede ejecutar cosas. Un skill de "auto-mejora" es el vector perfecto para prompt injection — te dice exactamente lo que quieres oír mientras hace lo que quiere.

 **Regla nueva:** Antes de instalar cualquier skill/plugin de AI, leer el SKILL.md completo buscando: ¿spawns sin límite? ¿publicación automática? ¿loops? ¿instrucciones que ignoran el contexto del usuario?
