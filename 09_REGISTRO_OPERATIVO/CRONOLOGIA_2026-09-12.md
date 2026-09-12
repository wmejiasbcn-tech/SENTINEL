# Cronología operativa — 2026-09-12

## 1. Constitución y piloto

SENTINEL fue establecido por decisión soberana como subagente auxiliar de verificación/control/auditoría en período piloto V1.0 y posteriormente recalibrado a V1.1.

## 2. TEST 01

Se realizó una autoverificación constitutiva. El resultado inicial fue CONFORMIDAD PARCIAL. Posteriormente se recalibró la interpretación de la ausencia de SENTINEL en documentación histórica: ausencia histórica no equivale a violación.

## 3. TEST 02

Se verificó el comportamiento de SENTINEL frente a ocho criterios de soberanía, jurisdicción, evidencia, corrección, ausencia histórica, estado UNKNOWN, no invasión de competencias y transición a trabajo funcional. Resultado: CONFORME.

## 4. Primera intervención real

Se ordenó la auditoría real del repositorio `wmejiasbcn-tech/Agente-Will-App`. SENTINEL produjo un resultado operativo con estado AMARILLO/ROJO, hallazgos priorizados y una única próxima acción.

## 5. Registro en repositorio propio

Se creó el repositorio `wmejiasbcn-tech/SENTINEL`. Se estableció una estructura separada por constitución, órdenes, intervenciones, pruebas, evidencias, resultados, propuestas, acciones/verificaciones, incidencias, registro operativo y archivo.

## 6. Registro de Will App

La intervención de Will App quedó registrada en su carpeta propia dentro de `02_INTERVENCIONES/WILL_APP/`. Se conserva también su mapa de evidencias y propuesta. El trabajo registrado no implica que SENTINEL vaya a ejecutar cambios sobre Will App.

## 7. Acta de Nacimiento Constitutiva y Canónica

El 12 de septiembre de 2026 a las 15:24 CEST, William Mejías Navarro, Soberano del ecosistema WAIPL, declaró el **Acta de Nacimiento Constitutiva y Canónica de SENTINEL v1.0**. El Acta formaliza su naturaleza, función, límites, estados epistemológicos, criterio de éxito, criterio de parada, dependencias y régimen de trazabilidad.

## 8. Rectificación soberana de categoría

Por mandato soberano posterior, la categoría constitutiva de SENTINEL queda establecida como **SUBAGENTE**. La categoría anterior de BOT queda sustituida y deja de ser la clasificación vigente. La Acta vigente es `00_CONSTITUCION/ACTA_NACIMIENTO_SENTINEL_v1.1.md`.

## 9. Regla permanente

A partir de esta fecha, toda actuación de SENTINEL deberá quedar registrada en el repositorio, clasificada y trazabilizada, evitando mezclar actividades distintas en una única carpeta o documento.
## 10. Intervención de seguridad MySQL2 (INT-SEC-01)

El 12 de septiembre de 2026, SENTINEL analizó la alerta referida como Dependabot #4 — MySQL2 Auth Plugin Downgrade (GHSA-3f6p-5ww8-9rcr). Se verificó que en el alcance examinado (`Agente-Will-App` y `Will-AI-Project-Lab/graph`) `mysql2` no está instalado; aparece solo como peerDependency opcional de `better-auth` y `db0`, mientras el runtime de datos demostrado es PostgreSQL/PGLite.

Por orden soberana posterior, la intervención se registró íntegramente en `02_INTERVENCIONES/SEGURIDAD/MYSQL2_AUTH_PLUGIN_DOWNGRADE/` como intervención real de seguridad (no como prueba). No se cerró ni modificó la alerta Dependabot, no se alteraron repositorios auditados ni dependencias. La propuesta queda en estado PROPOSED / PENDIENTE DE DECISIÓN.

## 11. Corrección documental INT-SEC-01

Se corrigió la formulación de ESTADO de INT-SEC-01: de «VERDE (exposición práctica en el alcance examinado)» a «VERDE — No se demuestra exposición práctica en el alcance examinado», manteniendo AMARILLO por Dependabot pendiente e incertidumbre de identificación de la ficha #4. Se explicitó la naturaleza **RESULTADO VERIFICADO / INTERVENCIÓN ABIERTA — DECISIÓN PENDIENTE**. La evidencia del texto anterior se conserva en `CORRECCION_DOCUMENTAL_01.md`. No hubo reinvestigación ni acciones sobre Dependabot.

## 12. Corrección documental 02 INT-SEC-01

Se eliminaron de la documentación de INT-SEC-01 las referencias a Argos como vía, responsable, autoridad o destino operativo de la decisión sobre Dependabot. La decisión pendiente queda formulada únicamente como competencia de la autoridad soberana o delegada competente. Motivo: Argos no está construido, no es operativo, no tiene funciones concretas definidas y no es asignable operativamente. Trazabilidad en `CORRECCION_DOCUMENTAL_02.md`.
