# LM_P02 (scans 11–20): research notes checked against the corrected transcription

Sources: `answers/unzipped/LM_P02/LM_P02_notes.md` and `second_pass/LM_P02_checked.tex`. Notes marked
"(second pass)" are mine; the ideas in them are checks or leads, not new results.

## First-pass notes

The first pass wrote no research notes for this package. Its notes file holds a table of 38 reading doubts, a table
of abbreviations and a paragraph on legibility and numbering, and `second_pass/ALL_RESEARCH_NOTES.md` records "(no
research notes found)" for LM_P02. So there is no research note to keep, correct or drop. The doubts are settled or
carried forward in `LM_P02_changes.md`. The abbreviation table needs these corrections against the checked text:

- **loc^t (uncertain), "probably localement". Correct.** On scan 12 the raised *t* is visible: "objets loc^t
  constants". On scan 13 the word is written out: "locale contractibilité".
- **Overlined m (uncertain), "probably même". Keep, now certain** (scan 14).
- **p.c. (alternative reading only). Drop.** Scan 20 reads "p.ex)".
- **ess., ssi (uncertain). Keep.** The ink does not settle them.
- **Missing. Add** resp. (scan 16), respectivement; sépar. (scan 18), séparable, which is followed on the page by a
  small glyph (a *k* or a raised "le").

## Second-pass notes

**S1. Scan 11, Prop. 1.11, claim without proof. (second pass)** The restored display records Hom_top(Ĉ,Ĉ′) ⊂
Hom(Ĉ′,Ĉ): a morphism of topoi is given by its inverse image, so Hom_top(Ĉ,Ĉ′) is the full subcategory of the
functors Ĉ′ → Ĉ that are left exact and commute with all inductive limits. A functor φ: C → C′ lands there as the
restriction φ*, which has both adjoints. The quasi-inverse is an equivalence by Diaconescu's theorem: morphisms
Ĉ → Ĉ′ are flat functors C′ → Ĉ, flatness in a presheaf topos is checked at each object of C, and a flat functor
from a groupoid to sets is representable (a filtered groupoid is equivalent to a point), so such a functor is a
functor C → C′ up to isomorphism.

**S2. Scan 11, 1.12, implication not pursued. (second pass)** For connected E ≃ Ens(G), E′ ≃ Ens(G′), 1.11 makes
Hom_top(E,E′) the category of homomorphisms G → G′ whose arrows u ⇒ v are the g′ ∈ G′ with v = int(g′)∘u; its
isomorphism classes are Hom(G,G′)/Int(G′). The page says "ponctués", so the explicitation has to compare the pointed
version (homomorphisms) with this unpointed one (homomorphisms up to conjugation). This is where the exterior
homomorphisms, and later the outer action Γ → Out(π), come from.

**S3. Scan 12, Thm 2.1, claims without proof. (second pass)** The NB "sans hyp. sur le topos E, E_lc est stable par
lim← finies" holds: two locally constant objects are constant over a common covering, and the constant-object
functor Ens → E is left exact. Commutation with arbitrary lim→ uses the hypotheses. Over each 1-connected generator U
a locally constant object is constant, maps between constant objects over a connected U come from maps of sets, and
the constant-object functor commutes with inductive limits; so coproducts and coequalisers of locally constant
objects stay locally constant.

**S4. Scan 12, margin, Grothendieck's question. (second pass)** The margin reads "peut-être faut-il supposer que E
ait « assez de points »": a doubt about the hypotheses, not a hypothesis in force. A lead, not checked in detail: the
usual Galois-theoretic proof of 2.1 uses no points. A locally constant L gives the functor U ↦ Hom(U,L) on the
1-connected generators, which inverts all their morphisms, so it is a functor on the groupoid obtained by inverting
them, and the comparison lemma glues back. If this holds, the question bears on 2.3, where Π1(E) is built from
points (S7, S9).

**S5. Scan 13, NB, Grothendieck's conjecture.** "Moyennant des hyp. convenables sur E (du type « locale
contractibilité »), on doit pouvoir définir les E_[i] pour ∀ i ∈ ℕ", with canonical morphisms E → ⋯ E_[i] → E_[i−1]
→ ⋯ E_[1] → E_0: the topos form of "tuage des Π_i pour i ≥ 2", a Postnikov tower. (second pass) E_[0] and E_[1] are
built from objects of E (sets over Π0(E), locally constant objects), and objects only detect Π0 and Π1. Reaching Π_i
for i ≥ 2 needs locally constant stacks (gerbes and their higher analogues), that is higher topoi: the direction of
Pursuing Stacks (1983) and of the later shape theory of ∞-topoi.

**S6. Scan 14, 2.3, reading of the arrow. (second pass)** "qui induisent des points de E_[1] grâce à E_[1] → E":
the morphism of topoi goes E → E_[1] (scan 13), so the arrow written here is the inclusion (2.1.1), the inverse
image. A fibre functor of E restricts along it to a fibre functor of E_[1]. The direction on the page is therefore
right, and the witnesses agree.

**S7. Scan 14, 2.3, claim without proof. (second pass)** "β est une équivalence (mais pas surjectif sur les
objets)": β is fully faithful by the definition of Π1(E). A multigaloisian topos has, up to isomorphism, one point
for each connected component (flat functors on a groupoid are representable, S1), and E and E_[1] have the same
components. So β is essentially surjective exactly when every connected component of E has a point; the claim needs
this hypothesis, a weak form of the "assez de points" of the margin on scan 12.

**S8. Scan 14, 2.3, example to Grothendieck's remark. (second pass)** "il ne s'ensuit pas nécessairement que les Hom
de Pt(E) soient tous de cardinal ≤ 1": a minimal example is the topos E of presheaves on the monoid M = {1, e} with
e² = e. A locally constant object is an M-set on which e acts bijectively, hence trivially, so E_[1] ≃ Ens and E is
1-connected. The point given by the representable functor has endomorphism monoid M, so a Hom of Pt(E) has two
elements and α is not even faithful.

**S9. Scan 15, implication not pursued. (second pass)** "bien qu'il soit ess. surj. si on suppose que E a
suffisamment de pts": as defined on scan 14, α: Pt(E) → Π1(E) is the identity on objects, so it is always
surjective on objects. The hypothesis on points is what makes the composite βα: Pt(E) → Pt(E_[1]) essentially
surjective (S7). On scan 15, "α" stands in effect for βα.

**S10. Scan 16, §3, implication not pursued.** With the corrected heading, §3 announces two variants,
"pro-multigaloisiennes" and profinite ("resp. profinies"), not a further kind of topos, and these pages give the
section no text. (second pass) Without local simple connectedness, the locally constant objects of a locally
connected topos give the classifying topos of a prodiscrete localic groupoid; this was worked out later (Moerdijk
1989, Bunge 1992). The profinite variant is the case of étale fundamental groups used in §5.

**S11. Scans 16–17, §4, claim without proof, with the margin "un peu vif !". (second pass)** "E′ → E est un
morphisme d'induction ssi C′ → C est fidèle". For a functor φ: C′ → C of groupoids, an automorphism of an object
(c′, u: φc′ → c) of the comma groupoid φ/c is an automorphism g of c′ with φ(g) = 1. So φ is faithful exactly when
these comma groupoids are discrete, that is when C′ is equivalent over C to the groupoid of elements of the
C-set c ↦ π0(φ/c); then E′ ≃ E_/S for that object S, as claimed.

**S12. Scans 17–18, implication. (second pass)** The insertion "classes d'isomorphie d'un(e) couple(s) (f,α)" and
the margin "Préciser les isomorphismes entre couples (f,α) et (g,β)" make the morphisms isomorphism classes. This
loses nothing: a 2-cell θ: f ⇒ g compatible with α and β must satisfy p₂θ = β⁻¹α, so θ is unique when it exists,
because p₂ is faithful. The 2-category of faithful groupoids over C is therefore equivalent to a category, and the
equivalence with E is one of categories.

**S13. Scan 18, claim without proof. (second pass)** "la catégorie E des schémas étales sur k est décrit … comme
les groupoïdes profinis au dessus du groupoïde profini (pt, Γ)": an étale k-scheme X gives the Γ-set X(k_s) and the
action groupoid of Γ on it, faithful over (pt, Γ). That groupoid is profinite only when X(k_s) is finite, so
"profinis" fits finite étale schemes, or has to be read component by component.

**S14. Scan 18, implication of a correction. (second pass)** The class announced is "[lisses quasi-projectifs de dim
≤ 1]", not "propres projectifs". It contains the open curves U = X∖S of §5, which the first-pass reading excluded.
The brackets and the inserted "[certains]" mark a class still to be cut out, which §5 does with the couples (X,S).

**S15. Scan 18, reading. (second pass)** In "le [struck ℰ] catégorie ℰ … est décrit" the masculine article and
participle survive from a first wording with a masculine subject (the struck ℰ after "le" suggests "le topos ℰ" or
just "ℰ"). "catégorie" came later without the agreement being changed; the witnesses normalise it to "la".

**S16. Scan 19, 5.1, claims. (second pass)** "(donc fini étale sur K)": S is finite and reduced over K, which has
characteristic 0, so S is a finite sum of spectra of finite separable extensions of K, hence finite étale. The
margin's letter (k or K) does not matter: the base of §5 is K. With S′ = f⁻¹(S)_red a morphism of couples restricts
to U′ = f⁻¹(U) → U, so removing further points (U′ ⊊ U with S′ ⊋ S) is not a morphism, and U′ → U is finite when f
is non-constant on every component.

**S17. Scan 20, Lemma 5.2, claim without proof; a hypothesis it needs. (second pass)** As written ("Soit Ω un corps
alg. clos") the lemma needs characteristic 0. In characteristic p, π1(A¹) is non-abelian (Artin–Schreier
coverings) although g = 0, n = 1, so a) does not imply d). For a hyperbolic U defined over a finite field, the powers
of Frobenius are infinitely many non-constant maps U → U, so d) does not imply c). In §5 the base field is of finite
type over ℚ, so the use made of the lemma there is unaffected.

**S18. Scan 20, margin e), claim. (second pass)** e) is the uniformization theorem: the cases of d) are exactly
those whose universal covering is the half-plane (the others give ℂ or the sphere). Whatever the sign in "Ω ∈/⊂ ℂ",
only an embedding Ω ⊂ ℂ gives X(ℂ), so this doubt of reading does not touch the mathematics.

**S19. Scan 20, margin f), Grothendieck's conjecture, marked "?!" (or "??").** For Ω = Q̄ and S ≠ ∅, f) offers a
further equivalent condition: the universal covering of U is isomorphic to that of P¹∖{0,1,∞}. (second pass) Since
e) already identifies the analytic universal coverings of all hyperbolic U with the half-plane, f) must be meant
algebraically, for the universal pro-étale covering over Q̄. There S ≠ ∅ restricts f) to affine U, whose
fundamental group is free like that of P¹∖{0,1,∞}, while for S = ∅ it is a surface group. Belyi's theorem (1979)
points this way (every curve over Q̄ has a map to P¹ branched only over {0,1,∞}, chosen to send S into {0,1,∞}, so
an open part of U is finite étale over P¹∖{0,1,∞}); I have not checked whether it yields an isomorphism of universal
coverings.

**S20. Scan 20, Déf. 5.3, definition and implication not pursued. (second pass)** The page's term is "anabélique";
the witnesses print "anabélien", the form used further on. The extension to couples over K goes by the connected
components of X_K̄ and is legitimate because d) is numerical (g and n do not change under extension of
algebraically closed fields), as the page says, "(par d) p.ex)". Components of dimension 0, which 5.1 a) allows
("dim ≤ 1"), fall outside 5.2 and need a convention.
