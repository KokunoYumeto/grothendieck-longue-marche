"""Integrate six frozen reviewed components while retaining preceding bytes."""
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
review = json.loads((root / 'records/checkpoint29_root_formal_reviews.json').read_text())
assert review['status'] == 'PASS_COMPLETE_SOURCE_REVIEW'
copies = review['copies']
assert [r['statement'] for r in copies] == ['A.87', 'A.88', 'B.138', 'B.139', 'B.140', 'B.141']
for row in copies:
    assert hashlib.sha256((root / row['source']).read_bytes()).hexdigest() == row['sha256']
    assert not (root / row['target']).exists()
backup = root / 'records/pdf_qa/checkpoint29_before_integration'
backup.mkdir(parents=True, exist_ok=False)
paths = ['LM4_SUCCESSOR_paper.' + suffix for suffix in ('pdf', 'tex', 'log', 'aux', 'bbl', 'blg', 'toc', 'out')]
paths += ['LM4_SUCCESSOR_results.csv', 'LM4_SUCCESSOR_references.bib',
          'LM4_SUCCESSOR_report.md', 'task_coverage.csv', 'sections/part_B.tex',
          'sections/b_sources.bib', 'code/assemble_register.py']
paths += [str(p.relative_to(root)) for p in (root / 'records').glob('build_*.log')]
for rel in paths:
    src = root / rel
    if not src.is_file(): continue
    suffix = '.retained.txt' if src.suffix in {'.aux', '.bbl', '.blg', '.toc'} else ''
    dest = backup / (rel + suffix)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
for row in copies:
    (root / row['target']).write_bytes((root / row['source']).read_bytes())
p = root / 'LM4_SUCCESSOR_paper.tex'
s = p.read_text()
needle = '\\input{sections/a_canonical_cusp_frame.tex}'
assert s.count(needle) == 1
s = s.replace(needle, needle + '\n' + '\n'.join('\\input{' + r['target'] + '}' for r in copies if r['statement'].startswith('A.')))
needle = 'unit equality nor the full word identity is established.'
assert s.count(needle) == 1
s = s.replace(needle, '''unit equality nor the full word identity is established. The actual
marked three-cycle gives a second exact criterion, with the unique cusp
frame and original solution explicit. The full Alexander coefficient
ring gives an exact test for the unit equality; its actual common
dihedral quotient proves equality modulo eight.''')
needle = '''trivial intersection, by their exact invariant-tree directions. Compact
whole-edge overlap and ambient filling survival are not inferred.'''
assert s.count(needle) == 1
s = s.replace(needle, '''trivial intersection, by their exact invariant-tree directions.
Arbitrary finite targets now prove full topology of both entire
unfilled edges, and a continuous kernel decomposition proves their
trivial whole compact intersection. The exact one-family quotient has
its actual source as fixed subgroup, also in full completion; the
original equality reduces to a specified remaining fixed-kernel
condition. Neither named retained coarse section can be normalized by
correcting the second source operator in the family kernel, ordinarily
or compactly. The actual regional retraction kernels have complete
graph presentations and ordered neck actions. The retained mixed square
relation obstructs the specified opposite-kernel retractions; regional
collapse and filling survival are not inferred.''')
p.write_text(s)
p = root / 'sections/part_B.tex'
s = p.read_text()
for row in copies:
    if row['statement'].startswith('B.'):
        line = '\\input{' + row['target'] + '}'
        assert line not in s
        s += line + '\n'
p.write_text(s)
p = root / 'sections/b_sources.bib'
s = p.read_text()
bib = (root / 'work_DE/next_marginal_source/RibesZalesskii2004_verified28.bib').read_text()
bib = bib[bib.index('@article'):].strip()
assert 'BRibesZalesskii2004FreeProducts' not in s
p.write_text(s.rstrip() + '\n\n' + bib + '\n')
(root / 'records/checkpoint29_formal_source_copies.json').write_text(json.dumps({
    'integrated_at': datetime.now(timezone.utc).isoformat(), 'copies': copies,
    'comparison': 'Every integrated component is byte-identical to its fully reviewed frozen source.'
}, indent=2) + '\n')
p = root / 'task_coverage.csv'
with p.open(newline='') as f:
    reader = csv.DictReader(f); fields = reader.fieldnames; tasks = list(reader)
assert len(tasks) == 49
for row in tasks:
    if row['task'] in {'A.7', 'A.8'}:
        for sid in ('A.87', 'A.88'):
            assert sid not in row['statement_ids'].split(';')
            row['statement_ids'] += ';' + sid
        row['state'] += ' A87 proves the exact marked three-cycle, unique pure frame and original regular cusp solution. A88 gives the full completed Alexander coefficient test and proves a_reg congruent to d modulo8 using the actual common dihedral quotient.'
        row['approaches'] += ' Complete marked frame transport; full F2[[Zhat]] coefficient module and T-minus-one injectivity; actual C4 and D8 comparison.'
        row['obstruction'] += ' Equality modulo8 does not prove equality of full profinite units; the exact full coefficient equation and nonlinear Omega identity remain separate gates.'
        if row['task'] == 'A.8':
            assert row['outcome'] == 'Open'
            row['next_step'] = 'Resolve Theta_u D_d=1 with every cyclic head and the subsequent nonlinear marked three-cycle/Omega identity; keep GT0, full-GT and general-P assumptions separate.'
    if row['task'] in {'B.4', 'B.4.a', 'B.4.b', 'B.4.c', 'B.4.h'}:
        assert row['outcome'] == 'Open'
        for sid in ('B.138', 'B.139', 'B.140', 'B.141'):
            assert sid not in row['statement_ids'].split(';')
            row['statement_ids'] += ';' + sid
        row['state'] += ' B138 proves the full topology and trivial whole compact intersection of the two unfilled edges. B139 proves the actual ordinary and compact one-family fixed-source equality and exact remaining-kernel reduction. B140 excludes family-kernel repair of either named coarse section in both categories. B141 gives the faithful regional kernel graph and complete mixed square filling, which obstructs the specified regional retractions.'
        row['approaches'] += ' Arbitrary finite-target cyclic-edge refinement; closed-product proof; continuous coproduct intersections; actual finite graph/cocycle quotient; two-equation full-module obstruction; inverse graph-kernel presentations and ordered neck cocycle.'
        row['obstruction'] += ' Local filling survival, ambient kappa-kernel symmetry, remaining fixed-kernel equality, other necks and global transfer remain unresolved. Failure of a retraction is not a regional-collapse proof.'
        row['next_step'] = 'Use the exact mixed relation and actual neck cocycle to resolve filling survival and ambient source/kernel comparisons; test the remaining fixed-kernel condition without identifying an infinite graph completion or substituting a smaller quotient.'
with p.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields); writer.writeheader(); writer.writerows(tasks)
subprocess.run([sys.executable, str(root / 'code/assemble_register.py')], check=True)
rows = list(csv.DictReader((root / 'LM4_SUCCESSOR_results.csv').open()))
assert len(rows) == 314
assert dict(Counter(r['status'] for r in rows)) == {'Known': 6, 'Proved': 270, 'Refuted': 19, 'Open': 19}
p = root / 'LM4_SUCCESSOR_report.md'
s = p.read_text(); assert s.splitlines()[0] == 'INCOMPLETE'
lines = s.splitlines(True)
start = next(i for i, line in enumerate(lines) if line.startswith('| Task or lead |'))
end = start
while end < len(lines) and lines[end].startswith('|'): end += 1
def cell(value): return value.replace('|', '\\|').replace('\n', ' ')
table = ['| Task or lead | Statements | Outcome and exact state |\n', '|---|---|---|\n']
table.extend('| ' + cell(r['task']) + ' | ' + cell(r['statement_ids']) + ' | **' + cell(r['outcome']) + '** — ' + cell(r['state']) + ' |\n' for r in tasks)
lines[start:end] = table
s = ''.join(lines)
s += '\n## Twenty-ninth-hour integrated coefficient, compact-source and mixed-filling proofs\n\n'
s += (root / 'records/twenty_ninth_hour_research_report.md').read_text()
s += '\nThe opening table is synchronized from all49 coverage rows. No task outcome changes. Final combined build and visible QA are bound separately to the resulting PDF.\n'
p.write_text(s)
print('Integrated A87/A88/B138/B139/B140/B141 byte-exactly:314 statements,270 Proved,114 references,49 task rows;both main decisions Open.')
