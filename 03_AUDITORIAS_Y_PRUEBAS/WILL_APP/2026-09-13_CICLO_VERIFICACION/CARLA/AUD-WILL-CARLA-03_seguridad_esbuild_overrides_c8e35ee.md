# AUD-WILL-CARLA-03 — Seguridad inmediata (esbuild + overrides)

**Fecha:** 2026-09-13  
**Fuente auditada:** Carla  
**SHA tip citado:** `c8e35ee730feb90e190fca384a821a6b1c0c54c7`  
**Jurisdicción:** SENTINEL N1

## ESTADO
VERDE (hecho en main + CI) · matices menores

## RESULTADO
**CONFORME en lo sustancial.** Estrategia de no mezclar majors Dependabot: razonable.

## EVIDENCIA
Cadena real (3 commits):
1. `426a978` — esbuild `^0.25.0` → `^0.28.2`
2. `efe54bf` — elimina `.github/workflows/apply-p0-runtime.yml`
3. `c8e35ee` — `overrides`: `protobufjs` `^7.6.5`, `ws` `^8.20.1`

- HEAD = `c8e35ee` — **VERIFICADO**
- Will App CI success (typecheck + build) — run 34754497575 — **VERIFICADO**
- Dependabot alerts **open = 0** — **VERIFICADO** (API)
- Code scanning **open = 4** entonces: #7 workflow permissions; #5/#6 system-prompt-injection; #4 missing-rate-limiting — encaja con badge «Security and quality 4»
- PRs majors **no** mezclados (≈7 Dependabot + 1 Vercel Analytics) — **VERIFICADO**
- `replace-waipl-system-instruction.yml` seguía en **failure** (ruido residual)
- Colateral: desaparición de `@types/node` en el patch de overrides; typecheck igual pasó
- Sin `package-lock.json` en repo → overrides menos reproducibles

## IMPACTO
Frente seguridad inmediata en código + validate: hecho. Contador visual «4» = Code scanning, no Dependabot.
