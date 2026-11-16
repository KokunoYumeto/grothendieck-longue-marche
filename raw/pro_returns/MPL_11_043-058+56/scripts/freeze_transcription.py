#!/usr/bin/env python3
"""Freeze the 50 visually audited page files and their ordered concatenation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re

root = Path(__file__).resolve().parents[1]
name = "MPL_11_043-058+56"
expected = [(11,n) for n in range(43,59) if n != 50] + [(56,n) for n in range(2,40) if n not in (10,19,34)]
log = root / "progress.log"
text = log.read_text()
assert not re.search(r"^transcription frozen ", text, re.M), "Already frozen"
assert not re.search(r"^context opened ", text, re.M), "Context already opened"
for c,n in expected:
    assert re.search(rf"^{c} scan {n:03} audited ",text,re.M), f"Missing audit {c}/{n}"
pages = [f"pages/{name}_{c}_scan{n:03}.tex" for c,n in expected]
combined = f"{name}_transcription.tex"
assert (root/combined).read_bytes() == b"".join((root/f).read_bytes()+b"\n" for f in pages)
hashes = {f: hashlib.sha256((root/f).read_bytes()).hexdigest() for f in pages + [combined]}
stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
lines = "".join(f"{digest}  {f}\n" for f,digest in hashes.items())
(root/"records/transcription_sha256.txt").write_text(lines)
(root/"records/transcription_freeze.json").write_text(json.dumps({"frozen_utc":stamp,"hashes":hashes},indent=2)+"\n")
with log.open("a") as f:
    f.write(lines)
    f.write("transcription frozen "+stamp+"\n")
print(json.dumps({"frozen_utc":stamp,"file_count":len(hashes),"combined_sha256":hashes[combined]}))
