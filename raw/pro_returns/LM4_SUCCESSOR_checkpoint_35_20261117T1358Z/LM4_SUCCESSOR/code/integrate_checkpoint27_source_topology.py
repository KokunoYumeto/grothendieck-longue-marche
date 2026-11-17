"""Integrate only the four complete, frozen and independently reviewed sources."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import hashlib
import json
import shutil
import subprocess
import sys

root=Path(__file__).resolve().parents[1]
read=lambda p:json.loads((root/p).read_text())
review=read('records/checkpoint27_root_formal_reviews.json')
assert review['status']=='PASS_COMPLETE_SOURCE_REVIEW'
copies=review['copies']
assert [r['statement'] for r in copies]==['B.131','B.132','B.133','B.134']
for row in copies:
    source=root/row['source'];target=root/row['target']
    assert hashlib.sha256(source.read_bytes()).hexdigest()==row['sha256']
    assert not target.exists()

backup=root/'records/pdf_qa/checkpoint27_before_integration'
backup.mkdir(parents=True,exist_ok=False)
for rel in ('LM4_SUCCESSOR_paper.pdf','LM4_SUCCESSOR_paper.tex',
            'LM4_SUCCESSOR_paper.log','LM4_SUCCESSOR_paper.bbl',
            'LM4_SUCCESSOR_results.csv','LM4_SUCCESSOR_references.bib',
            'LM4_SUCCESSOR_report.md','task_coverage.csv',
            'sections/part_B.tex','sections/b_sources.bib'):
    dest=backup/(rel+'.retained.txt' if rel.endswith('.bbl') else rel)
    dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(root/rel,dest)

for row in copies:
    (root/row['target']).write_bytes((root/row['source']).read_bytes())
p=root/'sections/part_B.tex';s=p.read_text()
for row in copies:
    line='\\input{'+row['target']+'}'
    assert line not in s;s+=line+'\n'
p.write_text(s)
(root/'records/checkpoint27_formal_source_copies.json').write_text(json.dumps({
    'integrated_at':datetime.now(timezone.utc).isoformat(),
    'copies':copies,'comparison':'Every integrated component is byte-identical to its reviewed frozen source.'
},indent=2)+'\n')

p=root/'sections/b_sources.bib';s=p.read_text()
assert 'BLopesZalesskii2025' not in s
s+='''
@article{BLopesZalesskii2025,
  author = {Lopes, Lucas C. and Zalesskii, Pavel A.},
  title = {Prosoluble subgroups of the profinite completion of the fundamental group of compact 3-manifolds},
  journal = {Journal of the London Mathematical Society},
  volume = {112},
  number = {4},
  pages = {e70330},
  year = {2025},
  doi = {10.1112/jlms.70330},
  url = {https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/jlms.70330},
  note = {Verified: publisher metadata and full primary text; first published 21 October 2025. Lemma 2.17 and Corollary 2.18, with their complete proofs, independently reopened 17 November 2026. Used only for opposite-vertex closed subgroups with trivial completed edge intersections in a proper free profinite amalgam; no general profinite Kurosh theorem is inferred.}
}
'''
p.write_text(s)

p=root/'LM4_SUCCESSOR_paper.tex';s=p.read_text()
needle='''That equality, remaining necks, global transfer and the final joint-source
condition remain unresolved.'''
replacement='''The corrected d-contact and inner source loop generate an actual free
group of rank two with its full induced profinite topology. The one-sided
source model is a proper quotient of the actual five-source image.
Before the cross filling, the entire marked six-source group has its
full topology; the final discrete and compact source kernels are specified
ambient normal-closure intersections. A two-sheet edge presentation gives
an ordinary kernel-matching saturation and a separate exact finite-target
criterion for the compact base kernel. Neither stabilization nor equality
between the closed discrete kernel and the compact kernel is inferred.
The fixed-source equality, remaining necks, global transfer and final
joint-source condition remain unresolved.'''
assert s.count(needle)==1
p.write_text(s.replace(needle,replacement))

p=root/'task_coverage.csv'
with p.open(newline='') as f:
    reader=csv.DictReader(f);fields=reader.fieldnames;tasks=list(reader)
assert len(tasks)==49
for row in tasks:
    if row['task'] not in {'B.4','B.4.a','B.4.b','B.4.c','B.4.h'}:continue
    assert row['outcome']=='Open'
    for sid in ('B.131','B.132','B.133','B.134'):
        assert sid not in row['statement_ids'].split(';')
        row['statement_ids']+=';'+sid
    row['state']+=' B131 now formally proves actual noncommutation of the corrected d-contact with m in both categories, the exact whole one-sided source image and the strict upper H5 kernel bound. B132 proves that the actual pair <m,D_s> is free rank two with full induced profinite topology. B133 proves the actual pre-cross six-source subgroup has full induced topology and identifies both final source kernels as actual ambient normal-closure intersections. B134 retains both mirror cross relations, gives the exact ordinary matching-kernel saturation and an independent finite matching-normal criterion for the compact base kernel.'
    row['state']=row['state'].replace('B131 remains a reviewed proposed source pending build/integration.','The formerly proposed B131 source is now integrated after complete source review and private QA; final combined QA is recorded separately.')
    row['approaches']+=' Uniform retained-character core omission; simultaneous all-integer Schreier orbit; arbitrary finite-kernel refinement by finite wreath targets; proper mirror-only completed amalgam and actual zero edge intersections; complete two-sheet relative edge presentation and independent finite regular-permutation extension.'
    row['obstruction']+=' The first one-sheet research regrouping omitted a necessary mirror conjugate; its actual-final-group identification was withdrawn and all original attempts retained. The corrected two-sheet construction does not prove finite-stage stabilization, cofinality of matching finite kernels, equality of closed discrete and compact source kernels, or the actual fixed-source equality.'
    row['next_step']='Evaluate the complete actual two-sheet matching kernels and their marked source intersection, compare the actual source with the discrete and compact fixed kernel, and retain all signed node/source translates. The other necks, global transfer and final joint-source condition remain subsequent gates.'
with p.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader();writer.writerows(tasks)

subprocess.run([sys.executable,str(root/'code/assemble_register.py')],check=True)
rows=list(csv.DictReader((root/'LM4_SUCCESSOR_results.csv').open()))
assert len(rows)==303
assert dict(Counter(r['status'] for r in rows))=={'Known':6,'Proved':259,'Refuted':19,'Open':19}

p=root/'LM4_SUCCESSOR_report.md';s=p.read_text()
assert s.splitlines()[0]=='INCOMPLETE'
lines=s.splitlines(True)
start=next(i for i,line in enumerate(lines) if line.startswith('| Task or lead |'))
end=start
while end<len(lines) and lines[end].startswith('|'):end+=1
def cell(value):return value.replace('|','\\|').replace('\n',' ')
table=['| Task or lead | Statements | Outcome and exact state |\n',
       '|---|---|---|\n']
table.extend('| '+cell(r['task'])+' | '+cell(r['statement_ids'])+' | **'+cell(r['outcome'])+'** — '+cell(r['state'])+' |\n' for r in tasks)
lines[start:end]=table
s=''.join(lines)
s+='\n## Twenty-seventh-hour integrated source topology and kernel comparison\n\n'
s+=(root/'records/twenty_seventh_hour_research_report.md').read_text()
s+='''
The opening task table has been synchronized from all 49 current coverage
rows. Its previous historical state, which lagged the newer body, is
retained in the complete before-integration report. This changes no task
outcome: both main decisions remain Open. The formal baseline now contains
303 statements (259 Proved, 19 Refuted, 19 Open, 6 Known) and 113 bibliography
entries. Final combined PDF build and visible QA are recorded separately.
'''
p.write_text(s)
print('Integrated B131--B134 byte-exactly:303 statements,259 Proved,113 references,49 opening task rows;both main decisions Open.')
