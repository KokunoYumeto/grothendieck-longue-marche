# LM_C4-248-266 (scans 248–266): research notes, checked against the corrected transcription

Each first-pass note (section 5 of `LM_C4-248-266_notes.md`, numbered here R01–R52 in their order) is checked
against `LM_C4-248-266_checked.tex` and kept, corrected or dropped, with the reason. Notes added in the second pass
are labelled S01–S04 ("second pass, own"). Kinds: conjecture/question, claim without proof, implication not
pursued, own idea. The pages are § 53, 5) of the manuscript (author's table: "Digression sur les revêtements des
germes d'espaces, et relations entre germes topologiques et germes différentiables des surfaces"). Notation:
D*ₓ the residual (punctured) germ at x, T̄ₓ the orientation module, 𝕊ₓ the circle of half-lines of Tang_x(X),
𝒜ₓ the ordered set of proper closed arcs of 𝕊ₓ (points allowed), Θ the functor (81).

## First-pass notes

**R01 — scan 248 — claim without proof — KEEP.** (56): Rev(D*ₓ) is an abelian Galois category whose π₁ is
identified ("canoniquement", still a doubtful reading) with T̄ₓ. The only justification on the page is that D*ₓ has
a "base" of spaces coming from discs centred at x whose π₁ form a constant projective system; independence of the
discs and behaviour under change of orientation are not addressed.

**R02 — scan 248 — claim without proof — KEEP, corrected.** "les rev. universels D*~ₓ de D*ₓ forment un groupoïde
connexe, de groupoïde fondamental T̄ₓ": the second "groupoïde" has the same ink as the first, but the sense is the
automorphism group of an object, i.e. "groupe fondamental". The proof obligations listed by the first pass
(existence of the covers on germs, comparison under restriction) stand.

**R03 — scans 249–250 — claim without proof — KEEP.** The homomorphism (60) (name now read K_x, as in (72)) is
described as π₁ of the inclusion D*ₓ ↪ U (61) and as the action of T̄ₓ on Γ(D*~ₓ, U' ×_U D*~ₓ); that the two
descriptions agree, and the left/right conventions, are not checked.

**R04 — scans 250–251 — claim without proof — KEEP, sharpened.** The NB of scan 250 supplies the step the note asked
for: if D*~ₓ comes from a universal cover of a punctured disc D*ₓ,ᵢ and ỹ, z̃ lie over y, z, then
Revuni(U, D*~ₓ) ≃ Revuni(U, y), Ũ = Revuni(U, z), and the choice of (62) is the choice of a path from y to z
(U loc. 1-connexe). Changing the path by an element of π changes (63) by an inner automorphism, hence the outer
homomorphism (65). The identification with Revuni(U, y) and its independence of i and ỹ are asserted, not proved.

**R05 — scan 252, left margin — question (author's proposal) — KEEP.** The author proposes to define an arc germ
as a germ of subset of X at x "satisfaisant à certaines propriétés…", which are not given. On scans 259–260 he
does pass from germs of subspaces to filters on X − x tending to x (images of cones), a step in this direction.

**R06 — scan 252 — claim without proof — KEEP.** The fibre functor (69) uses Rev([I]) ≃ (Ens), i.e. that [I] is
1-connected ("C'est évidemment un germe 1-connexe", stated without proof) and that truncating [0, ε] changes
nothing. The inserted D*_{X,x} names the residual germ inside the sentence (corrected placement), it adds no
condition.

**R07 — scan 251 — own idea (first pass) — KEEP.** For X = ℝ², U = ℝ² ∖ {0} the map T̄ₓ → π₁(U) ≃ ℤ is an
isomorphism; for X = S², U = S² ∖ {x} (a disc) it is zero. This correctly shows that (65) is an outer
homomorphism, not an embedding of a peripheral subgroup; high confidence is justified.

**R08 — scan 252 — own idea (first pass) — KEEP.** (68) only asks φ(0) = x and φ(t) ≠ x for t ∈ ]0, ε]; no
injectivity, so self-intersecting arcs are admitted. The construction (70) uses only the morphism [I] → D*ₓ, so
multiplicities do not matter there; they would matter for the subset-germ definition proposed in the margin.

**R09 — scan 253 — claim without proof — KEEP.** The factorisation [I] → D*~ₓ → D*ₓ and the "iso can." (71) are
asserted; they follow from the universal property of Revuni(D*ₓ, ([I], φ)) for a 1-connected [I], which is not
written out.

**R10 — scan 253 — implication not pursued — KEEP.** A germ of curve is "différentiable" if the germ of map I → X
is, "et de plus" the tangent map (73) at the origin is injective (scan 254); the definition is on germs, so
invariance under restriction is immediate, under reparametrisation it is not discussed (R11).

**R11 — scan 254 — implication not pursued — KEEP.** The half-tangent is the image of ℝ⁺ under (73); it is
unchanged by reparametrisations with positive derivative at 0, not by others. The page does not say which
reparametrisations are allowed.

**R12 — scan 254 — claim without proof — CORRECTED.** The equivalence (75) is "par construction" (inserted words):
(74) defines Isom(γ, γ') as the isomorphisms of the associated universal covers, so the functor is fully faithful
by definition, and since Revuni(D*ₓ) is a connected groupoid, essential surjectivity needs only one arc germ to
exist. The first-pass note overstated what remains to be proved.

**R13 — scan 254 — own idea (first pass) — KEEP (medium).** Two parametrisations of the same image give
canonically isomorphic objects of (75); the test is sound, its outcome predictable.

**R14 — scan 255 — claim without proof — KEEP.** (79): "Je vais définir une équivalence de catégories" from
differentiable arc germs to Π₁(𝕊ₓ), sending a germ to its half-tangent; the morphism bijections (80) are built on
scans 256–261.

**R15 — scan 255 — implication not pursued — KEEP.** The bijection (80) makes the passage from the punctured germ to
the circle of directions canonical, not only an abstract isomorphism of π₁'s; its naturality under diffeomorphisms
is the subject of (95)–(96) (scans 263–264).

**R16 — scan 255 — own idea (first pass) — KEEP.** Arcs with the same half-tangent and different higher-order terms
map to the same object of Π₁(𝕊ₓ); (92) (scan 261) gives the canonical comparison through {Δ}^~, so the test checks
exactly the step (91).

**R17 — scan 256 — claim without proof — KEEP.** Θ (81) is announced as a functor "qui sera une équivalence de
catégories"; functoriality is built on scans 258–260, the equivalence by the criterion (86bis).

**R18 — scan 256 — claim without proof ("on sait que") — KEEP.** Gr(𝒜ₓ) ≃ Π₁(𝕊ₓ): the arcs are closed, connected,
may be points, and the whole circle is excluded; with this, the poset's nerve is a model of the circle and (83)–(84)
(scan 257) make the equivalence explicit. Excluding 𝕊ₓ is essential (otherwise the poset has a top element and
Gr(𝒜ₓ) is simply connected).

**R19 — scan 256 — own idea (first pass) — KEEP.** Comparing with a finite cover of the circle by overlapping arcs is
a reasonable check of (83).

**R20 — scan 257 — claim without proof — KEEP.** (83)–(84): the zigzags {a} → A ← {b} define the morphisms of
Gr₀(𝒜ₓ); that they generate and satisfy exactly the relations of path classes is not proved.

**R21 — scan 257 — implication not pursued — CORRECTED.** The next page settles the sense: since 𝒢 is a groupoid,
a functor 𝒜ₓ → 𝒢 (86) factors uniquely through Gr(𝒜ₓ) ≃ Gr₀(𝒜ₓ) ≃ Π₁(𝕊ₓ), so the data (85) and (86) are
equivalent up to that canonical equivalence; scan 258 then gives the criterion for (85) to be an equivalence.

**R22 — scan 257 — own idea (first pass) — KEEP.** It is what (86bis) does with the two complementary arcs.

**R23 — scan 258 — claim without proof — KEEP, sharpened.** The criterion is correct: for a ≠ b the two arcs A, B
with end points a, b are complementary, the circuit {a} → A ← {b} → B ← {a} generates π₁(𝕊ₓ, a) ≃ ℤ, and a
functor from Π₁(𝕊ₓ) to a connected groupoid with π₁ ≃ ℤ is an equivalence iff it sends that generator to a
generator.

**R24 — scan 258 — claim without proof — KEEP.** (88)–(89): composing with "germe 1-connexe ↦ revêtement universel
qu'il définit" requires that category and the functor (89), not described.

**R25 — scan 259 — claim without proof — KEEP.** (88) sends A to a "filtre sur X−x tendant vers x" (replacing a
germ of subspace) and takes its germ; the equivalence relation on filters (germs) is not spelled out.

**R26 — scan 259 — claim without proof — KEEP, quote corrected.** The elements of 𝒜ₓ "s'identifient évidemment aux
cônes fermés C dans Tang_x(X), distincts de {0} et de l'espace tangent tout entier"; the correspondence (arc ↦ cone
of half-lines) includes point arcs (half-line cones) and is order-preserving.

**R27 — scan 259 — implication not pursued — KEEP.** The image of a cone depends on the local isomorphism f (90);
the strictly larger cones C' are introduced to remove this dependence (R28, S01).

**R28 — scan 260 — claim without proof — KEEP, quote corrected.** The image filter "ne dépend plus du choix de f"
(ink "plus", not "pas"): the image of C itself depends on f, the filter generated by the V∩(C'−{0}) no longer
does. The page gives no argument; S01 supplies one.

**R29 — scan 260 — claim without proof — KEEP.** With V convex, closed and symmetric, V∩(C'−{0}) is contractible
(in polar form {(θ, s) : θ in the proper arc A', 0 < s ≤ r(θ)}, an arc times a half-open interval) and the germ is
1-connected; this is stated as "évidemment".

**R30 — scan 260 — claim without proof — KEEP.** "on vérifie que ce dernier est bien une équivalence de groupoïdes,
via la vérification explicitée plus haut ((86bis))": the check that the two-arc circuit goes to a generator is not
carried out.

**R31 — scan 260 — own idea (first pass) — KEEP.** The polar-coordinate contraction is the standard proof of R29.

**R32 — scan 261 — claim without proof — KEEP, sharpened.** "γ ↪ {Δ}^~" means that the germ of the arc is finer than
the filter of the f(V∩(C'−{0})) for every cone C' strictly containing the half-line Δ; differentiability with
half-tangent Δ implies this (only the convergence of the direction of γ(t) to Δ is used), through any f of (90).

**R33 — scan 261 — implication not pursued — KEEP.** (92) and the diagram after it give the bijection (80) as
Isom(γ, γ') ≃ Isom(Θ(Δ), Θ(Δ')) ≃ Isom_{Π₁(𝕊ₓ)}(Δ, Δ'); compatibility with composition is not checked.

**R34 — scan 261 — own idea (first pass) — KEEP.** Writing the essential commutativity of (93) as a specified natural
isomorphism is a sound bookkeeping proposal.

**R35 — scan 262, margin — implication not pursued — KEEP.** "la difficulté ici provenait du fait qu'on n'avait pas
de morphisme direct entre le germe D*ₓ, et l'espace 𝕊ₓ": in a chart there is one (radial projection), see S02.

**R36 — scan 262 — claim without proof — KEEP.** (94) is defined as can ∘ Θ⁻¹, a quasi-inverse; its dependence on
choices is not recorded.

**R37 — scan 262 — implication not pursued — KEEP.** With a local isomorphism f (90), "la construction de Θ peut
s'expliciter comme une construction canonique dans un espace vectoriel V"; S02 gives that construction.

**R38 — scan 263 — claim without proof — KEEP.** The continuous dependence of D*~ₓ,Δ (and of V*~_Δ) on Δ is called
"tout à fait standard"; it is not shown.

**R39 — scan 263 — implication not pursued — KEEP.** An automorphism u of X fixing x and differentiable at x induces
ᵘD*ₓ and ᵘ𝕊ₓ (95); the comparison of their lifts is (96).

**R40 — scan 263 — own idea (first pass) — KEEP.** An angular coordinate makes the dependence explicit but needs a
choice; S02 avoids it.

**R41 — scan 264 — claim without proof — KEEP.** The bijection (96) of lift sets, an isomorphism of T̄ₓ-torsors, is
deferred: "la construction (96) sera faite dans les pages qui suivent, aboutissant à (122) p. 783" (outside this
package).

**R42 — scan 264 — question/plan — KEEP.** "J'ai envie de donner une description axiomatique de (94) et (96)": the
section E) "Axiomatisation: structure de corrélation entre rev. universels 𝕊̃ₓ et D*~ₓ" begins here.

**R43 — scan 264 — implication not pursued — KEEP.** 1) fixes V = Tang_x(X) (written 𝕍), 𝕊ₓ = V*/ℝ*⁺, 𝒜ₓ ↔ 𝒞ₓ
("cônes fermés" propres, ≠ V and {0}), and Ep(A), Ep(C) ("épaississement") the germ over D*ₓ; how Ep is defined
without a chart is the content of scans 259–260.

**R44 — scan 264 — own idea (first pass) — KEEP.** A reflection acts by −1 on T̄ₓ; testing (96) on it checks the
torsor conventions, which a rotation would not.

**R45 — scan 265 — claim without proof — KEEP.** 𝕊̃ₓ(A) and D*~ₓ(Ep(A)) are "l'un et l'autre Torseurs" under T̄ₓ:
nonempty and simply transitive because A and Ep(A) are 1-connected; stated, not proved.

**R46 — scan 265 — claim without proof — KEEP, sharpened.** Restriction goes from A' to A in (99), while (100) is
written H(A) → H(A'): it is the inverse of the composite of the restrictions, so (101) is covariant on the ordered
category 𝒜ₓ; no variance problem, transitivity follows from that of restrictions.

**R47 — scan 265 — implication not pursued — KEEP.** (102): a functor from 𝒜ₓ to the groupoid Tors(T̄ₓ) factors
through Gr(𝒜ₓ); the triviality of its monodromy is the claim of scan 266 (S03).

**R48 — scan 265 — own idea (first pass) — KEEP.** The monodromy of H is the difference of the two section
monodromies; S03 makes the sign condition explicit.

**R49 — scan 266 — claim without proof — KEEP.** "On sait que Gr(𝒜ₓ) est un T̄ₓ-groupoïde": (103)–(105) and the
marginal "i.e." identify Hom_{Gr(𝒜ₓ)}(A, A') with Isom_{Revuni(𝕊ₓ)}(𝕊̃ₓ,A, 𝕊̃ₓ,A'), a T̄ₓ-torsor; this rests on
(83).

**R50 — scan 266 — claim without proof — KEEP.** "Gr(H) est essentiellement constant, i.e. il définit sur les π₁
l'hom. nul T̄ₓ → T̄ₓ": not proved on the page; see S03 for what the proof needs.

**R51 — scan 266 — implication not pursued — KEEP.** The common value H(𝕊̃ₓ, D*~ₓ) with the isomorphisms iₐ (106)
"satisfaisant la condition de compatibilité" continues past the package ("s'expri-").

**R52 — scan 266 — own idea (first pass) — KEEP.** Computing the monodromy on a pair of complementary arcs is the
two-arc circuit of (86bis); it is the right test (S03).

## Second-pass notes (own)

**S01 — scan 260 — own idea (proof sketch; second pass, own) — confidence high.** Independence of f: for two local
isomorphisms f, f' with tangent map the identity, h = f⁻¹ ∘ f' satisfies h(v) = v + o(|v|) at 0. Given a cone C'
strictly containing C and a neighbourhood V of 0, choose a cone C'' strictly containing C and strictly inside C';
for V'' small, h(V''∩(C''−{0})) ⊂ V∩(C'−{0}), so f'(V''∩(C''−{0})) ⊂ f(V∩(C'−{0})), and symmetrically. The two
filter bases are cofinal in each other and define the same filter on X ∖ {x}. Only differentiability at 0 is used, matching the
"différentiable en x" asked of u on scan 263.

**S02 — scans 262–263 — own idea (second pass, own) — confidence high.** In a chart f (90), D*ₓ is the germ at 0 of
V ∖ {0}, and the radial projection V ∖ {0} → 𝕊 = (V ∖ {0})/ℝ*⁺ restricts to a homotopy equivalence on every
V∩(C'−{0}) with V convex; the universal cover of V* is the pull-back of that of 𝕊. This is the "construction
canonique dans un espace vectoriel V" of scan 262, it gives the continuity in Δ called "tout à fait standard" on
scan 263 without an angular coordinate, and it is the "morphisme direct" whose absence the margin of scan 262
names as the difficulty.

**S03 — scans 265–266 — own idea (second pass, own) — confidence medium.** Going once around 𝕊ₓ through arcs, the
transport in the T̄ₓ-torsors 𝕊̃ₓ(A) and D*~ₓ(Ep(A)) is translation by t₁ and t₂, the images of the positive
generator under the two identifications π₁(𝕊ₓ) ≃ T̄ₓ and π₁(D*ₓ) ≃ T̄ₓ (56). On H(A) = Isom(𝕊̃ₓ(A), D*~ₓ(Ep(A)))
the monodromy is t₂ − t₁. The claim "hom. nul" is therefore exactly t₁ = t₂, i.e. that the two identifications
agree under the comparison Θ; with opposite conventions the monodromy would be twice a generator, not 0.

**S04 — scan 249 — claim without proof (second pass, own).** "Si Rev(U) est multigaloisienne (p. ex. U loc
1-connexe)": with the digit read 1 (written over 0), the example is local simple connectedness, which gives
universal covers of every component and hence the multigaloisian structure. Local connectedness alone (the
underlying 0) would not suffice in general (spaces like the Hawaiian earring are locally connected and have no
universal cover).
