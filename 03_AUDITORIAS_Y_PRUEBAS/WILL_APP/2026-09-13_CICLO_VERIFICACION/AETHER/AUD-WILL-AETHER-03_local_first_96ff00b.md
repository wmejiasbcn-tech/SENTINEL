# AUD-WILL-AETHER-03 — Local-first voz (`96ff00b`)

**Fecha:** 2026-09-13  
**Fuente auditada:** Aether  
**SHA:** `96ff00bae49f8beae799c153ae865557e1bbb4bb`  
**Jurisdicción:** SENTINEL N1

## ESTADO
AMARILLO (P2 sigue abierto) · local-first **CONFORME en repo** · batería runtime no atestiguada por SENTINEL

## RESULTADO
Afirmación nuclear correcta: solo se invierte orden de endpoints de speak; no toca modelo/mic/`api/app.ts`/`#8`. **P2 no se cierra.** Matiz: Vercel no desplegó `96ff00b` (rate-limit).

## EVIDENCIA
- Diff: `WillVoice.tsx` (+1/−1) + borra `voice-local-first.yml` — **VERIFICADO**
- `speakUrls()`: `['/api/voice/speak', PUBLISHED_SPEAK]` (antes al revés) — **VERIFICADO**
- En hostname publicada: solo `/api/voice/speak` — **VERIFICADO**
- Fallback a publicada si local falla (`no_tts_key` → break → siguiente URL): **VERIFICADO en cliente**
- `api/app.ts` blob = `7ad5e94`; **#8** sigue open — **VERIFICADO**
- Voice ID / modelo intactos — **VERIFICADO**
- Status Vercel `96ff00b`: **failure** rate-limit — **VERIFICADO**
- Último Production success listado al auditar: `63a11a5` (antes del swap) → local-first **NO VERIFICADO** en JS servido públicamente
- Relé visor en `api/vercel.cjs` activo (acumulado P2; no introducido por este commit) — coherente con «visor sin clave habla por relé»
- 10 mpeg + timings: **DESCONOCIDO** aquí; test `voice-long-conversation` tiene 10 turnos + recovery tras 400 `request` (`308d316`) — soporta diseño, no ms
- UI 5–10 turnos: Aether admite solo 1 speak local — **CONFORME** (honestidad)
- Fallback «local muerto» a Vercel: él marca **NO VERIFICADO** — **CONFORME**
- Live publicada `hasServerKey: true` — **VERIFICADO**

## IMPACTO
P2 = AMARILLO. Epistemología de Aether mejor (IMPLEMENTADO/TESTEADO/VERIFICADO/NO VERIFICADO). Re-verificar local-first en URL pública cuando Vercel despliegue.
