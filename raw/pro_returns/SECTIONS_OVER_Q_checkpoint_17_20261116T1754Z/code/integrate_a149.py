#!/usr/bin/env python3
"""Integrate the fully audited coherent changed-radicand norm construction."""
from pathlib import Path
import datetime,json,subprocess
w=Path(__file__).resolve().parents[1];stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
p=w/'SECTIONS_OVER_Q_paper.tex';s=p.read_text()
anchor=r'\input{sections/harmonic_unit_scalar_obstruction.tex}'
entry=r'\input{sections/coherent_inert_radicand_update_agent.tex}'
assert anchor in s
if entry not in s:s=s.replace(anchor,anchor+'\n'+entry,1)
p.write_text(s)
record={
 'answers':'A5; A9; A15; L9; L10; L14; L20',
 'depends_on':'A.77/A.81 actual root-torsor module and Shapiro norms; A.140 wild norm family; exact F121 tame norm calculation; ray class field theory; finite3-group inertia argument; Milne ADT I4.10(a)/4.15; continuous coefficient Milnor sequence',
 'uses_local_theorem':'no; actual global/local class fields, finite-coefficient duality and norm maps are used',
 'manuscript_passages':'cote149; scans56–58,126–127; compatible norms after an actual changed radicand',
 'notes':'For a-prime=3*11^24 and rho_n^(3^n)=a-prime, there exists a compatible family of completed S_n-units b_n, S_n over2,3,11,infinity, with b_1=(1-alpha)(alpha²-2)11/(2+alpha)^3 and Norm_Q b_n=-2. Eleven is inert in Q(mu3), and its residue group has three-part exhausted by mu3. The ray-class sequence kills abelian3 extensions ramified only there; the finite3-group maximal-subgroup argument makes inertia at3 the full group in every radical-cyclotomic layer and kills its3-class group. A finite-module local-witness argument then gives Sha1=0, finite PT gives H2 localization injectivity, and finite-S finite H1 removes the diagonal coefficient/augmentation Milnor term. Exact permutation Shapiro maps produce one global compatible norm family and o_pol(a-prime,-2)=0. The old exponent24 cover retains its rational centre3 and a unit point at11. No ordinary completed-pair or full metabelian lift is claimed. Full saved-source root/local audits and independent960 stable-symbol/465 coefficient-projection checks passed.'}
p=w/'notes/register_metadata.json';m=json.loads(p.read_text());m['A.149']=record;p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
detail='A.149 constructs a compatible completed global S-unit norm family in the explicit changed tower for a-prime=3*11^24, retaining its prescribed first representative and norm-2 over Q; the actual one-variable obstruction vanishes.'
p=w/'SECTIONS_OVER_Q_report.md';lines=p.read_text().splitlines()
for i,line in enumerate(lines[:55]):
    if not line.startswith('| '):continue
    cells=[x.strip() for x in line.strip().strip('|').split('|')]
    if len(cells)!=3 or cells[0] not in {x.strip() for x in record['answers'].split(';')}:continue
    if 'A.149' not in cells[1]:cells[1]+=', A.149'
    if detail not in cells[2]:cells[2]+=' '+detail
    lines[i]='| '+' | '.join(cells)+' |'
heading='## Continued work: a compatible global family in the changed tower at eleven'
if heading not in lines:lines.extend(['',heading,'',stamp+': '+detail,'',
    'The first representative is beta=(1-alpha)(alpha²-2)11/(2+alpha)^3, alpha³=3. Its exact divisor has coefficients-2 and1 on the degree-one and degree-two eleven-primes, with weighted norm zero. At the quadratic place the cubic characters of alpha,1-alpha,U are1,0,2 and the stable symbol is8*2-1=0 modulo3. The original U cofactor is retained. The new coefficient ratio is11^24; the finite exponent24 cover has the stated rational point and an ordinary unit point at11.',
    'The global compatibility proof uses the actual splitting layers L_n=Q(rho_n,mu_{3^n}). The ray class group of Q(mu3) with modulus supported only at its inert eleven-prime has no3-part, because the residue group has order120 and global mu3 exhausts its3-part. In every finite Galois3 extension ramified only at3 and11, inertia at3 is the full group. Applying this to the canonical Hilbert3 class fields proves Cl(L_n){3}=0. For a finite coefficient module split by such a layer, a locally trivial cocycle restricts to an everywhere unramified3-character there and therefore vanishes; the full decomposition group at3 makes its local coboundary witness global.',
    'Finite Poitou–Tate duality now makes H2 localization injective over the one fixed finite set S. Each diagonal finite quotient of the actual norm-kernel module receives a map from a sufficiently deep permutation augmentation kernel. The proved local norm preimages kill its defect, hence the defect is globally zero at every finite quotient. Finiteness of finite-S H1 removes the coefficient inverse-limit term. The resulting single continuous H1 class projects, through the exact permutation Shapiro maps, to the compatible completed S-unit family. This proves global compatibility in the displayed changed tower rather than selecting unrelated finite-height solutions.',
    'The original q=511177 tower of A144 still has its separate unproved global inverse-family question. The q=11 theorem is a completed norm-family result with rational coefficients; it does not assert an ordinary completed unit-equation pair or a full metabelian lift. Iterating compatible updates to an actual infinite-support ordinary pair remains a concrete next step. Both main A1 assertions remain open.',''])
p.write_text('\n'.join(lines)+'\n')
p=w/'SECTIONS_OVER_Q_references.bib';s=p.read_text()
needle='I, Lemma 4.9 and Theorem 4.10(b), with the restricted-product definition on printed page55, reopened for the exact all-place finite Kummer image in A.132.'
extra=' I, Theorem4.10(a), printed p.57, and Corollary4.15, printed p.62, were independently reopened for A.149: perfect duality of the finite localization kernels and finiteness for a finite ramification set with3 inverted.'
if 'independently reopened for A.149' not in s:
    assert needle in s;s=s.replace(needle,needle+extra,1)
needle='V Theorem5.3 (global reciprocity, printed pp.178--179) and VIII Theorem3.1 (cyclic Hasse norm theorem, printed p.234) were reopened for A.147, with the exact principal-idele and local-to-global norm maps.'
extra=' V Theorems1.7,3.5,3.6 were reopened for A.149: the ray class exact sequence and its abelian extension correspondence, with the inert eleven-prime modulus.'
if 'were reopened for A.149: the ray' not in s:
    assert needle in s;s=s.replace(needle,needle+extra,1)
p.write_text(s)
audit=stamp+' A149 full root and independent saved-source audits PASS. Root reran all arithmetic certificates and reopened Milne CFT V1.7 and ADT I4.10(a)/4.15. Checked inert ray group and all higher conductor kernels, normal-closure/maximal-subgroup inertia argument, canonical Hilbert3 extension and intermediate class-group transfer; every local norm algebra at2,3,11,real/complex; exact finite-module cocycle witnesses and full three-decomposition map; Cartier dual splitting fields; stable diagonal coefficients, finite local kernel maps, finite-S H1/Milnor control; explicit V inverse permutation topology, compact nested cosets, cochain sections, Shapiro/corestriction and exact S_{j+1} indexing. Existence phrasing makes no uniqueness claim. The theorem retains its rational-coefficient one-variable scope and prescribed beta; no ordinary pair or full metabelian section is inferred.\n'
for name in ['notes/hour10_root_audits.md','notes/root_progress.md']:
    with(w/name).open('a')as f:f.write('\n'+audit)
r=subprocess.run(['python',str(w/'code/build_register.py')],check=True,capture_output=True,text=True)
out='Integrated audited A149.\n'+r.stdout
Path(__file__).with_name('integrate_a149_output.txt').write_text(out);print(out,end='')
