# EXIT_ONE_TYPE: research, proof, and source audit

## Status

**INCOMPLETE.** The comparison question for good smooth proper algebraic
threefold completions of a fixed open variety is not proved or refuted in
this draft, even in its projective simple-normal-crossings subcase. Its exact
formulation is `P3c-general`. The toric case is proved. Within the projective
simple-normal-crossings subcase, the case of a birational morphism and the
log-crepancy reduction for a general birational comparison are proved. The
unrestricted analytic version and an unrestricted stack version are refuted.
No implication from the proved reductions to the remaining general conjecture
is claimed.

The other numbered statements are classified individually as **Proved**,
**Refuted**, or **Known** in the results register. “Proved” means that a proof
is supplied in this draft, with its stated dependencies; it does not mean
that an external referee has certified it. “Known” identifies a result whose
substantive theorem is attributed to the verified literature. Counterexamples
are accompanied by the calculations establishing their stated properties.

The assembled register contains **63 numbered statements: 53 Proved, 8 Refuted,
1 Known, and 1 Open**. The readings register has **23 rows**. The bibliography
has **37 entries**, including the two official manuscript facsimiles with
explicitly descriptive titles and no inferred composition dates. All nine
mathematical check programs executed successfully; the two independent
identity implementations agree on their complete expanded data.

The paper and this report distinguish mathematical corrections from manuscript
readings. A correction that makes a theorem true is not evidence that the
manuscript actually contains that correction. Paleographic uncertainty is
preserved in `EXIT_ONE_TYPE_readings.csv`.

## Coverage of the requested parts

Stable identifiers below also appear as labels in the LaTeX source and as IDs
in the CSV. The final results CSV records the actual printed statement numbers.

| Task | Outcome and exact location | Material qualification |
|---|---|---|
| 1(a) | Normal-link mapping-space formula, coherent normal-bundle and flag construction: `P1a1–P1a2`. | Branch monodromy and the full étale Čech nerve are retained. A global holomorphic tubular embedding is not assumed. |
| 1(b) | Exact ordinary-exit criterion, full-to-relative implication, adjacent-test counterexample, and transgression correction: `P1b1–P1b3`. | Adjacent cyclic injections do not establish independence of a full meridian lattice. |
| 1(c) | Three reconstruction operations and two separating counterexamples: `P1c1–P1c2`. | Fundamental-groupoid reconstruction of the one-type needs no asphericity. Full derived reconstruction from one-types needs aspherical refined values. Ordinary exit truncation additionally needs full inertia injection. |
| 1(d) | Both shapes, their comparison fibres, connectivity, and first possible obstruction module: `P1d1–P1d3`. | The first nonzero failure need not be in degree two. The universal-cover bar uses the fundamental-groupoid local system. |
| 1(e) | Complete explicit categories for punctured spheres, stable five-pointed rational curves, toric surfaces, products, and the cusp: `P1e1–P1e5` and the five `P1e-…` cusp statements. | Mapping spaces, group actions, compositions, and nontrivial circle components are specified. The affine cusp, proper cusp, and stable orbifold replacement are different examples. |
| 2(a) | Admissible blow-up lattice calculation and the sharp stratal/non-stratal distinction: `P2a`. | A non-stratal admissible centre produces a nonzero full-lattice kernel. |
| 2(b) | Functorial exit comparison, normal-boundary comparison, and preservation of the proper end system: `P2b`. | Preservation of the open complement or of its end does not imply preservation of the ordinary exit category. |
| 3(a) | Surface core, corner refinements, minimal-model criterion, six requested classes, and analytic/stack scope corrections: `P3a-…`. | Analytic markings and marked bimeromorphic classes must be specified. The analytic torus has good Hopf compactifications in addition to toric ones. |
| 3(b) | Discrete elementary-fibration injection, profinite completion, and the corrected tower/stable-family statement: `P3b-…`. | A stable vertical family does not repair a bad base. Profinite assertions require the stated completed-lattice hypothesis or compatible tower construction. |
| 3(c) | Toric factorization, Mori hyperbolicity, the morphism case, and log-crepancy: `P3c-toric`, `P3c-Mori`, `P3c-morphism`, `P3c-crepant`. General claim: `P3c-general`. | **INCOMPLETE:** a common good/toroidal resolution of arbitrary good projective pairs is not obtained. Weighted toric factorization does not settle unweighted regular strong factorization. |
| 4(a) | Component-Segal counterexample, correct full-flag dual model, and categorical/spatial fibre formulas: `P4a1–P4a2`. | Taking connected components does not preserve the internal category's fibre products. |
| 4(b) | Exact contractibility consequence and compact link obstruction: `P4b`. | Contractible closed normalized intersections reconstruct the divisor from the dual; they do not identify the normal boundary with that dual. |
| 4(c) | Blow-up invariance, correctly scoped independence, analytic counterexample, and weight formulas: `P4c1`, `P4c3`, `P4c2`. | Algebraic properness and the specified bimeromorphic comparison matter. Degree zero and disconnectedness are handled explicitly. |
| 4(d) | Tropical link/dual identification, graph-groupoid distinction, genus-zero homotopy type and integral checks: `P4d1–P4d2`. | Coarse simplex quotients and homotopy quotients by graph automorphisms are different. |
| 4(e) | Exact information retained and lost by the maquette, with good projective examples: `P4e`. | The same dual can support links with different first Betti numbers; in the analytic torus example the same link has different duals. |
| 5(a) | Refutation of the two-depth groupoid colimit, sharp cutoff, and correct one-type consequence: `P5a1–P5a3`. | The bicategorical groupoid colimit is distinguished from a strict group colimit. The conclusion concerns the normal boundary, not the ambient compactification. |
| 5(b) | Infinite multicurve-poset fibre, genus-zero connectivity, independent small tests, and higher-genus counterexample: `P5b1–P5b4`. | A finite quotient complex is not substituted for the infinite fibre. The empty multicurve is included when the dimension cutoff reaches the open stratum. |
| 5(c) | All-genus two-level presentation, explicit presentations of the two pure mapping class groups, and complete identity families: `P5c1–P5c4`. | Local groups retain their internal relations. The higher-level extrapolation in all genera is false. Boundary-circle central extensions are not silently discarded. |

## The principal mathematical distinctions

### 1. Ordinary exits are controlled by full lattices

For a normal-crossings pair, the exit mapping space from a deeper stratum
to a more open one is the homotopy fibre of the two endpoint maps of the
corresponding angular incidence space. In a local chart the angular fibre
is a torus. Globally its branch choices form a finite incidence cover and
its circles are glued by the normal line bundles. This supplies the precise
object to which the holink comparison is applied (Miller, 2009, Theorem 4.9;
Jansen, 2024, Proposition 3.16 and Corollary 3.17).

The exact criterion is

\[
\operatorname{Exit}(X,D)\text{ is ordinary}
\quad\Longleftrightarrow\quad
\begin{cases}
\text{every open incidence stratum is aspherical},\\
\mathbb Z^{I_x}\longrightarrow\pi_1(X\setminus D)
\text{ is injective for every }x.
\end{cases}
\]

The full lattice is essential. The blow-up of the two affine coordinate axes
at a smooth point of one axis, with one additional exceptional point removed,
has aspherical strata and injective adjacent normal maps. At the new node,
however, the two normal meridians have the same image. The full map sends
`(a,b)` to `(a+b)e_x` and has primitive kernel `(1,-1)`.

The normal-bundle exact sequence begins with the spherical transgression

\[
\pi_2(S)\longrightarrow\mathbb Z^r\longrightarrow\pi_1(P_S)
\longrightarrow\pi_1(S)\longrightarrow1.
\]

Its first map is given by normal Chern numbers. Thus vanishing of `pi2(S)` is
sufficient for fibre-lattice injection, but it is not necessary. A trivial
normal line over a sphere has zero transgression, whereas the normal line
of a plane conic has degree four and its circle bundle has fundamental group
`Z/4`. The base in the manuscript's sequence (37) must be the appropriate
open incidence stratum.

### 2. Derived reconstruction and ordinary truncation are separate

The full coherent diagram of strata, normal links, and flags reconstructs
the ambient homotopy type. Applying the fundamental-groupoid functor
reconstructs its one-type because this functor preserves colimits in the
category of groupoids. If all open strata are aspherical, the refined link
values are also aspherical, so replacing them by their classifying
fundamental groupoids preserves the entire derived homotopy colimit.

Taking path components of the exit mapping spaces is a different operation.
For the one-punctured sphere, the derived groupoid diagram is
`* <- BZ -> *`, whose homotopy pushout is a sphere, but the ordinary exit
category is an interval. This example satisfies stratum asphericity and
fails meridian injection. The product of a projective line with an affine
line, with the zero section as boundary, gives the opposite separation:
the meridian injects, but the closed stratum is not aspherical and its
one-type diagram loses the sphere.

The genuine constructible infinity-topos has shape `B Exit`, while the
infinity-topos associated with the ordinary constructible-set topos has
shape `B(h Exit)`. Their comparison is always two-connected. More generally,
if every mapping-space component is `(r-1)`-connected, the comparison is
`(r+1)`-connected. Its first possible fibre group is the cokernel of the
alternating face map from degree-two to degree-one homology of the lifted
enriched bar. The lifting is performed using the fundamental-groupoid
local system, so the resulting module action and face coherences are
well-defined.

Affine quadrics show that the first nonzero disagreement can occur in any
degree `m >= 3`: the quadric is diffeomorphic to the tangent bundle of the
real sphere, and the ordinary exit category of its trivial-line zero-section
pair has an initial object. The comparison fibre is therefore the sphere.
The calculation is not restricted to a rank discrepancy in degree two.

### 3. The cusp requires three distinct models

The affine cuspidal fibration has trefoil group

\[
G=\langle a,b\mid a^2=b^3\rangle,
\qquad h=a^2=b^3,\quad m=ab^{-1}.
\]

The three exceptional multiplicities are `2, 3, 6`, and their self-intersections
after the full embedded resolution are `-3, -2, -1`. The two tail nodes
have rank-one kernels, while the cusp/central-node peripheral pair
`<m,h>` is a free abelian group of rank two and injects. The paper supplies
the entire eight-stratum exit diagram, including the circle components
at the two defective nodes, the central free-group actions, and the
gluing homomorphisms that determine composition.

The proper Weierstrass family has a different open group,
`Z^2 semidirect_A Z`, where `A` has order six. There `m=(0,1)` and
`h=(0,6)`, so the corresponding third-node lattice also has a kernel.
The affine and proper calculations are not interchanged.

After degree-six base change, the stable orbifold model retains the
finite stabilizer action. Its closed group is `C2*C3` in the affine case,
or `Z^2 semidirect C6` in the proper case. The normal circle maps to the
infinite central element `h`; centrality and the degree-six winding are
both used to identify it. The resulting two-stratum exit category is
ordinary. Rooting an unchanged defective boundary only replaces a lattice
by a finite-index sublattice and cannot remove a nonzero kernel. This
remains true for completed lattices. Finite monodromy by itself is not
an obstruction to goodness.

### 4. Compactification statements depend on their category

For a simultaneous-coordinate admissible blow-up, the new exceptional
meridian is the sum of the old meridians containing the centre. A
non-stratal centre leaves a point where all those strict transforms meet
the exceptional divisor, producing the explicit kernel
`(-1,...,-1,1)`. A stratal blow-up instead gives unimodular lattice charts.
The proof also tracks the reverse implication without assuming an
unjustified global map from a normal bundle into the open complement.

For surfaces, the paper uses the boundary core obtained by removing
rational tails, then analyzes corner blow-ups, corner contractions, and
minimal pairs. The statements are made within the specified marked
bimeromorphic class. The six requested examples are treated with the
same criterion. Algebraic and arbitrary holomorphic markings are
distinguished, including the relative Picard parameters for the product
of `C*` with a three-punctured sphere.

There are good analytic compactifications of the analytic two-dimensional
torus with different dual complexes. The projective toric pair has circle
dual; the explicit Jordan Hopf compactification has elliptic boundary and
point dual. Their normal boundaries are both three-tori. The quotient
coordinates, normal derivative, and primitive meridian winding are
computed in the paper. Ueda's (1979) theorem supplies the relevant analytic
classification context. The stronger unrestricted analytic comparison is
therefore false even when both pairs are good.

For stack comparisons, generic boundary inertia is not asserted to be
invariant under blow-up: a codimension-two stabilizer can become generic
on an exceptional divisor. The valid obstruction is instead triviality
of all inertia. A nonidentity stabilizer at a centre fixes an eigenline
in the projectivized normal representation, so some nontrivial inertia
survives the blow-up; representability gives the converse implication.
This prevents the specified rooted stack and scheme models from being
connected by the proposed representable stratal operations.

### 5. What is proved in the projective subcase of the remaining question

A good smooth projective normal-crossings pair admits no nonconstant algebraic map
from the affine line into any open stratum. A map extending to a rational
curve inside one stratum contradicts asphericity and positive Kähler area.
If its point at infinity meets deeper boundary, a sufficiently small
normal push-off produces a bounding loop with a nonzero positive meridian
vector, contradicting the full-lattice injection. Svaldi's (2019,
Theorem 1.1) Mori-hyperbolicity theorem then gives nefness of `K_X + D`.

For a proper birational morphism of good projective pairs, the logarithmic
Jacobian divisor is both effective and relatively nef. The negativity
lemma makes it zero. The logarithmic cotangent map is consequently an
isomorphism, and the explicit monomial-and-unit chart calculation verifies
log étaleness and toroidality. The required chart criterion is verified
against Kato (1989, Proposition 3.12 and Theorem 3.5). Toroidal weak
factorization gives the stated stratal comparison. This does not claim
that every toroidal morphism is itself a sequence of smooth stratal
blow-ups.

For a rational comparison, a common resolution gives

\[
K_W+B=p^*(K_X+D)+A_p=q^*(K_Y+E)+A_q.
\]

The two discrepancy divisors are effective. Applying the negativity lemma
in both directions proves

\[
p^*(K_X+D)=q^*(K_Y+E),\qquad A_p=A_q.
\]

The common effective divisor need not vanish. In particular, the resolution
need not be good, and its logarithmic canonical divisor need not be nef.
The morphism result therefore cannot simply be applied twice. This is
the exact remaining geometric gap within the projective simple-normal-crossings
subcase. The broader proper normal-crossings formulation also requires its
own scope reduction; nefness has not been asserted there without the
hypotheses of the proved theorem.

A focused boundary Atiyah-flop test is also analyzed. The possible numbers
of boundary intersections either contradict the good-stratum conditions,
force a conflicting stratal/non-stratal blow-up comparison, or violate
normal crossings. This excludes that proposed counterexample, but it
does not exclude every possible birational configuration.

For the toric case, the paper uses weak factorization with its exact
published source. The weighted theorem of Adiprasito and Pak (2026) is
kept separate from the unresolved unweighted regular strong-factorization
question. No common regular refinement obtainable by smooth star
subdivisions is inferred merely from rational stellar subdivisions.

### 6. Boundary maquettes and modular levels lose different information

The analytic internal incidence category remains valid. Its component
sets need not form the nerve of a category: the explicit free involution
example has two full triple-flag components over one composable pair,
with different composites. Retaining every full flag before taking
components gives the correct semisimplicial dual complex.

The divisor and the normal boundary are recovered from different
space-valued diagrams over this component model. Their maps to the dual
have fibres given by the corresponding path-coherent homotopy colimits.
Adding a constant `BH` factor changes those fibres while leaving the
coarse component complex unchanged. Good projective product examples
already show that the same point dual can have links with first Betti
numbers three and five. The plane line/conic comparison separately
isolates normal Euler numbers one and four.

In the proper algebraic setting, the dual computes weight zero of the
divisor and of the normal boundary, reduced weight zero of compactly
supported cohomology, and top weight of the open complement. The proof
handles `H_D^0(X)=0` separately and states connectedness for the reduced
degree-one formula. The stack version invokes the precise purity,
duality, and weight results in Tubach (2025), rather than treating stack
cohomology as coarse-space cohomology.

For modular levels, the two-depth bicategorical groupoid colimit already
fails on the three-dimensional coordinate example: it gives `Z^4`
instead of the full link's `Z^3`. Depths through `r` recover every
`k`-type uniformly exactly at the threshold `r >= k+2`. Thus depths one,
two, and three recover the fundamental groupoid. This does not require
asphericity of every link value.

The dimension filtration has an infinite multicurve-poset homotopy fibre.
The genus-zero connectivity theorem is proved by link joins and rank
deletion, with compact witnesses in the weak CW topology. In all genera,
the first three levels give nonempty, connected, and simply connected
fibres, and hence the stated ordinary presentation. A higher-level
extension fails at `(g,n,k)=(2,1,3)`, where Harer's curve-complex theorem
gives nonzero second homology. The finite genus-zero dual complexes are
not used as substitutes for these infinite posets.

The explicit group presentations are accompanied by complete first-identity
families: 24 for the nine-generator, 26-relator presentation of
`Gamma_0,6`; 12 for the specified `Gamma_0,5 x F_2` presentation; and
8 for `F_2^3`. Aspherical graph-bundle models and the exact universal-cover
cellular chain complexes establish completeness. Freely reducing the
expanded products checks the words themselves; it does not by itself
prove completeness of the families.

## Manuscript readings and substantive corrections

The readings register gives the requested package/scan locations, the
uncertain place, the mathematical evidence, and its strength. It does not
promote a mathematical inference to a confident transcription. The most
consequential decisions are these:

1. The ordinary-category reconstruction consequence discussed in MPL 147,
   folio 85, requires both stratum
   asphericity and full normal-lattice injectivity. The coherent derived
   groupoid reconstruction has a different hypothesis.
2. The normal sequence (37) uses the open incidence stratum and includes
   the possible `pi2` transgression. Neither the closed intersection nor
   an automatic initial injection can be silently substituted.
3. The transition discussion at MPL 147, scan 146 is handled by coherent
   homotopy specialization and deformation to the normal cone. It is not
   read as a proof of a global equivariant tubular embedding, invariant
   metric, or analytic normal-bundle linearization. The metric and collar
   choices are made on manifold atlas levels; the natural homotopy
   comparisons descend through the full Čech nerve.
4. At MPL 149, scan 133, folio 66, the final `U_infty` was legible in the
   original direct visual inspection and is retained as the reading. The
   replacement by `D` in the contractible-intersection assertion is an
   explicit mathematical correction, not a transcription change.
5. The internal incidence-category construction at MPL 147, scan 114,
   section 11, folio 56 is retained. The false inference is the passage
   to connected components while still expecting the same Segal fibre
   products.
6. At the level diagram (246), coherence two-cells are substantive. The
   two-depth bicategorical colimit is refuted by an exact nonabelian
   presentation calculation; a strict group-colimit simplification is a
   different operation.
7. The `X` in (247) is visibly unstarred in the retained inspection record.
   The correct conclusion concerns the normal boundary `X*`; the pair
   `(C,{0})` separates it from the ambient `X`.
8. The four elementary types at MPL 147, scan 60, folio 29 are
   `(0,4),(1,1),(0,5),(1,2)`. Their role in the low-dimensional
   complex-of-groups presentation is distinguished from the additional
   genus-zero three-dimensional relations among relations.

The final register distinguishes directly reverified passages from wording
that remains uncertain. The original official facsimiles were recovered and
the eleven root-audit scan pages were rendered again. A visible folio number
is recorded as such; a verso is identified as its continuation. No missing
folio number is invented.

## Executed programs and what they establish

All reported checks are exact unless the program explicitly identifies a
symbolic analytic identity. Actual outputs are included beside the programs.

| Program or family | Verified finite content | Limit of the check |
|---|---|---|
| `criterion_checks.py` | Primitive lattice kernels; order-six monodromy; Chern-map Smith forms; cellular Betti numbers; 26-object modular incidence enumeration; smooth toric determinants and self-intersections. | The program checks the stated models, not their geometric identification. |
| `boundary_checks.py` | Component-Segal orbit counts, genus-zero face vectors, signed boundary matrices, exact integer Smith forms, loop-graph inertia, and circle-bundle cokernels. | It computes finite coarse complexes, not the infinite multicurve fibres. |
| `boundary_analytic_checks.js` | Exact quotient-coordinate and normal-derivative identities at a rational contraction parameter; primitive meridian and torus homology checks. | The analytic quotient and its topology are proved in the text. |
| `levels_colimit.py` | The coordinate hexagon presentation and the distinction between truncated and full groupoid colimits. | The uniform cutoff theorem is proved by the skeletal and Čech argument. |
| `levels_braids.py` | All 26 braid-action equalities in a faithful free-group representation and 24 action compatibility checks. | Faithfulness and the group-presentation construction have separate proofs and citations. |
| `levels_stein.py` | Exact Levi-matrix minors with 14 and 93 positive monomials in the two requested cases. | Morse-theoretic connectivity uses the proved exhaustion and the cited theorem. |
| `levels_syzygies.py` and `levels_syzygies.js` | Independent full expansion and free reduction of all 44 identities; their complete JSON expansions agree. | Completeness follows from the aspherical graph-bundle models and universal-cover chain complexes. |
| `compactifications_checks.py` | Exact blow-up lattice matrices for ranks 1–7, cusp substitutions and both group models, root-index kernels, the projective-plane and Hirzebruch fans F0–F7, and fringe contraction. | The finite checks supplement the general proofs; the analytic classification and comparison results are not decided by this computation. |
| `assemble_delivery.py` | One row per numbered statement, no missing bibliography keys, normalized reading schema, and final printed numbering. | Metadata consistency is not formal proof verification. |

For `Delta_0,4`, `Delta_0,5`, and `Delta_0,6`, the face vectors are
`(3)`, `(10,15)`, and `(25,105,105)`. In the last case the projected
integer boundary matrix has 81 nonzero Smith entries, all equal to one.
Thus the computed first homology is zero integrally and second homology
is free of rank 24. The two smaller cases give reduced `H0=Z^2` and
`H1=Z^6`.

The independent identity checkers produce the same 24, 12, and 8 identities.
For the `Gamma_0,6` family, the number of conjugated relator factors in
the fully expanded identities ranges from 8 to 640, and the longest
conjugating word has length 171. The complete expansions are supplied,
so these are reviewable words rather than a list of asserted syzygies.

## Source verification and citation policy

The bibliography records exact versions and locations. It distinguishes
the manuscript or preprint actually inspected from a journal version whose
metadata alone was checked. The detailed source notes under `notes/` record
the primary PDFs and the theorem-level evidence. No claim is made that every
page of a long book or paper was read.

Several corrections are worth recording for reproducibility:

- Miller's article is in volume 4(1), pages **265–273**, with Theorem 4.9
  on page 272.
- The Kato–Nakayama DOI ends in **4041**:
  `10.2996/kmj/1138044041`.
- The two Jansen papers use different version-specific theorem numbers.
  The stable-curves PDF is version 2; the toolbox PDF is version 3.
- Thuillier's theorem numbers cited from the 2006 preprint are not
  represented as independently checked journal numbering.
- The toric weak-factorization source is Wlodarczyk's 2009 publication.
  The 2026 weighted result is not treated as unweighted strong factorization.
- The logarithmic differential criterion is Kato's Proposition 3.12;
  the chart criterion is Theorem 3.5.
- The analytic classification does not rely on an overbroad reading of
  a theorem about minimal surfaces. The required extension of maps to
  affine hyperbolic curves is proved separately using a finite cover,
  hyperbolic length, and removable singularities.

## Remaining work that would close the mathematical gap

The unresolved projective comparison requires an additional geometric
argument. The following are concrete next steps, not consequences already
proved:

1. Determine whether goodness forces the common effective logarithmic
   discrepancy divisor on a resolution to admit an elimination that
   preserves the full meridian injections at every step.
2. Alternatively, show that a log-crepant birational comparison between
   Mori-hyperbolic normal-crossings pairs is toroidal after modifications
   that preserve goodness. The proved morphism case would then apply.
3. Search for a higher-dimensional boundary log-flop escaping the
   explicit Atiyah-flop obstruction. A successful counterexample must
   verify every stratum's asphericity and every full lattice injection;
   checking only peripheral cyclic subgroups would not suffice.
4. Keep the analytic and stack counterexamples outside that restricted
   projective-scheme question. They refute the unrestricted formulation
   but do not settle the restricted one.

No additional assertion about profinite exodromy, Galois reconstruction,
wild reduction, or the later `EXIT_TOWER` project is inferred from the
results here. The stable IDs, printed numbers, dependency columns, and
complete source are intended to make subsequent use auditable.

## Build and delivery verification

The final PDF was compiled with LuaLaTeX and BibTeX using the APA 6 author–date
style supplied by `apacite`. It has **51 pages**. All 51 pages were rendered
and inspected in overview, with full-resolution inspection of the dense
formulas, tables, and bibliography pages identified in
`validation/visual_review.md`.

The final build has **zero TeX errors, missing glyphs, overfull boxes,
undefined citations or references, or unstable labels**. All **22 fonts are
embedded** and no Type3 bitmap font remains. Six underfull-box messages were
reviewed visually and do not produce a material spacing or readability defect.
The final compiler and bibliography logs are included under `validation/`.

The final metadata audit verifies one result row for every numbered statement,
all 37 bibliography entries, all 23 reading rows, and the printed statement
numbers. The independent Python and JavaScript expansions of all 44 identity
products agree exactly as data. `code/validation_output.json` records the
actual PDF size, hash, font count, page count, and zero-failure checks.

The archive includes a SHA-256 manifest for its files and is checked for ZIP
CRC integrity after creation. Temporary runtime dependencies, font caches,
private transfer helpers, and full downloaded source PDFs are excluded.
The complete mathematical deliverables, all nine mathematical check programs,
their actual outputs, and the delivery-validation programs are included.
