"""Consolidate reviewed post-freeze research contributions; never edits transcription."""
from pathlib import Path
import csv
import json
import re

ROOT=Path(__file__).resolve().parents[1]
REC=ROOT/'records'
assert (REC/'frozen_hashes.json').exists()

def items(filename):
    text=(REC/filename).read_text(encoding='utf-8')
    matches=list(re.finditer(r'^#{2,3} ([ADFR]\d\d) — ([^\n]+)\n',text,re.M))
    result={}
    for i,m in enumerate(matches):
        end=matches[i+1].start() if i+1<len(matches) else len(text)
        body=text[m.end():end]
        body=re.split(r'^## Verification limits',body,flags=re.M)[0].strip()
        result[m.group(1)]=(m.group(2),body,filename)
    return result

groups={}
for filename in ['research_root.md','research_arithmetic.md','research_fourier.md']:
    for key,value in items(filename).items():
        assert key not in groups
        groups[key]=value

consolidated={'D12':['A21'],'D14':['A20'],'A08':['D20'],'A09':['D22','D23'],'A13':['F17','F18'],'A19':['D13'],'F02':['D20'],'F23':['R01','R02']}
sections=[
 ('Arithmetic, Jacobians, and the requested 1983 bridge',[x for x in groups if x.startswith('A') and x not in consolidated]),
 ('Functor foundations, local duality, and support comparisons',[x for x in groups if x.startswith('D') and x not in consolidated]),
 ('Cote 47, the seven cote 44 theorems, and the Oda comparison',[x for x in groups if x.startswith('F') and x not in consolidated]),
 ('Reused typescripts and cancelled drafts',[x for x in groups if x.startswith('R') and x not in consolidated]),
]
parts=[(REC/'research_editorial_front.md').read_text().rstrip()]
index=[]
for heading,ids in sections:
    parts.append('## '+heading)
    for note in ids:
        title,body,filename=groups[note]
        parts.append('### '+note+' — '+title+'\n\n'+body)
        index.append({'note':note,'title':title,'working_record':filename,'section':heading})

flags=REC/'research_standing_sections.md'
if not flags.exists():
    raise FileNotFoundError('Standing registers must be complete before assembly')
standing=flags.read_text(encoding='utf-8').strip()
standing=re.sub(r'^(#{1,3}) ',lambda m:m.group(1)+'# ',standing,flags=re.M)
parts.append(standing)
parts.append((REC/'research_editorial_back.md').read_text().strip())
output=ROOT/'MPL_43_094-142_notes.md'
output.write_text('\n\n'.join(parts)+'\n',encoding='utf-8')
(REC/'research_consolidation.json').write_text(json.dumps({'included_note_count':len(index),'consolidated_working_items':consolidated,'items':index},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (REC/'research_note_index.csv').open('w',newline='',encoding='utf-8') as f:
    writer=csv.DictWriter(f,fieldnames=['note','title','working_record','section'])
    writer.writeheader();writer.writerows(index)
print(json.dumps({'path':str(output),'substantive_items':len(index),'words':len(output.read_text().split()),'bytes':output.stat().st_size},indent=2))
