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
| TEST-03 | Prueba | Matriz Canónica de Agentes WAIPL | `03_AUDITORIAS_Y_PRUEBAS/SENTINEL/TEST_03_AUDITORIA_MATRIZ_CANONICA_AGENTES.md` | Cerrada · reconstruida (resultado AMARILLO; H7 recalibrado) |
| INT-01 | Intervención | Will App | `02_INTERVENCIONES/WILL_APP/RESULTADO_AUDITORIA_01.md` | Resultado registrado |
| EVID-01 | Evidencia | Will App | `04_EVIDENCIAS/WILL_APP/REFERENCIAS_AUDITORIA_01.md` | Registrada |
| PROP-01 | Propuesta | Will App | `06_PROPUESTAS/WILL_APP/PROPUESTA_01.md` | Pendiente |
| INT-SEC-01 | Intervención seguridad | MySQL2 GHSA-3f6p-5ww8-9rcr / Positron | `02_INTERVENCIONES/SEGURIDAD/MYSQL2_AUTH_PLUGIN_DOWNGRADE/` | **VERDE — RESUELTA / VERIFICADA** (Lab #123+#124; Dependabot #4 fixed) |
| EVID-SEC-01 | Evidencia | MySQL2 | `02_INTERVENCIONES/SEGURIDAD/MYSQL2_AUTH_PLUGIN_DOWNGRADE/02_EVIDENCIAS/` | Registrada |
| DOC-SEC-01 | Corrección documental | INT-SEC-01 | `02_INTERVENCIONES/SEGURIDAD/MYSQL2_AUTH_PLUGIN_DOWNGRADE/04_RESULTADO/CORRECCION_DOCUMENTAL_01.md` | Histórica · sustituida por correcciones posteriores |
| DOC-SEC-02 | Corrección documental | INT-SEC-01 · sin Argos operativo | `02_INTERVENCIONES/SEGURIDAD/MYSQL2_AUTH_PLUGIN_DOWNGRADE/04_RESULTADO/CORRECCION_DOCUMENTAL_02.md` | Aplicada |
| DOC-SEC-03 | Corrección conclusión | INT-SEC-01 · Positron/mysql2 | `02_INTERVENCIONES/SEGURIDAD/MYSQL2_AUTH_PLUGIN_DOWNGRADE/04_RESULTADO/CORRECCION_CONCLUSION_PREVIA.md` | Aplicada |
| DOC-SEC-04 | Resultado final | INT-SEC-01 · cierre VERDE | `02_INTERVENCIONES/SEGURIDAD/MYSQL2_AUTH_PLUGIN_DOWNGRADE/04_RESULTADO/RESULTADO_FINAL_VERIFICADO.md` | Cerrada |
| DOC-SEC-05 | Ejecución remediación | INT-SEC-01 · cierre VERDE verificado | `02_INTERVENCIONES/SEGURIDAD/MYSQL2_AUTH_PLUGIN_DOWNGRADE/04_RESULTADO/EJECUCION_REMEDIACION_COMPLETA.md` | Cerrada |
| INV-SEC-01 | Investigación exposición | Positron Prisma→mysql2 | `02_INTERVENCIONES/SEGURIDAD/MYSQL2_AUTH_PLUGIN_DOWNGRADE/04_RESULTADO/INVESTIGACION_EXPOSICION_REAL.md` | Registrada |
| PROP-SEC-01 | Propuesta | Dependabot MySQL2 | `02_INTERVENCIONES/SEGURIDAD/MYSQL2_AUTH_PLUGIN_DOWNGRADE/05_PROPUESTA/PROPUESTA_PENDIENTE.md` | Histórica · superada por remediación |
| REG-INT-01 | Registro integral | Jornada SENTINEL 2026-09-12 | `09_REGISTRO_OPERATIVO/REGISTRO_INTEGRAL_2026-09-12.md` | Vigente · consolidado |
| REG-AUD-01 | Auditoría registro | Carla / trazabilidad jornada | `09_REGISTRO_OPERATIVO/REGISTRO_AUDITORIA_CARLA_2026-09-12.md` | Registrada · README corregido; TEST-03 reconstruido después |
| REG-GROK-01 | Exploración | Capacidades Grok Bot relevantes para futuras operaciones | `09_REGISTRO_OPERATIVO/REGISTRO_INTEGRAL_2026-09-12.md` | Observacional · sin incorporación |

## Regla de clasificación

Las pruebas de SENTINEL, los trabajos operativos sobre objetos externos, las evidencias, los resultados y las propuestas se conservan en espacios separados.

Las intervenciones de seguridad se registran bajo `02_INTERVENCIONES/SEGURIDAD/` y no se clasifican como pruebas de SENTINEL.

Los hitos transversales de la jornada se consolidan en `09_REGISTRO_OPERATIVO/REGISTRO_INTEGRAL_2026-09-12.md` sin sustituir los expedientes específicos.

## Regla de trazabilidad

Cada actuación futura debe incorporar, cuando sea posible: ID, fecha/hora, orden de origen, objeto, fuente/evidencia, acción realizada, resultado, estado epistemológico, propuesta, decisión, criterio de cierre y referencia al commit que registra el hecho.

## Regla de registro total

Todo lo que SENTINEL reciba como orden, haga, analice, concluya, proponga, ejecute, verifique o cierre debe quedar registrado en el repositorio, clasificado, separado y consultable. Cuando una actuación implique decisiones o cambios de otros agentes/proyectos, se conserva también la referencia necesaria para reconstruir la intervención sin sustituir la custodia del repositorio afectado.

## Regla constitutiva

La categoría vigente de SENTINEL es **SUBAGENTE**. Toda referencia histórica a BOT se conserva únicamente para trazabilidad y no constituye la definición vigente.

Toda entidad nueva de SENTINEL o modificación relevante de su marco constitutivo debe conservar su correspondiente registro documental y, cuando aplique, su Acta de Nacimiento o referencia a ella.
