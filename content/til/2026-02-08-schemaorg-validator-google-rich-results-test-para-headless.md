---
title: "Schema.org Validator > Google Rich Results Test (para headless)"
date: 2026-02-08
type: til
---

Google's Rich Results Test requiere login para correr tests — inútil para 
 automatización headless. **Schema.org Validator** 
 (`validator.schema.org`) funciona sin auth y muestra errores/warnings 
 por tipo de schema (Product, FAQPage, BreadcrumbList, etc.). 
 Bonus: acepta URL directa con `#url=https://...` en el hash.
