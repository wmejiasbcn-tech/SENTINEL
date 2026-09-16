#!/usr/bin/env python3
"""WAIPL Verification Gate v1.0 — evaluador de barrera de cierre (SENTINEL)."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

PENDING = {
    "PARCIAL",
    "DESCONOCIDO",
    "NO_VERIFICADO",
    "NO VERIFICADO",
    "UNKNOWN",
    "PENDING",
    "INCOMPLETE",
    "NO-VERIFICADO",
}


def _norm(value: Any) -> str:
    return str(value or "").strip().upper().replace("-", "_").replace(" ", "_")


def _pending_state(estado: Any) -> bool:
    n = _norm(estado)
    n_spaces = str(estado or "").strip().upper()
    if n in {_norm(x) for x in PENDING} or n_spaces in PENDING:
        return True
    if "NO_VERIFICADO" in n or n_spaces == "NO VERIFICADO":
        return True
    return False


def evaluate(case: dict[str, Any]) -> dict[str, Any]:
    """Aplica la barrera Gate v1.0. No altera Vár/Yata."""
    pieces = {
        "resultado": bool(case.get("resultado")),
        "evidencia": bool(case.get("evidencia")),
        "verificacion": bool(case.get("verificacion")),
        "dictamen": bool(case.get("dictamen")),
    }
    reqs = case.get("requisitos_obligatorios") or []
    pending = []
    for r in reqs:
        if not isinstance(r, dict):
            pending.append({"id": str(r), "estado": "NO_VERIFICADO", "reason": "malformed"})
            continue
        if _pending_state(r.get("estado")):
            pending.append(
                {
                    "id": r.get("id") or r.get("nombre") or "?",
                    "estado": r.get("estado"),
                }
            )

    pieces_ok = all(pieces.values())
    no_pending = len(pending) == 0
    closed = pieces_ok and no_pending and len(reqs) > 0

    if len(reqs) == 0:
        closed = False

    if closed:
        semaforo = "VERDE"
        open_flag = False
    else:
        semaforo = "AMARILLO"
        open_flag = True

    return {
        "gate": "WAIPL_VERIFICATION_GATE_v1.0",
        "case_id": case.get("id"),
        "pieces": pieces,
        "pieces_ok": pieces_ok,
        "requisitos_obligatorios_count": len(reqs),
        "pending_mandatory": pending,
        "semaforo": semaforo,
        "CLOSED": closed,
        "OPEN": open_flag,
        "jurisdicciones": {
            "Var": "verdad / auditoría de agentes-resultados-fuentes",
            "Yata": "auditoría de validadores (no de agentes)",
            "SENTINEL": "contraste N1 + aplicación de esta puerta",
        },
    }


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("uso: gate_evaluate.py <case.json>", file=sys.stderr)
        return 2
    path = Path(argv[1])
    case = json.loads(path.read_text(encoding="utf-8"))
    result = evaluate(case)
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    print()
    return 0 if result["CLOSED"] else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
