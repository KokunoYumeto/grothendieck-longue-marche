#!/usr/bin/env python3
"""Integrate the fully audited finite exclusion and all-coefficient source."""
from pathlib import Path
import shutil
ROOT=Path(__file__).resolve().parents[1];WORK=ROOT.parent/'work'
BACK=ROOT/'notes/tenth_compiler_preintegration';BACK.mkdir(exist_ok=True)
for rel in ['code/assemble_draft.py','code/update_results.py','code/make_checkpoint.py',
            'GT_TOWER_CHECK_paper.tex','GT_TOWER_CHECK_report.md','part_a_finite.tex']:
    dst=BACK/rel;assert not dst.exists(),'One-shot integration: '+rel
    dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/rel,dst)
parts=[('ghost_finite_cone_fusion.tex','part_a_finite_cone_fusion.tex'),
       ('tower_finite_orbifold_transport.tex','part_a_finite_orbifold_transport.tex'),
       ('tower_finite_branch_covariance.tex','part_a_finite_branch_covariance.tex'),
       ('tower_finite_cm_compiler.tex','part_a_finite_cm_compiler.tex'),
       ('ghost_integral_common_source.tex','part_a_integral_common_source.tex')]
p=ROOT/'code/assemble_draft.py';s=p.read_text()
needle=' "centralizer_common_mod12_survivor.tex":"part_a_common_mod12_survivor.tex",'
assert needle in s
s=s.replace(needle,needle+'\n'+'\n'.join(' "'+a+'":"'+b+'",' for a,b in parts))
s=s.replace('("ghost_mod4","centralizer_mod4")','("ghost_mod4","centralizer_mod4","ghost_mod4_review")')
needle='\nmapping={'
assert needle in s
s=s.replace(needle,'\n# Retain the authored standalone typesetting checks, excluding runtime caches.\n'
 'if (WORK/"tower_render").exists():\n'
 '    shutil.copytree(WORK/"tower_render",ROOT/"notes/standalone_render/tower",dirs_exist_ok=True,\n'
 '                    ignore=shutil.ignore_patterns("__pycache__"))\n'
 'for suffix in (".log",".stdout"):\n'
 '    source=WORK/("centralizer_contributions_check"+suffix)\n'
 '    if source.exists():\n'
 '        target=ROOT/"notes/standalone_render/centralizer"/source.name\n'
 '        target.parent.mkdir(parents=True,exist_ok=True)\n'
 '        shutil.copy2(source,target)\n'+needle)
p.write_text(s)
p=ROOT/'code/make_checkpoint.py';s=p.read_text()
s=s.replace('("ghost_mod4","centralizer_mod4")','("ghost_mod4","centralizer_mod4","ghost_mod4_review")')
needle='# Bytecode and runtime caches'
assert needle in s
s=s.replace(needle,'# Authored standalone render checks and exact independent replays.\n'
 'if (work/"tower_render").exists():\n'
 '    shutil.copytree(work/"tower_render",ROOT/"notes/standalone_render/tower",dirs_exist_ok=True,\n'
 '                    ignore=shutil.ignore_patterns("__pycache__"))\n'
 'for suffix in (".log",".stdout"):\n'
 '    source=work/("centralizer_contributions_check"+suffix)\n'
 '    if source.exists():\n'
 '        target_log=ROOT/"notes/standalone_render/centralizer"/source.name\n'
 '        target_log.parent.mkdir(parents=True,exist_ok=True)\n'
 '        shutil.copy2(source,target_log)\n'+needle)
p.write_text(s)
p=ROOT/'GT_TOWER_CHECK_paper.tex';s=p.read_text()
needle=r'\input{part_a_involution_configuration_fusion}'
assert needle in s
s=s.replace(needle,needle+'\n'+'\n'.join(r'\input{'+b.removesuffix('.tex')+'}' for a,b in parts[:-1]))
needle=r'\input{part_a_common_mod12_survivor}'
assert needle in s
s=s.replace(needle,needle+'\n'+r'\input{part_a_integral_common_source}')
p.write_text(s)
p=ROOT/'code/update_results.py';s=p.read_text();pos=s.index("pat=re.compile(r'\\\\begin")
new='''
add('A.4.57','A.4.18 and A.4.22 exact18-residue ordinary cubic centralizer; A.4.39--A.4.40 finite tower/compiler; A.4.47--A.4.49 translation recognition/fusion; A.4.53--A.4.54 actual branch and involution recognition; CONE/OBT/BCV exact branch-kernel transport; FCP.L1--L6 actual point-push linearization', 'Task A.4; Task A.7; Lead 1(2)',
    'One explicitly specified finite characteristic five-point level excludes every genuine gentle parity-one pentagon shadow, for every multiplier',
    'The joined finite output retains the linear-section period map and induced ordinary forgetting coordinate. Translation fusion and involution recognition supply one branch correction; exact all-centralizer covariance gives the finite CM square. W is literally Pc times C12 and its ordinary outer image is C12^2 semidirect Jc, proving the point-push linearization without an output automorphism assumption. The actual Jc centralizer has18 period residues with exponents i,j of equal parity; the48-case signed matrix replay gives Delta0. Composition with an actual Galois finite record handles every multiplier. All sizes are explicit monotone expressions. Full genuine-source enumeration at this specified level remains unexecuted; the theorem is not counted as completing that requested census. Root and ghost audited every comparison and the full finite domain.')
add('A.4.60','A.4.52 named eight-map common base; A.4.58 mixed coefficient maps; full1152-by769 integral relation Smith form; explicit integral source lattice and both target factorization maps; actual finite-exponent cofinality', 'Task A.4; Lead 1(2)',
    'The exact integral target is Z^100 plus C6^2 and the eight-map common source is a primitive rank97 lattice, with exact kernels and inverse limits for every coefficient',
    'Integral target maps retain both order-six torsion coordinates. The modular restriction Q=CW has lattice index3, detW=plus-or-minus3 and LC=I; all eight maps factor through C. The actual97-by800 free target projection has an integer right inverse, proving the common kernel Kprime J^m=(Kprime K^m) intersect(Fprime F^(6m)) uniformly. Target order192*m^100*gcd(m,6)^2, source order1728*m^97, pure abelianization C_(6m)^2, and exact CRT maps follow. Finite-exponent cofinality gives the displayed completed relative-abelian source and target. Root rebuilt both integral producers; all2+36 saved arrays match exactly.')

'''
s=s[:pos]+new+s[pos:]
s=s.replace('A.4.1--A.4.56; A.4.58--A.4.59; executed','A.4.1--A.4.60; executed')
p.write_text(s)
p=ROOT/'part_a_finite.tex';s=p.read_text()
needle='automorphism checks.\n'
assert needle in s
s=s.replace(needle,needle+'A.4.60 supplies the integral source and target maps for every\n'
 'coefficient modulus, retaining the exact order-six torsion and a\n'
 'split integral embedding of the rank-$97$ common source.\n')
needle='actual finite quotient of the original nine-point group.'
assert needle in s
s=s.replace(needle,needle+' A.4.57 now\n'
 'joins these maps into one explicitly specified characteristic finite\n'
 'five-point level which excludes every genuine parity-one pentagon\n'
 'shadow, for all multipliers. Its proof retains the same conjugator,\n'
 'the actual point-pushing module and the exact eighteen coupled\n'
 'cubic-centralizer period residues.\n')
old=''' The remaining nonidentity fibres
and the complete common finite census are still being
examined. The compactness result below supplies existence
but no substitute for that computation.'''
new=''' The complete enumeration of all genuine source records and their
pentagon values at the explicitly specified separating level remains
unexecuted. The smaller modulus-six and modulus-twelve tests have
actual parity-one survivors, as proved above. The compactness result
below records the earlier existence argument; A.4.57 now supplies
an explicit finite level and proof of exclusion. The requested
executed census remains the undecided part of task A.4.'''
assert old in s;s=s.replace(old,new);p.write_text(s)
p=ROOT/'GT_TOWER_CHECK_report.md';s=p.read_text();lines=s.splitlines()
for i,line in enumerate(lines):
    if line.startswith('| A.4 |'):
        lines[i]='| A.4 | A.4, A.4.1--A.4.60 | Open for the requested complete executed census; A.4.57 now specifies one characteristic finite five-point level excluding every genuine parity-one shadow for all multipliers. Genuine survivors at mod6 and mod12 and the integral common source for every modulus are proved. |'
    elif line.startswith('| A.7 |'):
        lines[i]='| A.7 | A.7; A.4.57 | Proved; Delta vanishes on full profinite GT, with an additional explicit finite exclusion proof |'
    elif line.startswith('| Lead 1 |'):
        lines[i]='| Lead 1 | A.8; A.1--A.7, A.4.1--A.4.60 | Main proof comparisons and signs are proved; an explicit finite separating level is now proved for every multiplier; its complete executed genuine-source census remains open |'
    elif line.startswith('| Lead 1(2) |'):
        lines[i]='| Lead 1(2) | A.3--A.5; A.4.57 | Signed normalization and explicit finite exclusion proved; the complete executed census remains open |'
s='\n'.join(lines)+'\n'
start=s.index('Tenth-hour working manuscript, 17 November 2026.');end=s.index('\n\n',start)
s=s[:start]+('Tenth-hour working manuscript, 17 November 2026. Checkpoints 01--09 remain unchanged. '
 'Checkpoint 09 was verified and saved with 372 pages, 173 statements and 85 actual full-page inspections. '
 'Seven further audited results are now integrated, bringing the working ledger to 180 statements: '
 '165 Proved, 2 Known and 13 Open. The new full build and its visual inspection are pending. '
 'The next hourly checkpoint and progress review are due at approximately 09:45 UTC.')+s[end:]
s=s.replace('The current working ledger has178 numbered statements:163Proved,2Known and13Open.',
            'The current working ledger has 180 numbered statements: 165 Proved, 2 Known and 13 Open.')
heading='## Tenth-hour advances on the main finite task\n\n'
assert heading in s
s=s.replace(heading,heading+
 'A.4.57 now specifies an explicit characteristic finite five-point level and proves that every genuine gentle pentagon shadow there has parity zero, for every multiplier. The complete source-record enumeration at that level has not been executed. The proof retains the actual nine-point branch map, the common translation and involution corrections, the one-conjugator finite CM square, and the exact eighteen-residue cubic-centralizer condition. Its additional point-pushing calculation proves the required linearization on the actual finite kernel. A.4.60 determines the entire integral eight-map source, including its index-three lattice marking and all torsion, and thereby gives exact source and target quotients for every modulus and their inverse limits. Both new proofs have passed independent audit and the applicable fresh exact certificate replays.\n\n')
p.write_text(s)
print('Integrated A.4.57 and A.4.60 with all finite transport inputs and actual maps.')
