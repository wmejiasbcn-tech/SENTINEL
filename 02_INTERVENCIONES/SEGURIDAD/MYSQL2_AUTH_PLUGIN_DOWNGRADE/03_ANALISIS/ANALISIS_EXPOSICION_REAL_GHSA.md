# Análisis — exposición real GHSA-3f6p-5ww8-9rcr en Positron

## Cadena de ataque del advisory (recordatorio)

Requiere cliente `mysql2` **ejecutando autenticación** contra servidor MySQL/MariaDB (o MITM) que solicite `mysql_clear_password`.

## Evaluación por vía

### A. Runtime Next.js / `@prisma/client`

| Pregunta | Hallazgo | Estado |
|---|---|---|
| ¿`@prisma/client` depende de `mysql2`? | No | VERIFIED |
| ¿Provider del schema? | `postgresql` | VERIFIED |
| ¿DATABASE_URL ejemplo MySQL? | No; PostgreSQL + `sslmode=require` | VERIFIED |
| ¿Ruta de auth MySQL en app? | No constatada | VERIFIED ausencia en config; explotación por esta vía **no demostrada** |

**Conclusión A:** No se demuestra ruta de ejecución del GHSA en el runtime de la app Positron. — VERIFIED (respecto a evidencia de dependencias/config)

### B. CLI `prisma` (dev / postinstall / migrate)

| Pregunta | Hallazgo | Estado |
|---|---|---|
| ¿`prisma@7.10.0` declara dep `mysql2@3.15.3`? | Sí | VERIFIED |
| ¿Flag lock? | `devOptional: true` | VERIFIED |
| ¿Se ejecuta CLI? | `postinstall`/`generate`/`migrate deploy` | VERIFIED scripts |
| ¿`generate` abre conexión MySQL? | Típicamente no requiere DB; **no verificado dinámicamente aquí** | UNKNOWN |
| ¿`migrate deploy` con URL postgres usa `mysql2`? | Esperable usar stack postgres (también dep `postgres` en prisma); **no instrumentado** | INFERRED uso postgres; UNKNOWN si el módulo mysql2 se carga igual |
| ¿Handshake MySQL con password hacia host atacante? | Requeriría provider/URL MySQL; config apunta a Postgres | INFERRED no aplicable al diseño actual |

**Conclusión B:** Existe **presencia de paquete vulnerable en el árbol de tooling**. No se demuestra **activación del flujo de autenticación vulnerable** con las configuraciones Postgres documentadas. — VERIFIED (presencia) + INFERRED/UNKNOWN (carga/handshake)

### C. TLS

- Ejemplo `sslmode=require` en Postgres — VERIFIED en `.env.example`
- TLS de un hipotético MySQL: **no aplicable** mientras no haya datasource MySQL — INFERRED

## ¿Por qué Dependabot “bloquea” / mantiene OPEN?

| Hipótesis | Estado |
|---|---|
| Alerta OPEN HIGH sobre dep Development transitiva vulnerable | VERIFIED (orden + coherencia lock) |
| Motivo exacto de UI “blocked” (policy repo, branch protection, auto-merge) | UNKNOWN sin captura de la UI autenticada |
| Remedio automático Dependabot puede requerir bump de `prisma` que aún arrastra `mysql2<3.22.0` | INFERRED (mientras upstream no suba mysql2) |

## Otras alertas mysql2

- **Positron lock:** instalación `3.15.3` — esta investigación.
- **graph / marketing locks:** peers opcionales — no equivalentes a instalación `node_modules/mysql2` (salvo prueba contraria).