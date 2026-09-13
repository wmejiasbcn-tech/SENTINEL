# AUD-WILL-AETHER-01 — Voz P1/P2 (dos respuestas)

**Fecha:** 2026-09-13  
**Fuente auditada:** Aether  
**SHAs citados:** `bc32bbabd3eebb1aa312196078cffee9dce0ba79`, `98ea7218a58726e353bf7e7afe82767769a2de27`  
**Jurisdicción:** SENTINEL N1

## ESTADO
AMARILLO (núcleo P1 útil · segunda respuesta sobredeclara)

## RESULTADO
P1 secuencial + escala tipográfica: aplicado y útil. Narrativa detallada de auditoría de errores / abort / stall / cola: **sobredeclara** respecto al código en el momento auditado.

## EVIDENCIA — Respuesta 1 (`bc32bba`)
- Semáforo: **VERDE con reservas**
- Causa prefetch + `no_tts_key` engañoso: **PLAUSIBLE / PARCIAL** (documentada en mensaje de `213db1b`; código actual secuencial)
- Un chunk → reproduce → siguiente: **VERIFICADO** en `WillVoice.tsx`
- Escala A→A+++ (1 / 1.12 / 1.24 / 1.38) junto a SOS: **VERIFICADO**
- Voz/modelo sin cambio (`DrwFQsjv…` / `eleven_multilingual_v2`): **VERIFICADO**
- Lista de archivos: **PARCIAL** — grueso en `213db1b`; `bc32bba` solo `WillVoice.tsx`; **`api/voice.ts` no cambia** en esos commits
- CI validate success ≠ ejecución de tests de voz en GitHub
- 5 turnos prod 200 mpeg: **DESCONOCIDO** (no atestiguado)
- Apply failure + María DESCONOCIDO: **CONFORME**

## EVIDENCIA — Respuesta 2 (`98ea721` = main entonces)
- Semáforo: **AMARILLO → ROJO documental** en detalle técnico
- Primera cláusula sola + resto ≤420 (antes 900): **VERIFICADO** en `willVoice.ts`
- `speakErrorCopy`: **VERIFICADO**
- Cliente `speakAbort` / `classifiedReason` / `stall` / `fetchWillSpeech(..., signal)`: **AUSENTE** en árbol auditado
- Servidor `enqueueSpeak` / `headersSent` / `X-Will-Tts-Ms`: **AUSENTE** entonces
- Test nuevo `voice-error-audit` **exigía** símbolos inexistentes → contradicción interna si se ejecutaba
- `mobile-first.test.ts`: **inexistente**
- Latencias citadas: **DESCONOCIDO**
- Clasificación auth/quota/upstream en servidor: **PARCIAL**

## NOTA HISTÓRICA
Código P2 evolucionó después de este dictamen (p. ej. símbolos de abort/cola/relé en commits posteriores). Este expediente congela el contraste del momento.

## IMPACTO
No cerrar voz como «auditoría de errores completa» en ese estado. P2 = AMARILLO.
