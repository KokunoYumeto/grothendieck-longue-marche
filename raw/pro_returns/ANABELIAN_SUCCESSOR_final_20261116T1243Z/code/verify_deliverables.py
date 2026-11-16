"""Check the assembled register, bibliography, report and LuaLaTeX output.

This is a document/reproducibility check, not a mathematical proof checker.
It also refreshes the index of retained program sources and nearby outputs.
"""
import argparse
import ast
import csv
import json
import re
from pathlib import Path

import fitz

W = Path(__file__).resolve().parents[1]
ap = argparse.ArgumentParser()
ap.add_argument('--name', default='current')
ap.add_argument('--render', default='')
args = ap.parse_args()

with (W/'ANABELIAN_SUCCESSOR_results.csv').open(newline='') as f:
    raw = list(csv.reader(f))
with (W/'ANABELIAN_SUCCESSOR_results.csv').open(newline='') as f:
    rows = list(csv.DictReader(f))
tex = (W/'ANABELIAN_SUCCESSOR_paper.tex').read_text()
log = (W/'ANABELIAN_SUCCESSOR_paper.log').read_text(errors='replace')
bib = (W/'ANABELIAN_SUCCESSOR_references.bib').read_text()
report = (W/'ANABELIAN_SUCCESSOR_report.md').read_text()
entries = re.split(r'(?m)(?=^@\w+\s*\{)', bib)[1:]
keys = [re.match(r'@\w+\s*\{([^,]+)', x).group(1) for x in entries]
claims = re.findall(r'\\begin\{claim\}\{([^}]+)\}', tex)
pdf = fitz.open(W/'ANABELIAN_SUCCESSOR_paper.pdf')
result = {
    'scope': 'Document and reproducibility checks only; mathematical audits are separate.',
    'pdf_pages': len(pdf),
    'pdf_metadata': pdf.metadata,
    'claims': len(claims),
    'register_rows': len(rows),
    'part_counts': {a: sum(x.startswith(a+'.') for x in claims) for a in ['A', 'F']},
    'column_counts': sorted(set(map(len, raw))),
    'duplicate_claims': sorted({x for x in claims if claims.count(x)>1}),
    'register_matches_claim_order': [x['id'] for x in rows] == claims,
    'unmapped': [x['id'] for x in rows if not x['answers (item or lead)']],
    'statuses': sorted(set(x['status'] for x in rows)),
    'bibliography_entries': len(entries),
    'duplicate_bibliography_keys': sorted({x for x in keys if keys.count(x)>1}),
    'bibliography_entries_without_verification_marker': [k for k,e in zip(keys,entries) if not re.search(r'\b(?:unverified|verified)\b',e,re.I)],
    'outcome_rows': re.findall(r'^\| ((?:A|F)\d+|L\d+) \|',report,re.M),
    'report_starts_incomplete': report.startswith('INCOMPLETE\n'),
    'overfull': re.findall(r'Overfull[^\n]*',log),
    'latex_warnings': re.findall(r'LaTeX Warning:[^\n]*',log),
    'package_warnings': re.findall(r'Package [^\n]* Warning:[^\n]*',log),
    'undefined_or_duplicate_references': re.findall(r'[^\n]*(?:undefined|multiply defined)[^\n]*',log),
}
assert result['column_counts']==[9]
assert result['register_matches_claim_order']
assert len(result['outcome_rows'])==28
assert not result['duplicate_claims'] and not result['unmapped']
assert not result['duplicate_bibliography_keys']
assert not result['bibliography_entries_without_verification_marker']
assert not result['undefined_or_duplicate_references']
assert not result['latex_warnings']
assert not result['package_warnings']
for line in result['overfull']:
    width = re.search(r'\(([0-9.]+)pt too wide\)',line)
    assert width and float(width.group(1))<=2, line

rendered=[]
if args.render:
    dest=W/'qa'/f'{args.name}_render';dest.mkdir(exist_ok=True)
    for page in sorted(set(int(x) for x in args.render.split(','))):
        assert 1<=page<=len(pdf)
        pdf[page-1].get_pixmap(matrix=fitz.Matrix(1.2,1.2)).save(dest/f'page_{page:03}.png')
        rendered.append(page)
    record={'pdf_pages':len(pdf),'rendered_pages':rendered,'visually_inspected_pages':[],
            'note':'Rendering alone is not visual inspection. Update only after actually viewing images.'}
    (W/'qa'/f'{args.name}_render_record.json').write_text(json.dumps(record,indent=2)+'\n')

programs=[]
for path in sorted(W.rglob('*')):
    if not path.is_file() or path.suffix not in {'.py','.cpp','.c','.sh'}:
        continue
    if ('__pycache__' in path.parts or 'retained_agent_code' in path.parts
            or 'native' in path.relative_to(W).parts):
        continue
    purpose='See source and owner audit for exact inputs and output routing.'
    if path.suffix=='.py':
        try:
            doc=ast.get_docstring(ast.parse(path.read_text()))
            if doc: purpose=doc.split('\n')[0]
        except (SyntaxError,UnicodeError):
            pass
    outputs=[str(q.relative_to(W)) for q in sorted(path.parent.glob(path.stem+'*'))
             if q.is_file() and q!=path and q.suffix not in {'.py','.cpp','.c','.sh','.tex','.md'}]
    programs.append([str(path.relative_to(W)),json.dumps(outputs),purpose])
with (W/'code/PROGRAM_INDEX.csv').open('w',newline='') as f:
    writer=csv.writer(f);writer.writerow(['program','nearby_named_outputs','purpose']);writer.writerows(programs)
result['retained_program_sources']=len(programs)
result['rendered_pages']=rendered
(W/'qa'/f'{args.name}_build_check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
