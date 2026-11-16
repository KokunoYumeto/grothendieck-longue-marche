# Part A working outcome table

| Prompt item | Paper statements | State |
|---|---|---|
| A.1 literature | A.1 | Sources opened and relevant theorem scopes checked; no exhaustive claim that R1 lacks a later antecedent. |
| A.2 / Lead 1 | A.2 | Proved from R2, with compactness and descent maps supplied. |
| A.2 / Lead 2 | A.3 | Proved from the finite central-refinement theorem in the refereed proof of LM7_PUSH D.50. |
| A.3 specified conjugator | A.4–A.6, A.15 | False, including for an actual Galois-conjugate of c; certificate in a group of order 16807. H1(C2,N) has exactly continuum cardinality. A.15 identifies its entire standard fibre by the quotient centralizer; exhaustion remains open. |
| A.4 levels | A.9–A.10, A.12, A.17 | Odd-prime conjugacy proved. A parity-one anti-invariant frame is now constructed at the relative dyadic level. Full dyadic classification and the two mixed-prime level classifications remain undetermined. |
| A.5 / Lead 3 | A.7–A.8, A.12, A.15–A.17 | Both named H1 sets have exactly continuum cardinality. Local c-equivariance of parity-one framed data is proved, using a compatible S3 lift through a pro-2 kernel. A full parity-one involution still requires a norm equation in the smaller specified framed kernel L. |
| A.6 parity | A.13 | Delta is zero on the entire standard family; no proof of universal vanishing or counterexample. |
| A.7 generation | A.11 | Reflection-triangle equivalence and detection on all relative levels proved. Ordinary pro-p tests are insufficient; the exact full third-cusp alignment remains necessary. |
| A.8 decision | A.14 | All three full conjugacy questions remain undecided. Abstract finite subgroup types are exactly 1 and C2 by R1, but this is not conjugacy classification. |

A.18 also refutes a blanket order-preserving version of R2 inside the actual peripheral groups: the pronilpotent automorphism that is c only at p=3 is an involution, but every full lift has mixed multiplier signs and therefore cannot have finite order by R1. This obstruction does not apply to A.17, whose multiplier is globally negative. A.19 gives the exact abelian refinement obstruction in H2(C2,M) and the conditional Z/4-character test for Delta.

## Main concrete correction

Task A.3 is false as written. Choose a Galois element theta=(mu,g) whose multiplier is 2 modulo 7 and set alpha=theta*c*theta^-1. The unique coboundary is h=g^-1. On the free class-three exponent-seven quotient the coefficient of log(g) on [X,Y] equals (mu^2-1)/24=1. A multiplier-one pure peripheral automorphism must have coefficient zero. Thus the exact psi proposed in the prompt fails at the third cusp already in a finite pro-7 quotient. It is not an exotic involution: alpha was deliberately taken from the standard conjugacy orbit. This isolates the error in the proposed normalization, rather than disguising it as a solution of the main question.

The certificate enumerates all 16807 elements of the group, checks exponent seven, computes the complete conjugacy orbit of xy (49 elements), excludes x*g^-1*y*g and includes x^2*g^-1*y^2*g in the orbit of (xy)^2. Code and stdout are retained.

## Correct cohomological distinction

The multiplier-one H1(C2,H) is not the set of full conjugacy classes. It already contains a closed copy of Zhat-units/{1,-1} from Galois conjugates, with Delta zero throughout. Its cardinality is continuum, even if the main full conjugacy question eventually has an affirmative answer. The full classes require quotienting this H1 by the multiplier-unit action, which need not fix its distinguished point. The same issue occurs for the fibre over c in the pronilpotent quotient: full conjugacy divides by the quotient centralizer acting by lifted conjugation. A.15 strengthens this: H1(C2,N) itself has exactly continuum cardinality, with the quotient centralizer modulo {1,c} giving exactly its entire full-standard fibre.

The proof also rechecks LM4 D.49 rather than taking it on authority: C_P(c)={1,c}. It uses LS1997 Prop4(i), the normalized homomorphic section in R1, the Harbater–Schneps S3-centralizer characterization, a finite Heisenberg calculation of the hexagon with f=1, and R1's global sign conclusion.

## Approaches tried and exact obstructions

1. Relative pronilpotent inverse limit: proved detection and surjective transition maps. Detection of already-existing full involutions does not construct compatible involution lifts.
2. Central obstruction lifting: proved Lead 2. The proof gives automorphisms and literal boundary conjugators but imposes no square-one equation.
3. R1 normalized h / third cusp: refuted by A.5. A conjugator can require a multiplier different from 1; for the constructed alpha the only full peripheral conjugator multipliers are ±mu by A.6.
4. Odd-prime local conjugacy: proved using the pro-p principal congruence kernel and Schur–Zassenhaus. This also proves the existence of some local multiplier-one peripheral conjugator for every odd p, despite failure of the particular globally fixed h.
5. Nonabelian H1: its size and the standard closed family are determined, but no invariant presently separates an additional full conjugacy orbit.
6. Gluing the two frames / Lead 3: a new compatible-complement lemma proves that the local parity-one r-frame can be made anti-invariant. An extension of S3 by a pro-2 group splits compatibly with a prescribed reflection because restriction H^n(S3,M)→H^n(C2,M) is an isomorphism for n≥1 and every finite F2[S3]-module. The exact word h=[x,y]x[x,y]x^-1 gives a reflection lift in the relative joint quotient: q(h)=(9,4;8,9) and q(h*d(h)^-1)=5I, where d=Ad(s)c. This produces an actual local b with b*r=r*b, q(b)=5I and d(b)=b^-1. R2 then lifts the framed data to sigma of Delta=1. Its product a=sigma*c satisfies a^2∈L, where L is the kernel retaining the identity relative action and both frames equal to one. The remaining equation is v*(a v a^-1)=a^-2 for v∈L. No global equivariant section or solution is proved. The finite map C4→C2 remains only a logical control showing that surjectivity alone cannot solve it.
7. Virtually free structure route: opened Herfort–Zalesskii2008 Theorem1.1 and §5 Lemma5.1. Their decomposition theorem is pro-p; the paper explicitly gives a full-profinite counterexample S3 amalg_C2 S3. That example has odd torsion and does not refute the more specific all-finite-subgroups-C2/rank-two-free-kernel statement needed here. Opened Pál–Quick Quasi-Boolean groups Theorems1.7/1.9/6.8: pro-2 real projectivity implies pro-2 free-product decomposition; full real projectivity only gives an embedding in a real free profinite group. Turning such an embedding into the marked full reflection triangle remains unresolved.
8. Latest literature: opened the 2026 Lochak–Nakamura–Schneps manuscript on the GT action in genus g with 0 or1 marked points. Its Theorem1.1 is an action theorem, not involution conjugacy. It does not supply the missing order-preserving lifts.
9. Equivariant count: the unrestricted formulation is false by the actual mixed-sign example A.18. In the globally negative A.17 fibre, the square obstruction at any finite abelian refinement is [a^2] in M^a/(1+a)M. It vanishes for odd-order M; dyadic terms remain. R2's boundary-class epimorphism count does not calculate this square class. The count cannot simply be reused with the additional order-two assertion.
10. Character refinement: a continuous Z/4 lift of Delta would force Delta to vanish on all involutions. A c-invariant Z/4 lift of delta on the multiplier-one subgroup would suffice as well. Local parity-one framed involutions rule out such a lift on the local framed target. A hypothetical global lift must instead detect a^2 inside L, with value two. Neither its existence nor its impossibility has been proved.
11. A.20 gives a second intrinsic failure of a proposed lift: the S3 subgroup generated by r and the locally glued reflection exists in the standard relative extension, but has no finite-subgroup lift in the standard full extension. All full S3 subgroups normalize a conjugate of the C3 factor, so are conjugate to the standard S3. In the finite quotient Q semidirect d, the new subgroup is not conjugate to that standard one. The exhaustive 576-element certificate finds a normalizer of order18 and nine d-norm values, disjoint from the three-element coset [5I]<r>. The short proof is the opposite-sign obstruction modulo four and three. This obstruction applies to the standard extension only; it does not exclude a new twisted extension attached to an exotic involution.

## Important typing of the new local result

A.17 constructs a framed cocycle. Its underlying automorphism before multiplying c is identity on B/R_nil(H0); after multiplying c it is literally c on that quotient. It does not exhibit a nonstandard involution in Out-sharp of any actual relative quotient. Delta does not descend to that unframed level: E58 itself has identity action there and Delta one. The two accessory frames at this quotient are nonunique, which is precisely why they must be retained as separate data.

## Sources opened

- LS1997: https://webusers.imj-prg.fr/~pierre.lochak/textes/inventiones.pdf — Prop4(i)(ii), proof and normalized definitions.
- Schneps1997: https://webusers.imj-prg.fr/~leila.schneps/SchnepsGT.pdf — §1.4(4).
- LS2006: https://webusers.imj-prg.fr/~leila.schneps/farb.pdf — Question1.4 including its follow-up finite-order question.
- HS2000: https://webusers.imj-prg.fr/~leila.schneps/HS.pdf — MainTheorem(a), Props3–4, Theorem2, normalized section.
- Collas2012 genus0: https://collas.perso.math.cnrs.fr/documents/Collas-Genus0_gt-action.pdf — Theorems3.3/3.10.
- Collas2012 genus1: https://collas.perso.math.cnrs.fr/documents/Collas-Genus1_gt_action.pdf — Theorems6.3/6.5; acting group GR retained.
- HZ2008: https://arxiv.org/pdf/0712.4244 and https://mat.unb.br/pz/arquivos/vfreepaper3.pdf — pro-p theorem and full-profinite counterexample.
- Pál–Quick: https://gereonq.folk.ntnu.no/boolean-group.pdf — Theorems1.7/1.9/6.8.
- LNS2026: https://webusers.imj-prg.fr/~leila.schneps/GTgenusg.pdf — Theorem1.1 and stated scope.
- Wykowski2026: https://ems.press/content/serial-article-files/53276 — introduction and Section2.1, especially Theorem2.4 and the distinction between abstract virtual freeness and a profinite tree action; DOI10.4171/GGD/851. No full-profinite realization theorem used.
- Herfort–Ribes1985: https://www.academia.edu/104225124/Torsion_elements_and_centralizers_in_free_products_of_profinite_groups — full paper text, Theorems A-prime, B-prime, and1 on printed157–160. DOI10.1515/crll.1985.358.155. The attempted EuDML and DigiZeitschriften URLs failed; the text actually read is the author-associated copy.

## Supplied records read

The two LM4 D.32/D.34 referee reports; LM7_PUSH D.50 source and its referee report; LM4 D.35, D.49, D.74, and D.77; source bibliographies. Refereed R1–R3 were used as authorized. No new claim of priority is made.

## Files

The growing paper source is A_involutions.tex. A_references.bib records verification status. A_results.csv is the statement register (25 rows, including the three requested editorial corrections E.50-E.52). check_A3_class3.py and check_A3_class3.out are the independently executed finite third-cusp certificate. check_A17_frame.py and check_A17_frame.out retain the independently executed relative-frame matrix certificate. check_A20_standard_extension.py and check_A20_standard_extension.out retain the full finite normalizer/norm enumeration. This report is a working record; the root paper must remain marked INCOMPLETE while A.12–A.14 remain open.

## Further recognition and editorial work

A.21 gives an explicit counterexample to full real-projective finite-graph recognition even when the open free subgroup has rank two and index two and every involution is self-centralizing. Put Gamma*=(product over odd p of Zp) semidirect Z2, with parity inversion, and E*=C2 coproduct Gamma*. Open Kurosh gives a rank-two free parity kernel. Its abelianization is C2 times Z2, excluding the only possible finite-graph candidate C2 coproduct Zhat. This example has only one involution class and does not meet R1's three-section hypothesis. A.22 adds the exact constraint on the latter case: the three distinguished reflections normally generate; if they fail to generate, their closed generated subgroup has infinite index. The required marked full generation is still open.

At the parent's request, sections/editorial.tex now contains E.50-E.52. E.50 proves the full-P form of LM4 D.28 independently of R1's final conclusion; E.51 proves the normalized homomorphic section and the integral Magnus torsion lemma directly, removing the D.25-D.32 citation cycle; E.52 supplies precisely Herfort-Ribes Theorem B-prime, with the primitive-boundary limitation retained. Their register rows are in A_results.csv for parent assembly.

Additional primary sources opened: Haran1985 complete three-page PDF https://www.tau.ac.il/~haran/Papers/non-free.pdf; Pal-Quick2025 publisher full text https://link.springer.com/article/10.1007/s00208-025-03145-2, especially Theorem2.1; Kochloukova-Zalesskii2007 complete author manuscript https://mat.unb.br/~pz/arquivos/Claus3.pdf, Theorem2 and Section1.1; Zalesskii2004 https://mat.unb.br/pz/arquivos/virproj.pdf, introduction and main theorem that quotient by the normal closure of torsion of a virtually projective profinite group is projective. The latter theorem does not supply a free-product decomposition and is not used as one. The KZ DOI redirect failed; no claim of reading that publisher page is made.
