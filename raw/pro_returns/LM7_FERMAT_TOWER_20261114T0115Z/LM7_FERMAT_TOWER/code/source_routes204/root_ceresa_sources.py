"""Retrieve the exact public primary PDFs used for the compact-handle audit."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import Request, urlopen
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parent
DEST = ROOT / 'source_route_raw'
DEST.mkdir(exist_ok=True)
ROUTES = [
 ('bloch1984', 'https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0350/LOG_0009.pdf'),
 ('hain_matsumoto2005', 'https://arxiv.org/pdf/math/0306037'),
 ('bisogno_li_litt_srinivasan2023', 'https://epiga.episciences.org/11131/pdf'),
 ('ellenberg_logan_srinivasan2024', 'https://padmask.github.io/CertifyingCeresa.pdf'),
]

def fetch(item):
    name, url = item
    record = {'name': name, 'url': url}
    try:
        with urlopen(Request(url, headers={'User-Agent': 'LM7-source-verification/1.0'}), timeout=30) as response:
            data = response.read(40_000_001)
            record.update({'http_status': response.status, 'final_url': response.url,
                           'content_type': response.headers.get('Content-Type')})
        assert len(data) <= 40_000_000, 'response exceeds bound'
        assert data.startswith(b'%PDF-'), 'response is not a PDF; no access challenge followed'
        path = DEST / (name + '.pdf')
        path.write_bytes(data)
        record.update({'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
                       'pdf_path': str(path)})
        text_path = path.with_suffix('.txt')
        run = subprocess.run(['pdftotext', '-layout', str(path), str(text_path)], capture_output=True, text=True)
        record.update({'text_extraction_exit_code': run.returncode,
                       'text_extraction_stdout': run.stdout, 'text_extraction_stderr': run.stderr})
        assert run.returncode == 0
        record.update({'text_path': str(text_path), 'text_bytes': text_path.stat().st_size,
                       'status': 'public PDF retrieved; reading scope recorded separately'})
    except Exception as exc:
        record.update({'status': 'retrieval failure', 'reason': type(exc).__name__ + ': ' + str(exc)})
    return record

with ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(fetch, ROUTES))
result = {'scope': 'Exact public primary-source URLs previously found through bibliographic or author sources. No credentials or access challenges were used. Third-party PDFs are research inputs excluded from the deliverable ZIP.',
          'routes': results}
(ROOT / 'root_ceresa_sources.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
