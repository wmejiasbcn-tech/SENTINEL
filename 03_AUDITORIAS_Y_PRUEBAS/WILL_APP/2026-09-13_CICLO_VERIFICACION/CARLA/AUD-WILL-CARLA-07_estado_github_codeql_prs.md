# AUD-WILL-CARLA-07 — Estado GitHub (CodeQL #8, issues, PRs) + corrección workflow

**Fecha:** 2026-09-13  
**Fuente auditada:** Carla  
**Main observado:** `66503c82b3edfecba7e8f443f5e9336ad84d1adc`  
**Jurisdicción:** SENTINEL N1

## ESTADO
CONFORME con el mapa de Carla · con un matiz de tip posterior en barge-in

## RESULTADO
La corrección al dictamen SENTINEL sobre el workflow es **ACEPTADA**. El repositorio **no** está VERDE en seguridad ni en CI limpio.

## EVIDENCIA

### Code scanning
- Open = **1** → **#8** `js/system-prompt-injection` en `api/app.ts:228` (`parts: [{ text: m.content }]`) — **VERIFICADO**
- Tags security / CWE-1427; `rule.severity=error` (UI High) — **VERIFICADO**
- No declarar seguridad VERDE — **CONFORME**

### Issues abiertas
- Exactamente **2**: #34 barge-in; #33 Fundación génesis/hibridación — **VERIFICADO**

### Pull requests
- Open = **11** — **VERIFICADO**
- Con checks/combined failure (lectura API): #32 Vite, #31 @vercel/node, #30 setup-node, #29 lucide, #27 resource discovery, #16 TypeScript, #14 plugin-react, #12 motion = **8 FAIL**
- OK: #28 checkout, #24 Express, #1 Analytics = **3 OK**
- Coincide con «8 de 11 fallando» — **VERIFICADO**
- No implica fusionar ahora — **CONFORME** (mayoritariamente Dependabot/majors)

### Workflow `replace-waipl-system-instruction.yml`
- **ABSENT** en `main` — **VERIFICADO**
- Eliminado en `8020878` (*chore: remove fragile system instruction patch workflow*) — **VERIFICADO**
- La frase de AUD-WILL-CARLA-06 que lo citaba como mantenimiento actual queda **obsoleta** (fotografía anterior). **No recrear** — **CONFORME**

### Barge-in / #34 (matiz tip)
- Carla: hook no conectado en WillChat — era cierto en `d222246`.
- Tip actual `66503c8` añade `onStartListening={() => speak.stop()}` en WillChat — **VERIFICADO**.
- Issue **#34 sigue open** — **VERIFICADO**. Por tanto turn-taking **no cerrado** documentalmente (faltan pruebas/abort pendiente según el propio issue).

## TABLA (aceptada con matiz)

| Área | Estado |
|---|---|
| Contenido Will | VERDE (sin reabrir) |
| Despliegue funcional | VERDE (no re-auditado en este turno) |
| Turn-taking | AMARILLO — #34 abierta (cableado parcial en tip) |
| Code scanning | ROJO/AMARILLO — #8 High abierto |
| CI / Dependabot | AMARILLO — 8/11 PR fallando |
| Workflow replace | ELIMINADO; no recrear |

## PRIORIDAD (Carla)
1. No retocar contenido — **CONFORME**  
2. #34 + prueba voz — **CONFORME**  
3. Auditar/tratar #8 antes de seguridad VERDE — **CONFORME**  
4. Luego Dependabot por causa real — **CONFORME**

## CORRECCIÓN A SENTINEL
Se marca como **caducada** la afirmación de mantenimiento vía `replace-waipl-system-instruction.yml` en AUD-WILL-CARLA-06 respecto al estado *actual* de `main`.
