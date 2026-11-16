#!/usr/bin/env python3
"""Integrate the audited Prym descent and the two-prime class quotient."""
from pathlib import Path
import datetime,json,subprocess
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
p=w/'SECTIONS_OVER_Q_paper.tex';s=p.read_text()
anchor=r'\input{sections/coherent_inert_radicand_update_agent.tex}'
entries=[r'\input{sections/harmonic_prym_selmer.tex}',r'\input{sections/two_inert_prime_class_limit_agent.tex}']
assert anchor in s
for e in entries:
    if e not in s:s=s.replace(anchor,anchor+'\n'+e,1)
    anchor=e
p.write_text(s)
records={
'A.150':{
 'answers':'A5; A10; A15; L7; L10; L14',
 'depends_on':'A.139 harmonic proper curve; A.143 original elliptic map; exact two involutions and divisor pushforwards; complete odd and dyadic two-isogeny descent; Milne EC2021 IV finite basis theorem p105',
 'uses_local_theorem':'no; explicit proper morphisms, local point tests and finite squareclass calculations',
 'manuscript_passages':'cote149; scans56–58; actual elliptic quotient maps and lifting tests',
 'notes':'Over K=Q(sqrt2), two actual degree-two quotient maps identify the complementary Prym factor up to the displayed isogeny with E_b times its conjugate, b=1146(1+sqrt2)^2 M^2. The literal conjugation isomorphism has cocycle [-1], forcing even K-rank. Exact two-isogeny Selmer groups have sizes64 and4, with displayed squareclass bases; all odd local conditions are sufficient and all ten dyadic residue witnesses lift by a strict Hensel bound. Hence rank is in {0,2,4,6}. No global points are inferred from Selmer survivors. Full root and independent audits and reruns passed.'},
'A.151':{
 'answers':'A5; A9; A15; L9; L10; L14; L20',
 'depends_on':'A.149 ray-class/inertia comparison; explicit cubic field Q(mu3,649^(1/3)); local Kummer root extraction; Milne CFT V1.7/3.3/3.5/3.6; finite PT and Shapiro',
 'uses_local_theorem':'no; explicit class fields and local radical maps',
 'manuscript_passages':'cote149; scans56–58,126–127; coherent norm towers and class obstructions',
 'notes':'For a=3*11^M1*59^M2 with positive multiples24, the fixed cubic F=Q(mu3,649^(1/3)) is disjoint from every radical-cyclotomic L_n by the exact total ramification at3. Beyond n0=1+max v3(Mi), F L_n/L_n is everywhere unramified and split at S above2,3,11,59,infinity. Its literal Artin maps give compatible onto S-class three-primary quotients and an onto inverse-limit quotient C3. The actual old exponent24 cover has unit points everywhere for M1=M2=24. No particular target norm obstruction value is inferred. Root and independent full audits and reruns passed; root-of-unity adjustment and the abelian-compositum hypothesis for the norm diagram are explicit.'}}
p=w/'notes/register_metadata.json';m=json.loads(p.read_text());m.update(records);p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
p=w/'SECTIONS_OVER_Q_references.bib';s=p.read_text()
new=(w/'notes/harmonic_prym_references.bib').read_text()
if '@book{AgentMilneEC2021,' not in s:s+='\n'+new+'\n'
needle='V Theorems1.7,3.5,3.6 were reopened for A.149: the ray class exact sequence and its abelian extension correspondence, with the inert eleven-prime modulus.'
extra=' V Proposition3.3, printed p.157, was independently reopened for A.151; its abelian-compositum hypothesis is verified before applying the ideal norm--Artin diagram.'
if extra.strip() not in s:
    assert needle in s;s=s.replace(needle,needle+extra,1)
p.write_text(s)
details={
'A.150':'A.150 gives the actual complementary Prym maps over Q(sqrt2), exact two-isogeny Selmer sizes64 and4, and the unconditional rank set {0,2,4,6}.',
'A.151':'A.151 constructs a compatible onto cubic S-class quotient in the explicit two-inert-prime tower; the particular target pairing remains uncomputed.'}
p=w/'SECTIONS_OVER_Q_report.md';lines=p.read_text().splitlines()
for i,line in enumerate(lines[:55]):
    if not line.startswith('| '):continue
    cells=[x.strip() for x in line.strip().strip('|').split('|')]
    if len(cells)!=3:continue
    for ident,rec in records.items():
        if cells[0] in {x.strip() for x in rec['answers'].split(';')}:
            if ident not in cells[1]:cells[1]+=', '+ident
            if details[ident] not in cells[2]:cells[2]+=' '+details[ident]
    lines[i]='| '+' | '.join(cells)+' |'
heading='## Continued work: complementary Prym descent and the two-prime class character'
if heading not in lines:
    lines.extend(['',heading,'',stamp+': '+details['A.150']+' '+details['A.151'],'',
    'The two Prym maps are the literal invariant functions x=aW^2/T and y=aW(T±1/sqrt2)/T. Their inverse quadratic equations and independent invariant differentials prove the degree-two quotient maps and the Jacobian isogeny. Integral scaling gives b=1146(1+sqrt2)^2 M^2. The conjugation isomorphism has square [-1] as a semilinear map, which proves rank parity. Every supported global squareclass is enumerated. At odd places the exact valuation and residue conditions are sufficient; at the dyadic place each surviving residue witness has error depth at least13 and a derivative of depth at most6. Thus the complete local intersection computes Selmer groups themselves, while global solubility and the exact rank remain under investigation.',
    'In the norm direction, the two inert primes11 and59 leave one ray-class cubic after quotienting their two residue characters by global mu3. The explicit field Q(mu3,649^(1/3)) splits at2 and3 and becomes split at the two support primes in the deep radical tower. It remains globally disjoint from every layer, whose entire three-adic decomposition group is totally ramified. The resulting nonzero S-class characters commute with the actual ideal norms and survive in the inverse limit. Their Shapiro images and finite PT duals are stated with their actual coefficient modules. No value of the original target obstruction is asserted.',
    'Both principal A1 assertions remain open. Higher-descent software experiments are retained separately; their unverified rank or pairing outputs are excluded from these theorem statements.',''])
p.write_text('\n'.join(lines)+'\n')
audit=stamp+' A150/A151 full root audits PASS. A150: both invariant fields, exact differential formula, boundary orders, integral scaling, conjugation cocycle, two isogenies and square-root inverse, twisting interpretation, all supported squareclasses, local sufficiency, dyadic Hensel bounds, complete finite spans, rank factor4 and parity checked. Consolidated certificate independently rerun. Milne EC2021 IV unnumbered finite basis theorem printed p105 reopened. A151: ray quotient, split local cubes, full three-adic closure and inertia, root-of-unity-adjusted extraction, every local splitting, actual Artin norm identity, compatible finite-fibre compactness, Shapiro and finite PT scope checked. Exact certificate independently rerun; Milne CFT V3.3 reopened and its abelian hypothesis verified.\n'
for name in ['notes/hour11_root_audits.md','notes/root_progress.md']:
    with(w/name).open('a')as f:f.write('\n'+audit)
r=subprocess.run(['python',str(w/'code/build_register.py')],check=True,capture_output=True,text=True)
out='Integrated audited A150 and A151.\n'+r.stdout
Path(__file__).with_name('integrate_a150_a151_output.txt').write_text(out);print(out,end='')
