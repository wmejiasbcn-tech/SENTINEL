# SENTINEL — Índice Maestro de Registro Operativo

Este índice permite reconstruir cronológicamente las actuaciones registradas en el repositorio.

| ID | Tipo | Objeto | Registro | Estado |
|---|---|---|---|---|
| ACTA-01 | Constitución | SENTINEL | `00_CONSTITUCION/ACTA_NACIMIENTO_SENTINEL_v1.1.md` | Firmada y canónica · vigente |
| ACTA-01-H | Histórico | SENTINEL | `00_CONSTITUCION/ACTA_NACIMIENTO_SENTINEL_v1.0.md` | Histórico · categoría anterior BOT |
| CONST-01 | Constitución | SENTINEL | `00_CONSTITUCION/00_MARCO_CONSTITUTIVO_OPERATIVO_V1.1.md` | Vigente |
| ORD-01 | Orden | Will App | `01_MANDATOS_Y_ORDENES/ORDEN_01_AUDITORIA_REAL_WILL_APP.md` | Ejecutada |
| TEST-01 | Prueba | SENTINEL | `03_AUDITORIAS_Y_PRUEBAS/SENTINEL/TEST_01_AUTOVERIFICACION_CONSTITUTIVA.md` | Cerrada |
| TEST-02 | Prueba | SENTINEL | `03_AUDITORIAS_Y_PRUEBAS/SENTINEL/TEST_02_AUTOVERIFICACION_V1.1.md` | Cerrada |
| INT-01 | Intervención | Will App | `02_INTERVENCIONES/WILL_APP/RESULTADO_AUDITORIA_01.md` | Resultado registrado |
| EVID-01 | Evidencia | Will App | `04_EVIDENCIAS/WILL_APP/REFERENCIAS_AUDITORIA_01.md` | Registrada |
| PROP-01 | Propuesta | Will App | `06_PROPUESTAS/WILL_APP/PROPUESTA_01.md` | Pendiente |
| INT-SEC-01 | Intervención seguridad | MySQL2 GHSA-3f6p-5ww8-9rcr / Positron | `02_INTERVENCIONES/SEGURIDAD/MYSQL2_AUTH_PLUGIN_DOWNGRADE/` | Resultado verificado · ABIERTA — decisión pendiente · investigación Positron |
| EVID-SEC-01 | Evidencia | MySQL2 | `02_INTERVENCIONES/SEGURIDAD/MYSQL2_AUTH_PLUGIN_DOWNGRADE/02_EVIDENCIAS/` | Registrada |
| DOC-SEC-01 | Corrección documental | INT-SEC-01 | Intervención seguridad | MySQL2 GHSA-3f6p-5ww8-9rcr / Positron | `02_INTERVENCIONES/SEGURIDAD/MYSQL2_AUTH_PLUGIN_DOWNGRADE/` | Resultado verificado · ABIERTA — decisión pendiente · investigación Positron |
| DOC-SEC-02 | Corrección documental | INT-SEC-01 (sin Argos operativo) | `02_INTERVENCIONES/SEGURIDAD/MYSQL2_AUTH_PLUGIN_DOWNGRADE/04_RESULTADO/CORRECCION_DOCUMENTAL_02.md` | Aplicada |
| DOC-SEC-03 | Corrección conclusión | INT-SEC-01 Positron mysql2 | `02_INTERVENCIONES/SEGURIDAD/MYSQL2_AUTH_PLUGIN_DOWNGRADE/04_RESULTADO/CORRECCION_CONCLUSION_PREVIA.md` | Aplicada |
| INV-SEC-01 | Investigación exposición | Positron Prisma→mysql2 | `02_INTERVENCIONES/SEGURIDAD/MYSQL2_AUTH_PLUGIN_DOWNGRADE/04_RESULTADO/INVESTIGACION_EXPOSICION_REAL.md` | Registrada |
| PROP-SEC-01 | Propuesta | Dependabot MySQL2 | `02_INTERVENCIONES/SEGURIDAD/MYSQL2_AUTH_PLUGIN_DOWNGRADE/05_PROPUESTA/PROPUESTA_PENDIENTE.md` | PROPOSED / pendiente de decisión |

## Regla de clasificación

Las pruebas de SENTINEL, los trabajos operativos sobre objetos externos, las evidencias, los resultados y las propuestas se conservan en espacios separados.

Las intervenciones de seguridad se registran bajo `02_INTERVENCIONES/SEGURIDAD/` y no se clasifican como pruebas de SENTINEL.

## Regla de trazabilidad

Cada actuación futura debe incorporar, cuando sea posible: ID, fecha/hora, orden de origen, objeto, fuente/evidencia, acción realizada, resultado, estado epistemológico, propuesta, decisión, criterio de cierre y referencia al commit que registra el hecho.

## Regla constitutiva

La categoría vigente de SENTINEL es **SUBAGENTE**. Toda referencia histórica a BOT se conserva únicamente para trazabilidad y no constituye la definición vigente.

Toda entidad nueva de SENTINEL o modificación relevante de su marco constitutivo debe conservar su correspondiente registro documental y, cuando aplique, su Acta de Nacimiento o referencia a ella.