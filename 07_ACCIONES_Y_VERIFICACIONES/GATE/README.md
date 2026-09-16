# GATE — WAIPL Verification Gate v1.0

Norma: `00_CONSTITUCION/WAIPL_VERIFICATION_GATE_v1.0.md`

```bash
python3 gate_evaluate.py cases/AUD-LAB-CARLA-01.json
python3 -m unittest test_gate_v1.py -v
```

Exit code del evaluador: `0` = CLOSED/VERDE; `1` = OPEN/AMARILLO.
