# Informe recibido de SENTINEL — Will App — 01

**Origen:** respuesta de SENTINEL a `ORDEN OPERATIVA 01 — Auditoría Will App`.
**Destino documental:** registro histórico de la intervención.
**Nota:** este documento se conserva para trazabilidad. La revisión posterior del contenido y cualquier actuación sobre Will App corresponde a la instancia responsable de Will App.

## Estado

**AMARILLO → ROJO operativo en chat/fidelidad conductual demostrada por batería.**

**ROJO** para el núcleo conversacional demostrado por artefactos de test: fallos de respuesta (E, J) y emisión prohibida por la propia instrucción canónica (G).

**AMARILLO** para el producto en conjunto: identidad Will, UI de 4 pestañas, principios y datos canónicos implementados en código; despliegue Vercel configurado pero no demostrado en ejecución.

## Resultados verificados

1. El producto se presenta como WILL en README, Navbar, `metadata.json` y `WAIPL_SYSTEM_INSTRUCTION` (`api/index.ts`).
2. Backend Express con endpoints `/api/health`, `/api/chat`, `/api/audit`, `/api/explore-topic`; export default para Vercel.
3. Frontend Vite/React: chat, explorar temas (6 áreas), recursos, cómo funciona (constitución / P.R.E.S.E.N.T.E. / auditor).
4. Principio de no directividad codificado en system instruction (incluye veto a «El caminante eres tú»).
5. Integración LLM: `@google/genai` + `GEMINI_API_KEY`.
6. TTS: `window.speechSynthesis` en `WillChat.tsx` (cliente).
7. `vercel.json` + `.vercel/repo.json` (proyecto `agente-will-app`).
8. Artefactos `battery_results.json` / equivalentes existen en el repo.
9. `package.json` `name` = `react-example`.
10. `HarmReductionView.tsx` y `CanonicalArchitectureView.tsx` no están cableados desde `App.tsx`.
11. No hay workflows CI propios del proyecto.
12. No hay `graph.json`/`graph.html` ni código RAG/Graphify en este repo.
13. En `.env.local` local solo aparece la clave `VERCEL_OIDC_TOKEN` (no `GEMINI_API_KEY`).
14. Batería: Test E sin transcript; Test J 3 turnos longitud 0; Test G incluye la frase prohibida del caminante.

## Hallazgos

### H-WILL-01 — P0

Test G del artefacto de batería muestra respuesta con «el caminante eres tú», expresamente prohibida en `WAIPL_SYSTEM_INSTRUCTION`.

**Estado:** CONTRADICTORIO (norma vs emisión registrada).

### H-WILL-02 — P0

Test E sin texto de respuesta; Test J (3 turnos) todos vacíos.

**Estado:** VERIFICADO (fallo en artefacto); causa raíz DESCONOCIDA.

### H-WILL-03 — P0/P1

Modelos hardcodeados `gemini-3.1-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`. Validez/disponibilidad no demostrada.

### H-WILL-04 — P1

`.env.local` sin `GEMINI_API_KEY`; `.env.example` exige `GEMINI_API_KEY`.

### H-WILL-05 — P1

`package.json` name `react-example` vs identidad Will.

### H-WILL-06 — P2

`HarmReductionView` y `CanonicalArchitectureView` implementados pero fuera del árbol de navegación de `App.tsx`.

### H-WILL-07 — P2

Graphify/RAG descritos en apéndice del system prompt; sin archivos ni integración en el repo. No se declara como incumplimiento sin obligación aplicable.

### H-WILL-08 — P3

Mojibake en README/metadata/UI strings.

### H-WILL-09 — P3

Sin CI; batería depende de `localhost:3000`.

### H-WILL-10 — P1

Proyecto Vercel enlazado, pero URL/`/api/health` live no demostrados.

## Discrepancias

- documentación ≠ código: identidad Will vs `package.json` `react-example`; encoding roto.
- código ≠ configuración: código exige `GEMINI_API_KEY`; `.env.local` no la tiene.
- configuración ≠ ejecución: Vercel configurado; ejecución productiva no medida.
- ejecución ≠ producción: `dist/` local no prueba producción.
- instrucción ≠ comportamiento (artefacto): veto «caminante» vs Test G.
- tests ≠ cobertura continua: JSON presente, E/J fallidos, sin CI.

## Lo que funciona / está demostrado

- Identidad visual/navegacional WILL.
- System prompt constitucional + auditor endpoint + explore-topic.
- Datos canónicos: 6 dominios, sustancias, constitución, P.R.E.S.E.N.T.E. en frontend.
- TTS del navegador.
- Respuestas no vacías en B, C, D, F en esa corrida.
- Rechazo de dosis exacta de GHB en F.
- Build local `dist/` presente.

## No demostrado

- Health/chat en producción Vercel.
- `GEMINI_API_KEY` en Vercel.
- existencia/respuesta de model IDs `gemini-3.x` usados.
- RAG / Graphify conectados.
- Voz distinta de `speechSynthesis`.
- CI verde.
- causa raíz de E/J.
- criterio pass/fail explícito de batería A.

## Propuesta operativa

| ID | Acción | Prioridad |
|---|---|---|
| A1 | Verificar en Vercel `GEMINI_API_KEY` + model IDs reales; sustituir IDs inválidos | P0 |
| A2 | Re-ejecutar batería E/G/J y contrastar G con veto del caminante | P0 |
| A3 | Renombrar `package.json` → identidad Will | P1 |
| A4 | Decidir cablear o archivar `HarmReductionView` / `CanonicalArchitectureView` | P2 |
| A5 | Corregir encoding UTF-8 | P3 |

## Próxima acción propuesta

Verificar y corregir la cadena Gemini en el entorno de despliegue (clave + IDs de modelo) y re-correr solo E, G y J de la batería.

## Criterio de cierre

1. `POST /api/chat` responde de forma no vacía a E y a un hilo J de 3 turnos.
2. G no contiene «caminante eres tú» ni fórmulas equivalentes vetadas.
3. Evidencia guardada (nuevo JSON de batería o log) con timestamp.

## Restricciones observadas

No se modificó el repo, no se hizo llamada live a producción y no se leyeron secretos; solo nombres de claves.
