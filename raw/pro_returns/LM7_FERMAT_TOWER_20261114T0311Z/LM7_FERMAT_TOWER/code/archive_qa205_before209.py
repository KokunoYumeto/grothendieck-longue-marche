"""Preserve the actual checkpoint205 render and review before rendering209."""
from pathlib import Path
import hashlib
import json
import shutil

base = Path(__file__).resolve().parents[1]
dest = base / 'qa' / 'history' / 'checkpoint205_before209'
dest.mkdir(parents=True, exist_ok=False)
rows = []
paths = [base/'qa'/'pdf_qa.json', base/'qa'/'visual_review.md',
         base/'code'/'pdf_qa.out']
paths += sorted((base/'qa').glob('contact_*.jpg'))
for path in paths:
    target = dest / path.name
    shutil.copy2(path, target)
    rows.append({'path':str(path.relative_to(base)), 'retained':str(target.relative_to(base)),
                 'bytes':target.stat().st_size,
                 'sha256':hashlib.sha256(target.read_bytes()).hexdigest()})
result = {'status':'PASS', 'files':rows}
(dest/'manifest.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
