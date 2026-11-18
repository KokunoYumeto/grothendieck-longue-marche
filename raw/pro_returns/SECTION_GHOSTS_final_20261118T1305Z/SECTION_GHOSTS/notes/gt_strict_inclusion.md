# The actual full gentle strictness witness (E.197–E.198)

## Question and outcome

The remaining clause of historical GT A.7 was the strict inclusion of the
full profinite GT group in the kernel of its original signed CM character.
E.191 already proves full character vanishing, and E.97 gives a full gentle
element of character one. The new proof supplies a different full gentle
element whose square has character zero and a nonzero pentagon.

The argument is written in `sections/part_E_gt_strict_inclusion.tex`.
The owner proof, parent full proof/source/code review, and both independent
peer full proof reviews are positive. Cohomology also reread E.57 in full
and reran the exact certificate. The historical A.7 row is now confirmed
on these complete in-run proofs, not on the historical register.

## Exact finite input

The seven Lyndon coefficients of h are those of E.197.1, in degree seven.
The standard convention is the longest proper Lyndon suffix, with x<y.
Expansion gives 62 nonzero integer associative coefficients, with largest
absolute value32. With z=−x−y and k=−h(z,x), all four identities in E.197.3
hold over the integers. Both actual S3 generator actions have outer
derivation difference −ad(h). This is checked on both free generators.

The infinitesimal braid map t_ij→(ij) in the integral group ring of S4
obeys every defining infinitesimal braid relation. The complete five-term
pentagon image is exactly160((34)−(12)). Its square-witness counterpart
is320((34)−(12)); modulo eleven these coefficients are respectively6 and1.

`code/check_gt_strict_inclusion.py` is standalone and uses only the Python
standard library. Its JSON companion retains all polynomial coefficients,
the six literal modular conjugations, residual sizes, and the entire
nonzero group-ring image. Deterministic payload SHA256:

`de390b3b14e063e6ea168c52f52f9a0af7c6066d4cc148855444a490a9c11dba`.

## Why this is an actual full-group witness

The proof does not exponentiate a rational Lie polynomial and assume
integrality. It first realizes the special derivation integrally in the
free pro-eleven group by successive ordinary lower-central error
cancellation. At degree m the correction map is
(a,b)→[a,y]+[b,−x−y], whose integral image is all of L_m. Every finite
eleven-group kills sufficiently deep ordinary commutators, so the
conjugators converge and their product equation is exact. The resulting
endomorphism is an automorphism by its Frattini action.

The special IA outer group and its closed filtration kernels are
pro-eleven. Fixed points of the genuine geometric S3 lift across the
leading quotient by coprime complement conjugacy, proved by central
induction in finite eleven-kernels and compactness. The centerless actual
modular extension recovers an automorphism of B_11; its cusp is fixed
literally, and a specific x-power correction makes the pair conjugator
pure. Nilpotent centralizer calculations show that the normalized pair
still has precisely h as its first term.

This actual B_11 action is placed in the eleven-primary component of the
actual pronilpotent fibre product over S3, with identity actions elsewhere.
The positive s/r conjugators can be chosen in the pro-eleven kernel by the
same coprime argument. E.57, whose finite character-count proof was
independently reconstructed and reviewed in this run, then gives a full
ordinary peripheral lift. Its cusp conjugator lies in R_nil(F); one inner
correction by its inverse fixes the full cusp without changing any retained
quotient coordinate. The two exact gentle cycles follow from the literal
s²=r³ relations, and the pure restriction is an actual automorphism.

The final pentagon is detected at fixed class seven. The integral pure
braid graded presentation is a published input; its homogeneous factors
are torsion free. The central full twist splits off, and removing it
does not change the degree-seven factor. Hall collecting coordinates of
the actual class-seven nilpotent quotient have denominators prime to
eleven and thus give finite eleven-group quotients by reduction. This
retains the nonzero degree-seven coefficient. No formal Lie solution is
being mistaken for the image of an actual source automorphism.

## Retrieval and primary sources

The following earlier source was recovered locally and fully read as a
search lead:

- `symmetry_retrieval/lm4_background/LM7_PUSH_checkpoint_09/sections/D_modular_coprime_agent.tex`, D.44, especially the actual centerless pullback and integral realization paragraphs.
- `symmetry_retrieval/lm4_background/LM7_PUSH_checkpoint_09/sections/D_full_weight9_agent.tex`, D.52, actual local-to-full argument.
- The associated weight-five source was also read to check conventions.

Neither old unrefereed theorem is cited as a proved input. The new source
reproves all the needed steps and replaces the imported historical
weight-nine nonvanishing claim by an explicit independently checked
degree-seven calculation.

Library searches for exact `GT_TOWER_CHECK`,
`GT_TOWER_CHECK_background.zip`, `part_b_weight9.tex`, and
`part_b_finite_images.tex` did not retrieve the historical missing Part B
proof. A broader phrase search for `weight-nine pentagon gentle` returned
an earlier prompt, not the proof. These negative retrieval results do not
assert that the files never existed.

Primary published source opened:

Cohen, F. R., & Prassidis, S. (2006). On injective homomorphisms for pure
braid groups, and associated Lie algebras. *Journal of Algebra, 298*(2),
363–370. https://doi.org/10.1016/j.jalgebra.2006.01.047

- Author-hosted published PDF: https://www.samos.aegean.gr/math/prasside/injective.pdf
- Opened web references: `turn329331306view0`, `turn329331306view1`.
- Exact locator: §2, printed pp366–367, integral infinitesimal braid
  presentation and split free-Lie decomposition.
- Exact locator: Lemma2.2, printed p368, centralizer of a generator in the
  integral free Lie algebra, including its tensor-algebra proof.
- Author preprint was independently opened at
  https://arxiv.org/pdf/math/0404278 (`turn475413448view1`); its §2 is
  author pp4–5. The published PDF is used for the final locators.
- Publisher metadata was verified by search (`turn871844802search0`);
  direct publisher open returned403, so no full-text claim rests on it.

Searches also included `Falk Randell lower central series fiber type
arrangement pure braid Lie algebra 1985 pdf theorem` and
`Kohno 1985 holonomy Lie algebra pure braid group Malcev completion
infinitesimal braid relations pdf`. Those led to the opened primary
Cohen–Prassidis source; no unopened Falk–Randell or Kohno theorem is used.

## Scope retained

The conclusion is the exact qualitative full-group strict inclusion
claimed in A.7. It does not identify every original finite Part B witness,
normalize every historical relative family, or supply the original
A.4.57 explicit compiler constants. C5 and A.4.57 retain their separate
historical scope until independently settled.

The final certificate also evaluates the literal five-cycle sphere pentagon
of Schneps2006 Definition1.1 p657, obtaining the negative of the displayed
2-versus-3 braid expression. Its central-shift map is explicit in E.198.
The primary source was reopened at https://webusers.imj-prg.fr/~leila.schneps/automorphisms.pdf
(web ref turn978464985view0); that page also recalls the faithful Galois inclusion.
