#!/usr/bin/env python3
"""Reconstruct an original QA PNG from its archived PDF; require exact bytes."""
from pathlib import Path
import argparse,hashlib,json
import fitz
ap=argparse.ArgumentParser();ap.add_argument('manifest',type=Path);ap.add_argument('original_path');ap.add_argument('output',type=Path);a=ap.parse_args()
base=a.manifest.resolve().parents[1]
manifest=json.loads(a.manifest.read_text());row=manifest['images'][a.original_path]
if a.output.exists():raise SystemExit('Refusing to overwrite '+str(a.output))
pdf=base/row['pdf_path']
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==row['pdf_sha256']
with fitz.open(pdf) as doc:
 data=doc[row['page']-1].get_pixmap(matrix=fitz.Matrix(row['scale'],row['scale'])).tobytes('png')
assert len(data)==row['bytes'] and hashlib.sha256(data).hexdigest()==row['sha256'],('Renderer byte mismatch',fitz.VersionBind,manifest['pymupdf_version'])
a.output.parent.mkdir(parents=True,exist_ok=True)
with a.output.open('xb') as f:f.write(data)
print('RESTORED exact QA PNG:',a.original_path,row['sha256'])
