# GATE — WAIPL Verification Gate v1.0

**Punto de cierre obligatorio:** `gate_close.py` (`close_case`).

```bash
python3 gate_close.py cases/AUD-LAB-CARLA-01.json
python3 gate_close.py cases/AUD-LAB-CARLA-01.json --force-verde   # bypass bloqueado
python3 -m unittest test_gate_v1.py -v
```

Norma: `00_CONSTITUCION/WAIPL_VERIFICATION_GATE_v1.0.md`
