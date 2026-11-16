#!/usr/bin/env python3
"""Read-only checks on frozen files; writes only final validation research records."""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json
import re
import sys

BASE = Path(__file__).resolve().parents[1]
STAMP = sys.argv[1] if len(sys.argv) > 1 else 'UTC time not supplied'
report = {'checked_utc': STAMP, 'checks': {}}

def check(name, condition, detail=None):
    report['checks'][name] = {'passed': bool(condition), 'detail': detail}
    if not condition:
        raise AssertionError(f'{name}: {detail}')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def table_escape(value):
    # Preserve literal existing backslashes before a pipe when GFM unescapes it.
    return re.sub(r'(\\*)\|', lambda m: '\\'*(2*len(m[1])+1)+'|', value)

expected = [(106,n) for n in range(2,18)] + [(107,n) for n in range(2,27)]
page_names = [f'MPL_106+107_{c}_scan{n:03}.tex' for c,n in expected]
pages = sorted((BASE/'pages').glob('*.tex'))
check('page_files_and_order', [p.name for p in pages] == page_names, len(pages))
for p,(c,n) in zip(pages,expected):
    text = p.read_text()
    prefix = (f'\\cotefile{{{c}}}\n' if n==2 else '') + f'\\scanpage{{{n}}}\n'
    check(f'page_marker_{c}_{n:03}', text.startswith(prefix))

frozen = json.loads((BASE/'records/frozen_sha256.json').read_text())
current = {rel:sha(BASE/rel) for rel in frozen}
check('all_42_frozen_hashes_unchanged', len(frozen)==42 and current==frozen,
      {'files':len(frozen), 'combined_sha256':current.get('MPL_106+107_transcription.tex')})
combined = (BASE/'MPL_106+107_transcription.tex').read_text()
check('combined_exactly_matches_ordered_pages', combined=='\n'.join(p.read_text() for p in pages))
check('combined_is_fragment', combined.startswith('\\cotefile{106}\n\\scanpage{2}\n') and '\\documentclass' not in combined)

with (BASE/'MPL_106+107_inventory.csv').open(newline='') as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    rows = list(reader)
check('inventory_eight_columns', fields==['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'], fields)
check('inventory_1202_all_yes', len(rows)==1202 and all(r['transcribed']=='yes' for r in rows),len(rows))
check('inventory_all_pages', set((int(r['cote']),int(r['scan'])) for r in rows)==set(expected))
check('inventory_allowed_sheet_kinds', set(r['sheet_kind'] for r in rows)<= {'text','reused_typed','cancelled_draft','cover'})
check('inventory_allowed_element_kinds', set(r['kind'] for r in rows)<= {'text','display','diagram','drawing','margin note','insertion','deletion'})
check('inventory_unique_element_ids', len({(r['cote'],r['scan'],r['element']) for r in rows})==len(rows))
report['inventory_counts'] = {'sheet_kinds':dict(Counter(r['sheet_kind'] for r in rows)), 'element_kinds':dict(Counter(r['kind'] for r in rows))}

doubts = [json.loads(line) for line in (BASE/'records/doubts.jsonl').read_text().splitlines()]
check('doubts_342', len(doubts)==342,len(doubts))
check('all_doubt_macros_indexed', len(re.findall(r'\\(?:unsure|illegible)\{',combined))==len(doubts))
doubt_md = (BASE/'MPL_106+107_doubts.md').read_text()
check('doubts_markdown_342_rows', len(re.findall(r'^\| 10[67] \| \d{3} \| TeX ',doubt_md,re.M))==342)
check('notation_precedes_doubts', doubt_md.index('## Package notation table') < doubt_md.index('## Reading doubts'))

progress = (BASE/'progress.log').read_text()
for label in ('done','audited'):
    marked = [(int(c),int(n)) for c,n in re.findall(r'^(106|107) scan (\d{3}) '+label+r' ',progress,re.M)]
    check('progress_'+label+'_all_41', marked==expected, len(marked))
check('freeze_precedes_context_open', progress.index('transcription frozen') < progress.index('context opened'))

notes = (BASE/'MPL_106+107_notes.md').read_text()
ids = ([f'C106-{n:02}' for n in range(1,21)]+[f'RQ-{n:02}' for n in range(1,15)]+
       [f'O{n}' for n in range(1,5)]+[f'R{n}' for n in range(1,12)]+
       [f'H{n:02}' for n in range(1,14)]+[f'SP-L{n:02}' for n in range(1,8)])
for ident in ids:
    count = len(re.findall(r'^#{3,6} '+re.escape(ident)+r' — ',notes,re.M))
    check('note_'+ident, count==1,count)
check('R106_V1_present', len(re.findall(r'^#{3,6} Own-idea verification note R106-V1$',notes,re.M))==1)
check('standing_questions_present', '## C. Standing question:' in notes and '## D. Standing question:' in notes)

sp = json.loads((BASE/'records/research_strata_paths.json').read_text())['mappings']
br = json.loads((BASE/'records/research_bisite_residue.json').read_text())['rows']
all_ids = [r['id'] for r in sp+br]
check('dossier_255_unique_ids', len(all_ids)==255 and len(set(all_ids))==255)
check('dossier_all_255_rows_in_main_notes', all(re.search(r'^\| (?:\*\*)?'+re.escape(ident)+r'(?:\*\*| —| \|)',notes,re.M) for ident in all_ids))
check('dossier_family_counts', Counter(i.split()[0] for i in all_ids)=={'STRATA':10,'PATHS':76,'BISITE':113,'RESIDUE':56})
for row in sp:
    check('statement_preserved_'+row['id'], table_escape(row['supplied_statement']) in notes)
for row in br:
    check('statement_preserved_'+row['id'], table_escape(row['supplied_statement_exact']) in notes)

new = json.loads((BASE/'records/research_new_and_homotopy_mapping.json').read_text())
check('new_12_plus_3', len(new['numbered_results'])==12 and len(new['known_notices'])==3 and len(new['mapping'])==15)
for row in new['numbered_results']:
    check('new_statement_preserved_'+row['id'], row['result'].replace('|',r'\|') in notes)

table_errors = []
width = None
for n,line in enumerate(notes.splitlines(),1):
    if line.startswith('|'):
        cols = len(re.split(r'(?<!\\)\|',line))-2
        if width is None: width = cols
        elif cols!=width: table_errors.append([n,cols,width])
    else: width = None
check('notes_markdown_table_columns', not table_errors, table_errors)
clean = re.sub(r'```[\s\S]*?```','',notes)
clean = re.sub(r'`[^`\n]*`','',clean)
stack=[];math_errors=[]
for m in re.finditer(r'(?<!\\)\\[()\[\]]',clean):
    token=m[0]
    if token in (r'\(',r'\['):
        if stack: math_errors.append(['nested',token])
        stack.append(token)
    else:
        wanted=r'\(' if token==r'\)' else r'\['
        if not stack or stack[-1]!=wanted: math_errors.append(['mismatched',token])
        else:stack.pop()
check('notes_explicit_math_delimiters', not math_errors and not stack,math_errors+stack)
check('notes_no_ephemeral_web_refs', not re.search(r'\bturn\d+(?:view|search)\d+\b',notes))
check('no_known_bad_context_filename', 'DER_V-b.tex' not in notes)

report['structural_validation_at_freeze'] = json.loads((BASE/'records/structural_validation.json').read_text())
report['full_latex_compilation'] = 'Unavailable: missing format and packages; no successful compile claimed.'
report['notes_bytes'] = len(notes.encode())
report['notes_word_count_whitespace'] = len(notes.split())
report['passed'] = all(v['passed'] for v in report['checks'].values())
(BASE/'records/final_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'passed':report['passed'],'checks':len(report['checks']),'pages':len(pages),'inventory_rows':len(rows),'doubts':len(doubts),'dossier_statements':len(all_ids),'notes_bytes':report['notes_bytes'],'frozen_hashes_unchanged':True},ensure_ascii=False))
