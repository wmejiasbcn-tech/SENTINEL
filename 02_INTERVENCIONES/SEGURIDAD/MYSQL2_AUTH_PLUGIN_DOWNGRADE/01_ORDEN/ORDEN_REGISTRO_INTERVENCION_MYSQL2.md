# Orden — Registro obligatorio de intervención MySQL2

**ID intervención:** INT-SEC-01  
**Emisor:** William Mejías Navarro (Soberano WAIPL)  
**Receptor:** SENTINEL  
**Fecha/hora (recepción de la orden de registro):** 2026-09-12T17:41:00Z  
**Canal:** chat operativo SENTINEL (Nodo Central)

## Objeto

Registrar íntegramente la intervención de seguridad relativa al informe:

«INFORME SENTINEL — Alerta MySQL2 Auth Plugin Downgrade»

como **INTERVENCIÓN REAL DE SEGURIDAD**, no como prueba de SENTINEL.

## Clasificación obligatoria

```
02_INTERVENCIONES/
  SEGURIDAD/
    MYSQL2_AUTH_PLUGIN_DOWNGRADE/
```

Con subdivisión mínima: `01_ORDEN` … `06_ESTADO` (más `07_VERIFICACION_INFORME` para trazabilidad).

## Prohibiciones explícitas (NO EJECUTAR)

1. NO cerrar, descartar ni modificar la alerta Dependabot.
2. NO modificar repositorios auditados (`Agente-Will-App`, `Will-AI-Project-Lab`).
3. NO cambiar dependencias.
4. NO instalar `mysql2`.
5. NO modificar configuración.
6. NO abrir otra batería de pruebas ni ampliar la investigación innecesariamente.

## Estado de la propuesta analítica

**PROPOSED / PENDIENTE DE DECISIÓN.**

## Resultado esperado de esta orden

Registrar → verificar el informe → concluir → dejar propuesta → actualizar Índice Maestro y Cronología Operativa, de modo que la intervención se reconstruya desde el repositorio sin el chat.