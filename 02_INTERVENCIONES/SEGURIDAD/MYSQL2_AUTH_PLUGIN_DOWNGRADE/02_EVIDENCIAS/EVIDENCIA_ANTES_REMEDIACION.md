# Evidencia ANTES de remediación — INT-SEC-01

**Registrado:** 2026-09-12T20:27:56+02:00  
**Ref git Lab:** `origin/main` = `41855c48dbe37d2fa674daecefd994a6887dbd30`  
**Método:** `git show origin/main:positron/...` (sin modificar Lab aún)

## Versiones package.json (Positron)

| Paquete | Rango |
|---|---|
| `@prisma/client` | `^7.10.0` (dependencies) |
| `prisma` | `^7.10.0` (devDependencies) |
| `overrides` | **ausente** (null) |

## package-lock.json (ANTES)

| Clave | Valor | Estado |
|---|---|---|
| `node_modules/mysql2`.version | **3.15.3** | VERIFIED |
| resolved | `mysql2-3.15.3.tgz` | VERIFIED |
| `devOptional` | true | VERIFIED |
| `node_modules/prisma`.version | 7.10.0 | VERIFIED |
| `node_modules/prisma` → mysql2 | **3.15.3** | VERIFIED |

## Advisory

- GHSA-3f6p-5ww8-9rcr; vulnerable `<3.22.0`; patched `3.22.0`
- Dependabot #4 OPEN (estado previo del expediente; re-verificación post-remediación pendiente)

## Schema / runtime

- provider = `postgresql` — VERIFIED
- Sin overrides previos

## Decisión de vía (pre-cambio)

- Prisma estable siguiente con mysql2 parcheado: **no disponible** (tag `prev`=7.10.0; `latest`=8.0.0-rc — major RC, no elegida)
- **Vía elegida:** `overrides.mysql2` ≥ 3.22.0 (pin preferido `3.24.4` latest patch), regenerar lock — reversible, sin bump major Prisma