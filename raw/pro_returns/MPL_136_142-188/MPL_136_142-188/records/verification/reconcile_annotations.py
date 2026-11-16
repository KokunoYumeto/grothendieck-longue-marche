"""Quote exact source macros and existing inventory metadata for manual reconciliation."""
from pathlib import Path
import csv,io,hashlib,json
from tex_macro_extract import extract_file
ROOT=Path('/workspace/scratch/fce80d805cc4/MPL_136_142-188')
OUT=Path('/workspace/scratch/fce80d805cc4/verification')
SPECS=[
 (144,['deleted:6','deleted:7','deleted:9','deleted:10'],[20,33],
  'The two-count difference is accounted for by two existing grouped deletion rows. Element 20 explicitly names both `hom dans C_k` and `B`; element 33 explicitly names both `u_i:M` and `est loc. finie`. Each of these rows corresponds textually to two separate deleted arguments. No additional fragment is left unaccounted for by this count comparison.'),
 (146,['margin:1','margin:2'],[13,19],
  'The first margin wrapper contains a figure. Element 13 records that figure as a drawing; element 19 records the numeric margin. The extra margin wrapper thus has an existing drawing entry.'),
 (155,['diagram:1','deleted:2','deleted:3'],[3,4,17,24,25],
  'The upper array has existing display entries 3 and 4; its diagram-wrapper count therefore exceeds the number of rows classified as diagram. At the bottom, element 25 names the first of the two deleted objects on source line 48. No separate row explicitly names the second deleted object, `\\operatorname{Hom}_k(s^k,C\\otimes k)`. The existing first-words field may label the whole cancelled row, so the intended grouping needs the sole visual reader to decide.'),
 (157,['diagram:1'],[17,22],
  'The diagram starts with the expression identified by display element 17 (`s^k=prod`). Element 22 records another product expression and is included for disambiguation. There is existing display coverage of these expressions, while no row is classified as diagram. The source fragment below identifies the exact arrow-bearing block for metadata reconciliation.'),
 (158,['margin:1','margin:2','margin:3','margin:4'],[15,16,17,18],
  'The first margin wrapper contains a figure recorded by drawing element 15. The other three margin wrappers have the three numeric margin-note entries 16–18. The extra margin wrapper therefore has existing drawing coverage.'),
 (162,['margin:1','deleted:7','deleted:8','deleted:9'],[1,2,25,29,33,34],
  'The title inside the first margin wrapper is represented by text element 1 and drawing element 2. The remaining three margins have margin-note entries 29, 33 and 34. Three deleted arguments on source lines 47–48 all contain `1`; grouped deletion element 25 says `index 1 on A prime twice and a prime`. That grouped row accounts for the count difference structurally, but its wording and the three literal arguments require the reader’s reconciliation.'),
 (168,['deleted:2','deleted:7','deleted:8','deleted:9','deleted:10','deleted:11'],[3,4,23,26],
  'All four extra deletion occurrences have existing grouped or differently classified coverage: the outer deleted formula is display element 3, whose first-words field explicitly says deleted; its nested alpha deletion is element 4. Element 23 explicitly lists the three deleted arguments at source line 40, accounting for two extra occurrences. Element 26 explicitly says twice and accounts for the two arguments at source line 47, accounting for one extra occurrence.'),
 (184,['margin:1'],[6,12,34],
  'The first margin wrapper contains only a deleted formula. Deletion element 6 records that formula and its marginal position. The other two margins have entries 12 and 34. The extra margin-wrapper count therefore has existing deletion coverage.'),
]
with (ROOT/'MPL_136_142-188_inventory.csv').open(newline='') as f:
 reader=csv.DictReader(f);fields=reader.fieldnames;inventory=[dict(row,csv_row=i) for i,row in enumerate(reader,2)]
report=['# Annotation/inventory reconciliation — source-only review','','This report quotes the current LaTeX and existing inventory metadata. It makes no claims about unseen ink. Counts are reconciled through explicit grouped labels or nested wrapper structure. No deliverable was changed.','','## Items needing the reader’s decision','','- Scan 155, source line 48: the second deleted diagram object has no separately identifying inventory row; deletion element 25 may be intended to cover both objects.','- Scan 162, source lines 47–48: three deleted arguments are literal `1`; grouped element 25 describes “twice and a prime.”','- Scan 155 upper array and scan 157 arrow-bearing product block have display rows but no corresponding diagram-kind rows.','', '## Exact evidence by scan','']
records=[]
for scan,refs,elements,explanation in SPECS:
 path=ROOT/'pages'/f'MPL_136_142-188_136_scan{scan}.tex'
 macros,errors=extract_file(path)
 by_id={m['id']:m for m in macros}
 report += [f'### Scan {scan}','',explanation,'']
 selected=[]
 for ref in refs:
  key=f'{scan}:{ref}'
  m=by_id[key];selected.append(m)
  report += [f"Source `{m['id']}`, TeX line {m['line']}"+ (f"–{m['end_line']}" if m['end_line']!=m['line'] else '')+':','', '```latex',m['source'],'```','']
 report += ['Existing inventory rows (CSV row numbers shown separately; fields otherwise reproduced exactly):','']
 selected_rows=[]
 for r in inventory:
  if int(r['scan'])==scan and int(r['element'].split('.')[-1]) in elements:
   selected_rows.append(r)
   stream=io.StringIO();writer=csv.DictWriter(stream,fieldnames=fields);writer.writerow({k:r[k] for k in fields})
   report += [f"CSV row {r['csv_row']}, scan/element {scan}/{r['element']}:",'','```csv',stream.getvalue().rstrip('\r\n'),'```','']
 records.append({'scan':scan,'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'explanation':explanation,'macros':selected,'inventory_rows':selected_rows})
(OUT/'annotation_inventory_reconciliation.md').write_text('\n'.join(report),encoding='utf-8')
(OUT/'annotation_inventory_reconciliation.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Saved exact-source reconciliation for',len(SPECS),'scans.')
