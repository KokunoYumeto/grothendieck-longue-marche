"""Freeze or verify the diplomatic transcription; never silently rewrite it."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
NAME = "MPL_156-1+156-2"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
paths = [ROOT / "pages" / f"{NAME}_{c}_scan{n:03}.tex"
         for c, count in [("156-1", 27), ("156-2", 19)]
         for n in range(1, count + 1)]
assert all(p.is_file() for p in paths)
combined = ROOT / f"{NAME}_transcription.tex"
expected = "\n".join(p.read_text().rstrip() + "\n" for p in paths)
assert combined.read_text() == expected, "Combined fragment differs from ordered page files."
assert expected.startswith("\\cotefile{156-1}\n\\scanpage{1}")
assert len(re.findall(r"\\scanpage\{", expected)) == 46
assert re.findall(r"\\cotefile\{(.*?)\}", expected) == ["156-1", "156-2"]
hashes = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
          for p in paths + [combined]}
manifest = ROOT / "records" / "transcription_freeze.json"
if manifest.exists():
    frozen = json.loads(manifest.read_text())
    assert hashes == frozen["sha256"], "FROZEN TRANSCRIPTION CHANGED"
    with (ROOT / "progress.log").open("a") as log:
        log.write(f"frozen transcription hashes verified unchanged {NOW}; all 46 page files and combined fragment match freeze at {frozen['frozen_utc']}\n")
    print("All 47 SHA-256 hashes unchanged.")
else:
    logtext = (ROOT / "progress.log").read_text()
    audited = set(re.findall(r"(156-[12]) scan (\d{3}) audited ", logtext))
    required = {(c, f"{n:03}") for c, count in [("156-1", 27), ("156-2", 19)] for n in range(1, count + 1)}
    assert required <= audited, "Not all second audits logged."
    assert "context opened" not in logtext, "Context was already opened."
    manifest.write_text(json.dumps({"frozen_utc": NOW, "sha256": hashes}, indent=2) + "\n")
    (ROOT / "transcription.sha256").write_text("".join(f"{h}  {p}\n" for p, h in hashes.items()))
    with (ROOT / "progress.log").open("a") as log:
        log.write(f"transcription frozen {NOW}\n")
        for path, digest in hashes.items():
            log.write(f"SHA-256 {path} {digest}\n")
    print(f"Transcription frozen {NOW}; 47 hashes recorded.")
