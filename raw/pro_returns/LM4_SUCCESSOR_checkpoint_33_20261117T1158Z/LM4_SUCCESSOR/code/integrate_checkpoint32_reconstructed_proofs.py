"""Integrate fourteen newly reviewed reconstructions, preserving the restored31 files."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv, hashlib, json, re, shutil, subprocess, sys

root = Path(__file__).resolve().parents[1]
read = lambda rel: (root / rel).read_text()
review = json.loads(read('records/checkpoint32_root_formal_reviews.json'))
assert review['status'] == 'PASS_COMPLETE_SOURCE_REVIEW'
copies = review['copies']
expected = ['A.' + str(n) for n in range(95, 103)] + ['B.' + str(n) for n in range(155, 161)]
assert [row['statement'] for row in copies] == expected
for row in copies:
    data = (root / row['source']).read_bytes()
    assert hashlib.sha256(data).hexdigest() == row['sha256']
    assert not any(c < 32 and c not in (9, 10) for c in data)
    assert not (root / row['target']).exists()
for rel, digest in review['independent_reviews'].items():
    assert hashlib.sha256((root / rel).read_bytes()).hexdigest() == digest

paper = read('LM4_SUCCESSOR_paper.tex')
anchor = r'\input{sections/a_affine_character_pentagon.tex}'
assert paper.count(anchor) == 1
paper = paper.replace(anchor, anchor + '\n' + '\n'.join(
    r'\input{' + row['target'] + '}' for row in copies if row['statement'].startswith('A.')))
old = 'whose abelianization compares two specified full units. Neither that\nunit equality nor the full word identity is established.'
new = ('whose abelianization compares two specified full units. For actual\n'
       'full-GT involutions the full unit equality is now proved; the full\n'
       'nonlinear word identity remains open.')
assert paper.count(old) == 1
paper = paper.replace(old, new)
old = 'comparison; the remaining scalar condition is exactly all odd cyclic\nheads.'
new = ('comparison. An actual sphere-kernel affine construction proves the\n'
       'remaining equality at every odd cyclic head, and a finite-ring\n'
       'version proves vanishing of the entire Alexander hexagon class,\n'
       'including every even head and its nilpotent coefficient layers.')
assert paper.count(old) == 1
paper = paper.replace(old, new)
anchor = 'swap duality. Canonical realization and the nonlinear word remain open.'
assert paper.count(anchor) == 1
paper = paper.replace(anchor, anchor + '\n'
    'The original sphere quotient retains its primitive rank-three kernel.\n'
    'The actual negative involution has a full based correction of integral\n'
    'abelian class minus the specified generator, and explicit cabling\n'
    'arrows identify its regular cusp frame. Every marked odd-boundary\n'
    'cover retains its entire free pro-two Schreier kernel, all signed\n'
    'index wraps, and this same original correction. These are statements\n'
    'before any further square or nilpotent filling.')
anchor = 'The remaining local fixed-kernel generation is not\nimplied.'
assert paper.count(anchor) == 1
paper = paper.replace(anchor, anchor + '\n'
    'The unique fixed coset gives an ordinary paired-free relative kernel\n'
    'with one cone factor, and its full family-indexed basis retains all\n'
    'deleted cores and actual nodal connectors. The fixed-source section\n'
    'already exists before filling, with an exact crossed involution defect\n'
    'and a minimal invariant defect filling. Separately, recursive degree-five\n'
    'heads and solvable source images are not cofinal. Every actual\n'
    'characteristic finite nilpotent Birman target is abelian and has only\n'
    'a two-element source action, excluding the required affine stabilizer\n'
    'condition for a specified alternating-group source quotient.')

part_b = read('sections/part_B.tex')
for row in copies:
    if row['statement'].startswith('B.'):
        part_b += r'\input{' + row['target'] + '}\n'
with (root / 'task_coverage.csv').open(newline='') as stream:
    reader = csv.DictReader(stream)
    fields, tasks = reader.fieldnames, list(reader)
assert len(tasks) == 49
old_outcomes = [(row['task'], row['outcome']) for row in tasks]
for row in tasks:
    if row['task'] in {'A.7', 'A.8'}:
        for sid in expected[:8]:
            assert sid not in row['statement_ids'].split(';')
            row['statement_ids'] += ';' + sid
        row['state'] += ' Reconstructed formal cycle32: A95–A102 prove the specified center-free-head boundary, actual sphere/free-kernel and relative pro-two topology, original involution and full cabling correction, exact regular cusp bridge, full-GT integral coefficient equality, full-ring three-cover Alexander vanishing, and the entire marked odd-boundary Schreier kernel with the original involution.'
        row['approaches'] += ' Reversible original sphere presentation; full based cabling arrows; characteristic finite-two targets; finite-ring affine pentagon with weighted fourth-pair coefficient; every CRT thickening and signed Schreier wrap.'
        row['obstruction'] = 'For actual full-GT involutions the full scalar equality and full Alexander hexagon class are settled. The nonlinear full-word criterion and canonical conjugacy remain open. No full-GT pentagon is supplied for arbitrary GT0 canonical data. The separately normalized actual CM parity comparison remains open.'
        row['next_step'] = 'Use the new actual affine signed mod-three/mod-twelve research proof and original CM frame definitions to determine the remaining comparison, while retaining the full nonlinear cusp and genuine canonical-realization gates.'
    if row['task'] in {'B.4', 'B.4.a', 'B.4.b', 'B.4.c', 'B.4.h'}:
        for sid in expected[8:]:
            assert sid not in row['statement_ids'].split(';')
            row['statement_ids'] += ';' + sid
        row['state'] += ' Reconstructed formal cycle32: B155–B160 give the exact single-fixed-coset paired kernel, full deleted-family basis and actual connectors, noncofinal recursive dihedral heads, the solvable-source/affine-stabilizer boundary, a generic marked section with its exact crossed defect and minimal invariant filling, and exclusion of all actual characteristic finite nilpotent Birman targets for the specified A5 neighborhood.'
        row['approaches'] += ' Ordinary Kurosh and full actual-closure comparison; exact coset star; marked generic section and crossed defect; all-depth wreath-product prime support; explicit A5 quotient; actual mixed-braid action on all abelian coordinates.'
        row['obstruction'] = 'The actual remaining fixed kernel is not yet proved generated by the three contact orbits. The new continuous cohomology research identifies the correct contact-image equality, not injectivity of the whole map. Other necks, full-base transfer, and the original B75 uniform finite-neighborhood condition remain open. Nonnilpotent targets are not excluded.'
        row['next_step'] = 'Compare the exact continuous cohomology kernel with the closure of the three whole contact-orbit images; retain every actual node and connector. In parallel attack the original B75 uniform identity-stabilizer criterion with genuinely realized nonnilpotent targets.'
assert [(row['task'], row['outcome']) for row in tasks] == old_outcomes
assert all(next(row for row in tasks if row['task'] == t)['outcome'] == 'Open' for t in ('A.8', 'B.4'))

report = read('LM4_SUCCESSOR_report.md')
assert report.splitlines()[0] == 'INCOMPLETE'
lines = report.splitlines(True)
start = next(i for i,line in enumerate(lines) if line.startswith('| Task or lead |'))
end = start
while end < len(lines) and lines[end].startswith('|'):
    end += 1
cell = lambda s: s.replace('|', r'\|').replace('\n', ' ')
lines[start:end] = ['| Task or lead | Statements | Outcome and exact state |\n', '|---|---|---|\n'] + [
    '| ' + cell(row['task']) + ' | ' + cell(row['statement_ids']) + ' | **' + cell(row['outcome']) + '** — ' + cell(row['state']) + ' |\n' for row in tasks]
report = ''.join(lines) + '\n\n' + read('records/thirty_second_hour_research_report.md')

backup = root / 'records/pdf_qa/checkpoint32_recovered31_before_integration'
assert not backup.exists()
paths = ['LM4_SUCCESSOR_paper.' + ext for ext in ('pdf','tex','log','aux','bbl','blg','toc','out')]
paths += ['LM4_SUCCESSOR_results.csv','LM4_SUCCESSOR_references.bib','LM4_SUCCESSOR_report.md','task_coverage.csv','sections/part_B.tex','sections/b_sources.bib','code/assemble_register.py']
paths += [str(p.relative_to(root)) for p in (root/'records').glob('build_*.log')]
for rel in paths:
    src = root / rel
    if src.is_file():
        suffix = '.retained.txt' if src.suffix in {'.aux','.bbl','.blg','.toc'} else ''
        dst = backup / (rel + suffix)
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
for row in copies:
    (root/row['target']).write_bytes((root/row['source']).read_bytes())
(root/'LM4_SUCCESSOR_paper.tex').write_text(paper)
(root/'sections/part_B.tex').write_text(part_b)
(root/'sections/b_sources.bib').write_text(read('sections/b_sources.bib') + '\n' + read('work_DE/B160_primary32.bib'))
(root/'LM4_SUCCESSOR_report.md').write_text(report)
with (root/'task_coverage.csv').open('w',newline='') as stream:
    writer=csv.DictWriter(stream,fieldnames=fields);writer.writeheader();writer.writerows(tasks)
(root/'records/checkpoint32_formal_source_copies.json').write_text(json.dumps({
    'integrated_at':datetime.now(timezone.utc).isoformat(),'copies':copies,
    'comparison':'Every integrated source is byte-identical to its reviewed reconstruction. Lost pre-outage hashes are not current identities.'},indent=2)+'\n')
subprocess.run([sys.executable,str(root/'code/assemble_register.py')],check=True)
rows=list(csv.DictReader((root/'LM4_SUCCESSOR_results.csv').open()))
assert len(rows)==347 and dict(Counter(row['status'] for row in rows))=={'Known':6,'Proved':303,'Refuted':19,'Open':19}
assert len(re.findall(r'^@',read('LM4_SUCCESSOR_references.bib'),re.M))==115
print('Integrated14 newly reviewed reconstructions:347 statements,303 Proved,115 references,49 tasks; both mains and actual CM parity Open.',flush=True)
