#!/usr/bin/env python3
"""Independent read-only replay of the exact all-depth D93 support."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parents[1]
source = root / "notes/de_ordinary_kernel_smith_certificate.py"
namespace = {"__name__": "fgh_D93_smith_replay", "__file__": str(source)}
exec(compile(source.read_text(), str(source), "exec"), namespace)
result = namespace["run"]()
owner = json.loads(source.with_suffix(".json").read_text())
assert result == owner
destination = root / "notes/fgh_D93_smith_certificate_rerun.json"
destination.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
assert destination.read_bytes() == source.with_suffix(".json").read_bytes()
print(json.dumps({"status": "PASS", "whole_json_byte_equal": True,
                  "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                  "result_sha256": hashlib.sha256(destination.read_bytes()).hexdigest()}, indent=2))
