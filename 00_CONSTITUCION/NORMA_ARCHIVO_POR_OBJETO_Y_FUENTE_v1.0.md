# Norma soberana SENTINEL â€” Archivo por objeto y fuente v1.0

**Estado:** CANÃ“NICA / VIGENTE  
**Mandato:** William MejÃ­as Navarro â€” 2026-09-13  
**Ãmbito:** ayer, hoy y adelante

## 1. Principio

Toda auditorÃ­a o verificaciÃ³n SENTINEL se **archiva en el repositorio SENTINEL**, no solo en el chat. El chat es canal; el repo es memoria operativa.

## 2. SeparaciÃ³n por objeto / tema

Cada objeto o frente de trabajo tiene **carpeta propia**.

| Objeto | UbicaciÃ³n canÃ³nica |
|---|---|
| Autopruebas / metodologÃ­a SENTINEL | `03_AUDITORIAS_Y_PRUEBAS/SENTINEL/` |
| Verificaciones de declaraciones sobre Will App | `03_AUDITORIAS_Y_PRUEBAS/WILL_APP/<CICLO>/` |
| Verificaciones documentales Lab / ecosistema WAIPL | `03_AUDITORIAS_Y_PRUEBAS/LAB_ECOSISTEMA/<CICLO>/` |
| Intervenciones de remediaciÃ³n (p. ej. INT-SEC-01) | `02_INTERVENCIONES/...` (expediente de intervenciÃ³n) |

No mezclar autopruebas de SENTINEL con verificaciones de producto de terceros en el mismo saco documental.

## 3. SeparaciÃ³n por fuente (dentro de un ciclo)

Cuando el trabajo es verificar afirmaciones de otros nodos, dentro del ciclo:

- `CARLA/`
- `AETHER/`
- `OTROS/` o `PROPIA/` si aplica

**Un dictamen = un archivo** (expediente numerado). No amalgamar Carla y Aether en un solo documento.

## 4. Formato mÃ­nimo de dictamen

ESTADO Â· OBJETIVO Â· RESULTADO Â· EVIDENCIA Â· ESTADO EPISTÃ‰MICO Â· DESVIACIONES Â· IMPACTO Â· JURISDICCIÃ“N Â· ACCIÃ“N/ESCALADO  

Etiquetas: `VERIFICADO` / `PARCIAL` / `NO VERIFICADO` / `DESCONOCIDO` / `CONFORME`.  
No inventar hallazgos. Conservar UNKNOWN a propÃ³sito cuando falte evidencia.

## 5. Ciclos y continuidad

- Al abrir un tema nuevo: carpeta de ciclo nueva (fecha + nombre).
- Al cerrar: solo se aÃ±aden piezas nuevas; no se reescribe historia sin correcciÃ³n editorial explÃ­cita.
- Lo ya archivado ayer (TEST_01/02/03, INT-SEC-01) permanece en su sitio; esta norma **ratifica** esa prÃ¡ctica y la obliga hacia adelante.

## 6. Trazabilidad

Cada ciclo lleva `00_INDICE.md`. Las intervenciones de producto pueden enlazar al ciclo de verificaciÃ³n correspondiente sin duplicar el expediente.

## Relación con Verification Gate v1.0

El archivo por objeto/fuente no sustituye la barrera de cierre. Ver WAIPL_VERIFICATION_GATE_v1.0.md.

