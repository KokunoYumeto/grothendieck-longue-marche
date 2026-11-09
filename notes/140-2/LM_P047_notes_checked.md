# LM_P047 (scans 461–470): research notes, checked against the corrected text

Each first-pass note (`answers/unzipped/LM_P047/LM_P047_notes.md`, §5) is kept, corrected or dropped, with the reason.
Unnumbered first-pass bullets are numbered here by scan and order (464-1, 464-2, …). Notes marked **[2nd pass]** are
mine. Quotations follow `LM_P047_checked.tex`. Notation: X_g = V_0 ∪ ⋃_j T_j (sphere X_0 minus 2g antipodal disks,
plus g tubes); ρ_j the twist of (29) in T_j (a full Dehn twist: ρ_j(z,t) = (z·e^{iπ(t+1)}, t)); ℋ = ⟨ρ_j⟩;
𝒢 = ℋ ⋊ {1,τ}; F = 𝔻_{2g} × ⟨τ⟩.

## A. First-pass notes

**461-R1 — scan 461 — unproved claim — keep, sharpened.** The semidirect product 𝒢 = ℋ ⋊ {1,τ} follows from (41)
(τ_{I'} = ρ_{I'}τ), the normality of ℋ shown on scan 460, τ ∉ ℋ (orientation character) and (42). As homeomorphisms
ℋ ≅ ℤ^I is immediate (twists of infinite order with disjoint supports); in the mapping class group it is the standard
independence of Dehn twists about disjoint, pairwise non-isotopic essential curves (here a cut system).

**461-R2 — scan 461 — unpursued implication — keep.** The whole coset τℋ consists of anti-involutions; the conjugacy
question is taken up on scan 463. The ink calls this coset ℋ⁻ (l. 2) and ℋ^{-1} (l. 9), not 𝒢⁻; the note is unaffected.

**461-R3 — scan 461 — unproved claim — corrected.** The gap is smaller than stated: σ = τ on V_0 has no fixed point
there, (44)–(45) give the fixed set in each tube exactly (empty or the middle circle S_j×{0}), and the tubes are disjoint,
so X_g^σ is the disjoint union of the circles with n_j odd and (46) counts all components.

**462-R1 — scan 462 — unpursued implication — keep.** The index |I'_u| forgets which tubes carry odd exponents; the
parity vector in ℋ/ℋ² is the finer invariant used on scan 463 (see 463-R4 for its orbits).

**462-R2 — scan 462 — unproved claim — corrected (reading and status).** The sentence reads "Il en résulte par des
raisons générales que u est conjugué dans 𝒜_g = Aut(X_g) (par un élément de A_g^+) à τ_{I'} = ρ_{I'}τ = τρ_{I'}^{-1}
ou aussi ρ_{I'}^{-1}τ = τρ_{I'}" (not "Il est visible"; the last formula is not cancelled). The claim is proved by the
criterion of scan 463: for ρ' = ∏ρ_j^{n_j}, ρ'' = ρ_{I'_u}^{-1}, ρ'ρ''^{-1} = ∏ρ_j^{n_j+δ_j} (δ_j = 1 iff n_j odd) lies in
ℋ², so ρ = ∏ρ_j^{(n_j+δ_j)/2} ∈ ℋ ⊂ 𝒜_g^+ conjugates u to τ_{I'_u}. The "general reasons" (Weichold's classification of
real structures by number of ovals and dividing type) give the same, since X_g minus part of a cut system is connected.

**463-R1 — scan 463 — unpursued implication — keep.** ℋ-classes of anti-involutions in 𝒢 ↔ ℋ/ℋ² ≅ (ℤ/2)^g (2^g
classes), against g+1 classes in Aut(X_g) (one for each number |I'| of ovals).

**463-R2 — scan 463 — conjecture (expectation) — keep.** An informal preference, with no extremal statement; the
symmetry group realised is 𝔻_{2g} × {±1} ⊂ O(3), of order 8g (scan 464).

**463-R3 — scan 463 — unproved claim — keep.** Scan 465 asserts the equivariant construction ("la surface X_g est
déterminée sans ambiguïté, et le groupe 𝔻_{2g} y opère par transport de structure"); what has to be checked is the
μ_{2g}-equivariance of the tube gluings and that the half-turns act on the tubes compatibly with the (z,t) coordinates.

**463-R4 — scan 463 — own idea (first pass) — corrected: computed.** 𝔻_{2g} acts on the g diagonals through a dihedral
group of order 2g (the half-turn about the polar axis acts trivially) and τ does not change parities, so the
𝔻_{2g}^~·ℋ-classes of the anti-involutions τρ (ρ ∈ ℋ) are the subsets of ℤ/g up to dihedral symmetry, i.e. binary
bracelets of length g. For g ≤ 3 these are g+1, as in Aut(X_g); from g = 4 on there are more (g = 4: 6 against 5,
adjacent versus opposite pairs of diagonals), so the remaining fusion needs mapping classes outside 𝔻_{2g}^~ ⋉ ℋ.

**463-R5 — scan 463 — own idea (first pass) — kept, answered by 463-R4.** Small genera g ≤ 3 already realise all
Aut(X_g)-classes of the τρ inside 𝔻_{2g}^~ ⋉ ℋ; g = 4 is the first genus where they do not.

**464-1 — scan 464 — unproved claim — corrected.** τz = −1/z̄ is the antipodal map −id ∈ O(3), which is central, so the
commutation with 𝔻_n ⊂ SO(3) and 𝔻_n^~ ≅ 𝔻_n × ℤ/2 (order 8g for n = 2g) are immediate; z ↦ 1/z̄ is the reflection in
the equatorial plane and z ↦ −z the half-turn about the polar axis, as written. The extra ζ-like glyph in
"u_{ζ,α,β} = ζu_{ζ,α}τ^β" stays unread; the two case formulas below it contain no extra factor.

**464-2 — scan 464 — unpursued implication — corrected (reading).** The reservation reads "τ renverse l'orientation,
donc est à manier avec réserve pour ce qui concerne le 'transport de structure' dans la situation présente" ("est à"
and "manier" written over cancelled words; no "à priori"). Its mathematical content is (42): transport by an
orientation-reversing map turns a Dehn twist into the inverse twist, so 𝔻_{2g}^~ acts on ℋ by signed permutations.

**464-3 — scan 464 — unproved claim — keep.** The margin condition "D'_0 ne rencontre pas ζD'_0, où ζ = exp 2iπ/2g"
makes the 2g holes disjoint; as τ(ζ) = −ζ on 𝕌, the holes form g antipodal pairs, as needed.

**464-4 — scan 464 — own idea (first pass) — keep.** A spherical cap about P_0 = 1 of angular radius < π/2g is disjoint
from its rotates by μ_{2g} (centres 2π/2g apart on the equator), which makes the margin condition explicit.

**465-1 — scan 465 — unproved claim — keep.** (49) for orientation-preserving u ∈ 𝔻_{2g} follows once u maps tubes to
tubes in the standard coordinates and commutes with τ on V_0. The ink writes "le polygone à 2μ côtés" (a slip for 2g).

**465-2 — scan 465 — unproved claim — keep.** For orientation-preserving u the twist of T_j is carried to the twist of
T_{u(j)} whether or not u exchanges the ends of the tube, so the display with the cancelled number (51) holds as an
identity of homeomorphisms when the tube coordinates are transported by u.

**465-3 — scan 465 — unpursued implication — corrected.** There is no kernel to compute: on V_0 an element uh
(u ∈ 𝔻_{2g}, h ∈ 𝒢) acts as u or as uτ ∈ O(3), which forces u = 1 and h ∈ ℋ, and a non-trivial element of ℋ moves
points of some tube; the action of 𝔻_{2g}·𝒢 on X_g is faithful.

**465-4 — scan 465 — question — keep.** The extension of the 𝔻_{2g}^~ action is settled on scan 466 (τ_{X_0} ↦ τ_g).

**465-5 — scan 465 — own idea (first pass) — keep, answered.** On one tube, orientation-preserving symmetries
transport twists to twists and τ inverts them (42): "permute versus invert" is exactly the orientation character.

**466-1 — scan 466 — unproved claim — keep.** τ_g commutes with 𝔻_{2g} because −id is central in O(3) and the tube
extension of τ is chosen equivariantly.

**466-2 — scan 466 — alternative convention — keep.** τ_I has the g middle circles as fixed set (g ovals, non-dividing),
τ_g none: two non-conjugate real structures, either of which could represent τ_{X_0}. The raised mark on τ_I in the
fixed-set sentence is still unread.

**466-3 — scan 466 — unproved claim — keep.** τ_I = ρ_Iτ_g commutes with 𝔻_n because ρ_I = ∏ρ_i is 𝔻_{2g}-invariant
by the display uρ_ju^{-1} = ρ_{u(j)} of scan 465; the argument is complete given that display.

**466-4 — scan 466 — opinion ("il ne semble pas important") — keep.** The two conventions differ by ρ_I, all of whose
exponents are odd, so ρ_I ∉ ℋ² and τ_g, τ_I are not even ℋ-conjugate (nor conjugate in Aut(X_g): 0 versus g ovals).

**466-5 — scan 466 — unproved claim — keep.** 𝔻_{2g}^~.ℋ ⊃ 𝒢 = {1,τ_g}.ℋ: τ_g ∈ 𝔻_{2g}^~ acts by inversion and
𝔻_{2g} by permuting the ρ_j; this signed-permutation module is what (52) must encode (see 469-1). The ink numbers this
display (51); the witnesses print (52).

**466-6/466-7 — scan 466 — own ideas (first pass) — merged and answered.** The change of convention is the change of
splitting of 𝒢 → {±1} from τ_g to τ_I = ρ_Iτ_g; by 466-4 the two splittings are not ℋ-conjugate.

**467-1 — scan 467 — programme (conjecture kind) — keep. develop: yes.** "Expliciter l'action extérieure de ce
produit ½ direct sur le groupe fondamental π_g, avec une attention toute particulière à l'action du groupe (ℤ/2ℤ)³ …
qui stabilise un des cylindres T_j." Statement to attack: *for the antipodal-tube model of X_g (holes at μ_{2g} on the
equator, g tubes joining antipodal holes), give a presentation of π_1(X_g, pole) adapted to the tubes (the surface
relation in this "panachée" arrangement) and compute ε_0, ε_1, τ_g, ρ_j and the stabiliser (ℤ/2)³ of one tube as
explicit outer automorphisms.* Status: the action of twists on π_1 is classical (e.g. Zieschang–Vogt–Coldewey;
Farb–Margalit, *A Primer on Mapping Class Groups*); I know no treatment of this configuration; a finite computation.

**467-2 — scan 467 — unproved claim — keep, verified.** The stabiliser in 𝔻_{2g} of the diagonal {ζ_0, −ζ_0} is
{1, c, ε, εc} (c the half-turn about the polar axis, ε the half-turn about the axis through ζ_0); with −id this gives the
eight sign changes in the orthonormal frame (axis through ζ_0, orthogonal equatorial axis, polar axis), for g ≥ 2.

**467-3 — scan 467 — programme — corrected (reading changes the content).** Item 2 reads "Étendre l'action sur π_g du
groupe de Teichmüller (plus ou moins) 'spécial' de chacun des T_j, en l'action d'un groupe analogue d'un ensemble plus
grand obtenu en lui rajoutant une 'lanière' L (d'où un tore à 1 trou …)", not "Étudier … ou l'action": the plan is to
extend the action from the tube's group to the groups of the one-holed torus T_j ∪ L and of the two-holed torus
T_j ∪ L ∪ L'; "spécial" presumably means fixing the boundary pointwise.

**467-4 — scan 467 — unproved claim — keep, verified.** T_j ∪ L (annulus plus a band joining its two boundary circles
through V_0) has χ = −1 and one boundary circle: a one-holed torus; adding L' = τ(L) gives χ = −2 and two boundary
circles: a two-holed torus. Both statements are right; the drawings agree.

**467-5 — scan 467 — margin claim — keep; known.** The mapping class group of the one-holed torus fixing the boundary
is the braid group B_3, a central extension 1 → ℤ → B_3 → SL(2,ℤ) → 1 (the boundary twist (ab)^6 generates an index-2
subgroup of the centre), and B_3 is the preimage of SL(2,ℤ) in the universal cover of SL(2,ℝ) (classical; cf. Milnor,
*Introduction to Algebraic K-Theory*, §10). Grothendieck's "extension centrale remarquable" is exactly this.

**467-6 — scan 467 — own idea (first pass) — merged into 467-1.**

**467-7 — scan 467 — own idea (first pass) — keep, answered.** Boundary fixed pointwise gives B_3 (the central
extension); boundary only preserved, or a puncture, gives SL(2,ℤ). The "spécial" group of the margin is the first.

**468-1 — scan 468 — conjecture — corrected (reading changes the content).** The text reads "Il est possible qu'il
faudra considérer de près ce dernier, pour étudier les relations entre les éléments de 𝒯_g provenant des ensembles
précédents": the two-holed torus just described is to be studied closely for the relations among mapping classes
coming from the tube, the one-holed and the two-holed tori; nothing about pairs ("pris a deux"). Later presentations
of Mod(S_g) do state relations through such small subsurfaces: chain relations on one- and two-holed tori, lantern
relations on four-holed spheres (Hatcher–Thurston 1980; Wajnryb 1983; Gervais 2001).

**468-2 — scan 468 — conjecture — keep.** Writing ∏[a_i,b_i] = 1 for handles arranged "panachée" (all tubes crossing
the equator) instead of "à la queue-leu-leu" is part of the computation of 467-1.

**468-3 — scan 468 — unproved claim — corrected.** All listed relations hold for the geometric generators (ε_1 fixes
the tube j_0 and preserves orientation, so it commutes with ρ_0 and τ; c = (ε_0ε_1)^g preserves every tube; τ commutes
with 𝔻_{2g}); the defect is completeness, see 469-1. The NB margin now reads "ε_0 bouge le sommet du repère, ε_1 l'arête
et pas le sommet, donc ε_1(j_0) = j_0": ε_0, ε_1 are the reflections of a flag (vertex, edge) of the 2g-gon.

**468-4 — scan 468 — unpursued implication — kept, answered by 469-1.** The information missing from the relations is
exactly the commutation of ρ_0 with its 𝔻_{2g}-conjugates.

**469-1 — scan 469 — unproved claim ("sauf erreur") — corrected: false for g ≥ 2. develop: yes.** (52) says that
⟨ε_0,ε_1,τ⟩ = F = 𝔻_{2g} × ⟨τ⟩ and that τ' is an involution commuting with K = ⟨ε_1, (ε_0ε_1)^g⟩ ≅ (ℤ/2)²; the group
presented is therefore the amalgam F *_K (K × ⟨τ'⟩) of two finite groups, which is virtually free and cannot be
𝔻_{2g}^~ ⋉ ℋ ⊃ ℤ^g when g ≥ 2 (for g = 1 both are (ℤ/2)² × D_∞, and (52) is right). Since τ(τ'τ)τ = (τ'τ)^{-1} already
follows from τ² = τ'² = 1, the missing relations are only that x = τ'τ (= ρ_0) commute with its conjugates. Statement to
attack: *for g ≥ 2, (52) together with [τ'τ, (ε_0ε_1)^k τ'τ (ε_0ε_1)^{-k}] = 1 for 1 ≤ k ≤ ⌊g/2⌋ is a presentation of
𝔻_{2g}^~ ⋉ ℋ, while (52) alone presents the virtually free group (𝔻_{2g} × ℤ/2) *_{(ℤ/2)²} (ℤ/2)³.* Status: elementary
(presentations of semidirect products with signed permutation modules; Karrass–Pietrowski–Solitar for virtual
freeness); no published treatment of this presentation known to me.

**469-2 — scan 469 — unproved claim — keep, verified.** With ε'_i = τε_i and τ commuting with ε_i: ε'_i² = (τε_i)²,
(τε'_i)² = ε_i², (ε'_0ε'_1)^{2g} = (ε_0ε_1)^{2g}, (τ'(ε'_0ε'_1)^g)² = (τ'(ε_0ε_1)^g)², and (τ'ε_1)² becomes
(τ'(τε'_1))². So (52bis) is a Tietze transform of (52), "les mêmes relations sauf la dernière de la deuxième ligne",
and equally incomplete.

**469-3 — scan 469 — unpursued implication — keep.** The torus analogy is developed on scan 470; see 470-3 and the
second-pass note C-3.

**469-4 — scan 469 — own idea (first pass) — kept, superseded by 469-1.** The g = 2 test was right; it generalises to
every g ≥ 2.

**470-1 — scan 470 — conjecture — corrected (reading).** "on a vraiment envie d'en avoir (?) une caractérisation
intrinsèque dans 𝒯_g — ou dans 𝒮_g (?)": the second group letter is unresolved (S, G or C; witnesses S_g). The question
itself is open-ended; 470-3 shows the first candidate characterisation fails.

**470-2 — scan 470 — unproved claim — keep.** Realised by homeomorphisms supported in the tubes, ℋ fixes V_0 pointwise,
hence acts on π_1(X_g, pole) by genuine (based) automorphisms; correct.

**470-3 — scan 470 — conjecture — corrected: false as stated. develop: yes (variant).** "Ce sont peut-être les
sous-groupes abéliens-libres maximaux" fails in 𝒯_g for g ≥ 2: V_0 is a sphere with 2g ≥ 4 holes and carries 2g − 3
disjoint essential non-peripheral curves, which with the g tube cores form a pants decomposition; its 3g − 3 twists
generate ℤ^{3g−3} ⊋ ℋ (3g − 3 is the maximal rank: Birman–Lubotzky–McCarthy 1983). Even among subgroups inverted by τ_g,
ℋ is not maximal (a τ_g-invariant curve in V_0 separating the holes into two antipodal halves adds a twist). Statement
to attack: *for a fixed-point-free anti-involution τ of X_g (g ≥ 3), the maximal rank of a free abelian subgroup
A ⊂ Mod^±(X_g) with τaτ^{-1} = a^{-1} for all a ∈ A is 2g − 1.* Status: lower bound 2g − 1 from the lifts of g + 1
disjoint one-sided curves of the quotient N_{g+1} plus one inverted product T_cT_{τc} per τ-orbit of a pants decomposition
of the two lifted copies of S_{0,g+1} (my construction; for g = 2 it gives 3 = 3g − 3); the upper bound is open to my
knowledge.

**470-4 — scan 470 — question — corrected: answered in substance.** "On aimerait étudier le normalisateur — est-ce
exactement ce qui provient des autom de X_g − ⋃T̊_i ≃ V_0 ?" The normaliser of the twist group of a multicurve C is the
stabiliser of C (fT_cf^{-1} = T_{f(c)}, and a twist T_d lies in ⟨T_C⟩ only if d ∈ C), and the stabiliser of the cut
system maps, with kernel ℋ, onto the mapping classes of V_0 that permute the 2g boundary circles compatibly with their
pairing into tubes (cutting homomorphism; cf. Farb–Margalit, *Primer*, ch. 3). So: yes, modulo ℋ and with the pairing
condition on the boundary circles.

**470-5 — scan 470 — conjecture (analogy) — corrected (reading), keep.** "Les SL(2,ℤ) associés aux 'lanières' à travers
le tube T_j jouent-ils un rôle analogue à celui des groupes SL(2,K) ou GP(1,k) 'de rang 1' … ? Si Jean ne 'mord' …"
(one tube; "ne"). No precise statement is posed; the analogy belongs with Harvey's curve complex as an analogue of the
Tits building (1981) and its later development (Ivanov); see C-3.

**470-6 — scan 470 — own idea (first pass) — kept, settled.** The essential curve in V_0 exists for g ≥ 2 and its twist
is independent of ℋ; this is the refutation in 470-3.

**470-7 — scan 470 — own idea (first pass) — keep, refined.** Based formulas at a pole hold for the subgroup fixing the
poles: ℋ and the rotations μ_{2g}; ε_0, ε_1 (half-turns about equatorial axes) and τ_g exchange the poles and need a
connecting path.

**470-8 — scan 470 — own idea (first pass) — keep.** Homological actions of the lanière groups: see C-3, where the
symplectic image changes the analogy.

## B. Notes on cancelled material

**[2nd pass] B-1 — scan 462 — unpursued implication (cancelled).** The cancelled paragraph after "ou aussi
ρ_{I'}^{-1}τ = τρ_{I'}" finds 𝒢 "trop petit" to conjugate all τρ and proposes, "d'une part en introduisant des groupes
de symétries supplémentaires, d'autre part en complétant chaque T_j par une configuration plus" [grande]: the two moves
carried out on scans 463–468 (the dihedral symmetries; the lanières). The cancelled margin computes
(τρ)(τρ')(τρ)^{-1} = τρ²ρ'^{-1}, so τρ' ~ τρ'' as soon as ρ² = ρ'ρ'', which is the criterion of scan 463.

## C. Second-pass notes

**[2nd pass] C-1 — scans 461–463 — own idea.** The 2^g ℋ-classes and the g+1 Aut(X_g)-classes of the anti-involutions
τρ are linked by the bracelet count of 463-R4; a natural next step is to name, for g = 4, a mapping class of X_g
conjugating τ_{{0,1}} to τ_{{0,2}} (it must move the cut system, e.g. a handle exchange in the "panachée" arrangement).
develop: no.

**[2nd pass] C-2 — scan 469 — own idea.** The corrected presentation of 469-1 has generators ε_0, ε_1, τ, τ' and
4 + ⌊g/2⌋ relation types; written with ε'_0, ε'_1 as in (52bis) all four generators are anti-involutions and the
commutation relations become [τ'τ, (ε'_0ε'_1)^k τ'τ (ε'_0ε'_1)^{-k}] = 1, since ε'_0ε'_1 = ε_0ε_1. develop: no (part of
469-1).

**[2nd pass] C-3 — scans 469–470 — unpursued implication.** Under H_1, each ρ_j maps to the transvection
v ↦ v + ⟨v, s_j⟩s_j, so ℋ maps to commuting unipotent elements in the unipotent radical of the Siegel parabolic of the
Lagrangian spanned by the tube cores, not to a torus of Sp(2g,ℤ). In the dictionary of Harvey and Ivanov, stabilisers
of multicurves play the role of parabolic subgroups and twist groups that of (centres of) unipotent radicals; the
"maximal torus" picture fits the pants twist groups ℤ^{3g−3}, whose stabiliser modulo the twists is finite, better than
ℋ, whose normaliser modulo ℋ (470-4) is infinite. The lanière groups B_3 → SL(2,ℤ) then look like root SL_2's attached
to the parabolic of the cut system. develop: no (interpretive; no single statement to prove).

**[2nd pass] C-4 — scan 465 — remark.** The ink's "polygone à 2μ côtés" is a slip for 2g sides (the g diagonals of the
regular 2g-gon with vertices μ_{2g}); no mathematical consequence.
