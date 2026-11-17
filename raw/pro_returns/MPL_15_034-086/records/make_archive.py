"""Package deliverables and work records; exclude sources and rendered source pages."""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile

PACKAGE = Path(__file__).resolve().parent.parent
WORKSPACE = PACKAGE.parent.parent
SOURCE_SUFFIXES = {".jpg", ".jpeg", ".png", ".pdf", ".zip", ".pyc"}

def verify_frozen():
    expected = json.loads((PACKAGE / "records/frozen_sha256.json").read_text())
    for relative, value in expected.items():
        actual = hashlib.sha256((PACKAGE / relative).read_bytes()).hexdigest()
        if actual != value:
            raise SystemExit(f"Frozen hash mismatch: {relative}")
    return len(expected)

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--checkpoint", type=int)
    group.add_argument("--final", action="store_true")
    parser.add_argument("--stamp", required=True)
    args = parser.parse_args()
    checked = verify_frozen()
    name = (
        f"MPL_15_034-086_checkpoint_{args.checkpoint:02d}.zip"
        if args.checkpoint is not None else "MPL_15_034-086.zip"
    )
    destination = WORKSPACE / name
    if destination.exists():
        raise SystemExit(f"Refusing to overwrite: {destination}")
    paths = sorted(
        p for p in PACKAGE.rglob("*")
        if p.is_file() and "__pycache__" not in p.parts
        and p.suffix.lower() not in SOURCE_SUFFIXES
    )
    action = f"checkpoint {args.checkpoint:02d}" if args.checkpoint is not None else "final archive"
    with (PACKAGE / "progress.log").open("a", encoding="utf-8") as log:
        log.write(f"{action} prepared {args.stamp}; {checked} frozen hashes unchanged; {len(paths)} files included; supplied sources excluded\n")
    with zipfile.ZipFile(destination, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in paths:
            archive.write(path, path.relative_to(PACKAGE))
    with zipfile.ZipFile(destination) as archive:
        bad = archive.testzip()
        if bad:
            raise SystemExit(f"ZIP integrity failure: {bad}")
    print(json.dumps({
        "path": str(destination),
        "files": len(paths),
        "bytes": destination.stat().st_size,
        "sha256": hashlib.sha256(destination.read_bytes()).hexdigest(),
    }, indent=2))

if __name__ == "__main__":
    main()
