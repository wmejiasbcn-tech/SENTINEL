# INT-SEC-01 — Ejecución de remediación completa

**Fecha:** 2026-09-12T21:54:00+02:00  
**Estado:** **VERDE — RESUELTA / VERIFICADA**

## ANÁLISIS

Vía autorizada: override fijo `mysql2@3.24.4` (sin Prisma 8 RC).  
Tras el override (#123), `prisma generate` fallaba por config Prisma 7 preexistente (P1012 `url` en schema) y Positron no tenía App Router. Se completó la ruta funcional PostgreSQL (#124) sin cambiar major de Prisma.

## EJECUCIÓN REAL

1. ANTES (commit `41855c4`): mysql2 **3.15.3**; Dependabot #4 OPEN.  
2. Override + lock (#123 → `35859e4`): mysql2 **3.24.4**.  
3. Dependabot #4 → **fixed** (2026-09-12T18:43:28Z); OPEN=0.  
4. prisma.config.ts + schema sin `url` + `@prisma/adapter-pg` + App Router mínimo (#124 → `cee8816`).  
5. Verificación limpia: `npm ci` OK; `prisma generate` OK; `prisma validate` OK; `next build` OK; `npm ls mysql2` = `3.24.4 overridden`.

## CAMBIO REALIZADO

| Commit Lab | Contenido |
|---|---|
| `35859e4` (PR #123) | `overrides.mysql2=3.24.4` + lock |
| `cee8816` (PR #124) | prisma.config.ts, schema PG, adapter-pg, app mínima |

Prisma permanece en **7.10.0**.

## EVIDENCIA ANTES/DESPUÉS

| | ANTES (41855c4) | DESPUÉS (cee8816) |
|---|---|---|
| mysql2 resuelto | 3.15.3 | **3.24.4** |
| Dependabot #4 | open | **fixed** |
| prisma generate | P1012 | **OK** |
| next build | sin app/ | **OK** |
| provider | postgresql | **postgresql** |

## PRUEBAS

| Prueba | Resultado | Estado |
|---|---|---|
| npm ci limpio | 477/478 pkgs, exit 0 | VERIFIED |
| prisma generate | Cliente 7.10.0 generado | VERIFIED |
| prisma validate | schema valid | VERIFIED |
| npm ls mysql2 | 3.24.4 overridden | VERIFIED |
| PrismaClient + PrismaPg | CLIENT_ADAPTER_OK | VERIFIED |
| next build | exit 0, ruta `/` | VERIFIED |
| tsc (previo a build) | exit 0 | VERIFIED |

## VERIFICACIÓN DE SEGURIDAD

- mysql2@3.15.3 **ausente** del árbol resuelto — VERIFIED  
- mysql2@3.24.4 **presente** — VERIFIED  
- Sin provider mysql en schema — VERIFIED  
- Runtime vía `PrismaPg` / `pg` (PostgreSQL) — VERIFIED  
- Conclusión histórica «mysql2 no instalado» **conservada** como corrección documental previa — VERIFIED (no borrada)

## VERIFICACIÓN DEPENDABOT

- Alert #4: **fixed** — VERIFIED  
- Alertas OPEN: **0** — VERIFIED  

## RESULTADO

INT-SEC-01 **RESUELTA / VERIFICADA**.

## COMMIT

- Lab: `35859e4`, `cee8816`  
- SENTINEL: este registro + índice/cronología

## ESTADO FINAL

**VERDE — RESUELTA / VERIFICADA**

## CRITERIO DE CIERRE

CUMPLIDO: vulnerable eliminado + 3.24.4 presente + lock OK + install OK + Prisma funcional + Positron funcional + pruebas OK + PostgreSQL intacto + Dependabot #4 resuelto.