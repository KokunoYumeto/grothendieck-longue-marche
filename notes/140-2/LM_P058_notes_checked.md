# LM_P058 (scans 571–575): research notes checked against the corrected text

Each first-pass research note (R1–R20, from `answers/unzipped/LM_P058/LM_P058_notes.md`, section 5) is checked against `LM_P058_checked.tex` and kept, corrected or dropped, with a reason. Quotations follow the corrected transcription. R16–R19 remain the first-pass model's own ideas. Notes added in this pass are labelled "second pass (own)". The first pass's table of doubts and list of abbreviations are superseded by `LM_P058_changes.md`.

These pages (ms pp. 290–292) close §37 of the author's later table of contents, "Modules des courbes elliptiques via Legendre, ou M1,1[2]′ ≃ U0,3 = M0,4" (from ms p. 272). The table puts the start of §38, "Détermination de π0,3 ≃ S+0,3", at ms p. 291. No section number is visible on these scans; the "Complément sur le rapport anharmonique" begins on the unnumbered scan 574.

## First-pass notes

**R1. Scans 571–572, (74)–(75). Unproved claim. Corrected.**
"Sauf erreur, ces groupes sont resp. les groupes $A_4$ du tétraèdre orienté, et celui $A_5$ de l'icosaèdre orienté", followed by table (75). The orders in (74) are right, with GP(1, F_q) = PGL(2, F_q), the homography group of order q(q²−1); Sl(2,F_3)/±1 ≅ A_4, Sl(2,F_5)/±1 ≅ A_5 and GP(1,F_3) ≅ 𝔖_4 hold. *Reason:* the inserted line now reads "SΓ'_4 ≃ A_4" (subscript settled), which conflicts with (75); see S1, and S2 for "GP(1,F_5) ≃ groupe du biicosaèdre".

**R2. Scan 571. Unproved claim. Kept, with a check.**
"Si je me rappelle bien, les cas n=2,3,4,5 épuisent les cas de courbes modulaires congruentielles $M_{1,1}[n]$ qui soient rationnelles." The recollection is right: for n ≥ 3 the compactified curve has genus 1 + μ_n(n−6)/(12n), with μ_n = |Sl(2,Z/n)/±1| (12, 24, 60 for n = 3, 4, 5). This is 0 for n = 3, 4, 5 and at least 1 for n ≥ 6; level 2 is the λ-line. *Reason:* reading unchanged; the claim is classical but not proved on the page.

**R3. Scan 571. Unproved claim. Corrected (quotation).**
"il était clair a priori, par l'isom entre $\mathcal T'_{1,1}$ et le "groupe cartographique triangula- orienté" $\pi'_{0,3}$, qu'on devait retrouver tous les polyèdres réguliers finis à faces des triangles de cette façon, mais non pas que ce soit avec des sous-groupes de congruence(s), très exactement." The contrast is between existence (each such polyhedron is a quotient of the triangle group) and the fact that the kernels are exactly principal congruence subgroups. *Reason:* the ink has "triangula-", broken off at the line end, and a lowercase π; the substance stands.

**R4. Scans 571 (margin) and 573, (76). Implication not pursued. Corrected.**
The margin reads "sauf un, à "arêtes repliées" -- celui de la figure (76), cf plus bas…". The exception is the map of case b) (one vertex, three folded edges, one triangle). It is the quotient of the tetrahedral curve $M_{1,1}[3]$ by the normal subgroup V_4 of A_4, not one of the curves $M_{1,1}[n]$. *Reason:* the margin reading is settled, and 572–573 identify the exception.

**R5. Scan 572, quotients a)–c) and d). Unproved claim. Corrected.**
"b) Cas $A_4$ : le quotient $\mathbb Z/3\mathbb Z=C_3$ (via $\mathfrak S_4\to\mathfrak S_3$, induisant $A_4\to C_3$)". The list is complete: the proper nontrivial normal subgroups are A_3 in 𝔖_3, V_4 in A_4, V_4 and A_4 in 𝔖_4, none in A_5, giving ±1, C_3, 𝔖_3 and ±1. The 𝔖_3-quotient in c) is reduction from level 4 to level 2, i.e. the level-2 curve of the first row of (75); its ±1-quotient is case a). *Reason:* the subscript 4 is now settled (the first pass left 2|4 open), so the written map is the expected one.

**R6. Scan 572, case a). Unproved claim. Corrected, with a check.**
"le rev. quadratique de $Y=\mathbb P^1(\mathbb C)-\{0,1,\infty\}$, qui est non ramifié en ∞ (car l'indice de ramification doit diviser 2 et 3), qui correspond donc au rev. $y=\sqrt{x(x-1)}$". The argument fixes the coordinate: ∞ is the point of order 3, 1 the point of order 2 (case b), 0 the cusp. Then y² = x(x−1), branched at 0 and 1 only, gives one vertex of index 2 over 0, one ordinary edge over 1 and two monogons over ∞: the map of type (2,1) drawn on the page. *Reason:* the first pass asked for the branch-point conventions; the text itself fixes them, and the check confirms the description (the struck radical beside it is not used).

**R7. Scans 572–573, case b) and (76). Unproved claim. Corrected, with a check.**
"Le cas b) est le rev. cyclique d'ordre 3 : ramifié seulement en 0 et en ∞ … donc carte régulière sphérique de type (3,3), avec des arêtes qui sont des boucles repliées … 1 seul sommet, trois arêtes repliées qui en sortent, une face triangulaires." With the coordinate of R6 the cover is y³ = x. It has one vertex of index 3 over 0, one face of index 3 over ∞, and three unramified points over 1, i.e. three folded edges; Riemann–Hurwitz gives genus 0. *Reason:* "triangulaires" (a plural ending after "une face") is what the ink has; mathematically there is one triangular face.

**R8. Scan 573. Conjecture (expected necessary condition). Corrected (quotation).**
"il faudrait que le groupe de Galois-Poincaré du rev. soit multiple de 12 (mult. de 4 et de 6 ?!), pour que la courbe modulaire ait une chance d'être rigidifiante." A natural reading: the stabilisers in Sl(2,Z) of the points with j = 1728 and j = 0 are cyclic of orders 4 and 6. A rigidifying cover must keep them injective in its Galois group, whose order is then divisible by lcm(4,6) = 12. *Reason:* "?!" is now settled; the explanation is an interpretation, not stated on the page.

**R9. Scan 573. Conjecture (research question). Kept.**
"d'expliciter la relation entre les points des courbes rationnelles correspondantes, et entre courbes elliptiques à rigidifications de Jacobi, d'échelon respectivement 3,4,5." *Reason:* reading unchanged; the inserted "courbes elliptiques à" is confirmed.

**R10. Scan 573. Expectation about existing work. Kept, with a lead.**
"Et il y a sûrement des choses précises dans Klein". The obvious places to look are Klein's *Vorlesungen über das Ikosaeder* (1884) and Klein–Fricke, *Vorlesungen über die Theorie der elliptischen Modulfunctionen* (1890–92), which treat levels 3, 4, 5 through the tetrahedral, octahedral and icosahedral equations. *Reason:* reading unchanged; the page names no work, and the lead is this pass's suggestion.

**R11. Scan 573. Conjecture (desired extension). Corrected.**
"on aimerait faire des choses un peu plus fines, qui soient valables simultanément en toutes caractéristiques i.e. sur des schémas de base généraux." *Reason:* the first pass's "quiconque|quelconque" was a misreading. The ink has "généraux", as the witnesses print. Only the number of "toutes caractéristiques" stays open; the aim (arbitrary bases, all characteristics at once) is clear.

**R12. Scans 573–574. Conjecture (suggested connection). Corrected.**
"Ce souci semble intimement lié à la question des opérations de $\Gamma_{\mathbb Q}$ sur les classes d'isomorphie des cartes, et plus particulièrement des cartes sphériques régulières. C'est assez extraordinaire que Jean Malgoire, depuis trois ans que la question est là, n'y ait pas encore touché -- Dieu sait qu'elle est juteuse !" *Reason:* the group is Γ_Q, a Γ with a doubled stem as in "IΓQ" in the author's TOC, not Π. "intimement" is confirmed against the witnesses' "intuitivement", and the name is legible. See S6.

**R13. Scan 574. Unproved claim. Kept, with a check.**
The construction of "la section correspondante λ de $U_{0,3}$" from local coefficients "avec $ad-bc$ inversible". Independence of the choice of (a,b,c,d) and gluing are not discussed, but the result (79) involves no choice, which settles both where the $x_i$ are finite. At ∞ one needs homogeneous coordinates (R16). *Reason:* reading unchanged; S5 shows why "sections partout distinctes" is exactly what is needed.

**R14. Scan 575. Unproved claim. Kept, with a check.**
"elle est caractérisé par les deux propriétés : a) invariance … et b) $f(0,1,\infty,x_4)=x_4$ (avec un grain de sel …". Uniqueness takes one line: for distinct x_1, x_2, x_3 take the homography u with u(x_1,x_2,x_3) = (0,1,∞); then f(x) = f(0,1,∞,u x_4) = u(x_4) = λ(x). *Reason:* reading unchanged (the ink has "caractérisé"); the "grain de sel" concerns the meaning of f at ∞.

**R15. Scan 575, diagram and (80). Unproved claim. Kept, with a check.**
The kernel of 𝔖_4 → 𝔖_3 is the Klein group V_4, which fixes λ. For example, (12)(34) sends λ to (x_3−x_2)(x_1−x_4)/((x_1−x_2)(x_3−x_4)) = λ. The six φ_σ are λ, 1/λ, 1−λ, 1/(1−λ), λ/(λ−1), (λ−1)/λ. *Reason:* reading unchanged; S7 checks the inverse-index convention.

**R16. Scans 574–575. Own idea (first pass). Kept.**
Homogeneous coordinates for the cross-ratio, to cover sections that meet ∞ and to glue. *Reason:* still apt; the affine computation on 574 leaves exactly this aside (R13).

**R17. Scan 575 with 573. Own idea (first pass). Kept, with a remark.**
Small characteristic. In characteristic 3 the 𝔖_3-orbit {−1, 2, 1/2} and the roots of λ²−λ+1 both collapse to λ = −1. In characteristic 2 the first orbit leaves $U_{0,3}$ and the second is {ω, ω²} ⊂ F_4: these are the coincidences j = 0 = 1728 in characteristics 3 and 2. *Reason:* this confirms where the first-pass model expected exceptional behaviour.

**R18. Scan 573. Own idea (first pass). Kept.**
State the level-3, 4, 5 correspondences as comparisons of moduli functors. *Reason:* unaffected by the corrections; R11 now reads "sur des schémas de base généraux", the setting the idea proposes.

**R19. Scans 572–573. Own idea (first pass). Kept, with a remark.**
Test the rigidification criterion on the small quotients. The test is immediate: the covers a) and b) have Galois groups of orders 2 and 3, not multiples of 12, so by the author's criterion they cannot rigidify. This is what "Ces cas semblent donc nettement moins intéressants" concludes. *Reason:* R8 now gives a reading of "4 et 6".

**R20. Scans 574–575. Implication not pursued. Kept, with a remark.**
The quotient of the λ-line by the 𝔖_3 of (80) is the j-line, j = 2⁸(λ²−λ+1)³/(λ²(λ−1)²). This is the Legendre picture "M1,1[2]′ ≃ U0,3" of §37, so the Complément gives its coordinates over a general base. *Reason:* reading unchanged; the identification is classical and not made on these pages.

## Second-pass notes (own)

**S1. Scan 571, (74). Slip (second pass, own).**
"en fait, on doit avoir $S\Gamma'_4\simeq A_4$": Sl(2,Z/4)/±1 has order 24, and (75) itself pairs n = 4 with 𝔖_4. The group of order 12 isomorphic to A_4 is $S\Gamma'_3$ of the first row, of index 2 in GP(1,F_3) ≃ 𝔖_4, as the next sentence says. The line presumably means $S\Gamma'_3\simeq A_4$.

**S2. Scan 571, (74). Claim that fails as written (second pass, own).**
"GP(1,F_5) (ordre 120) ≃ groupe du biicosaèdre": PGL(2,F_5), acting on the six points of P¹(F_5), is isomorphic to 𝔖_5, whose centre is trivial. The binary icosahedral group Sl(2,F_5) and the full icosahedral group A_5 × Z/2 both have centres of order 2. Under any usual meaning of "groupe du biicosaèdre" the isomorphism therefore fails; the underlined "bi" may mark the author's own doubt.

**S3. Scan 572. Claim that needs a qualification (second pass, own).**
"Comme autres courbes modulaires (pas congruentielles) rationnelles galoisiennes sur $\widetilde M_{1,1}$": the quotients of $M_{1,1}[n]$ by normal subgroups of $S\Gamma'_n$ correspond to subgroups of Sl(2,Z) containing Γ(n). These are congruence subgroups in the usual sense. "pas congruentielles" can only mean "not one of the curves $M_{1,1}[n]$".

**S4. Scans 572–573. Implication not pursued (second pass, own).**
With the coordinate of R6 (0 the cusp, 1 the point of order 2, ∞ the point of order 3), vertices lie over 0, edges over 1 and faces over ∞. Then $M_{1,1}[n]$ for n = 3, 4, 5 is a triangulation with n triangles at each vertex (tetrahedron, octahedron, icosahedron, as in (75)). The folded edges of (76) are the points over 1 where the cover is unramified. This dictionary is used but not stated on these pages.

**S5. Scan 574. Check (second pass, own).**
From the solved system, ad − bc = ac(x_1−x_3) = a²(x_2−x_1)(x_1−x_3)/(x_2−x_3), and λ − 1 = (x_4−x_2)(x_1−x_3)/((x_2−x_1)(x_4−x_3)). So for invertible a, the inserted "ad−bc inversible" amounts to the invertibility of the differences of x_1, x_2, x_3. λ avoids 0, 1, ∞ exactly when x_4 is disjoint from the other three, which is why the insertion asks for sections "partout distinctes" and why λ is a section of $U_{0,3}$.

**S6. Scans 573–575. Own idea (second pass; confidence medium).**
The 𝔖_3 of (80) acts on P¹ by homographies with integer coefficients. A_4, 𝔖_4 and A_5 are not subgroups of PGL_2(R), whose finite subgroups are cyclic or dihedral. Over R they act only on the form of P¹ without real points (the conic x²+y²+z² = 0, with automorphism group SO(3)). So for n = 3, 4, 5 any description over Q of a regular map together with its automorphisms needs twisted forms or larger fields, which may be one source of the arithmetic interest the author sees in the Γ_Q question.

**S7. Scan 575, (80). Check (second pass, own).**
Write (σx)_i = x_{σ⁻¹i}; then σ(τx) = (στ)x, so (80) gives φ_{στ} = φ_σ ∘ φ_τ. The inverse indices are what make σ ↦ φ_σ a homomorphism; indices x_{σi} would give an anti-homomorphism.
