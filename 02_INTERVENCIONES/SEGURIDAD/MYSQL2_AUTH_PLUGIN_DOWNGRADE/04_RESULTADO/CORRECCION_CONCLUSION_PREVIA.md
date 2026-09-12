# CORRECCIÓN DE CONCLUSIÓN PREVIA — INT-SEC-01

**Fecha:** 2026-09-12T20:21:12+02:00  
**Tipo:** corrección de conclusión (no borrado de evidencia histórica)

## Afirmación anterior (expediente inicial)

Se concluyó, tras examinar principalmente `graph/` y Will App, que `mysql2` **no estaba instalado** (solo peer opcional de `better-auth`/`db0`).

## Corrección

Esa conclusión era **incompleta / incorrecta como afirmación global del Lab**.

**Evidencia nueva (Dependabot #4 + `origin/main`):**

- En `positron/package-lock.json` existe `node_modules/mysql2` versión **3.15.3**.
- Introducida por **`prisma@7.10.0`** (devDependency / `devOptional`).

## Conservación

- El análisis de `graph/` (peers sin instalación) **sigue siendo válido en su alcance**.
- Queda registrado que el informe temprano **no abarcó Positron** (checkout local estaba desactualizado / sin carpeta `positron`).
- No se oculta el error de alcance: se reclasifica.

## Estado epistemológico

- Conclusión previa «mysql2 no instalado en el Lab»: **CONTRADICTORY** respecto a Positron en `origin/main`.
- Reformulación correcta: «mysql2 no instalado en el alcance `graph`/Will App examinado entonces; **sí** aparece instalado en lock de Positron vía Prisma». — VERIFIED