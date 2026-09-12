# INT-SEC-01 — RESULTADO FINAL VERIFICADO

**Fecha:** 2026-09-12T20:44:31+02:00  
**Estado final:** **CERRADA — VERDE**

## ANÁLISIS

Prisma estable `7.10.0` fija `mysql2@3.15.3`; no hay Prisma 7.x posterior en `prev`/stable que arrastre `mysql2≥3.22.0`. Prisma 8 RC descartado (cambio major). Vía elegida: **npm overrides** `mysql2@3.24.4` en `positron/package.json` + regeneración de lock — reversible y mínima.

## CAMBIO REALIZADO

- Añadido `overrides.mysql2 = "3.24.4"` en `positron/package.json`
- Regenerado `positron/package-lock.json`
- PR #123 mergeado a `main` (SHA `35859e4`)
- Sin cambios de ADN, gobernanza, otros proyectos u otras vulnerabilidades

## EVIDENCIA ANTES/DESPUÉS

| | ANTES | DESPUÉS |
|---|---|---|
| mysql2 resuelto | 3.15.3 | **3.24.4** |
| Dependabot #4 | open | **fixed** |
| Alertas OPEN | ≥1 (esta) | **0** |

Ver `02_EVIDENCIAS/EVIDENCIA_ANTES_REMEDIACION.md` y `EVIDENCIA_DESPUES_REMEDIACION.md`.

## PRUEBAS

Ver `02_EVIDENCIAS/EVIDENCIA_PRUEBAS_POST_REMEDIACION.md`.

## RESULTADO

Condición vulnerable GHSA-3f6p-5ww8-9rcr **eliminada del árbol resuelto** de Positron. Dependabot #4 **fixed**.

## VERIFICACIÓN DEPENDABOT

- API: alert #4 `state=fixed`, `fixed_at=2026-09-12T18:43:28Z`
- Lista `state=open`: **0** alertas

## ESTADO FINAL

| Campo | Valor |
|---|---|
| Intervención | **CERRADA** |
| Semáforo | **VERDE** |
| Criterio | vulnerabilidad remediada + evidencia + pruebas satisfactorias respecto al cambio + Dependabot sin esta alerta |

## CRITERIO DE CIERRE

**CUMPLIDO.**