# Índice de pendientes técnicos SENTINEL

| ID | Área | Estado | Dueño | Siguiente acción | Criterio de cierre |
|---|---|---|---|---|---|
| R-001 | Gate service/API | ABIERTO | SENTINEL / autoridad operativa | Diseñar interfaz autenticada para emitir/verificar receipts fuera de CLI local | Cliente autenticado envía `case`, recibe receipt firmado y queda evento persistido |
| R-002 | Almacén inmutable | ABIERTO | SENTINEL / autoridad operativa | Definir almacenamiento append-only para eventos Gate y aprobaciones HITL | Cada cierre y verificación queda persistido con trazabilidad inmutable |
| R-003 | HITL | PARCIAL | SENTINEL | Integrar verificación criptográfica o evidencia firmada del aprobador humano | Toda aceptación humana requerida es verificable por actor, timestamp y evidencia |
| R-004 | Validación documental | PARCIAL | SENTINEL | Ampliar validadores para correlacionar claims markdown de cierre con receipts/evidencias | Un cierre documental inconsistente falla CI |
| R-005 | Cobertura operativa | ABIERTO | SENTINEL | Añadir tests end-to-end y smoke checks automatizados del circuito completo | Existe batería E2E automatizada del flujo de verificación |
