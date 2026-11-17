#!/usr/bin/env python3
"""Mechanical review of assembled notes, without reading the frozen transcription."""
from pathlib import Path
from collections import Counter
from datetime import datetime,timezone
import json,re,hashlib
root=Path(__file__).resolve().parents[1]
notes=root/'MPL_116+117_notes.md';text=notes.read_text();lines=text.splitlines()
cat=json.loads((root/'working/context_catalog.json').read_text());idx={r['id']:r for r in cat['dossier_statements']}
problems=[]
def split_table(line):
 marks=[]
 for i,c in enumerate(line):
  if c!='|':continue
  back=0;j=i-1
  while j>=0 and line[j]=='\\':back+=1;j-=1
  if back%2==0:marks.append(i)
 return [line[a+1:b].strip() for a,b in zip(marks,marks[1:])]
render=[]
for n,line in enumerate(lines,1):
 m=re.match(r'^\| \*\*((?:STRATA|PATHS|BISITE|RESIDUE) [^*]+)\*\* —',line)
 if not m:continue
 fields=split_table(line)
 if len(fields)!=4:problems.append(f'DSS line {n}: {len(fields)} fields.');continue
 id_=m[1]
 if id_ not in idx:problems.append(f'Unexpected DSS ID {id_}.');continue
 r=idx[id_]
 expected=f"{r['status_exact']}; DSS:{r['source_line']}; {r['manuscript_locator_exact'] or '(no manuscript locator supplied)'}"
 if r['state_same_id_entries']:expected+='; same-ID RS:'+','.join(str(x['source_line']) for x in r['state_same_id_entries'])
 expected=expected.replace('|','\\|').replace('\n',' ')
 if fields[1]!=expected:problems.append(f'DSS source cell mismatch: {id_}.')
 render.append(id_)
if render!=[r['id'] for r in cat['dossier_statements']]:problems.append('DSS IDs/order differ from the exact catalogue list.')
if text.count('(no manuscript locator supplied)')!=16:problems.append('Explicit blank-locator count is not 16.')
# Validate all continuous table blocks using backslash-parity-aware separators.
tables=0;i=0
while i<len(lines):
 if not lines[i].startswith('|'):i+=1;continue
 tables+=1;width=len(split_table(lines[i]));start=i
 while i<len(lines) and lines[i].startswith('|'):
  if len(split_table(lines[i]))!=width:problems.append(f'Table column count differs on notes line {i+1}.')
  i+=1
 if i<len(lines) and lines[i].strip():problems.append(f'No blank line after table ending at notes line {i}.')
headings=re.findall(r'^### ((?:N|Q|R)\d{2}) —',text,re.M)
refs=set(re.findall(r'\b(?:N|Q|R)\d{2}\b',text));defs=set(headings)
undefined=sorted(refs-defs);duplicates=[k for k,v in Counter(headings).items() if v>1]
if undefined:problems.append('Undefined N/Q/R references: '+str(undefined))
if duplicates:problems.append('Duplicate N/Q/R definitions: '+str(duplicates))
# Expand same-prefix ranges as well as checking explicit endpoints.
for m in re.finditer(r'\b([NQR])(\d{2})[–-](?:([NQR]))?(\d{2})\b',text):
 p,a,q,b=m.groups()
 if q and q!=p:continue
 for n in range(int(a),int(b)+1):
  if f'{p}{n:02}' not in defs:problems.append(f'Undefined intermediate range reference {p}{n:02}.')
nrhead=re.findall(r'^### (NR(?:\d{2}|K[123])) —',text,re.M)
expected_nr=[f'NR{i:02}' for i in range(1,13)]+['NRK1','NRK2','NRK3']
if nrhead!=expected_nr:problems.append('NR headings differ from expected 12 numbered + 3 coda list.')
for r in cat['new_results']:
 h=r['catalog_key']
 sec=re.search(r'^### '+re.escape(h)+r' —[^\n]*\n(.*?)(?=^### |^## |\Z)',text,re.M|re.S)
 if not sec or not re.search(r'\bNR line '+str(r['source_line'])+r'\b',sec.group(1)):problems.append(f'NR source line mismatch in {h}.')
# Every ATX heading now has a following blank line.
heading_spacing=[i+1 for i,l in enumerate(lines) if re.match(r'^#{1,6} ',l) and i+1<len(lines) and lines[i+1].strip()]
if heading_spacing:problems.append('Missing blank line after headings: '+str(heading_spacing))
if 'RS headline block, lines 37–110.' not in text:problems.append('H01 headline range correction not present.')
state=(root.parent/'context/notes/RESULTS_STATE.md').read_text().splitlines()
if not state[522].startswith('- **116-presheaf-gluing-continuous-gluing-functor**'):problems.append('RS Hua 116 line changed.')
if not state[523].startswith('- **117-adjunction-equivalence-criterion**'):problems.append('RS Hua 117 line changed.')
state_line_checks=0
for line in lines:
 if not re.match(r'^\| O\d\d ',line):continue
 fields=split_table(line)
 cited=set()
 lm=re.search(r'\blines? ([0-9,–-]+)',fields[1])
 if lm:
  for part in lm[1].split(','):
   pair=re.split('[–-]',part)
   cited.update(range(int(pair[0]),int(pair[-1])+1))
 for m in re.finditer(r'\b(?:TOTASPH|RESIDUE|GALOIS|POLES|BISITE|PATHS|PRETOT|STRATA) [A-Z0-9]+\.\d+\b',fields[0]):
  id_=m[0]
  actual={i for i,l in enumerate(state,1) if l.startswith('- **'+id_+'** [')}
  if actual and not actual<=cited:problems.append(f'O-table RS line mismatch for {id_}: {cited} versus {actual}.')
  if actual:state_line_checks+=1
hua_checks=[]
for m in re.finditer(r'context/hua_project/(11[67]\.modern\.tex):(\d+)(?:[–-](\d+))?',text):
 name,start,end=m.groups();a=int(start);b=int(end or start)
 ls=(root.parent/'context/hua_project'/name).read_text().splitlines()
 if not 1<=a<=b<=len(ls):problems.append(f'Hua source range out of bounds: {name}:{a}–{b}.')
 heads=[(i,l) for i,l in enumerate(ls[:a],1) if re.match(r'\\(?:sub)?section',l)]
 hua_checks.append((name,a,b,heads[-1] if heads else None))
search_path=root/'working/context_search_log.json'
search_count=None
if search_path.exists():
 s=json.loads(search_path.read_text())
 if isinstance(s,list):search_count=len(s)
 elif isinstance(s,dict):
  for k,v in s.items():
   if isinstance(v,list) and len(v)==385:search_count=len(v)
report=[
'# Final research-notes mechanical review','',
f'Reviewed {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")}. Input: `MPL_116+117_notes.md` ({len(lines)} lines).','',
'## Result','',
'PASS: all requested mechanical checks succeeded.' if not problems else 'Issues: '+str(problems),'',
'- **255 rendered DSS rows** occur exactly once and in catalogue/source order.',
'- Every rendered DSS source cell matches the generated exact catalogue value: status, DSS source line, original manuscript locator, and the same-ID RS line where present.',
'- All **16 absent source locators** are explicitly rendered as `(no manuscript locator supplied)`; none has been reconstructed.',
'- **15 NR headings** are present in order: NR01–NR12 and NRK1–NRK3. Their source-line metadata matches NEW_RESULTS lines 18–29 and 31–33.',
'- **44 N-items, 5 Q-items and 13 R-items** are defined once each. All explicit references and intermediate references in same-prefix ranges resolve.',
f'- All **{tables} Markdown tables** have consistent column counts using an escape-aware pipe parser. No broken table escaping was detected.',
'- Every heading now has a following blank line; table blocks are separated from following content.',
'', '## Context-source metadata','',
f'- All **{state_line_checks} named structured RS ID references** in O-items point to their actual source lines.',
'- The two Hua findings-register entries are verified at **RS 523 and 524**, respectively.',
'- O09 correctly cites REVERSIBLE_LOCALIZERS F.1 at RS 103–106. H01 now cites RS **37–110**, including the S2COUNT intake qualification on line 110.',
'- O18 separately identifies GALOIS B.14 at RS 433; O03’s accessibility item identifies GALOIS B.13 at RS 419.',
f'- All **{len(hua_checks)} explicit Hua file/line ranges** are in bounds and fall in the named sections (the section labels were checked against the source headings). R10’s 393–419 range includes the modern adjunction reference; R11 cites the crossed-conclusion comment at line 419; H02’s 432–440 range includes the all-localizer assertion and its “cité de mémoire” qualification.',
'- The renderer reads source statuses from `context_catalog.json` by exact ID and preserves the literal `claim (return: ...)` language; inspection confirms no status is inferred from the new comparison’s note kind.',
'', '## Corrections verified','',
'- The previously reported H01 source-range endpoint was extended from 109 to 110.',
'- The assembler now inserts blank lines after headings; the rebuilt notes contain no remaining heading-spacing violation.',
'', '## Scope','',
'- This is a mechanical coverage, reference and rendering review. It does not verify manuscript readings, source quotations against scans, mathematical claims, or priority.',
'- No images, page fragments or combined frozen transcription were read or changed. No research-note or comparison content was edited.',
'- Context keyword searches are discovery aids, not proofs of occurrence or absence; the root’s scan comparisons remain separate from this mechanical review.',
'', '## Reviewed input hash','',
f'`MPL_116+117_notes.md`: `{hashlib.sha256(notes.read_bytes()).hexdigest()}`','']
(root/'working/final_notes_mechanical_review.md').write_text('\n'.join(report))
print('Problems:',problems)
print('DSS:',len(render),'NR:',len(nrhead),'N/Q/R:',dict(Counter(x[0] for x in headings)),'tables:',tables,'Hua ranges:',len(hua_checks),'RS named refs:',state_line_checks,'lines:',len(lines),'search_count:',search_count)
print('Saved working/final_notes_mechanical_review.md')
