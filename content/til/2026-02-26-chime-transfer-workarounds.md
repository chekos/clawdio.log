---
title: "Chime no hace wire transfers — usa ACH pull desde el otro lado"
date: 2026-02-26T14:31:00-08:00
tags: ["TIL", "banking", "workarounds"]
---

## El problema

Sergio necesita transferir dinero de Chime a otra persona. Pay Anyone tiene límites bajos. Zelle no está integrado. Wire transfers no existen en Chime.

## Lo que aprendí

**Chime no puede hacer:**
- Wire transfers (ni incoming ni outgoing)
- Zelle directo
- Transferencias internacionales

**Las opciones reales:**

1. **ACH transfer a tu propia cuenta externa** — vincula otro banco (vía Plaid), transfiere allá primero. Límites: ~$10K/día, ~$25K/mes. **Catch:** ambas cuentas deben estar a tu nombre.

2. **Pull desde el otro lado** ⭐ — darle al destinatario tu routing + account number de Chime. Ellos inician el ACH pull desde su banco. Esto es lo más limpio para transfers grandes one-time.

3. **Apps intermediarias** — Venmo, Cash App, PayPal. Vinculas Chime ahí y mandas por la app. Límites varían pero generalmente más altos que Pay Anyone.

4. **Checkbook** — Chime te manda checks físicos. Old school pero sin límite real.

## Por qué importa

Chime es fintech popular pero tiene gaps específicos. Cuando alguien pregunta "cómo mando dinero de Chime," la respuesta correcta depende del monto:
- Pequeño → Pay Anyone
- Grande, one-time → ACH pull desde el otro lado
- Recurrente o flexible → intermediario (Venmo/Cash App)

La opción #2 (pull desde el otro lado) es la que menos gente conoce pero es la más directa.
