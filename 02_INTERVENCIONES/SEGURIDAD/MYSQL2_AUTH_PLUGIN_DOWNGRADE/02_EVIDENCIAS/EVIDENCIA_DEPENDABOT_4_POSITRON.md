# Evidencia primaria Dependabot #4 — Positron

**Registrado:** 2026-09-12T20:21:12+02:00  
**Fuente primaria:** declaración soberana + contraste con `origin/main` de `wmejiasbcn-tech/Will-AI-Project-Lab` (lectura `git show` / `git grep`, sin modificar el Lab).

## Datos de la alerta (aportados / contrastados)

| Campo | Valor | Estado |
|---|---|---|
| Repositorio | `wmejiasbcn-tech/Will-AI-Project-Lab` | VERIFIED (declaración + repo existente) |
| Alert | Dependabot #4 | VERIFIED como dato de orden; ficha privada no re-leída por API en esta sesión |
| Manifest | `positron/package-lock.json` | VERIFIED en `origin/main` |
| Paquete | `mysql2@3.15.3` | VERIFIED en lock (`node_modules/mysql2` version 3.15.3) |
| Cadena | `prisma@7.10.0` → `mysql2@3.15.3` | VERIFIED (deps de `node_modules/prisma`) |
| Severidad | HIGH / GHSA-3f6p-5ww8-9rcr | VERIFIED (advisory + orden) |
| Affected / patched | `<3.22.0` / `3.22.0` | VERIFIED (advisory) |
| Clasificación GitHub | Development | VERIFIED (orden); coherente con `devOptional: true` en lock — VERIFIED |

## Extracto lock (`origin/main`)

- `node_modules/mysql2`: version `3.15.3`, flag `devOptional: true`
- `node_modules/prisma`: version `7.10.0`, dependencies incluyen `mysql2: 3.15.3` y `postgres: 3.4.7`, flag `devOptional: true`
- `node_modules/@prisma/client`: version `7.10.0` — **sin** dependencia `mysql2` (solo `@prisma/client-runtime-utils`)

## Otras menciones mysql2 en el monorepo (`origin/main`)

| Ubicación | Naturaleza | Estado |
|---|---|---|
| `positron/package-lock.json` | Paquete instalable `mysql2@3.15.3` | VERIFIED — **única instalación efectiva hallada** |
| `graph/package-lock.json` | peer opcional better-auth / db0 | VERIFIED — no bloque `node_modules/mysql2` |
| `08_MARKETING_PRESENTACION/principios-inteligencia-hibrida/package-lock.json` | peer opcional (patrón similar) | VERIFIED presencia de peers; instalación efectiva **UNKNOWN** sin inspección de `node_modules` allí |