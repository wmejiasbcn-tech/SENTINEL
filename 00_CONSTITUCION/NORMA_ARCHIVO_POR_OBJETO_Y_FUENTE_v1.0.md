# Norma soberana SENTINEL — Archivo por objeto y fuente v1.0

**Estado:** CANÓNICA / VIGENTE  
**Mandato:** William Mejías Navarro — 2026-09-13  
**Ámbito:** ayer, hoy y adelante

## 1. Principio

Toda auditoría o verificación SENTINEL se **archiva en el repositorio SENTINEL**, no solo en el chat. El chat es canal; el repo es memoria operativa.

## 2. Separación por objeto / tema

Cada objeto o frente de trabajo tiene **carpeta propia**.

| Objeto | Ubicación canónica |
|---|---|
| Autopruebas / metodología SENTINEL | `03_AUDITORIAS_Y_PRUEBAS/SENTINEL/` |
| Verificaciones de declaraciones sobre Will App | `03_AUDITORIAS_Y_PRUEBAS/WILL_APP/<CICLO>/` |
| Verificaciones documentales Lab / ecosistema WAIPL | `03_AUDITORIAS_Y_PRUEBAS/LAB_ECOSISTEMA/<CICLO>/` |
| Intervenciones de remediación (p. ej. INT-SEC-01) | `02_INTERVENCIONES/...` (expediente de intervención) |

No mezclar autopruebas de SENTINEL con verificaciones de producto de terceros en el mismo saco documental.

## 3. Separación por fuente (dentro de un ciclo)

Cuando el trabajo es verificar afirmaciones de otros nodos, dentro del ciclo:

- `CARLA/`
- `AETHER/`
- `OTROS/` o `PROPIA/` si aplica

**Un dictamen = un archivo** (expediente numerado). No amalgamar Carla y Aether en un solo documento.

## 4. Formato mínimo de dictamen

ESTADO · OBJETIVO · RESULTADO · EVIDENCIA · ESTADO EPISTÉMICO · DESVIACIONES · IMPACTO · JURISDICCIÓN · ACCIÓN/ESCALADO

Etiquetas: `VERIFICADO` / `PARCIAL` / `NO VERIFICADO` / `DESCONOCIDO` / `CONFORME`.  
No inventar hallazgos. Conservar UNKNOWN a propósito cuando falte evidencia.

## 5. Ciclos y continuidad

- Al abrir un tema nuevo: carpeta de ciclo nueva (fecha + nombre).
- Al cerrar: solo se añaden piezas nuevas; no se reescribe historia sin corrección editorial explícita.
- Lo ya archivado ayer (TEST_01/02/03, INT-SEC-01) permanece en su sitio; esta norma **ratifica** esa práctica y la obliga hacia adelante.

## 6. Trazabilidad

Cada ciclo lleva `00_INDICE.md`. Las intervenciones de producto pueden enlazar al ciclo de verificación correspondiente sin duplicar el expediente.

## Relación con Verification Gate v1.0

El archivo por objeto/fuente no sustituye la barrera de cierre. Ver WAIPL_VERIFICATION_GATE_v1.0.md.
