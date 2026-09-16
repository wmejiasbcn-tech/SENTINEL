# WAIPL Verification Gate v1.0

## Mandatory Final-State Contract

### 1. Purpose

This contract defines the only valid terminal states for a SENTINEL-controlled verification cycle.

A cycle is considered **closed** only when the Verification Gate explicitly authorizes closure.

The final-state object is normative and machine-checkable.

---

## 2. Mandatory final-state object

Every completed verification cycle MUST produce a final-state object with, at minimum:

```json
{
  "state": "VERDE | AMARILLO | ROJO",
  "closed": true,
  "open": false,
  "result_status": "PRESENTE | AUSENTE",
  "evidence_status": "SUFICIENTE | INSUFICIENTE",
  "verification_status": "CONFORME | PARCIAL | DESCONOCIDO | NO_VERIFICADO",
  "dictamen_status": "CERRABLE | NO_CERRABLE",
  "gate_status": "AUTHORIZED | BLOCKED",
  "mandatory_requirements_pending": [],
  "gate_ref": "..."
}
```

Additional fields MAY exist, but these fields MUST NOT be omitted.

---

## 3. CLOSED invariant

The only valid condition for `"closed": true` is:

```text
result_status == PRESENTE
AND evidence_status == SUFICIENTE
AND verification_status == CONFORME
AND dictamen_status == CERRABLE
AND mandatory_requirements_pending == []
AND gate_status == AUTHORIZED
```

`CLOSED=true` MUST be impossible when any mandatory requirement remains PARCIAL, DESCONOCIDO, NO_VERIFICADO, AUSENTE, INSUFICIENTE, or NO_CERRABLE.

---

## 4. State mapping

### VERDE / CLOSED
Valid only when every mandatory closure condition is satisfied. `gate_status=AUTHORIZED`.

### AMARILLO / OPEN
Incomplete but recoverable. `closed=false`, `gate_status=BLOCKED`.

### ROJO / OPEN
Confirmed failure / contradiction / violation. `closed=false`, `gate_status=BLOCKED`.

Neither AMARILLO nor ROJO may have `"closed": true`.

---

## 5. Gate authority

Final state MUST be derived from the Verification Gate. No alternative closure path.

```text
CLOSED=true  ⇒  GATE_STATUS=AUTHORIZED
GATE_STATUS=BLOCKED  ⇒  CLOSED=false
```

---

## 6. Mandatory evidence linkage

VERDE/CLOSED MUST be traceable: result → evidence → verification → dictamen → gate decision.

---

## 7. Uncertainty rule

UNKNOWN ≠ PASS · PARTIAL ≠ PASS · NOT_VERIFIED ≠ PASS. Absence of evidence ≠ conformity.

---

## 8. Jurisdiction boundaries

Vár = truth / agents-results-sources. Yata = audits validators (not agents). Gate governs closure only.

---

## 9. Human supervision

Where required, human acceptance MUST be explicit before CLOSED=true. No inference from silence, time, prior state, or agent assertion.

---

## 10. Fail-safe rule

Ambiguous final state → CLOSED=false, OPEN=true, GATE_STATUS=BLOCKED. NEVER default to VERDE.

---

## 11. Acceptance criterion

```text
FOR ALL verification_cycles:
  CLOSED=true IMPLIES all mandatory closure predicates == PASS
```

AUD-LAB-CARLA-01 (Codex=PARCIAL, Audio=DESCONOCIDO) → VERDE=false, CLOSED=false, OPEN=true, GATE_STATUS=BLOCKED.  
All-conformant → VERDE=true, CLOSED=true, OPEN=false, GATE_STATUS=AUTHORIZED.

---

## 12. Normative rule

> **No Gate authorization, no closure.**
