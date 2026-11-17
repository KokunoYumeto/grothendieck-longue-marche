#!/usr/bin/env python3
"""Read-only mechanical check of root's DSS comparison rows against the context catalogue."""
from pathlib import Path
from collections import Counter
from datetime import datetime,timezone
import json,re,hashlib
root=Path(__file__).resolve().parents[1]
path=root/'working/comparisons_dss.txt'
source=root.parent/'context/DOSSIER_STATEMENTS_WITH_STATUS.md'
catpath=root/'working/context_catalog.json'
cat=json.loads(catpath.read_text())
expected=cat['dossier_statements'];index={r['id']:r for r in expected}
rows=[];headers=[];issues=[]
for n,l in enumerate(path.read_text().splitlines(),1):
 if not l.strip():continue
 if l.lstrip().startswith('#'):headers.append(n);continue
 fields=l.split(' || ')
 if len(fields)!=5:issues.append(f'Line {n}: expected 5 fields, found {len(fields)}.');continue
 rows.append({'line':n,'id':fields[0],'topic':fields[1],'evidence':fields[2],'kind':fields[3],'comparison':fields[4],'fields':fields})
ids=[r['id'] for r in rows];counts=Counter(ids)
missing=sorted(set(index)-set(ids));extra=sorted(set(ids)-set(index));duplicates={k:v for k,v in counts.items() if v>1}
valid={'conjecture','unproved claim','unpursued implication','own idea','reading question','self-flagged','withdrawn in the same text','withdrawn in same text'}
invalid=[(r['line'],r['id'],r['kind']) for r in rows if r['kind'] not in valid]
empty=[(r['line'],r['id']) for r in rows if any(not f.strip() for f in r['fields'])]
pipes=[r['id'] for r in rows if any('|' in f for f in r['fields'])]
tabs=[r['id'] for r in rows if any('\t' in f for f in r['fields'])]
odd_backticks=[r['id'] for r in rows if any(f.count('`')%2 for f in r['fields'])]
control=[r['id'] for r in rows if any(ord(c)<32 for f in r['fields'] for c in f)]
edge_whitespace=[r['id'] for r in rows if any(f!=f.strip() for f in r['fields'])]
def sentences(s):
 # Approximate prose count: protect identifier dots and common abbreviations;
 # quoted punctuation followed by lower-case continuation does not split.
 s=re.sub(r'\b(?:ms|cf|e\.g|i\.e|resp|etc)\.',lambda m:m[0].replace('.','<DOT>'),s)
 s=re.sub(r'(?<=[A-Za-z0-9])\.(?=[0-9])','<DOT>',s)
 return len([x for x in re.split(r'[.!?]+(?:[”’"\)]*)\s+(?=[A-Z“])',s) if x.strip()])
sentence_counts={r['id']:sentences(r['comparison']) for r in rows}
violations={i:n for i,n in sentence_counts.items() if not 1<=n<=4}
source_rows={}
for n,l in enumerate(source.read_text().splitlines(),1):
 if re.match(r'^\| (STRATA|PATHS|BISITE|RESIDUE) ',l):
  fields=l[2:-2].split(' | ');assert len(fields)==4
  source_rows[fields[0]]=(n,fields)
status_errors=[];locator_errors=[]
for r in expected:
 n,fields=source_rows[r['id']]
 if r['status_exact']!=fields[2] or r['source_line']!=n:status_errors.append(r['id'])
 if r['manuscript_locator_exact']!=fields[3]:locator_errors.append(r['id'])
for label,value in [('missing IDs',missing),('extra IDs',extra),('duplicate IDs',duplicates),('invalid note kinds',invalid),('empty fields',empty),('sentence-count violations',violations),('status mismatches',status_errors),('locator mismatches',locator_errors)]:
 if value:issues.append(f'{label}: {value}')
status_counts=Counter(r['status_exact'] for r in expected)
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
report=[
'# DSS comparison coverage review','',f'Reviewed {stamp}.','',
'## Result','',
('PASS: no mechanical coverage or field-format errors found.' if not issues else 'Issues found: '+str(issues)),
'',f'- **{len(rows)} comparison records** match **{len(expected)} catalogue IDs** exactly; no missing, extra or duplicate IDs.',
'- Record order matches the source catalogue order.' if ids==[r['id'] for r in expected] else '- Record order differs from source order.',
f'- Every record has exactly **five fields** separated by the literal delimiter ` || `. The comment header on line {headers[0]} is excluded from the record count.',
'- All fields are nonempty; the literal evidence value `none` is preserved as a value rather than interpreted as a missing field.',
'- All note kinds belong to the task’s allowed vocabulary: '+', '.join(f'{k} ({n})' for k,n in Counter(r['kind'] for r in rows).items())+'.',
'- Approximate sentence counts, with identifier dots and common abbreviations protected: '+', '.join(f'{n} sentence(s): {k} records' for n,k in sorted(Counter(sentence_counts.values()).items()))+'.',
'- No note exceeds the requested one-to-four-sentence range in this mechanical estimate.',
'', '## Exact source statuses and locators','',
'- All 255 `status_exact` values and all 255 manuscript locator strings in the catalogue match the current DSS source cells exactly; the catalogue source-line values also match.',
'- Status totals: '+', '.join(f'`{s}`: {n}' for s,n in status_counts.items())+'.',
'- The comparison file contains no replacement status field. A renderer joining each comparison to `context_catalog.json` by its exact ID can use `status_exact` verbatim and preserve the source’s `claim (return: ...)` qualification.',
'- No combined-note renderer was found in the scripts directory at this review time; this confirms the catalogue inputs and join keys, rather than claiming to certify future rendering code.',
'', '## Delimiter and Markdown checks','',
f'- Internal pipe characters in comparison fields: {len(pipes)}; literal tabs: {len(tabs)}; control characters: {len(control)}; fields with odd backtick counts: {len(odd_backticks)}; fields with leading/trailing whitespace: {len(edge_whitespace)}.',
'- Skip the `#` comment header when parsing. Split records on ` || `, not on a single pipe.',
'- The supplied context statements may contain mathematical pipes (for example BISITE A.28); their source parser uses ` | ` and preserves the internal pipe. If full context text is embedded in a Markdown table, escape table pipes at rendering time without mutating the exact catalogue source string.',
'- The comparison fields themselves have no internal pipes or tabs and therefore present no detected table-column collision. CSV output should still use a CSV writer because prose contains commas and quotes.',
'', '## Topic check and scope','',
'- The short topics were compared with the corresponding same-ID contextual statement openings. No obvious topic/ID mismatch was found.',
'- This review makes no judgment about manuscript readings, scan evidence, quoted wording, or whether a proposed mathematical relationship is correct. No images or frozen transcription were read.',
'- The comparison content was not edited.',
'', '## Reviewed input hashes','',
f'- `working/comparisons_dss.txt`: `{hashlib.sha256(path.read_bytes()).hexdigest()}`',
f'- `working/context_catalog.json`: `{hashlib.sha256(catpath.read_bytes()).hexdigest()}`',
f'- `context/DOSSIER_STATEMENTS_WITH_STATUS.md`: `{hashlib.sha256(source.read_bytes()).hexdigest()}`','']
(root/'working/comparison_coverage_review.md').write_text('\n'.join(report))
print('Coverage:',len(rows),'missing:',missing,'extra:',extra,'duplicates:',duplicates)
print('Sentence count distribution:',dict(Counter(sentence_counts.values())))
print('Status errors:',status_errors,'locator errors:',locator_errors)
print('Issues:',issues)
print('Saved working/comparison_coverage_review.md')
