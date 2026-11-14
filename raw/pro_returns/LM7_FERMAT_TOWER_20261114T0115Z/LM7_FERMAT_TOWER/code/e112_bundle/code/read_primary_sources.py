"""Fetch the public author source and extract it for exact proof verification."""
from pathlib import Path
from urllib.request import urlopen
import hashlib
import json
import subprocess

root=Path(__file__).resolve().parents[1]
sources=root/'sources'
sources.mkdir(exist_ok=True)
url='https://www.jmilne.org/math/Books/ADTnot.pdf'
with urlopen(url,timeout=30) as response:
    data=response.read(10_000_001)
    status=response.status
assert len(data)<=10_000_000 and data.startswith(b'%PDF-')
pdf=sources/'Milne_ADT_original.pdf'
pdf.write_bytes(data)
txt=sources/'Milne_ADT_original.txt'
run=subprocess.run(['pdftotext','-layout',str(pdf),str(txt)],
                   stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
assert run.returncode==0,run.stdout.decode(errors='replace')
result={'status':'PASS','public_url':url,'http_status':status,
        'pdf_sha256':hashlib.sha256(data).hexdigest(),
        'pdf_bytes':len(data),'extraction_sha256':hashlib.sha256(txt.read_bytes()).hexdigest(),
        'scope':'Retrieval/extraction only. Actual proof reads are recorded separately. '
        'The third-party PDF and full extraction are excluded from the deliverable package.'}
(root/'ledger').mkdir(exist_ok=True)
(root/'ledger'/'e112_source_retrieval.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
