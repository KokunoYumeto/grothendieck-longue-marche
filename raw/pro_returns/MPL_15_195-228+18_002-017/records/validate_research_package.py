#!/usr/bin/env python3
"""Read-only final integrity and research-metadata audit, writing one report."""
from pathlib import Path
from collections import Counter
import json,re,hashlib,datetime,csv

R=Path(__file__).resolve().parents[1]
P='MPL_15_195-228+18_002-017'
errors=[]; warnings=[]
notes=json.loads((R/'records/research_notes_all.json').read_text())
searches=json.loads((R/'records/research_context_searches.json').read_text())['searches']
ids=[n['id'] for n in notes]
if len(ids)!=len(set(ids)):errors.append('Duplicate observation IDs')
if set(ids)!={n['id'] for n in searches}:errors.append('Observation/context-search IDs differ')
fields={'id','title','kind','location','quote','terms','context','ledger','body'}
locations=[];sentence_review=[]
for n in notes:
    if set(n)!=fields:errors.append(f"{n['id']}: unexpected schema")
    if any(not n[k] for k in fields):errors.append(f"{n['id']}: empty field")
    if 'own idea' in n['kind'] and 'confidence' not in n['body'].lower():
        errors.append(f"{n['id']}: own idea lacks confidence statement")
    for cote,scan,spec in re.findall(r'(?<!context)(15|18)/(\d{3}):L([^;]+)',n['location']):
        path=R/'pages'/f'{P}_{cote}_scan{scan}.tex'
        if not path.exists():errors.append(f"{n['id']}: missing witness {path.name}");continue
        count=len(path.read_text().splitlines())
        for a,b in re.findall(r'(\d+)(?:[–-](\d+))?',spec):
            a=int(a);b=int(b or a)
            if a<1 or b<a or b>count:errors.append(f"{n['id']}: invalid lines {a}–{b} of {path.name}")
            locations.append(dict(id=n['id'],cote=int(cote),scan=int(scan),first_line=a,last_line=b))
    # Advisory only: abbreviations and formulas can defeat prose segmentation.
    s=re.sub(r'\\\(.*?\\\)','MATH',n['body'])
    s=re.sub(r'\([^)]*\d{4}[^)]*\)','CITATION',s)
    chunks=[x for x in re.split(r'(?<=[.!?])\s+(?=[A-Z])',s.strip()) if x]
    if len(chunks)>4:sentence_review.append(dict(id=n['id'],heuristic_sentences=len(chunks)))
text=(R/f'{P}_notes.md').read_text()
for h in ['## Standing question I:','## Standing question II:','### Linear statement, non-linear statement','## Primary bibliography and checked versions']:
    if h not in text:errors.append('Missing required notes section '+h)
if re.search(r'|turn\d+(?:view|search)|Post-freeze research draft in progress|TODO|TBD',text):
    errors.append('Unresolved draft/tool marker in canonical notes')
if len(re.findall(r'^### [APMBRX]\d+ — ',text,re.M))!=len(notes):
    errors.append('Rendered observation count differs')
frozen=json.loads((R/'records/frozen_manifest.json').read_text())
changed=[]
for f,digest in frozen['sha256'].items():
    if hashlib.sha256((R/f).read_bytes()).hexdigest()!=digest:changed.append(f)
if changed:errors.append('Frozen files changed: '+', '.join(changed))
inventory=list(csv.DictReader((R/f'{P}_inventory.csv').open()))
if any(n['transcribed']!='yes' for n in inventory):errors.append('Inventory contains unfinished row')
sheet_by_page={}
for row in inventory:
    key=(int(row['cote']),int(row['scan']))
    old=sheet_by_page.setdefault(key,row['sheet_kind'])
    if old!=row['sheet_kind']:errors.append('Inconsistent sheet kind '+str(key))
bibliography=(R/'records/notes_bibliography.md').read_text()
report=dict(run_utc=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
    pass_integrity=not errors,observations=len(notes),observations_by_prefix=dict(Counter(x[0] for x in ids)),
    context_searches=len(searches),individual_witness_ranges_checked=len(locations),
    inventory_rows=len(inventory),inventory_pages=len(sheet_by_page),sheet_kinds=dict(Counter(sheet_by_page.values())),
    bibliography_entries=len(re.findall(r'^\*\*[^\n]+\(\d{4}[ab]?\)',bibliography,re.M)),
    uncertainty_entries=len((R/'records/final_doubt_rows.jsonl').read_text().splitlines()),
    frozen_files_checked=len(frozen['sha256']),frozen_files_changed=changed,
    heuristic_sentence_review=sentence_review,errors=errors,warnings=warnings,
    limits='This check verifies stored structure, references and hash preservation; it does not inspect manuscript images, certify all readings, or validate scientific arguments.')
(R/'records/final_research_check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
