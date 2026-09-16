#!/usr/bin/env python3
from __future__ import annotations

import json
import unittest
from pathlib import Path

from final_state import REQUIRED_FIELDS, build_final_state
from gate_close import assert_no_alternate_close_api, close_case

HERE = Path(__file__).resolve().parent
CASES = HERE / "cases"


class TestFinalStateContract(unittest.TestCase):
    def test_aud_lab_carla_01_contract(self):
        case = json.loads((CASES / "AUD-LAB-CARLA-01.json").read_text(encoding="utf-8"))
        out = close_case(case)
        for f in REQUIRED_FIELDS:
            self.assertIn(f, out)
        self.assertNotEqual(out["state"], "VERDE")
        self.assertFalse(out["closed"])
        self.assertTrue(out["open"])
        self.assertEqual(out["gate_status"], "BLOCKED")
        self.assertEqual(out["state"], "AMARILLO")
        ids = {p["id"] for p in out["mandatory_requirements_pending"]}
        self.assertIn("codex_ley_como_fichero", ids)
        self.assertIn("corpus_audio_este_chat", ids)

    def test_all_conforme_contract(self):
        case = json.loads((CASES / "CASE_ALL_CONFORME.json").read_text(encoding="utf-8"))
        out = close_case(case)
        self.assertEqual(out["state"], "VERDE")
        self.assertTrue(out["closed"])
        self.assertFalse(out["open"])
        self.assertEqual(out["gate_status"], "AUTHORIZED")
        self.assertEqual(out["result_status"], "PRESENTE")
        self.assertEqual(out["evidence_status"], "SUFICIENTE")
        self.assertEqual(out["verification_status"], "CONFORME")
        self.assertEqual(out["dictamen_status"], "CERRABLE")
        self.assertEqual(out["mandatory_requirements_pending"], [])

    def test_bypass_blocked(self):
        case = json.loads((CASES / "AUD-LAB-CARLA-01.json").read_text(encoding="utf-8"))
        out = close_case(case, force_verde=True, force_closed=True, desired_semaforo="VERDE")
        self.assertFalse(out["closed"])
        self.assertEqual(out["gate_status"], "BLOCKED")
        self.assertTrue(out.get("bypass_attempt", {}).get("blocked"))

    def test_injected_closed_ignored(self):
        case = json.loads((CASES / "AUD-LAB-CARLA-01.json").read_text(encoding="utf-8"))
        case["closed"] = True
        case["state"] = "VERDE"
        case["CLOSED"] = True
        out = close_case(case)
        self.assertFalse(out["closed"])
        self.assertEqual(out["gate_status"], "BLOCKED")

    def test_rojo_cannot_close(self):
        case = {
            "id": "fail",
            "resultado": True,
            "evidencia": True,
            "verificacion": True,
            "dictamen": True,
            "confirmed_failure": True,
            "requisitos_obligatorios": [{"id": "x", "estado": "CONFORME"}],
        }
        out = close_case(case)
        self.assertEqual(out["state"], "ROJO")
        self.assertFalse(out["closed"])
        self.assertEqual(out["gate_status"], "BLOCKED")

    def test_fail_safe_ambiguous(self):
        out = build_final_state({"id": "amb", "ambiguous_final_state": True})
        self.assertFalse(out["closed"])
        self.assertTrue(out["open"])
        self.assertEqual(out["gate_status"], "BLOCKED")
        self.assertNotEqual(out["state"], "VERDE")

    def test_human_acceptance_required_blocks(self):
        case = json.loads((CASES / "CASE_ALL_CONFORME.json").read_text(encoding="utf-8"))
        case["human_acceptance_required"] = True
        case["human_acceptance"] = False
        out = close_case(case)
        self.assertFalse(out["closed"])
        self.assertEqual(out["gate_status"], "BLOCKED")

    def test_no_forbidden_apis(self):
        assert_no_alternate_close_api()


if __name__ == "__main__":
    unittest.main()
