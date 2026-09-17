#!/usr/bin/env python3

from __future__ import annotations

import json
import os
import unittest
from pathlib import Path

os.environ.setdefault("SENTINEL_GATE_HMAC_KEY", "sentinel-gate-fixture-key")

from waipl_gate.case_schema import CaseValidationError
from waipl_gate.final_state import REQUIRED_FIELDS, build_final_state
from waipl_gate.gate_close import assert_no_alternate_close_api, close_case
from waipl_gate.receipt import case_fingerprint

HERE = Path(__file__).resolve().parent
CASES = HERE / "cases"


class TestFinalStateContract(unittest.TestCase):
    def test_aud_lab_carla_01_contract(self):
        case = json.loads((CASES / "AUD-LAB-CARLA-01.json").read_text(encoding="utf-8"))
        out = close_case(case)
        for field in REQUIRED_FIELDS:
            self.assertIn(field, out)
        self.assertEqual(out["state"], "AMARILLO")
        self.assertFalse(out["closed"])
        self.assertTrue(out["open"])
        self.assertEqual(out["gate_status"], "BLOCKED")

    def test_all_conforme_contract(self):
        case = json.loads((CASES / "CASE_ALL_CONFORME.json").read_text(encoding="utf-8"))
        out = close_case(case)
        self.assertEqual(out["state"], "VERDE")
        self.assertTrue(out["closed"])
        self.assertEqual(out["gate_status"], "AUTHORIZED")
        self.assertEqual(out["receipt"]["case_fingerprint"], case_fingerprint(case))
        self.assertEqual(out["receipt"]["receipt_version"], "1.1")
        self.assertIn("expires_at", out["receipt"])

    def test_bypass_blocked(self):
        case = json.loads((CASES / "AUD-LAB-CARLA-01.json").read_text(encoding="utf-8"))
        out = close_case(case, force_verde=True, force_closed=True, desired_semaforo="VERDE")
        self.assertFalse(out["closed"])
        self.assertEqual(out["gate_status"], "BLOCKED")

    def test_injected_closed_rejected(self):
        case = json.loads((CASES / "AUD-LAB-CARLA-01.json").read_text(encoding="utf-8"))
        case["closed"] = True
        case["state"] = "VERDE"
        with self.assertRaises(CaseValidationError):
            close_case(case)

    def test_rojo_cannot_close(self):
        case = {
            "id": "fail",
            "resultado": True,
            "evidencia": True,
            "verificacion": True,
            "dictamen": True,
            "result_ref": "fail:result",
            "evidence_refs": ["fail:evidence"],
            "dictamen_ref": "fail:dictamen",
            "confirmed_failure": True,
            "requisitos_obligatorios": [{"id": "x", "estado": "CONFORME"}],
        }
        out = close_case(case)
        self.assertEqual(out["state"], "ROJO")
        self.assertFalse(out["closed"])

    def test_fail_safe_ambiguous(self):
        out = build_final_state(
            {
                "id": "amb",
                "resultado": False,
                "evidencia": False,
                "verificacion": False,
                "dictamen": False,
                "result_ref": "amb:result",
                "evidence_refs": ["amb:evidence"],
                "dictamen_ref": "amb:dictamen",
                "requisitos_obligatorios": [{"id": "ambiguous", "estado": "DESCONOCIDO"}],
                "ambiguous_final_state": True,
            }
        )
        self.assertFalse(out["closed"])
        self.assertEqual(out["gate_status"], "BLOCKED")

    def test_human_acceptance_required_blocks_without_artifact(self):
        case = json.loads((CASES / "CASE_ALL_CONFORME.json").read_text(encoding="utf-8"))
        case["human_acceptance_required"] = True
        with self.assertRaises(CaseValidationError):
            close_case(case)

    def test_human_acceptance_required_accepts_signed_artifact(self):
        case = json.loads((CASES / "CASE_ALL_CONFORME.json").read_text(encoding="utf-8"))
        case["human_acceptance_required"] = True
        case["human_acceptance"] = {
            "approved": True,
            "actor": "wmn",
            "approved_at": "2026-09-17T13:00:00Z",
            "reason": "cierre autorizado",
            "evidence_ref": "ACTA-HITL-001",
            "signature": "signed-by-wmn",
        }
        out = close_case(case)
        self.assertTrue(out["closed"])

    def test_invalid_case_missing_refs_fails(self):
        case = {
            "id": "bad",
            "resultado": True,
            "evidencia": True,
            "verificacion": True,
            "dictamen": True,
            "requisitos_obligatorios": [],
        }
        with self.assertRaises(CaseValidationError):
            close_case(case)

    def test_no_forbidden_apis(self):
        assert_no_alternate_close_api()


if __name__ == "__main__":
    unittest.main()
