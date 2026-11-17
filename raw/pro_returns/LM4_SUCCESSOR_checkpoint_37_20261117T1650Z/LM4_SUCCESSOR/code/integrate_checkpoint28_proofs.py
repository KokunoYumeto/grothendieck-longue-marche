"""Integrate the five frozen, completely reviewed sources byte-exactly."""
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
review = json.loads((root / 'records/checkpoint28_root_formal_reviews.json').read_text())
assert review['status'] == 'PASS_COMPLETE_SOURCE_REVIEW'
copies = review['copies']
assert [r['statement'] for r in copies] == ['A.85', 'A.86', 'B.135', 'B.136', 'B.137']
for row in copies:
    assert hashlib.sha256((root / row['source']).read_bytes()).hexdigest() == row['sha256']
    assert not (root / row['target']).exists()
backup = root / 'records/pdf_qa/checkpoint28_before_integration'
backup.mkdir(parents=True, exist_ok=False)
for rel in ('LM4_SUCCESSOR_paper.pdf', 'LM4_SUCCESSOR_paper.tex',
            'LM4_SUCCESSOR_paper.log', 'LM4_SUCCESSOR_paper.bbl',
            'LM4_SUCCESSOR_results.csv', 'LM4_SUCCESSOR_references.bib',
            'LM4_SUCCESSOR_report.md', 'task_coverage.csv',
            'sections/part_B.tex', 'sections/b_sources.bib',
            'code/assemble_register.py'):
    dest = backup / (rel + '.retained.txt' if rel.endswith('.bbl') else rel)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(root / rel, dest)
for row in copies:
    (root / row['target']).write_bytes((root / row['source']).read_bytes())
p = root / 'LM4_SUCCESSOR_paper.tex'
s = p.read_text()
needle = '\\input{work_A/A_involutions.tex}'
assert s.count(needle) == 1
s = s.replace(needle, needle + '\n' + '\n'.join('\\input{' + r['target'] + '}' for r in copies if r['statement'].startswith('A.')))
needle = 'leave the full marked generation question unresolved.'
assert s.count(needle) == 1
s = s.replace(needle, needle + ''' The actual
Klein four action makes the canonical coset defect induced over the
constant finite-group ring. A uniquely normalized regular cusp frame
gives an exact nonlinear word criterion for the involution conjugacy,
whose abelianization compares two specified full units. Neither that
unit equality nor the full word identity is established.''')
needle = 'The fixed-source equality, remaining necks, global transfer and final\njoint-source condition remain unresolved.'
assert s.count(needle) == 1
s = s.replace(needle, '''The entire completed inner star has an exact cone centralizer;
the new fixed source norm has no fixed preimage there. Explicit before
and after face retractions determine their internal filling kernels.
The actual unfilled edge maps admit a symmetric local filling with
trivial fixed subgroup. The two whole ordinary ambient edge groups have
trivial intersection, by their exact invariant-tree directions. Compact
whole-edge overlap and ambient filling survival are not inferred.
The fixed-source equality, remaining necks, global transfer and final
joint-source condition remain unresolved.''')
p.write_text(s)
p = root / 'sections/part_B.tex'
s = p.read_text()
for row in copies:
    if not row['statement'].startswith('B.'): continue
    line = '\\input{' + row['target'] + '}'
    assert line not in s
    s += line + '\n'
p.write_text(s)
p = root / 'code/assemble_register.py'
s = p.read_text()
old = "for p in sorted((P/'sections').glob('b_*.tex')):"
assert s.count(old) == 1
s = s.replace(old, "for p in sorted([*(P/'sections').glob('a_*.tex'), *(P/'sections').glob('b_*.tex')]):")
old = "r'\\\\statement\\{(B\\.(\\d+))\\}\\{([^}]+)\\}\\{'"
assert s.count(old) == 1
s = s.replace(old, "r'\\\\statement\\{([AB]\\.(\\d+))\\}\\{([^}]+)\\}\\{'")
old = "answers=banswers.get(int(m[2]),'B.4')"
assert s.count(old) == 1
s = s.replace(old, "answers=(banswers.get(int(m[2]),'B.4') if m[1].startswith('B.') else 'A.7;A.8')")
p.write_text(s)
p = root / 'sections/b_sources.bib'
s = p.read_text()
old = 'url={https://www.mathnet.ru/links/13bb2695581b8afbc15265283e477fde/sm1715_eng.pdf}'
assert s.count(old) == 1
s = s.replace(old, 'url={https://www.mathnet.ru/eng/sm1715}')
p.write_text(s)
(root / 'records/checkpoint28_formal_source_copies.json').write_text(json.dumps({
    'integrated_at': datetime.now(timezone.utc).isoformat(), 'copies': copies,
    'comparison': 'Every integrated component is byte-identical to its reviewed frozen source.'
}, indent=2) + '\n')
p = root / 'task_coverage.csv'
with p.open(newline='') as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    tasks = list(reader)
assert len(tasks) == 49
for row in tasks:
    if row['task'] in {'A.7', 'A.8'}:
        for sid in ('A.85', 'A.86'):
            assert sid not in row['statement_ids'].split(';')
            row['statement_ids'] += ';' + sid
        row['state'] += ' A85 proves the actual V4 fixed-coset and constant-ring induced Fox-defect structure. A86 gives the unique regular cusp frame, the exact nonlinear Omega criterion and its abelianization as the difference of two full units. Neither the two-unit equality nor Omega=1 is established.'
        row['approaches'] += ' Complete coupled semilinear Fox matrices; full section-class count; closed pointed transversal; actual cusp centralizer and same-conjugator square cancellation; actual C44 coefficient identification.'
        row['obstruction'] += ' The dihedral image of Omega vanishes identically and does not compare the two full units. Constant-ring induction does not give full group-ring splitting or marked generation.'
        if row['task'] == 'A.8':
            assert row['outcome'] == 'Open'
            row['next_step'] = 'Use the actual marked three-cycle and LM7/R2 compatibility to compare a_reg with d, then address the full nonlinear Omega word; retain separate GT0, GT and general-P scopes.'
    if row['task'] in {'B.4', 'B.4.a', 'B.4.b', 'B.4.c', 'B.4.h'}:
        assert row['outcome'] == 'Open'
        for sid in ('B.135', 'B.136', 'B.137'):
            assert sid not in row['statement_ids'].split(';')
            row['statement_ids'] += ';' + sid
        row['state'] += ' B135 proves whole inner-base noninjectivity, its entire completed cone centralizer, failure of fixed lifting for the actual source norm, and exact retracted-face kernels. B136 proves the actual unfilled maps and symmetric local quotient with trivial fixed subgroup. B137 proves trivial intersection of the whole two ordinary ambient edge groups by exact tree directions.'
        row['approaches'] += ' Full signed m/v presentation and all forty ordinary nodes; common winding finite targets; proper completed inner amalgam; exact block retractions; complete local symmetric fold; actual all-power fork and invariant-tree direction comparison.'
        row['obstruction'] += ' Whole compact edge overlap, translated overlap control, local filling survival and ambient kappa-kernel invariance remain separate gates. Ordinary trivial intersection does not prove free-product generation or post-filling injection.'
        row['next_step'] = 'Analyze actual translated overlaps and compatible full finite targets, prove or refute local filling survival and ambient kappa-kernel symmetry, and compare the final source to the actual fixed kernel before the remaining necks and global transfer.'
with p.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(tasks)
subprocess.run([sys.executable, str(root / 'code/assemble_register.py')], check=True)
rows = list(csv.DictReader((root / 'LM4_SUCCESSOR_results.csv').open()))
assert len(rows) == 308
assert dict(Counter(r['status'] for r in rows)) == {'Known': 6, 'Proved': 264, 'Refuted': 19, 'Open': 19}
p = root / 'LM4_SUCCESSOR_report.md'
s = p.read_text()
assert s.splitlines()[0] == 'INCOMPLETE'
lines = s.splitlines(True)
start = next(i for i, line in enumerate(lines) if line.startswith('| Task or lead |'))
end = start
while end < len(lines) and lines[end].startswith('|'): end += 1
def cell(value): return value.replace('|', '\\|').replace('\n', ' ')
table = ['| Task or lead | Statements | Outcome and exact state |\n', '|---|---|---|\n']
table.extend('| ' + cell(r['task']) + ' | ' + cell(r['statement_ids']) + ' | **' + cell(r['outcome']) + '** — ' + cell(r['state']) + ' |\n' for r in tasks)
lines[start:end] = table
s = ''.join(lines)
s += '\n## Twenty-eighth-hour integrated cusp, inner-star and overlap proofs\n\n'
s += (root / 'records/twenty_eighth_hour_research_report.md').read_text()
s += '''
The opening table is synchronized from all 49 coverage rows. This changes
no task outcome. The formal baseline has 308 statements: 264 Proved,
19 Refuted, 19 Open and 6 Known, with 113 bibliography entries. Both main
decisions remain Open. Final combined build and visible QA are recorded
separately and bound to the resulting PDF.
'''
p.write_text(s)
print('Integrated A85/A86/B135/B136/B137 byte-exactly:308 statements,264 Proved,113 references,49 task rows;both main decisions Open.')
