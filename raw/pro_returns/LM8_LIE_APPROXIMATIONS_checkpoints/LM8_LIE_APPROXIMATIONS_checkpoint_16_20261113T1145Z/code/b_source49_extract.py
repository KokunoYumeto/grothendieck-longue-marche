#!/usr/bin/env python3
"""Extract exact original pages needed for the full signed source audit."""
from pathlib import Path
import hashlib
import json
import subprocess
from pypdf import PdfReader, PdfWriter
from pypdf._page import PageObject
from b_source47_extract import RemoteFile, page_at, ROOT, URL, SIZE

out=ROOT/'source_checks'/'140-3-signed'
out.mkdir(parents=True,exist_ok=True)
stream=RemoteFile()
reader=PdfReader(stream,strict=True)
tree=reader.trailer['/Root']['/Pages']
manifest=[]
for number in [530,534,549,550,559,560]:
    raw=page_at(tree,number-1)
    page=PageObject(reader,raw.indirect_reference)
    page.update(raw)
    writer=PdfWriter()
    writer.add_page(page)
    dest=out/f'pdfpage{number:03d}.pdf'
    with dest.open('wb') as handle:
        writer.write(handle)
    subprocess.run(['pdftoppm','-singlefile','-scale-to','1800','-png',str(dest),str(dest.with_suffix(''))],check=True)
    manifest.append({'original_pdf_page_one_based':number,'original_pdf_page_zero_based':number-1,
                     'local_file':str(dest.relative_to(ROOT)),
                     'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()})
    print('saved original page',number,flush=True)
result={'source_url':URL,'source_pdf_bytes':SIZE,'pages':manifest,
        'new_range_requests':stream.requests,'new_bytes_fetched':stream.fetched,
        'scope':'Exact original images. Manuscript folios and readings require direct visual inspection.'}
(out/'extraction_manifest.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2),flush=True)
