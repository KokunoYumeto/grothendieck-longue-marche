# LM_P08 (scans 71–80): research notes, checked against the corrected transcription

Each first-pass research note (§ 4 of `answers/unzipped/LM_P08/LM_P08_notes.md`, numbered 1–23 there, R01–R23
here) is checked against `LM_P08_checked.tex` and kept, corrected or dropped, with the reason. Notes added in the
second pass are labelled S01–S03 ("second pass, own"). Kinds: conjecture, claim without proof, implication not
pursued, own idea. Literature named below is a lead for later reading; it was not checked against the corpus in this
pass.

Tally: 19 kept (several with a corrected quotation), 4 corrected, none dropped; 3 own notes.

## First-pass notes

**R01 — scan 71 — conjecture — KEEP.**
"Je présume qu'un peu de sueur permettrait de prouver que cela marche encore dans le cas général (sans supposer les
Γ_i = Im(ℰ_i → Γ) égaux à Γ)" is confirmed word for word. What is to be extended is the statement just before it,
that the π-conjugacy class of f : ℰ' → ℰ over Γ "suffit à déterminer l'hom 𝒟' → 𝒟 dans la cat. bordélique",
obtained only under Γ_i = Γ. A proof has to recover the boundary data when the Γ_i are proper open subgroups of Γ.

**R02 — scans 72–73 — claim without proof — KEEP, quotation corrected.**
The ink reads "les classes d'isomorphismes des couples (γ,λ) correspondent aux classes de L_i-conjugaison
(L_i = Ker(ℰ_i → Γ_i)) de sections de l'ext. ℰ_i de Γ_i par L_i" ("sections" over a struck "morphismes"). The added
datum is "une iso γ(D̃_i) ≃ D̃_i^* donnant l'isom identique par application des σ_i" (first pass: "l'iso … de σ_i"),
and the functor is named γ on the arrow Π_{D_i} → Π_{D_i^*}. The checks the first pass asks for (naturality,
compatibility with σ_i, independence of the chosen D̃_i^*) are not written in the text.

**R03 — scan 73 — claim without proof — KEEP.**
"(s'il y en a, et on sait qu'il y en a…)": the torsor Σ_i is asserted nonempty without argument at this point. The
text supplies the argument on scan 76 ("Donc on a bien trouvé une section de Π_{D^*} sur Π_D"), from the tower
O(∞,t) of roots of a uniformiser, under the local hypotheses of scan 75 (characteristic 0, henselian "jauge" with
residue field k = K_i).

**R04 — scan 73 — claim without proof — KEEP, sharpened.**
In continuous cohomology H^1(K_i, T(G_m)) ≃ lim_n H^1(K_i, μ_n) holds because the μ_n are finite: the obstruction,
lim^1 of the finite groups μ_n(K_i), vanishes (leads: Tate 1976, Invent. Math. 36; Jannsen 1988, Math. Ann. 280).
The display needs the full T(G_m) = lim_n μ_n over all n, as the next display writes it ("H^1(K_i,T(G_m)) ≃
lim_n (K_i^*)_n"); an ℓ-adic T_ℓ would give only the ℓ-part. The mathematics therefore does not support ℓ in the
subscript that is still open in the ink ("T_e|T_ℓ").

**R05 — scan 74 — claim without proof — KEEP; name of the map corrected, own check added.**
The map is the "hom kummérien" K_i^* → H^1(K_i, T(G_m)) (first pass: "canonique"); its kernel is ∩_n K_i^{*n}, and
the text asserts "Comme K_i est de t.f. sur Q, cet hom est injectif". Own check: on a normal proper model of K_i over
its field of constants F (a number field), the divisor of such an x is divisible by every n, so x ∈ F^*; its n-th
roots are algebraic over F, hence lie in F, and valuations with Dirichlet's unit theorem give x = 1. Finite type
over Q is used exactly here; for an algebraically closed field the kernel is the whole group.

**R06 — scan 74 — implication not pursued — KEEP.**
"un sous-K_i^*-torseur (i.e. un élément de Σ_i/K_i^*)" (K_i^* inserted) is confirmed: the datum is an orbit, not a
preferred splitting. Its behaviour under a change of the chosen D̃_i^* (scan 72) is not examined in the text.

**R07 — scans 74–75 — claim without proof (cancelled passage) — KEEP, readings corrected.**
The cancelled passage asserts that O_{s_i} = Ô_{X,s_i} "contient canoniquement le sous-corps K_i (p.ex. comme
clôture entière de K dans O_{s_i})" and that a uniformiser t "définit un K_i-isom O_{s_i} ≃ K_i[[T]]", where a struck
"K[[t" precedes "isom" (the first pass had one illegible item). Its continuation on scan 75 has "K_i = k(s)", and the
margin "faire un raisonnement local général, en laiss. tomber l'indice i" announces the general local argument with
k, O and L that replaces it. Both cancelled claims hold in characteristic 0 (Hensel lifts K_i/K uniquely into
Ô_{X,s_i}), but they are not part of the surviving text.

**R08 — scan 76 — claim without proof — KEEP, quotation corrected.**
"posant O' = O ⊗_k k' (qui est aussi une jauge hensélienne sur k' de corps résiduel k', de corps des fractions
L' ≃ L ⊗_k k'), on a des iso can." (first pass: "posons"). The ring isomorphisms are base change of
O[T_n]/(T_n^n − s); the field statement needs L ⊗_k k' to be a field, which holds because k is algebraically closed
in L (O integrally closed, residue field k). The first index of each pair of displays is still "n|∞" in the ink; the
witnesses read n, which makes the second display of each pair the limit of the first.

**R09 — scan 76 — claim without proof — KEEP.**
"Or si k' est alg clos, O' str. hensélien, on sait que L'(∞,t) est alors alg. clos" ("alors" is clear; the first
pass marked it doubtful). If O' is a henselian discrete valuation ring with algebraically closed residue field of
characteristic 0, every finite extension of L' is tamely and totally ramified, hence generated by a root of the
uniformiser (μ_n ⊂ k'), so the union of the L'(n,t) is algebraically closed: the henselian form of Puiseux's
theorem. The text then identifies k' with the algebraic closure k̄ of k in L'(∞,t) = L̄, which gives the section of
Π_{D^*} over Π_D.

**R10 — scan 76 — own idea (first pass) — KEEP, confirmed on the ink.**
Ink and both witnesses read s' = su^n, an arrow O(n,s) → O(n,s') and "par T_n → uT_n" (without the first pass's
bars). Under this map the source relation T_n^n − s goes to u^n s' − s = s(u^{2n} − 1), which is not 0 in general;
T_n ↦ u^{-1}T_n, or the same map in the direction O(n,s') → O(n,s), is consistent. The slip is the author's and
stays in the transcription unemended.

**R11 — scan 76 — claim without proof — KEEP.**
"d'où par passage à la limite" needs, for every n, an n-th root w_n of s'/s with w_{mn}^m = w_n, so that the level
maps commute with T_n ↦ T_{mn}^m. For s'/s ∈ 1+m such a system exists and is unique (Hensel in residue
characteristic 0: X^n − w has exactly one root ≡ 1), which is the case scan 77 uses; for a general unit the roots
need not exist in O. The second argument of the limit map, "λ(∞,u|n)", is still open in the ink.

**R12 — scan 77 — claim without proof — KEEP, quotation corrected.**
The ink reads "i.e. u|v ∈ 1+m (qui est un ss-groupe divisible de O^*] alors s,s' définissent des sections
isomorphes" (first pass: "s.-groupe", "]|)", and u where the letter may be v). The unique divisibility of 1+m is
immediate by Hensel (R11) and gives the compatible roots needed for the whole tower. The conclusion is an isomorphism
of sections, not equality of representatives, as the first pass noted.

**R13 — scan 77 — claim without proof — KEEP.**
"On constate aussitôt que cette application est compatible avec l'hom Θ : k^* → H^1(k,T(G_m)) sur les groupes d'op.
de ces torseurs" is confirmed. Replacing t by at (a ∈ k^*, lifted to O^*) changes the section by the Kummer class of
a or of a^{-1}, according to the convention of R10 and to how k^* acts on bases; the text fixes neither.

**R14 — scan 77 — own idea (first pass) — CORRECT.**
The author glosses (m/m²)^* as "(ens des bases de m/m²) qui est un torseur sous k^*": the star means the nonzero
vectors of the cotangent line, not a dual, and the later "plongement de m/m²" (no star) means the same set. The
comparison the first pass proposes is still useful against later conventions: a tangent vector is a basis of the
dual line, and t ↦ at scales it by a^{-1}, so indexing by tangent vectors (S01) inverts the k^*-action.

**R15 — scan 78 — implication not pursued — KEEP.**
"Il faudrait expliciter le comportement de cette structure suppl. relativement à des morphismes (provenant de
situations géométriques)" is confirmed. No formula is given; scan 80 then changes the morphisms themselves (the
partial index set I'_f), and such a formula would have to follow that change.

**R16 — scan 78 — implication not pursued — KEEP.**
"la relation avec la norme des 1-formes différentielles --- j'ai la flemme de l'expliciter en long et en large !" is
confirmed; the norm is not defined on these pages. The bases of m/m² of scan 77 are the nonzero 1-forms at s_i
(m/m² is the fibre of Ω¹ at s_i), so the norm presumably describes how these bases, and with them the geometric
sub-torsors, transform under a finite morphism, where a uniformiser t pulls back to a unit times t'^e for
ramification index e (own reading, unchecked).

**R17 — scans 78–79 — implication not pursued — CORRECT.**
The paragraph opens "La chose nouvelle que je retiens surtout" (first pass: "essentielle"), and the insertion "∀i"
gives one "famille transcendante" of splittings of ℰ → Γ for each i ∈ I (article and endings overwritten towards the
singular, still marked), indexed by a torsor under H^1(K_i|K, T(G_m)) ≃ lim (K^*)_n and containing the "géométriques"
sub-family indexed by a K^*-subtorsor. With "corriger … que ceux-là" on scan 79 (R20), the exhaustion concerns the
splittings just described, the whole transcendental families and those of the rational points of X\S, not the
geometric sub-families alone.

**R18 — scan 79 — claim without proof — KEEP.**
"On vérifie que les classes de π-scindages obtenus pour|par des indices i,i' distincts sont distinctes, même en se
ramenant aux π-scindages corr. de l'ext. de Γ par π_ab … (je ne fais pas le détail des vérifications, via
Mordell-Weil…)" is confirmed except "pour|par". The arithmetic input is presumably that over a field of finite type
over Q the rational points of the (generalized) Jacobian form a finitely generated group (Mordell–Weil, Lang–Néron),
so that its Kummer map is injective; lead, not checked.

**R19 — scan 79 — claim without proof — KEEP.**
"et distincts des scindages associés aux pts. rat/K de X\S" is confirmed; this second separation assertion is also
left without argument.

**R20 — scan 79 — conjecture — CORRECT.**
The ink reads "Il faudrait corriger la conj. bordélique dans le cas (III̅), en énonçant (sous toutes réserves,
encore !) qu'il n'y a (peut-être) pas d'autres scindages de l'ext. ℰ de Γ par π que ceux-là ...." (first pass:
"envisager", "III|IV", "ceux-ci"). The case is the overlined III of scans 66–67 (LM_P07), that of the splittings of
ℰ → Γ: the author corrects his earlier conjecture by admitting, besides the splittings from rational points of X\S,
the transcendental families at the points of S, and no others. This is the section conjecture for affine curves with
its cuspidal sections (S02).

**R21 — scan 80 — claim without proof — KEEP, answered.**
"(se prolongeant bien sûr en f̂ : X' → X)" is confirmed. For smooth complete curves the extension is automatic (a
morphism from a regular curve minus finitely many points to a proper curve extends uniquely, by the valuative
criterion), hence "bien sûr". Its consequence "S' ⊃ f̂^{-1}(S)_red, mais S' peut être strictement plus grand" is what
forces the partial index set I'_f.

**R22 — scan 80 — own idea (first pass) — KEEP.**
The corrected text defines τ only on I'_f: "τ est défini comme I'_f → I" (first pass: "reste|c'est défini"). With the
condition read as in R23, composition closes: for g : 𝒟'' → 𝒟' and f : 𝒟' → 𝒟 put I''_{f∘g} = τ_g^{-1}(I'_f) ⊂ I''_g,
and the composite kills the inertia of every other index. The commutation data α_{D*U} and the rest of the
definition continue on scan 81, beyond this package.

**R23 — scan 80 — own idea (first pass) — CORRECT, strengthened.**
The letter is ℰ'_{i'} in the ink (the script ℰ of "ℰ' → ℰ" just above; CSG/IUT "Ei′ ⊂ E′"), so the alternative
ξ'_{i'} is dropped, and read literally the condition is impossible as soon as the image of ℰ'_{i'} in Γ is
nontrivial, since f_ℰ is a homomorphism over Γ. Geometrically a puncture s'_{i'} sent into X\S has its loop killed:
f_ℰ should be trivial on the inertia L'_{i'} = κ'_{i'}(T(K̄)) and give on ℰ'_{i'}/L'_{i'} the splitting attached to
the point f̂(s'_{i'}) of X\S. The NB that follows in the CSG text (line 1743, scan 81) indeed passes to the quotient
of ℰ' by the invariant subgroup generated by the L'_{i'} = κ'_{i'}(T(K̄)), i' ∈ I'\I'_f. So ℰ'_{i'} is an author's
slip for L'_{i'}, kept in the transcription; the NB itself is to be checked on the ink in package P09.

## Second-pass notes (own)

**S01 — scans 76–77 — implication not pursued (own).**
The sections attached to a uniformiser t modulo 1+m, i.e. to a basis of the cotangent line m/m², are tangential base
points before the name: Deligne introduced these in 1989 as "points base à l'infini" (Le groupe fondamental de la
droite projective moins trois points, MSRI Publ. 16; section not checked). These pages already state, with short
arguments, their basic properties: independence of t modulo 1+m, k^*-equivariance through the Kummer map Θ, and
injectivity for k of finite type over Q. The contravariance noted in R14 (cotangent bases here, tangent vectors
there) has to be fixed before formulas are compared.

**S02 — scans 78–79 — conjecture (own reading).**
With the corrected readings, the conjecture of scan 79 is the section conjecture for an affine hyperbolic curve:
every splitting of ℰ → Γ comes from a rational point of X\S or lies in the cuspidal packet of a K-rational point of
S, a torsor under H^1(K, Ẑ(1)) = lim (K^*)_n that contains the tangential splittings as a K^*-subtorsor. K^* is
countable and its completion is not, so almost all cuspidal splittings are "transcendantes", which is presumably why
the author uses the word. Leads, not checked against the corpus: Grothendieck's letter to Faltings (27 June 1983);
J. Stix, Rational points and arithmetic of fundamental groups, LNM 2054 (2013), on cuspidal sections.

**S03 — scan 71 — own check (reading).**
In "L_i = Ker(p_i : ℰ_i → Γ) = 1|l' Im(κ_i : T(K̄) → ℰ_i ∩ π)" the witnesses' "= 1 =" would make L_i trivial,
against scan 73, where "κ_i : L_i ←∼ T(K̄_i)" identifies L_i with the inertia at s_i. The mathematics therefore
favours "l'Im(…)", the article before the image, while the ink (one hooked stroke, no clear apostrophe) leaves it
open; the transcription keeps \unsure{1|l'}.
