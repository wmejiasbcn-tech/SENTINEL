# AUD-WILL-CARLA-04 — CodeQL: cuatro alertas (`24a6f60`)

**Fecha:** 2026-09-13  
**Fuente auditada:** Carla  
**SHA:** `24a6f6038c4183f72ceb3d58ecf6e7182ff09ac9`  
**Jurisdicción:** SENTINEL N1

## ESTADO
VERDE en código/CI/Vercel · AMARILLO en cierre del panel (2/4 aún open al auditar)

## RESULTADO
**CONFORME en implementación y estrategia; PARCIAL** en «4 alertas → causas corregidas» como cierre del analizador.

## EVIDENCIA
Cadena:
- `d4b97c0` — `ci.yml` → `permissions: contents: read`
- `95b1b8a` — `express-rate-limit` global (`limit: 120`, `windowMs: 15*60*1000`); eliminación de `contextDimension` en system prompt; `contextMap` estático por `detectedContext.type`
- `97dd5ee` — dependencia `express-rate-limit` `^8.7.0`
- hotfix temporal → eliminado en `24a6f60`

Verificación:
- Typecheck + Build SUCCESS — run 34755679385
- Vercel SUCCESS en ese commit
- Panel API tras análisis: **#7 fixed**, **#6 fixed**, **#5 open**, **#4 open**
  - #4 apuntaba a `server.ts` `app.get("*")` + `sendFile` (no solo rutas API)
  - #5 seguía viendo dataflow user→systemInstruction vía `detectedContext`/mapa
- PRs majors dejados abiertos deliberadamente — **VERIFICADO**

## IMPACTO
Remediación útil; no cantar «0 Open» hasta remate (ver AUD-WILL-CARLA-05).
