# AUD-GATE-PIN-SYNC-01 — PROPUESTA

## Respuesta A/B/C/D (re-vendor desde `dc8275b` / tip Gate)
**C + D**
- **C** — no aporta valor al perímetro Production actual (ya VERDE/CLOSED con pin `f877f2e`).
- **D** — introduce riesgo de regresión (receipt HMAC, schema case, layout package, human_acceptance).

No es **A** (necesario): Production acreditada sin el tip.
No es solo **B**: el tip es endurecimiento SENTINEL-side útil *eventualmente*, pero no “recomendable ya” sobre Will Production sin cutover.

## Recomendación
**MANTENER PIN** `f877f2e` (`f877f2e20b65de64a68ff98aff752b1bc3c23d2c`)

## Alternativas descartadas ahora
- **RE-VENDOR** a `dc8275b`/HEAD: prohibido sin orden explícita + plan cutover (HMAC secret, adapter, smokes, nuevo expediente Production).
- **OTRA ACCIÓN** inmediata de código: no. Solo análisis y archivo.

## Siguiente orden ejecutable (Soberano — NO ejecutar en este expediente)
`ORDEN-PROPUESTA: Documentar matriz de cutover pin→tip (HMAC env, case_schema, layout waipl_gate vs flat vendor, human_acceptance object, smoke T-A/B/R/F/X + receipt verify) como AUD-GATE-PIN-CUTOVER-01 analysis-only; sin tocar Production ni pin hasta Gate AUTHORIZED explícito.`
