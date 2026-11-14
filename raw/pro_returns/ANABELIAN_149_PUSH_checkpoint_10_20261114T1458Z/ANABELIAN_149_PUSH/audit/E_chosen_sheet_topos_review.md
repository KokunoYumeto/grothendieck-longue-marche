# Independent review of E.13 chosen-sheet naturality

**Reviewer:** `/root/topos`. **Scope:** the auxiliary surface-group functor, balanced cover/filling square, and E.13.3–E.13.4. The genus-zero centre argument is being separately revised by its author and is not certified by this note.

## 1. Balanced square

The auxiliary functor into outer continuous homomorphisms of finitely generated profinite surface groups is valid. Hom_cont(P,Q) is a closed relation-defined subset of a finite power of Q. Quotient by the compact inner action is compact Hausdorff, and composition is continuous. The mapping-class action exists independently of its conjectural faithfulness. Thus E.8 extends the discrete functor.

A completed covering remains an index-d injection and a completed filling remains surjective. For vf′=fu, choosing the target conjugator gives v_*(J′)=J. Both J′ and v_*^{-1}(J) have indexd, so they are equal. This recovers the actual puncture-pullback right cover orbit. A new source cusp killed by u cannot map to an old target cusp, whose peripheral inertia survives v. The d new cusps are therefore exactly the d degree-one preimages of the new target cusp.

## 2. The cancellation step needs an explicit lemma

The equation fu=fa0u cannot simply be cancelled using only the auxiliary surface-group functor: that could hide a mapping-class congruence-kernel assumption. An actual Hurwitz forgetful argument proves the discrete chosen-sheet assertion, but the arbitrary F-image square also needs the completed categorical version.

The following restricted cancellation lemma supplies it:

> Let f:S→T be a pure finite covering and u:S_D→S fill a distinguished colour D of ordinary source punctures. Then the discrete right stabilizer of fu is the inverse image of Deck(f) under the mapping-class forgetting homomorphism. After completion its stabilizer is likewise the inverse image of the same finite deck group.

Here is why the lemma survives the full diagram relations used in E.8. Every covering/filling word has an oriented finite branched compactification. At each coloured source end, whether its final image is a retained target end or an ordinary target point, and the corresponding positive local degree, remain constant under a diagram isotopy. For coverings these are the transported local covering data. A filling moves a disjoint interior configuration and cannot move a filled point across a retained target puncture. Equal-actual-composite relations preserve those data literally. Inserting such a relation into a longer word preserves them by composition.

For fu, every end in D has an ordinary final image and local degree1; the old ends are exactly the inverse images of old target ends with the original covering indices. Thus at every stage of a relation chain starting at fu, filling D extends the compactified map uniquely to a finite étale covering S→T. This extension sends a diagram isotopy to a pure-cover isotopy, and sends equal actual composites to equal extensions. Consequently equality fu=fu a implies f=f forget(a) in the pure-cover category. The reverse implication is immediate. The discrete stabilizer is therefore exactly forget^{-1}(Deck(f)).

For completion, the source forgetting map is surjective. Right exactness of profinite completion identifies its kernel with the closure of the discrete filling stabilizer; no injection of a congruence quotient is used. Since Deck(f) is finite, the full preimage of Deck(f) is the closure of its discrete preimage: each deck element has a discrete lift, and the kernel is already that closure. E.8's stabilizer formula now gives the asserted completed equality. This is precisely the cancellation needed for an arbitrary completed image square.

## 3. Chosen-sheet subgroup and naturality

With one of the d new degree-one cusps distinguished, the cover stabilizer is trivial: a deck transformation fixing that unramified point is the identity. Hence a target mapping class has at most one lift respecting the distinguished point.

A point-pushing loop b lifts with filled marking equal to the identity exactly when its lift returns the chosen sheet. Discretely these loops form the index-d subgroup f_*pi1(S,p). The additional filling condition removes a possible deck adjustment. Forgetting the other d−1 moving points returns exactly the based lift of the loop on S.

The completed target lifting subgroup is open. By the restricted cancellation lemma, the filled source marking of a lifted point-push lies in the finite group Deck(f). Its identity condition is therefore an open kernel. Discrete point-pushing elements are dense in the relevant open subgroup; hence the kernel is the completion of the just described index-d subgroup, not a potentially larger congruence subgroup. The filling retaining only the chosen point identifies it with P_S by the full Birman sequence.

All equations and colour-forgetting maps survive F. The balanced-square calculation identifies its completed image with the correct puncture pullback. The same subgroup construction there gives (Ff)_* psi_S=psi_T f_* up to the one expected target inner automorphism. This proves naturality rather than assuming that F commutes with the auxiliary fundamental-group functor.

**Outcome:** E.13.3–E.13.4 pass with the explicit restricted cancellation lemma above incorporated. No congruence subgroup property, peripheral Magnus theorem, or unproved categorical cartesian predicate is required.

## Final updated-candidate pass

I read the revised `audit/E_Hurwitz_injectivity_candidate.tex`, including the restricted cancellation block and the revised chosen-sheet completion block. The final text uses a shorter valid proof of the discrete cancellation lemma: the ordinary pi1 functor and surjectivity of u_* show that the forgotten mapping class acts through the normalizer of the discrete covering subgroup; the corresponding deck transformation has the same outer pi1 action. The ordinary homotopy-to-isotopy theorem then identifies those two discrete mapping classes. This is used before completion, so no profinite Dehn–Nielsen–Baer theorem or congruence subgroup property enters.

The added rational graph-homology calculation correctly shows that the finite deck group survives in the completed mapping-class group. Its free action on the affine surface gives H1=Q plus r−1 copies of the regular representation, with r≥2. Thus the action is faithful and a finite integral-homology quotient detects it. Taking the finite union of lifted deck cosets and the closure of the forgetting kernel proves the exact completed stabilizer formula.

The paragraph reducing arbitrary completed markings to an actual cover/filling composite is valid: lift the source marking of the cover through the surjective completed forgetting map, then combine it with the filling's source marking. This is exactly the step needed for the arbitrary F-image square. The revised chosen-sheet proof invokes that formula directly and then takes the open identity kernel of a finite deck quotient. Consequently its density assertion and its identification with the completed index-d based covering subgroup are justified.

**Final scoped verdict:** the revised restricted cancellation and chosen-sheet naturality statements pass. The independent boundary-profile proof above is corroboration, not an additional hypothesis needed by the final argument. This note does not certify the separate arithmetic-image selection argument.


Final location update: degeneration integrated the reviewed argument as sections/E_Hurwitz_injectivity_extension.tex, Claim E.13. The earlier candidate path is historical; the review conclusions apply to the integrated argument with the discrete restricted-cancellation proof and chosen-sheet completion.
