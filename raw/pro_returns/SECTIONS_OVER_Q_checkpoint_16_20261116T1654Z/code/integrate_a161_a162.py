#!/usr/bin/env python3
"""Integrate the audited elliptic lifting locus and changed-seed norm theorem."""
from pathlib import Path
import datetime
import json
import subprocess

w = Path(__file__).resolve().parents[1]
stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
records = {
    'A.161': {
        'answers': 'A5; A10; A15; L7; L10; L14',
        'depends_on': 'A.143 rank-two elliptic quotient; A.160 full Selmer classification; actual quadratic torsor and tangent maps; finite Kummer injections and compatible continuous cocycles',
        'uses_local_theorem': 'no; the exact domain consists of full Selmer sections with the specified zero torsor class',
        'manuscript_passages': 'cote149; scans56–58 and126–127; actual finite-cover lifting and compact Kummer comparison',
        'notes': 'The literal degree-two cover from D-open to E minus E[2] is W²=y/(36M), with inverse T=(x/1146+1)/2. Full Selmer sections with zero torsor class are exactly those admitting full Selmer lifts through this cover. A160 makes all of them cuspidal, and their full compact Kummer images are exactly the four rational two-torsion classes. The tangent lifting squareclasses are [M] at the finite two-torsion cusps and [-M] at infinity. All four occur. The completed Mordell–Weil formulation retains this precise section/lift domain; it does not assign sections to arbitrary completed points.',
        'detail': 'A.161 determines the full Selmer lifting locus through the actual quadratic cover of the rank-two elliptic quotient: every such section is cuspidal and its compact class is one of the four rational two-torsion classes. The exact tangent squareclasses and converse occurrence are proved.'
    },
    'A.162': {
        'answers': 'A5; A9; A15; L10; L14; L20',
        'depends_on': 'A.140 explicit pure-tower local Artin norm map; A.156 exact norm seed; explicit prime generators and residue characters; full decomposition group at three; Oki Proposition6.4 torus duality; split divisor sequences and snake map',
        'uses_local_theorem': 'no',
        'manuscript_passages': 'cote149; scans56–58 and126–127; fixed actual norm tower and the completed support obstruction',
        'notes': 'For d=649 and a=3d^24, put h11=11/(2+alpha)^3, h59=59/(2+2alpha-alpha²)^3, f=h11*h59², b1=(1-alpha)*f³ and b2=beta2*f. These actual S-units have exact norms b2 to b1 to -2. The literal tame uniformizer formula proves all-depth local norm membership, and compact local fibres or explicit archimedean factors give compatible local families. At every finite height, the global norm torus splits over Omega_m with decomposition group at3 equal to its whole Galois group; torus duality kills its Hasse norm kernel. Thus b2 has an actual global field-norm preimage at every height and the fixed triple extends through every finite height. A snake-map divisor quotient records the remaining completed S-unit obstruction. No single infinite global family or all-height fixed-support family is asserted.',
        'detail': 'A.162 changes the first seed explicitly and proves compatible local norm families at every place and an actual global field-norm preimage at every finite height in the same tower. An exact divisor quotient retains the unresolved completed fixed-support obstruction and infinite global compatibility question.'
    }
}

p = w/'SECTIONS_OVER_Q_paper.tex'
s = p.read_text()
anchor = r'\input{sections/harmonic_prym_full_sha.tex}'
inputs = ['harmonic_positive_rank_lift_classification.tex', 'two_inert_changed_seed_repair_agent.tex']
assert anchor in s and all((w/'sections'/name).exists() for name in inputs)
if not any(name in s for name in inputs):
    s = s.replace(anchor, anchor+'\n'+'\n'.join(r'\input{sections/'+name+'}' for name in inputs), 1)
else:
    assert all(name in s for name in inputs)
p.write_text(s)

p = w/'notes/register_metadata.json'
metadata = json.loads(p.read_text())
for ident, rec in records.items():
    metadata[ident] = {k:v for k,v in rec.items() if k != 'detail'}
p.write_text(json.dumps(metadata, indent=2, ensure_ascii=False)+'\n')

p = w/'SECTIONS_OVER_Q_report.md'
lines = p.read_text().splitlines()
assert lines[0] == 'INCOMPLETE'
for i, line in enumerate(lines[:55]):
    if not line.startswith('| '):
        continue
    cells = [x.strip() for x in line.strip().strip('|').split('|')]
    if len(cells) != 3:
        continue
    for ident, rec in records.items():
        if cells[0] in {x.strip() for x in rec['answers'].split(';')}:
            if ident not in cells[1]:
                cells[1] += ', '+ident
            if rec['detail'] not in cells[2]:
                cells[2] += ' '+rec['detail']
    lines[i] = '| '+' | '.join(cells)+' |'
heading = '## Continued work: the exact elliptic lifting locus and a changed norm seed'
if heading not in lines:
    lines.extend(['', heading, '', stamp+': '+records['A.161']['detail']+' '+records['A.162']['detail'], '',
        'The elliptic comparison is the actual finite etale cover W²=y/(36M). The torsor class supplies a fixed sheet, hence a full section lift, with point and cusp decomposition groups checked at every place. The harmonic full Selmer classification then gives the exact four compact two-torsion classes. Its continuous-cohomology formulation is justified by compatible finite cocycle representatives, and its tangent maps have the stated coefficients and completed square roots.',
        'The changed seed retains the actual tower a=3*649^24 and norm bottom -2. Multiplication by h11*h59² cancels the two stable cubic characters while changing the first-level element by its cube. Explicit uniformizers retain the nonzero valuations at11 and59 in every higher norm test. The unique three-adic decomposition group is the full splitting group, so the norm-torus localization kernel vanishes. This proves actual field-norm solvability at each finite height. The support quotient keeps track of the exact additional condition for a completed S-unit preimage. Its vanishing and a single infinite global family are still unresolved.',
        'Both principal A1 assertions remain open. The new statements are entered with their exact full-section, finite-height, and support scopes.', ''])
p.write_text('\n'.join(lines)+'\n')

audit = stamp+' A161/A162 integrated after complete root source reads, independent peer audits, and retained exact root certificate reruns. Root reopened Stoll Proposition3.6/3.7 and Oki Proposition6.4 in their primary PDFs. Oki applies to every torus split by the actual finite Galois extension, so D3=G kills the precise H2 restriction kernel. A161 includes the finite-cocycle compactness comparison; A162 includes compatible factors at every complex place. Full Selmer scope, fixed tower, remaining S-support quotient, and both open A1 assertions are retained.\n'
for name in ['notes/hour12_root_audits.md', 'notes/root_progress.md']:
    with (w/name).open('a') as f:
        f.write('\n'+audit)

p = w/'notes/hour12_typesetting_corrections.json'
corrections = json.loads(p.read_text())
for correction in corrections:
    correction['after'] = 'The third complete build through A160 has zero overfull hboxes/vboxes and no undefined references or citations; visual review remains due before checkpoint12.'
p.write_text(json.dumps(corrections, indent=2)+'\n')

proc = subprocess.run(['python', str(w/'code/build_register.py')], capture_output=True, text=True, check=True)
out = 'Integrated audited A161 and A162 with their precise scope and source comparisons.\n'+proc.stdout
Path(__file__).with_name('integrate_a161_a162_output.txt').write_text(out)
print(out, end='')
