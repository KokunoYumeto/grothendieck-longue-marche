from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
def audit(cote,scan,note="checked against scan; no further changes"):
    stamp=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    with (ROOT/"progress.log").open("a") as f:
        f.write(f"{cote} scan {scan:03} audited {stamp}\n")
    with (ROOT/"working"/"audit_notes.md").open("a") as f:
        f.write(f"- {cote} scan {scan:03}: {note}\n")
    (ROOT/"MPL_116+117_transcription.tex").write_bytes(b"".join(p.read_bytes() for p in sorted((ROOT/"pages").glob("*.tex"))))
