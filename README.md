# 'SENTINEL'

**SENTINEL — Subagente auxiliar de verificación, control y auditoría del ecosistema WAIPL. Registro operativo, evidencias, resultados, propuestas y trazabilidad de sus intervenciones.**

## Finalidad del repositorio

Este repositorio constituye la **custodia operativa y trazabilidad propia de SENTINEL**.

Todo lo que SENTINEL haga, reciba como orden, analice, concluya, proponga, ejecute, verifique o cierre debe quedar registrado aquí de forma clasificada, separada y consultable.

## Categoría constitutiva

**SUBAGENTE.**

La categoría anterior de BOT queda sustituida por mandato soberano. La definición vigente se encuentra en `00_CONSTITUCION/ACTA_NACIMIENTO_SENTINEL_v1.1.md`.

## Principio de registro total

> **TODO lo que se hace en SENTINEL queda registrado en repositorio.**

No se utiliza un único archivo o carpeta para mezclar intervenciones diferentes. Cada actividad operativa tiene su propio espacio y conserva su evidencia, resultados, propuestas y verificaciones.

## Estructura

- `00_CONSTITUCION/` — naturaleza, mandato, límites y marco constitutivo.
- `01_MANDATOS_Y_ORDENES/` — órdenes operativas recibidas y su trazabilidad.
- `02_INTERVENCIONES/` — trabajos reales sobre proyectos, productos o componentes concretos. Cada intervención tiene carpeta propia.
- `03_AUDITORIAS_Y_PRUEBAS/` — pruebas y auditorías identificadas como tales, separadas de los trabajos reales.
- `04_EVIDENCIAS/` — evidencias y referencias de soporte, organizadas por intervención.
- `05_RESULTADOS/` — resultados emitidos por SENTINEL.
- `06_PROPUESTAS/` — propuestas operativas derivadas de resultados.
- `07_ACCIONES_Y_VERIFICACIONES/` — acciones ejecutadas/autorizadas y comprobaciones posteriores.
- `08_INCIDENCIAS/` — incidencias, bloqueos y cuestiones pendientes.
- `09_REGISTRO_OPERATIVO/` — índice maestro y trazabilidad cronológica de la actividad.
- `10_ARCHIVO/` — material histórico cerrado que deba conservarse.

## Separación de trabajos

Una intervención sobre un producto no se mezcla con una prueba sobre SENTINEL.

Ejemplo:

`02_INTERVENCIONES/WILL_APP/` contiene el registro del trabajo de auditoría realizado sobre Will App.

Las pruebas de comportamiento de SENTINEL permanecen separadas en `03_AUDITORIAS_Y_PRUEBAS/`.

Si en el futuro existe una intervención sobre Web, Graphy, I+D+i+e+A u otro ámbito, tendrá su propia carpeta.

## Relación con otros repositorios

El repositorio SENTINEL registra **la intervención de SENTINEL**. No sustituye la custodia del repositorio auditado.

La evidencia original debe permanecer en su fuente cuando corresponda. SENTINEL conserva la referencia necesaria para localizarla y reconstruir qué hizo, sobre qué evidencia y con qué resultado.

## Regla de estado

SENTINEL distingue obligatoriamente entre:

- `VERIFIED`
- `INFERRED`
- `PROPOSED`
- `UNKNOWN`
- `CONTRADICTORY`

No se presenta como hecho aquello que no esté demostrado.

## Estado actual

**SUBAGENTE · PILOTO V1.1**.

El repositorio se encuentra en fase de establecimiento de la trazabilidad operativa inicial.
