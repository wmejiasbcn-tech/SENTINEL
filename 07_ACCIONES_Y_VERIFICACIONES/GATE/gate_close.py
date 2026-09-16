#!/usr/bin/env python3
"""
Único punto de cierre operacional SENTINEL bajo WAIPL Verification Gate v1.0.

Ningún circuito puede declarar VERDE/CLOSED=true sin pasar por close_case().
Cualquier intento de forzar cierre se ignora: gobierna únicamente gate_evaluate.
"""

from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from gate_evaluate import evaluate

# Marcador interno: solo close_case puede emitir VERDE/CLOSED
_AUTHORIZED_CLOSE_TOKEN = object()


class GateBypassError(PermissionError):
    """Se intentó cerrar en VERDE sin autorización del Gate."""


def _receipt(case: dict[str, Any], decision: dict[str, Any]) -> dict[str, Any]:
    payload = json.dumps({"case": case, "decision": decision}, sort_keys=True, ensure_ascii=False)
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    return {
        "gate": "WAIPL_VERIFICATION_GATE_v1.0",
        "entry_point": "gate_close.close_case",
        "timestamp_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "case_id": case.get("id"),
        "semaforo": decision["semaforo"],
        "CLOSED": decision["CLOSED"],
        "OPEN": decision["OPEN"],
        "sha256": digest,
        "pending_mandatory": decision.get("pending_mandatory", []),
    }


def close_case(
    case: dict[str, Any],
    *,
    force_verde: bool = False,
    force_closed: bool = False,
    desired_semaforo: str | None = None,
    _token: object | None = None,
) -> dict[str, Any]:
    """
    Única API pública de cierre.

    force_verde / force_closed / desired_semaforo se aceptan solo para que los
    tests demuestren el bypass: se IGNORAN siempre. El Gate manda.
    """
    decision = evaluate(case)

    # Defensa en profundidad: aunque un caller inyectara campos, se sobrescriben
    decision["CLOSED"] = bool(decision.get("CLOSED")) and not decision.get("pending_mandatory")
    if decision.get("pending_mandatory") or not decision.get("pieces_ok"):
        decision["semaforo"] = "AMARILLO"
        decision["CLOSED"] = False
        decision["OPEN"] = True

    # Cualquier intento de forzar VERDE queda bloqueado si el Gate no autoriza
    if force_verde or force_closed or (desired_semaforo and str(desired_semaforo).upper() == "VERDE"):
        if not decision["CLOSED"]:
            decision["bypass_attempt"] = {
                "force_verde": force_verde,
                "force_closed": force_closed,
                "desired_semaforo": desired_semaforo,
                "blocked": True,
                "reason": "Gate no autoriza CLOSED=true",
            }
            # No elevar: permanece AMARILLO/OPEN
            decision["semaforo"] = "AMARILLO"
            decision["CLOSED"] = False
            decision["OPEN"] = True

    decision["receipt"] = _receipt(case, decision)
    decision["closure_entry_point"] = "gate_close.close_case"
    decision["authorized"] = decision["CLOSED"]
    # token reservado (no usado por callers externos)
    _ = _token
    return decision


def close_case_file(path: str | Path, receipt_path: str | Path | None = None) -> dict[str, Any]:
    path = Path(path)
    case = json.loads(path.read_text(encoding="utf-8"))
    decision = close_case(case)
    out = receipt_path or path.with_suffix(path.suffix + ".gate_receipt.json")
    Path(out).write_text(json.dumps(decision["receipt"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    decision["receipt_path"] = str(out)
    return decision


def assert_no_alternate_close_api() -> None:
    """Garantiza que este módulo no expone helpers que seteen CLOSED sin evaluate."""
    forbidden = ["set_closed", "force_close", "mark_verde", "declare_verde"]
    g = globals()
    for name in forbidden:
        if name in g:
            raise GateBypassError(f"API prohibida presente: {name}")


assert_no_alternate_close_api()


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("uso: gate_close.py <case.json> [--force-verde]", file=sys.stderr)
        return 2
    force = "--force-verde" in argv
    args = [a for a in argv[1:] if not a.startswith("--")]
    decision = close_case_file(args[0]) if not force else close_case(
        json.loads(Path(args[0]).read_text(encoding="utf-8")), force_verde=True
    )
    json.dump(decision, sys.stdout, ensure_ascii=False, indent=2)
    print()
    return 0 if decision["CLOSED"] else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
