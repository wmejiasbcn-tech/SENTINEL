# AUD-GATE-PIN-SYNC-01 — DIFF TÉCNICO

## SHAs resueltos
| Ref | Full SHA | Rol |
|---|---|---|
| Vendor pin Will App | `f877f2e20b65de64a68ff98aff752b1bc3c23d2c` | Pin acreditado Production |
| Tip Gate reportado | `dc8275b0ba01e209d5a4a4ec99e5c5ff8e0e0dbd` | Merge PR #1; **último commit que toca paths Gate** |
| SENTINEL `origin/main` HEAD | `03557287cfaf873f85c36ecd5687e3a572ace659` | Docs-only después de `dc8275b` (sin delta Gate code) |

`dc8275b` **es ancestro** de HEAD. Gate code tip efectivo = `dc8275b` (commits `dc8275b..HEAD` sobre paths Gate: **0**).

## Paths Gate
- Canonical: `07_ACCIONES_Y_VERIFICACIONES/GATE/` (+ package `waipl_gate/` desde tip)
- CI: `.github/workflows/gate-v1.yml`
- Contrato: `00_CONSTITUCION/WAIPL_VERIFICATION_GATE_v1.0*.md` (sin cambios en rango Gate code)

## Commits Gate `f877f2e..dc8275b` (6 sobre paths Gate; 10 commits totales en rango)
1. `4c4f47e` Harden Gate receipts and repo validation
2. `01e4350` Address Gate validation review feedback
3. `e928025` Fix Gate review findings
4. `e1fc853` Finish Gate validation cleanup
5. `a8637a4` Resolve final Gate review comments
6. `706dad1` fix(ci): handle expected Gate rejection under bash errexit

(+ merge `dc8275b` y commits docs/otros no-Gate en el rango completo de 10).

## Diffstat `f877f2e..dc8275b` (Gate paths)
18 files, **+1167 / −528** (incluye workflow). Sin workflow: ~+1153/−503.

Material:
- **Refactor layout:** módulos planos → package `waipl_gate/` + shims `from waipl_gate.* import *`
- **NUEVO:** `waipl_gate/case_schema.py`, `case_schema.json`, `validate_repo.py`
- **receipt.py:** seal SHA-256 → **HMAC-SHA256** (`SENTINEL_GATE_HMAC_KEY`); schema v1.1 (`issued_at`/`expires_at`/`issuer`/`receipt_version`); `closure_entry_point` → `waipl_gate.gate_close.close_case`; verify exige match exacto LIVE_MATCH_FIELDS
- **gate_evaluate.py:** `validate_case`; `human_acceptance` deja de ser bool → objeto con `approved`; añade `human_acceptance_ok`
- **gate_close.py:** propaga force flags a `close_case_file`; valida case
- **final_state.py:** `validate_case`; trace incluye `human_acceptance`; entry_point package path
- **tests / CI:** ampliación adversarial + gate-v1.yml bash errexit

## Will App vendor (Production `d76f991`)
- `SOURCE.md` / `GATE_MANIFEST.json`: pin = `f877f2e20b65de64a68ff98aff752b1bc3c23d2c`
- Core vendored (hashes = pin SENTINEL exactos):
  - `gate_close.py` `c09ca663…`
  - `gate_evaluate.py` `c3f6d063…`
  - `final_state.py` `4a79f29b…`
  - `receipt.py` `e46b3fcb…`
- Will-only (no Gate tip): `will_app_adapter.py`, `gate_http_auth.py`, bridge TS, tests integración

## Si se re-vendor desde `dc8275b` / tip
Aterrizarían: package layout, case_schema estricto, receipt HMAC+TTL, semántica human_acceptance, validate_repo (SENTINEL-side), tests tip — **incompatible** con adapter/bridge actuales sin cutover coordinado.
