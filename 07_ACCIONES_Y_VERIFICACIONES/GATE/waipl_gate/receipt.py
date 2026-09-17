#!/usr/bin/env python3
"""Receipt binding — impide reutilizar o forjar cierres sin Gate."""

from __future__ import annotations

import hashlib
import hmac
import json
import os
from datetime import datetime, timedelta, timezone
from typing import Any

from .case_schema import CaseValidationError, validate_case

RECEIPT_VERSION = "1.1"
RECEIPT_CONTRACT = "WAIPL_VERIFICATION_GATE_v1.0_FINAL_STATE_CONTRACT"
HMAC_ENV_VAR = "SENTINEL_GATE_HMAC_KEY"
DEFAULT_ISSUER = "SENTINEL/WAIPL Verification Gate"
CANONICAL_RECEIPT_FIELDS = (
    "contract",
    "receipt_version",
    "case_id",
    "case_fingerprint",
    "state",
    "closed",
    "open",
    "result_status",
    "evidence_status",
    "verification_status",
    "dictamen_status",
    "gate_status",
    "mandatory_requirements_pending",
    "gate_ref",
    "issued_at",
    "expires_at",
    "issuer",
    "closure_entry_point",
)
LIVE_MATCH_FIELDS = (
    "contract",
    "receipt_version",
    "case_id",
    "case_fingerprint",
    "state",
    "closed",
    "open",
    "result_status",
    "evidence_status",
    "verification_status",
    "dictamen_status",
    "gate_status",
    "mandatory_requirements_pending",
    "gate_ref",
    "issuer",
    "closure_entry_point",
)


def _get_hmac_key() -> bytes:
    value = os.environ.get(HMAC_ENV_VAR)
    if not value:
        raise RuntimeError(f"missing required environment variable: {HMAC_ENV_VAR}")
    return value.encode("utf-8")


def _parse_utc(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)


def _canonical_json(data: dict[str, Any]) -> str:
    return json.dumps(data, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def _seal(payload: dict[str, Any]) -> str:
    return hmac.new(_get_hmac_key(), _canonical_json(payload).encode("utf-8"), hashlib.sha256).hexdigest()


def case_fingerprint(case: dict[str, Any]) -> str:
    """Huella canónica del case."""
    validate_case(case)
    material = {
        "id": case.get("id"),
        "resultado": bool(case.get("resultado")),
        "evidencia": bool(case.get("evidencia")),
        "verificacion": bool(case.get("verificacion")),
        "dictamen": bool(case.get("dictamen")),
        "requisitos_obligatorios": case.get("requisitos_obligatorios") or [],
        "confirmed_failure": bool(case.get("confirmed_failure") or case.get("rojo")),
        "human_acceptance_required": bool(case.get("human_acceptance_required")),
        "human_acceptance": case.get("human_acceptance"),
        "ambiguous_final_state": bool(case.get("ambiguous_final_state")),
        "result_ref": case.get("result_ref"),
        "evidence_refs": case.get("evidence_refs") or [],
        "dictamen_ref": case.get("dictamen_ref"),
    }
    return hashlib.sha256(_canonical_json(material).encode("utf-8")).hexdigest()


def _canonical_receipt_payload(final_state: dict[str, Any], case: dict[str, Any]) -> dict[str, Any]:
    issued_at = final_state["timestamp_utc"]
    expires_at = (_parse_utc(issued_at) + timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%SZ")
    return {
        "contract": RECEIPT_CONTRACT,
        "receipt_version": RECEIPT_VERSION,
        "case_id": case.get("id"),
        "case_fingerprint": case_fingerprint(case),
        "state": final_state["state"],
        "closed": final_state["closed"],
        "open": final_state["open"],
        "result_status": final_state["result_status"],
        "evidence_status": final_state["evidence_status"],
        "verification_status": final_state["verification_status"],
        "dictamen_status": final_state["dictamen_status"],
        "gate_status": final_state["gate_status"],
        "mandatory_requirements_pending": final_state["mandatory_requirements_pending"],
        "gate_ref": final_state["gate_ref"],
        "issued_at": issued_at,
        "expires_at": expires_at,
        "issuer": DEFAULT_ISSUER,
        "closure_entry_point": "waipl_gate.gate_close.close_case",
    }


def bind_receipt(final_state: dict[str, Any], case: dict[str, Any]) -> dict[str, Any]:
    payload = _canonical_receipt_payload(final_state, case)
    receipt = dict(payload)
    receipt["seal"] = _seal(payload)
    return receipt


def verify_receipt(case: dict[str, Any], receipt: dict[str, Any]) -> dict[str, Any]:
    """Valida receipt, HMAC, caducidad y coherencia exacta con el Gate live."""
    from .final_state import build_final_state

    reasons: list[str] = []
    if not isinstance(receipt, dict):
        return {"valid": False, "authorized_closure": False, "reasons": ["receipt_not_object"]}

    try:
        validate_case(case)
    except CaseValidationError as exc:
        return {"valid": False, "authorized_closure": False, "reasons": [f"invalid_case:{exc}"]}

    missing_fields = [field for field in (*CANONICAL_RECEIPT_FIELDS, "seal") if field not in receipt]
    if missing_fields:
        return {
            "valid": False,
            "authorized_closure": False,
            "reasons": [f"missing_receipt_fields:{','.join(missing_fields)}"],
        }

    fp = case_fingerprint(case)
    if receipt.get("case_id") != case.get("id"):
        reasons.append("case_id_mismatch")
    if receipt.get("case_fingerprint") != fp:
        reasons.append("case_fingerprint_mismatch")

    try:
        expected_seal = _seal({field: receipt[field] for field in CANONICAL_RECEIPT_FIELDS})
        if not hmac.compare_digest(str(receipt.get("seal")), expected_seal):
            reasons.append("seal_invalid")
    except RuntimeError:
        reasons.append("seal_key_unavailable")

    try:
        expires_at = _parse_utc(str(receipt.get("expires_at")))
        if expires_at < datetime.now(timezone.utc):
            reasons.append("receipt_expired")
    except ValueError:
        reasons.append("expires_at_invalid")

    try:
        _parse_utc(str(receipt.get("issued_at")))
    except ValueError:
        reasons.append("issued_at_invalid")

    live = build_final_state(case)
    expected_payload = _canonical_receipt_payload(live, case)
    for field in LIVE_MATCH_FIELDS:
        if receipt.get(field) != expected_payload.get(field):
            reasons.append(f"field_mismatch:{field}")

    valid = len(reasons) == 0
    authorized = valid and live.get("closed") is True and live.get("gate_status") == "AUTHORIZED"
    return {
        "valid": valid,
        "authorized_closure": authorized,
        "reasons": reasons,
        "live_gate_status": live.get("gate_status"),
        "live_closed": live.get("closed"),
    }


def assert_closure_authorized(case: dict[str, Any], receipt: dict[str, Any]) -> None:
    result = verify_receipt(case, receipt)
    if not result["authorized_closure"]:
        raise PermissionError(f"closure not authorized: {result['reasons']}")
