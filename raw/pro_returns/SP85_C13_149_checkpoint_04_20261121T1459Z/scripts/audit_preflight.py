"""Check literal coverage of editing and margin content in frozen first readings.

This is a bookkeeping diagnostic, not image reading. A flagged item requires
manual review because a box may use a different but equivalent transcription.
"""
from pathlib import Path
import csv, json, re

ROOT=Path(__file__).resolve().parents[1]

def contents(text, command):
    for m in re.finditer(r'\\'+command+r'\{',text):
        start=m.end();depth=1;i=start
        while i<len(text) and depth:
            if text[i] in '{}':
                preceding=0;j=i-1
                while j>=0 and text[j]=='\\':preceding+=1;j-=1
                if preceding%2==0:depth+=1 if text[i]=='{' else -1
            i+=1
        yield text[start:i-1]

def compact(text):return re.sub(r'\s+','',text)

report=[]
for page in sorted((ROOT/'pages').glob('*.tex')):
    first=ROOT/'second'/f'{page.stem}_first.tsv'
    if not first.exists():continue
    readings=[compact(r['reading']) for r in csv.DictReader(first.open(),delimiter='\t')]
    for command in ['inserted','deleted','margin','mspage']:
        for content in contents(page.read_text(),command):
            if not any(compact(content) in r for r in readings):
                report.append({'page':page.stem,'kind':command,'content':content})
(ROOT/'records/audit_preflight.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(report,ensure_ascii=False,indent=2))
