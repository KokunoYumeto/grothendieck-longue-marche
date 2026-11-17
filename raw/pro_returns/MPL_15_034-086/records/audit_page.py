"""Records the root reader's completed second visual comparison; never reads images."""
from pathlib import Path
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parent.parent
def audit(scan, note):
    now=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    with (ROOT/"progress.log").open("a") as f:
        f.write(f"scan {scan:03d} audited {now}\n")
    with (ROOT/"records/second_reading.md").open("a") as f:
        f.write(f"\n## Scan {scan:03d} — {now}\n{note}\n")
    print(f"scan {scan:03d} audited")
