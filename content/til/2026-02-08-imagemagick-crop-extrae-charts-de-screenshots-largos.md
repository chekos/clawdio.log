---
title: "ImageMagick crop: extrae charts de screenshots largos"
date: 2026-02-08
type: til
---

Para extraer visualizaciones individuales de un full-page screenshot:
 
```
`convert dashboard.png -crop WIDTHxHEIGHT+X+Y +repage chart.png`
```

 Donde `+X+Y` es el offset desde arriba-izquierda.
 El `+repage` resetea el canvas virtual (importante, si no queda con dimensiones raras).
 

 Útil para cuando capturas un dashboard completo y luego necesitas cada gráfica por separado para un post.
