#!/usr/bin/env python3
"""WAIPL Verification Gate v1.0 — evaluación de piezas y requisitos."""

from __future__ import annotations

from typing import Any

from .case_schema import validate_case

PENDING = {
    "PARCIAL",
    "DESCONOCIDO",
    "NO_VERIFICADO",
    "NO VERIFICADO",
    "UNKNOWN",
    "PENDING",
    "INCOMPLETE",
    "NO-VERIFICADO",
    "AUSENTE",
    "INSUFICIENTE",
    "NO_CERRABLE",
    "NO CERRABLE",
}


def _norm(value: Any) -> str:
    return str(value or "").strip().upper().replace("-", "_").replace(" ", "_")


def pending_state(estado: Any) -> bool:
    n = _norm(estado)
    raw = str(estado or "").strip().upper()
    if n in {_norm(x) for x in PENDING} or raw in PENDING:
        return True
    if "NO_VERIFICADO" in n or "NO_CERRABLE" in n:
        return True
    return False


def worst_verification_status(pending: list[dict[str, Any]], reqs: list[dict[str, Any]]) -> str:
    if not reqs:
        return "NO_VERIFICADO"
    if not pending:
        return "CONFORME"
    states = {_norm(p.get("estado")) for p in pending}
    if "PARCIAL" in states:
        return "PARCIAL"
    if "DESCONOCIDO" in states or "UNKNOWN" in states:
        return "DESCONOCIDO"
    return "NO_VERIFICADO"


def evaluate(case: dict[str, Any]) -> dict[str, Any]:
    """Evalúa piezas y requisitos. No emite el contrato final."""
    validate_case(case)

    if case.get("ambiguous_final_state"):
        return {
            "gate": "WAIPL_VERIFICATION_GATE_v1.0",
            "case_id": case.get("id"),
            "ambiguous": True,
            "pieces": {"resultado": False, "evidencia": False, "verificacion": False, "dictamen": False},
            "pieces_ok": False,
            "pending_mandatory": [{"id": "_ambiguous", "estado": "DESCONOCIDO"}],
            "confirmed_failure": False,
            "human_acceptance_required": bool(case.get("human_acceptance_required")),
            "human_acceptance": case.get("human_acceptance"),
        }

    pieces = {
        "resultado": bool(case.get("resultado")),
        "evidencia": bool(case.get("evidencia")),
        "verificacion": bool(case.get("verificacion")),
        "dictamen": bool(case.get("dictamen")),
    }
    reqs = case.get("requisitos_obligatorios") or []
    pending: list[dict[str, Any]] = []
    for r in reqs:
        if pending_state(r.get("estado")):
            pending.append({"id": r.get("id") or r.get("nombre") or "?", "estado": r.get("estado")})

    confirmed_failure = bool(case.get("confirmed_failure") or case.get("rojo"))
    human_req = bool(case.get("human_acceptance_required"))
    human_acceptance = case.get("human_acceptance")
    human_ok = isinstance(human_acceptance, dict) and human_acceptance.get("approved") is True

    return {
        "gate": "WAIPL_VERIFICATION_GATE_v1.0",
        "case_id": case.get("id"),
        "ambiguous": False,
        "pieces": pieces,
        "pieces_ok": all(pieces.values()),
        "requisitos_obligatorios_count": len(reqs),
        "pending_mandatory": pending,
        "verification_status": worst_verification_status(pending, reqs),
        "confirmed_failure": confirmed_failure,
        "human_acceptance_required": human_req,
        "human_acceptance": human_acceptance,
        "human_acceptance_ok": human_ok,
        "evidence_refs": case.get("evidence_refs") or [],
        "result_ref": case.get("result_ref"),
        "dictamen_ref": case.get("dictamen_ref"),
    }
