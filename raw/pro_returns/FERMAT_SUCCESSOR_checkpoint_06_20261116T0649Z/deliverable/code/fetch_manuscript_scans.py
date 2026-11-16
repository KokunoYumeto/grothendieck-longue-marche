"""Fetch the public Montpellier primary scan needed for task D.1."""
from pathlib import Path
import hashlib,json,urllib.request
root=Path(__file__).resolve().parents[2]
url='https://grothendieck.umontpellier.fr/145.pdf'
p=root/'work/primary/Grothendieck_cote145.pdf'
if not p.exists():
    req=urllib.request.Request(url,headers={'User-Agent':'Research audit; primary manuscript retrieval'})
    data=urllib.request.urlopen(req,timeout=45).read()
    assert data.startswith(b'%PDF-'),data[:100]
    p.write_bytes(data)
else:data=p.read_bytes()
r={'url':url,'path':str(p.relative_to(root)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'retrieval':'Direct official university PDF; raw scan excluded from research checkpoint packages.'}
(root/'deliverable/records/cote145_retrieval.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
