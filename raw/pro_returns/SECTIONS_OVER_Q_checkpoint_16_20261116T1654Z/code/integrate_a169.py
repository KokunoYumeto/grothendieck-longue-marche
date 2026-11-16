#!/usr/bin/env python3
"""Integrate the fully audited metabelian classification in the fixed class."""
from pathlib import Path
import datetime
import json
import subprocess

w = Path(__file__).resolve().parents[1]
stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
record = {
    'answers': 'A1; A5; A10; L7; L10; L12',
    'depends_on': 'A.68 exact abelian-cover commutator intersection; A.160 full Prym Sha and finite local boundary support; A.163 proper boundary class; A.167 affine classification and exact downstairs deck action; Stoll Theorem3.11; proved number-field completed Kummer injection and finite-extension descent',
    'uses_local_theorem': 'no; actual local point/cusp matching is part of the stated quotient-section domain',
    'manuscript_passages': 'cote149; scans54–58 and126–127; specified-class full-metabelian section and actual cusp-packet comparison',
    'notes': 'Every continuous full-metabelian tripod section locally matching actual point/cusp sections and satisfying the specified combined mod8 class [64a^2] is the image of an actual full rational cusp section. On the selected D sheet its class is uniquely (P,tau) with four rational boundary labels and tau in completed Q×. Downstairs precisely tau and -tau are identified by the actual rational deck action. The proof uses the actual H_n=ker(Pi→Pi_ab/n), n=8j!, literal Fermat-to-D maps and coherent transitions, Stoll3.11 on each finite boundary fibre, nonsplit boundary-module recovery via completed Kummer injectivity over number fields, and one compact nested family of conjugators in H/Pi-double-prime. Both principal assertions for arbitrary full sections and the other Kummer classes remain open.'
}

p = w / 'SECTIONS_OVER_Q_paper.tex'
s = p.read_text()
anchor = r'\input{sections/two_inert_raw_two_class_obstruction.tex}'
new = r'\input{sections/harmonic_full_metabelian_classification.tex}'
assert anchor in s
if new not in s:
    s = s.replace(anchor, anchor + '\n' + new, 1)
p.write_text(s)

p = w / 'notes/register_metadata.json'
meta = json.loads(p.read_text())
meta['A.169'] = record
p.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + '\n')

p = w / 'SECTIONS_OVER_Q_references.bib'
s = p.read_text()
old = 'Propositions 3.6 and 3.7, Theorem 6.4 with its geometric-cover comparison'
new_bib = 'Propositions 3.6 and 3.7, Theorem 3.11 on an arbitrary finite subscheme (printed page 11), Theorem 6.4 with its geometric-cover comparison'
assert old in s or new_bib in s
s = s.replace(old, new_bib)
s = s.replace('Proposition 3.6 has no Tate--Shafarevich finiteness hypothesis.', 'Proposition 3.6 and Theorem 3.11 have no Tate--Shafarevich finiteness hypothesis; the latter proof and its finite-extension descent were reopened for A.169.')
p.write_text(s)

detail = 'A.169 completes the full-metabelian classification in the specified combined mod8 class: every locally point/cusp-matching section is an actual full cusp image. Its exact downstairs classes are four copies of completed Q× modulo multiplication by -1.'
p = w / 'SECTIONS_OVER_Q_report.md'
lines = p.read_text().splitlines()
assert lines[0] == 'INCOMPLETE'
answers = {x.strip() for x in record['answers'].split(';')}
for i, line in enumerate(lines[:55]):
    if not line.startswith('| '):
        continue
    cells = [x.strip() for x in line.strip().strip('|').split('|')]
    if len(cells) != 3 or cells[0] not in answers:
        continue
    if 'A.169' not in cells[1]:
        cells[1] += ', A.169'
    if cells[0] == 'A1':
        cells[2] = 'Open: neither general full assertion over Q is established. A.160 proves full Prym Sha finiteness and classifies full Selmer sections in the specified combined mod8 class. A.169 proves the exact full-metabelian classification in that class under actual local point/cusp matching, with unique selected-cover cusp and completed tangent, and the precise downstairs sign identification. Both principal assertions outside these proved scopes remain open.'
    elif detail not in cells[2]:
        cells[2] += ' ' + detail
    lines[i] = '| ' + ' | '.join(cells) + ' |'
heading = '## Continued work: full metabelian classification in the specified class'
if heading not in lines:
    lines.extend(['', heading, '', stamp + ': ' + detail, '',
        'The new proof retains only actual abelian covers of the tripod, so each affine-cover quotient receives the full metabelian extension. Their equations and maps to D are given explicitly. Stoll Theorem3.11 determines the proper boundary point on each cover even when its boundary fibre is not split over Q. A proved completed Kummer localization injection over every number field, together with a literal finite-extension cocycle inverse, recovers the unique inertia parameter in the nonsplit boundary module. Pushing these full cusp sections to D recovers one fixed full cusp packet and parameter. Nested nonempty closed conjugator sets in the same compact group then identify the given section in the full metabelian quotient itself. The exact deck centralizer proves that only multiplication by -1 identifies the selected-cover parameters downstairs.', '',
        'The root and both independent peers read the complete proof. The exact map certificate and independent reruns passed. This result answers the stated quotient problem in the specified class; arbitrary Kummer classes, the general full section conjecture, and universal birational lifting remain on the open list.', ''])
p.write_text('\n'.join(lines) + '\n')

audit = stamp + ' A169 integrated after full root, local and birational proof audits, exact certificate reruns and root reopening of Stoll3.11. Selected-cover and downstairs conjugacies, nonsplit inertia recovery and the compact inverse limit all passed.\n'
for name in ['notes/hour13_root_audits.md', 'notes/root_progress.md']:
    with (w / name).open('a') as f:
        f.write('\n' + audit)
proc = subprocess.run(['python', str(w / 'code/build_register.py')], capture_output=True, text=True, check=True)
out = 'Integrated audited A169.\n' + proc.stdout
Path(__file__).with_name('integrate_a169_output.txt').write_text(out)
print(out, end='')
