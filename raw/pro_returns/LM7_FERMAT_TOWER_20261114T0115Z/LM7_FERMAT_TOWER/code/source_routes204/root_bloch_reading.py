"""Render the retrieved Bloch primary source and retain OCR for reading navigation."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parent
PDF = ROOT / 'source_route_raw/bloch1984.pdf'
DEST = ROOT / 'source_route_raw/bloch1984_pages'
DEST.mkdir(exist_ok=True)
assert hashlib.sha256(PDF.read_bytes()).hexdigest() == '9eb338771cda7e4e33f638e69dffda0afc092f9f2e0268e92f3d1b18359707a0'
render = subprocess.run(['pdftoppm', '-r', '125', '-png', str(PDF), str(DEST / 'page')], capture_output=True, text=True)
assert render.returncode == 0, render.stderr
pages = sorted(DEST.glob('page-*.png'))
assert len(pages) == 16

def ocr(path):
    target = path.with_suffix('')
    run = subprocess.run(['tesseract', str(path), str(target), '--psm', '3'], capture_output=True, text=True)
    path.with_suffix('.out').write_text(run.stdout + run.stderr)
    assert run.returncode == 0, path
    return {'image':str(path), 'image_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'ocr_exit_code':run.returncode, 'ocr_path':str(target.with_suffix('.txt'))}

with ThreadPoolExecutor(max_workers=3) as pool:
    records = list(pool.map(ocr, pages))
full = '\n\n'.join('--- PDF page ' + str(i + 1) + ' ---\n' + Path(rec['ocr_path']).read_text()
                    for i, rec in enumerate(records))
(ROOT / 'source_route_raw/bloch1984.ocr.txt').write_text(full)
result = {'status':'PASS','scope':'Source rendering and OCR navigation only; mathematical reading scope is recorded separately and formulas are checked on the page images.',
          'pdf_pages':len(pages),'render_stdout':render.stdout,'render_stderr':render.stderr,'pages':records}
(ROOT / 'root_bloch_reading.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
