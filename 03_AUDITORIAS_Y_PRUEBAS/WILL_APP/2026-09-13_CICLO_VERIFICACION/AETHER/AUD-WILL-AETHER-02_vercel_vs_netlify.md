# AUD-WILL-AETHER-02 — Vercel vs Netlify (no migrar)

**Fecha:** 2026-09-13  
**Fuente auditada:** Aether  
**Jurisdicción:** SENTINEL N1

## ESTADO
VERDE en veredicto operativo · AMARILLO en varios datos técnicos

## RESULTADO
**CONFORME el fondo:** no migrar ahora; María sigue en Vercel; Netlify = después / espejo comercial. Corregir errores de hecho antes de usar la tabla como ficha canónica.

## EVIDENCIA — VERIFICADO
- Front Vite + Express empaquetado en `api/vercel.cjs` (`package.json` build + `vercel.json`)
- TTS ElevenLabs `DrwFQsjvHFpLcKyvtbE3` / `eleven_multilingual_v2`
- URL viva `https://agente-will-app.vercel.app` (200)
- `maxDuration: 60` en `vercel.json`
- Sin `netlify.toml` / sin migración en curso
- Live `/api/voice/config`: `hasServerKey: true`, `listen: true`
- Migrar = reescribir funciones (no interruptor)
- Hobby Vercel = no comercial (Fair Use); Netlify Free admite comercial (docs)
- Background 15 min Netlify inútil para TTS síncrono
- Netlify no cura Safari / quota ElevenLabs / TTFA de modelo / mismos navegadores

## DESVIACIONES
1. **«Escucha: xAI STT» — INCORRECTO** en código: `/api/voice/listen` = ElevenLabs `speech-to-text` (scribe). `XAI_API_KEY` = fallback de conversación en `api/app.ts`. Comentario de `.env.example` desactualizado.
2. **«ffmpeg en camino de escucha» — AUSENTE** (0 hits en repo).
3. **Límite de cuerpo — inversión relativa:** Netlify buffered ~6 MB; Vercel Function body ~4.5 MB → Vercel es el techo más bajo para mic en base64.
4. Relé visor: CORS sí; relé activo no demostrado en el momento de esa auditoría (función `visorTtsOrigin` sin uso entonces).
5. Sitio Netlify `harmonious-conkies-6741aa` + SSO: **DESCONOCIDO** (sin panel).
6. Timings TTS citados: **DESCONOCIDO** en el turno.

## IMPACTO
Decisión soberana de mantener Vercel ahora: sostenida. Argumento comercial = el más sólido «para después».
