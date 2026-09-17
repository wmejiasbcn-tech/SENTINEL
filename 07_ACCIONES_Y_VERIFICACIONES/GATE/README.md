# GATE v1.0

- Cierre: `waipl_gate.gate_close.close_case`
- Aceptación persistida: `waipl_gate.gate_close.accept_closure(case, receipt)`
- Binding: `waipl_gate.receipt` (`case_fingerprint` + HMAC `seal` + expiración)
- Contrato de entrada: `case_schema.json`
- Variable requerida: `SENTINEL_GATE_HMAC_KEY`

```bash
cd /home/runner/work/SENTINEL/SENTINEL
export SENTINEL_GATE_HMAC_KEY='local-test-only-key'
export PYTHONPATH="$PWD/07_ACCIONES_Y_VERIFICACIONES/GATE"
python3 -m unittest discover -s "$PWD/07_ACCIONES_Y_VERIFICACIONES/GATE" -p 'test_*.py' -v
python3 "$PWD/07_ACCIONES_Y_VERIFICACIONES/GATE/validate_repo.py"
```
