# AUD-GATE-PIN-SYNC-01 — f877f2e ↔ dc8275b

## ESTADO
**ABIERTO / ANÁLISIS — SIN CAMBIO OPERATIVO**

## OBJETO

Determinar el impacto del paso desde el Gate pinado en Production:

f877f2e20b65de64a68ff98aff752b1bc3c23d2c

al HEAD actual de SENTINEL:

dc8275b0ba01e209d5a4a4ec99e5c5ff8e0e0dbd

Sin re-vendorizar, sin modificar el pin de Production y sin redeploy.

## COMPARACIÓN GIT

Repositorio: wmejiasbcn-tech/SENTINEL

- Base: f877f2e
- Head: dc8275b
- Estado: **ahead**
- Commits nuevos: **10**
- Merge-base: f877f2e
- Ficheros afectados por la comparación: **27**

## HALLAZGOS

### 1. Reorganización interna del Gate
El código ejecutable principal pasa a 07_ACCIONES_Y_VERIFICACIONES/GATE/waipl_gate/, con wrappers conservando los entrypoints gate_close.py, gate_evaluate.py y receipt.py.

**Clasificación:** COMPATIBLE en la superficie CLI/importación directa; **requiere revisar la integración de import paths** si se replica el árbol interno completo.

### 2. Validación estricta de casos
Aparece case_schema.json y validate_case, con additionalProperties=false y campos obligatorios adicionales, incluidos result_ref, evidence_refs y dictamen_ref.

**Clasificación:** **REQUIERE CAMBIO** para cualquier consumidor que emita casos antiguos sin esos campos o con propiedades no admitidas.

### 3. Human-in-the-loop formalizado
human_acceptance deja de ser un booleano simple cuando la aceptación es requerida y pasa a exigir un artefacto estructurado; cuando procede, exige además signature.

**Clasificación:** **REQUIERE CAMBIO** para cualquier integración que dependa del formato booleano anterior.

### 4. Receipt endurecido
La versión nueva del receipt es **1.1** e incorpora:
- HMAC-SHA256 mediante SENTINEL_GATE_HMAC_KEY
- issued_at / expires_at
- issuer
- verificación exacta de campos contra el Gate live
- rechazo explícito de receipts caducados

**Clasificación:** **REQUIERE CAMBIO** en la integración del receipt y en la provisión/configuración de secretos. Semánticamente es un endurecimiento, pero no es un cambio invisible para el consumidor.

### 5. Revalidación del caso antes de cerrar
build_final_state y close_case llaman a validate_case antes de producir el estado final.

**Clasificación:** COMPATIBLE como control; puede provocar rechazo donde el Gate anterior aceptaba casos incompletos.

### 6. CI y validación del repositorio
La CI pasa a descubrir test_*.py, ejecuta validación de repositorio y valida receipts persistidos mediante validate_repo.py.

**Clasificación:** SIN IMPACTO directo en Production runtime; refuerzo de verificación.

### 7. Invariante de cierre conservada
El contrato mantiene la barrera esencial:

closed=true → gate_status=AUTHORIZED

y

gate_status=BLOCKED → closed=false

También se conservan las defensas adversariales contra inyección de VERDE/CLOSED, reutilización de receipts y manipulación de estado.

**Clasificación:** COMPATIBLE / SIN REGRESIÓN observable en la comparación estática revisada.

## CONCLUSIÓN PROVISIONAL

El salto f877f2e → dc8275b **no es un cambio meramente editorial**. Contiene endurecimientos de seguridad y validación que modifican el contrato técnico de entrada y de receipts.

Por tanto:

**Re-vendorizar ahora:** **NO NECESARIO para mantener la Production acreditada existente.**

**Re-vendorizar en una futura evolución:** **ADMISIBLE y técnicamente justificable, pero solo después de una prueba de compatibilidad/migración específica del Will App** que cubra:
1. esquema de case;
2. human acceptance;
3. receipt v1.1;
4. SENTINEL_GATE_HMAC_KEY;
5. equivalencia de T-A/B/R/F/X;
6. ausencia de regresión en el circuito S2S.

## ESTADO DEL CAMBIO

~~~text
Production actual = CONFORME con pin f877f2e
SENTINEL actual   = dc8275b
Diferencia        = SIGNIFICATIVA / CONTRATO Y SEGURIDAD
Re-vendor ahora    = NO
Redeploy ahora     = NO
Pin sync           = REQUIERE ESTUDIO DE COMPATIBILIDAD ANTES DE EJECUTAR
~~~

## REGLA DE CIERRE

Este expediente permanece **OPEN** hasta disponer de una decisión soberana posterior sobre si iniciar una migración de pin. No se autoriza ningún cambio de Production como consecuencia de este análisis.
