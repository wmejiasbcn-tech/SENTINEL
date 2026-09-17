#!/usr/bin/env python3
"""AUDITORÍA ADVERSARIAL DE BYPASS — WAIPL Verification Gate v1.0."""

from __future__ import annotations

import copy
import json
import os
import unittest
from pathlib import Path

os.environ.setdefault("SENTINEL_GATE_HMAC_KEY", "sentinel-gate-fixture-key")

from waipl_gate.case_schema import CaseValidationError
from waipl_gate.gate_close import accept_closure, close_case
from waipl_gate.receipt import _seal, case_fingerprint, verify_receipt

HERE = Path(__file__).resolve().parent
CASES = HERE / "cases"


def load(name: str) -> dict:
    return json.loads((CASES / name).read_text(encoding="utf-8"))


class TestAdversarialBypass(unittest.TestCase):
    def test_A_inject_verde_closed_in_case_is_rejected(self):
        case = load("AUD-LAB-CARLA-01.json")
        case["state"] = "VERDE"
        case["closed"] = True
        case["CLOSED"] = True
        case["gate_status"] = "AUTHORIZED"
        with self.assertRaises(CaseValidationError):
            close_case(case)

    def test_B_force_flags(self):
        case = load("AUD-LAB-CARLA-01.json")
        out = close_case(case, force_verde=True, force_closed=True, desired_semaforo="VERDE")
        self.assertFalse(out["closed"])
        self.assertTrue(out["bypass_attempt"]["blocked"])

    def test_C_checklist_mutation_after_good_snapshot(self):
        case = load("CASE_ALL_CONFORME.json")
        good = close_case(case)
        self.assertTrue(good["closed"])
        mutated = copy.deepcopy(case)
        mutated["requisitos_obligatorios"][0]["estado"] = "PARCIAL"
        out = close_case(mutated)
        self.assertFalse(out["closed"])
        self.assertEqual(out["gate_status"], "BLOCKED")

    def test_D_reuse_receipt_on_different_case(self):
        good_case = load("CASE_ALL_CONFORME.json")
        bad_case = load("AUD-LAB-CARLA-01.json")
        good = close_case(good_case)
        receipt = good["receipt"]
        check = verify_receipt(bad_case, receipt)
        self.assertFalse(check["valid"])
        self.assertFalse(check["authorized_closure"])
        self.assertTrue(
            any(reason in check["reasons"] for reason in ["case_id_mismatch", "case_fingerprint_mismatch"])
        )
        acc = accept_closure(bad_case, receipt)
        self.assertFalse(acc["accepted"])
        self.assertFalse(acc["closed"])
        self.assertTrue(acc["bypass_rejected"])

    def test_E_forged_receipt_claims_closed_nonconformant_case(self):
        case = load("AUD-LAB-CARLA-01.json")
        forged = {
            "contract": "WAIPL_VERIFICATION_GATE_v1.0_FINAL_STATE_CONTRACT",
            "receipt_version": "1.1",
            "case_id": case["id"],
            "case_fingerprint": case_fingerprint(case),
            "state": "VERDE",
            "closed": True,
            "open": False,
            "result_status": "PRESENTE",
            "evidence_status": "SUFICIENTE",
            "verification_status": "CONFORME",
            "dictamen_status": "CERRABLE",
            "gate_status": "AUTHORIZED",
            "mandatory_requirements_pending": [],
            "gate_ref": "forged",
            "issued_at": "2026-09-17T13:00:00Z",
            "expires_at": "2026-10-17T13:00:00Z",
            "issuer": "SENTINEL/WAIPL Verification Gate",
            "closure_entry_point": "waipl_gate.gate_close.close_case",
            "seal": "deadbeef",
        }
        check = verify_receipt(case, forged)
        self.assertFalse(check["authorized_closure"])
        self.assertTrue(
            any(reason.startswith("field_mismatch:") for reason in check["reasons"]) or "seal_invalid" in check["reasons"]
        )
        acc = accept_closure(case, forged)
        self.assertFalse(acc["closed"])

    def test_F_forged_receipt_for_conformant_case_is_rejected(self):
        case = load("CASE_ALL_CONFORME.json")
        legit = close_case(case)
        forged = {k: v for k, v in legit["receipt"].items() if k != "seal"}
        forged["seal"] = "forged-without-secret"
        check = verify_receipt(case, forged)
        self.assertFalse(check["valid"])
        self.assertIn("seal_invalid", check["reasons"])
        acc = accept_closure(case, forged)
        self.assertFalse(acc["accepted"])

    def test_G_tamper_seal_after_bind(self):
        case = load("CASE_ALL_CONFORME.json")
        out = close_case(case)
        receipt = copy.deepcopy(out["receipt"])
        receipt["seal"] = "tampered"
        check = verify_receipt(case, receipt)
        self.assertFalse(check["valid"])
        self.assertIn("seal_invalid", check["reasons"])

    def test_H_missing_receipt(self):
        case = load("CASE_ALL_CONFORME.json")
        acc = accept_closure(case, None)  # type: ignore[arg-type]
        self.assertFalse(acc["accepted"])
        self.assertFalse(acc["closed"])

    def test_I_descontextualized_receipt_same_id_different_body(self):
        case = load("CASE_ALL_CONFORME.json")
        out = close_case(case)
        receipt = out["receipt"]
        other = copy.deepcopy(case)
        other["evidence_refs"] = ["tampered-evidence"]
        check = verify_receipt(other, receipt)
        self.assertFalse(check["valid"])
        self.assertIn("case_fingerprint_mismatch", check["reasons"])
        acc = accept_closure(other, receipt)
        self.assertFalse(acc.get("authorized_closure", acc["accepted"]))

    def test_J_evaluate_alone_does_not_close(self):
        from waipl_gate.gate_evaluate import evaluate

        case = load("CASE_ALL_CONFORME.json")
        ev = evaluate(case)
        self.assertNotIn("closed", ev)
        self.assertNotIn("gate_status", ev)

    def test_K_invariant_forall_known_paths(self):
        for name in ("AUD-LAB-CARLA-01.json", "CASE_ALL_CONFORME.json"):
            out = close_case(load(name))
            if out["closed"]:
                self.assertEqual(out["gate_status"], "AUTHORIZED")
                self.assertEqual(out["state"], "VERDE")
            if out["gate_status"] == "BLOCKED":
                self.assertFalse(out["closed"])

    def test_L_expired_receipt_rejected(self):
        case = load("CASE_ALL_CONFORME.json")
        out = close_case(case)
        receipt = copy.deepcopy(out["receipt"])
        receipt["expires_at"] = "2020-01-01T00:00:00Z"
        check = verify_receipt(case, receipt)
        self.assertFalse(check["valid"])
        self.assertIn("receipt_expired", check["reasons"])
        acc = accept_closure(case, receipt)
        self.assertFalse(acc["accepted"])
        self.assertFalse(acc["closed"])

    def test_M_authentic_expired_receipt_rejected(self):
        case = load("CASE_ALL_CONFORME.json")
        out = close_case(case)
        receipt = copy.deepcopy(out["receipt"])
        receipt["issued_at"] = "2020-01-01T00:00:00Z"
        receipt["expires_at"] = "2020-01-31T00:00:00Z"
        receipt["seal"] = _seal({k: receipt[k] for k in receipt if k != "seal"})
        check = verify_receipt(case, receipt)
        self.assertFalse(check["valid"])
        self.assertIn("receipt_expired", check["reasons"])
        self.assertNotIn("seal_invalid", check["reasons"])
        acc = accept_closure(case, receipt)
        self.assertFalse(acc["accepted"])
        self.assertFalse(acc["closed"])


if __name__ == "__main__":
    unittest.main()
