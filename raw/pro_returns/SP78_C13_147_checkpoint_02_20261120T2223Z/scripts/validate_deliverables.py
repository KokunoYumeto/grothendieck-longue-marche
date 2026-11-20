#!/usr/bin/env python3
"""Structural checks only: no OCR, rendering, compilation or textual inference."""
from pathlib import Path
import csv,json,re,hashlib,sys
root=Path(__file__).resolve().parents[1]
scans=[54,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,72,73,74,75,76,77,78,79]
complete='--complete' in sys.argv
reports={int(p.stem[-3:]):json.loads(p.read_text()) for p in (root/'reviewed').glob('*.json')}
issues=[]
def issue(s):issues.append(s)
if complete and set(reports)!=set(scans):issue(f'Approved scans mismatch: {sorted(reports)}')
for n,r in sorted(reports.items()):
    name=f'147_scan{n:03}';p=root/'pages'/f'{name}.tex'
    if not p.exists():issue(f'{name}: missing page');continue
    s=p.read_text()
    if not re.search(r'\\scanpage\{'+str(n)+r'\}',s):issue(f'{name}: wrong/missing scanpage')
    depth=0
    for c in re.sub(r'\\[{}%]|%[^\n]*','',s):
        if c=='{':depth+=1
        elif c=='}':depth-=1
        if depth<0:break
    if depth:issue(f'{name}: unbalanced curly braces {depth}')
    for c in r.get('changes',[]):
        if not (c.get('against_C') or c.get('against_H')):issue(f'{name}: no witness difference at {c.get("id")}')
        if not c.get('crop') or not (root/'crops'/Path(c['crop']).name).is_file():issue(f'{name}: missing change crop {c.get("id")}')
        if len(c.get('box',[]))!=4:issue(f'{name}: missing box {c.get("id")}')
    ids=[d['id'] for d in r.get('decisions',[])]
    if len(ids)!=len(set(ids)):issue(f'{name}: duplicate mark decision')
    for d in r.get('decisions',[]):
        if d['decision']!='undecided' and ('(' not in d.get('crop','') or '.png' not in d.get('crop','')):issue(f'{name}: resolved mark without a crop {d["id"]}')
    for row in r.get('inventory',[]):
        if row.get('transcribed')!='yes':issue(f'{name}: untranscribed inventory element {row.get("element")}')
    for suffix in ['boxes','first']+(['second'] if complete else []):
        if not (root/'second'/f'{name}_{suffix}.tsv').exists():issue(f'{name}: missing {suffix} reading')
    if complete and not r.get('audit_complete'):issue(f'{name}: audit not approved')
combined=root/'SP78_C13_147_transcription.tex'
if combined.exists():
    target='\\cotefile{147}\n\n'+'\n\n'.join((root/'pages'/f'147_scan{n:03}.tex').read_text().rstrip() for n in sorted(reports))+'\n'
    if combined.read_text()!=target:issue('Combined fragment does not match page files')
if complete:
    expected=list(csv.DictReader((root.parent/'input/SP78_C13_147_texts/MARKS.tsv').open(),delimiter='\t'))
    actual=list(csv.DictReader((root/'decisions.tsv').open(),delimiter='\t'))
    if [r['id'] for r in expected]!=[r['id'] for r in actual]:issue('decisions.tsv does not reproduce all MARKS IDs in input order')
    for f in ['SP78_C13_147_changes.md','SP78_C13_147_collation.tsv','SP78_C13_147_doubts.md','SP78_C13_147_inventory.csv','SP78_C13_147_notes.md','SP78_C13_147_sheet_feedback.md','SP78_C13_147_hand_log.md','CHECK_EVENTS.tsv','progress.log']:
        if not (root/f).is_file():issue(f'Missing deliverable {f}')
result={'approved_pages':len(reports),'complete_check':complete,'issues':issues}
print(json.dumps(result,ensure_ascii=False,indent=2))
sys.exit(1 if issues else 0)
