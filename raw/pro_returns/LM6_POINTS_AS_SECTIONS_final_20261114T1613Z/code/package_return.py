#!/usr/bin/env python3
"""Create an immutable, fully inventoried checkpoint or final return ZIP."""
from pathlib import Path
import argparse,csv,hashlib,io,json,zipfile

p=argparse.ArgumentParser();p.add_argument('--checkpoint');p.add_argument('--final',action='store_true')
a=p.parse_args();assert bool(a.checkpoint)!=bool(a.final)
R=Path(__file__).resolve().parents[1];out=R/'deliverable';ID='LM6_POINTS_AS_SECTIONS'
required=[f'{ID}_paper.tex',f'{ID}_paper.pdf',f'{ID}_results.csv',
          f'{ID}_readings.csv',f'{ID}_references.bib',f'{ID}_report.md']
for name in required:assert (out/name).is_file(),name
check=json.loads((out/'typesetting_check.json').read_text())
assert check['overfull_over_2pt']==0 and not check['missing_characters']
assert not check['undefined_references_or_citations']
qa=json.loads((R/'visual_qa.json').read_text())
assert qa['pdf_sha256']==hashlib.sha256((out/f'{ID}_paper.pdf').read_bytes()).hexdigest()
assert set(qa['rendered_pages'])<=set(qa['visually_inspected_pages'])
assert qa['status']=='passed'
rows=list(csv.DictReader((out/f'{ID}_results.csv').open()))
assert len(rows)==len({r['id'] for r in rows})
index=json.loads((R/'statement_index.json').read_text())
assert [r['id'] for r in rows]==[r['id'] for r in index]
assert all(r['status'] in ['Proved','Refuted','Known','Open'] for r in rows)
assert (out/f'{ID}_report.md').read_text().startswith('INCOMPLETE\n')

members={name:out/name for name in required}
for f in (R/'code').rglob('*'):
    if f.is_file() and '__pycache__' not in f.parts:
        members['code/'+str(f.relative_to(R/'code'))]=f
section_source=R/'assembly_snapshot/sections'
if not section_source.exists():section_source=R/'sections'
for f in section_source.glob('*.tex'):members['research/sections/'+f.name]=f
for pattern in ['*_refs.bib','*_references.bib','*_results.json','*_results_add.json',
                '*_readings.json','*_audit.md','*_audit_*.md','*_live_notes.md','*_coverage.md','*_coverage.json']:
    for f in R.glob(pattern):members['research/'+f.name]=f
for name in ['Root_report.md','coverage.json','manuscript_concordance.json',
             'statement_index.json','register_build_output.json','state.json']:
    f=R/name
    if f.exists():members['research/'+name]=f
for f in R.glob('package_checkpoint_*_output.json'):
    members['research/checkpoints/'+f.name]=f
if a.final:
    for f in sorted(R.parent.glob(f'{ID}_checkpoint_*.zip')):
        members['checkpoints/'+f.name]=f
for name in ['typesetting_check.json',f'{ID}_paper.log',f'{ID}_paper.aux',
             f'{ID}_paper.blg','build_pass1.txt','build_pass2.txt',
             'build_pass3.txt','bibtex_output.txt']:
    f=out/name
    if f.exists():members['verification/'+name]=f
members['verification/visual_qa.json']=R/'visual_qa.json'
for name in ['final_register_verification.json','render_output.json','final_visual_reuse.json']:
    f=R/name
    if f.exists():members['verification/'+name]=f
for q in qa['rendered_pages']:
    f=R/'rendered/current'/f'page{q:03d}.png'
    members['verification/rendered/'+f.name]=f
prompt=R.parent/'upload/PROMPT(20261114-105916).md'
if prompt.exists():members['research/request/PROMPT.md']=prompt

buf=io.StringIO();w=csv.writer(buf);w.writerow(['input_path','bytes','sha256'])
inputs=R.parent/'inputs'
for f in sorted(inputs.rglob('*')):
    if f.is_file():w.writerow([str(f.relative_to(R.parent)),f.stat().st_size,hashlib.sha256(f.read_bytes()).hexdigest()])
manifest=buf.getvalue().encode()
readme='''# Reproducing this research return

The six requested deliverables are at the ZIP root. The paper source is
self-contained; compile it with LuaLaTeX, then BibTeX, then LuaLaTeX twice.
The LaTeX packages are standard TeX Live packages listed in its preamble.

All executed mathematical programs and their actual outputs are in code/.
They use Python 3 with numpy and sympy where imported. Programs either
write their named outputs beside the source or print their result as JSON
on standard output; the corresponding captured output is retained in code/.
The document-rendering utility additionally uses pypdf and pdftoppm.

The modular writing state and exact input manifest are in research/.
To resume the assembly utilities, make a working directory, copy research/*
into it, place code/ beside sections/, and create deliverable/. Copy the
six root deliverables into that deliverable/ directory. The scripts
assemble.py, build_pdf.py and build_registers.py then use the same layout
as the executed working state. The supplied inputs are identified by the
manifest; they are not duplicated in this ZIP.

Finite computations certify only the finite claims stated in their outputs.
The infinite mathematical assertions are proved in the paper. A source
marked verified was opened; that flag does not certify all of its proofs.
This return is INCOMPLETE, as explained in the report and each Open row.
'''.encode()

suffix='final' if a.final else 'checkpoint_'+a.checkpoint
destination=R.parent/f'{ID}_{suffix}.zip'
assert not destination.exists(),'Refusing to overwrite an earlier package'
hashes=[]
with zipfile.ZipFile(destination,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=7) as z:
    for name,f in sorted(members.items()):
        data=f.read_bytes();z.writestr(name,data)
        hashes.append(f'{hashlib.sha256(data).hexdigest()}  {name}')
    for name,data in [('research/input_manifest.csv',manifest),('README.md',readme)]:
        z.writestr(name,data);hashes.append(f'{hashlib.sha256(data).hexdigest()}  {name}')
    z.writestr('SHA256SUMS.txt','\n'.join(hashes)+'\n')
result={'zip':str(destination),'bytes':destination.stat().st_size,
        'sha256':hashlib.sha256(destination.read_bytes()).hexdigest(),
        'members':len(hashes)+1,'numbered_statements':len(rows),
        'visual_and_typesetting_gates':'passed'}
(R/('package_'+suffix+'_output.json')).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
