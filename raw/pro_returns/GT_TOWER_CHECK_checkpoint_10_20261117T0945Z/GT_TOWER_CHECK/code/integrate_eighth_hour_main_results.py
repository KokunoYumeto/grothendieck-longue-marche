#!/usr/bin/env python3
"""Integrate the three fully audited eighth-hour main-task proofs."""
from pathlib import Path
import shutil,re
ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent/'work'
BACKUP=ROOT/'notes/eighth_hour_preintegration'
BACKUP.mkdir(exist_ok=True)
names=['tower_finite_genus_one_action.tex','centralizer_odd_target_survivors.tex',
       'main_finite_cm_forgetting_discrepancy.tex','main_cm_discrepancy_family_supplement.tex']
for name in names:
    target=BACKUP/name
    assert not target.exists()
    shutil.copy2(WORK/name,target)
p=WORK/'centralizer_odd_target_survivors.tex'
t=p.read_text()
t=re.sub(r'\\paragraph\{([^}]+)\}',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\quad',t)
p.write_text(t)
p=WORK/'main_finite_cm_forgetting_discrepancy.tex'
t=p.read_text().replace('=operatorname{im}',r'=\operatorname{im}')
t=t.replace('The joined finite normalizer has an order-three discrepancy between descent and forgetting',
            'The full signed-period kernel is the exact discrepancy between finite descent and ordinary forgetting')
needle='This statement gives the exact failure of the proposed'
assert needle in t
t=t.replace(needle,
    'More precisely, the image under $d\\operatorname{pr}_G$ of the centralizer subgroup with ordinary forgetting value one is exactly\n'
    '$\\ker(J_c\\to\\operatorname{SL}_2(\\mathbb Z/12))\\cong C_3^4$, as proved in (CDF.1)--(CDF.9) below.\n'
    'This equality also retains all the additional solvable coordinates with value one.\n'+needle)
supp=(WORK/'main_cm_discrepancy_family_supplement.tex').read_text()
supp=supp.replace(r'\paragraph{The discrepancy realizes the entire signed-period kernel.}',
                  r'\par\medskip\noindent\textbf{The discrepancy realizes the entire signed-period kernel.}\quad')
t+='\n'+supp
p.write_text(t)
p=ROOT/'code/assemble_draft.py'
t=p.read_text()
needle=' "tower_finite_e44_comparison.tex":"part_a_finite_e44_comparison.tex",'
assert needle in t
t=t.replace(needle,needle+'\n'+
 ' "tower_finite_genus_one_action.tex":"part_a_finite_genus_one_action.tex",\n'+
 ' "centralizer_odd_target_survivors.tex":"part_a_odd_target_survivors.tex",\n'+
 ' "main_finite_cm_forgetting_discrepancy.tex":"part_a_cm_forgetting_discrepancy.tex",')
p.write_text(t)
p=ROOT/'GT_TOWER_CHECK_paper.tex'
t=p.read_text();needle=r'\input{part_a_finite_e44_comparison}'
assert needle in t
t=t.replace(needle,needle+'\n'+r'\input{part_a_finite_genus_one_action}'+'\n'+
            r'\input{part_a_odd_target_survivors}'+'\n'+r'\input{part_a_cm_forgetting_discrepancy}')
p.write_text(t)
p=ROOT/'code/update_results.py'
t=p.read_text();needle="pat=re.compile(r'\\\\begin"
pos=t.index(needle)
addition="""
add('A.4.40','A.4.26; A.4.37; A.4.39; A.6.1 local quilt identities; exact Birman kernel; faithful mod3 graph homology; finite actual gentle records', 'Task A.4; Lead 1(2)',
    'One bounded finite five-point input gives the actual genus-one mapping-class and punctured-surface actions, including the full ordinary compact forgetting factor',
    'The90-generator bound retains every required stabilizer map. Literal local weights descend through the universal pure kernels; their actual finite record proves invertibility. A characteristic graph-homology cover kills projected centers, so the actual Birman image yields Aut(Q), not just its inner quotient. The full j0 factor is preserved. Identification with d on the larger finite normalizer is refuted by A.4.42 and requires a further recognition refinement.')
add('A.4.41','B.2.7--B.2.9 full canonical-cover image equality; B.2.27 pants-kernel word; exact six source-deck maps; source abelianization C_N^2; compactness of the actual gentle source', 'Task A.4; Lead 1(2)',
    'Every specified finite family of odd-derived or exponent-four odd-normal targets admits a genuine parity-one gentle survivor, with literal normalized signed frames',
    'The auxiliary cubic frame is a suitable odd power of [[x4,y4],z4]^2. Its signed image is5I on all six decks and its tested coordinates are1. Its full canonical-cover lift commutes with r by the coprime2/3 identity. Normalization retains the identity f-record and Delta1. Compactness gives one genuine survivor for each entire directed family, also with D_P=1 and harmonic parameter0. The cap216 source is computed exactly: degree3954, order2^8*3^15, pure abelianization C12^2. Relative pro3 refinements over the stated exponent4 bases cannot settle the requested exclusion.')
add('A.4.42','A.4.19--A.4.25 actual compatible-pair and perfect-image calculations; retained nine-coset ordinary forgetting map; exact Hermitian reflection and six Cayley lifts', 'Task A.4; Lead 1(2)',
    'The equality of finite CM descent and ordinary forgetting is false on the joined finite centralizer; its exact discrepancy image is the full C3^4 signed-period kernel',
    'An explicit order3 isometry k centralizes the actual deck matrices, has nonscalar first-order quotient and lies in Omega. The actual sixth-derived joint source realizes k with all lower and nine ordinary-forgetting values1. Six exact Cayley lifts realize all first-order symmetric parameters; quotienting the actual two scalar inner rows yields all81 classes. The retained period comparison gives the reverse inclusion. Every additional finite solvable family still leaves the full discrepancy image. This retains the proved equality on the image of the ordinary geometric normalizer and identifies the necessary next recognition step.')

"""
t=t[:pos]+addition+t[pos:]
t=t.replace('A.4.1--A.4.39;', 'A.4.1--A.4.42;')
p.write_text(t)
print('Integrated A.4.40--A.4.42; every preintegration source preserved.')
