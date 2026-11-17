#!/usr/bin/env python3
"""Integrate the reviewed finite fusion, exact source kernel, and involution recognition."""
from pathlib import Path
import shutil
ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent/'work'
BACK=ROOT/'notes/ninth_hour_recognition_preintegration'
BACK.mkdir(exist_ok=True)
for relative in ('code/assemble_draft.py','code/update_results.py',
                 'GT_TOWER_CHECK_paper.tex','GT_TOWER_CHECK_report.md','part_a_finite.tex'):
    dest=BACK/relative
    assert not dest.exists(), 'One-shot integration: '+relative
    dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(ROOT/relative,dest)

p=WORK/'root_involution_configuration_recognition.tex'
t=p.read_text().replace('all four pair permutations','all permutations of the four pairs')
p.write_text(t)
parts=[('tower_finite_configuration_fusion.tex','part_a_finite_configuration_fusion.tex'),
       ('main_fivepoint_common_kernel.tex','part_a_fivepoint_common_kernel.tex'),
       ('root_involution_configuration_recognition.tex','part_a_involution_configuration_recognition.tex')]
for src,_ in parts:shutil.copy2(WORK/src,BACK/src)
p=ROOT/'code/assemble_draft.py';t=p.read_text()
needle=' "centralizer_mixed_mod6_identity.tex":"part_a_mixed_mod6_identity.tex",'
assert needle in t
t=t.replace(needle,needle+'\n'+'\n'.join(' "'+src+'":"'+dst+'",' for src,dst in parts))
p.write_text(t)
p=ROOT/'GT_TOWER_CHECK_paper.tex';t=p.read_text()
t=t.replace(r'\input{part_a_ternary_harmonic_survivor}',
            r'\input{part_a_ternary_harmonic_survivor}'+'\n'+r'\input{part_a_finite_configuration_fusion}')
t=t.replace(r'\input{part_a_mixed_mod6_identity}',
            r'\input{part_a_mixed_mod6_identity}'+'\n'+r'\input{part_a_fivepoint_common_kernel}'+'\n'+r'\input{part_a_involution_configuration_recognition}')
p.write_text(t)

p=ROOT/'code/update_results.py';t=p.read_text();pos=t.index("pat=re.compile(r'\\\\begin")
new='''
add('A.4.49','A.4.40 finite genus-one and universal-curve action; A.4.46--A.4.47 explicit configuration refinement; two cyclic reduced-cone Tate comparisons; actual grid isotopy; executed unrestricted signed period equations', 'Task A.4; Lead 1(2)',
    'One explicit finite five-point level fuses every transported translation copy at the recognition output for every multiplier',
    'Two complete characteristic-cover recursions retain the first normalizer detector and the higher complement domain. Reduced cones retain degree-1 for empty fixed sets and prove a lower fixed point after289covers. Every grid section has an actual pure extended conjugator with its deck displacement. The universal-source reflection makes the power1 modulo3; four exact rows and the separate compact cusp quotient force positive orientation. The resulting beta map has sourceU and targetE0, fixesH elementwise, and transports ordinary normalizers into the recognized ordinary image. No automorphism of E0 or finite-shadow census is asserted.')
add('A.4.52','A.4.45 split fifth retraction; executed actual common binary and ternary insertion modules; exact modular exponent lattice; literal scalar CRT', 'Task A.4; Lead 1(2)',
    'The common source kernels for all eight five-point insertions at m2,3,6 are exactly (Kprime K^m) intersect (Fprime F^(6m))',
    'Both actual prime source modules have rank97 over base288. The modular exponent lattice has index12 and two explicit generating witness words; its added abelian image has order3 with s inversion and r identity. Equality of indices proves the reverse kernel inclusion. Literal CRT gives E6=E2 fibreproduct E3 over B/J, retaining every named generator and all eight insertions. Orders are1728*m^97, pure abelianization C_(6m)^2 and both generator orders6m.')
add('A.4.54','Actual normalized configurations at n9..12; Smith fixed-set theorem; binary free graph quotient; two-row LHS and finite Tate filtration; actual relative homology H1(T,Z_n;F2); Γ6 split subgroup', 'Task A.4; Lead 1(2)',
    'Explicit binary refinements recognize the full ordinary elliptic-involution centralizer at every specified finite ambient output for n9,10,11,12',
    'Fixed components number1,3,6,6 with exact ordered branch assignments and four independent pair-sign monodromies. Fixed loops map onto the ordinary configuration-kernel centralizer. Exactly2n-1 characteristic cohomology-killing covers recognize its finite image. The relative-homology factor forces A p_j+p_(tau0)=p_(tauj), retaining a movingorigin; an actual affine map and lifted sphere isotope match period and every label. Their difference lies in the detected configuration kernel. Induction from K_n semidirect Γ6 has index144*n! and the stated explicit finite bound. The program checks all76032 period/label cases and constructs each compatible finite arc block.')

'''
t=t[:pos]+new+t[pos:]
t=t.replace('A.4.1--A.4.48; A.4.50--A.4.51; executed',
            'A.4.1--A.4.52; A.4.54; executed')
p.write_text(t)

p=ROOT/'part_a_finite.tex';t=p.read_text()
needle='A.4.51 then excludes every parity-one identity parameter\n'
assert needle in t
t=t.replace(needle, 'A.4.49 supplies geometric fusion at the translation\n'
 'recognition level for every multiplier, through an explicitly\n'
 'specified finite five-point input. '+needle)
needle='at the mixed modulus-six level through the actual binary\nand ternary source maps.'
t=t.replace(needle,needle+' A.4.52 identifies the exact\n'
 'common source kernel and its literal Chinese remainder\n'
 'comparison. A.4.54 gives explicit finite recognition of\n'
 'the ordinary elliptic-involution centralizer on each of\n'
 'the nine-, ten-, eleven- and twelve-point configurations.\n')
p.write_text(t)

p=ROOT/'GT_TOWER_CHECK_report.md';t=p.read_text()
t=t.replace('A.4.1--A.4.48; A.4.50--A.4.51','A.4.1--A.4.52; A.4.54')
lines=t.splitlines()
for i,line in enumerate(lines):
    if line.startswith('| A.4 |'):
        lines[i]='| A.4 | A.4, A.4.1--A.4.52; A.4.54 | Open; finite translation fusion and ordinary-normalizer recognition are proved for every multiplier, and the elliptic-involution centralizers have explicit recognition refinements; the exact common mod6 source is known, its identity fibre has parity0, and the nonidentity full-cover census plus finite branch-sphere naturality continue |'
t='\n'.join(lines)+'\n'
old='The finite competing-complement fusion and its orientation marking are being completed separately; no unfinished comparison is used as a proved premise of these integrated results.'
new='''A.4.49 completes the competing-translation fusion at the recognition output for every multiplier. Its reduced-cone proof retains the degree-minus-one empty-fixed-set class; its grid path and actual deck displacement are explicit. The signed relative period calculation excludes the reversing grid after the specified reflection on the universal finite source. The resulting map has sourceU and targetE0; no unproved stability of an arbitrary finite quotient kernel is used. Root and two independent reviewers checked the full proof, and the signed matrix certificate was rerun.

A.4.52 proves the exact common kernel of all eight insertions for m=2,3,6: (Kprime K^m) intersect (Fprime F^(6m)). The source has order1728*m^97, pure abelianization C_(6m)^2 and named generator orders6m. The complete binary and ternary computations, the determinant12 lattice witness and the actual Chinese remainder fibre products were independently replayed.

A.4.54 proves finite recognition of the entire ordinary elliptic-involution centralizer at a specified ambient output for n=9,10,11,12. The fixed-locus components number1,3,6,6, with the exact ordered fixed-label assignments. A binary refinement through2n-1 characteristic covers recognizes the ordinary fixed-loop image. Relative homology retains the movingorigin term and forces the period/branch-label compatibility; an actual affine map and lifted sphere isotopy give the required ordinary correction. The finite Γ6 induction has index144*n!. All76032 period/label cases were checked, with exact compatible blocks and incompatible fixed-column obstructions retained. Ghost independently audited the complete proof and reopened the Smith source at its exact printed locations.

The remaining finite CM comparison must still retain the branch-order double-cover map and the action on motions involving two different pair images. The four separate branch-quartet forgettings alone do not supply that final finite comparison. The nonidentity mod6 source records are being tested through actual finite automorphisms and then their full canonical covers. These are continuing parts of task A.4, rather than completed census claims.'''
assert old in t;t=t.replace(old,new)
p.write_text(t)
print('Integrated A.4.49, A.4.52 and A.4.54 with exact remaining finite scope.')
