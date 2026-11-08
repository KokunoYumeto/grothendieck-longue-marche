# LM_P03 (scans 21–30): research notes checked against the corrected transcription

Sources: `answers/LM_P03_apparatus.md` (first-pass notes R1–R17) and `second_pass/LM_P03_checked.tex`. The context
from §5 (scan 19 and the witnesses) is that K is a field of finite type over Q (so of characteristic 0),
Γ = Gal(K̄/K), and in 5.1 S is a finite reduced subscheme lying in the 1-dimensional components of X. Notes marked
"(second pass)" are mine; the ideas in them are checks or leads, not new results.

## First-pass notes

**R1. Scans 21–22, unproved claim. Keep (corrected).** "On trouve ainsi un foncteur … dans la «catégorie des groupoïdes
profinis sur Π₁(K)», définie comme au n°4". The first pass read "comme on sait", but the page refers to n°4 for the
target category. A check of functoriality must use the morphisms defined there, including how the commutation
isomorphisms α compose.

**R2. Scan 23, unproved claim. Keep (corrected, proof added).** The page reads "dont l'image *sera* d'ailleurs
nécessairement ouverte donc d'indice fini". (Second pass) Proof: a connected X, locally of finite type over K, has a
closed point x with k(x) finite over K, so the image of π₁(X) → Γ contains the open subgroup Gal(K̄/k(x)). That image
is compact, hence closed, and a closed subgroup containing an open subgroup is open, so it has finite index. The claim
therefore holds for every such X, not only for the X of 5.1.

**R3. Scan 23, Conjecture 5.5, conjecture. Keep.** "La restriction du foncteur précédent … aux schémas projectifs
lisses de dim. ≤ 1 et anabéliens … est pleinement fidèle." The margin beside it now reads with certainty "C'est un peu
faux cf §9". See S1 and S2 below for the convention on S and the status of the conjecture.

**R4. Scan 23, margin, qualification of 5.5. Correct.** The doubtful word is *faux* (confirmed), and the reference is
"cf §9" (the witnesses print "n°9"). §9 does exist: the author's table lists "9. Structure tangentielle en les s ∈ S
(sections d'extensions «de deuxième type»)", ms. p. 34. What exactly is "un peu faux" has to be read in §9; these
pages do not say.

**R5. Scans 23–24, unproved claim. Keep.** The equivalence "Il revient au même de dire ceci" (the *m̄* is now read)
between the groupoid form 5.5 and the pointed form, labelled on the page "Conjecture 5.5 bis" (all witnesses print
"Définition"). Pro is right that the comparison has to use morphisms up to a chosen path, "(ou classe de chemins)
f(ξ) ≃ ξ′". Strictly base-point-preserving maps are not enough.

**R6. Scan 24, unproved claim. Keep.** "Ces conjectures se réduisent à la théorie de Galois, pour des X de dim 0." For
connected X = Spec L, with L finite separable over K, full faithfulness is the Galois correspondence between finite
étale K-schemes and finite Γ-sets. Nothing in the corrected text changes this.

**R7. Scan 24, unproved claim. Keep (argument added).** (Second pass) For X projective, smooth and connected over K,
K′ = H⁰(X, O̲_X) is a finite field extension, because it is finite-dimensional, reduced and has no nontrivial
idempotents. X is geometrically connected over K′, and X_K̄ is the disjoint union of the [K′:K] conjugates of X ⊗_{K′} K̄,
which all have the same genus. So the two formulations in the parenthesis agree.

**R8. Scan 24, unproved claim. Keep (sharpened).** "On voit aisément (prenant X′ = Spec(K), X = P¹_K ou courbe
elliptique sur K) qu'elles deviennent fausses sinon". (Second pass, medium–high) For P¹_K, the map π₁(P¹_K) → Γ is an
isomorphism, so all K-points induce the same morphism over Γ: faithfulness fails. For an elliptic curve E, the
sections up to conjugacy are H¹(Γ, T(E)), and the K-points enter through the Kummer map E(K) → E(K)^∧ ↪ H¹(Γ, T(E)).
Over a field of finite type over Q, E(K) is finitely generated, so this map is injective; but E(K)^∧ is uncountable
when the rank is positive, so fullness fails.

**R9. Scan 25, conjecture (expectation). Keep (with ink detail).** "On trouvera des conjectures (p.ex) pour X courbe
géom. connexe sur K de genre 1 (resp. 0), pourvu que S soit de degré ≥ 1 (resp. ≥ 3)." The ink shows the genus digits
rewritten (1 over 0 and 0 over 1), and the degree condition replacing a struck "restriction de S :". These are exactly
the hyperbolic cases 2g − 2 + deg S > 0, where deg S counts geometric points.

**R10. Scans 25–26, (6.1), unproved claim. Keep (corrected).** The labels "surj. sur Hom" (i_s) and "fidèle" (q_s), and
Π₁(s) ≃ Π₁(D_s). The lower map is j_s, not f_s, and the composite on the curved arrow is p_s or ρ_s, which the ink
does not decide. (Second pass) In characteristic 0, a henselian discretely valued field and its completion have the
same absolute Galois group (Krasner's lemma), so "(ou le complété, si on y tient)" changes nothing. Surjectivity of
Gal(K̄_s/K_s) → Gal(k̄(s)/k(s)) and injectivity of Gal(k̄(s)/k(s)) → Γ (k(s) is finite over K) are standard.

**R11. Scan 26, unproved claim. Keep (corrected).** "dont le noyau, on le sait par Kummer, est canoniquement isom. à
T_?(k̄_s) ≃ T(K̄_s) [≃ T(K̄)]". (Second pass) Pro's worry about residue characteristic does not arise: since
char k(s) = 0, all inertia is tame and Kummer theory over K_s^{nr} identifies it with Ẑ(1). The comparisons of μ_n
between K̄, K̄_s and k̄_s come from the chosen K-embedding and from reduction (bijective because n is invertible), so
the isomorphism is canonical once ξ_s is chosen. The subscript of the first T remains unread.

**R12. Scan 27, bracketed lemma, unproved claim. Keep (reading corrected).** The defined notion is introduced as
"[qu'on] peut appeler le π₁ relatif"; the first pass had "qu'on appelle le". Pro's proof route is right. To identify
the kernels at ξ₁ and ξ₂ over the same η, lift an arrow ξ₁ → ξ₂ to one mapping to id_η: connectedness gives an arrow,
and surjectivity on Hom corrects it. Two lifts differ by a kernel element, which acts trivially because the kernel is
abelian.

**R13. Scan 28, own idea (consistency check). Keep (confirmed and sharpened).** The display reads
"π₁(Π₁(D_S)/Π₁(S)) ≃ j_S*(𝒯(K))" without a star (CSG agrees; IUT prints D_S*). (Second pass, high on the mathematics) As
written, the left side is trivial, because Π₁(D_S) → Π₁(S) is an equivalence (each D_s is henselian, cf. the ≃ in
(6.1)). The isomorphism with j_S*(𝒯(K)) needs D_S*, as on scan 27. This is a slip in the manuscript, and the
transcription keeps the ink.

**R14. Scans 29–30, own idea. Keep (confirmed).** The cancelled 4°) reads "où σ est fidèle, ρ surjectif sur les Hom
et à noyau abélien". The final version has a) σ an isomorphism on π₀ and epi on Hom with abelian kernel, b) ψ
faithful, and c) ρ faithful. (Second pass) In the geometric situation the final version is the correct one: σ_S is
surjective on Hom with kernel the inertia, and ρ_S is faithful under hyperbolicity (see R15). So the cancelled draft
had the roles of σ and ρ exchanged.

**R15. Scan 30, bracketed conditions c)–d), unproved claim (expectation). Keep (made concrete).** "[ c) ρ est fidèle
... d) φ est épi mod. gr. finis sur les Aut ... ]". (Second pass, medium) d) is the abstract form of scan 23's "image
… ouverte donc d'indice fini" for π₁(U) → Γ. c) amounts to injectivity of the decomposition groups
Gal(K̄_s/K_s) → π₁(X∖S). This holds when the cusp inertia Ẑ(1) injects into the geometric fundamental group, that is,
when no geometric component of X∖S meeting S is an affine line (π₁(A¹_K̄) = 1 in characteristic 0), which is where
the anabelian hypothesis enters.

**R16. Scan 30, unpursued implication. Keep (reading corrected).** The page reads "(qui est *même* l'identité … mais il
vaut mieux oublier qu'il en *soit* ainsi)". The inference stands: α is to be treated as structure, so morphisms of
such systems must carry compatibility with α. That is what the next pages begin to define (CSG: "un morphisme de Π′
dans Π est un système de trois foncteurs …").

**R17. Scans 23–24, own idea. Keep.** Testing full faithfulness on morphisms Spec(K) → X is exactly the section-
conjecture part of 5.5 (see S2). R8 gives the two failures outside the anabelian range.

## Second-pass notes

**S1. Scan 23, Conjecture 5.5, unpursued implication (a convention to fix).** The parenthesis takes "S est la réunion
des composantes de dim 0", which does not fit 5.1 b), where S lies in the 1-dimensional components. In 5.5, therefore,
"anabélien" can only mean that the curve components are geometrically of genus ≥ 2, with the isolated points kept as
0-dimensional objects. Scan 24 ("elles ne concernent que des X tels que les comp. connexes de X_K̄ soient de genre
≥ 2") confirms this. Confidence: medium.

**S2. Scan 23, Conjecture 5.5 and the margin "C'est un peu faux cf §9", own idea with literature.** For dominant
morphisms of hyperbolic curves over a sub-p-adic field, which includes every field of finite type over Q, the Hom form
of 5.5 is a theorem of S. Mochizuki ("The local pro-p anabelian geometry of curves", Invent. Math. 138 (1999)). The
part with 0-dimensional sources, that is L-points of X, is the section conjecture, which is still open. Whether §9
("Structure tangentielle en les s ∈ S") is about this part has to be read there; this is a lead, not a finding.
Confidence: high for the literature, low for the link to §9.

**S3. Scan 21, §5.4, unpursued implication (reading-dependent).** In "plus gén. à ∀ schéma X loc de t.f. sur S|ξ, on
associe … Π₁(X) … muni du [hom.] canonique Π₁(X) → Π₁(K)", if the glyph is S (the witnesses' reading, favoured by the
ink), the base of the generalisation does not match the displayed map to Π₁(K) ≃ [Tors(Γ)], since with base S the
natural target would be Π₁(S). Worth checking against how §5.4 is used later. Confidence: low.

**S4. Scan 26, "(i.e.|ou) sur Π₁(K)", own idea.** The two readings say different things. j_s: Π₁(s) → Π₁(K) is
faithful but not an equivalence unless k(s) = K. A structure over Π₁(s) gives one over Π₁(K) by composing with j_s,
but not conversely, so "ou" (a weaker alternative) fits the mathematics better than "i.e.". The ink does not decide
(confidence: low).

**S5. Scan 28, bottom margin, unproved claim.** "… des comp. conn. de X∖S, ou encore de X" is true under 5.1 b): S
is a finite set of closed points on the 1-dimensional components, and removing finitely many closed points from an
irreducible smooth curve leaves a nonempty irreducible open subset. So π₀(X∖S) = π₀(X) (confidence: high).

**S6. Scans 28–30, unpursued implication.** The cancelled draft built the system over Π₀, the groupoid of components
("Ce group. Π₀ … des comp. conn. …"), with ψ: Π_D → Π₀ faithful and φ: Π_U → Π₀. The final version uses
Π_e = Π₁(Spec K) instead. These pages do not say whether the final data (a)–d)) still determine Π₀; condition a)
only fixes π₀(Π_{D*}) ≅ π₀(Π_D), the points of S. Confidence: medium.
