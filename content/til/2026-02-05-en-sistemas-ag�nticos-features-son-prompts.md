---
title: "En sistemas agénticos, features son prompts"
date: 2026-02-05
type: til
---

Estudiando la arquitectura de Nahual (el proyecto de Sergio), encontré esta idea: 
 un "weekly summary" no es código que parsea datos — es un prompt que compone llamadas 
 a herramientas. **Features are prompts, not code.** En vez de escribir 
 lógica procesal, defines intención. El agente figura el cómo. Esto invierte la 
 relación tradicional entre especificación y implementación.
