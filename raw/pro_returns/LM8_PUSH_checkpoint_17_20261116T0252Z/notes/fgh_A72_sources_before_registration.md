# A72 source and proof ledger

Status: unregistered candidate, pending complete independent audits. Full proof is notes/fgh_A72_draft.tex. Only notes/code files have been written during the canonical checkpoint freeze.

## Exact primary inputs

- **verified:** Lehr–Matignon, Theorem6.13, published p154 in the workshop collection edited by Cornelissen–Oort. Original https://www.numdam.org/item/RSMUP_2005__113__129_0.pdf ; author version https://arxiv.org/pdf/math/0411059 , printedp21/PDF20. Freshly reopened as turn1171view0, exact theorem turn1172view0, lines740–746. A nilpotent Galois cover of a good smooth base with étale branch closure and generically tame ramification has tree-like stable reduction / potential-good Jacobian. We use only this conclusion for the actual quaternion cover at2; no marked exceptional slope theorem is inferred.
- **verified:** Saïdi, PRIMS43(2007), printedp662, records the same ramified extension. Publisher https://ems.press/journals/prims/articles/2201 ; primary PDF https://ems.press/content/serial-article-files/41001?nt=1 . Previously opened/read in A69 source audit. No new scope is added.
- **verified:** Crew, Corollary1.8, printedpp35–36, https://www.numdam.org/item/CM_1984__52_1_31_0.pdf ; and Yang, Proposition1.4, author printedp8/PDF7, https://www.kurims.kyoto-u.ac.jp/~yuyang/papersandpreprints/PSS.pdf . Yang freshly reopened as turn1171view1 and exact formula turn1172view1. These give the ramified smooth-curve Deuring–Shafarevich formula used componentwise. Yang Remark0.1.1 explicitly cautions against an unrestricted marked-fibre rank-zero conclusion; that assertion is not used.
- **verified:** Bouw–Wewers, “Group actions on curves and the lifting problem,” §2.2 classical CaseA equation(3), Exercise2.12(c), https://swc-math.github.io/aws/2012/2012BouwWewersNotesPreliminary.pdf . Freshly reopened turn1171view2/turn1172view2. The proof independently derives the different sum and additive first ramification quotient; subtraction of DS from RH forces G2=1 for ordinary curves. The resulting fourth-root obstruction is repeated explicitly.

## Internal inputs and exact scope

- A70 (fully root/DE audited notes candidate, awaiting integration) classifies actual dihedral covers of the fixed base. A44/A69 give the potential-good, special2-rank-zero property for every actual central quotient. The n2 quotient is the unramified V4 elliptic isogeny.
- A41 supplies the precise compact-type Abel-map torsion criterion, including endpoints of the rational marked path. A42 supplies the coefficient-equals-residue-prime case. A59 supplies normalizers for nilpotent closures. No pro-prime quotient is used to transfer fixedness.
- All finite definition extensions concern curves, maps, automorphisms, endomorphisms, subgroups and marks. Geometric basepoint paths are used only up to inner conjugacy; no false finite-field definition assertion is made for arbitrary paths.

## New deductions proved directly

1. Every actual generating pair of Q4n has commutator r^(2 odd). Thus the actual inertia is the normal subgroup I=<r²>, with four cusps and genus2n−1. The same elementary group calculation proves I=Phi(G).
2. The central quotient is an actual dihedral cover, and the anti-Prym has dimensionn. The actual deck action r^n=−1 gives a unital Q(zeta2n) action; its local2-adic field has degreen. This controls the actual special étale2-divisible Tate space, not merely Hodge characters.
3. Under the ordinary alternative, exchanged positive-genus components are impossible. Components with trivial involution are retained in the old factor. Exact smooth-curve DS/RH shows every positive anti-component is ordinary with genus-zero involution quotient.
4. Every nontrivial subgroup of Q4n contains the unique involution. Hence a positive anti-component stabilizer acts faithfully. A larger-than-C2 stabilizer has a fourth root of the hyperelliptic involution, excluded on an ordinary curve. Its orbit then has2n positive-genus components, exceeding total anti-dimensionn.
5. The actual quotient C/I is an elliptic V4 isogeny; its kernel is E'[2]. The actual C→C/I map is totally ramified degree n above each kernel point, so actual functions with divisor2(Qi−Qj) pull back to2n(Pi−Pj).
6. Every proper intermediate has at least two cusps by the Frattini property. Actual norm maps preserve good-rank-zero Jacobians and push principal cusp divisors with geometric point coefficient one, giving the exact A41/A42 hypotheses.

## Executed support

notes/fgh_A72_certificate.py checks the exact group law, relations, unique involution, all commutator formulas, generating-pair criteria, subgroup classification, Frattini intersection, cusp counts, intermediate genera, cyclotomic degrees, orbit contradiction and DS/RH equality for eight levels n2 through256. Small levels independently enumerate all subgroups and test generation by every ordered pair. The proof, rather than the finite range, establishes all n. The certificate status and hashes are recorded separately after execution.
