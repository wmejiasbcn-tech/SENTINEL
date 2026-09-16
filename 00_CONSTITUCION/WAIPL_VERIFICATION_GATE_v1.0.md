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

```text
RESULTADO PRESENTE
+ EVIDENCIA SUFICIENTE
+ VERIFICACIÓN COMPLETA
+ DICTAMEN CERRABLE
+ NINGÚN REQUISITO OBLIGATORIO PENDIENTE
        ↓
VERDE / CLOSED = true
```

En cualquier otro caso: **AMARILLO / OPEN** (`CLOSED = false`).

## 3. Punto exacto del circuito (cierre operacional)

**Única API autorizada de cierre:**

`07_ACCIONES_Y_VERIFICACIONES/GATE/gate_close.py` → función `close_case()` / CLI `gate_close.py`

Reglas:

1. Todo intento de declarar `VERDE` / `CLOSED=true` en el circuito SENTINEL **debe** pasar por `close_case()`.
2. `close_case()` llama siempre a `gate_evaluate.evaluate()` y **ignora** cualquier `force_verde`, `force_closed`, `desired_semaforo` o campos `CLOSED`/`semaforo` inyectados en el case.
3. No existen APIs `set_closed` / `force_close` / `mark_verde` / `declare_verde` en el módulo de Gate.
4. Un dictamen que afirme `VERDE/CLOSED` **sin** receipt emitido por `close_case` es **no conforme** bajo esta norma.

Evaluador: `gate_evaluate.py` (cálculo).  
Cierre: `gate_close.py` (gobernanza + receipt).

## 4. Jurisdicciones (inalteradas)

- **Vár** = verdad / auditoría de agentes, resultados y fuentes.
- **Yata** = auditoría de los **validadores** (no de agentes).
- **SENTINEL** = contraste N1 + aplicación de esta puerta.
- **Soberano** = autoridad final cuando corresponda.

## 5. Criterio de conformidad operacional

El Gate está **operativamente cerrado** solo cuando los tests demuestran que:

> **el circuito no puede producir `CLOSED=true` si el Gate no lo autoriza**, incluso ante intento explícito de bypass.
