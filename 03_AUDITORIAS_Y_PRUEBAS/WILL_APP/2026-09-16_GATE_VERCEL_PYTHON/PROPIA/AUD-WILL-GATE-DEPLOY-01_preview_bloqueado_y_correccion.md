# AUD-WILL-GATE-DEPLOY-01 — Integración Gate Will App (HTTPS → Python Function)

## ESTADO
**AMARILLO / OPEN / CLOSED=false**

No declarar: `Verification Gate v1.0 — producción CONFORME`.

## OBJETIVO
Resolver BLOQUEO 1 (Node/Vercel no ejecuta Python vía `spawn`) y BLOQUEO 2 (Gate ausente del artefacto de despliegue), según arquitectura obligatoria:

```text
Will App Node/Vercel
        ↓ HTTPS
Vercel Function Python
        ↓
WAIPL Verification Gate v1.0 canónico SENTINEL (pin f877f2e)
        ↓
Final-State Contract + receipt
```

## RESULTADO (al cierre de este dictamen)

1. **Código en `Agente-Will-App` main:** tip `c72c9853a9b322f0170317c3d86bfb56a181ab19` (incluye feat `089627e` + fixes).
2. **Implementación realizada (árbol):**
   - Vendor Gate + `SOURCE.md` + `GATE_MANIFEST.json` + CI anti-divergencia
   - `api/gate/close.py`, `api/gate/verify.py`
   - Cliente Node HTTPS (`api/verificationGate.ts`) — sin `spawn(python)`; fail-closed
   - Anti-replay HMAC+timestamp (±300s) documentado como **obligatorio** (`docs/GATE_ANTI_REPLAY_v1.md`)
   - `vercel.json` con builds Python antes del catch-all Node
3. **Tests locales (pre-deploy) OK:** T-A, T-B, T-R, T-X (adapter/adversarial), T-F (Node fail-closed), T-G (0 spawn en `api/**`).
4. **Preview / producción remotas:** **NO ACREDITADAS** en este expediente (ver desviaciones).

## EVIDENCIA

### A. Commits Will App

| SHA | Mensaje |
|---|---|
| `089627e1037204626021c621b30a2c37d84141cd` | feat(gate): Python Vercel Function + HTTPS Node client (pin f877f2e) |
| `ef77fb2d755352b8fcb0af2cf7ac1a872ec813de` | fix(will): repair invalid package.json and pin Node 24.x *(en realidad solo tocó vercel.json)* |
| `c72c9853a9b322f0170317c3d86bfb56a181ab19` | fix(will): restore valid package.json JSON and engines.node 24.x |

Padre de `089627e`: `c95241c438cfcade8c5f48a9e8e08c91d45f292a`.

Archivos principales en `089627e`:
`.env.example`, `.github/workflows/gate-sync-check.yml`, `api/gate/close.py`, `api/gate/verify.py`, `api/vercel.cjs`, `api/verificationGate.ts`, `docs/GATE_ANTI_REPLAY_v1.md`, `docs/GATE_ENV.md`, `package.json`, `requirements.txt`, `scripts/check_gate_manifest.py`, `tests/gate-http-client.test.ts`, `vercel.json`, `waipl_verification_gate/GATE_MANIFEST.json`, `waipl_verification_gate/SOURCE.md`, `waipl_verification_gate/gate_http_auth.py`.

### B. Fallo Preview/CI acreditado sobre `089627e`

- Deployment Vercel: `dpl_Fmfepnu47S4ty8wZKxpAAAkCn83J`
- URL: `https://agente-will-albsdb7pu-wmejiasbcn-8378s-projects.vercel.app`
- Estado: **Error**
- Git commit desplegado en ese intento: `089627e`
- Log: `Skipping build cache since Node.js version changed from "24.x" to ""` → Error
- GitHub check `validate`: **failure** — `npm error EJSONPARSE` en `package.json` por literal `` `n `` insertado en scripts (`test:gate` / `test:gate:http`)
- Rutas del deployment fallido ya listaban `/api/gate/close` → `close.py` y `/api/gate/verify` → `verify.py` (config parcial presente; build no READY)

### C. Corrección posterior

- Tip `origin/main` al archivar: `c72c9853a9b322f0170317c3d86bfb56a181ab19`
- `package.json` revalidado localmente (`json.load` OK) + `engines.node: 24.x`
- **Pendiente al archivar:** redeploy Preview READY + smoke T-A/B/R/F/X remotos + acreditación artefacto + producción

### D. Gate SENTINEL (no reescrito)

Pin canónico: `f877f2e20b65de64a68ff98aff752b1bc3c23d2c`  
Will App no debe modificar lógica del Gate; sync vía manifest/CI.

### E. Anti-replay (decisión)

**INCORPORADO (no opcional):** Bearer + `X-WAIPL-Timestamp` + HMAC-SHA256(secret, `"{ts}."||body`), ventana ±300s.  
Riesgo residual v1: replay exacto dentro de ventana sin store de nonces.

## ESTADO EPISTÉMICO

| Afirmación | Estado |
|---|---|
| Código Gate+HTTPS en main Will App (tip c72c985) | VERIFICADO (git ls-remote) |
| Tests locales A/B/R/X/F/G en OK antes del primer deploy | VERIFICADO (ejecución Nodo) |
| Preview READY con Functions Python respondiendo | **NO VERIFICADO** / pendiente |
| Smoke remoto T-A/B/R/F/X | **NO VERIFICADO** |
| Producción CONFORME | **PROHIBIDO declarar** — no acreditada |
| Vár/Yata modificados | NO (fuera de alcance; intactos) |

## DESVIACIONES

1. Primer `package.json` del feat `089627e` quedó JSON-inválido (error de edición PowerShell) → CI/Vercel fallaron.
2. Auto-review en chat de grupo bloqueó el push inicial; el soberano empujó `089627e`; SENTINEL empujó después `ef77fb2..c72c985`.
3. Ciclo Preview→prod smoke **no cerrado** en esta sesión.

## IMPACTO

Sin Preview/prod acreditados, el Gate **no** está demostrado en el circuito de despliegue vivo. El código en git apunta a la arquitectura mandada; la barrera de cierre remoto permanece abierta.

## JURISDICCIÓN

- SENTINEL: verificación / archivo / no autoridad ejecutiva de prod.
- Will App (`Agente-Will-App`): artefacto de despliegue.
- Gate canónico: repo SENTINEL @ `f877f2e`.

## ACCIÓN

1. Confirmar deployment Vercel tip `c72c985` en READY (Preview).
2. Ejecutar smoke T-A/B/R/F/X + SHA + presencia Functions Python.
3. Solo si Preview ACREDITADO → producción + mismos smokes.
4. No cerrar VERDE/CLOSED sin receipt `gate_close` / Final-State Contract.

## ESCALADO

Al Soberano: continuación operativa del redeploy/smoke (o mandato explícito a SENTINEL para reanudar desde `c72c985`).

## DICTAMEN FINAL (este archivo)

```text
PREVIEW → NO ACREDITADO (al momento del archivo)
PRODUCCIÓN → NO CONFORME / NO ACREDITADA
ESTADO EXPEDIENTE → AMARILLO / OPEN
```
