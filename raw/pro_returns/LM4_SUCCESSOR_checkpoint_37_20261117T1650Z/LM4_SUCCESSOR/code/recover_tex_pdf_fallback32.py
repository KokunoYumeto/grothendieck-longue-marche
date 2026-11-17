"""Root-authorized private pdfLaTeX format fallback; no paper build."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import os
import subprocess

root = Path(__file__).resolve().parents[1]
runtime = root.parent / 'tex_runtime'
logs = root / 'records/tex_recovery32'
env = dict(os.environ, **json.loads((runtime / 'env.json').read_text()))
args = ['pdftex', '--ini', '--interaction=nonstopmode', '--jobname=pdflatex',
        '--progname=pdflatex', 'pdflatex.ini']
run = subprocess.run(args, cwd=runtime / 'formats', env=env, capture_output=True)
(logs / 'pdf_fallback_format.out').write_bytes(run.stdout)
(logs / 'pdf_fallback_format.err').write_bytes(run.stderr)
fmt = runtime / 'formats/pdflatex.fmt'
record = dict(recorded_at=datetime.now(timezone.utc).isoformat(), args=args,
              returncode=run.returncode, main_paper_build_performed=False,
              format=str(fmt), format_exists=fmt.is_file())
if fmt.is_file():
    record['format_sha256'] = hashlib.sha256(fmt.read_bytes()).hexdigest()
(logs / 'pdf_fallback_format.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
raise SystemExit(run.returncode)
