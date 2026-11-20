#!/usr/bin/env python3
"""Documentary and structural checks only; never compiles LaTeX or recognizes images."""
from pathlib import Path
import argparse,csv,hashlib,json,re
root=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--partial',action='store_true');a=p.parse_args()
errors=[];warnings=[]
records=[json.loads(f.read_text()) for f in sorted((root/'records').glob('scan[0-9][0-9][0-9].json'))]
scans=[r['scan'] for r in records]
expected=list(range(2,10))
if (scans!=expected and not a.partial) or (scans!=expected[:len(scans)]):errors.append('Page record coverage/order is incomplete or nonconsecutive.')
kinds={'text','display','diagram','drawing','margin note','insertion','deletion'}
collation_kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
expected_cols=['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence']
src=root.parent/'source/SP35_CW_156-7_witnesses/codex/H156-01/pages'
page_report=[]
all_ids=[]
for r in records:
 n=r['scan'];page=root/'pages'/f'H156-01_156-7_scan{n:03d}.tex'
 if not page.exists():errors.append(f'Missing page {n}');continue
 text=page.read_text()
 if not re.search(r'\\scanpage\{0*'+str(n)+r'\}',text):errors.append(f'Wrong scan marker {n}')
 if len(r['unresolved'])!=text.count(r'\unsure{')+text.count(r'\illegible{'):errors.append(f'Doubt inventory/TeX count differs on {n}')
 c=(src/page.name).read_text()
 if len(r['C_doubt_audit'])!=c.count(r'\unsure{')+c.count(r'\illegible{'):errors.append(f'C doubt audit count differs on {n}')
 for rn in ['R1','R2','R3']:
  for suffix in ['tex','json','md']:
   if not (root/'readers'/rn/f'scan{n:03d}.{suffix}').exists():errors.append(f'Missing {rn} scan{n:03d}.{suffix}')
 for d in r['decisions']:
  all_ids.append(d['id'])
  if set(d.get('readers',{}))!={'R1','R2','R3'}:errors.append('Incomplete reader comparison '+d['id'])
  if d['confidence'] not in {'high','medium','low'}:errors.append('Invalid confidence '+d['id'])
  if d.get('diff_H') and d['kind'] not in collation_kinds:errors.append('Invalid H collation kind '+d['id'])
  for crop in d.get('crop','').split('; ') if d.get('crop') else []:
   if not (root/crop).exists():errors.append('Missing evidence crop '+crop)
 for x in r['inventory']:
  if x['kind'] not in kinds:errors.append(f'Invalid inventory kind on {n}: '+x['kind'])
 if re.search(r'\\(?:newcommand|renewcommand|def|documentclass|begin\{document\})\b',text):errors.append(f'Preamble or new macro in page {n}')
 page_report.append(dict(scan=n,decisions=len(r['decisions']),C_doubts=len(r['C_doubt_audit']),unresolved=len(r['unresolved']),inventory=len(r['inventory']),sha256=hashlib.sha256(page.read_bytes()).hexdigest()))
if len(all_ids)!=len(set(all_ids)):errors.append('Duplicate decision IDs')
combined=root/'SP35_CW_156-7_transcription.tex'
expected_combined='\n\n'.join((root/'pages'/f'H156-01_156-7_scan{n:03d}.tex').read_text().rstrip() for n in scans)+'\n'
if combined.read_text()!=expected_combined:errors.append('Combined fragment differs from ordered page files')
with (root/'SP35_CW_156-7_collation.tsv').open(newline='') as f:
 reader=csv.DictReader(f,delimiter='\t');hrows=list(reader)
 if reader.fieldnames!=expected_cols:errors.append('Wrong collation columns')
 if len(hrows)!=sum(bool(d.get('diff_H')) for r in records for d in r['decisions']):errors.append('H collation row count differs')
 for d in hrows:
  if int(d['our_scan'])-1!=int(d['their_page']):errors.append('Wrong H-to-scan mapping')
  if d['marked_in_H'] not in {'yes','no'}:errors.append('Invalid H doubt flag')
with (root/'SP35_CW_156-7_inventory.csv').open(newline='') as f:
 reader=csv.DictReader(f);inv=list(reader)
 if reader.fieldnames!=['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']:errors.append('Wrong inventory columns')
 if any(d['transcribed']!='yes' for d in inv):errors.append('Inventory contains untranscribed element')
 if len(inv)!=sum(len(r['inventory']) for r in records):errors.append('Inventory row count differs')
progress=(root/'progress.log').read_text()
for n in scans:
 if not re.search(r'^scan '+f'{n:03d}'+r' done \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC$',progress,re.M):errors.append(f'Missing completion gate for scan {n}')
if list(root.rglob('*.zip')):errors.append('Nested ZIP found inside output tree')
if (root/'source').exists() or (root/'upload').exists():errors.append('Original attachment tree found inside output')
report=dict(pages=page_report,collation_rows=len(hrows),inventory_rows=len(inv),errors=errors,warnings=warnings,validation_scope='This validator performs no compilation or OCR. Documentary counts, paths, coverage, macro declarations and ordered concatenation checked. No manuscript transcription was compiled. A separate synthetic diagnostic compilation deviation is explicitly recorded in records/protocol_deviations.md.')
(root/'records/package_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
