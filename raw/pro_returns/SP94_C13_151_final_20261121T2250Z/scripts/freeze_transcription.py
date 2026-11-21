"""Freeze or verify the completed transcription; never alters a reading."""
from pathlib import Path
import hashlib
import json
import sys
from compile_records import WORK, now

mode = sys.argv[1]
assert mode in ("freeze", "verify")
state = json.loads((WORK / "run_state.json").read_text())
assert len(state["order"]) == 24
assert set(state["completed"]) == set(state["order"])
assert set(state["audited"]) == set(state["order"])
files = [WORK / "pages" / (p + ".tex") for p in state["order"]]
files.append(WORK / "SP94_C13_151_transcription.tex")
hashes = {str(p.relative_to(WORK)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
manifest = WORK / "audit" / "frozen_transcription_sha256.json"
stamp = now()
if mode == "freeze":
    assert not manifest.exists(), "A frozen transcription already exists."
    manifest.write_text(json.dumps({"frozen_utc": stamp, "sha256": hashes}, indent=2) + "\n")
    with (WORK / "progress.log").open("a") as f:
        f.write("transcription frozen " + stamp + "\n")
        for name, digest in hashes.items():
            f.write("SHA-256 " + digest + "  " + name + "\n")
else:
    frozen = json.loads(manifest.read_text())
    assert hashes == frozen["sha256"], "Transcription changed after freeze."
    with (WORK / "progress.log").open("a") as f:
        f.write("transcription hashes unchanged " + stamp + ": all 24 page files and combined transcription verified\n")
print(json.dumps({"action": mode, "utc": stamp, "files": len(files), "unchanged": mode == "verify"}))
