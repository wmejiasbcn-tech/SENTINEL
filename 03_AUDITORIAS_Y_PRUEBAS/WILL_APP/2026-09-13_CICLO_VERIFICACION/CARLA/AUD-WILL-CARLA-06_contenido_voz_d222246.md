# AUD-WILL-CARLA-06 — Contenido recalibrado + voz barge-in (prep) · `d222246`

**Fecha:** 2026-09-13  
**Fuente auditada:** Carla  
**Tip citado:** `d22224648b16e21a5ad618c561c3babbfe5e5de8` (= `main`)  
**Jurisdicción:** SENTINEL N1

## ESTADO
VERDE en contenido + despliegue · AMARILLO en cierre de voz (barge-in incompleto, Issue #34 abierta)

## OBJETIVO
Contrastar: recalibración de instrucción (RRRR/RRDD informativo, fuentes, lenguaje no normativo, conversación); interrupción de voz; Issue #34; Vercel READY.

## RESULTADO
**CONFORME en lo sustancial**, con matiz de atribución de commits y con voz **no cerrada** (como ella misma dice).

## EVIDENCIA

### Contenido (`api/app.ts`)
Cadena relevante: `2f6f275` (*recalibrate Will harm-reduction guidance*) modifica `api/app.ts` (+19/−1). El tip `d222246` **incluye** ese cambio en historia.

En `WAIPL_SYSTEM_INSTRUCTION` (lectura en `d222246`):
| Claim Carla | Veredicto |
|---|---|
| RRRR/RRDD no = silencio informativo; info práctica general no personalizada | **VERIFICADO** |
| Puente GTT, Energy Control, Ministerio de Sanidad, GESIDA, OMS/WHO, ONUSIDA, CDC si verificable | **VERIFICADO** |
| No inventar títulos/enlaces/docs/recomendaciones | **VERIFICADO** |
| No pautas personalizadas de dosificación / no prescribir | **VERIFICADO** |
| Evitar «consumo responsable» como fórmula | **VERIFICADO** |
| Ban exacto «disfruta con responsabilidad» | **PARCIAL** — no aparece esa frase literal; sí el marco no normativo / «consumo responsable» |
| Tras pregunta, no invadir turno con otro bloque | **VERIFICADO** (MODO CONVERSACIÓN) |
| Una cosa cada vez / turnos cortos | **VERIFICADO** |

### Mecanismo de mantenimiento
- Workflow `.github/workflows/replace-waipl-system-instruction.yml` actualizado (`0af9a90`, también `6e82b9b`) con `NEW_INSTRUCTION` embebida — **VERIFICADO** como mecanismo anti-regresión a versión antigua.
- `docs/P0_RUNTIME_SYSTEM_INSTRUCTION.txt`: **NO** refleja el texto nuevo (puente/silencio = 0). La fuente viva efectiva es `api/app.ts` + workflow, no ese `.txt`.

### Voz / barge-in
- `d222246`: añade `onStartListening?` a `MicProps` y lo invoca **antes** de `beginListen()` — **VERIFICADO** (hook preparado).
- `WillChat.tsx`: `onStartListening` = **0** usos — **NO cableado** a `speak.stop()` — **VERIFICADO** (coincide con Issue #34).
- Abort de fetch TTS pendiente al tomar mic: **NO VERIFICADO** como cerrado (Issue lo pide explícitamente).
- Carla **no** declara el problema cerrado — **CONFORME**.

### Issue #34
- Open, título *Voice: implement conversational turn-taking / barge-in*, creada 2026-09-13 — **VERIFICADO**.
- Cuerpo: stop audio + abort TTS pendiente + tests Android/`test:mic`/`test:compat`/`lint` — **VERIFICADO**.

### Despliegue
- `main` = `d222246` — **VERIFICADO**.
- Vercel Production deployment success «Deployment has completed» — **VERIFICADO**.
- Will App CI success en ese SHA — **VERIFICADO**.

### Alcance
No reforma general de arquitectura; foco contenido + prep voz — **CONFORME** con el diff observado.

## ESTADO EPISTÉMICO
Repo + Issue + Actions/Vercel status. Comportamiento conversacional real y barge-in en dispositivo: **NO VERIFICADO** (evaluación María / expertos pendiente, como dice Carla).

## DESVIACIONES / MATICES
1. El tip `d222246` es el commit de **voz (hook)**; el contenido está sobre todo en `2f6f275` (incluido en main).
2. Fuente `.txt` P0 desactualizada respecto a la instrucción embebida.
3. Barge-in: preparado ≠ cerrado.

## IMPACTO
Contenido recalibrado y en producción. Voz: Issue #34 es el cierre técnico pendiente. No dar por VERDE el turn-taking hasta cableado + abort + pruebas.

## ACCIÓN
Archivar en ciclo WILL_APP / CARLA. Siguiente contraste útil: cuando Aether cierre #34.
