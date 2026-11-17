"""Integrate six byte-bound, completely reviewed actual-neck propositions."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import hashlib
import json
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
review = json.loads((root/'records/checkpoint25_root_formal_reviews.json').read_text())
assert review['status'] == 'PASS_COMPLETE_SOURCE_REVIEW'
copies = [
 ('work_DE/B118_boundary_neck_intersection_proposed.tex', 'sections/b_boundary_neck_intersection.tex'),
 ('work_CE/B119_ordinary_filling_fixed_source_proposed.tex', 'sections/b_ordinary_filling_fixed_source.tex'),
 ('work_A/B120_intermediate_boundary_amalgam_proposed.tex', 'sections/b_intermediate_boundary_amalgam.tex'),
 ('work_A/B121_final_neck_retraction_proposed.tex', 'sections/b_final_neck_retraction.tex'),
 ('work_DE/B122_intermediate_completed_centralizer_proposed.tex', 'sections/b_intermediate_completed_centralizer.tex'),
 ('work_CE/B123_two_operator_fixed_kernel_proposed.tex', 'sections/b_two_operator_fixed_kernel.tex'),
]
assert set(review['formal_sources']) == {s for s, _ in copies}
for source, target in copies:
    assert hashlib.sha256((root/source).read_bytes()).hexdigest() == review['formal_sources'][source]
    assert not (root/target).exists()

backup = root/'records/pdf_qa/checkpoint25_before_integration'
backup.mkdir(parents=True, exist_ok=False)
for name in ('LM4_SUCCESSOR_paper.pdf', 'LM4_SUCCESSOR_paper.tex',
             'LM4_SUCCESSOR_paper.log', 'LM4_SUCCESSOR_paper.bbl',
             'LM4_SUCCESSOR_results.csv', 'LM4_SUCCESSOR_references.bib'):
    target = backup/(name+'.retained.txt' if name.endswith('.bbl') else name)
    target.write_bytes((root/name).read_bytes())

records = []
for source, target in copies:
    data = (root/source).read_bytes()
    (root/target).write_bytes(data)
    records.append({'source': source, 'integrated': target,
                    'sha256': hashlib.sha256(data).hexdigest(),
                    'comparison': 'Byte-identical completely reviewed frozen source.'})
(root/'records/checkpoint25_formal_source_copies.json').write_text(json.dumps({
    'integrated_at': datetime.now(timezone.utc).isoformat(), 'copies': records}, indent=2)+'\n')
p = root/'sections/part_B.tex'
s = p.read_text()
for _, target in copies:
    line = '\\input{'+target+'}'
    assert line not in s
    s += line+'\n'
p.write_text(s)

p = root/'LM4_SUCCESSOR_paper.tex'
s = p.read_text()
s = s.replace('\\date{16 November 2026', '\\date{17 November 2026', 1)
old = '''the embedded branch word is retained. The source image after the two
cross relations, the remaining necks, global transfer, deeper nonabelian
lifting and subsequent joint-source condition remain unresolved.'''
new = '''the embedded branch word is retained. The actual boundary subgroup
has its full topology, and its intersection with the completed neck is
exactly the full-prefix procyclic subgroup. An intermediate boundary
amalgam is proper in full completion; its cone centralizer is the closure
of the discrete centralizer. Its four remaining relations are squares
in a fully embedded completed carrier. After those relations, the actual
ordinary neck remains a retract, with full profinite topology. An exact
rank-eleven fiber quotient with two fixed source operators retains all
forty node seeds and every signed translate. It reduces the actual
unfilled source equality to the specified family-kernel fixed subgroup;
the retained filled quotient has exactly its free-two source as fixed
subgroup, also in full completion. The unfilled fixed-kernel equality,
remaining necks, global transfer and final joint-source condition remain
unresolved.'''
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
    for n in range(118,124):
        sid = f'B.{n}'
        assert sid not in row['statement_ids'].split(';')
        row['statement_ids'] += ';'+sid
    row['state'] += ' B118 proves the actual boundary full topology and completed neck intersection. B119 gives the exact ordinary13 presentation and the full filled fixed-source group. B120 proves the proper completed intermediate boundary amalgam, its discrete F6 cone centralizer, and full topology of the four-square carrier. B121 proves an actual ordinary one-neck retraction onto the common F5 neck after all cross/prefix relations. B122 proves the intermediate completed cone centralizer equals the closure of its discrete centralizer, without asserting Fhat6 injection. B123 gives the whole actual F11/two-source-operator presentation and the exact remaining discrete/full family-kernel fixed-source gate.'
    row['approaches'] += ' Boundary HNN detector and compatible finite kernels; literal raw source rewrites; finite dihedral carrier extension and final explicit reflection retraction; connected profinite fixed graph and compact coset quotient; complete signed two-operator orbit of all forty ordinary node seeds.'
    row['obstruction'] += ' The intermediate centralizer formula does not transfer through the four final square relations. The actual neck retraction is not asserted to be equivariant for the selected cone. The remaining equality is J^delta=I discretely and Jbar^delta=Ibar in the actual full completion, with all signed node/source translates retained.'
    row['next_step'] = 'Determine the actual family-kernel fixed subgroup in the exact two-operator presentation, preserving every node and source translate. Compare the final source centralizer with the intermediate closure result, then treat the other necks and global transfer while retaining the separate final joint-source condition.'
with p.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader(); writer.writerows(rows)

subprocess.run([sys.executable, str(root/'code/assemble_register.py')], check=True)
rows = list(csv.DictReader((root/'LM4_SUCCESSOR_results.csv').open()))
assert len(rows) == 292
assert dict(Counter(r['status'] for r in rows)) == {'Known':6,'Proved':248,'Refuted':19,'Open':19}

p = root/'LM4_SUCCESSOR_report.md'
s = p.read_text()
assert s.splitlines()[0] == 'INCOMPLETE'
marker = '## Twenty-fifth-hour research: the actual final neck and its fixed kernel'
assert marker not in s
s += '\n'+marker+'\n\n'+(root/'records/twenty_fifth_hour_research_report.md').read_text()
p.write_text(s)
print('Integrated B118--B123: 292 statements, 248 Proved; both main decisions remain Open.')
