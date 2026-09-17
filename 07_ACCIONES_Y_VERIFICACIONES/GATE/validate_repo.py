#!/usr/bin/env python3
"""Repo-wide validation for SENTINEL text integrity, Gate cases, receipts, and secrets."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from waipl_gate import validate_case, verify_receipt

REPO_ROOT = Path(__file__).resolve().parents[2]
GATE_DIR = Path(__file__).resolve().parent
TEXT_EXTENSIONS = {".md", ".txt", ".py", ".json", ".yml", ".yaml"}
MOJIBAKE_TOKENS = ("â€”", "â€“", "â†", "â€œ", "â€", "CANÃ", "CANÃ“", "��", "\x00")
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA|EC|OPENSSH|DSA|PGP) PRIVATE KEY-----"),
    re.compile(r"\b(?:ghp|github_pat|gho|ghu|ghs)_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bAIza[0-9A-Za-z\-_]{20,}\b"),
    re.compile(r"(?i)(?:api[_-]?key|token|secret|password)\s*[:=]\s*['\"][A-Za-z0-9_\-/.+=]{16,}['\"]"),
]


def iter_text_files() -> list[Path]:
    files: list[Path] = []
    for path in REPO_ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() in TEXT_EXTENSIONS:
            files.append(path)
    return files


def validate_utf8_and_mojibake(errors: list[str]) -> None:
    for path in iter_text_files():
        if path == Path(__file__).resolve():
            continue
        raw = path.read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"UTF8_ERROR {path}: {exc}")
            continue
        for token in MOJIBAKE_TOKENS:
            if token == "\x00":
                if b"\x00" in raw:
                    errors.append(f"MOJIBAKE {path}: contains NUL bytes")
                    break
                continue
            if token in text:
                errors.append(f"MOJIBAKE {path}: suspicious token {token!r}")
                break


def validate_cases_and_receipts(errors: list[str]) -> None:
    for case_path in sorted((GATE_DIR / "cases").glob("*.json")):
        if case_path.name.endswith(".gate_receipt.json"):
            continue
        try:
            case = json.loads(case_path.read_text(encoding="utf-8"))
            validate_case(case)
        except Exception as exc:
            errors.append(f"CASE_INVALID {case_path}: {exc}")
            continue

        receipt_path = case_path.with_name(case_path.name + ".gate_receipt.json")
        if receipt_path.exists():
            try:
                receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
                check = verify_receipt(case, receipt)
                if not check["valid"]:
                    errors.append(f"RECEIPT_INVALID {receipt_path}: {check['reasons']}")
            except Exception as exc:
                errors.append(f"RECEIPT_ERROR {receipt_path}: {exc}")


def validate_operational_indexes(errors: list[str]) -> None:
    backlog = REPO_ROOT / "08_INCIDENCIAS" / "INDICE_PENDIENTES_TECNICOS.md"
    if not backlog.exists():
        errors.append(f"MISSING_BACKLOG {backlog}")


def scan_for_secrets(errors: list[str]) -> None:
    for path in iter_text_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f"SECRET_PATTERN {path}: matched {pattern.pattern}")
                break


def main() -> int:
    errors: list[str] = []
    validate_utf8_and_mojibake(errors)
    validate_cases_and_receipts(errors)
    validate_operational_indexes(errors)
    scan_for_secrets(errors)
    if errors:
        print("SENTINEL repo validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("SENTINEL repo validation OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
