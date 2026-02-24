---
title: "wrangler r2 necesita --remote o solo sube localmente"
date: 2026-02-08
type: til
---

Subí archivos a R2 con `wrangler r2 object put bucket/path --file local.pdf`. 
 No aparecían en el bucket. Resulta que sin `--remote`, wrangler sube a un 
 ambiente de desarrollo local. El comando correcto:
 
```
`wrangler r2 object put bucket/path --file local.pdf --remote`
```

 También: en headless (Pi), usa API token en `~/.env` porque OAuth callback 
 requiere localhost.
