# AUD-WILL-GATE-DEPLOY-01 — ORDEN-PROD-SMOKE (bridge) RESULTADO
Fecha: 2026-09-17 Europe/Madrid
Surface: https://agente-will-app.vercel.app
Deployment: dpl_FABuKuwcnXVnNWuRBDBPL3yd4sDG
SHA: 46b7bca4718dfb8cd26e843aad1919f2acdf542d
Pin: f877f2e intacto

## Resultados
- T-A (bridge): FAIL — HTTP 401 SSO Protected deployment en Node→Python
- T-B (bridge): FAIL — idem
- T-R (bridge): FAIL — ok=false, Protected deployment en verify
- T-F (direct /api/gate/close): PASS — 401 missing/invalid bearer, BLOCKED
- T-X (direct): PASS — 401 invalid bearer (rechazo; skew/sig no aislados porque bearer falla primero)

## Bridge exposure
Codigo: /api/verification-gate sin auth de aplicacion.
En esta corrida no se logro AUTHORIZED anonimo porque Node no alcanzo Python (SSO).
Riesgo residual CASO B permanece latent.

## Decision
CORREGIR — no cerrar Production / expediente.

## Siguiente accion
GATE_PYTHON_BASE_URL=https://agente-will-app.vercel.app en Production + re-smoke T-A/B/R.
