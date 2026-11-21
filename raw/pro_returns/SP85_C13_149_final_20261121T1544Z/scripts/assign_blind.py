"""Record an image-only assignment only after all first readings are committed."""
from pathlib import Path
import json,sys,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1]
page,agent=sys.argv[1:3]
records=list((ROOT/'records').glob('149_scan*.json'))
assert len(records)==23, 'All 23 first readings must be committed first'
path=ROOT/'records/assignments.json'
a=json.loads(path.read_text())
assert a['first'][page]!=agent, 'Blind reader has already read this page'
assert page not in a['second'], 'Blind assignment already exists'
assert not (ROOT/'second'/f'{page}_second.tsv').exists()
a['second'][page]=agent
path.write_text(json.dumps(a,indent=2)+'\n')
hashes={suffix:hashlib.sha256((ROOT/'second'/f'{page}_{suffix}.tsv').read_bytes()).hexdigest() for suffix in ['first','boxes']}
assignment={'page':page,'reader':agent,'time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'precomparison_hashes':hashes}
(ROOT/'second'/f'{page}_assignment.json').write_text(json.dumps(assignment,indent=2)+'\n')
print(page,agent,'assigned; first reading and box-list hashes recorded')
