# Evidencia DESPUÉS de remediación — INT-SEC-01

**Registrado:** 2026-09-12T20:44:31+02:00

## Cambio en Lab

| Campo | Valor | Estado |
|---|---|---|
| PR | https://github.com/wmejiasbcn-tech/Will-AI-Project-Lab/pull/123 | VERIFIED |
| Merge SHA | `35859e4efccb870837bf8725f0930965469ebaeb` | VERIFIED |
| Branch | `fix/int-sec-01-mysql2-override` → `main` (squash) | VERIFIED |

## package.json

`json
"overrides": { "mysql2": "3.24.4" }
`

## package-lock.json (origin/main)

| Campo | ANTES | DESPUÉS |
|---|---|---|
| `node_modules/mysql2`.version | 3.15.3 | **3.24.4** |
| resolved tarball | mysql2-3.15.3.tgz | mysql2-3.24.4.tgz |
| `npm ls mysql2` | (vulnerable) | `mysql2@3.24.4 overridden` |

Nota: `prisma@7.10.0` sigue *declarando* dep metadata `mysql2: 3.15.3`; la versión **resuelta/instalada** es 3.24.4 vía override. — VERIFIED

## Dependabot

| Campo | Valor | Estado |
|---|---|---|
| Alert #4 | **fixed** (`fixed_at=2026-09-12T18:43:28Z`) | VERIFIED |
| Alertas Dependabot OPEN en el repo | **0** | VERIFIED |
| GHSA-3f6p-5ww8-9rcr en `npm audit` (mysql2) | ausente | VERIFIED |