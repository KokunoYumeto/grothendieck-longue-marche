# Nonlinear Wajnryb finite source calculations

## Completed S3/S4 batch (E76)

The exact free-group model is `code/de_wajnryb_free_model.py/.json/.out/.err`.
It verifies all inverses, all A/B/C/C-prime relations in genera2,3,4,
boundary preservation, the exact positive inner boundary-twist action,
and the integral comparison to E72. The initial guessed negative sign
failed the literal assertion and is preserved in
`research/E72_nonlinear_initial_boundary_sign/`.

The finite models are the exhaustive actions on all epimorphic closed
surface tuples modulo all target automorphisms:

| group/genus | all tuples | boundary tuples | epimorphic tuples | points | raw/faithful source |
|---|---:|---:|---:|---:|---:|
| S3,2 |1296|486|360|60|1080/48|
| S3,3 |46656|16038|15120|2520|75600/342|
| S4,2 |331776|34176|21600|900|16200/552|

The constructors are `de_wajnryb_s3_model.py` and
`de_wajnryb_s4_model.py`. Their actual target point maps, all original
epimorphism codes and their orbit maps, multiplication tables and
automorphism maps are retained. S4 has two actual mapping-class orbits,
sizes540 and360; both are retained. Its automorphism proof tests all36
Cayley candidates, obtaining exactly24 inner maps. Its complete subgroup
enumeration has30 subgroups and the8 maximal proper subgroups.

The `_source.py` programs retain all six source cosets and every required
NS action evaluation. Faithful compression uses actual B-set point
intertwiners. All97 N-basis sixth powers and all4656 pair commutators
vanish in each source, proving the complete factorization through G6.
The S3 source orders, separately computed in the saved ambient arrays,
are216 in genus2 and46656 in genus3; no common-map conclusion uses these
orders alone.

The `_fibres.py` programs evaluate all24 original E17 f-words, check all37
old/homogeneous correction generator words have identity source value,
and thereby retain all18 parameters and both multiplier residues.
All864 old points pass all Wajnryb relations. Each model has3 distinct
corrected generator tuples. Explicit simultaneous point intertwiners
prove each corrected image is the entire original finite target.
The S3 generators have order6; S4 generators have order12, so every
multiplier lift1 modulo72 is covered. Identity controls pass.

The S4 source/fibre engines were generated from the S3 engines with
retained provenance `de_wajnryb_s4_engines_prepare.json`. Their first
metadata/source logs are preserved in
`research/E74_S4_initial_engine_metadata/`. Before the S4 fibre run, the
period was explicitly changed to12 and the generation graph was made
to retain both complete orbits. No mathematical negative run is being
treated as an exclusion.

Formal proof: `sections/E_wajnryb_surface_covers_agent.tex` (E76).
Scope: the actual finite maps and complete fixed-G6 fibres. The tests
retain every later correction in N-prime N^6. They do not resolve the
full-GT image of Delta.

## Next source

`de_wajnryb_a5_model.py` is constructing the same genus2 surface-cover
action for A5, using all12,960,000 tuples in a streamed enumeration.
Aut(A5)=S5 is proved from the actual five Klein-subgroup action; no
source factorization or fibre outcome is asserted before computation.
