# GATE v1.0

- Cierre: `waipl_gate.gate_close.close_case`
- Aceptación persistida: `waipl_gate.gate_close.accept_closure(case, receipt)`
- Binding: `waipl_gate.receipt` (`case_fingerprint` + HMAC `seal` + expiración)
- Contrato de entrada: `case_schema.json`
- Variable requerida: `SENTINEL_GATE_HMAC_KEY`

```bash
export SENTINEL_GATE_HMAC_KEY='local-test-only-key'
python3 -m unittest test_gate_v1.py test_adversarial_bypass.py -v
python3 validate_repo.py
```
