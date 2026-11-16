#!/usr/bin/env python3
"""Use actual quotient word collection, rather than a truncated raw normal form.

The canonical map of centralizations is valid, but the two deterministic
collectors can select different consistency-equivalent formal tail vectors.
All search targets must be the directly replayable original quotient words.
"""
from pathlib import Path
from collections import defaultdict
import hashlib,json
b=Path(__file__).resolve().parent
old=json.loads((b/'pbc_suffix3_initial_rows.json').read_text())
rows={r['label']:r['tail'] for r in map(json.loads,(b/'pbc_suffix3_initial_validate.jsonl').read_text().splitlines())}
def add(*vectors):
 d=defaultdict(int)
 for v in vectors:
  for i,a in zip(v[::2],v[1::2]):d[i]+=a
 return [x for i,a in sorted(d.items()) if a for x in (i,a)]
target=add(rows['target_s'],rows['target_r'],rows['target_product'])
extras=[rows['extra_'+str(i+1)] for i in range(len(old['extras']))]
assert extras==old['extras']
new={'source_sha256':old['source_sha256'],'target':target,'extras':extras,
 'collection':'Actual original quotient words, independently collected by pbc_positive_collector; no processed relation lattice.'}
(b/'pbc_suffix3_actual_initial_rows.json').write_text(json.dumps(new,separators=(',',':'))+'\n')
# The source/input layout is one line per word and one per scalar block.
lines=(b/'pbc_suffix3_primary.dat').read_text().splitlines();n=int(lines[0]);target_line=2+n+n*(n-1)//2+4
assert list(map(int,lines[target_line].split()))==[len(old['target'])]+old['target']
lines[target_line]=' '.join(map(str,[len(target)]+target))
out=b/'pbc_suffix3_primary_v2.dat';out.write_text('\n'.join(lines)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
first=dict(zip(old['target'][::2],old['target'][1::2]));second=dict(zip(target[::2],target[1::2]))
report={'status':'PASS: actual quotient target and all original frame words recollected',
 'actual_target_support':len(target)//2,'all_extra_rows_equal':True,
 'raw_projected_target_difference_coordinates':sum(first.get(i,0)!=second.get(i,0) for i in set(first)|set(second)),
 'correction':'Raw collection is not functorial before consistency relations. Use the actual quotient target; the Hopf map identifies its class with the original target.',
 'superseded_attempt':'pbc_suffix3_v1, paused before any claim; all records retained.',
 'hashes':{p.name:sha(p) for p in [b/'pbc_suffix3_original_source.json',b/'pbc_positive_collector.cpp',b/'pbc_positive_collector',b/'pbc_suffix3_initial_validate.jsonl',out]}}
(b/'pbc_suffix3_actual_initial_validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
