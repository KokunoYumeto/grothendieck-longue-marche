"""Integrate nine completely reviewed sources, retaining all preceding bytes."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import hashlib
import io
import json
import shutil
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
review = json.loads((root/'records/checkpoint30_root_formal_reviews.json').read_text())
assert review['status'] == 'PASS_COMPLETE_SOURCE_REVIEW'
copies = review['copies']
assert [r['statement'] for r in copies] == ['A.89','A.90','A.91','B.142','B.143','B.144','B.145','B.146','B.147']
for row in copies:
    assert hashlib.sha256((root/row['source']).read_bytes()).hexdigest() == row['sha256']
    assert not (root/row['target']).exists()

paper = (root/'LM4_SUCCESSOR_paper.tex').read_text()
anchor = '\\input{sections/a_alexander_dihedral_coefficient.tex}'
assert paper.count(anchor) == 1
paper = paper.replace(anchor, anchor+'\n'+'\n'.join('\\input{'+r['target']+'}' for r in copies if r['statement'].startswith('A.')))
anchor = 'dihedral quotient proves equality modulo eight.'
assert paper.count(anchor) == 1
paper = paper.replace(anchor, anchor+''' The actual hexagon class gives
the full weighted coefficient identity. Under the additional full-GT
hypothesis, the prescribed pro-two hexagon proves the entire dyadic
comparison; the remaining scalar condition is exactly all odd cyclic
heads. The actual cube reversal acts as minus the identity on the
integral cyclic-cover module. Its complete three-cover covariance
therefore supplies no additional single-cover linear equation.''')
anchor = 'collapse and filling survival are not inferred.'
assert paper.count(anchor) == 1
paper = paper.replace(anchor, anchor+''' Eight unrestricted first-order
equations exclude every coarse section, ordinarily and after full
completion. The actual extension class has infinite integral order and
is nonzero at every odd coefficient prime. An explicit cochain argument
excludes sections over every finite-index or open subgroup, for both
the coarse and one-family fillings. Those particular classes restrict
to zero on the actual fixed source, whose entire stabilizer gives an
exact ordinary coset-basis and centralizer-extension presentation.
The full cyclic square and leaf filling has a proper internal carrier
amalgam, with its extra ambient kernel retained. The complete family
link proves that the prescribed center-basis change admits no injective
extension to the ordinary regional kernel, even with arbitrary family
images. Noninjective extensions exist; no filling collapse follows.''')
part_b = (root/'sections/part_B.tex').read_text()
for row in copies:
    if row['statement'].startswith('B.'):
        line = '\\input{'+row['target']+'}'
        assert line not in part_b
        part_b += line+'\n'

with (root/'task_coverage.csv').open(newline='') as stream:
    reader=csv.DictReader(stream);fields=reader.fieldnames;tasks=list(reader)
assert len(tasks) == 49
old_outcomes = [(r['task'],r['outcome']) for r in tasks]
for row in tasks:
    if row['task'] in {'A.7','A.8'}:
        for sid in ('A.89','A.90','A.91'):
            assert sid not in row['statement_ids'].split(';')
            row['statement_ids'] += ';'+sid
        row['state'] += ' A89 formalizes the actual full hexagon-class identity and full-GT dyadic equality. A90 identifies the exact remaining all-odd-head criterion. A91 proves that the actual integral and three-cover dihedral covariance imposes no extra single-cover linear condition, while retaining the common-word and pentagon gates.'
        row['approaches'] += ' Entire ordered Alexander substitutions; prescribed pro-two hexagon; odd-head norm-line argument; integral action on all conjugate generators and complete three-cover S3 covariance.'
        row['obstruction'] += ' Common-word and full pentagon compatibility have not supplied the all-odd-head condition. The covariance identity is tautological on the actual single-cover abelianization; this does not settle the nonlinear word.'
    if row['task'] in {'B.4','B.4.a','B.4.b','B.4.c','B.4.h'}:
        for sid in ('B.142','B.143','B.144','B.145','B.146','B.147'):
            assert sid not in row['statement_ids'].split(';')
            row['statement_ids'] += ';'+sid
        row['state'] += ' B142 proves unrestricted coarse nonsplitting and actual infinite-order/odd-prime extension classes. B143 proves both virtual nonsplitting theorems and the exact zero pullback of these classes to the actual fixed source. B144 gives its complete L=H intersection S presentation. B145/B146 give the whole cyclic normalization and internally proper full leaf carrier. B147 excludes every injective extension of the prescribed center change, even with arbitrary family mixing, by the entire triple link.'
        row['approaches'] += ' All fourteen arbitrary lift variables and eight exact equations; actual characteristic finite-kernel refinement; coefficient-weighted cochain averaging; complete coset retraction; all-integer leaf recurrence; full free-product family stabilizers and centralizing-HNN normal form.'
        row['obstruction'] += ' The first-jet classes vanish on the actual fixed-source restriction, which is not finite index/open. The complete stabilizer and marked commutation test remain unresolved. The specified center automorphism cannot be extended injectively to the regional graph group; rewritten relations are essential. The cyclic carrier restriction and actual icosahedral uniform finite-cover condition remain Open.'
        row['next_step'] = 'Resolve the entire fixed stabilizer or its marked commutation condition, and compare complete one-sided and mirror filling kernels. Keep B75 actual icosahedral uniform characteristic finite-cover separation as the direct main target, without substituting an intermediate carrier or a pro-p shadow.'
assert [(r['task'],r['outcome']) for r in tasks] == old_outcomes
assert next(r for r in tasks if r['task']=='A.8')['outcome']=='Open'
assert next(r for r in tasks if r['task']=='B.4')['outcome']=='Open'

report = (root/'LM4_SUCCESSOR_report.md').read_text()
assert report.splitlines()[0] == 'INCOMPLETE'
lines = report.splitlines(True)
start = next(i for i,line in enumerate(lines) if line.startswith('| Task or lead |'))
end=start
while end<len(lines) and lines[end].startswith('|'):end+=1
cell=lambda v:v.replace('|','\\|').replace('\n',' ')
table=['| Task or lead | Statements | Outcome and exact state |\n','|---|---|---|\n']
table += ['| '+cell(r['task'])+' | '+cell(r['statement_ids'])+' | **'+cell(r['outcome'])+'** — '+cell(r['state'])+' |\n' for r in tasks]
lines[start:end]=table
report=''.join(lines)+'\n\n'+(root/'records/thirtieth_hour_research_report.md').read_text()

backup=root/'records/pdf_qa/checkpoint30_before_integration'
assert not backup.exists()
paths=['LM4_SUCCESSOR_paper.'+suffix for suffix in ('pdf','tex','log','aux','bbl','blg','toc','out')]
paths += ['LM4_SUCCESSOR_results.csv','LM4_SUCCESSOR_references.bib','LM4_SUCCESSOR_report.md','task_coverage.csv','sections/part_B.tex','sections/b_sources.bib','code/assemble_register.py']
paths += [str(p.relative_to(root)) for p in (root/'records').glob('build_*.log')]
for rel in paths:
    src=root/rel
    if not src.is_file():continue
    suffix='.retained.txt' if src.suffix in {'.aux','.bbl','.blg','.toc'} else ''
    dest=backup/(rel+suffix);dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(src,dest)
for row in copies:
    (root/row['target']).write_bytes((root/row['source']).read_bytes())
(root/'LM4_SUCCESSOR_paper.tex').write_text(paper)
(root/'sections/part_B.tex').write_text(part_b)
(root/'LM4_SUCCESSOR_report.md').write_text(report)
with (root/'task_coverage.csv').open('w',newline='') as stream:
    writer=csv.DictWriter(stream,fieldnames=fields);writer.writeheader();writer.writerows(tasks)
(root/'records/checkpoint30_formal_source_copies.json').write_text(json.dumps({'integrated_at':datetime.now(timezone.utc).isoformat(),'copies':copies,'comparison':'Every integrated source is byte-identical to its final fully reviewed owned source.'},indent=2)+'\n')
subprocess.run([sys.executable,str(root/'code/assemble_register.py')],check=True)
rows=list(csv.DictReader((root/'LM4_SUCCESSOR_results.csv').open()))
assert len(rows)==323
assert dict(Counter(r['status'] for r in rows))=={'Known':6,'Proved':279,'Refuted':19,'Open':19}
assert (root/'LM4_SUCCESSOR_references.bib').read_bytes()==(backup/'LM4_SUCCESSOR_references.bib').read_bytes()
print('Integrated nine unchanged final sources:323 statements,279 Proved,114 references,49 tasks;both main decisions Open.')
