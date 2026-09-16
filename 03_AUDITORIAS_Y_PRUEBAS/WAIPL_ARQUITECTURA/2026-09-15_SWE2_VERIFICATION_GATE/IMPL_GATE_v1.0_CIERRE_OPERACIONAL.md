# Cierre operacional Gate v1.0

**Punto exacto:** `07_ACCIONES_Y_VERIFICACIONES/GATE/gate_close.py` → `close_case()`  
**Prueba de no-bypass:** `test_bypass_force_verde_blocked`, `test_injected_closed_ignored`  
**CI:** `.github/workflows/gate-v1.yml`

AUD-LAB-CARLA-01 + `--force-verde` → AMARILLO CLOSED=false (bypass bloqueado).  
CASE_ALL_CONFORME → VERDE CLOSED=true.
