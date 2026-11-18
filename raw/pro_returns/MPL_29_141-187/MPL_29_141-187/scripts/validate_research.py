#!/usr/bin/env python3
"""Check research identifiers, metadata and search/check-event coverage.

This is a formatting/coverage gate, not a mathematical proof checker or a
substitute for editorial review of quotations, sentence counts or citations.
"""
from pathlib import Path
import csv, re, sys

root=Path(__file__).resolve().parents[1]
text=(root/'MPL_29_141-187_notes.md').read_text()
notes=list(re.finditer(r'^## (N\d+\.\d+) — ([^\n]+)\n([\s\S]*?)(?=^## |^# |\Z)',text,re.M))
main=[m[1] for m in notes]
standing=re.findall(r'^\| ((?:SF|T)[A-Za-z0-9]+) \|',text,re.M)
ids=main+standing
errors=[]
if len(ids)!=len(set(ids)):errors.append('Duplicate note or standing-table ID')
allowed={'conjecture','unproved claim','unpursued implication','own idea','reading question','self-flagged: a step he himself marks as unverified','withdrawn in the same text'}
for m in notes:
    nid,body=m[1],m[3]
    k=re.search(r'\*\*Kind:\*\* (.*?)(?= \*\*|\n|$)',body)
    kind=k[1].rstrip('. ').strip() if k else ''
    if kind not in allowed:errors.append(f'{nid}: missing/noncanonical kind {kind!r}')
    if kind=='own idea' and not re.search(r'\*\*Confidence(?:/reason)?:\*\*',body):errors.append(f'{nid}: own idea lacks confidence/reason field')
    if '**Context:**' not in body:errors.append(f'{nid}: no context locator')
    if not re.search(r'\*\*(?:Witness|File/scan|File/scans|Scan|Scans):\*\*',body):errors.append(f'{nid}: no scan witness')
with (root/'records/CONTEXT_QUERIES.tsv').open(newline='') as f: queries=list(csv.DictReader(f,delimiter='\t'))
with (root/'records/CONTEXT_SEARCHES.tsv').open(newline='') as f: searches=list(csv.DictReader(f,delimiter='\t'))
qid={r['note_id'] for r in queries};sid={r['note_id'] for r in searches}
if qid!=set(ids):errors.append(f'Query coverage mismatch: missing {sorted(set(ids)-qid)}, extra {sorted(qid-set(ids))}')
if sid!=set(ids):errors.append(f'Executed-search coverage mismatch: missing {sorted(set(ids)-sid)}, extra {sorted(sid-set(ids))}')
allowed_types={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found',"refuted, with the refined statement's id"}
with (root/'CHECK_EVENTS.tsv').open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t')
    if reader.fieldnames!=['statement_id','date','who','type','outcome']:errors.append('Incorrect CHECK_EVENTS header')
    events=list(reader)
for row in events:
    if any(not v.strip() for v in row.values()):errors.append('Empty check-event field')
    if row['type'] not in allowed_types:errors.append('Noncanonical check-event type: '+row['type'])
    if 'refuted' in row['type'] and not re.search(r'Refined|refined',row['outcome']):errors.append('Refutation has no refined-statement reference: '+row['statement_id'])
for ref in re.findall(r'\bN\d+\.\d+\b',text):
    if ref not in set(main):errors.append('Broken note reference: '+ref)
for key in set(re.findall(r'\[(S\d+)(?:,|\])',text)):
    if not re.search(r'^\| '+key+r' \|',text,re.M):errors.append('Missing external source key: '+key)
if 'WORKING INTEGRATION' in text:errors.append('Working-draft marker remains in final report')
print('RESEARCH STRUCTURAL CHECK: '+('FAIL' if errors else 'PASS'))
print(f'Main notes: {len(main)}; self-flagged entries: {sum(x.startswith("SF") for x in standing)}; title/count entries: {sum(x.startswith("T") for x in standing)}')
print(f'Per-item executed searches: {len(sid)}; actual mathematical check events: {len(events)}')
print('Scope: identifiers, fields, reference integrity and recorded-search coverage only; no proof or image-reading certification.')
for e in errors:print('ERROR:',e)
sys.exit(bool(errors))
