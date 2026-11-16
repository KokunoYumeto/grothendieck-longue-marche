"""Retrieve the official primary manuscript; do not package the raw scan."""
from pathlib import Path
import hashlib
import json
import urllib.request

root = Path(__file__).resolve().parents[2]
url = 'https://grothendieck.umontpellier.fr/140-4.pdf'
path = root/'work/primary/Grothendieck_cote1404.pdf'
part = path.with_suffix('.part')
if not path.exists():
    request = urllib.request.Request(url, headers={'User-Agent': 'Research audit; primary manuscript retrieval'})
    with urllib.request.urlopen(request, timeout=45) as response, part.open('wb') as out:
        total = int(response.headers['Content-Length'])
        done = 0
        while chunk := response.read(1024*1024):
            out.write(chunk)
            done += len(chunk)
            if done % (8*1024*1024) == 0:
                print(f'{done}/{total} bytes', flush=True)
    assert done == total, (done,total)
    assert part.open('rb').read(5) == b'%PDF-'
    part.rename(path)
record = {'url':url,'path':str(path.relative_to(root)),
          'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
          'retrieval':'Official university primary manuscript; raw scan excluded from research archives.'}
(root/'deliverable/records/cote1404_retrieval.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2),flush=True)
