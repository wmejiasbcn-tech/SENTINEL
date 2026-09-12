# Análisis de explotabilidad — INT-SEC-01

## Resumen del defecto (capa npm)

Un cliente `mysql2` &lt; 3.22.0 puede, ante `AuthSwitchRequest` a `mysql_clear_password`, enviar la contraseña en claro sin exigir TLS. Requiere servidor MySQL malicioso o MITM en la ruta de autenticación.

## Cadena de ataque requerida

1. Binario/paquete `mysql2` **instalado y cargado** en runtime.
2. Código que abra conexión MySQL con credenciales.
3. Destino controlado por atacante o canal sin protección adecuada.

## Aplicación a WAIPL (evidencia disponible)

| Condición | ¿Cumple? | Estado |
|---|---|---|
| `mysql2` instalado en `graph/node_modules` | No (directorio ausente) | VERIFIED |
| Dependencia directa en `graph/package.json` | No | VERIFIED |
| Peer opcional declarado por `better-auth` / `db0` | Sí (metadata lock) | VERIFIED |
| Runtime DB MySQL | No constatado; evidencia apunta a Postgres (`pg`/Neon) + PGLite | VERIFIED uso Postgres/PGLite; **no** se afirma «imposible en todo el universo WAIPL» |
| Imports MySQL en `graph/src` (búsqueda realizada) | Sin coincidencias | VERIFIED ausencia en alcance buscado |
| Will App usa `mysql2` | No en `package.json` main | VERIFIED |

## Distinción crítica

**peerDependency opcional ≠ dependencia instalada.**  
La presencia de `mysql2` en `peerDependencies` / `peerDependenciesMeta` del lockfile **no** implica que el paquete esté resuelto en `node_modules`.

## Clasificación de riesgo

| Tipo | Dictamen |
|---|---|
| Riesgo del advisory npm (genérico) | High — VERIFIED (fuentes públicas) |
| Riesgo real demostrado en checkout examinado | **No demostrado** (falta cliente instalado + uso MySQL) |
| Prioridad operativa SENTINEL | **P3 informativa / higiene Dependabot** — INFERRED como priorización operativa (no CVSS recalculado) |

## Regla de evidencia (V1.1)

No se declara incumplimiento, breach ni fuga: no hay los cuatro elementos (obligación aplicable + fuente + aplicabilidad a runtime + hecho observado de fuga).