#!/usr/bin/env python3
"""Verify frozen files without modifying any transcription file."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, sys
root = Path(__file__).resolve().parents[1]
frozen=json.loads((root/"records/transcription_freeze.json").read_text())
bad=[f for f,h in frozen["hashes"].items() if hashlib.sha256((root/f).read_bytes()).hexdigest()!=h]
stamp=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
result={"checked_utc":stamp,"files_checked":len(frozen["hashes"]),"unchanged":not bad,"mismatches":bad}
print(json.dumps(result))
if "--log" in sys.argv:
    with (root/"progress.log").open("a") as f:
        f.write("frozen transcription hashes "+("unchanged" if not bad else "MISMATCH")+" "+stamp+" files="+str(len(frozen["hashes"]))+"\n")
sys.exit(bool(bad))
