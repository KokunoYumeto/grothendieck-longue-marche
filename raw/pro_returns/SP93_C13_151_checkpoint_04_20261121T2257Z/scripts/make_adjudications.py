"""Turn explicitly supplied root decisions into audit records; never reads ink.
Input is a JSON mapping from every differing box ID to evidence, changed, and
optionally final. Retained readings use the immutable first TSV verbatim.
"""
from pathlib import Path
import argparse,csv,json
ROOT=Path('/workspace/scratch/d12e26a9cd50/SP93_C13_151_work')
p=argparse.ArgumentParser();p.add_argument('scan');p.add_argument('decisions');a=p.parse_args()
name=f'151_scan{int(a.scan):03d}'
with (ROOT/'second'/f'{name}_comparison.tsv').open(newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
manual=json.loads(Path(a.decisions).read_text());different=[r for r in rows if r['same_tokens']=='no']
if set(manual)!={r['box'] for r in different}:raise ValueError('Every and only different box must be explicitly decided.')
result=[]
for r in different:
 d=manual[r['box']]
 if not isinstance(d.get('changed'),bool) or not d.get('evidence'):raise ValueError('Missing explicit decision/evidence.')
 if d['changed'] and not d.get('final'):raise ValueError('Changed reading must be supplied explicitly.')
 result.append(dict(box=r['box'],final=d.get('final',r['first']),evidence=d['evidence'],changed=d['changed'],crop=f'crops/{name}_second_{r["box"]}.png'))
(ROOT/'reviews'/f'{name}_audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'scan':a.scan,'decisions':len(result),'changed':sum(d['changed'] for d in result)}))
