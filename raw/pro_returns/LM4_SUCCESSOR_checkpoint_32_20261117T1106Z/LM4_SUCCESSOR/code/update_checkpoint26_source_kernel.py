"""Integrate seven completely reviewed actual-source/family-kernel proofs."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import hashlib
import json
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
review = json.loads((root/'records/checkpoint26_root_formal_reviews.json').read_text())
assert review['status'] == 'PASS_COMPLETE_SOURCE_REVIEW'
copies = [
 ('work_DE/B124_outer_source_retract_proposed.tex', 'sections/b_outer_source_retract.tex'),
 ('work_A/B125_ordinary_star_single_cross_proposed.tex', 'sections/b_ordinary_star_single_cross.tex'),
 ('work_A/B126_final_prefix_axes_proposed.tex', 'sections/b_final_prefix_axes.tex'),
 ('work_CE/B127_family_kernel_schreier_proposed.tex', 'sections/b_family_kernel_schreier.tex'),
 ('work_DE/B128_compact_family_module_proposed.tex', 'sections/b_compact_family_module.tex'),
 ('work_CE/B129_compact_nonlifting_proposed.tex', 'sections/b_compact_nonlifting.tex'),
 ('work_CE/B130_actual_source_commutator_proposed.tex', 'sections/b_actual_source_commutator.tex'),
]
assert set(review['formal_sources']) == {s for s, _ in copies}
for source, target in copies:
    assert hashlib.sha256((root/source).read_bytes()).hexdigest() == review['formal_sources'][source]
    assert not (root/target).exists()

backup = root/'records/pdf_qa/checkpoint26_before_integration'
backup.mkdir(parents=True, exist_ok=False)
for name in ('LM4_SUCCESSOR_paper.pdf', 'LM4_SUCCESSOR_paper.tex',
             'LM4_SUCCESSOR_paper.log', 'LM4_SUCCESSOR_paper.bbl',
             'LM4_SUCCESSOR_results.csv', 'LM4_SUCCESSOR_references.bib',
             'LM4_SUCCESSOR_report.md', 'task_coverage.csv'):
    target = backup/(name+'.retained.txt' if name.endswith('.bbl') else name)
    target.write_bytes((root/name).read_bytes())
(backup/'part_B.tex.retained.txt').write_bytes((root/'sections/part_B.tex').read_bytes())

records = []
for source, target in copies:
    data = (root/source).read_bytes()
    (root/target).write_bytes(data)
    records.append({'source':source, 'integrated':target,
                    'sha256':hashlib.sha256(data).hexdigest(),
                    'comparison':'Byte-identical completely reviewed frozen source.'})
(root/'records/checkpoint26_formal_source_copies.json').write_text(json.dumps({
    'integrated_at':datetime.now(timezone.utc).isoformat(), 'copies':records}, indent=2)+'\n')
p = root/'sections/part_B.tex'
s = p.read_text()
for _, target in copies:
    line = '\\input{'+target+'}'
    assert line not in s
    s += line+'\n'
p.write_text(s)

p = root/'LM4_SUCCESSOR_paper.tex'
s = p.read_text()
old = '''subgroup, also in full completion. The unfilled fixed-kernel equality,
remaining necks, global transfer and final joint-source condition remain
unresolved.'''
new = '''subgroup, also in full completion. The outer five-source factor survives
as an actual retract, and the entire source image has exact abelianization
of rank six in both categories. The full six-generator source map is
nevertheless noninjective: an explicit nontrivial source commutator
vanishes by actual node and cross relations. Its two factors generate
an actual two-dimensional integral torus-group retract, with the full
induced profinite topology. The final four-prefix filling also kills a
specified nontrivial element of the completed intermediate centralizer.
Before the cross filling, the original-parity cover is a proper full
profinite star; the cross filling has one specified commutator relator.
The completed corner face is exact, while the four prefix axes have
sharp two-edge overlaps and discrete malnormal cyclic stabilizers.
The whole family kernel has an exact all-orbit Schreier presentation.
Its continuous abelianization is a free rank-eight module over the
retained completed group ring, with an exchanged-pair involution and
zero Tate groups. A finite source-level detector gives a missing
invariant abelian class. An actual residue-three free-two retract
proves that this class has no fixed lift, also in the actual closed
kernel. These results do not decide the unfilled fixed-source equality.
That equality, remaining necks, global transfer and the final joint-source
condition remain unresolved.'''
assert old in s
p.write_text(s.replace(old, new, 1))

p = root/'task_coverage.csv'
with p.open() as stream:
    reader = csv.DictReader(stream)
    fields, rows = reader.fieldnames, list(reader)
assert len(rows) == 49
for row in rows:
    if row['task'] not in {'B.4','B.4.a','B.4.b','B.4.c','B.4.h'}:
        continue
    assert row['outcome'] == 'Open'
    for n in range(124,131):
        sid = f'B.{n}'
        assert sid not in row['statement_ids'].split(';')
        row['statement_ids'] += ';'+sid
    row['state'] += ' B124 proves the actual outer F5 source retract after all relations and the exact source-image abelianizations Z6 and Zhat6. B125 proves the proper original-parity star and exact single cross-commutator quotient. B126 proves the actual completed corner face and discrete malnormal prefix-axis family. B127 gives the whole nonlinear Schreier presentation and exact discrete family module. B128 identifies the actual compact family abelianization with a free completed-group-ring module and proves the finite source-level limitation. B129 proves actual discrete and compact nonlinear nonlifting through an equivariant free-two retract. B130 settles source injectivity negatively in both categories by the exact relation [m,s1 s4^-1 s1^-1]=1, proves an actual Z2/Zhat2 retract, and proves that the final filling kills a nontrivial completed intermediate-centralizer element.'
    row['approaches'] += ' Actual inverse outer basis and six independent characters; fully invariant two-edge finite kernels; complete corner-face and all-axis coefficient calculation; whole signed Schreier connectors; inverse continuous compact-module maps; residue-three equivariant free-fiber retract; exact three-node norm identity and finite detection of the source-domain commutator; compatible finite vertex targets detecting the intermediate commutator.'
    row['obstruction'] += ' The earlier unproved full source injection is now excluded by B130; its source domain remains free-six, while its actual image has a nontrivial kernel and contains a Z2 retract. The paired abelian module and zero Tate groups do not imply nonlinear fixed lifting, as B129 proves in the actual closed kernel. The fixed-source equalities remain Open; no fixed element outside the source has been constructed.'
    row['next_step'] = 'Determine further actual source relations and the exact source image, then compare that image with the actual discrete and compact fixed kernel in the whole two-operator presentation. Retain every node/source translate and the completed intermediate filling kernel. After that, address the other necks, global transfer and the separate final joint-source condition.'
with p.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

subprocess.run([sys.executable, str(root/'code/assemble_register.py')], check=True)
rows = list(csv.DictReader((root/'LM4_SUCCESSOR_results.csv').open()))
assert len(rows) == 299
assert dict(Counter(r['status'] for r in rows)) == {'Known':6,'Proved':255,'Refuted':19,'Open':19}

p = root/'LM4_SUCCESSOR_report.md'
s = p.read_text()
assert s.splitlines()[0] == 'INCOMPLETE'
marker = '## Twenty-sixth-hour research: an actual source kernel and nonlinear fixed lifting'
assert marker not in s
s += '\n'+marker+'\n\n'+(root/'records/twenty_sixth_hour_research_report.md').read_text()
p.write_text(s)
print('Integrated B124--B130: 299 statements, 255 Proved; both main decisions remain Open.')
