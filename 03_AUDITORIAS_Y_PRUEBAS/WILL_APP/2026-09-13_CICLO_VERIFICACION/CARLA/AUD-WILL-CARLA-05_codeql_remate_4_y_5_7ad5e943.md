# AUD-WILL-CARLA-05 — Remate CodeQL #4 y #5 (`7ad5e943`)

**Fecha:** 2026-09-13  
**Fuente auditada:** Carla  
**SHA citado:** `7ad5e943830dc6b13f7d10fbdd01df3ab4903e45`  
**Jurisdicción:** SENTINEL N1

## ESTADO
VERDE en remediación #4/#5 + análisis CodeQL · AMARILLO operativo (Vercel rate-limit; CI no en ese SHA)

## RESULTADO
**CONFORME.** Carla no inventa verde de Vercel. #4 y #5 quedan **fixed** en panel.

## EVIDENCIA
- `c476117` — `frontendLimiter` explícito en `server.ts` antes del fallback estático
- `7ad5e943` — elimina por completo el bloque `detectedContext → contextMap → systemInstruction` (−16 líneas); `systemInstruction = WAIPL_SYSTEM_INSTRUCTION` solo
- Workflow temporal `fix-codeql-prompt.yml` autoeliminado — **ABSENT**
- CodeQL Push on main: Analyze (actions) + Analyze (javascript-typescript) **success**
- API: **#4 fixed**, **#5 fixed**
- Vercel en `7ad5e943`: **failure** — «Deployment rate limited - retry in 24 hours» / `build-rate-limit` — **VERIFICADO**
- `ci.yml` runs con `head_sha=7ad5e943` → **0**; CI success sí en `c476117`
- Residual posterior (fuera del remate): **#8** `js/system-prompt-injection` open en tip de voz — no es #5 reabierto

## IMPACTO
Remate seguridad CodeQL #4/#5 cerrado. No tocar más seguridad hasta ciclo CI/Vercel; siguiente frente voz.
