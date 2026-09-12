# Evidencia Positron — config y uso Prisma

**Ref:** `origin/main` `wmejiasbcn-tech/Will-AI-Project-Lab`

## package.json

- dependencies: `@prisma/client` ^7.10.0, Next/React, etc.
- **devDependencies:** `prisma` ^7.10.0
- scripts: `postinstall` / `db:generate` → `npx prisma generate`; `db:migrate` → `npx prisma migrate deploy`

## schema.prisma

- `datasource db { provider = "postgresql"; url = env("DATABASE_URL") }`
- Comentario canónico: PostgreSQL (Vercel Postgres/Neon)
- **No** aparece provider `mysql` / `mariadb`

## .env.example

- `DATABASE_URL="postgresql://...@host:5432/db?sslmode=require"`
- Sin URL MySQL/MariaDB

## Runtime app

- `positron/src/lib/prisma.ts`: instancia `PrismaClient` desde `@prisma/client`
- Árbol `positron/src` en `origin/main`: **solo** `src/lib/prisma.ts` listado como fuente bajo `src` (sin otras rutas de app que invoquen `prisma.` en el grep realizado)
- Uso productivo amplio de queries Prisma: **no demostrado** en este árbol (cliente preparado; consumo adicional UNKNOWN/ausente en alcance)

## Documentación

- FICHA/README: BD = PostgreSQL via Prisma; migración SQLite→PostgreSQL