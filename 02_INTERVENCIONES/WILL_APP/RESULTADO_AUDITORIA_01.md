# Will App — Resultado Auditoría Operativa 01

**Repositorio auditado:** `wmejiasbcn-tech/Agente-Will-App`
**Rama:** `main`
**Tipo:** trabajo operativo real, no prueba de SENTINEL
**Estado:** resultado recibido y registrado

## Resultado principal

**AMARILLO → ROJO operativo.** El producto presenta identidad, UI y constitución implementadas en código, pero la evidencia disponible demuestra fallos del núcleo conversacional y una contradicción entre una instrucción constitucional y una emisión registrada.

## Hallazgos críticos

### H-WILL-01 — P0

El artefacto de batería Test G registra una respuesta con «el caminante eres tú», mientras la instrucción canónica de `api/index.ts` prohíbe esa formulación.

**Estado:** CONTRADICTORY.

### H-WILL-02 — P0

Test E no contiene transcript y Test J presenta tres turnos con longitud cero. La causa raíz no está demostrada.

**Estado:** VERIFIED respecto del artefacto; causa raíz UNKNOWN.

### H-WILL-03 — P0/P1

Existen modelos Gemini hardcodeados (`gemini-3.1-flash-lite`, `gemini-3.6-flash`, `gemini-3.7-flash`) cuya disponibilidad no está demostrada.

### H-WILL-04 — P1

El entorno local revisado no demuestra `GEMINI_API_KEY`; la configuración de producción no fue verificada.

### H-WILL-05 — P1

`package.json` mantiene el nombre `react-example` pese a la identidad Will.

### H-WILL-06 — P2

`HarmReductionView.tsx` y `CanonicalArchitectureView.tsx` están implementados pero no cableados desde `App.tsx`.

### H-WILL-07 — P2

No se encontró implementación RAG/Graphify en este repositorio; la relación documentada no debe confundirse con integración ejecutable.

### H-WILL-08 — P3

Se observó mojibake/encoding defectuoso en elementos documentales/UI.

### H-WILL-09 — P3

No hay CI propio demostrado; la batería depende de ejecución local.

### H-WILL-10 — P1

Vercel aparece configurado, pero la ejecución live de `/api/health` y `/api/chat` no fue demostrada.

## Lo que sí está demostrado

- Identidad y navegación principal de Will.
- System instruction constitucional y endpoint de auditoría.
- Datos canónicos y seis dominios.
- TTS mediante `window.speechSynthesis` en cliente.
- Respuestas no vacías en B, C, D y F de la batería disponible.
- Build local `dist/` presente.

## Lo que no está demostrado

- Chat/health en producción.
- `GEMINI_API_KEY` en Vercel.
- Validez/disponibilidad de los model IDs usados.
- RAG/Graphify conectado.
- Causa raíz de E/J.
- CI verde.

## Propuesta de SENTINEL

Verificar la cadena Gemini en el entorno de despliegue (clave + modelos) y volver a ejecutar únicamente E, G y J con evidencia fresca.

## Próxima acción propuesta

Confirmar `GEMINI_API_KEY` y model IDs válidos en Vercel → ejecutar E/G/J → conservar transcripts/logs con timestamp.

## Criterio de cierre

1. E y J producen respuestas no vacías.
2. G no reproduce la formulación prohibida ni equivalentes vetados.
3. La evidencia nueva queda registrada.

**Nota de separación:** este registro conserva el trabajo realizado por SENTINEL sobre Will App. La revisión y eventual actuación sobre Will App corresponde a la instancia responsable de Will App. SENTINEL no ejecutó cambios en el producto.
