# Estado operativo — INT-SEC-01

| Campo | Valor |
|---|---|
| ID | INT-SEC-01 |
| Fase | **REMEDIACIÓN EN CURSO** (orden soberana limpieza completa) |
| Naturaleza | INTERVENCIÓN TÉCNICA AUTORIZADA — reversible, limitada a Positron mysql2 |
| Semáforo | AMARILLO → objetivo VERDE tras evidencia |
| Antes | mysql2@3.15.3 en positron/package-lock.json |
| Vía | overrides mysql2 ≥3.22.0 (pin 3.24.4) — sin Prisma 8 RC |
| Actualizado | 2026-09-12T20:27:56+02:00 |