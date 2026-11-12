#!/usr/bin/env python3
"""Registers for the proved parts and exact source remainders of B.16."""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
row={
 'id':'B.16',
 'statement':'The completed modular group has the unique central sign twist, a faithful peripheral automorphism comparison, unique normalized conjugators on Z^!, and canonical quotient normalizer sections; named geometric comparison and unquotiented section lifts remain.',
 'status':'Open',
 'where_proved':'sections/B_modular_comparison.tex, B.16 proved part, finite model, and exact residuals (R1)--(R3)',
 'depends_on':'C.2; B.13; E.15; Herfort--Ribes1984 Theorems1,2 (precise reductions supplied)',
 'manuscript_passages (section; folio; scan)':'49.V.8--9; folios590--596,609--618 with dual pagination; C3 scans573--582,612--629',
 'depends_on_doubtful_reading (scan, alternatives)':'579 sigma|tau prime;581 Theta exponent epsilon2 versus nu2;582 marginal ! correction;615 action onC2;616 N_rho versus N_sigma',
 'notes':'Open applies only to source comparisons (R1)--(R3), not to the normalized conjugator theorem. Full finite groups SL2F3,SL2Z4 enumerated; mod4 has48 automorphisms and central kernel2, but finite normalization has two beta choices. Primary Herfort--Ribes announcement pp31--34 read directly and theorem hypotheses checked; not represented as a proof from finite tests.'
}

def read(scan,place,support,strength='Exact mathematical implication; not a claim to settle an ambiguous glyph visually.'):
 return dict(package=('LM_C3-568-586' if int(scan.split('--')[0])<587 else
                     'LM_C3-606-624' if int(scan.split('--')[0])<625 else 'LM_C3-625-643'),
  scan=scan,**{'the \\unsure or \\illegible place':place,
  'what the mathematics supports':support,'how strongly':strength})

readings=[
 read('573--574','Kernel of Aut(C) to Aut(C/omega) described as characters to the centre',
      'A central twist must have chi(omega)=0 to fix the central involution; all two characters of C_ab=C12 satisfy this. The kernel is exactlyC2, not an unrestricted character statement for arbitrary central extensions.'),
 read('579','mu_sigma={1,unsure{sigma|tau prime}} in(23)',
      'sigma has order4; tau prime=sigma^-1 tau is an involution. The asserted order2 subgroup and its trivial intersection with the orientation-preserving subgroup require tau prime. This is an algebraic disambiguation.'),
 read('581','(35)Theta^{epsilon2(u)} and marginal exponentnu2(u)',
      'The exponent must be nu2(u) inZ/2 with epsilon2=(-1)^nu2. Literal exponents+1 and-1 both giveTheta and cannot encode identity whenepsilon2=+1. The marginal nu2 correction has the correct type.'),
 read('582','Main line Z versus Z^! and the marginal restriction to M^![0]',
      'The normalized statement belongs to Z^!=kernel of action onS3. Inner e belongs toZ but acts nontrivially onS3. Z^! has index2 and maps to gamma with kernelL^2, whereas Z has kernelL.'),
 read('615','(131)epsilon2 acting onL_sigma/{plus/minus1}=C2',
      'Aut(C2) is trivial, so this quotient extension isC2 x gamma. Inversion byepsilon2 is meaningful on the unquotientedC4, not itsC2 quotient.'),
 read('616','(134)image arrows written toN_rho while the formula uses beta^-1u',
      'The formula b(u)=beta^-1u takes values inN_sigma^*. For u=tau, b(u)=tau inverts sigma but does not sendrho to rho^{plus/minus1}. Thus N_sigma is mathematically required in this definition.'),
 read('628--629','Diagram26: modular schemes versus the elliptic moduli stack and its rigidification; the question about a curve of invariant0 overQ and the following correction',
      'The objects overQ are the elliptic stack and its central-C2 rigidification, distinct from the affine groupM and from the coarse j-line. The smooth curve y^2=x^3+1 has c4=0,c6=-864,Delta=-432,j=0. Its existence does not identify the particular source gerbe object or its section; scan629 already makes this distinction. Exact invariants are executed inD_motives.py.',
      'Both photographs directly inspected, with checked transcription and exact invariant calculation; no final palaeographical claim.')
]

residual=(
 'R1: for the source-defined action iota:Pscript=Mtilde03->Aut(C/omega), identify its image and topology with the explicitly defined peripheral automorphism group Abar, and identify Ntilde11 with formalG overC andomega. '
 'R2: decide splitting of Es=gamma x_{N_sigma^*/omega} N_sigma^* for the proved section b_gamma; b onZ^! does not descend becauseb(e^2)=omega. Construct the specified source sectionM(0), then identify N_sigma^* intersectM(0)Pi0 withgamma and N_rho^* intersectM(0)Pi0 withker epsilon3 and the geometric sections. '
 'R3: identify Er=gamma x_{N_rho^*/omega} N_rho^* for proved a_gamma with source gamma-tilde/N_rho-question and with the finiteD8 inflation. '
 'These are separate from B.8.5 and the arithmetic image problemD.7; late filtration/lift-law residuals are recorded by B.17/B.18.'
)
proved=(
 'C_ab=C12, centerC=C2; all central-quotient automorphisms lift and kernel is the unique sign twist; peripheral automorphism groups ofC andC/omega are isomorphic. '
 'G/omega is the formal peripheral automorphism group; signs are linked and unique; Pi0 is invariant; Z^! has index2 and kernelL^2 overgamma. '
 'Unique normalizedalpha,beta onZ^!; homomorphisms a-bar andb, their exact values onL^2, quotient sections and C3 semidirectgamma/C2 directgamma decompositions.'
)
computed=(
 'code/AB_modular_comparison.py/.out/.json: exhaustive automorphism enumerations forSL2F3(24automorphisms,kernel1) andSL2Z4(48automorphisms,image24,kernel2); '
 'S4 quotient certified onfourC3 subgroups; all16 linkedU12 pairs andeightmod2-trivial pairs checked; each hasoneparity-correctalpha andtwobeta; explicitidentityambiguity and central-twist loop-conjugacy witnessmod4.'
)
coverage=[dict(task=t,outcome='partly settled',statement_ids='B.16',
  proved_cases=proved,executed_computations=computed,
  exact_smallest_undecided_instance=residual)
 for t in ('A.a','A.b','B.c','B.g')]
assert r'\begin{statement}{B.16}{Open}' in (ROOT/'sections/B_modular_comparison.tex').read_text()
for name,obj in [('B_modular_comparison_results.json',[row]),
                 ('B_modular_comparison_readings.json',readings),
                 ('B_modular_comparison_coverage.json',coverage)]:
 (ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
print(f'B.16: 1 statement row, {len(readings)} reading rows, 4 exact task-coverage rows.')
