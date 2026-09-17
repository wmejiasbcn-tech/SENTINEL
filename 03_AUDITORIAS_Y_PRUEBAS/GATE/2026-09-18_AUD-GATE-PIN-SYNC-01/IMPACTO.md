# AUD-GATE-PIN-SYNC-01 — IMPACTO (clasificación por área)

Leyenda: SIN IMPACTO | COMPATIBLE | REQUIERE CAMBIO | REGRESIÓN | NO VERIFICABLE

| Área | Clasificación | Notas |
|---|---|---|
| Gate core (evaluate/close) | **REGRESIÓN** / REQUIERE CAMBIO | Package import path; `validate_case` estricto; `human_acceptance` bool→objeto rompe cases existentes |
| Receipt | **REGRESIÓN** | Seal SHA-256 → HMAC; campos nuevos; entry_point distinto; receipts pin inválidos bajo tip |
| Auth (Will bridge / `gate_http_auth`) | **SIN IMPACTO** (delta SENTINEL) | Tip Gate no toca bridge Will; auth S2S fuera del diff Gate |
| Anti-replay | **COMPATIBLE** parcial / REQUIERE CAMBIO | Tip añade expiry receipt; anti-replay HTTP Will-side intacto; cutover necesita clave HMAC |
| Final-State Contract | **REQUIERE CAMBIO** | Campos/trace/`closure_entry_point`; contract id igual pero binding distinto |
| Cierre (`gate_status`/`closed`) | **COMPATIBLE** (invariante) | Invariante CLOSED/AUTHORIZED se mantiene; camino de entrada y precondiciones cambian |
| Tests | **REQUIERE CAMBIO** | Tests tip asumen package + schema + HMAC env |
| Hardening | **COMPATIBLE** (SENTINEL) / **REGRESIÓN** (Will si se aplica crudo) | Hardening real en tip; en Production pin-conforme es riesgo si se force-sync |
| Behavior change | **REGRESIÓN** | Semántica aceptación humana + validación case + seal |
| Will App compatibility | **REGRESIÓN** | Manifest/hashes, adapter plano, verify path Production romperían |

## Perímetro Production actual
Ya **CONFORME** con pin `f877f2e`. Deltas tip **no aportan** valor inmediato al perímetro acreditado; sí introducen riesgo de regresión si se re-vendor sin plan.
