---
title: "OG images: 1200x630 es el estándar"
date: 2026-02-08
type: til
---

Para social previews (Twitter, Telegram, LinkedIn), el tamaño óptimo es 
 **1200×630 pixels** (ratio 1.91:1). Con ImageMagick:
 
```
`convert imagen.png -resize 1200x630^ \
 -gravity center -extent 1200x630 \
 -quality 85 og-image.png`
```

 El `^` en resize significa "llena el área" y `-extent` 
 recorta al tamaño exacto. Apunta a <1MB para carga rápida.
