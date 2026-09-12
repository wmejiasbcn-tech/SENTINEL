# Verificación del informe SENTINEL — INT-SEC-01

Revisión de afirmaciones relevantes del informe chat vs evidencia.  
Regla: no convertir ausencia en absoluto si la evidencia no lo permite.

| # | Afirmación | Veredicto | Evidencia / matiz |
|---|---|---|---|
| 1 | Advisory = GHSA-3f6p-5ww8-9rcr | **VERIFIED** | Título + advisory público |
| 2 | Afecta mysql2 &lt; 3.22.0 | **VERIFIED** | GHSA / OSV / Snyk |
| 3 | Corregido en ≥ 3.22.0 | **VERIFIED** | GHSA + release v3.22.0 |
| 4 | Relación con better-auth | **VERIFIED** | peer opcional `mysql2 ^3.0.0` en lock bajo `node_modules/better-auth` |
| 5 | Relación con db0 | **VERIFIED** | peer opcional `mysql2 *` en lock bajo `node_modules/db0` |
| 6 | Ausencia efectiva de mysql2 instalado | **VERIFIED** en checkout Lab `graph` examinado (no `node_modules/mysql2`). **No** se afirma para todos los entornos/CI no inspeccionados | Alcance: checkout local Lab + package.json Will App main |
| 7 | Uso PostgreSQL/PGLite | **VERIFIED** en `db.ts` / `migrate.mjs` del `graph` examinado | No excluye otros servicios WAIPL no auditados aquí |
| 8 | Ausencia de imports/conexiones MySQL | **VERIFIED** como *no encontrado en la búsqueda realizada* bajo `graph/src` | No equivale a prueba formal de vacío absoluto en todo el monorepo histórico |
| 9 | peerDependency ≠ instalada | **VERIFIED** | Definición npm + ausencia de paquete instalado |
| 10 | Imposibilidad de acceder a alerta privada Dependabot en esta sesión | **VERIFIED** | 404 público + sin `gh` auth |
| 11 | Clasificación P3 | **INFERRED** (priorización operativa SENTINEL) | No es score CVSS; el advisory genérico sigue High |
| 12 | No hay evidencia de explotación o fuga | **VERIFIED** | No se observó uso del cliente ni captura; **no** se afirma «imposible que exista fuera del alcance» |

## Corrección / precisión respecto al informe chat

- Donde el informe dijo «no explotable», el cierre documental precisa: **no explotable en el alcance verificado**; riesgo npm genérico permanece.  
- El número Dependabot #4 permanece **INFERRED** sin lectura autenticada de la ficha.