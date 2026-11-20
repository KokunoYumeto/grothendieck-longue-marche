from pathlib import Path
import json,re,hashlib,csv
out=Path(__file__).resolve().parents[1]
errors=[];counts={k:0 for k in ['unsure','illegible','deleted','inserted','margin','diagram','figure']}
def escaped(s,pos):
    n=0;pos-=1
    while pos>=0 and s[pos]=='\\':n+=1;pos-=1
    return n%2==1
def literal_positions(s,token):
    return [m.start() for m in re.finditer(re.escape(token),s) if not escaped(s,m.start())]
for p in sorted((out/'pages').glob('*.tex')):
    t=p.read_text();s=re.sub(r'(?<!\\)%[^\n]*','',t)
    depth=0
    for m in re.finditer(r'[{}]',s):
        if escaped(s,m.start()):continue
        depth+=1 if m.group()=='{' else -1
        if depth<0:errors.append(f'{p.name}: premature closing brace');break
    if depth:errors.append(f'{p.name}: brace balance {depth}')
    if len(literal_positions(s,'$'))%2:errors.append(f'{p.name}: odd dollar count')
    if len(literal_positions(s,'\\['))!=len(literal_positions(s,'\\]')):errors.append(f'{p.name}: display delimiters')
    env=[]
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',s):
        kind,name=m.groups()
        if kind=='begin':env.append(name)
        elif not env or env.pop()!=name:errors.append(f'{p.name}: environment {name} mismatch')
    if env:errors.append(f'{p.name}: unclosed environments {env}')
    for k in counts:counts[k]+=len(re.findall(r'\\'+k+r'\{',s))
    for bad in ['\\uncertain{','\\struck{','\\marginal{','\\ill{','\\emph{']:
        if bad in s:errors.append(f'{p.name}: unexpected H macro {bad}')
    if '\\begin{tikzcd}' in s and 'ampersand replacement=\\&' not in s:errors.append(f'{p.name}: tikzcd missing ampersand replacement')
inventory=list(csv.DictReader((out/'SP52_CW_156-4+156-6_inventory.csv').open()))
if any(x['transcribed']!='yes' for x in inventory):errors.append('Inventory has unfinished elements')
allowed_kinds={'text','display','diagram','drawing','margin note','insertion','deletion'}
allowed_sheets={'text','reused_typed','typescript','letter','list','cancelled_draft','cover'}
for x in inventory:
    if x['kind'] not in allowed_kinds:errors.append(f"Inventory kind {x['kind']} at {x['scan']}")
    if x['sheet_kind'] not in allowed_sheets:errors.append(f"Inventory sheet kind {x['sheet_kind']} at {x['scan']}")
for entry in json.loads((out/'page_order.json').read_text()):
    key=f"{entry['cote']}_{int(entry['our_scan']):03d}"
    p=out/'decisions'/f'{key}.json'
    if not p.exists():continue
    d=json.loads(p.read_text())
    if not (out/'pages'/d['filename']).exists():errors.append(f"Missing page file for {d['key']}")
    for x in d['differences']:
        if x['confidence'] not in {'high','medium','low'}:errors.append(f"Bad confidence at {d['key']} / {x['location']}")
        if not x.get('crop'):errors.append(f"No adjudicator crop reference at {d['key']} / {x['location']}")

result={'pages':len(list((out/'pages').glob('*.tex'))),'marks':counts,'inventory_elements':len(inventory),'errors':errors}
(out/'validation.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result))
