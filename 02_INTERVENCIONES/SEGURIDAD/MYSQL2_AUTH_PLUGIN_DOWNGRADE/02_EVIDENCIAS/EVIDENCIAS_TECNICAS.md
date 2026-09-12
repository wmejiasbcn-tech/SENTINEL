# Evidencias técnicas — INT-SEC-01

**Fecha de captura/registro:** 2026-09-12  
**Estado epistemológico global de este expediente:** mixto (VERIFIED / INFERRED / UNKNOWN según fila)

## 1. Repositorios examinados

| Repositorio | Superficie | Resultado breve |
|---|---|---|
| `wmejiasbcn-tech/Agente-Will-App` | `package.json` en `main` (raw GitHub) | Sin dependencia `mysql2` — VERIFIED |
| `wmejiasbcn-tech/Will-AI-Project-Lab` | checkout local `Documents\GitHub\Will-AI-Project-Lab` | `mysql2` solo como peer opcional en `graph/package-lock.json` — VERIFIED |
| `wmejiasbcn-tech/SENTINEL` | registro de esta intervención | N/A (destino de registro) |

## 2. Archivos examinados (Lab / Will App)

| Archivo | Hallazgo |
|---|---|
| `Will-AI-Project-Lab/graph/package.json` | Dependencias: `pg`, `@electric-sql/pglite`, `better-auth`, `kysely`; **sin** `mysql2` directo — VERIFIED |
| `Will-AI-Project-Lab/graph/package-lock.json` (~L4312, L4351–4353) | `better-auth@1.6.30` declara peer `mysql2: ^3.0.0` con `peerDependenciesMeta.mysql2.optional: true` — VERIFIED |
| `Will-AI-Project-Lab/graph/package-lock.json` (~L4840–4872) | `db0@0.3.4` (dev) declara peer opcional `mysql2: *` — VERIFIED |
| `graph/node_modules/mysql2` | **No existe** en el checkout examinado — VERIFIED |
| `graph/src/lib/db.ts` | Backend `neon` \| `pglite` (Postgres); no MySQL — VERIFIED |
| `graph/scripts/migrate.mjs` | Usa `import pg from "pg"` y `DATABASE_URL` — VERIFIED |
| Búsqueda de imports `mysql2` / createConnection MySQL bajo `graph/src` | Sin hallazgos — VERIFIED (ausencia de coincidencias en la búsqueda realizada) |
| `Agente-Will-App/package.json` (main) | Sin `mysql2` — VERIFIED |

## 3. Fuentes externas

| Fuente | Uso |
|---|---|
| https://github.com/advisories/GHSA-3f6p-5ww8-9rcr | Identidad del advisory, severidad High, rango &lt; 3.22.0, parche 3.22.0 |
| https://deps.dev/advisory/osv/GHSA-3f6p-5ww8-9rcr | Confirmación de alcance/versiones |
| https://security.snyk.io/vuln/SNYK-JS-MYSQL2-19498545 | CVSS ~8.2, CWE-522, remedio upgrade ≥ 3.22.0 |
| https://github.com/sidorares/node-mysql2/releases/tag/v3.22.0 | Release que deshabilita `mysql_clear_password` por defecto |
| Docs mysql2 Authentication Switch | Cleartext deshabilitado por defecto post-parche; opt-in `enableCleartextPlugin` |

## 4. Intentos sobre alerta Dependabot privada

| URL / acción | Resultado |
|---|---|
| `.../Agente-Will-App/security/dependabot/4` | HTTP 404 (no legible públicamente) — VERIFIED |
| `.../Will-AI-Project-Lab/security/dependabot/4` | HTTP 404 (no legible públicamente) — VERIFIED |
| `gh` API Dependabot en box / Nodo | No disponible (sin `gh` auth / `gh` no instalado en Nodo) — VERIFIED |

**Conclusión parcial:** el número Dependabot «#4» **no** pudo leerse como ficha privada autenticada. La vinculación al GHSA se basa en el **título exacto** aportado por el Soberano + correlación con GHSA-3f6p-5ww8-9rcr — estado: **INFERRED** respecto al número de alerta; **VERIFIED** respecto al advisory público.

## 5. Commits de repos auditados (contexto)

No se modificó ningún commit de los repos auditados en esta intervención.  
Referencias de trabajo previas (contexto Will App, no alteradas aquí): checkout Lab `main` local; Will App remote `main`.

## 6. Acciones NO ejecutadas (por orden)

Ver `05_PROPUESTA/` y `06_ESTADO/`.