# LM_P048 (scans 471–480): research notes, checked against the corrected text

Each first-pass note (`answers/unzipped/LM_P048/LM_P048_notes.md`, §5, R01–R44) is kept, corrected or dropped, with
the reason. Notes marked **[2nd pass]** are mine. Quotations follow `LM_P048_checked.tex`. Notation: 𝕀Γ is the
doubled-stem Γ (`\mathbb{\Gamma}`), Γ, Γ′, Γ″ the single-stem Galois groups; 𝒯̂, 𝒯̂̂, 𝒢̂, 𝒢̂̂, 𝓜, 𝒩 as written on the
pages. Literature named in my notes is from memory and is to be checked before it is cited.

## A. First-pass notes

**R01 — scan 472 — conjecture — keep, corrected.** The text reads "d'où une application injective Discrét(π) ↪
Discrét(π′); on voudrait prouver qu'elle est compatible avec la relation d'équivalence [de l'arithmétisation, doubt]",
so that every arithmétisation (and prédiscrétification) of π gives one of π′. The goal is well-definedness on
classes; the injectivity on discrétifications is asserted, not proved (see C-1).

**R02 — scan 472 — conjecture — keep.** Injectivity of P⁺(π) → P⁺(π′) and A(π) → A(π′) is the stated aim; 473
reduces it to the relations (2). The A-map is drawn as a plain stroke, which does not change the statement.

**R03 — scan 472 — unproved claim — keep, corrected.** The reduction is "au cas où π′ est invariant caractéristique"
("invariant" is not cancelled). Existence is standard: a topologically finitely generated profinite group has finitely
many open subgroups of a given index, and their intersection is an open characteristic subgroup inside π′; injectivity
for π″ ⊂ π′ ⊂ π descends to π′ because the map for π″ factors through the map for π′.

**R04 — scan 473 — unproved claim — keep, corrected.** ① "L'hom 𝒢̂̂(π₀) → 𝒢̂̂(π′₀) envoie 𝓜(π₀) dans 𝓜(π′₀)" is the
"assertion repérée" of 474. The horizontal links of the diagram are the hand's inclusion sign (hook, no head, as in
Discrét(π) ↪ Discrét(π′) on 472), so the rows read 𝒢̂⁺ ⊂ 𝓜 ⊂ 𝒢̂̂; the first pass's doubt about their direction is
settled.

**R05 — scan 473 — unproved claim — keep.** The diagram is used to show that π₁ and π₀ giving the same oriented
prédiscrétification (resp. arithmétisation) of π implies the same for π′₁, π′₀; the claim is a well-definedness step,
separate from injectivity.

**R06 — scan 473 — unproved claim — keep, sharpened.** The intersections in (2) are taken in 𝒢̂̂(π′₀) through the
restriction map of ①; unless that map is injective (not stated) they mean preimages. The equivalence with injectivity
is asserted ("qui revient aux relations").

**R07 — scan 473 — own idea — keep, sharpened.** If r: G → G′ maps H ⊂ M ⊂ G into H′ ⊂ M′, then M/H → M′/H′ is
injective iff r⁻¹(H′) ∩ M = H. The first relation of (2), 𝒢̂⁺(π₀) = r⁻¹(𝒢̂⁺(π′₀)) ∩ 𝒢̂̂(π₀), implies this because
𝓜(π₀) ⊂ 𝒢̂̂(π₀); this is exactly why ① plus (2) give the injectivity of (3) on 474.

**R08 — scans 472–473 — own idea — keep.** Separating preservation, well-definedness on classes and injectivity
matches the order of the text (472, 473 ①, 473 (2)).

**R09 — scan 474 — unproved claim — corrected.** The sentence is "L'assertion repérée étant admise, l'assertion non
repérée signifie aussi que l'hom. can. (3) est injectif": ① (the marked assertion) makes (3) defined, (2) (the
unmarked one) gives its injectivity (R07), and surjectivity "par construction (via 𝕀Γ_Q)" gives ② "(3) est bijectif".
The first pass's "assertion propre / non propre" has no basis in the ink.

**R10 — scan 474 — conditional — keep.** The bijection (4) P_a(π) → P_{a′}(π′) is conditional ("on trouverait"),
compatible with the isomorphism (3).

**R11 — scan 474 — unproved claim — keep.** "inv. car." is "invariant caractéristique" of 472; the extension to an
arbitrary open π′ ⊂ π is the reduction of R03 read backwards.

**R12 — scan 474 — unpursued implication — keep.** The "correspondances arithm. extérieures" refer to § 28; to be
compared there.

**R13 — scan 475 — unproved claim — keep.** The connected groupoid of potential curves whose π₁ ext. is the common
value of the 𝕀Γ_{g,ν} rests on the conditional bijections (3).

**R14 — scan 475 — proposed construction — keep, corrected.** "comme des sous-groupes finis du m̄ π₀,₃" is a slip for
subgroups of finite index (476: "ss-groupe d'indice fini de π₀,₃"; CSG supplies "[d'indices]"). The cancelled first
version "un multiple commun N de 2g−2+ν et 2g′−2+ν′" fixed the index; see C-3.

**R15 — scan 475 — question — corrected.** The ink reads "indépendant de toute conjecture", not "de notre conjecture":
he asks which parts of the yoga hold unconditionally. The example ("le fait que les hom surjectifs can.
𝕀Γ_{g,ν} → 𝕀Γ_{g,ν′} (g le m̄, ν′ constant) n'est pas établi") omits its predicate; the transcription supplies none.

**R16 — scan 475 — conditional premise — corrected.** The premise is 𝒯̂̂(π′₀) ∩ 𝒢̂⁺(π₀) = 𝒢̂⁺(π₀), with the script T
of 𝒯̂_{g,ν} (479), not a double-hatted 𝒢. An equality A ∩ B = B says B ⊂ A: every element of 𝒢̂⁺(π₀), seen on π′,
lies in 𝒯̂̂(π′₀). It is therefore not the first relation of (2) restated; it is the input from which he expects the
bijectivity of 𝕀Γ_{π₀} → 𝕀Γ_{π′₀} (476).

**R17 — scan 475 — own idea — keep.** Testing the canonical identifications 𝕀Γ_{g,ν} ≅ 𝕀Γ_{g′,ν′} around a triangle
of correspondances remains the right coherence check.

**R18 — scan 476 — conditional consequence — keep.** "(qui est un énoncé de nature relativement anodin …) on
conclurait à la bijectivité": all conclusions down to "iso pour ∀(g,ν)" depend on the premise of R16.

**R19 — scan 476 — unproved claim — keep.** Factorisation through 𝕀Γ₀,₃ and isomorphism for ν large are distinct
claims; the condition "ν assez grand" is satisfiable for every g (C-5).

**R20 — scan 476 — cancelled draft — keep, corrected.** The cancelled block reads "l'image des noyau(x) Θ … est finie";
this weaker goal is the one proved without hypothesis on 477–478 ("sont finis"), so the cancellation postpones it.

**R21 — scan 476 — sufficient condition — keep, corrected.** The ink has "rev. étale de X₀,₃" (not 𝒰₀,₃). The inserted
"(avec sa str. à lacets)" is automatic for the subgroup of an étale cover of the thrice-punctured sphere, whose
punctures all lie over the three cusps.

**R22 — scan 476 — proof step — keep, corrected.** The ink reads "d'indice fini et car. dans π₀,₃" (CSG/IUT "contenu
dans", which is vacuous). Characteristic in π₀,₃ puts π″ in the situation (π, π′) with π′ characteristic, where the
hypothetical bijection gives 𝕀Γ₀,₃ ⥲ 𝕀Γ_{g″,ν″} (top row of the diagram on 477); such π″ exist (C-4).

**R23 — scan 476 — own idea — keep, made concrete.** For an étale cover of degree d of the thrice-punctured sphere,
multiplicativity of the Euler characteristic gives 2g−2+ν = d, so [π̂₀,₃ : π_{g,ν}] = 2g−2+ν; this is the index the
cancelled text on 475 was choosing.

**R24 — scan 477 — conditional claim — corrected.** "Notons p.ex. que les 𝕀Γ₀,ν → 𝕀Γ₀,₃ (ν ≥ 3) sont alors
bijectifs" holds under the premise of 475 ("si on savait"); the margin before "Soit une courbe algébrique" marks where
that hypothesis is dropped (C-6).

**R25 — scan 477 — unpursued implication — keep.** "ceci ne dit rien sur la fidélité éventuelle p.ex. de
𝕀Γ₀,₃ → 𝕀Γ_{g,0} = 𝕀Γ_g (g ≥ 2) ou 𝕀Γ₀,₃ → 𝕀Γ_{1,1} = 𝕀Γ₁": the closed and once-punctured cases stay open here;
see C-7 for the literature.

**R26 — scan 477 — own idea — keep.** Comparing kernels before and after forgetting punctures is the natural check
for the cases ν < 3.

**R27 — scan 478 — unproved claim — corrected.** "OPS que U′ est un rev. étale de (U₀,₃)_K", after enlarging K and
puncturing, is Belyi's theorem (any curve over a number field maps to P¹ unramified outside 0, 1, ∞, with a prescribed
finite set of algebraic points sent into {0, 1, ∞}). The reduction is not elementary; it rests on the "résultat du
russe" cited on 479.

**R28 — scan 478 — unproved claim — keep.** The finiteness of the image of Θ′ = Γ′ ∩ Θ in the outer automorphisms of
π′ ⊂ π̂₀,₃, then in 𝕀Γ_{π′}, 𝒩(π) and 𝕀Γ_π; the proof is R29.

**R29 — scan 478 — own idea — keep, simplified.** Elements of Θ act on π̂₀,₃ by inner automorphisms (Θ is the
kernel to 𝕀Γ₀,₃), and those of Θ′ preserve π′, so on π′ they act through N(π′)/π′, which is finite because π′ is
open. No centraliser argument is needed.

**R30 — scan 478 — unproved claim — keep.** The based action on π₁(U, P) (P rational over K) is obtained by applying
the outer result to U∖{P}; the comparison between the two is what remains to be written.

**R31 — scan 478 — claim — keep, status corrected.** Under the margin of 477 the finiteness of the kernels of
𝕀Γ₀,ν → 𝕀Γ₀,₃ (ν ≥ 3) is claimed without hypothesis: take U = P¹ minus ν rational points; the kernel is the image of Θ,
finite because Θ′ has finite image and Θ/Θ′ embeds in the finite Γ_Q/Γ′. By Belyi it is even trivial (C-7).

**R32 — scan 478 — claim — corrected.** The worry about one finite quotient for all ℓ is answered by the same
argument: ∏_ℓ T_ℓ(Jac C) = π̂₁(C)^{ab} and inner automorphisms act trivially on the abelianisation, so Θ′ acts on it
through its finite image in Out(π̂₁(C)); every abelian variety over K is a quotient of a Jacobian, whence "On voit
facilement que pour tte V.A. A" for all ℓ at once. The quantifier is "toute V.A." (not "la/les").

**R33 — scan 478 — conjecture — keep, with its answer.** "Il devient très difficile de s'imaginer comment il pourrait
se faire que Θ′ [doubt Θ] n'opère pas, en fait, trivialement !" The expectation is right: Θ = 1 by Belyi's theorem,
which he invokes on the next page (C-7).

**R34 — scan 478 — own idea — keep as a remark.** Of its two gaps, the first (one finite image for all ℓ) is closed by
R32 and the second (triviality) by Belyi (C-7).

**R35 — scan 479 — expectation — keep, identified.** "le résultat du russe que m'a signalé Deligne" is Belyi's theorem
(G. V. Belyi, Izv. Akad. Nauk SSSR, 1979), which gives the injectivity of Γ_Q → 𝕀Γ₀,₃; surjectivity is "par
construction" (474), so "est iso" follows if 𝕀Γ₀,₃ is the image of Γ_Q. GLOBAL_PASS T3 makes the same identification.

**R36 — scan 479 — unpursued implication — keep, letters settled.** 𝒩_{g,ν} is the extension of 𝕀Γ_{g,ν} by 𝒯̂_{g,ν}
(outer actions), 𝓜_{g,ν} the extension of 𝕀Γ_{g,ν} by 𝒢̂_{g,ν} (effective actions); outer actions of 𝕀Γ_Q on π₁ ≃
π̄_{g,ν} would be splittings of these, for ν large and g fixed.

**R37 — scan 479 — programme — keep.** The "question essentielle": an algebraic characterisation of 𝕀Γ₀,₃ and of the
𝒩_{g,ν}, and of the admissible splittings (those coming from curves over number fields).

**R38 — scan 480 — conjecture — corrected.** The opening reads "qu'[il suffit, struck] ce sont exactement les actions
relevant l'action ext. donnée, qui ne normalisent aucun ss-groupe à lacets, ou encore telle que π̂₀,₃^{Γ″+} [struck
sign] (1)": the admissible splittings are conjectured to be exactly the lifts that normalise no loop subgroup, with an
inserted equivalent ending in "(1)", his sign for the trivial group (relation sign struck). This is an early form of a
section-conjecture-type criterion, the excluded lifts being those attached to the cusps; compare the 1983 letter to
Faltings and the work of Nakamura and Stix on cuspidal sections.

**R39 — scan 480 — expectation — keep.** "il faille y apporter des conditions plus subtiles, faisant intervenir les
Frobenius" (ink "apporter"; CSG/IUT "ajouter").

**R40 — scan 480 — programme — keep.** An intrinsic description of admissible outer actions "sans avoir à passer par
des actions effectives admissibles".

**R41 — scan 480 — claim — keep.** An outer action on π̂₀,₃ does not induce one on an open subgroup π′; R43 gives the
elementary reason.

**R42 — scan 480 — unpursued implication — keep.** He assumes an outer action on π′ compatible with π′ → π̂₀,₃ and
deducing the action on π "(mod iso)"; the page ends at "de".

**R43 — scan 480 — own idea — keep.** C₃ ⊂ S₃: conjugation by a transposition is inner on S₃ but inverts C₃, which is
not inner on the abelian C₃. Correct.

**R44 — scan 480 — own idea — keep.** N_P(H)/H → Out(H) measures the ambiguity of restriction; self-normalising H is
the first test case.

## B. Second-pass notes

**[2nd pass] C-1 — scan 472 — unproved claim.** "d'où une application injective Discrét(π) ↪ Discrét(π′)" is asserted
without argument. In the characteristic case it reduces to: an element y ∈ π′ normalising D = π₀ ∩ π′ lies in D
(write x₁ = x₀y with x₀ ∈ π₀, using π₀π′ = π). That follows if π′ has trivial centre and an automorphism of the surface
group D that becomes inner on its completion π′ is inner (Grossman, 1974; to check).

**[2nd pass] C-2 — scans 473–474 — structure.** With "repérée" restored, 473–474 read: ① gives the map
𝓜(π₀)/𝒢̂⁺(π₀) → 𝓜(π′₀)/𝒢̂⁺(π′₀); (2) gives its injectivity; the construction via 𝕀Γ_Q gives surjectivity, hence ②;
(4) is the induced bijection of arithmétisations of types a, a′. Only (2) and the surjectivity are left unproved there.

**[2nd pass] C-3 — scan 475 — unpursued implication.** By C-5's Euler-characteristic count the index of π_{g,ν̃} in
π̂₀,₃ is forced to be 2g−2+ν̃; "quitte à passer de g,ν à g,ν̃ avec ν̃ ≥ ν" is the freedom to adjust that index, which is
what the cancelled "multiple commun N de 2g−2+ν et 2g′−2+ν′" was arranging before he replaced it by an arbitrary
correspondance.

**[2nd pass] C-4 — scan 476 — claim with proof.** Every open π_{g,ν′} ⊂ π̂₀,₃ contains an open subgroup π″ that is
characteristic in π̂₀,₃ (the intersection of the finitely many open subgroups of the same index), of some type
(g″,ν″) with 2g″−2+ν″ = [π̂₀,₃ : π″]. So the π″ "d'indice fini et car. dans π₀,₃" of 476 always exists.

**[2nd pass] C-5 — scan 476 — claim with proof.** For every g ≥ 0, (x,y) ↦ x^{2g+1} on y² = x^{2g+1} − 1 is branched
only over 0, 1, ∞, has degree 4g+2 and 2 + (2g+1) + 1 = 2g+4 points over them; so π_{g,2g+4} is an open subgroup of
index 4g+2 of π̂₀,₃ with its loop structure. The hypothesis "il suffit que la surface de type (g,ν) (ou (g,ν′) avec
ν′ ≤ ν) puisse s'obtenir comme rev. étale de X₀,₃" therefore holds for all ν ≥ 2g+4.

**[2nd pass] C-6 — scan 477 — status of the argument.** The margin "On ne fait plus d'hypothèse conjecturale (telle que
l'injectivité dans (3)" separates the conditional yoga of 474–477 (resting on the injectivity of (3)) from the argument
that begins "Soit une courbe algébrique": finite image of Θ′ in Out(π′), finite kernels of 𝕀Γ₀,ν → 𝕀Γ₀,₃, finite
action on Tate modules. That argument still uses Belyi's theorem in the reduction "OPS que U′ est un rev. étale de
(U₀,₃)_K" (R27).

**[2nd pass] C-7 — scans 477–479 — literature.** Belyi's theorem makes the outer action of Gal(Q̄/Q) on π̂₁(P¹∖{0,1,∞})
faithful, so Θ = 1 and the "impression" of 479 is correct. The faithfulness asked about on 477 for closed curves and
type (1,1) is, for the action on π̂₁ of a hyperbolic curve, due to Matsumoto (1996, affine) and Hoshi–Mochizuki (proper);
whether this settles 𝕀Γ₀,₃ → 𝕀Γ_g and 𝕀Γ₀,₃ → 𝕀Γ₁ as defined in LM (quotients by 𝒯̂⁺) is to be checked (GLOBAL_PASS T4).

**[2nd pass] C-8 — scan 475 — question answered later in the batch.** The corrected question "indépendant de toute
conjecture" (R15) is answered on 477–479: unconditionally, finiteness of the kernels (478); with Belyi, 𝕀Γ_Q ≅ 𝕀Γ₀,₃
(479); the identification of all 𝕀Γ_{g,ν} with 𝕀Γ₀,₃ still needs the bijectivity of (3).
