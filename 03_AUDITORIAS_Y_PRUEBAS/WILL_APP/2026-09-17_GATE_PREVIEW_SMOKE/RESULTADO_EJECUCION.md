# AUD-WILL-GATE-DEPLOY-01 — RESULTADO EJECUCIÓN PREVIEW SMOKE
Fecha: 2026-09-17 (Europe/Madrid)
Pin Gate: f877f2e (sin cambio)
Will tip fuente: 46b7bca4718dfb8cd26e843aad1919f2acdf542d

## ORDEN-1
PASS. Mecanismo: header x-vercel-protection-bypass (automation-bypass del proyecto).
Anon: HTTP 401 Protected deployment.
Con bypass: alcanza Function (unauthorized missing bearer / respuestas Gate).

## ORDEN-2
PASS. GATE_SHARED_SECRET presente en entorno Preview (Secret; valor no expuesto). Distinto registro del de Production.

## Preview
deployment: dpl_5o7GE98sUe4GqRiQvpLRtYCo7MLy
url: https://agente-will-9fn2xow94-wmejiasbcn-8378s-projects.vercel.app
READY: sí (deploy Completing → ready)
SHA meta Vercel: 46b7bca4718dfb8cd26e843aad1919f2acdf542d
Functions: api/gate/close.py (13.61MB), api/gate/verify.py (13.61MB)
Pin vendor: sin cambio

## Smokes Preview
T-A PASS — AMARILLO/BLOCKED closed=false
T-B PASS — VERDE/AUTHORIZED closed=true + receipt
T-R PASS — verify.valid=true authorized_closure=true
T-F PASS — 401 missing/invalid bearer; sin AUTHORIZED fabricado
T-X PASS — 401 bad signature / timestamp skew

## Producción
NO ejecutada / NO acreditada en esta fase.

## Expediente
AMARILLO/OPEN respecto a producción CONFORME.
Preview smoke funcional: ACREDITADO (esta batería).
