#!/usr/bin/env python3
"""Run the repository publication checker from the local update skill."""

from __future__ import annotations

import runpy
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
runpy.run_path(str(ROOT / "scripts" / "check_publications.py"), run_name="__main__")
