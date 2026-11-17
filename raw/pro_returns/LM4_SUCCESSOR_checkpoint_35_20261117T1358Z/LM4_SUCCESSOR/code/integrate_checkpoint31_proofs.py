"""Integrate ten completely reviewed proofs while retaining all preceding bytes."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import hashlib
import json
import shutil
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
read = lambda rel: (root / rel).read_text()
review = json.loads(read('records/checkpoint31_root_formal_reviews.json'))
assert review['status'] == 'PASS_COMPLETE_SOURCE_REVIEW'
copies = review['copies']
expected = ['A.92', 'A.93', 'A.94'] + ['B.' + str(n) for n in range(148, 155)]
assert [row['statement'] for row in copies] == expected
for row in copies:
    data = (root / row['source']).read_bytes()
    assert hashlib.sha256(data).hexdigest() == row['sha256']
    assert not any(c < 32 and c not in (9, 10) for c in data)
    assert not (root / row['target']).exists()
for rel, digest in review['independent_reviews'].items():
    assert hashlib.sha256((root / rel).read_bytes()).hexdigest() == digest

paper = read('LM4_SUCCESSOR_paper.tex')
anchor = r'\input{sections/a_dihedral_covariance_limitation.tex}'
assert paper.count(anchor) == 1
paper = paper.replace(anchor, anchor + '\n' + '\n'.join(
    r'\input{' + row['target'] + '}' for row in copies
    if row['statement'].startswith('A.')))
anchor = 'therefore supplies no additional single-cover linear equation.'
assert paper.count(anchor) == 1
paper = paper.replace(anchor, anchor + r''' The same actual full
source word realizes all three permitted odd Alexander coordinates,
including weighted swap duality, independently of its odd dihedral
rotation. The actual canonical and negative-hexagon equations give the
complete displayed three-module boundary. Every nonabelian affine
image of the marked pure four-strand group factors through one of five
literal free-two quotients. Hence the full first elementary-two layer
over every odd abelian head adds no pentagon condition beyond exact
swap duality. Canonical realization and the nonlinear word remain open.''')
anchor = 'images. Noninjective extensions exist; no filling collapse follows.'
assert paper.count(anchor) == 1
paper = paper.replace(anchor, anchor + r''' The complete ordinary
one-family stabilizer is cyclic and admits a marked fixed section.
The remaining source kernel has an exact presentation on three whole
contact orbits. The complete first filling is a free-coset extension
with the opposite square's base component retained; its mirrored free
neck has an explicit coordinate position and retraction. An actual
peripheral-cocycle correction identifies the compact stabilizer with
the procyclic inner source, using explicit finite-index free bases.
An arbitrary-target finite permutation construction then proves full
induced topology of the mixed fixed source and extends its marked
section to the completed fixed projection. A net argument identifies
the actual source-kernel closure with the intersection of the two
actual closures. The remaining local fixed-kernel generation is not
implied.''')
part_b = read('sections/part_B.tex')
for row in copies:
    if row['statement'].startswith('B.'):
        line = r'\input{' + row['target'] + '}'
        assert line not in part_b
        part_b += line + '\n'

with (root / 'task_coverage.csv').open(newline='') as stream:
    reader = csv.DictReader(stream)
    fields, tasks = reader.fieldnames, list(reader)
assert len(tasks) == 49
old_outcomes = [(row['task'], row['outcome']) for row in tasks]
for row in tasks:
    if row['task'] in {'A.7', 'A.8'}:
        for sid in expected[:3]:
            assert sid not in row['statement_ids'].split(';')
            row['statement_ids'] += ';' + sid
        row['state'] += ' Latest formal cycle31: A92 proves exact common-word and weighted-duality surjectivity at all odd heads. A93 computes the actual canonical three-module boundary and independent marked dihedral coordinate. A94 classifies every nonabelian affine P4 image into five literal free-two quotients and proves the whole first elementary-two/odd-abelian-head pentagon limitation.'
        row['approaches'] += ' Uniform norm idempotents and compact simultaneous realization; exact negative hexagon and canonical Klein-four action; complete all-field affine classification and nontrivial-coefficient averaging.'
        row['obstruction'] = 'The displayed module and affine pentagon constraints do not determine actual canonical realization or the full nonlinear cusp word. The all-odd-head scalar criterion for actual full-GT data and the canonical nonlinear involution comparison remain open; arbitrary duality-word realization does not settle them.'
        row['next_step'] = 'Retain the full primitive boundary in the actual relative pro-two sphere kernel and prove the based canonical involution comparison, including its actual cocycle. Continue the main full conjugacy gate without replacing canonical data by arbitrary tangent words.'
    if row['task'] in {'B.4', 'B.4.a', 'B.4.b', 'B.4.c', 'B.4.h'}:
        for sid in expected[3:]:
            assert sid not in row['statement_ids'].split(';')
            row['statement_ids'] += ';' + sid
        row['state'] += ' Latest formal cycle31: B148–B150 give the exact free-three stabilizer normalization, full ordinary cyclic stabilizer, marked section and three-whole-orbit contact-kernel presentation. B151–B152 retain the complete first filling, opposite square base component and mirrored-neck coordinate placement (final survival already B121). B153 proves the actual compact stabilizer directly from the corrected cocycle and two finite-index free bases. B154 proves full induced Ja topology, the marked compact fixed section and the actual source-kernel closure intersection identity.'
        row['approaches'] += ' Exact ordered peripheral correction q_s=delta(h_s); explicit free-basis isomorphism of index-two subgroups; primitive full profinite centralizers; arbitrary finite-target induced permutation construction retaining T0; continuous section and net argument; entire coset stabilizers and both filling families.'
        row['obstruction'] = 'The exact local remaining question is (closure K_rem)^delta=closure I_src in the stated actual ambient completion. Its generation is unresolved. Other necks, full-base transfer and the original B75 icosahedral uniform finite-neighborhood criterion are still open. Neither internal carrier properness, free-neck survival nor the marked compact section proves those gates.'
        row['next_step'] = 'Attack the entire remaining fixed kernel with all three actual contact orbits and all nodal translates, then transfer through the other necks and actual full base. In parallel construct the original B75 finite detector for every prescribed source neighborhood, retaining all original source directions.'
assert [(row['task'], row['outcome']) for row in tasks] == old_outcomes
assert all(next(row for row in tasks if row['task'] == name)['outcome'] == 'Open'
           for name in ('A.8', 'B.4'))

report = read('LM4_SUCCESSOR_report.md')
assert report.splitlines()[0] == 'INCOMPLETE'
lines = report.splitlines(True)
start = next(i for i, line in enumerate(lines) if line.startswith('| Task or lead |'))
end = start
while end < len(lines) and lines[end].startswith('|'):
    end += 1
cell = lambda value: value.replace('|', r'\|').replace('\n', ' ')
table = ['| Task or lead | Statements | Outcome and exact state |\n',
         '|---|---|---|\n']
table += ['| ' + cell(row['task']) + ' | ' + cell(row['statement_ids']) +
          ' | **' + cell(row['outcome']) + '** — ' + cell(row['state']) + ' |\n'
          for row in tasks]
lines[start:end] = table
report = ''.join(lines) + '\n\n' + read('records/thirty_first_hour_research_report.md')

backup = root / 'records/pdf_qa/checkpoint31_before_integration'
assert not backup.exists()
paths = ['LM4_SUCCESSOR_paper.' + ext for ext in
         ('pdf', 'tex', 'log', 'aux', 'bbl', 'blg', 'toc', 'out')]
paths += ['LM4_SUCCESSOR_results.csv', 'LM4_SUCCESSOR_references.bib',
          'LM4_SUCCESSOR_report.md', 'task_coverage.csv', 'sections/part_B.tex',
          'sections/b_sources.bib', 'code/assemble_register.py']
paths += [str(p.relative_to(root)) for p in (root / 'records').glob('build_*.log')]
for rel in paths:
    src = root / rel
    if not src.is_file():
        continue
    suffix = '.retained.txt' if src.suffix in {'.aux', '.bbl', '.blg', '.toc'} else ''
    dest = backup / (rel + suffix)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
for row in copies:
    (root / row['target']).write_bytes((root / row['source']).read_bytes())
(root / 'LM4_SUCCESSOR_paper.tex').write_text(paper)
(root / 'sections/part_B.tex').write_text(part_b)
(root / 'LM4_SUCCESSOR_report.md').write_text(report)
with (root / 'task_coverage.csv').open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader()
    writer.writerows(tasks)
(root / 'records/checkpoint31_formal_source_copies.json').write_text(json.dumps({
    'integrated_at': datetime.now(timezone.utc).isoformat(),
    'copies': copies,
    'comparison': 'Every integrated source is byte-identical to its final fully reviewed owned source.'
}, indent=2) + '\n')
subprocess.run([sys.executable, str(root / 'code/assemble_register.py')], check=True)
rows = list(csv.DictReader((root / 'LM4_SUCCESSOR_results.csv').open()))
assert len(rows) == 333
assert dict(Counter(row['status'] for row in rows)) == {
    'Known': 6, 'Proved': 289, 'Refuted': 19, 'Open': 19}
assert (root / 'LM4_SUCCESSOR_references.bib').read_bytes() == (
    backup / 'LM4_SUCCESSOR_references.bib').read_bytes()
print('Integrated ten unchanged final sources:333 statements,289 Proved,114 references,49 tasks;both main decisions Open.')
