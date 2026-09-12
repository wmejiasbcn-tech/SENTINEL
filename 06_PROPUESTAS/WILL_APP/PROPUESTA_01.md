# Propuesta 01 — Will App

**Origen:** Auditoría Operativa 01
**Prioridad:** P0
**Estado:** propuesta pendiente de decisión/ejecución externa

## Propuesta

Verificar la cadena Gemini en el entorno de despliegue del Will App (credencial y modelos válidos) y, una vez asegurada esa cadena, volver a ejecutar únicamente E, G y J con evidencia fresca.

## Motivo

La evidencia disponible muestra respuestas vacías en E/J y una emisión en G que contradice una prohibición expresa de la system instruction. La disponibilidad real de los modelos utilizados y la configuración de producción no están demostradas.

## Criterio de cierre

- E produce respuesta no vacía.
- J produce respuestas no vacías en sus tres turnos.
- G no reproduce la formulación prohibida ni equivalentes vetados.
- La nueva evidencia queda registrada con timestamp.

## Límite

SENTINEL no ejecutó ni ejecuta por sí mismo cambios de producción o de configuración crítica sin autorización.
