#!/usr/bin/env python3
"""Integrate the audited fixed-coordinate image and escaping-support construction."""
from pathlib import Path
import datetime
import json
import subprocess

w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
p=w/'SECTIONS_OVER_Q_paper.tex'
s=p.read_text()
anchor=r'\input{sections/stable_local_norm_agent.tex}'
assert anchor in s
for source in ['fixed_local_completion_image.tex','harmonic_escaping_support.tex']:
    entry='\\input{sections/'+source+'}'
    if entry not in s:s=s.replace(anchor,anchor+'\n'+entry,1)
    anchor=entry
p.write_text(s)

p=w/'notes/register_metadata.json'
meta=json.loads(p.read_text())
meta['A.132']={
 'answers':'A8; A9; A12; A15; L2; L14; L17; L20',
 'depends_on':'A.10; A.55; A.76; A.85; A.128; finite-coefficient Poitou–Tate exact localization sequence',
 'uses_local_theorem':'no; exact multiplicative groups, finite Kummer theory and global duality',
 'manuscript_passages':'cote149; scans56–58,126–127; all-place coordinate matching for a rational puncture',
 'notes':'Proves injectivity at each rational finite-power quotient using every finite valuation and the dyadic sign, and an exact equality between the completed diagonal image and all-place finite matching for one fixed local family. Finite representatives are unique and automatically compatible. Gives the exact restricted-product and character-orthogonality criterion, and literal convergent local Euler products for ordinary integer valuations. The actual finite restriction maps explain what A85 initialization supplies. Root full proof audit and retained executed certificate passed.'
}
meta['A.133']={
 'answers':'A5; A8; A9; A12; A15; L2; L9; L14; L17; L20',
 'depends_on':'A.80; A.83; A.85; A.90 exact mixed root stabilizers; A.128; A.132; Chebotarev and good-reduction curve bound',
 'uses_local_theorem':'no; explicit Kummer-cover maps, actual ordinary local points and field reciprocity',
 'manuscript_passages':'cote149; scans56–58,126–127; completed harmonic Kummer data and one new puncture',
 'notes':'Constructs one ordinary completed harmonic triple at old punctures0,1,1/2, with initial rational centre1/4 and infinite support in every old coordinate. At new puncture2 every finite common field is Q(sqrt2,sqrt−3), all initialization obstruction elements vanish and every finite list of prescribed old points lifts through an everywhere locally soluble augmented cover. Infinitely many separately allocated primes have fixed centre2+p and valuation one at the new coordinate, so the one fixed all-place tuple has no global squareclass there. The exact mixed-coordinate maps preserve the required root symbols and fixed centres. Includes an effective choice convention. No fundamental-group section is inferred. Root proof audit and exact finite certificate passed.'
}
p.write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')

p=w/'SECTIONS_OVER_Q_report.md'
lines=p.read_text().splitlines()
items={'A5','A8','A9','A12','A15','L2','L9','L14','L17','L20'}
detail=('A.132 identifies the exact completed diagonal image: finite matching at every place for the same local family forces unique compatible coefficients. A.133 constructs a harmonic completed triple with every finite common-character obstruction zero and every finite prescribed-point initialization possible, but no new squareclass at puncture2 for its fixed all-place centres; infinitely many forced centres2+p have valuation one.')
changed=0
for i,line in enumerate(lines[:55]):
    if not line.startswith('| '):continue
    cells=[z.strip() for z in line.strip().strip('|').split('|')]
    if len(cells)!=3 or cells[0] not in items:continue
    for identifier in ['A.132','A.133']:
        if identifier not in cells[1]:cells[1]+=', '+identifier
    if detail not in cells[2]:cells[2]+=' '+detail
    lines[i]='| '+' | '.join(cells)+' |'
    changed+=1
heading='## Exact fixed-coordinate completion and harmonic escaping support'
if heading not in lines:
    lines.extend(['',heading,'',stamp+': '+detail,
    'The new distinction is proved by explicit maps. The restriction map from one all-place tuple to its coordinates at finitely many places sends the A133 tuple into every finite initialization image. The entire tuple lies outside the all-place image already modulo two. A132 proves that, once the latter image membership holds at every exponent, injectivity makes all exponent transitions automatic. Thus no extra inverse-limit obstruction is claimed after fixed all-place finite matching.',
    'The escaping-support construction begins at the literal rational harmonic point1/4, retains the fixed old boundary quadratic fields and root-symbol invariants, and adds a fresh prime splitting the current fibre at2 and all old boundary fields. Hensel lifting fixes the centre2+p there permanently. Actual mixed-power maps refine the three old coefficients through cofinal factorial exponents; a separate fresh prime at each refinement gives infinite support for each old coordinate. The retained program executes15 split-prime examples and180 root lifts,512 mixed genus bounds and the coefficient, cofinality, local-product and valuation identities. The infinite recursion is proved and its finite choices specified; no infinite computation is claimed. The construction alone asserts no fundamental-group section.',''])
p.write_text('\n'.join(lines)+'\n')

audit=('A132 and A133 root full audits passed: all-place finite Kummer injection including the dyadic sign; automatic exponent compatibility; exact character image and convergent ordinary local products; all four fixed boundary squareclass fields; mixed-exponent genus and stabilizer maps; every unit-root and symbol invariant; Hensel-preserved forced centres; cofinal factorial classes and retained ordinary integer valuations; finite initialization through literal power maps; infinite valuation-one exclusion. Root independently reran the retained certificate:10000 valuation/sign instances,29075 finite transitions,5206 local tail congruences,four squareclass spans,576 coordinate identities,512 genus bounds,1829 cofinality identities,15 split primes,180 actual root lifts,75 root-precision instances and60 finite support exclusions; all passed. A128 concluding scope was updated to reference the exact restriction maps and avoid suggesting an additional inverse-limit obstruction after all-place finite matching.')
for name in ['notes/hour9_root_audits.md','notes/root_progress.md']:
    p=w/name
    s=p.read_text() if p.exists() else '# Ninth-hour root audits\n'
    if audit not in s:p.write_text(s+'\n'+stamp+' '+audit+'\n')

result=subprocess.run(['python',str(w/'code/build_register.py')],check=True,text=True,capture_output=True)
out=f'Integrated A132 and A133 in numerical order; updated {changed} outcome rows.\n'+result.stdout+'Both A1 assertions remain open.\n'
Path(__file__).with_name('integrate_a132_a133_output.txt').write_text(out)
print(out,end='')
