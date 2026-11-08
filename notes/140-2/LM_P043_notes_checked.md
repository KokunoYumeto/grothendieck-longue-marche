# LM_P043 (scans 421–430): research notes, checked against the corrected text

Each first-pass note (numbered as in `LM_P043_notes.md`, section 5) is kept, corrected or dropped, with the reason. Notes added in this pass are labelled "second pass (own)". Source: Grothendieck, *La Longue Marche à travers la théorie de Galois* (1981), Montpellier cote 140-2, scans 421–430.

## First-pass notes

1. **Scan 421: question. Keep.** "L'unicité est-elle de ttes façons claire ?" asks whether the partial splitting over Γ′ extends uniquely to Γ. The corrected text puts the splitting over *the* subgroup Γ′ ("du sous-groupe Γ′"), not over subgroups in general.

2. **Scan 421: conjecture. Keep, with the doubt removed.** "je présume qu'on doit avoir L^{Γ′}=1" is now a secure reading. The condition is said to generalise condition ③ of an earlier page.

3. **Scan 421: unproved claim. Keep, corrected.** The kernel is L = Ker((N_a)_{I′} → N_a), and the extension of Γ is pulled back from the extension (N_a)_{I′} of N_{a′} by L along Γ → N_{a′}. The first pass had N_0, N_{0′}. Identity (31), Norm_𝓔(Γ′) ∩ L = L^{Γ′}, is called "évident". The claim that L^{Γ′}=1 gives uniqueness (Γ̃ = Norm_𝓔(Γ′)), and that existence means Norm_𝓔(Γ′) → Γ is onto, is stated without proof.

4. **Scan 421: own idea (first pass). Correct.** The worry about continuity of an inverse does not arise in the profinite setting of these pages. A continuous bijective homomorphism between compact Hausdorff groups is a homeomorphism, so "épi (donc iso…)" holds once the map is continuous. The remaining point is the injectivity, which comes from L^{Γ′}=1 via (31).

5. **Scans 421–422: proposed investigation. Correct.** The text reads "dans certains contextes (au moins celui des actions arithmétiquement fidèles, i.e. Γ → 𝚪_a injectif — qui correspond normalement au cas de courbes alg. définies sur des ext. algébriques de ℚ)". The first pass had "(on visera alors des …", "arithmétiques" and "Π_a". So the arithmetically faithful case is the minimal context in which "admissible" is to be made precise. Returning to curves and finite coverings, which also gives a way to vary g, remains a plan.

6. **Scan 422: expectation. Correct.** He wants to take up "le formalisme précédent" (not "le problème") under another, perhaps more general, aspect. It is expected to apply also to *discrete* groups with loops (the formalism of the U!). Keep the separation of the discrete and profinite cases.

7. **Scan 423: unpursued implication. Keep.** Strict transitivity is demanded: a covariant functor from the category of cofinite parts U (with inclusions) to groupoids, over the evident functor on objects. Strictness versus coherence up to isomorphism is not discussed here.

8. **Scan 423: unpursued implication. Keep, wording corrected.** The local maps Π_{D_i^*} → Π_{U_I} are to be compatible with the "morphismes de transition" Π_{U_I} → Π_{U_J} (I ⊃ J). For fixed I they make Π_{U_I} a groupoid with loops through Π_{D_I^*} = ∐_{i∈I} Π_{D_i^*} → Π_{U_I}.

9. **Scan 423, margin: own idea (first pass). Correct.** The margin is now mostly read. If 𝒳 is finite and I = 𝒳, Π_∅ is not to be the empty groupoid but a groupoid "qui s'envoie dans les précédents…". Strict transitivity cannot then be required, and "il faudra(it) peut-être … hyp. anabéliennes sur Π_{U_I} dans ce cas". The finite case is thus explicitly set aside from strictness, and anabelian hypotheses are suggested for it.

10. **Scan 424: unproved claim. Keep.** The composite Π_{D_i^*} → Π_{U_J} → Π_{U_I} (i ∈ J∖I, J ⊃ I) is "constant", so that Π_{U_I} is deduced from Π_{U_J} by "bouchage des trous". Constancy alone does not say that Π_{U_I} is the universal such quotient; that would have to be imposed or proved.

11. **Scan 424: unproved claim. Correct.** The model "pouvait se visualiser" with a topological orientable surface X and a part 𝒳 meeting every connected component. For 𝒳 = I (𝒳 finite), the exceptional groupoid is the fundamental groupoid of X∖I = X∖{𝒳}, that is X minus the whole finite set 𝒳; the first pass had "X∖{x}". The text says one will have trouble mapping it into the others with strict transitivity, "qu'à cela ne tienne !". This agrees with the margin of scan 423 (note 9).

12. **Scan 424: own idea (first pass). Keep.** Comparing strict transition maps with maps defined up to natural isomorphism is a sensible test. The text itself only notes the difficulty in the exceptional case.

13. **Scan 425: unpursued implication. Keep.** Γ acts strictly on 𝒳, on the Π_{U_I} and on the Π_{D_i^*}, which it permutes ("N.B. qu'il permute entre eux"), commuting with all transition and local maps. The struck margin copy of "(qu'il permute entre eux)" shows that the phrase was added afterwards.

14. **Scan 425: unproved claim. Keep.** "On aura des difficultés, si 𝒳 est fini … pour la commutation stricte … mais passons" defers the finite case again.

15. **Scan 425: own idea (first pass). Keep.** The axiom read now is "si Γ′ est admissible alors tt ss-groupe Γ″ ⊃ Γ′ aussi" (upward closure), with admissible subgroups ≠ 1. Nothing is said about intersections, so testing closure under finite intersections remains a fair question.

16. **Scan 425: canceled draft. Keep.** The canceled conditions defined admissibility of Γ′ by 𝒳^{Γ′} meeting every connected component of 𝒳 = U_∅. They also considered the operation of Γ_P on π₁(U_I, P). This is abandoned material and not an assumption.

17. **Scan 426: conjecture / aim. Keep.** "Nous voulons des conditions qui assurent que 𝒳 et les Π_{U_I} etc. [peuvent|puissent] se reconstruire à isom. can. près" from the bare ("nues") groupoid or topos data with Γ-operators. This states an aim, not a theorem.

18. **Scan 426: conjecture / aim. Keep, notation corrected.** The single datum is the operation of Γ on the outer group with loops π₁(Π_{U_I}) attached to I (lower-case π₁; the first pass had Π₁). The data to be recovered are the Π_V for V ⊃ U_I, the Π_{D_i^*} (i ∈ I) and the action of Γ.

19. **Scan 426: own idea (first pass). Keep.** Test cases with different stabiliser patterns under condition 1° (Γ_P ≠ {1} of finite index) are a reasonable probe.

20. **Scan 427: unproved claim. Keep.** The direct direction is "immédiat, par l'opération de forage des trous". The task is the converse ("en sens inverse"): rebuilding Π_{U_I} and the action from Π_𝒳 (or rather the topos B_{Π_𝒳}).

21. **Scan 427: conjecture. Keep.** "sous réserve d'anabélianité, disons de Π_𝒳, on peut ± réconstituer Π_{U_I} et l'action de Γ dessus …". The sign after "anabélianité" is still unread.

22. **Scan 427: unproved claim. Correct.** The text reads "On veut au moins une description intrinsèque des éléments de 𝒳, et de l'action de Γ dessus, via cette action « molle »". The first pass had "On veut en avoir une" and "visible". So the minimal aim is to recover the points of 𝒳 with their Γ-action from the *soft* (outer) action alone. For 𝒳 connected this is an outer action of Γ on a group "à lacets (sans lacets !)".

23. **Scans 427–428: unproved claim. Correct.** The continuation reads "du moins si 𝒳 est infini donc qu'on puisse prendre I de cardinal arbitrairement grand". The infinitude of 𝒳 is given as what allows I to be taken arbitrarily large, hence π(I) anabelian for I "assez grand". The size threshold and the precise anabelian property are not stated.

24. **Scan 428: unpursued implication. Keep.** Condition 2°: the evident map U_I → Pt(B_{π(I),Γ♮}) ≅ {classes of π(I)-conjugacy of germs of splittings of the extension 𝓔(I) of Γ by π(I)} should be injective and Γ-compatible. Injectivity separates points but does not identify the image.

25. **Scan 428: open question. Keep.** "il faudrait pouvoir donner une caractérisation de l'image".

26. **Scan 428: unproved claim. Correct.** Compatible arithmetisations on the π(I), compatible with the hole-filling homomorphisms and the Γ-action, give "un hom canonique de Γ dans le groupe commun 𝚪 des autom. arithmétiquement (ext. de ces arithmétisations". The group is the bold 𝚪 (first pass: Π). Making this precise needs the definition of that common group and independence of the choices of representatives.

27. **Scan 428: unproved claim. Correct.** The parenthesis is "(et même Γ → M_{π(∅)=π}, — qui est déjà une donnée nettement plus forte)"; the first pass had "(cad = …" and "chose". The stronger datum is a homomorphism of Γ to M of π = π(∅) itself, compared with the homomorphism to the common group 𝚪. Grothendieck calls it markedly stronger without argument.

28. **Scan 428: own idea (first pass). Keep.** Restriction to open subgroups (germs) and π(I)-conjugation should be kept as separate equivalences when testing injectivity. The written words "germes de scindages" are secure.

29. **Scans 427–428: own idea (first pass). Keep.** A two-step diagram I ⊂ J tests how the point maps and the filling homomorphisms commute.

30. **Scan 428: own idea (first pass). Keep, with 𝚪 for Π.** Model the common group 𝚪 first on a short diagram of puncture sets and compare it with the group at I = ∅.

31. **Scan 429: proposed criterion. Correct.** One may suppose given a notion of admissible lifting making the map a bijection U_I = 𝒳∖I ≅ Pt_ad(B_{π(I)},Γ♮). "Ceci signifie … que *la notion d'admissibilité* satisfait aux conditions 1°) : 6°) vues ci-dessus" (first pass: "ce critère"). The conditions 1°–6° belong to earlier pages.

32. **Scan 429: conjecture. Keep.** What is to be called an admissible operation of Γ on an outer profinite group with loops "reste pour le moment conjectural".

33. **Scans 429–430: conjecture. Correct.** The experimental definition reads: an action Γ → 𝒯̂̂(π) (first pass: 𝓔̂̂) respecting an arithmetisation a, i.e. factoring through N_a, such that the image of Γ → N_a/𝒯̂_a = 𝚪_a is open (first pass: "= Π_a"), together with the non-normalisation conditions on scan 430. CSG elsewhere writes 𝒯̂̂(π) for Autextlac(π) (its line 6359). Whether this definition has the bijection property of note 31 is left open.

34. **Scan 430: unpursued implication. Keep.** For each hole-filling homomorphism π → π′_i, N(π)_i → M(π′_i), neither the corresponding image of Γ_i nor that of any open subgroup Γ′ of Γ_i may normalise an L′_j (j ∈ I(π′_i) = I∖{i}). Requiring this for all open subgroups makes it a condition on germs.

35. **Scan 430: conjecture. Keep, reading secured.** "peut-être même faudrait-il imposer π^{(Γ′+)} = (1), où Γ′+ est le noyau de Γ′ → Ẑ* (χ)". Then "on s'attend que l'on ait alors π^{Γ′} = (1), et si ce n'était le cas, il faudrait l'introduire dans la définition". This is to hold for each relative filling (I′ ⊂ I(π), i ∈ I′) defining Γ_{(I′,i)} → M(π(I′)).

36. **Scan 430, upper margin: conjecture. Correct.** The note is cancelled: long strokes cross it, and no witness carries it while all carry the lower note. It is an abandoned alternative. The condition just stated is perhaps superfluous and premature, and it might be that the subgroup K of M(π) normalising L_i and, modulo Ker(π → π′_i), L_j is "trop petit": its image in 𝚪 (or Π) = M(π)/𝒯̂(π) (letters doubtful) would not be of finite index. Treat it as a cancelled idea.

37. **Scan 430, lower margin: unproved claim. Correct.** CSG prints this note as footnote 118. It reads: "Plus généralement, pour i ∈ I′ ⊂ I = I(π), on impose que la vraie action de Γ_{I′,i} sur π(I′) correspondante [à i] ne normalise aucun sous-groupe L_j (j ∈ I∖I′) — on est ramené pour ceci au cas où I′ = I∖{j}, donc où π(I′) n'a (qu'une) seule classe [de] lacets… (si g ≥ 1)". The reduction to one remaining hole is asserted without proof. The genus condition is now read as g ≥ 1 (si|et still open).

38. **Scan 430: unproved claim. Correct.** The sentence ends "et qu'" and continues on scan 431: "il en est de même pour l'action induite sur chaque π(I′) …" (P044). A true action lifting a given admissible action is itself admissible (defines an admissible action on a π′ of type (g, ν+1)) iff the action, or rather its germ, normalises no L_i, and the same holds for the induced actions.

39. **Scan 430: own idea (first pass). Keep.** Γ′+ ⊂ Γ′ gives π^{Γ′} ⊂ π^{Γ′+}, so the imposed condition π^{(Γ′+)} = (1) implies π^{Γ′} = (1). Grothendieck's "on s'attend que l'on ait alors π^{Γ′} = (1)" must therefore mean "from admissibility" rather than "from the stronger condition", for which it would be trivial.

40. **Scan 430: own idea (first pass). Keep.** Compare one filling with two successive fillings, tracking normalisers of a remaining L_j and images of open subgroups. This tests the reduction claimed in the lower margin (note 37).

## Notes added in the second pass (own)

41. **Scan 421: own idea.** In the ink the kernel's target is N_a without a prime, while the extension is "de N_{a′} par L" and the map is Γ → N_{a′}. For L to be the kernel of the extension (N_a)_{I′} → N_{a′}, the target must be N_{a′}. The unprimed N_a in Ker(…) looks like a slip of the pen; the transcription keeps the ink.

42. **Scans 422 and 429: own idea.** With Γ profinite, "arithmétiquement fidèle" (Γ → 𝚪_a injective) makes Γ isomorphic to a closed subgroup of 𝚪_a. Adding the open-image condition of the experimental definition, the arithmetically faithful admissible actions are exactly those where Γ maps isomorphically onto an open subgroup of 𝚪_a. In that case condition 2° compares points of 𝒳 with sections over open subgroups of the arithmetic group, which is the setting of the section conjecture.

43. **Scan 424: own idea.** For I = 𝒳 the object set U_I = 𝒳∖I is empty, so restricting the fundamental groupoid of X∖I to U_I, as in the general case, would give the empty groupoid. That is what the margin of 423 excludes ("pas le groupoïde vide"). Grothendieck therefore takes the whole fundamental groupoid of X∖I = X∖𝒳, written "X∖{𝒳}" (the braces are a notational slip), whose objects are points outside 𝒳. Its object set is not U_∅ = ∅, so the maps from it cannot be inclusions on objects. This is exactly why strict transitivity fails in this case.

44. **Scan 428: own idea.** The step from "Γ → 𝚪" (exterior, arithmetic) to "Γ → M_{π}" (the stronger datum) is a lifting problem along M_π → 𝚪, whose kernel is of the type 𝒯̂(π). A lift exists iff the extension of Γ pulled back from M_π → 𝚪 splits. This is the same kind of splitting question as on scan 421. The comparison "nettement plus forte" is therefore measured by such a nonabelian obstruction, which the text does not discuss.

45. **Scan 427: own idea.** The word "molle" is the key term. The reconstruction is to use only the soft (outer) action of Γ on π, not a true action. This matches the later criterion on scan 430, where a true action lifting an admissible outer one is examined separately ("Notons qu'une vraie action …").
