# Pruebas post-remediación — INT-SEC-01

**Registrado:** 2026-09-12T20:44:31+02:00  
**Entorno:** checkout local Nodo Central, `positron/` tras override + `npm ci --ignore-scripts`

| Prueba | Resultado | ¿Regresión del override? | Estado |
|---|---|---|---|
| Lock resuelve mysql2 ≥3.22.0 | 3.24.4 | N/A (objetivo) | VERIFIED |
| `npm ls mysql2` | `3.24.4 overridden` bajo prisma | No | VERIFIED |
| `npm audit` sin GHSA-3f6p | OK (mysql2 no en vulns) | No | VERIFIED |
| Disk `node_modules/mysql2` | 3.24.4 | No | VERIFIED |
| Disk `prisma` | 7.10.0 (sin bump major) | No | VERIFIED |
| `prisma generate` | Falla P1012 (`url` en schema no soportado por Prisma 7 config) | **No** — preexistente al scaffold Prisma 7 | VERIFIED fallo; INFERRED no causado por override |
| `next build` | Falla: no hay `app`/`pages` | **No** — scaffold incompleto preexistente | VERIFIED |
| Schema provider | `postgresql` | Sin cambio | VERIFIED |
| Otras alertas npm high (prisma/deepmerge-ts) | 3 highs restantes | Fuera de alcance INT-SEC-01 | VERIFIED presencia; no remediadas |

## Conclusión de pruebas

La remediación mysql2 **no introduce** regresiones atribuibles al override. Los fallos de generate/build son del estado previo de Positron.