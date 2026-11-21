"""Apply the reviewed exact metadata proposals; diplomatic text stays unchanged."""
from pathlib import Path
import copy,hashlib,json,re
from datetime import datetime,timezone
w=Path('/workspace/scratch/b8c6ff258063/SP87_C13_149_work')
blocks=re.findall(r'```json\n(.*?)\n```',(w/'review/final_late_documentation_findings.md').read_text(),re.S)
patches=json.loads(blocks[0])+json.loads(blocks[1]);assert len(patches)==19
records={};originals={}
protected=list((w/'pages').glob('*.tex'))+list((w/'second').glob('*.tsv'))
digests={p:hashlib.sha256(p.read_bytes()).hexdigest() for p in protected}
for p in patches:
 assert p['file'] in {f'review/149_scan{s:03d}_reviewed.json' for s in (96,97,98,100)}
 path=w/p['file']
 if path not in records:
  originals[path]=json.loads(path.read_text());records[path]=copy.deepcopy(originals[path])
 r=records[path];sel=p['selector']
 if sel.get('top_level'):obj=r
 else:
  assert sel['array'] in {'hand_observations','notation_additions','inventory','abbreviations','check_events'}
  matches=[x for x in r[sel['array']] if all(x.get(k)==v for k,v in sel['match'].items())]
  assert len(matches)==1,p['id'];obj=matches[0]
 if p['op']=='replace_substring':
  assert obj[p['field']].count(p['old'])==p['expected_occurrences']==1,p['id']
  obj[p['field']]=obj[p['field']].replace(p['old'],p['new'],1)
 elif p['op']=='replace_fields':
  assert all(obj.get(k)==v for k,v in p['old'].items()),p['id']
  obj.update(p['new'])
 else:raise ValueError(p['op'])
for path,r in records.items():
 for k in ('changes','marks','second_boxes','diff_coverage','unresolved'):
  assert r.get(k)==originals[path].get(k),(path,k)
for path,r in records.items():path.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
assert all(hashlib.sha256(p.read_bytes()).hexdigest()==h for p,h in digests.items())
with (w/'progress.log').open('a') as f:f.write('late metadata reconciled '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+': applied19 guarded clarifications on096/097/098/100; one existing check-event description says initial prefix instead of initial E, with mathematical content/type/attribution unchanged; all page and second-stage TSV hashes unchanged.\n')
print('Applied19 guarded metadata clarifications; all page and second-stage TSV bytes unchanged.')
