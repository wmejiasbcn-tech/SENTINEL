# INT-SEC-01 — Investigación técnica de exposición real

**Fecha:** 2026-09-12T20:21:12+02:00  
**Objetivo:** Determinar si `mysql2@3.15.3` (Prisma 7.10.0 / `positron/package-lock.json`) tiene ruta efectiva de ejecución susceptible a GHSA-3f6p-5ww8-9rcr.

---

## ANÁLISIS

Ver `03_ANALISIS/ANALISIS_EXPOSICION_REAL_GHSA.md` y evidencias en `02_EVIDENCIAS/`.

Resumen:

1. Dependencia transitiva real en Positron: `prisma@7.10.0` → `mysql2@3.15.3` (`devOptional`).
2. Runtime app usa `@prisma/client` + provider **postgresql**; `@prisma/client` **no** depende de `mysql2`.
3. No hay configuración MySQL/MariaDB en schema ni `.env.example`.
4. El GHSA exige handshake MySQL con el cliente vulnerable; esa condición **no está demostrada** en el diseño Positron actual.
5. La presencia del paquete en el árbol de **tooling** explica Dependabot OPEN (Development) sin equivaler automáticamente a explotabilidad en producción.

---

## RESULTADOS

| # | Resultado | Estado |
|---|---|---|
| R1 | `mysql2@3.15.3` está en el lock de Positron | VERIFIED |
| R2 | Cadena `prisma@7.10.0` → `mysql2@3.15.3` | VERIFIED |
| R3 | Clasificación Development / `devOptional` coherente | VERIFIED |
| R4 | Provider y URL de ejemplo = PostgreSQL (+ sslmode=require) | VERIFIED |
| R5 | `@prisma/client` sin dep `mysql2` | VERIFIED |
| R6 | Ruta de explotación GHSA en runtime app **no demostrada** | VERIFIED (no demostración) |
| R7 | Carga/handshake mysql2 durante `prisma generate`/`migrate` sobre Postgres | UNKNOWN / INFERRED no-MySQL |
| R8 | Conclusión previa «no instalado» queda corregida respecto a Positron | CONTRADICTORY → corregida |

---

## DISCREPANCIAS CON INFORME ANTERIOR

| Informe anterior | Ahora |
|---|---|
| mysql2 no instalado (énfasis graph) | **Sí instalado** en Positron lock vía Prisma |
| Alerta tratada como peer metadata | Alerta #4 apunta a **manifest Positron** con versión concreta 3.15.3 |
| Riesgo práctico nulo por ausencia de paquete | Paquete presente en tooling; **explotación MySQL aún no demostrada** |
| P3 solo higiene peers | Sigue siendo principalmente **riesgo de supply-chain/tooling**; producción Postgres sin ruta MySQL demostrada |

---

## RIESGO REAL

**Demostrado:**

- Dependencia vulnerable presente en árbol de desarrollo/tooling de Positron (`mysql2@3.15.3` < 3.22.0).
- Advisory HIGH aplicable al paquete si se usara para autenticar contra MySQL.

**No demostrado:**

- Ejecución de autenticación MySQL vulnerable en Positron (runtime o migrate) con las configs actuales.
- Fuga de credenciales.
- Uso de MySQL/MariaDB como provider.

**Dictamen de exposición:**  
**NO SE DEMUESTRA EXPOSICIÓN REAL AL GHSA EN EL DISEÑO POSTGRES ACTUAL.**  
**SÍ SE DEMUESTRA PRESENCIA DE DEPENDENCIA VULNERABLE EN TOOLING (Development).**

Semáforo sugerido para esta fase: **AMARILLO** (alerta OPEN + paquete presente; sin ruta MySQL demostrada).

---

## PROPUESTA DE REMEDIACIÓN (PROPOSED — no ejecutar)

1. **Preferente:** actualizar `prisma` / `@prisma/client` a una versión que declare `mysql2 >= 3.22.0` cuando exista (seguimiento upstream).
2. **Alternativa controlada:** `overrides`/`resolutions` a `mysql2@>=3.22.0` en `positron/package.json`, tras validación de compatibilidad con Prisma 7.10 (requiere mandato y prueba).
3. **Mientras tanto:** mantener Dependabot OPEN; no descartar como “false positive” absoluto — es dependencia real en lock, aunque la explotación MySQL no esté demostrada.
4. **No** cambiar el provider a MySQL.
5. Decisión: autoridad soberana o delegada competente.

---

## PRODUCTO DOCUMENTAL

Este expediente bajo INT-SEC-01 + evidencias + corrección de conclusión previa.

---

## SIGUIENTE ACCIÓN

Una sola: **decidir remediación** (esperar upstream Prisma vs override `mysql2@>=3.22.0` vs otra) sin cerrar Dependabot hasta evidenciar versión parcheada en lock.

---

## CRITERIO DE CIERRE

1. Decisión soberana/delegada registrada; y  
2. Evidencia en `positron/package-lock.json` de `mysql2 >= 3.22.0` **o** aceptación formal documentada del riesgo residual de tooling con monitoreo; y  
3. Índice Maestro en estado final de la intervención.