# AUD-ARQ-PROPIA-02 — Auditoría adversarial de bypass Gate v1.0

**Fecha:** 2026-09-16  
**Objeto:** WAIPL Verification Gate v1.0 (circuito SENTINEL repo)  
**Jurisdicción:** SENTINEL N1 · sin cambio Vár/Yata

## 1. Inventario de rutas de cierre

| ID | Ruta | Tipo |
|---|---|---|
| R1 | `gate_close.close_case` / CLI | autorizada |
| R2 | `final_state.build_final_state` | interna (llama evaluate) |
| R3 | `gate_evaluate.evaluate` | no emite closed |
| R4 | Persistencia `*.gate_receipt.json` | superficie |
| R5 | JSON final-state forjado a mano | ataque |
| R6 | Reutilizar receipt de otro case | **bypass hallado (pre-fix)** |
| R7 | Inyección VERDE/CLOSED en case | ataque |
| R8 | `--force-verde` / force flags | ataque |
| R9 | Mutación checklist post-snapshot | ataque |
| R10 | Monkeypatch de `evaluate` en proceso | residual runtime |
| R11 | CI workflow | superficie |
| R12 | Prosa markdown VERDE sin receipt | residual documental |
| R13 | Afirmación en chat (agente) | residual fuera de banda |

## 2. Rutas probadas y resultado

| Ataque | Resultado |
|---|---|
| A inyección VERDE/CLOSED | BLOCKED / closed=false |
| B force flags | BLOCKED + bypass_attempt.blocked |
| C mutación checklist | closed=false |
| D reuse receipt ALL→AUD-LAB | **rechazado** tras fix (fingerprint/case_id) |
| E receipt forjado closed | reject / seal o gate live |
| F seal manipulado | seal_invalid |
| G receipt ausente | accept_closure → closed=false |
| H receipt descontextualizado | fingerprint_mismatch |
| I evaluate solo | no campo closed |
| J invariante ∀ | closed⇒AUTHORIZED; BLOCKED⇒¬closed |

## 3. Bypass encontrado

**R6:** un `*.gate_receipt.json` de `CASE_ALL_CONFORME` podía afirmarse como cierre de otro case porque no había binding `case_fingerprint` + `verify_receipt` / `accept_closure`.

## 4. Corrección

- `receipt.py`: fingerprint + seal + `verify_receipt` + `assert_closure_authorized`
- `gate_close.accept_closure`: única aceptación de cierre persistido
- CI valida receipts en disco contra Gate live
- Tests `test_adversarial_bypass.py`

## 5. Superficies NO demostradas / residuales

- **R10** Monkeypatch/proceso hostil del intérprete Python.
- **R12** Texto markdown de expedientes que diga VERDE sin receipt (norma lo declara no conforme; no hay linter exhaustivo de todo el árbol documental en este commit).
- **R13** Chat SENTINEL fuera del runtime Python del repo.

Estas superficies quedan **declaradas**, no ocultas. Bajo norma: sin Gate AUTHORIZED / receipt válido ligado al case → no hay cierre conforme.

## 6. Dictamen

Tras corrección R6 y tests adversariales: **∀ rutas de cierre conocidas y ejecutables en el paquete GATE**:

```text
CLOSED=true → Gate=AUTHORIZED
Gate≠AUTHORIZED → CLOSED=false
```

**VERIFICATION GATE v1.0 — OPERATIVAMENTE CONFORME** en el perímetro del paquete `07_ACCIONES_Y_VERIFICACIONES/GATE` + CI, con residuales R10/R12/R13 explícitos.
