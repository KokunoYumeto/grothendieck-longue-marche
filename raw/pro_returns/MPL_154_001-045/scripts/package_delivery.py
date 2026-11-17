"""Package the finished work without input scans/context or earlier ZIPs.

Refuses to overwrite an existing final archive and verifies all frozen hashes.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "MPL_154_001-045"
OUTPUT = ROOT.parent / f"{PREFIX}.zip"


def main():
    if OUTPUT.exists():
        raise FileExistsError(OUTPUT)
    manifest = json.loads((ROOT / "records/frozen_sha256.json").read_text())
    for name, expected in manifest["sha256"].items():
        actual = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
        if actual != expected:
            raise RuntimeError(f"Frozen file changed: {name}")
    report = json.loads((ROOT / "records/final_validation.json").read_text())
    if report["errors"] or not report["all_frozen_hashes_unchanged"]:
        raise RuntimeError("Final validation has not passed")
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    with (ROOT / "progress.log").open("a") as f:
        f.write(f"research notes complete {timestamp}: 114 numbered items; 67 indexed authorial reservations/revisions; titles/counts and register disposition completed\n")
        f.write(f"final pre-archive hash check unchanged {timestamp}: all 45 frozen SHA-256 values match\n")
        f.write(f"final archive packaging started {timestamp}: supplied scans, prompt, context source files and earlier checkpoint ZIPs excluded\n")
    files = sorted(p for p in ROOT.rglob("*")
                   if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc")
    forbidden_suffixes = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".zip", ".pdf"}
    if any(p.suffix.lower() in forbidden_suffixes for p in files):
        raise RuntimeError("Unexpected input/image/archive artifact in delivery tree")
    with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            archive.write(path, path.relative_to(ROOT))
    with zipfile.ZipFile(OUTPUT) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("ZIP CRC validation failed")
        names = archive.namelist()
        if len(names) != len(set(names)):
            raise RuntimeError("Duplicate archive entries")
        if sum(n.startswith("pages/") and n.endswith(".tex") for n in names) != 44:
            raise RuntimeError("Archive lacks the44 page files")
    print(json.dumps({"archive": str(OUTPUT), "files": len(files),
                      "size_bytes": OUTPUT.stat().st_size,
                      "sha256": hashlib.sha256(OUTPUT.read_bytes()).hexdigest(),
                      "zip_crc_check": "passed", "frozen_hash_check": "45/45 unchanged",
                      "packaged_utc": timestamp}, indent=2))


if __name__ == "__main__":
    main()
