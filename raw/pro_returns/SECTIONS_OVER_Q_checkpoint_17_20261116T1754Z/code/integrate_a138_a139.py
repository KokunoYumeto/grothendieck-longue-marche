#!/usr/bin/env python3
"""Integrate the reviewed fixed-tower unit construction and small detector."""
from pathlib import Path
import datetime, json, subprocess
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
p=w/'SECTIONS_OVER_Q_paper.tex'
s=p.read_text()
anchor=r'\input{sections/harmonic_tripod_finite_obstruction.tex}'
entries=[r'\input{sections/constant_tower_unit_lift_agent.tex}',r'\input{sections/harmonic_cyclic_finite_obstruction.tex}']
assert anchor in s
for entry in entries:
    if entry not in s:s=s.replace(anchor,anchor+'\n'+entry,1)
    anchor=entry
p.write_text(s)
p=w/'notes/register_metadata.json'
meta=json.loads(p.read_text())
data={
'A.138':{
 'answers':'A5; A7; A8; A9; A12; A15; L9; L10; L14; L17; L20',
 'depends_on':'A.77 norm-family criterion; A.105 actual pure-three fields; single-prime inertia argument; Hilbert three-class fields; cyclic Hasse norm theorem; exact unit divisor correction',
 'uses_local_theorem':'no; the norm family is constructed directly on the fixed rational radicand tower',
 'manuscript_passages':'cote149; scans56–58,126–127; compatible unit cofactors and completed norm families',
 'notes':'On K_n=Q(3^(1/3^n)) the exact unit U=alpha_1²−2 extends through a compatible pro-three unit family U_n. Actual norm-compatible units v_n are constructed with v_1=U² by surjectivity of unit norms in the Galois splitting tower; unique half-powers are taken only in the pro-three completions. The single-prime inertia proof gives vanishing three-parts of the needed class groups, and ideal-divisor correction proves actual unit norm surjectivity. The first-depth quotient lambda_*kappa(U)=chi_9 is nonzero, proved by explicit S3 action and Frobenius61. The family beta_n=(1−alpha_n)U_n retains the canonical two-divisors. The radicand is fixed at3; changing it to an infinite-support coordinate remains open. Full root and local_preprint audits and independent certificate reruns passed.'},
'A.139':{
 'answers':'A5; A7; A8; A9; A12; A15; L2; L9; L10; L14; L17; L20',
 'depends_on':'A.134 completed harmonic triple; A.137 nonsplit central-extension descent; actual cyclic degree-eight cover; explicit Nielsen and Schreier maps',
 'uses_local_theorem':'no; actual quotient sections with precisely prescribed finite local images are excluded',
 'manuscript_passages':'cote149; scans56–58,126–127; completed tripod Kummer pairs and finite/metabelian section lifting',
 'notes':'The very same completed tripod pair of A137 is excluded by the actual geometric quotient Q_D=(C2)^8 semidirect C16 of order4096 and exact class8. Its degree-eight genus-three cover is W^8=t²(1−t)/(64a²), with literal inverse to W^4=T(T−1)(T−1/2)/a. The proper Brauer class (T−c,d) has invariant1/2 at2 and0 elsewhere on every local sheet above the specified centres. The exact Nielsen/Schreier isomorphism gives the quotient, the lamp-ideal recurrence gives its exact class, and Pi double-prime and Gamma9 both lie in K_D. The nonsplit arithmetic central descent gives the reciprocity contradiction. Full root and local_preprint source audits and independent finite certificate reruns passed. This identifies a detecting quotient, without asserting that class8 is the earliest obstruction or a universal bound for all ghosts.'}
}
meta.update(data)
p.write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
p=w/'SECTIONS_OVER_Q_report.md'
lines=p.read_text().splitlines()
details={
'A.138':'A.138 constructs a coherent nonzero unit cofactor on the fixed pure-three norm tower, through actual unit-norm surjectivity and pro-three half-powers. Its first-depth cyclotomic quotient is explicitly nonzero. A changed infinite-support radicand is still unresolved.',
'A.139':'A.139 sharpens the exclusion of the same completed tripod pair to an actual metabelian geometric quotient of order4096 and exact nilpotency class8; every local sheet and the nonsplit Brauer descent are proved.'}
for i,line in enumerate(lines[:55]):
    if not line.startswith('| '):continue
    cells=[z.strip() for z in line.strip().strip('|').split('|')]
    if len(cells)!=3:continue
    for key,record in data.items():
        if cells[0] not in {x.strip() for x in record['answers'].split(';')}:continue
        if key not in cells[1]:cells[1]+=', '+key
        if details[key] not in cells[2]:cells[2]+=' '+details[key]
    lines[i]='| '+' | '.join(cells)+' |'
heading='## A coherent unit family and a class-eight metabelian detector'
if heading not in lines:
    lines.extend(['',heading,'',stamp+': '+details['A.138']+' '+details['A.139'],
    'For A138, the fields L_n=Q(3^(1/3^n),mu_(3^n)) and their intervening cyclic cubic steps are ramified at one prime over three. Every inertia subgroup normally generates the finite three-group over Q(mu_3); its class number one forces total ramification. Applying this argument to each Hilbert three-class field proves its triviality. Global reciprocity and the cyclic norm theorem supply a field norm for each unit. An exact ideal-divisor correction, with class-group order prime to three and a Bezout identity, makes that preimage an actual unit. Norming the compatible splitting-field units to K_n and then taking the unique half-power in the pro-three completion produces the announced family. The precise first-depth quotient is calibrated at61.',
    'For A139, the morphism W=X0X1Xh gives a genus-three cyclic cover of degree eight over the tripod. The inverse formula T=1/2−4aW^4/t identifies it with the quartic product equation. Every local lift lies on T=T_p or T=1−T_p; the latter occurs only where minus one is a fourth power. At the two support primes admitting that sheet, the Brauer first entries are explicit squares. The central-extension argument of A137 therefore descends the same nonzero global invariant sum through the Frattini quotient of this smaller cover. The Nielsen basis u=xy^(−2), v=y identifies the quotient with (C2)^8 semidirect C16. Its lower-central dimensions are7,6,5,4,3,2,1,0. The weight-eight commutator is the sum of all eight lamp coordinates. The retained graph certificate verifies all4096 normal forms and8192 generator products.',
    'These proofs make concrete progress within the active open problems. Both A1 assertions remain open.',''])
p.write_text('\n'.join(lines)+'\n')
note=stamp+' A138 and A139 integrated after full root/local saved-source audits. Root independently reran both exact certificates. A138 proves actual unit norm surjectivity and a compatible pro-three family on the fixed tower, with exact cyclotomic quotient. A139 proves the smaller actual class8 metabelian detector for the same completed pair, including all local sheets and the nonsplit descent. Neither changes the open status of A1.\n'
for name in ['notes/hour9_root_audits.md','notes/root_progress.md']:
    p=w/name
    with p.open('a') as f:f.write('\n'+note)
r=subprocess.run(['python',str(w/'code/build_register.py')],check=True,text=True,capture_output=True)
out='Integrated A138 and A139.\n'+r.stdout
Path(__file__).with_name('integrate_a138_a139_output.txt').write_text(out)
print(out,end='')
