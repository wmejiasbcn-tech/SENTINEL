# Propuesta — INT-SEC-01

**Estado:** PROPOSED / PENDIENTE DE DECISIÓN  
**No ejecutada** por orden expresa del Soberano (2026-09-12).

## Acción propuesta (no aplicada)

Gestionar administrativamente la alerta Dependabot asociada (referida como #4 / GHSA-3f6p-5ww8-9rcr) como:

- *not applicable*, o  
- *vulnerable dependency not reachable*,

justificando:

1. `mysql2` no instalado en el checkout `graph/` examinado;  
2. solo peer opcional de `better-auth` / `db0`;  
3. runtime de datos = Postgres/PGLite;  
4. Will App sin `mysql2`.

## Qué NO se debe hacer sin decisión nueva

- Instalar `mysql2` «para silenciar» la alerta.  
- Modificar `package.json` / lock de Lab o Will App sin mandato.  
- Alterar configuración de producción.

## Motivo de no ejecución

Orden soberana §3: «NO EJECUTAR LA PROPUESTA» / propuesta en PROPOSED / PENDIENTE DE DECISIÓN.