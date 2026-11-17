#!/usr/bin/env python3
"""Integrate the exact cubic source and the explicit CM target re-marking."""
from pathlib import Path
import shutil,re
ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent/'work'
backup=ROOT/'notes/eighth_hour_preintegration'
for name in ('main_finite_cm_forgetting_discrepancy.tex','tower_finite_genus_one_action.tex'):
    shutil.copy2(WORK/name,backup/(name+'.before_marking'))
supp=(WORK/'main_cm_marking_fiber_product.tex').read_text()
supp=re.sub(r'\\paragraph\{([^}]+)\}',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\quad',supp)
cut=supp.index(r'\par\medskip\noindent\textbf{The full joint image')
marking=supp[:cut];pairimage=supp[cut:]
p=WORK/'main_finite_cm_forgetting_discrepancy.tex';t=p.read_text()
needle=r'\begin{result}{A.4.42}'
assert needle in t
t=t.replace(needle,marking+'\n'+needle)
t=t.replace('from A.4.25 and A.4.22.  The last map is the actual',
            'from A.4.25 and A.4.22, with the target marking specified by (MFP.1)--(MFP.3) below.  The last map is the actual')
t=t.replace('This equality also retains all the additional solvable coordinates with value one.',
            'This equality also retains all the additional solvable coordinates with value one.\n'
            'On the zero-label finite normalizer, the complete image of $(d\\operatorname{pr}_G,j_0^\\dagger)$ is the fiber product\n'
            '$J_c\\times_{\\operatorname{SL}_2(\\mathbb Z/12)}J_c$, of order $1152\\cdot3^8$, by (MFP.5)--(MFP.7).')
t+='\n'+pairimage
p.write_text(t)
p=WORK/'tower_finite_genus_one_action.tex';t=p.read_text()
needle='It factors through the specified subgroup of the\nuniversal finite level, by (FGA.6).'
assert needle in t
t=t.replace(needle,
 'Its target uses the aligned marking (MFP.1)--(MFP.3):\n'
 '$j_0=\\sigma_Jj_0^{\\mathrm{up}}$.  The actual free-group\n'
 'swap $s_J$ preserves the compact quotient kernel, as\n'
 'proved there. Write $F_c^{\\mathrm{al}}=s_JF_cs_J^{-1}$.\n'
 +needle)
t=t.replace(r'j_0\Psi_F=\operatorname{Ad}(F_c)j_0.',r'j_0\Psi_F=\operatorname{Ad}(F_c^{\mathrm{al}})j_0.')
p.write_text(t)
p=ROOT/'code/assemble_draft.py';t=p.read_text()
needle=' "centralizer_reversed_binary_obstruction.tex":"part_a_reversed_binary_obstruction.tex",'
assert needle in t
t=t.replace(needle,needle+'\n'+
 ' "tower_cubic_orbit_orbifold.tex":"part_a_cubic_orbit_orbifold.tex",')
p.write_text(t)
p=ROOT/'GT_TOWER_CHECK_paper.tex';t=p.read_text()
needle=r'\input{part_a_reversed_binary_obstruction}'
assert needle in t;t=t.replace(needle,needle+'\n'+r'\input{part_a_cubic_orbit_orbifold}');p.write_text(t)
p=ROOT/'code/update_results.py';t=p.read_text()
pos=t.index("pat=re.compile(r'\\\\begin")
addition="""
add('A.4.44','A.4.7 exact graph centralizer and torsion recognition; literal C3*C3 Schreier rewriting; exact affine torus action and finite graph chains', 'Task A.4; Lead 1(2)',
    'The actual cubic orbifold over the nine-point translation cover has a simultaneous finite cone and cusp detector',
    'The exact source is C3*C3 with index3 free torus subgroup and index27 nine-point surface group. Its marked CM element is the cusp c, with c^3=[x,y], while the two finite factors have unmarked fixed triples. The relative graph quotient over every retained finite input D has order|D|*3^(1+|D|/3) and centralizer projections exactly the three named cyclic subgroups. The entire first layer of order3^13 was replayed: all27 residues, rank6 centralizer equations, kernel fibres dimension4, and exactly12 nonidentity order3-lift residues. Ambient H-normalizer recognition remains a further step.')

"""
t=t[:pos]+addition+t[pos:]
t=t.replace('A.4.1--A.4.43;', 'A.4.1--A.4.44;')
t=t.replace('This retains the proved equality on the image of the ordinary geometric normalizer and identifies the necessary next recognition step.',
 'The actual swap a<->b aligns the forgetting target, and the integral3J comparison proves equality on the ordinary geometric normalizer. The full joint image is exactly the fibre product over SL2(Z/12), of order1152*3^8. This identifies the necessary next recognition step.')
p.write_text(t)
p=ROOT/'part_a_finite.tex';t=p.read_text()
needle='task constructs a stronger geometric recognition\nrefinement and executes the complete genuine-source'
assert needle in t
t=t.replace(needle,'task constructs a stronger geometric recognition\n'
 'refinement.  A.4.44 now supplies the exact cubic orbifold\n'
 'source and simultaneous relative cone and cusp detectors.\n'
 'The task also executes the complete genuine-source')
p.write_text(t)
p=ROOT/'GT_TOWER_CHECK_report.md';t=p.read_text()
t=t.replace('A.4.1--A.4.43','A.4.1--A.4.44')
t=t.replace('Seven further independently audited results','Eight further independently audited results')
t=t.replace('All seven newly integrated proofs','All eight newly integrated proofs')
t=t.replace('163 statements:148Proved','164 statements:149Proved')
t=t.replace('163 numbered statements:148Proved','164 numbered statements:149Proved')
needle='The separate all-multiplier normalization supplement is preserved'
addition='''A.4.44 gives the actual C3*C3 orbifold source over the nine-point translation cover, with every cone and cusp marking fixed before finite reduction. The marked linear CM class lifts to the infinite-order cusp c, with c^3=[x,y]; the two finite cone factors have unmarked fixed triples. For every retained finite orbifold input D, one explicit relative graph layer has centralizer projection exactly the named cyclic subgroup for all three elements. Root replayed the entire first layer of order3^13: all27 residues, the rank-six centralizer equations, four-dimensional fibres, twelve nonidentity residues admitting order-three lifts, and the marked cusp's exact order9. The actual finite affine action and its three branch orbits were checked. This supplies a precise source for the continuing relative geometric recognition; it does not assert the missing ambient normalizer equality.

The A.4.42 marking audit now specifies the actual free-group swap a<->b on the compact quotient. Its induced involution aligns ordinary forgetting with descent; the integral covering matrix3J proves equality on the actual ordinary normalizer before any finite reduction. With that alignment, the exact complete joint image of the two finite outputs is Jc times-over-SL2(Z/12) Jc, of order7,558,272. The unaligned version is the explicitly isomorphic twisted fibre product. Thus every comparison retains its actual marking morphism.

'''
assert needle in t;t=t.replace(needle,addition+needle);p.write_text(t)
print('Integrated A.4.44 and the exact CM marking/fibre product; ledger count164.')
