#!/usr/bin/env python3
"""Convert the retained primary PostScript using a writable temporary area."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import tempfile

root = Path(__file__).resolve().parent.parent
dest = root.parent / 'source_cache' / 'Ihara_beta_gamma'
source = dest / 'Ihara_RIMS1224.ps'
pdf = dest / 'Ihara_RIMS1224.pdf'
plain = dest / 'Ihara_RIMS1224.txt'
with tempfile.TemporaryDirectory(prefix='ihara_gs_', dir=dest) as temporary:
    environment = dict(os.environ)
    environment['TMPDIR'] = temporary
    converted = subprocess.run(['ps2pdf', str(source), str(pdf)],
                               capture_output=True, text=True, env=environment)
record = {'conversion_returncode': converted.returncode,
          'conversion_stdout': converted.stdout,
          'conversion_stderr': converted.stderr}
if converted.returncode == 0:
    extracted = subprocess.run(['pdftotext', '-layout', str(pdf), str(plain)],
                               capture_output=True, text=True)
    record.update(text_returncode=extracted.returncode,
                  text_stderr=extracted.stderr,
                  pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest())
(root / 'code' / 'convert_ihara_beta_gamma.json').write_text(
    json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
