#!/usr/bin/env python3
from __future__ import annotations

import sys

from waipl_gate.gate_close import *  # noqa: F401,F403
from waipl_gate.gate_close import main


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
