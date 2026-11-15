#!/usr/bin/env python3
"""Locate brief note cues in the frozen files without modifying them.
Normalization is only an aid to locating quotations; the diplomatic files remain authoritative.
"""
import json, re, unicodedata
from pathlib import Path
from research_items import ITEMS
ROOT=Path(__file__).resolve().parent.parent

def norm(s):
    s=unicodedata.normalize('NFKD',s)
    s=''.join(c for c in s if not unicodedata.combining(c))
    s=re.sub(r'\\(?:unsure|deleted|inserted|uline|uuline|margin|text|mathrm|operatorname|mathbf|mathcal|underline|overline)\s*', '',s)
    s=s.replace('\\prime',"'").replace('^{\\prime}',"'")
    s=re.sub(r'\\[A-Za-z]+', '',s)
    return ' '.join(re.findall(r'\w+',s.lower()))

records=[]
for item in ITEMS:
    # Only numerals in the scans field, expanding simple ranges written with dash/en dash.
    source_scans=set()
    field=item['scans']
    for a,b in re.findall(r'(\d{3})[–-](\d{3})',field):
        source_scans.update(range(int(a),int(b)+1))
    source_scans.update(map(int,re.findall(r'\b\d{3}\b',field)))
    source_scans.discard(122)
    parts=[p.strip() for p in re.split(r';|\.\.\.|…',item['quote']) if norm(p)]
    matches=[]
    for n in sorted(source_scans):
        path=ROOT/'pages'/f'MPL_136_095-141_136_scan{n:03d}.tex'
        if not path.exists():continue
        for ln,line in enumerate(path.read_text().splitlines(),1):
            for part in parts:
                if norm(part) and norm(part) in norm(line):
                    matches.append(dict(scan=n,line=ln,cue_part=part))
    records.append(dict(id=item['id'],quote=item['quote'],matches=matches,status='located' if matches else 'manual_review'))
OUT=ROOT/'records'/'note_quote_locations.json'
OUT.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(notes=len(records),located=sum(bool(x['matches']) for x in records),manual_review=[x['id'] for x in records if not x['matches']]),ensure_ascii=False))
for r in records:
    if not r['matches']:print(r['id'],r['quote'])
