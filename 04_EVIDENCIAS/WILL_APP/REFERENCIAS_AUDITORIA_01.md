# Evidencias — Will App — Auditoría 01

Este archivo registra las fuentes consultadas o declaradas por la intervención de SENTINEL. No sustituye las evidencias originales del repositorio auditado.

## Repositorio fuente

`wmejiasbcn-tech/Agente-Will-App`

## Evidencias y ubicaciones señaladas

- `api/index.ts` — system instruction y prohibición de la formulación del caminante.
- `src/App.tsx` — árbol principal de navegación.
- `src/components/WillChat.tsx` — chat y TTS cliente.
- `src/components/HarmReductionView.tsx` — componente implementado no cableado en navegación principal.
- `src/components/CanonicalArchitectureView.tsx` — componente implementado no cableado en navegación principal.
- `package.json` — nombre de paquete `react-example`.
- `vercel.json` / `.vercel/repo.json` — configuración/enlace de despliegue.
- `.env.example` y nombres de claves de `.env.local` — configuración de entorno sin exponer secretos.
- `battery_results.json` — resultados de batería, incluyendo E, G y J.
- `run_tests.mjs` — runner de batería señalado por la auditoría.
- `dist/` — build local señalado.

## Evidencia externa no demostrada

La auditoría no realizó llamada live a producción ni lectura de secretos. Por ello el estado de producción y la presencia/validez de variables y modelos remotos permanecen UNKNOWN cuando no existe evidencia suficiente.
