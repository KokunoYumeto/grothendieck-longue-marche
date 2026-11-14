# E.59: the complete SL2(F3) Ferrari correction fibres

Date: 2026-11-13. Owner: arithmetic_sections.

## Exact result

The universal Ferrari target is built from all16 epimorphism kernels of
the free Ferrari group onto SL2(F3), with the actual Nielsen maps and
their uniquely determined automorphism transporters. Its order is
43,486,543,872 = 2^29 3^4. The free image has order2^14 3^2; the Nielsen
image has order2^15 3^2. No independence of the sixteen SL2 factors is
assumed.

The actual source retains all six standard pure evaluation pairs and all
six B/F cosets. Its faithful action compresses from13824 to1956 points
using explicit isomorphisms of transitive B-sets. Its order is
48,922,361,856 = 2^26 3^6. The image P of the actual rank97 subgroup N_B
has order2^20 3^4. Its index576 equals the original index of N_B, so the
source retains the actual Q=SL2(Z/12)/± quotient.

The exact image C of N_B' has order512, exponent4, and centre8. The
coordinate maps (q,i)=(0,0),(0,1),(0,3), in the saved zero-based orders,
identify C with Q8^3: each coordinate has an explicit quaternion
multiplication table and the joint map is a bijection of512 elements.
All97 sixth powers lie in C. Thus the whole image of K6=N_B' N_B^6 is C,
and all of C is already realized by literal N_B' words. This proves
the exact image of K6 intersect F', not merely a lower bound.

For each of the24 retained E.17 G6 words, the whole fibre has512 possible
values. Exactly4 satisfy both complete gentle norms in the actual common
source. Exactly2 also satisfy the full group pentagon and all three
four-strand braid relations. All96 gentle values generate the entire
three-strand source; all48 pentagon values generate the entire target.
Both full twists are fixed at every one of the48 points. The source
generation calculation is supplemented by the exact Goursat argument
in the manuscript to retain the common G6 factor.

The corrected words retain the old G6 value. A separate actual matrix
calculation gives24 distinct CM pairs and12 extra pairs, with the
nontrivial integral cusp gauges fully retained. Consequently every
admissible retained CM matrix pair survives this finite test. This does
not give a compatible full profinite pentagon lift, and does not enumerate
the other affine G6 points or multiplier residues in the same matrix fibre.

## Actual maps and generation argument

The source is rho:B→G24 obtained from theta_i(b_q w b_(qw)^-1).
Its common quotient with G6 is G24/C. The image of B in G6×G24 is
exactly G6×_(G24/C)G24: a discrepancy over the same common value is
corrected by an actual K6 word mapping to C.

For a corrected word f, the source generators are S=sf and R=f^-1 r.
Their product is the old tau. Each retained old normalized point acts
on Q by the actual inner cusp gauge g=q(x)^h, so the corrected common
Q-map is Inn(g) q and has kernel N_B. The images of N_B in the old and
new factors are therefore a subdirect product. The old N_B image is
abelian; the common quotient of the new N_B image kills its derived
group C. Hence the corrected image contains the whole kernel C over
G6. Surjectivity on both displayed factors consequently gives the
whole actual common source.

Every source and target order is certified by the exact complete
Schreier implementation. Each added strong generator has an original-word
DAG, every final Schreier relation is sifted, and the independent Python
array reader re-evaluates all saved strong words. There are96 source
and48 target certificates in a_cm_sl23_generation_certificates.

The source CM frames before gauge are A,beta,V=1. The actual common
left gauge changes them to (gA,g beta,g), not to (gA,g beta,1).
Thus T=(gA)^-1g=A^-1 and W=(g beta)^-1g=beta^-1. The independent label
program checks these equations, the corresponding inner Q-action on s,r,
and the positive E.1 signs. It does not replace a nontrivial gauge by1.

## Executed programs and saved results

- a_cm_sl23_model.py: exact matrix group, all automorphisms, all epikernels,
  actual Ferrari maps and target orders; PASS,0.762s.
- a_cm_sl23_source.py: literal N images and initial retained-word probe;
  PASS,15.867s. This is the input for the complete correction calculation.
- a_cm_sl23_induced.py: all36 induced coordinates, faithful compression,
  literal N and H words, source permutation inputs; PASS,4.691s.
- Exact source chains: B order2^26 3^6; N order2^20 3^4; N' order512.
  Auxiliary H computations are retained separately and are not needed
  for the E.59 correction theorem.
- a_cm_sl23_corrections.py: complete nonabelian512-element correction
  enumeration and24 exhaustive fibres; PASS,47.601s.
- a_cm_sl23_generation.py: all96 source and48 target generation checks,
  every literal word, independent word-DAG replays, exact Q8^3 maps;
  PASS,225.538s.
- a_cm_sl23_periodic.py: both literal full twists at all48 pentagon points;
  PASS,10.266s.
- a_cm_sl23_cm_labels.py: every actual old frame, its common left gauge,
 24 distinct pairs and12 extra pairs; PASS,1.699s.

The compiled Schreier executable used for the authoritative generation
run has SHA256
479421ccc08c5fb58e5dac2328736471cd071175ec237d5c9de3322806823fa1.
Its source has SHA256
1446a8b86d6412544db6b254c2fa3b073b536d8cdadfd49eb86c5382716b9b32.
The exact source file is retained and can be compiled independently.
Timing fields are descriptive and are excluded from semantic replay
comparisons; all mathematical arrays, words, tables, counts, and maps
are compared exactly.

## Preserved unsuccessful or incomplete stages

1. The initial word-only probe finds that only retained index5 passes
   without correction. Its output explicitly says this does not exclude
   the fibre. The full512 calculation repairs every one of those
   representative-word failures.
2. The first correction invocation was interrupted by incoming task
   steering before producing output. Its empty stdout/stderr are kept as
   a_cm_sl23_corrections_interrupted_initial.*; the completed run is separate.
3. The first generation driver stopped before a generation claim because
   a list was concatenated with the tuple returned by the exact fword
   rewriter. The failed source and outputs are kept as
   a_cm_sl23_generation_failed_tuple_initial.*. Converting that tuple to
   a list is the only correction; the completed run then passed.
4. The first CM-label helper incorrectly asserted that every retained
   integral cusp gauge had trivial Q-image. Its assertion failed before
   any output claim. The full source and failure are retained as
   a_cm_sl23_cm_labels_failed_trivial_gauge.*. The corrected program
   retains the actual common left gauge and verifies the exact morphism
   above. The earlier manuscript text is preserved in
   E59_before_Q_gauge_correction.tex. No correction count or group-order
   computation used the failed trivial-gauge assertion.
5. The first written TeX draft and an initial31.78047pt filename overflow
   are preserved. The final source is compiled in an isolated directory;
   the active paper assembler and build were not modified.

## Remaining E.3 work

This complete finite target gives no exclusion of the extra CM coset.
The full question still requires an actual identity forced by the
pentagon in every quotient, or a compatible full lift. The current
parallel theoretical route concerns the genus-one relations and their
precise restriction to full GT. The SL2(F3) calculation can be combined
with further actual target quotients only after proving the common
source and kernel maps; no direct-product or cofinality claim is assumed.

The independent E.58 proof review is in A_E58_independent_review.md.
It concerns the full gentle source theorem and does not assert its
constructed element satisfies the pentagon.
