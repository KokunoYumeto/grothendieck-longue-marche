#!/usr/bin/env python3
"""Retrieve the author-hosted primary preprint, retaining the exact source.

The URL is the RIMS-1224 link on the institute's 1999 preprint index.
No theorem is inferred from retrieval success or failure.
"""
from pathlib import Path
import gzip
import hashlib
import json
import shutil
import subprocess
import urllib.request

root = Path(__file__).resolve().parent.parent
dest = root.parent / 'source_cache' / 'Ihara_beta_gamma'
dest.mkdir(parents=True, exist_ok=True)
url = 'https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1224.ps.gz'
record = {'url': url}
try:
    with urllib.request.urlopen(url, timeout=30) as response:
        data = response.read()
    compressed = dest / 'Ihara_RIMS1224.ps.gz'
    compressed.write_bytes(data)
    postscript = dest / 'Ihara_RIMS1224.ps'
    postscript.write_bytes(gzip.decompress(data))
    record.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                  postscript_bytes=postscript.stat().st_size)
    converter = shutil.which('ps2pdf')
    record['converter'] = converter
    if converter:
        pdf = dest / 'Ihara_RIMS1224.pdf'
        result = subprocess.run([converter, str(postscript), str(pdf)],
                                text=True, capture_output=True)
        record['conversion_returncode'] = result.returncode
        record['conversion_stdout'] = result.stdout
        record['conversion_stderr'] = result.stderr
        extractor = shutil.which('pdftotext')
        if result.returncode == 0 and extractor:
            textfile = dest / 'Ihara_RIMS1224.txt'
            result = subprocess.run([extractor, '-layout', str(pdf), str(textfile)],
                                    text=True, capture_output=True)
            record['text_returncode'] = result.returncode
            record['text_stderr'] = result.stderr
except Exception as error:
    record['error_type'] = type(error).__name__
    record['error'] = str(error)
(root / 'code' / 'fetch_ihara_beta_gamma.json').write_text(
    json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
