# Cycle 31: root primary readings and the direct compact-stabilizer argument

This record concerns research after the immutable thirtieth capture. Earlier archives and all frozen thirtieth-cycle proofs are unchanged. Both main questions remain Open.

## Actual readings and their limits

We read Boggi's original arXiv:0910.4305v5, Proposition 3.4, the complete printed proof of Theorem 4.2 (retrieval lines 573–922), and the explicit stabilizer-closure deduction at lines 965–970. The theorem includes the separating four-punctured-sphere case; the printed detailed argument is nonseparating and states that the separating case is analogous. We checked the actual separating marking separately. DE read the characteristic-cover and homology-graph dependencies in arXiv:1111.2372 and recorded their exact scope. We do not claim to have reread every background result on moduli stacks. Root retrievals include `turn1101view0` and `turn1102view0`.

We also read the entire §2.2.5 of Farb and Margalit, Version 5.0, printed pp. 57–60, including both proofs of Propositions 2.6 and 2.7. The text gives the branched-torus curve correspondence and the mapping-class map to PSL(2,Z) with Klein-four kernel. The successful institutional primary copy is https://pagine.dm.unipi.it/~a019210/Farb%20Magalit_Primer%20on%20Teichmuller%20theory.pdf (`turn1116view0`, `turn1122view0`). The author's book list identifies the published book as Princeton University Press, 2012. We retain the version-specific page locator instead of silently identifying draft and published pagination.

Before the thirtieth capture, we had read Boggi and Funar's arXiv:2004.04135v4, printed pp. 17–20, including Theorem 4.5, Lemma 4.8, Corollary 4.9 and the stabilizer discussion. That is corroborating exposition, not a replacement for the original proof. The original theorem is not a statement about arbitrary finite-subgroup centralizers. No completion/intersection exchange for two arbitrary closed subgroups is imported.

We now read the complete §5 of McReynolds's arXiv:0901.4663v2 (11 March 2010), including the printed proofs of Lemmas 5.1–5.3 and Proposition 3.1, together with the explicit n=4 deduction and the marked Birman identity stated as Lemma 2.2. Root retrievals are `turn1124view0`, `turn1125view0` and `turn1128view0`. The publisher metadata was independently opened: https://nyjm.albany.edu/j/2012/18-47.html (`turn1129view0`), New York Journal of Mathematics 18 (2012), 925–942. At the time of this record the observations below are about the inspected arXiv version; DE is separately comparing the final published passages.

## Auxiliary proof precautions and a direct comparison

The arXiv Lemma 5.3 construction must not be read as valid for an arbitrary fixed prime. If its finite noncyclic head is a p-group and the chosen coefficient prime is p, all successive constructed groups and their quotients remain finite p-groups. A nontrivial quotient still surjecting onto that head therefore cannot be centerless. Nor is passing from an arbitrary group to its quotient by its center, without further argument, a general centerless construction. We retain the printed attempt and qualify the earlier proof audit. This observation is not a refutation of genus-zero CSP.

A complete independent repair of the centerless-refinement input is available. For an epimorphism F_r→Q, r≥2, choose a prime ell not dividing |Q| and let N be its kernel. The finite quotient E=F_r/(N^ell[N,N]) has elementary abelian kernel V. The finite Cayley-cover chain sequence and Maschke splitting give V≅F_ell⊕F_ell[Q]^(r−1). Averaging splits the extension E over Q. Quotienting E by V^Q therefore gives I_Q^(r−1)⋊Q, where I_Q is the augmentation ideal. This module has no Q-invariants and is faithful: a group element acting trivially on I_Q also acts trivially on the complementary norm line, hence on the faithful regular module. The resulting quotient is centerless and still maps onto Q. This is an explicit replacement proof, not an assertion that the printed construction has been verified as written. DE records the full chain-sequence and finite-detector details.

For the four-punctured-sphere comparison itself an even shorter argument suffices. Write Π=F_3 with a peripheral free generator λ and Π_0=Π/<<λ>>=F_2. An outer continuous automorphism preserving the peripheral conjugacy classes has a representative fixing λ. Two such representatives differ by conjugation by an element of C_hatΠ(λ)=closure<λ>; this disappears in hatΠ_0. The induced map to Aut(hatΠ_0) is consequently well-defined and multiplicative. It is continuous by descent from the compact closed subgroup of representatives fixing λ, so no continuous selection of conjugators is assumed. For the actual Birman point-push map Π_0=PMod(S_0,4), the induced automorphism is the inner automorphism of the pushed loop. Density extends this identity to full completions. Since hatF_2 has trivial center, the completed point-push map is injective. Thus the exact required full/procongruence comparison has an independent proof. The original full Asada proof was not newly retrieved in this cycle.

## The stronger direct proof in the actual one-family group

The final local result can avoid that mapping-class comparison altogether. We use only the actual coarse group E_0=T_0⋊S, T_0=F(r,b,w), S=F(m,u), the actual involution δ(r)=b, δ(w)=w^−1, and the ordered cocycle h_st=α_s(h_t)h_s. Characteristic finite-index fiber refinements give the full fiber topology; the two genuine sections S and H have full topology by projection. Thus h extends continuously to hatS. The already checked identities are α_s(r)=h_s r h_s^−1 and χ_x(h_s)=0, with χ_x(r)=1.

Set q_s=δ(h_s). Because α_s commutes with δ, q_st=α_s(q_t)q_s. Consequently

    βtilde_s=Inn(q_s^−1) α_s

is an actual continuous homomorphism of the completed source into Aut(hatT_0), and it fixes b exactly. Descending through the closed normal closure of b defines β on hatF(r,w). There is no arbitrary conjugator choice. The literal generator values are

    β_m(r)=r,  β_m(w)=r w^−1,
    β_u=Inn(w^−2).

For the second formula h_u=w^−1r and q_u=w b, so the omitted b factor disappears only after taking the stated quotient. This correction is essential.

The ordinary index-two subgroup S_p=ker(exp_m mod2) has free basis m²,u,mum^−1. Its three inner heads under β are

    r,  w^−2,  w r^−1 w r^−1.

They are a free basis of the index-two subgroup H_0=ker(exp_w mod2) of F(r,w). Explicitly, with the standard Schreier basis x=r,t=w²,z=w r w^−1, put y=t^−1 and c=z^−1 t x^−1. The inverse change is t=y^−1 and z=(cxy)^−1. These mutually inverse free-basis changes prove the assertion without a word census or an unproved finite-index claim. Therefore hatS_p identifies under β with Inn(hatH_0); the full topology of H_0 follows from its actual finite index in F(r,w), and the inner map is injective because hatF(r,w) has trivial center.

Inside hatE_0 define L_c=hatH∩hatS. Its elements have h_s=q_s=1, hence β_s is the descended actual α_s and fixes r. If s has even parity, its inner head belongs to C_hatF(r,w)(r)=closure<r>. The free-basis identification sends m² to r, so s belongs to closure<m²>. For odd parity, multiply by m^−1 and apply the even case. Conversely every profinite power of m belongs to both actual section closures. Thus L_c=closure<m>, with every completion and embedding specified. The earlier cocycle/character calculation also identifies L_c with the exact-r stabilizer; it uses C_hatT_0(r)=closure<r> and χ_x(r)=1, not an arbitrary subgroup-intersection theorem.

Root checked the literal generator actions, cocycle order, free-basis inverse and both parity steps. A and DE independently checked the same argument. CE is saving the complete final source and formal B153. The geometric branch and its corrected primary audits remain preserved as independent research records; the direct local proof does not depend on them.

## Consequence and remaining gate

We read the entire finite-permutation topology proof in `work_CE/one_family_fixed_source_full_topology31.txt`. For any finite target of J_a, compact separation of hatH from the relevant closed subset of hatS gives the necessary intersection refinement. The induced finite set Dbar×_(Sbar)A supports an Hbar-centralized permutation extending the marked source generator. Evaluation is used only on the J_a-stable identity fiber. This proves full induced topology of J_a in the actual one-family ambient group. The existing ordinary marked section therefore extends to the completed fixed projection. The net argument proves closure(I_src)=closure(H_src)∩closure(K_rem), with no assumption about the abstract completion of the infinite-rank kernel.

These are local one-neck conclusions. The remaining local equality is (closure K_rem)^δ=closure I_src. It is not proved by the stabilizer or topology arguments. Transfer to the other necks and the original B75 icosahedral finite-neighborhood criterion also remain open.

## Retrieval failures retained

The following attempted locations did not supply a readable source: the Funar author PDFs `https://www-fourier.univ-grenoble-alpes.fr/~funar/bf_final.pdf` and `https://www-fourier.ujf-grenoble.fr/~funar/congruencev1.pdf` timed out; the author's Utah Primer page returned 403; `https://math.uchicago.edu/~margalit/mcg/mcgv50.pdf` returned 403; and the indexed NMU mirror `https://euclid.nmu.edu/~joshthom/Teaching/MA589/farbmarg.pdf` returned 404. Successful arXiv or institutional retrievals are identified above. No reading or verification is attributed to the failed fetches.

## References

Boggi, M. (2014). On the procongruence completion of the Teichmüller modular group. *Transactions of the American Mathematical Society, 366*(10), 5185–5221. https://doi.org/10.1090/S0002-9947-2014-05971-0

Boggi, M., & Funar, L. (2023). Automorphisms of procongruence curve and pants complexes. *Journal of Topology, 16*(3), 936–989. https://doi.org/10.1112/topo.12306

Farb, B., & Margalit, D. (2012). *A primer on mapping class groups*. Princeton University Press. The freshly inspected text is the authors' Version 5.0, with January 2011 preface; its §2.2.5 pagination is stated above.

McReynolds, D. B. (2012). The congruence subgroup problem for pure braid groups: Thurston's proof. *New York Journal of Mathematics, 18*, 925–942. https://nyjm.albany.edu/j/2012/18-47.html
