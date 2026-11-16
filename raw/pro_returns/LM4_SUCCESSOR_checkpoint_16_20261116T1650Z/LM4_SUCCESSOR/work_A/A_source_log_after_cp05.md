# Supplementary primary-source log after checkpoint05

Earlier exact-source checks are recorded in A_references.bib and A_report.md.

## Poonen2017, added for A.54

- Author-hosted primary text: https://math.mit.edu/~poonen/papers/Qpoints.pdf . Opened directly at web reference turn502view0; exact Theorem6.7.3/Corollary6.7.4 located at turn503view0/turn503view1.
- Printed page194, PDF index207, supplies the continuous profinite Hochschild–Serre spectral sequence and inflation–restriction sequence for a closed normal subgroup. The coefficients in A54 are finite discrete continuous modules, within those hypotheses.
- Metadata: Bjorn Poonen (2017), Rational Points on Varieties, Graduate Studies in Mathematics186, American Mathematical Society, DOI10.1090/gsm/186. Verified using the author's errata/CV and AMS DOI record (search turn504search1/12/14).
- Application: normal pro-p′ averaging yields all-degree vanishing on the initial base; the five-term sequence computes new-base H1 exactly. No converse or extension theorem beyond the displayed sequence is attributed to this source.
- No supplied-background PDF was copied into the deliverable.

## A.55–A.57 and recovery

These statements add no external recognition theorem. Their continuous cohomology uses the already checked Poonen source, and their free-product cohomology uses the already registered profinite Bass--Serre inputs. The central extension, coefficient ring, exact source relations, and finite witnesses are proved or computed in the component itself. After environment replacement, the complete reviewed source was reconstructed and every cited seventh-hour stdout regenerated; see `RECOVERY_A_20261116.md`. The post-checkpoint exact-center and integral-norm proposals remain separate until formal integration is authorized.

## 2026-11-16, after checkpoint09: local cubic group identification

Opened and read the primary full PDF Eaton (2024), *Blocks whose defect groups are Suzuki 2-groups*, arXiv:2401.04028v2, https://arxiv.org/pdf/2401.04028 (web reference turn631view0). Section2 on printedpage3 defines A(m,theta) by (alpha,beta)(gamma,delta)=(alpha+gamma,beta+delta+alpha theta(gamma)). With theta(t)=t^4 and (alpha,beta)=(a^2,z), this is exactly our64-element law (a,z)(b,w)=(a+b,z+w+a^2b). Only this definition and elementary coordinate comparison are used. No block-classification or broad automorphism claim is imported. The scalar cocycles, stem256group, and actual source-attainment proof are checked directly in this project. Bibliography key AEaton2024.


## A.80, after checkpoint13: general-field semisimplicity

Milne, J. S. (2025), Group Theory, version4.01, primary author PDF https://www.jmilne.org/math/CourseNotes/GT.pdf, was opened directly. Theorem7.4 and Proposition7.9 on printed103--106 were read, including the general-field averaging proof. Only Maschke and semisimplicity are cited. The finite-field induction adjunction and index-two restriction positivity are proved directly in A80. Full retrieval and scope notes are A80_source_notes.md; bibliography key AMilne2025.


## A.81, checkpoint14: verified prime factorization and actual source algebra

Milne, J. S. (2020), Algebraic Number Theory, version3.08, primary author PDF https://www.jmilne.org/math/CourseNotes/ANT.pdf, was opened directly. Theorem3.34 and its Galois transitivity proof, Theorem3.41 and its proof, and Remark3.43 verify the root-mod-p to unramified degree-one prime step. The finite Galois extension then has all residue degrees one. Theorem8.31 and Corollary8.32 were independently opened as a stronger comparison, but A81 supplies its own elementary polynomial proof of infinitely many split primes outside any finite set. No density or Chebotarev dependency is used. Source references include turn740view0, turn741view0/1 and the independent root reading turn746view0/1. Bibliography key AMilneANT2020 has an explicit verified note. AMilne2025 likewise now has the literal verified marker.

The representation case analysis, actual exterior-square central kernel, source r-correction, compact-surface central cusp scalar, and boundary averaging correction are proved directly in A81. They do not appeal to a general order-preserving lifting theorem. Parent and CE formal-source reviews pass. The standalone component is five pages with no errors, overflows, or undefined citations, as recorded in A81_component_build.out and A81_component_QA.txt.


## A82–A83, checkpoint15: verified prescribed involution classes and exact module scope

Haran, D. (1990), Closed subgroups of G(Q) with involutions, Journal of Algebra129(2),393–411, DOI10.1016/0021-8693(90)90227-F, was opened directly at the primary author PDF https://www.tau.ac.il/~haran/Papers/closed_subgp_invs.pdf. Definition1.1(4), Remark1.2(b), Proposition2.3 and its complete proof on printed394–398 were read. The conjugacy-closed allowed involution set is part of the exact embedding-problem statement. Own retrieval references: turn755view0, turn756view0/1; independent parent turn757view0; independent CE turn762view0. Bibliography key AHaran1990 has a literal verified note. Proposition1.4 only embeds the group in a free product and is not used to infer a decomposition.

The parent also opened Haran–Jarden(1985), Annali della Scuola Normale Superiore di Pisa12,449–489, Corollary6.2 and its proof on466–467, primary Numdam ASNSP_1985_4_12_3_449_0.pdf (turn760view1). Its finite auxiliary cover has a self-contained derivation in A82 from the already checked full-profinite free-product torsion theorem: the compact set of squares over forbidden classes avoids1 and can be excluded by a finite normal quotient. No unproved category change or proper-solution assertion is imported.

A82's compact-module and inverse-limit basis arguments and A83's actual surface-pair/polygon calculations are proved in full. Only general-field semisimplicity uses the already verified AMilne2025. The regular case explicitly retains the complete C43 free-index-two, cusp-action, one-section and self-centralizer hypotheses. The exact incidence cokernels are stated separately from target freeness. Formal-source parent and CE reviews: PASS. Standalone QA: A82_A83_component_build.out and A82_A83_component_QA.txt, six pages clean.


## A84, checkpoint15: verified Cartan injectivity and symmetric finite group algebra

Webb, P. (2016), A Course in Finite Group Representation Theory, Cambridge University Press, primary author prepublication https://www-users.cse.umn.edu/~webb/RepBook/RepBookLatex.pdf, was independently opened. Proposition10.2.1 and its complete character-pairing proof, Theorem10.2.2 and proof, and Corollary10.2.4 and proof on printed174–178 give the required independence and injectivity of the finite group-algebra Cartan map. The surrounding text uses invertibility over Q; A84 uses only injectivity, not an integral surjectivity assertion. Proposition8.5.2 and Corollary8.5.6/proof verify dual projectivity and projective-cover duality; A84 also gives the finite primitive-idempotent argument. Own independent source references: turn779view0/1/2/3, turn780view0/1/2/3 and turn782view0/1/2; parent references turn772view0/1/2 and turn774view0/1.

A84's finite-field descent, exact base change of the continuous projective Hom dual, lift through p-power coefficients, and compact compatible-isomorphism construction are supplied directly. It does not use inverse-limit duality of underlying compact vector spaces. The original scoped A83 proof is retained with a forward pointer. Component source and standalone QA pass: A84_component_build.out and A84_component_QA.txt. Bibliography key AWebb2016 carries the explicit verified note.


## B85, checkpoint16: verified relative tangential specialization

Deligne, P. (1989), Le groupe fondamental de la droite projective moins trois
points, in Galois Groups over Q, MSRI Publications16, pp79--297, Springer.
Verified primary author PDF:
https://publications.ias.edu/sites/default/files/61_LeGroupeFondamentalDroite.pdf.
Sections15.17--15.19 and15.22--15.26 were opened and read directly, with
independent root and CE readings. Own retrievals include turn806view1,
turn807view0, and turn809view0/1/2; CE separately opened turn810view0,
turn811view0/1, and turn812view0. Section15.19 requires a smooth relative
curve over a normal base and an etale boundary section. B85 supplies exactly
that explicit rational U/B,S model, with F(0,q)=250. Sections15.17--15.18
verify classical compatibility and descent;15.22--15.26 supply the formal
interpretation. No unproved higher-dimensional variant is used.

The same actual source path transports the entire diagram. It need not be
Galois invariant, and no equality with the arithmetic section of the old
rational base point is claimed. The exact local braid fixes the b^{-1}
orientation. The new six-character scope is calculated over Q(zeta5)[w],
not by sampled numerical roots. Bibliography key BDeligne1989 has a literal
verified status note. Accepted proof: B85_tangential_Galois.tex; primary
review: work_CE/review_tangential_product_one_Galois_15h.txt. Parent and CE
full formal-source reviews, including B85.6, PASS.


## B87, checkpoint16: full profinite centralizers and actual completion

The already verified primary Herfort--Ribes(1985) text, Theorem B' and its
proof with Lemma3, printed159--160, was reopened directly at the
bibliography's author-associated URL. Own retrieval turn815view0; root
independent retrievals turn817view0/1; CE independently reopened the same
primary text. The theorem identifies the centralizer of a nonidentity
finite-factor element in a full free profinite product with its centralizer
inside that factor. It applies exactly to C2 coproduct C2 coproduct Fhat2.
The proof uses no arbitrary closed-subgroup Kurosh statement and no pro-p
recognition inference. Existing verified key A_HR1985 is retained unchanged.

The actual product bundle, two-cone orbifold marking, characteristic finite
quotient construction, and finite mod-two cone-permutation detector are
proved explicitly in B87. Thus full completion exactness and actual source
topology are established in this case instead of assumed from a general
free-by-free slogan. The primary theorem is the only non-elementary
centralizer input. Root and CE full-source review PASS; genuine rational
identity certificate and clean four-page component QA retained.


### Checkpoint16: B89 actual symmetric intersection and completion

Verified primary author PDFs:
- Brown and Loday (1987), *Van Kampen theorems for diagrams of spaces*,
  Topology26(3),311--335, DOI10.1016/0040-9383(87)90004-8,
  https://groupoids.org.uk/pdffiles/RB-Loday1.pdf . Opened and read Lemma4.1
  and its proof on printed320, including its weaker homotopy-fiber
  surjectivity condition. Theorem3.1 and Cor3.4 checked for context.
  Own retrievals turn826view0/turn827view0; root and CE independently reopened.
- Brown (1984), *Coproducts of crossed P-modules: Applications to second
  homotopy groups and to the homology of groups*, Topology23(3),337--345,
  DOI10.1016/0040-9383(84)90016-8,
  https://www.groupoids.org.uk/pdffiles/coproducts-Topology.pdf . Opened and
  read Props2.5/2.8 and Theorem3.1/Cor3.2 with proofs, establishing the
  ordinary mutual-commutator identification for normal-subgroup inclusions.
  Own retrievals turn828view0/turn829view0; root independently opened full text.

Both accepted bibliography notes carry explicit verified labels. No
profinite-excision result is attributed to these discrete sources. The
actual compact proof is self-contained via finite-kernel virtual splitting
and the full induced topology of the actual fiber product. Root's Porter
and Korkes--Porter leads were not needed and are not theorem dependencies.

Research/formal proof: symmetric_intersection_commutator_16h.md and
B89_symmetric_intersection.tex. Independent CE review:
work_CE/review_B89_intersection_completion_16h.txt. DE full-source PASS also
received. Exact mixed geometry uses DE's genuine Q(zeta5) certificate; no
new finite-group census is asserted.
