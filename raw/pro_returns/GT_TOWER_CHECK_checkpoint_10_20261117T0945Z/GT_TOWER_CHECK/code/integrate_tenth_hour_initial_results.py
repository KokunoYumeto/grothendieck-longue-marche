#!/usr/bin/env python3
"""Integrate four complete audited proofs, preserving the previous working text."""
from pathlib import Path
import shutil
ROOT=Path(__file__).resolve().parents[1]
BACK=ROOT/'notes/tenth_hour_initial_preintegration'
BACK.mkdir(exist_ok=True)
for name in ['code/assemble_draft.py','code/update_results.py','code/make_checkpoint.py',
             'GT_TOWER_CHECK_paper.tex','GT_TOWER_CHECK_report.md','part_a_finite.tex']:
    dest=BACK/name
    assert not dest.exists(),'One-shot integration: '+name
    dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/name,dest)
parts=[('tower_finite_branch_output.tex','part_a_finite_branch_output.tex'),
       ('ghost_diagonal_disk_parameter.tex','part_a_diagonal_disk_parameter.tex'),
       ('centralizer_common_mod6_canonical_survivor.tex','part_a_common_mod6_canonical_survivor.tex'),
       ('root_involution_configuration_fusion.tex','part_a_involution_configuration_fusion.tex'),
       ('ghost_common_quartic_kernel.tex','part_a_common_quartic_kernel.tex')]
p=ROOT/'code/assemble_draft.py';s=p.read_text()
needle=' "root_involution_configuration_recognition.tex":"part_a_involution_configuration_recognition.tex",'
assert needle in s
s=s.replace(needle,needle+'\n'+'\n'.join(' "'+a+'":"'+b+'",' for a,b in parts))
needle='\nmapping={'
assert needle in s
s=s.replace(needle,'\n# New coefficient-four programs retain their own directory and all failures.\n'
    'for dirname in ("ghost_mod4","centralizer_mod4"):\n'
    '    if (WORK/dirname).exists():\n'
    '        shutil.copytree(WORK/dirname,ROOT/"code"/dirname,dirs_exist_ok=True,\n'
    '                        ignore=shutil.ignore_patterns("__pycache__"))\n'+needle)
p.write_text(s)
p=ROOT/'code/make_checkpoint.py';s=p.read_text();needle='# Bytecode and runtime caches'
assert needle in s
s=s.replace(needle,'# Preserve the additional coefficient-four computations, including failed lifts.\n'
    'for dirname in ("ghost_mod4","centralizer_mod4"):\n'
    '    if (work/dirname).exists():\n'
    '        shutil.copytree(work/dirname,ROOT/"code"/dirname,dirs_exist_ok=True,\n'
    '                        ignore=shutil.ignore_patterns("__pycache__"))\n'+needle)
p.write_text(s)
p=ROOT/'GT_TOWER_CHECK_paper.tex';s=p.read_text()
needle=r'\input{part_a_fivepoint_common_kernel}'
assert needle in s
s=s.replace(needle,needle+'\n'+r'\input{part_a_finite_branch_output}'+'\n'+r'\input{part_a_diagonal_disk_parameter}')
needle=r'\input{part_a_involution_configuration_recognition}'
s=s.replace(needle,needle+'\n'+r'\input{part_a_common_mod6_canonical_survivor}'+'\n'+r'\input{part_a_involution_configuration_fusion}'+'\n'+r'\input{part_a_common_quartic_kernel}')
p.write_text(s)
p=ROOT/'code/update_results.py';s=p.read_text();pos=s.index("pat=re.compile(r'\\\\begin")
metadata='''
add('A.4.53','A.4.54 finite involution recognition; actual C2*C2*C2*F4 orbifold and two covering characters; primitive peripheral graph detector; characteristic free-surface reconstruction; executed Artin/free-basis maps', 'Task A.4; Lead 1(2)',
    'An explicit finite ambient quotient of the original nine-point mapping class group retains the actual ordered-pole branch output',
    'The exact maps retain the original genus-one cover character and the distinct four-root cover character, the signed free basis, full Pc forgetting and primitive point-push homology modulo12. A mod3 graph layer detects the primitive b0 conjugator. Characteristic surface refinement reconstructs an intrinsic orbifold quotient; both boundary lifts act inner on it. Its cusp gate makes the final conjugator even, proving actual kernel containment and a homomorphism on the ambient centralizer image. The companion collar/diagonal proof retains the same local five-point parameter. Full compiler assembly and census remain separate.')
add('A.4.55','A.4.52 exact common mod6 source; literal finite automorphism census; full integral L2/[B,L2] presentation; both primary homology edge maps; B.2.7 and B.2.9 full lift', 'Task A.4; Lead 1(2)',
    'The complete mixed-mod6 five-point pentagon test has an actual multiplier-one gentle survivor with Delta1',
    'Binary affine mask31 is an actual finite automorphism; ternary f=A=1. The exact full binary multiplier is C2^16, its pure-frame correction quotient C2^5. The explicit s-centralizer correction at indices0,2,6,8,17 kills the defect in the integral HNF lattice. Natural maps with kernels3^98 and2^97 kill both primary defects; stem surjectivity gives the full canonical automorphism. The full finite-certificate lift and36-divisible normalization preserve all eight insertion records. The first failed point and all24 binary-family counts are retained. Root and ghost independently replayed and audited the proof.')
add('A.4.56','A.4.54 binary configuration refinement; exact induced finite period coordinate; reduced-cone Tate comparison; actual Gamma3 branch-assignment words; evaluated isotopy groupoid', 'Task A.4; Lead 1(2)',
    'A second explicit binary refinement fuses every order2 element in the exact involution fibre to an ordinary pure positive conjugate at the recognition output',
    'The label and finite-period fibre is exactly (K_n/V1)iota. Two-n-minus-one cohomology-killing covers force a fixed point in the lower cover. Six explicit integral Gamma3 words realize every ordered two-torsion assignment; a lifted sphere isotopy matches all four pair coordinates and signs. The actual path gives alpha=psi^-1 ell, with its deck correction retained. Both independent audits checked the conjugation direction and all source maps. No stability of an arbitrary transported quotient kernel is assumed.')
add('A.4.58','A.4.52 named common source; complete coefficient4 relation reduction; both insertion/modular factorization maps; exact exponent lattice; literal coefficient CRT', 'Task A.4; Lead 1(2)',
    'The exact coefficient4/12 targets have mixed torsion while their eight-map common source is free of rank97 over the coefficient ring',
    'The actual target relation matrix has667 unit pivots and a rank2 even residual, yielding C4^100 plus C2^2; the failed free102 lift is preserved. Explicit maps LQ=I, T=QF and Q=TG prove the full common source C4^97, retaining all source substitutions and binary basis changes. Its kernel is (Kprime K^4) intersect Fprime F^24. Actual CRT gives the modulus12 kernel (Kprime K^12) intersect Fprime F^72, source order1728*12^97 and abelianization C72^2. The target12 kernel is C12^100 plus C6^2. Root fresh replay matches every saved array.')

'''
s=s[:pos]+metadata+s[pos:]
s=s.replace('A.4.1--A.4.52; A.4.54; executed','A.4.1--A.4.56; A.4.58; executed')
p.write_text(s)
p=ROOT/'part_a_finite.tex';s=p.read_text()
needle='common source kernel and its literal Chinese remainder\ncomparison.'
assert needle in s
s=s.replace(needle,needle+' A.4.55 proves a genuine parity-one survivor\n'
    'in a nonidentity fibre of that entire mixed-modulus-six test.\n'
    'A.4.58 computes the next mixed coefficient-four and coefficient-twelve\n'
    'targets with their exact common source kernels.\n')
needle='the nine-, ten-, eleven- and twelve-point configurations.'
assert needle in s
s=s.replace(needle,needle+' A.4.56\n'
    'adds explicit pure positive fusion in their specified finite involution\n'
    'fibres. A.4.53 retains the final ordered-pole branch output by an\n'
    'actual finite quotient of the original nine-point group.\n')
p.write_text(s)
p=ROOT/'GT_TOWER_CHECK_report.md';s=p.read_text()
s=s.replace('Current state at checkpoint09','Current state during tenth-hour work')
start=s.index('Ninth-hour checkpoint, 17 November 2026.');end=s.index('\n\n',start)
s=s[:start]+('Tenth-hour working manuscript, 17 November 2026. Checkpoints01--09 remain unchanged. '
    'Checkpoint09 was verified and saved with372pages,173statements and85actual full-page inspections. '
    'Four further audited results are now integrated, bringing the working ledger to177statements:162Proved,2Known,13Open. '
    'The new full build and its visual inspection are pending. The next hourly checkpoint and progress review are due at approximately09:45UTC.')+s[end:]
lines=s.splitlines()
for i,line in enumerate(lines):
    if line.startswith('| A.4 |'):
        lines[i]='| A.4 | A.4, A.4.1--A.4.56; A.4.58 | Open; explicit translation and involution recognition/fusion and the actual ambient branch output are proved; the full mod6 test has a genuine parity1 nonidentity survivor; exact mixed-mod4/12 source maps are proved, and the remaining finite branch covariance/compiler and executed separating-level census continue |'
s='\n'.join(lines)+'\n'
heading='## Ninth-hour advances on the main finite task'
assert heading in s
s=s.replace(heading,'## Tenth-hour advances on the main finite task\n\n'
    'A.4.53 supplies an actual ambient nine-point quotient retaining the ordered-pole branch output, with both cover characters and the residual evenness test. Its diagonal-disk continuation gives the literal same-parameter local braid action. A.4.56 adds explicit finite involution fusion, with pure positive ordinary corrections and actual path/deck markings. A.4.55 supplies a genuine full gentle parity-one survivor of the entire mixed-mod6 pentagon test, after its complete integral canonical-cover correction and normalization. A.4.58 computes the next coefficient-four and mixed-twelve targets, retaining the binary torsion that the first attempted lift missed. The full finite CM compiler and the next genuine survivor gate continue in separately retained sources.\n\n'+heading)
old='The current ledger has173 numbered statements:158Proved,2Known and13Open.'
assert old in s
s=s.replace(old,'The current working ledger has177 numbered statements:162Proved,2Known and13Open. The newly integrated full build and visual check are pending. The last verified checkpoint had173numbered statements:158Proved,2Known,13Open.')
p.write_text(s)
print('Integrated A.4.53, A.4.55, A.4.56 and A.4.58; extended exact new-directory retention.')
