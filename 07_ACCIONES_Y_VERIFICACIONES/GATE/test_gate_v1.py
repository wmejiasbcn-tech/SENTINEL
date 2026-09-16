#!/usr/bin/env python3
"""Tests Gate v1.0 — evaluador + cierre operacional obligatorio."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from gate_close import GateBypassError, assert_no_alternate_close_api, close_case, close_case_file
from gate_evaluate import evaluate

HERE = Path(__file__).resolve().parent
CASES = HERE / "cases"


class TestGateEvaluate(unittest.TestCase):
    def test_aud_lab_carla_01_cannot_close(self):
        case = json.loads((CASES / "AUD-LAB-CARLA-01.json").read_text(encoding="utf-8"))
        out = evaluate(case)
        self.assertEqual(out["semaforo"], "AMARILLO")
        self.assertFalse(out["CLOSED"])

    def test_all_conforme_closes_verde(self):
        case = json.loads((CASES / "CASE_ALL_CONFORME.json").read_text(encoding="utf-8"))
        out = evaluate(case)
        self.assertEqual(out["semaforo"], "VERDE")
        self.assertTrue(out["CLOSED"])


class TestGateCloseOperational(unittest.TestCase):
    """El Gate gobierna el cierre: no hay ruta alternativa a VERDE/CLOSED."""

    def test_close_aud_lab_carla_01(self):
        case = json.loads((CASES / "AUD-LAB-CARLA-01.json").read_text(encoding="utf-8"))
        out = close_case(case)
        self.assertEqual(out["semaforo"], "AMARILLO")
        self.assertFalse(out["CLOSED"])
        self.assertTrue(out["OPEN"])
        self.assertEqual(out["closure_entry_point"], "gate_close.close_case")
        self.assertIn("receipt", out)

    def test_bypass_force_verde_blocked(self):
        case = json.loads((CASES / "AUD-LAB-CARLA-01.json").read_text(encoding="utf-8"))
        out = close_case(case, force_verde=True, force_closed=True, desired_semaforo="VERDE")
        self.assertEqual(out["semaforo"], "AMARILLO")
        self.assertFalse(out["CLOSED"])
        self.assertTrue(out["OPEN"])
        self.assertTrue(out.get("bypass_attempt", {}).get("blocked"))

    def test_injected_closed_ignored(self):
        """Si el case JSON trae CLOSED/semaforo, evaluate/close no los usan como autoridad."""
        case = json.loads((CASES / "AUD-LAB-CARLA-01.json").read_text(encoding="utf-8"))
        case["CLOSED"] = True
        case["semaforo"] = "VERDE"
        out = close_case(case)
        self.assertFalse(out["CLOSED"])
        self.assertEqual(out["semaforo"], "AMARILLO")

    def test_close_all_conforme(self):
        case = json.loads((CASES / "CASE_ALL_CONFORME.json").read_text(encoding="utf-8"))
        out = close_case(case)
        self.assertEqual(out["semaforo"], "VERDE")
        self.assertTrue(out["CLOSED"])
        self.assertFalse(out["OPEN"])
        self.assertTrue(out["authorized"])

    def test_receipt_file_written(self):
        with tempfile.TemporaryDirectory() as td:
            src = Path(td) / "case.json"
            src.write_text((CASES / "CASE_ALL_CONFORME.json").read_text(encoding="utf-8"), encoding="utf-8")
            out = close_case_file(src)
            self.assertTrue(out["CLOSED"])
            self.assertTrue(Path(out["receipt_path"]).is_file())

    def test_no_forbidden_apis(self):
        assert_no_alternate_close_api()


if __name__ == "__main__":
    unittest.main()
