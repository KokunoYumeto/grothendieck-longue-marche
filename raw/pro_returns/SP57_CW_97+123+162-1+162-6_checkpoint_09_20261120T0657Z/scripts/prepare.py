from pathlib import Path
import csv, re, json, shutil
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[2]
NAME='SP57_CW_97+123+162-1+162-6'
W=ROOT/'source'/f'{NAME}_witnesses'
OUT=ROOT/'out'
rows=list(csv.DictReader((W/'page_map.tsv').open(),delimiter='\t'))
for i,row in enumerate(rows,1):
    stem=Path(row['codex_file']).stem
    row.update(order=i,stem=stem)
    p=ROOT/'packets'/stem
    p.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(W/row['codex_file'],p/'C.tex')
    ht=(W/row['hua_file']).read_text()
    pat=r'(?m)^\\page\{'+row['their_page']+r'\}'
    m=re.search(pat,ht)
    assert m,stem
    rest=ht[m.start():]
    end=re.search(r'(?m)^\\page\{|\\end\{document\}',rest[m.end()-m.start():])
    if end: rest=rest[:m.end()-m.start()+end.start()]
    if stem=='C123-01_123_scan003':
        # H explicitly assigns this adjacent unnumbered heading to feuillet 3,
        # our scan 4, outside the selected package. See packet_boundary_notes.md.
        rest=rest.split('\\section*{Lissification des morphismes de Kostant}',1)[0]
    (p/'H.tex').write_text(rest)
    f=W/'codex'/row['folder']
    doubts=(f/(row['folder']+'_doubts.md')).read_text()
    n=row['our_scan']
    selected=[l for l in doubts.splitlines() if re.match(r'^\|\s*'+n+r'(?:\s*\||\s*,)',l)]
    notes=(f/(row['folder']+'_notes.md')).read_text()
    selected+=['\nPrior C notes (matching lines):']+[l for l in notes.splitlines() if re.search(r'\b[Ss]can(?:s)? '+n+r'\b',l) or re.match(r'^\|\s*'+n+r'\s*\|',l)]
    (p/'C_questions.md').write_text('\n'.join(selected)+'\n')
    (p/'meta.json').write_text(json.dumps(row,indent=2))
(OUT/'page_order.json').write_text(json.dumps(rows,indent=2))
shutil.copyfile(W/'codex/H97-01/PREAMBLE.tex',OUT/'PREAMBLE.tex')
source=(W/'codex/H97-01/PROMPT.md').read_text()
conventions=source[source.index('## Absolute rules'):source.index('## The attached draft')]
(OUT/'briefs/conventions.md').write_text(conventions)
if not (OUT/'briefs/notation.md').exists():
    (OUT/'briefs/notation.md').write_text('# Notation table in progress\n\nNo readings established before page 1. Check every glyph on its own ink.\n')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
if not (OUT/'progress.log').exists():
    (OUT/'progress.log').write_text(now+'\nRun: GPT-6 Astra Pro; effort setting not exposed. Main reader plus three fresh independent agents per page.\nSource archive extracted once; 26 pages in page_map.tsv order. No OCR or external research.\n')
    (OUT/'CHECK_EVENTS.tsv').write_text('statement_id\tdate\twho\ttype\toutcome\n')
    (OUT/f'{NAME}_changes.md').write_text('# Changes and decisions\n\nCounts will be computed from the decided page records.\n')
    (OUT/f'{NAME}_notes.md').write_text('# Notes while reading\n\nOnly the supplied pages are used. Reading and transcription alone are not mathematical verification.\n')
    (OUT/f'{NAME}_collation.tsv').write_text('folder\ttheir_page\tour_scan\tline\ttheir_reading\tcodex_reading\tfinal_reading\tscan_shows\tkind\tmarked_in_H\tconfidence\n')
    (OUT/f'{NAME}_inventory.csv').write_text('scan,sheet_kind,hand,element,kind,position,first_words_or_objects,transcribed\n')
    (OUT/f'{NAME}_doubts.md').write_text('# Notation and remaining doubts\n\nNo page decided yet.\n')
    (OUT/f'{NAME}_workflow.md').write_text('# Workflow record\n\nInitial brief: briefs/reader_v01.md. Each reader is a fresh agent with no inherited conversation and no access to other readers\' work. Pages are sequential in page_order.json.\n')
print('Prepared',len(rows),'isolated text packets; progress started',now)
