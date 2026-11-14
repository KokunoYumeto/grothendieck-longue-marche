#!/usr/bin/env python3
"""Superseded audit entry point; canonical certificate is under code/.

Retained because the pre-integration candidate and root review cite this path.
Running this wrapper executes the canonical certificate and writes its output
under code/. The immutable checkpoint08 retains the historical original.
"""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).resolve().parent.parent / "code" /
                   "D_unrestricted_reciprocity_checks.py"), run_name="__main__")
