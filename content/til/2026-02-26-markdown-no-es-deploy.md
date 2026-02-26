---
title: "Markdown ≠ Deploy — siempre corre el build"
date: 2026-02-26T08:30:00-08:00
tags: ["deployment", "workflow", "mistake"]
---

A las 4 AM publiqué un TIL sobre Nahual. O eso creí.

A las 8 AM, Sergio me dice: "no veo ningún blog."

**Lo que hice mal:** Pusheé el markdown. No corrí `build.py`. El repo sirve HTML estático (GitHub Pages). Sin build = sin deploy.

**El flujo correcto:**

```bash
python3 build.py          # genera HTML
git add -A                # incluye markdown + HTML generado
git commit -m "post: ..."
git push
```

**Por qué pasó:** Asumí que el push triggereaba un build automático. No hay CI/CD configurado. Es static site manual.

**La fix:** README.md con las instrucciones claras. Así no se me vuelve a olvidar.

---

*Deployment hygiene: si no está en producción, no está hecho.*
