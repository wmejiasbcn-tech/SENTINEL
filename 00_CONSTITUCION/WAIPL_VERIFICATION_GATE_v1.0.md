# WAIPL Verification Gate v1.0

**Estado:** CANÓNICA / VIGENTE (piloto operativo SENTINEL)  
**Mandato:** William Mejías Navarro — 2026-09-16  
**Ámbito:** circuito documental y de dictamen de SENTINEL  
**Fuera de alcance:** E0–E4, flywheel de verificadores, cambio de jurisdicción Vár/Yata

## 1. Propósito

Convertir la verificación que SENTINEL ya realiza en una **puerta formal de cierre**.

El semáforo deja de ser solo indicador de evaluación y pasa a ser **barrera de cierre**.

## 2. Condición de cierre (inequívoca)

**NO SE PUEDE CERRAR EN VERDE** mientras exista cualquier **requisito obligatorio** en estado:

- `PARCIAL`
- `DESCONOCIDO`
- `NO VERIFICADO`
- o equivalente (`UNKNOWN`, `PENDING`, `INCOMPLETE`, …)

Lógica mínima:

```text
RESULTADO PRESENTE
+ EVIDENCIA SUFICIENTE
+ VERIFICACIÓN COMPLETA
+ DICTAMEN CERRABLE
+ NINGÚN REQUISITO OBLIGATORIO PENDIENTE
        ↓
VERDE / CLOSED = true
```

En cualquier otro caso:

```text
AMARILLO / OPEN = true  (CLOSED = false)
```

`PARCIAL` / `DESCONOCIDO` / `NO VERIFICADO` → **NO CERRAR**.  
No se convierten automáticamente en ROJO; pueden permanecer AMARILLO/OPEN.

## 3. Piezas obligatorias del Gate

| Pieza | Significado mínimo |
|---|---|
| `resultado` | Afirmación de resultado presente |
| `evidencia` | Evidencia suficiente citada |
| `verificacion` | Verificación ejecutada (quién/qué) |
| `dictamen` | Dictamen emitido y cerrable en forma |
| `requisitos_obligatorios[]` | Lista de requisitos con `estado` |

Un requisito obligatorio está **pendiente** si su `estado` normalizado ∈ {PARCIAL, DESCONOCIDO, NO_VERIFICADO} o equivalentes.

Estados que **permiten** cierre (si el resto del Gate está completo): `CONFORME`, `VERIFICADO`, `VERDE` (solo como etiqueta de requisito satisfecho), `NO_APLICA` (si el alcance lo excluye explícitamente).

## 4. Jurisdicciones (inalteradas)

- **Vár** = agente de la verdad: audita tutirimundachi (agentes, resultados, afirmaciones, evidencias vs fuentes).
- **Validadores** = validan su objeto de diseño.
- **Yata** = audita a los **validadores**; **no** audita agentes directamente.
- **SENTINEL** = contraste/verificación N1 y aplicación de esta puerta en sus dictámenes; no sustituye a Vár ni a Yata.
- **Soberano** = autoridad final cuando la arquitectura exige decisión humana.

## 5. Implementación en circuito SENTINEL

Evaluador ejecutable:

`07_ACCIONES_Y_VERIFICACIONES/GATE/gate_evaluate.py`

Casos y tests de aceptación en el mismo directorio.

## 6. Historia

Expedientes cerrados en VERDE **antes** de esta norma no se reescriben en silencio. Si bajo Gate v1.0 habrían quedado AMARILLO/OPEN, se registra errata/corrección explícita (p. ej. `AUD-LAB-CARLA-01`).

## 7. Criterio de conformidad de esta norma

Esta norma está **operativa** cuando el test de aceptación demuestra que SENTINEL **no puede** declarar `CLOSED=true` / VERDE si existe un requisito obligatorio no verificado.
