# LM_P05 (scans 41–50): research notes, checked against the corrected transcription

The first pass's research notes R01–R23 (`answers/unzipped/LM_P05/LM_P05_notes.md`, section 4) are checked here against
`LM_P05_checked.tex`. 12 are kept with corrections, 1 is sharpened, 10 are kept as they are, and none is dropped. Notes C1–C9 are mine
(Claude Opus 5.5, second pass). Quotations follow the corrected transcription; [a|b] marks a reading the ink leaves
open. Notation: 𝓔 is written E.

## First-pass notes

**R01 — scan 41 — claim without proof ("sauf erreur") — KEEP, corrected.** The reading is now "Reste à exprimer les
deux compatibilités de (f_{D*}, f_D, f_U, α_{D*D}, α_{De}, α_{D*U}, α_{Ue}) avec lui-= et avec K". The two
compatibilities are of the tuple with itself (the "première", the relation on the γ's and α's) and with K (the
"deuxième", f_{i′}∘k′_{i′} = k_i). The letter before (β_{i′}) on scan 41 is still open: ρ-like in the insertion,
overwritten in the box. Scan 42 restates the same formula with p, which is the only reading that type-checks
(β_{i′} ∈ E, the other factors in Γ).

**R02 — scan 42, left margin — claim without proof — KEEP, corrected.** It now reads: "Comme les E_i ↪ E sont
injectifs, f_{i′} est connu quand on connait f_E et β_{i′} (l'existence [de|des] f_{i′} est donc une condition sur
les couples f_E, β_{i′} … savoir que int(β_{i′})^{-1} f_E ρ′_{i′} [E′_{i′}] dans [ρ_i(E_i)|p_i(E_i)])". The note's
split stands: uniqueness comes from injectivity, existence from the image condition. Only ρ_i(E_i) makes the
condition meaningful (the image lies in E), although the glyph looks like a Latin p.

**R03 — scan 42, right margin — claim without proof — KEEP, corrected.** The note is now readable: "NB. OPS les
γ′_{i′}, γ_i égaux à 1 (en choisissant l'image de [ψ|φ]σ(D_i^*) [sur] Spec(K̄) via l'isom. de φ(ρ(D_i^*)) ≃ φ(Ũ)
avec Spec K̄". The γ's are set to 1 by transporting the base point along the comparison φρ ≅ ψσ (the 2-cell α of the
square), which is the simultaneous choice the first-pass note asked about. With γ = 1 the relation (*) becomes
α = p(β_{i′})α_{i′}.

**R04 — scans 42–43 — claim without proof — KEEP, corrected.** The reference is now identified. The formula
α_{i′} = γ_i^{-1}p(β_{i′}^{-1})αγ′_{i′}, i.e. αγ′_{i′} = p(β_{i′})γ_iα_{i′}, carries the tag (*) on scan 42, and
"la relation plus précise (*)" of scan 43 points to it. CK also tags it (∗). See C2 for what (*) gives on the Γ-face.

**R05 — scans 43–44 — implication not pursued — KEEP, corrected.** The heading in the ink is "Catégorie bordélique
précisée"; the witnesses' "Conjecture bordélique précisée" is their misreading. The last isomorphism is
E_i ∩ π ≃ T(K̄) with k_i written over the sign, without an arrowhead, so its direction is not fixed on scan 43. Scan 47
then defines k_i: T(K̄) ≃ Ker p_i, which settles the dictionary question the note raises.

**R06 — scan 44, 2° — claim without proof — KEEP, sharpened.** With the relation now read as ⊂ (not =), "∃ i ∈ I
(unique!)" has a proof under the natural geometric hypothesis (C4).

**R07 — scan 44 — own idea (first pass) — KEEP.** The diagnostic (two indices naming the same subgroup) is still
the right test of the bare definition. C4 names the hypothesis that excludes it: distinct cuspidal inertia subgroups
meet trivially.

**R08 — scan 44, left margin "NB : d_{i′} est aussi unique…" — claim without proof — KEEP.** The ink does not
settle whether the index in "k_i∘(d·id_{T(K̄)})" carries a prime. Uniqueness of d holds because T(K̄) is
torsion-free, so multiplication by distinct positive integers gives distinct maps.

**R09 — scan 44, upper left margin — question — KEEP, corrected.** The question is now read: "Les β_{i′} pas uniques
(si β_{i′} convient, aussi γβ_{i′}, avec [γ|γ_i] ∈ Im k_i). Mais α unique [?!|??]". C1 answers it.

**R10 — scan 44 — implication not pursued — KEEP.** The inversion "remplacer les β_{i′} par les β_{i′}^{-1}" and the
sense f_E ρ′_{i′} →^{β_{i′}} ρ_i f_{i′} are confirmed on the image.

**R11 — scans 44–45 — claim without proof — KEEP, corrected.** The text is "de *déduire* Π_D par factorisation
canonique", not "définir". The factorisation induces an iso on π_0 (no "les") and an epi on the π_1, followed by a
faithful functor. This is the 1-image factorisation of Π_{D*} → Π_e (essentially surjective and full, then
faithful).

**R12 — scan 45, vertical margin — claim without proof — KEEP, corrected.** The text reads "un syst. local de
groupes ([commutatifs|abéliens]) sur Π_{D*}, et on peut alors [définir|écrire] [k̄|k] : (φρ)^*T_K ≃ π_1(φρ)". Both
alternatives are abelian; the identification is the Kummer datum K of the quintuplet (C5).

**R13 — scan 45, oblique margin — implication not pursued — KEEP, corrected.** The ink names the integer: "doit être
la multiplication par un d [indice de ramification] (qui est une application π_0(Π′_{D*}) → N^*)". The check the
note proposes (behaviour of d under composition) is multiplicativity d_{g∘f} = d_f·(d_g∘π_0(f)); scan 50 shows the
character χ entering it.

**R14 — scans 45–46 — claim without proof — KEEP.** The cancelled "k, k′ modulo multiplication par un indice de
ramification" is confirmed: the author removed the Kummer condition from the 0-morphisms, which only keep the two
squares.

**R15 — scan 46 — claim without proof — KEEP, corrected.** On scan 46 the map E → Γ is labelled φ, not p (C6). The
last sentence reads "E_i est remplacé par groupe isom, l'isom défini à aut. int. près": the interlinear "l'isom"
belongs before "défini".

**R16 — scans 47–48 — question — KEEP.** The question about Kummer data in terms of outer groups is confirmed
verbatim.

**R17 — scans 47–48 — own idea (first pass) — KEEP.** The idea is unaffected by the corrections.

**R18 — scans 48–49 — claim without proof — KEEP, corrected.** Item a) now reads "[s'explicite en termes du choix
d'un isom ν : f(Ũ′) ≃ Ũ (un autre choix modifie f_E par un int(β), β ∈ E)]", parallel to b)'s "[s'explicite en
termes du choix d'un iso f_{D*}(Ũ′_{i′}) ≃^{ν_{i′}} Ũ_i …]". The notion being described is a "1-morphisme f de D′
dans D", not an "homomorphisme" as the witnesses have it.

**R19 — scan 49 — claim without proof — KEEP.** β_{i′} = p(α_{i′})α is confirmed, with α_{i′} ∈ E (box) and α ∈ Γ
(box). The witnesses' "α_{i′} ∈ Γ" is their error (C3).

**R20 — scan 50 — claim without proof — KEEP.** The ink reads "la compatibilité de f^0_{i′}", not the witnesses'
"fonctorialité". The β_{i′} of this formula is the element of Γ from scan 49, not the β_{i′} ∈ E of scans 41–44 (C7).

**R21 — scans 44 and 50 — own idea (first pass) — KEEP.** The ink has N^* on scan 44 and N on scan 50.

**R22 — scans 44, 49–50 — own idea (first pass) — KEEP.** Finite-quotient tests remain the right way to catch an
inverse or order slip, especially with two different β's in play (C7).

**R23 — scan 50 — next step announced — KEEP, corrected.** The second 1-morphism is f′ = (f′_E, τ′, (f′_{i′}), α′,
([α′_{i′}|α′_i])); the "g′" alternative is excluded by the ink.

## My notes (Claude Opus 5.5, second pass)

**C1 — scan 44 — answer to the question "Mais α unique ?!" (own idea).** By 1°, p∘f = int(α)p′ fixes α only up to
the centralizer of p′(E′) in Γ, and p′(E′) is open (scan 47: images of the p's are open). For Γ the absolute Galois
group of a number field, open subgroups have trivial centralizer (a standard fact; cf. Neukirch–Schmidt–Wingberg,
ch. XII), so α is unique. Over a finite field Γ ≅ Ẑ is abelian, int(α) = id for every α, and uniqueness fails
completely. The "?!" is therefore a genuine arithmetic hypothesis on K.

**C2 — scans 42–43 — what the relation (*) gives (implication not pursued).** On the Γ-face of the prism, (*)
αγ′_{i′} = p(β_{i′})γ_iα_{i′} gives int(α)int(γ′_{i′}) = int(p(β_{i′}))·int(γ_i)int(α_{i′}). The right face is thus
commutative up to int(p(β_{i′})), the image under p of the 2-cell int(β_{i′}) of the E-face; it is commutative on the
nose only when p(β_{i′}) centralizes Γ. "Commutative … sur Γ tout entier en vertu de (*)" should be read as
commutativity with this 2-cell, which (*) records exactly.

**C3 — scan 49 — the type of α_{i′} (reading with consequence).** The box reads α_{i′} ∈ E (with α ∈ Γ in c)), as
ρ_i f_{i′} = int(α_{i′}) f_E ρ′_{i′} and β_{i′} = p(α_{i′})α require. CSG and IUT print "α_{i′} ∈ Γ". On scan 51
(LM_P06) the author's own annotation interchanges the two ranges; scan 49 does not.

**C4 — scan 44, 2° — proof route for "unique!" (own idea).** Write L_i = Im k_i = E_i ∩ π. By 1°
(p∘f = int(α)p′), an element of E′_{i′} goes into π under int(β_{i′}^{-1})f exactly when it lies in
E′_{i′} ∩ π′ = L′_{i′}. So int(β_{i′}^{-1})f(E′_{i′}) ∩ π = d_{i′}L_i ≠ 1. If the image
lay in E_i and E_j with i ≠ j, then d_{i′}L_i ⊂ E_i ∩ E_j ∩ π = I_i ∩ I_j. For a hyperbolic curve, inertia subgroups
of distinct cusps meet trivially, so this is a contradiction and i is unique.

**C5 — scan 44, 2° — why ⊂ and not = (reading with consequence).** With "=", the same computation gives
d_{i′}L_i = L_i, which in T(K̄) ≅ Ẑ(1) forces d_{i′} = 1: only unramified maps would survive. The ink's ⊂ is the
reading compatible with the ramification index d_{i′} ∈ N^* that the same condition introduces. The witnesses'
"=" would change the category.

**C6 — scans 40, 44, 46, 47 — notation φ and p (reading note).** The map E → Γ is called φ on scan 46 (as in the
relation (*) φ f_E = int(α)φ of scan 40) and p from scan 47 on, where π = Ker p. The p of 1° on scan 44 is the same
map. Scan 45 also distinguishes φ′ (source triangle) from φ.

**C7 — scans 41–50 — two different β_{i′} (reading note).** On scans 41–44, β_{i′} is an element of E (the box on 41
writes E′; scans 42 and 44 write E), the commutation element of the E-squares. On scans 49–50, β_{i′} = p(α_{i′})α
is an element of Γ, and χ(β_{i′}) on scan 50 is its cyclotomic character. Under the convention fixed on scan 44
(β replaced by β^{-1}), the factor χ(β_{i′}) should be checked against χ(β_{i′})^{-1} with this second β.

**C8 — scan 45 — "2 foncteurs et 3 iso de foncteurs" (implication not pursued).** The quintuplet (f_{D*}, f_U,
α_{D*U}, α_{Ue}, K) counts K as the third isomorphism. The oblique margin turns it into a condition: f_{D*}^* of the
Kummer identification must be multiplication by d. The later 4-tuples f = (f_{D*}, f_U, α_{D*U}, α_{Ue}) and the
struck "k, k′ modulo …" on scan 46 show the datum becoming a property. 0-morphisms then carry no Kummer condition.

**C9 — scan 41 — the prime in "β_{i′} ∈ E′" (reading note).** The box on scan 41 writes β_{i′} ∈ E′. The relation
right below, f_E ρ′_{i′} = int(β_{i′})ρ_{τi′}∘f_{i′}, needs β_{i′} ∈ E, which is what scans 42 and 44 write. The prime
is the author's slip and is kept in the transcription.
