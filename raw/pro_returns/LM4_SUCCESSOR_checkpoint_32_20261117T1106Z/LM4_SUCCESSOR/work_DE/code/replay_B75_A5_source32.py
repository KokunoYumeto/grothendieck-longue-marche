"""One root-authorized replay to obtain the previously omitted exit status."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import sys

root = Path(__file__).resolve().parents[2]
source = root / 'work_DE/code/check_B75_A5_source32.py'
base = root / 'work_DE/code/check_B75_A5_source32_exit_verified'
for suffix in ('.out', '.err', '.json'):
    assert not base.with_suffix(suffix).exists(), 'Never overwrite replay evidence'
run = subprocess.run([sys.executable, str(source)], cwd=root, capture_output=True)
base.with_suffix('.out').write_bytes(run.stdout)
base.with_suffix('.err').write_bytes(run.stderr)
record = dict(recorded_at=datetime.now(timezone.utc).isoformat(),
              authorization='Root explicitly authorized one replay to resolve the missing numeric exit-code field.',
              source=str(source.relative_to(root)),
              source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
              subprocess_returncode=run.returncode,
              stdout_sha256=hashlib.sha256(run.stdout).hexdigest(),
              stderr_sha256=hashlib.sha256(run.stderr).hexdigest(),
              stderr_bytes=len(run.stderr), original_attempt_preserved=True)
base.with_suffix('.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
raise SystemExit(run.returncode)
