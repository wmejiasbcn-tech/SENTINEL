#!/usr/bin/env python3
"""Tests de aceptación WAIPL Verification Gate v1.0."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from gate_evaluate import evaluate

HERE = Path(__file__).resolve().parent
CASES = HERE / "cases"


class TestGateV1(unittest.TestCase):
    def test_aud_lab_carla_01_cannot_close(self):
        case = json.loads((CASES / "AUD-LAB-CARLA-01.json").read_text(encoding="utf-8"))
        out = evaluate(case)
        self.assertEqual(out["semaforo"], "AMARILLO")
        self.assertFalse(out["CLOSED"])
        self.assertTrue(out["OPEN"])
        pending_ids = {p["id"] for p in out["pending_mandatory"]}
        self.assertIn("codex_ley_como_fichero", pending_ids)
        self.assertIn("corpus_audio_este_chat", pending_ids)

    def test_all_conforme_closes_verde(self):
        case = json.loads((CASES / "CASE_ALL_CONFORME.json").read_text(encoding="utf-8"))
        out = evaluate(case)
        self.assertEqual(out["semaforo"], "VERDE")
        self.assertTrue(out["CLOSED"])
        self.assertFalse(out["OPEN"])
        self.assertEqual(out["pending_mandatory"], [])

    def test_missing_piece_blocks_close(self):
        case = {
            "id": "missing_evidence",
            "resultado": True,
            "evidencia": False,
            "verificacion": True,
            "dictamen": True,
            "requisitos_obligatorios": [{"id": "x", "estado": "CONFORME"}],
        }
        out = evaluate(case)
        self.assertFalse(out["CLOSED"])
        self.assertEqual(out["semaforo"], "AMARILLO")

    def test_no_verificado_blocks_close(self):
        case = {
            "id": "nv",
            "resultado": True,
            "evidencia": True,
            "verificacion": True,
            "dictamen": True,
            "requisitos_obligatorios": [{"id": "y", "estado": "NO VERIFICADO"}],
        }
        out = evaluate(case)
        self.assertFalse(out["CLOSED"])
        self.assertEqual(out["semaforo"], "AMARILLO")


if __name__ == "__main__":
    unittest.main()
