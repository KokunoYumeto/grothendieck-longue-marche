from pathlib import Path
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
def audit(n, note):
    stamp=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    with (ROOT/"progress.log").open("a",encoding="utf-8") as f: f.write(f"scan {n:03} audited {stamp}\n")
    with (ROOT/"records"/"visual_audit.md").open("a",encoding="utf-8") as f: f.write(f"- Scan {n}: {note} ({stamp}).\n")
    print(f"Audited scan {n}")
