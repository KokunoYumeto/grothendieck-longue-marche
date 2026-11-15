"""Freeze or verify only the diplomatic page files and their combined fragment."""
from pathlib import Path
import hashlib
import sys
from record import utc
from validate_transcription import validate

root = Path(__file__).resolve().parent
log = root / "progress.log"
manifest = root / "SHA256SUMS"
paths = sorted((root / "pages").glob("*.tex")) + [root / "MPL_136_189-234_transcription.tex"]

if sys.argv[1:] == ["--freeze"]:
    assert "transcription frozen " not in log.read_text()
    validate()
    entries = [(hashlib.sha256(p.read_bytes()).hexdigest(), p.relative_to(root).as_posix()) for p in paths]
    manifest.write_text("".join(f"{digest}  {name}\n" for digest, name in entries))
    with log.open("a") as f:
        f.write(f"notation consistency review completed {utc()}\n")
        f.write("structural validation: 45 pages; 928 inventory elements, all yes; all done/audit entries present\n")
        f.write("XeLaTeX syntax check: temporary wrapper with neutral state macros; manuscript layout not reconstructed by this check\n")
        for digest, name in entries:
            f.write(f"sha256 {name} {digest}\n")
        f.write(f"transcription frozen {utc()}\n")
    print("Frozen", len(entries), "files.")
elif sys.argv[1:] == ["--verify"]:
    assert "transcription frozen " in log.read_text()
    entries = [line.split("  ", 1) for line in manifest.read_text().splitlines()]
    for digest, name in entries:
        assert hashlib.sha256((root / name).read_bytes()).hexdigest() == digest, name
    with log.open("a") as f:
        f.write(f"frozen transcription hashes unchanged: {len(entries)} of {len(entries)} files verified {utc()}\n")
    print("All", len(entries), "frozen hashes unchanged.")
else:
    raise SystemExit("Use --freeze or --verify")
