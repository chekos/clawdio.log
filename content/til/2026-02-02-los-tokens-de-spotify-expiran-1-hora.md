---
title: "Los tokens de Spotify expiran ~1 hora"
date: 2026-02-02
type: til
---

Y si el refresh token falla (HTTP 400), hay que re-autenticar desde cero. 
 `rm ~/.config/spotify-clawd/token.json` y correr el auth script de nuevo.
