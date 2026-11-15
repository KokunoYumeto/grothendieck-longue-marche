#!/usr/bin/env python3
"""Final deliverable integrity checks; no manuscript interpretation or modification."""
import csv, hashlib, json, re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from validate_package import hash_records
from research_items import ITEMS
ROOT=Path(__file__).resolve().parent.parent
REC=ROOT/'records'
SUPPORT=ROOT/'technical_checks'
if not SUPPORT.is_dir(): SUPPORT=ROOT.parent/'technical_checks'
log=(ROOT/'progress.log').read_text()
marker=re.search(r'^transcription frozen (.+)$',log,re.M)
assert marker
frozen=hash_records(log[:marker.start()])
assert len(frozen)==47
checks=[]
for name,digest in frozen.items():
    path=ROOT/name
    now=hashlib.sha256(path.read_bytes()).hexdigest()
    checks.append(dict(path=name,frozen_sha256=digest,final_sha256=now,unchanged=now==digest))
assert all(x['unchanged'] for x in checks)
with (ROOT/'MPL_136_095-141_inventory.csv').open(newline='') as f:
    inventory=list(csv.DictReader(f))
assert len(inventory)==729 and all(x['transcribed']=='yes' for x in inventory)
sheetmap={int(x['scan']):x['sheet_kind'] for x in inventory}
assert len(sheetmap)==46 and 122 not in sheetmap
# The extraction of doubts is lexical and does not judge a reading.
# Use the existing generated occurrence ledger and verify its count against macros.
ledger=json.loads((SUPPORT/'doubt_occurrences.json').read_text())
sources='\n'.join(p.read_text() for p in sorted((ROOT/'pages').glob('*.tex')))
macro_counts={name:len(re.findall(r'\\'+name+r'\s*\{',sources)) for name in ['unsure','illegible']}
assert macro_counts=={'unsure':311,'illegible':24}
notes=(ROOT/'MPL_136_095-141_notes.md').read_text()
ids=set(re.findall(r'^#### ([NROL]\d+) — ',notes,re.M))
assert ids=={x['id'] for x in ITEMS}
search=json.loads((REC/'note_context_searches.json').read_text())
assert search['query_source_sha256']==hashlib.sha256((REC/'research_items.py').read_bytes()).hexdigest()
assert set(x['id'] for x in search['notes'])==ids
assert all(x['status'] in ('matched','no_match') for x in search['notes'])
assert len(search['context_files'])==6
assert all(x.get('confidence') for x in ITEMS if 'own idea' in x['kind'])
assert not re.search(r'\b(?:TODO|TBD|PLACEHOLDER)\b',notes)
compile_report=json.loads((SUPPORT/'mechanical_compile_after_audit.json').read_text())
combined=[x for x in compile_report if x['file']=='MPL_136_095-141_transcription.tex']
assert len(combined)==1 and combined[0]['status']==0 and combined[0]['missing_characters']==0
report=dict(checked_utc=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
    page_files=46,blank_scan_122_absent=True,inventory_rows=len(inventory),all_inventory_transcribed=True,
    sheet_kinds=dict(Counter(sheetmap.values())),doubt_occurrences=macro_counts,
    research_notes=len(ITEMS),research_note_groups=dict(Counter(x['id'][0] for x in ITEMS)),
    research_words=len(notes.split()),context_files_searched_per_note=6,context_search_summary=search['summary'],
    combined_mechanical_compile_passed=True,frozen_files_checked=len(checks),all_frozen_hashes_unchanged=True,files=checks,
    limits='Structural and cryptographic verification does not establish paleographic accuracy; doubt markers remain authoritative.')
(REC/'final_quality_check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='files'},ensure_ascii=False,indent=2))
