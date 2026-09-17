#!/usr/bin/env python3
"""Formal input contract for WAIPL Verification Gate cases."""

from __future__ import annotations

from datetime import datetime
from typing import Any

CASE_SCHEMA: dict[str, Any] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://waipl.local/sentinel/gate/case.schema.json",
    "title": "WAIPL Verification Gate Case",
    "type": "object",
    "additionalProperties": False,
    "required": [
        "id",
        "resultado",
        "evidencia",
        "verificacion",
        "dictamen",
        "result_ref",
        "evidence_refs",
        "dictamen_ref",
        "requisitos_obligatorios",
    ],
    "properties": {
        "id": {"type": "string", "minLength": 1},
        "resultado": {"type": "boolean"},
        "evidencia": {"type": "boolean"},
        "verificacion": {"type": "boolean"},
        "dictamen": {"type": "boolean"},
        "result_ref": {"type": "string", "minLength": 1},
        "evidence_refs": {
            "type": "array",
            "items": {"type": "string", "minLength": 1},
            "minItems": 1,
        },
        "dictamen_ref": {"type": "string", "minLength": 1},
        "requisitos_obligatorios": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["estado"],
                "properties": {
                    "id": {"type": "string", "minLength": 1},
                    "nombre": {"type": "string", "minLength": 1},
                    "estado": {"type": "string", "minLength": 1},
                    "reason": {"type": "string", "minLength": 1},
                },
                "anyOf": [{"required": ["id"]}, {"required": ["nombre"]}],
            },
        },
        "confirmed_failure": {"type": "boolean"},
        "rojo": {"type": "boolean"},
        "ambiguous_final_state": {"type": "boolean"},
        "human_acceptance_required": {"type": "boolean"},
        "human_acceptance": {
            "type": ["object", "null"],
            "additionalProperties": False,
            "required": ["approved", "actor", "approved_at", "reason", "evidence_ref"],
            "properties": {
                "approved": {"type": "boolean"},
                "actor": {"type": "string", "minLength": 1},
                "approved_at": {"type": "string", "format": "date-time", "minLength": 1},
                "reason": {"type": "string", "minLength": 1},
                "evidence_ref": {"type": "string", "minLength": 1},
                "signature": {"type": "string", "minLength": 1},
            },
        },
    },
}

FORBIDDEN_INPUT_FIELDS = {"state", "closed", "open", "CLOSED", "OPEN", "semaforo", "gate_status", "receipt"}
ALLOWED_TOP_LEVEL_FIELDS = set(CASE_SCHEMA["properties"]) | {"id", "resultado", "evidencia", "verificacion", "dictamen", "result_ref", "evidence_refs", "dictamen_ref", "requisitos_obligatorios"}


class CaseValidationError(ValueError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise CaseValidationError(message)


def _is_non_empty_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _parse_datetime(value: str, field: str) -> None:
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise CaseValidationError(f"{field} must be ISO-8601") from exc


def validate_case(case: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(case, dict):
        raise CaseValidationError("case must be a JSON object")

    forbidden = sorted(FORBIDDEN_INPUT_FIELDS.intersection(case))
    _require(not forbidden, f"forbidden closure fields in case: {', '.join(forbidden)}")

    unknown = sorted(set(case) - ALLOWED_TOP_LEVEL_FIELDS)
    _require(not unknown, f"unknown top-level fields in case: {', '.join(unknown)}")

    for field in CASE_SCHEMA["required"]:
        _require(field in case, f"missing required field: {field}")

    for field in ("id", "result_ref", "dictamen_ref"):
        _require(_is_non_empty_text(case.get(field)), f"{field} must be a non-empty string")

    for field in ("resultado", "evidencia", "verificacion", "dictamen"):
        _require(isinstance(case.get(field), bool), f"{field} must be boolean")

    evidence_refs = case.get("evidence_refs")
    _require(isinstance(evidence_refs, list) and len(evidence_refs) >= 1, "evidence_refs must be a non-empty list")
    for idx, ref in enumerate(evidence_refs):
        _require(_is_non_empty_text(ref), f"evidence_refs[{idx}] must be a non-empty string")

    reqs = case.get("requisitos_obligatorios")
    _require(isinstance(reqs, list), "requisitos_obligatorios must be a list")
    for idx, req in enumerate(reqs):
        _require(isinstance(req, dict), f"requisitos_obligatorios[{idx}] must be an object")
        _require("estado" in req and _is_non_empty_text(req.get("estado")), f"requisitos_obligatorios[{idx}].estado is required")
        _require(
            _is_non_empty_text(req.get("id")) or _is_non_empty_text(req.get("nombre")),
            f"requisitos_obligatorios[{idx}] must include id or nombre",
        )
        extra_req = sorted(set(req) - {"id", "nombre", "estado", "reason"})
        _require(not extra_req, f"requisitos_obligatorios[{idx}] has unknown fields: {', '.join(extra_req)}")

    for field in ("confirmed_failure", "rojo", "ambiguous_final_state", "human_acceptance_required"):
        if field in case:
            _require(isinstance(case.get(field), bool), f"{field} must be boolean")

    acceptance = case.get("human_acceptance")
    _require(acceptance is None or isinstance(acceptance, dict), "human_acceptance must be object or null")
    if isinstance(acceptance, dict):
        required_fields = ["approved", "actor", "approved_at", "reason", "evidence_ref"]
        for field in required_fields:
            _require(field in acceptance, f"human_acceptance.{field} is required")
        _require(isinstance(acceptance.get("approved"), bool), "human_acceptance.approved must be boolean")
        for field in ("actor", "approved_at", "reason", "evidence_ref"):
            _require(_is_non_empty_text(acceptance.get(field)), f"human_acceptance.{field} must be a non-empty string")
        _parse_datetime(acceptance["approved_at"], "human_acceptance.approved_at")
        if "signature" in acceptance:
            _require(_is_non_empty_text(acceptance.get("signature")), "human_acceptance.signature must be a non-empty string")
        extra_acceptance = sorted(set(acceptance) - {"approved", "actor", "approved_at", "reason", "evidence_ref", "signature"})
        _require(not extra_acceptance, f"human_acceptance has unknown fields: {', '.join(extra_acceptance)}")

    if case.get("human_acceptance_required"):
        _require(isinstance(acceptance, dict), "human_acceptance_required=true requires human_acceptance object")
        _require(acceptance.get("approved") is True, "human_acceptance_required=true requires approved=true")
        _require(_is_non_empty_text(acceptance.get("signature")), "human_acceptance_required=true requires signature")

    return case
