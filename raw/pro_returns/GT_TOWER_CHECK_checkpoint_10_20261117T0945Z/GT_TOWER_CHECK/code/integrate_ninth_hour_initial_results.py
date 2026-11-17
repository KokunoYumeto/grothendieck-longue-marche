#!/usr/bin/env python3
"""Integrate the fully reviewed configuration and genuine-source advances."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT.parent / 'work'
BACKUP = ROOT / 'notes/ninth_hour_preintegration'
BACKUP.mkdir(exist_ok=True)
for relative in ('code/assemble_draft.py', 'code/update_results.py',
                 'GT_TOWER_CHECK_paper.tex', 'GT_TOWER_CHECK_report.md',
                 'part_a_finite.tex'):
    dst = BACKUP / relative
    assert not dst.exists(), 'This integration is one-shot: '+relative
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / relative, dst)

parts = [
    ('tower_configuration_fixed_locus.tex', 'part_a_configuration_fixed_locus.tex'),
    ('tower_effective_configuration_recognition.tex', 'part_a_effective_configuration_recognition.tex'),
    ('main_fivepoint_signed_source_module.tex', 'part_a_fivepoint_signed_source_module.tex'),
    ('centralizer_ternary_harmonic_survivor.tex', 'part_a_ternary_harmonic_survivor.tex'),
    ('centralizer_odd_refinement_harmonic.tex', 'part_a_odd_refinement_harmonic.tex'),
    ('centralizer_mixed_mod6_identity.tex', 'part_a_mixed_mod6_identity.tex'),
]
for src, _ in parts:
    assert (WORK / src).exists(), src
    shutil.copy2(WORK / src, BACKUP / src)
p = ROOT / 'code/assemble_draft.py'
t = p.read_text()
needle = ' "centralizer_ternary_fivepoint_retraction.tex":"part_a_ternary_fivepoint_retraction.tex",'
assert needle in t
t = t.replace(needle, needle+'\n'+'\n'.join(' "'+src+'":"'+dst+'",' for src, dst in parts))
p.write_text(t)
p = ROOT / 'GT_TOWER_CHECK_paper.tex'
t = p.read_text()
needle = r'\input{part_a_ternary_fivepoint_retraction}'
assert needle in t
t = t.replace(needle, needle+'\n'+'\n'.join(r'\input{'+Path(dst).stem+'}' for _, dst in parts))
p.write_text(t)

p = ROOT / 'code/update_results.py'
t = p.read_text()
pos = t.index("pat=re.compile(r'\\\\begin")
addition = '''
add('A.4.46','Actual normalized configuration homeomorphism; eight free forgetful fibrations; Edmonds2012 printed273--274 Smith theorem and lifting proposition', 'Task A.4; Lead 1(2)',
    'The ordinary nine-label translation action has48 fixed grids and a unique fixed lift, giving a trivial configuration-kernel centralizer',
    'The map sends each configuration to its differences from label0. Its fixed equations give exactly Hom_inj(C3^2,T[3]); the universal cover is contractible by the actual rank2..9 tower. Smith acyclicity and discreteness give the unique fixed point. The parameter a corresponds to T_-a/3 and is compared with the other convention by a->-a.')
add('A.4.47','A.4.46; A.4.7 graph homology; two-row LHS restriction maps; explicit bounded cellular Tate complexes; A.4.24 label-period certificate; A.4.42 aligned ordinary normalizer', 'Task A.4; Lead 1(2)',
    'An explicit characteristic finite configuration refinement recognizes the canonical translation normalizer and centralizer at the old joint output',
    'Two actual restrictions kill positive cohomology in each free-extension step.289 characteristic covers and two cyclic Tate comparisons kill the unwanted projected deck centralizer. The subgroup K0 semidirect Gamma(3) has index24*9!, and its induced finite map retains K0/V exactly. Removing the actual affine source representative proves both normalizer-image equalities and the ordinary forgetting comparison. The extra induced period map identifies exactly the finite configuration semidirect subgroup; competing-complement fusion requires the further marking proof.')
add('A.4.48','A.4.45 exact fifth retraction; actual eight-map rank97 source; B.2.7--B.2.9 full canonical image equality; B.2.26 harmonic frame; natural integral H2 comparison for an odd kernel', 'Task A.4; Lead 1(2)',
    'The actual ternary five-point level admits a genuine full parity-one identity parameter with cubic frame1 and a lifted harmonic frame',
    'The common source has order1728*3^97, kernel3^98 overQ576, named generator orders18 and pure abelianization C18^2. Sylow conjugacy and the actual H2 isomorphism on2-primary central kernels lift the harmonic frame through the full canonical cover. Normalization preserves every source coordinate. The exact signed base frame is [[9,4],[8,9]] modulo12 and the shear is1; hence Delta1. Every one of the eight insertions and the full target pentagon is identity.')
add('A.4.50','A.4.48 canonical-cover comparison; B.2.8 andB.2.26 original full source; exact abelian C_n^2 join; compactness; executed cap216 and source-order certificates', 'Task A.4; Lead 1(2)',
    'One genuine normalized parity-one parameter is identity in every finite odd-kernel refinement of the original full source',
    'The added abelian kernel has odd exponentm and order dividingm^2 for n=12m. The same full canonical lift and exact normalization work for every finite intersection; closedness gives the simultaneous element. The concrete joint ternary/cap/Schreier source has generator order36 and pure abelianization C36^2. Both cap IV evaluations and all eight ternary five-point insertions are identity for the same actual parameter.')
add('A.4.51','A.4.45 literal split retraction for m=6; full binary s-vertex module rank97; all eight base source fibres; ternary r-centralizer gate; original signed covariance', 'Task A.4; Lead 1(2)',
    'Every actual multiplier-one parameter in the identity fibre at the specified mixed modulus-six five-point quotient has Delta0',
    'The binary vertex source is exactly B/(Kprime K^2), of order576*2^97. Its correction space has rank45 and all eight pure s-centralizer residues are tested; only identity lifts, with explicit dual obstructions for every failed residue. The same fifth insertion retains both binary and ternary modular sources, forcing both signed frames and the shear to1. The other finite parameter fibres remain to be enumerated.')

'''
t = t[:pos]+addition+t[pos:]
t = t.replace('A.4.1--A.4.45; executed', 'A.4.1--A.4.48; A.4.50--A.4.51; executed')
p.write_text(t)

p = ROOT / 'part_a_finite.tex'
t = p.read_text()
start = t.index('discrepancy between finite CM descent')
end = t.index('\\end{result}', start)
t = t[:start]+'''discrepancy between finite CM descent and ordinary
forgetting at the original joined output. A.4.44 supplies
the exact cubic orbifold source and simultaneous relative
cone and cusp detectors. A.4.45 proves the split five-point
retraction retaining the full ternary modular detector.
A.4.46--A.4.47 now construct the normalized configuration
source and an explicit characteristic refinement recognizing
the canonical translation normalizer at that output.
A.4.48 constructs a genuine parity-one harmonic identity
parameter in the ternary five-point level. A.4.50 extends
it simultaneously through every odd refinement of the
specified full source, including the joint cap tests.
A.4.51 then excludes every parity-one identity parameter
at the mixed modulus-six level through the actual binary
and ternary source maps. The remaining nonidentity fibres
and the complete common finite census are still being
examined. The compactness result below supplies existence
but no substitute for that computation.
'''+t[end:]
p.write_text(t)

p = ROOT / 'GT_TOWER_CHECK_report.md'
t = p.read_text()
t = t.replace('Current state at checkpoint08', 'Current state after checkpoint08')
t = t.replace('A.4.1--A.4.45', 'A.4.1--A.4.48; A.4.50--A.4.51')
old = '| A.4 |'
lines = t.splitlines()
for i, line in enumerate(lines):
    if line.startswith(old):
        lines[i] = '| A.4 | A.4, A.4.1--A.4.48; A.4.50--A.4.51 | Open; explicit canonical translation-normalizer recognition is proved; genuine harmonic identity parameters survive the ternary level and all stated odd refinements, while the mixed-modulus-six identity fibre has parity0; competing-complement marking and the complete nonidentity shadow census continue |'
t = '\n'.join(lines)+'\n'
start = t.index('Eighth-hour checkpoint,')
end = t.index('\n\nThe manuscript proves', start)
t = t[:start]+'''Ninth-hour working manuscript, 17 November 2026. Research began at approximately23:45UTC on16November. Checkpoints01--08 remain unchanged; checkpoint08 was verified and saved with345pages,165numbered statements and91full-page visual inspections. The current new proofs are being integrated and will receive a new complete build and visual inspection before the next hourly archive. The next checkpoint and progress review are due at approximately08:45UTC.'''+t[end:]
anchor = '## Part B: actual images, descent, involutions and arrows'
section = '''## Ninth-hour advances on the main finite task

A.4.46 identifies the actual normalized torus configuration space, its48 fixed grids and the unique fixed point in its universal cover. A.4.47 replaces an appeal to a completed centralizer by an explicit finite construction: a cohomology-killing recursion through the eight free extensions, followed by289 characteristic cover refinements and two finite cyclic Tate comparisons. Its actual induced mapping-class quotient retains the prescribed configuration quotient injectively and projects its canonical translation normalizer and centralizer exactly onto the ordinary images. The aligned CM descent and ordinary forgetting maps therefore agree after this specified projection. The additional finite period coordinate identifies the exact configuration semidirect subgroup for transport.

The common source of the eight ternary five-point insertions is calculated coefficientwise. Its base has order288; its new module has dimension97, and the actual B-source has order1728*3^97. The module maps onto the retained modular vertex image with a two-dimensional kernel on which s acts by-I and r byI. Its named generators have order18 and its pure abelianization is C18^2. Root reproduced every matrix and the complete source-order calculation, including an independent int64 replay matching every retained array.

A.4.48 lifts the original harmonic frame through the full canonical cover of this source. The actual homology map is an isomorphism on2-primary central kernels because its source kernel overQ576 is odd. It kills the full central commutator obstruction, and the exact normalization preserves every recorded finite value. This gives a genuine full Delta1 parameter whose eight ternary insertions and pentagon are all identity. The precise signed frame is [[9,4],[8,9]] modulo12. A.4.50 extends the construction simultaneously through all odd refinements of the original full source by compactness. It also retains the two cap216 evaluations and every indicated deck and Schreier coordinate in one actual common source of generator order36 and pure abelianization C36^2.

A.4.51 computes all eight pure binary harmonic-centralizer residues in the full actual97-dimensional source module. The correction space has rank45 and only identity lifts; explicit dual functionals exclude every other residue. The literal fifth retraction at modulus6 simultaneously retains this binary source and the ternary cubic source, so an actual multiplier-one parameter with identity fifth insertion has both signed frames equal toI and Delta0. This is an exact identity-fibre exclusion. The remaining nonidentity records are under active investigation.

Root proof-review details, exact opened primary locations and every replay are preserved in `notes/ninth_hour_root_proof_audit.md` and `notes/reproduced/ninth_hour_sources/`. The finite competing-complement fusion and its orientation marking are being completed separately; no unfinished comparison is used as a proved premise of these integrated results.

'''
assert anchor in t
t = t.replace(anchor, section+anchor)
p.write_text(t)
print('Integrated A.4.46--48, A.4.50--51 and the exact common-source proof; prior files preserved.')
