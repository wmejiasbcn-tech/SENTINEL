# Cierre de intervención — INT-SEC-01

**Fecha/hora de cierre documental:** 2026-09-12T17:45:00Z (aprox.; registro en repositorio SENTINEL)  
**Tipo:** intervención real de seguridad  
**ACCIÓN EJECUTADA SOBRE ALERTA / REPOS AUDITADOS:** **NINGUNA**

---

## ESTADO

**VERDE** (exposición práctica en el alcance examinado)  
**AMARILLO** (alerta Dependabot / advisory sigue existiendo como superficie administrativa no gestionada por SENTINEL)

---

## RESULTADO

La alerta corresponde al advisory público **GHSA-3f6p-5ww8-9rcr** (mysql2 &lt; 3.22.0). En el alcance verificado (`Agente-Will-App` + `Will-AI-Project-Lab/graph`), `mysql2` **no está instalado**; aparece solo como **peerDependency opcional** de `better-auth` y `db0`. El uso de datos demostrado es **PostgreSQL (`pg`/Neon) + PGLite**. No hay evidencia de explotación ni de fuga de credenciales.

---

## RIESGO REAL DEMOSTRADO

- Existencia del defecto en el ecosistema npm para clientes `mysql2` vulnerables (advisory High).
- Presencia de menciones de `mysql2` como peer opcional en el lockfile de `graph/`.

---

## RIESGO NO DEMOSTRADO

- Instalación efectiva de `mysql2` en `node_modules` del checkout examinado.
- Código de aplicación abriendo conexiones MySQL.
- Explotación, MITM o captura de plaintext en WAIPL.
- Contenido exacto autenticado de la ficha privada Dependabot #4 (404 / sin API).
- Que «#4» sea inequívocamente este GHSA sin lectura autenticada (queda **INFERRED** por título).

---

## PROPUESTA

**PROPOSED / PENDIENTE DE DECISIÓN:** que la autoridad competente (Soberano / Argos / quien tenga acceso Dependabot) decida si descarta la alerta como *not applicable / vulnerable dependency not reachable*, **sin** instalar `mysql2` y **sin** modificar dependencias salvo decisión expresa distinta.

---

## ACCIÓN EJECUTADA

**NINGUNA** sobre Dependabot, Will App, Lab Graphy ni dependencias.

**Sí ejecutado:** registro documental completo en `wmejiasbcn-tech/SENTINEL`.

---

## DECISIÓN PENDIENTE

1. ¿Descartar / anotar la alerta Dependabot como no aplicable?  
2. ¿Mantenerla abierta como recordatorio de higiene de peers?  
3. ¿Alguna otra acción de Argos/ciberseguridad?

---

## CRITERIO DE CIERRE DEFINITIVO

La intervención podrá cerrarse definitivamente cuando:

1. Quede registrada una **decisión soberana o delegada** sobre el tratamiento de la alerta Dependabot; y  
2. Si se afirma resolución técnica, exista evidencia de que el estado del lockfile/install sigue sin cliente `mysql2` vulnerable en uso, o de que cualquier uso futuro cumple `mysql2 >= 3.22.0` + TLS; y  
3. El Índice Maestro refleje el estado final (p. ej. Cerrada / Archivada).

Hasta entonces: **registrada, verificada, propuesta pendiente**.