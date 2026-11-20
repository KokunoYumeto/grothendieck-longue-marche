"""Freeze or verify exactly the 24 page fragments and their concatenation."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib

W = Path(__file__).resolve().parents[1]
SCANS = (26,27,28,29,30,31,33,34,35,36,37,38,39,40,41,42,
         44,45,46,47,48,49,50,51)
NAMES = tuple(f"pages/142_scan{n:03}.tex" for n in SCANS) + (
    "SP70_C13_142_transcription.tex",)
MANIFEST = W / "TRANSCRIPTION_SHA256SUMS"

def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

def digest(name):
    return hashlib.sha256((W / name).read_bytes()).hexdigest()

p = argparse.ArgumentParser()
p.add_argument("mode", choices=("freeze", "check"))
args = p.parse_args()
assert len(NAMES) == 25
assert sorted(p.name for p in (W / "pages").glob("*.tex")) == [
    f"142_scan{n:03}.tex" for n in SCANS]

if args.mode == "freeze":
    assert not MANIFEST.exists(), "The transcription is already frozen"
    progress = (W / "progress.log").read_text()
    assert "transcription frozen " not in progress
    for n in SCANS:
        assert f"scan {n:03} audited " in progress, f"Missing audit: {n}"
    hashes = [(digest(name), name) for name in NAMES]
    with MANIFEST.open("x") as f:
        for sha, name in hashes:
            f.write(f"{sha}  {name}\n")
    with (W / "progress.log").open("a") as f:
        f.write("transcription frozen " + now() + "\n")
        for sha, name in hashes:
            f.write(f"sha256 {sha} {name}\n")
    print("FROZEN: 24 pages and combined fragment; 25 SHA-256 values recorded")
else:
    rows = [line.split("  ", 1) for line in MANIFEST.read_text().splitlines()]
    assert tuple(name for sha, name in rows) == NAMES
    changed = [name for sha, name in rows if digest(name) != sha]
    if changed:
        raise SystemExit("FROZEN TRANSCRIPTION CHANGED: " + ", ".join(changed))
    with (W / "progress.log").open("a") as f:
        f.write("transcription hashes unchanged " + now()
                + "; all 25 SHA-256 values verified\n")
    print("UNCHANGED: all 25 frozen SHA-256 values match")
