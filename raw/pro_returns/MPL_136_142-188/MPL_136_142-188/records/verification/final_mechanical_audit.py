#!/usr/bin/env python3
"""Mechanical deliverable audit only: hashes, structure, metadata, and bounds."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import re,csv,json,hashlib
ROOT=Path('/workspace/scratch/fce80d805cc4/MPL_136_142-188')
OUT=Path('/workspace/scratch/fce80d805cc4/verification')
PACKAGE='MPL_136_142-188'
SCANS=[n for n in range(142,189) if n!=161]
EXPECTED_IDS={f'N{n:03d}' for n in range(1,69)}
errors=[];warnings=[]

def hashes(text):
 result={}
 for line in text.splitlines():
  m=re.fullmatch(r'(?:sha256\s+)?([0-9a-fA-F]{64})\s+\*?(.+?)\s*',line)
  if m:result[m[2].removeprefix('./')]=m[1].lower()
 return result

def check_hashes(entries,label,expected):
 if set(entries)!=expected:errors.append(label+' has an unexpected hashed-path set')
 mismatches=[]
 for name,digest in entries.items():
  path=ROOT/name
  if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=digest:mismatches.append(name)
 if mismatches:errors.append(label+' hash mismatches: '+', '.join(mismatches))
 return {'entries':len(entries),'mismatches':mismatches}

page_paths=[ROOT/'pages'/f'{PACKAGE}_136_scan{n}.tex' for n in SCANS]
page_lengths={n:len(path.read_text().splitlines()) for n,path in zip(SCANS,page_paths)}
combined=ROOT/f'{PACKAGE}_transcription.tex'
expected_paths={str(path.relative_to(ROOT)) for path in page_paths}|{combined.name}
log=(ROOT/'progress.log').read_text()
freeze_hashes=hashes((ROOT/'records/frozen.sha256').read_text())
log_hashes=hashes(log)
freeze_check=check_hashes(freeze_hashes,'freeze manifest',expected_paths)
log_check=check_hashes(log_hashes,'progress log',expected_paths)
if freeze_hashes!=log_hashes:errors.append('Freeze manifest and progress-log hash maps differ')
concatenated=b''.join(path.read_bytes() for path in page_paths)
combined_equal=combined.read_bytes()==concatenated
if not combined_equal:errors.append('Combined transcription differs from exact ordered page concatenation')
with (ROOT/f'{PACKAGE}_inventory.csv').open(newline='') as f:inventory=list(csv.DictReader(f))
if len(inventory)!=949:errors.append(f'Inventory row count is {len(inventory)}, expected 949')
if any(row['transcribed']!='yes' for row in inventory):errors.append('Inventory contains a transcribed value other than yes')
done=[int(n) for n in re.findall(r'(?m)^136 scan (\d+) done .+',log)]
audited=[int(n) for n in re.findall(r'(?m)^(?:136 )?scan (\d+) audited .+',log)]
for label,values in [('done',done),('audited',audited)]:
 if Counter(values)!=Counter(SCANS):errors.append(label+' markers do not cover all 46 scans exactly once')

notes=(ROOT/f'{PACKAGE}_notes.md').read_text()
heading_pattern=re.compile(r'(?m)^#{1,6}\s+(N\d{3})\b[^\n]*')
headings=list(heading_pattern.finditer(notes));heading_ids=[m[1] for m in headings]
if Counter(heading_ids)!=Counter(EXPECTED_IDS):errors.append('N001–N068 heading coverage is not exactly once each')
fields=['Source','Kind','Short source quotation','Context','Register']
field_pattern=re.compile(r'^\s*(?:[-*]\s*)?(?:\*\*)?('+ '|'.join(map(re.escape,fields))+r')(?:\*\*)?\s*:(?:\*\*)?\s*(.*)$',re.M)
metadata={};missing_fields=[];duplicate_fields=[];bounds_checks=[];unparsed_segments=[]
for index,heading in enumerate(headings):
 identity=heading[1];end=headings[index+1].start() if index+1<len(headings) else len(notes)
 section=notes[heading.end():end]
 pairs=field_pattern.findall(section);counts=Counter(name for name,_ in pairs)
 values={name:value.strip() for name,value in pairs}
 for field in fields:
  if counts[field]==0 or not values.get(field):missing_fields.append({'id':identity,'field':field})
  if counts[field]>1:duplicate_fields.append({'id':identity,'field':field,'count':counts[field]})
 metadata[identity]=values
 source=values.get('Source','')
 for segment in source.split(';'):
  if not re.search(r'\blines?\b',segment,re.I):continue
  lineword=re.search(r'\b(?:TeX\s+)?lines?\s+',segment,re.I)
  if not lineword:
   unparsed_segments.append({'id':identity,'metadata':'Source','reason':'line wording without following numeric range'});continue
  before=segment[:lineword.start()]
  before=re.sub(r'(?:printed\s+)?p\.\s*\d+(?:\s*[-–—]\s*\d+)?','',before,flags=re.I)
  candidates=[int(x) for x in re.findall(r'\b\d{3}\b',before) if int(x)!=136]
  tail=segment[lineword.end():]
  spec=re.match(r'\d+(?:\s*[-–—]\s*\d+)?(?:\s*(?:,|and|et)\s*\d+(?:\s*[-–—]\s*\d+)?)*',tail)
  tail=spec[0] if spec else ''
  ranges=[]
  for m in re.finditer(r'\b(\d+)(?:\s*[-–—]\s*(\d+))?',tail):
   a=int(m[1]);b=int(m[2] or m[1]);ranges.append((a,b))
  if not candidates or not ranges:
   unparsed_segments.append({'id':identity,'metadata':'Source','reason':'missing unambiguous scan or numeric range'});continue
  for scan in candidates:
   for start,endline in ranges:
    limit=page_lengths.get(scan)
    status='pass' if limit is not None and 1<=start<=endline<=limit else 'out_of_bounds'
    entry={'id':identity,'scan':scan,'start_line':start,'end_line':endline,'fragment_length':limit,'status':status}
    bounds_checks.append(entry)
    if status!='pass':errors.append(f'{identity}: scan {scan}, source lines {start}–{endline}, fragment length {limit}')
if missing_fields:errors.append('Missing/empty note metadata fields')
if duplicate_fields:errors.append('Duplicate note metadata fields')
references=re.findall(r'\bN(\d+)\b',notes)
out_of_range=sorted({f'N{n}' for n in references if not 1<=int(n)<=68})
if out_of_range:errors.append('Out-of-range N references: '+','.join(out_of_range))
queries=json.loads((ROOT/'records/context_search.json').read_text())
query_ids=[item.get('id') for item in queries]
if Counter(query_ids)!=Counter(EXPECTED_IDS):errors.append('Context query records do not cover N001–N068 exactly once')
empty_queries=[item.get('id') for item in queries if not isinstance(item.get('query'),str) or not item['query'].strip()]
if empty_queries:errors.append('Missing/empty query strings: '+','.join(map(str,empty_queries)))

doubts=(ROOT/f'{PACKAGE}_doubts.md').read_text()
row_mentions=[]
for lineno,line in enumerate(doubts.splitlines(),1):
 for pattern in [r'\b([0-9][0-9,]*)[-‑– ]row\s+inventory\b',r'\binventory\s+(?:contains|has|records)?\s*([0-9][0-9,]*)\s+rows\b']:
  for m in re.finditer(pattern,line,re.I):
   number=int(m[1].replace(',',''));row_mentions.append({'markdown_line':lineno,'row_count':number,'matches_inventory':number==len(inventory)})
   if number!=len(inventory):errors.append(f'Doubts line {lineno}: inventory count {number} differs from {len(inventory)}')
if not row_mentions:warnings.append('No literal inventory row-count statement recognized in doubts file')
summary={
 'checked_at_utc':datetime.now(timezone.utc).isoformat(),'freeze_manifest':freeze_check,'progress_hashes':log_check,
 'freeze_maps_identical':freeze_hashes==log_hashes,'combined_exact_concatenation':combined_equal,
 'combined_sha256':hashlib.sha256(combined.read_bytes()).hexdigest(),'inventory_rows':len(inventory),
 'done_markers':len(done),'audit_markers':len(audited),'note_heading_count':len(headings),'note_ids':heading_ids,
 'missing_metadata_fields':missing_fields,'duplicate_metadata_fields':duplicate_fields,
 'context_query_records':len(queries),'empty_context_queries':empty_queries,'N_reference_occurrences':len(references),
 'out_of_range_N_references':out_of_range,'source_line_range_checks':bounds_checks,'source_metadata_segments_unparsed':unparsed_segments,
 'doubts_inventory_count_mentions':row_mentions,'errors':errors,'warnings':warnings,
}
(OUT/'final_mechanical_audit.json').write_text(json.dumps(summary,indent=2)+'\n')
lines=['# Final mechanical audit','',f"Checked: {summary['checked_at_utc']}",'',f"Result: {len(errors)} errors; {len(warnings)} warnings.",'', '| Check | Result |','|---|---|',f'| Freeze manifest / progress-log hashes | {len(freeze_hashes)} / {len(log_hashes)} entries; all checked |',f'| Exact combined concatenation | {combined_equal} |',f'| Inventory | {len(inventory)} rows |',f'| Done / audited markers | {len(done)} / {len(audited)} |',f'| Numbered note headings | {len(headings)} |',f'| Required metadata | {len(missing_fields)} missing/empty; {len(duplicate_fields)} duplicated |',f'| Associated context-query records | {len(queries)}; {len(empty_queries)} empty queries |',f'| N cross-references | {len(references)} occurrences; {len(out_of_range)} out of range |',f'| Source line-range bounds | {len(bounds_checks)} checks; {sum(r["status"]!="pass" for r in bounds_checks)} out of bounds |',f'| Source segments with line wording not parsed | {len(unparsed_segments)} |',f'| Doubts inventory row-count claims | {len(row_mentions)} recognized; {sum(not r["matches_inventory"] for r in row_mentions)} inconsistent |','']
if errors:
 lines+=['## Errors','']+['- '+e for e in errors]+['']
if warnings:
 lines+=['## Warnings','']+['- '+w for w in warnings]+['']
if unparsed_segments:
 lines+=['## Unparsed source metadata segments','']+[f"- {r['id']}: {r['reason']}" for r in unparsed_segments]+['']
lines+=['This audit performs only byte, syntax, metadata, and numerical-bound checks. It does not assess the notes’ semantic claims or inspect images. No deliverable was changed.','']
(OUT/'final_mechanical_audit.md').write_text('\n'.join(lines))
print(json.dumps({k:v for k,v in summary.items() if k not in {'note_ids','source_line_range_checks'}},indent=2))
print('Parsed source range checks:',len(bounds_checks))
raise SystemExit(1 if errors else 0)
