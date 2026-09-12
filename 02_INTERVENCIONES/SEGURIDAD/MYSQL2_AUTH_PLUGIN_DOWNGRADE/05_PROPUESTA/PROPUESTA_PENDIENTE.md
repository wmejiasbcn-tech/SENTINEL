# Propuesta — INT-SEC-01 (actualizada tras investigación Positron)

**Estado:** PROPOSED / PENDIENTE DE DECISIÓN  
**No ejecutada.**

## Decisión pendiente

descartar/anotar/mantener u otra decisión determinada por la autoridad soberana o delegada competente — **teniendo en cuenta** que ya no aplica el relato «mysql2 no instalado» a Positron.

## Opciones de remediación (no aplicadas)

1. Esperar Prisma que arrastre `mysql2 >= 3.22.0`.
2. Override a `mysql2@>=3.22.0` con validación.
3. Mantener alerta OPEN documentando riesgo tooling vs no-exposición MySQL demostrada.

## Prohibido sin mandato nuevo

Modificar package.json/lock, instalar paquetes, cerrar Dependabot, ejecutar PoC.