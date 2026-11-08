# LM_P017 (scans 161–170): research notes checked against the corrected text

Each first-pass note (R01–R23, from `answers/unzipped/LM_P017/LM_P017_notes.md`) is checked against `LM_P017_checked.tex`. Each is kept, corrected or dropped, with the reason. Notes S01–S07 are the second pass's own and are labelled as such. The kinds are:
- conjecture or question: an open question or expectation stated by Grothendieck;
- unproved claim: asserted without proof on these pages;
- unpursued implication;
- own idea.

## First-pass notes

**R01 — scan 161 — unproved claim, cancelled — kept, with a correction.** A boxed and struck passage starts ", donnons-nous un sous topos (néc^t. ouvert) B_{D₁\*} de B_{D\*}". It sets B_{D\*} ≃ B_{D₀\*} ⊔ B_{D₁\*}, gives the analogous decomposition of B_D, defines B_{π₀(D\*)} = B_S and forms a "somme amalgamée" B_U′ over B_{D₁\*}. This is an abandoned first attempt at a partial filling. The same idea returns, uncancelled, on scans 169–170, where B_{D₀\*} is "un sommande direct".
*Reason:* the reading is confirmed (apart from the opening comma), and the link to scans 169–170 is added.

**R02 — scans 161–162 — unproved claim (kind changed) — corrected.** The corrected text is negative: "dans ce cas S_ét [or X_ét, overwritten] ne peut se reconstituer à partir de B_{D\*} comme B_I avec I = π₀(B_{D\*}), il faut tenir compte des corps résiduels k(s) … i.e. des groupes de Galois Gal(k̄(s)/k(s))". The first pass read "on peut". This is the stated reason for the new starting datum B_U ← B_{D\*} → B_S, with σ inducing an isomorphism on Π₀ and surjective on Hom. No proof is given. For S_ét the point is that ∐_s B_{Gal(k(s)ˢ/k(s))} is a discrete topos B_I only when the residue fields are separably closed.
*Reason:* the negation is restored, and the note now states the claim rather than an open comparison.

**R03 — scans 162–163 — unproved claim — corrected.** The choices are:
- universal coverings D̃ᵢ\* of the components Dᵢ\*;
- a universal covering Ũ of B_U;
- isomorphisms ρ_!(D̃ᵢ\*) ≃ Ũ.

With these choices, and B_U connected, the situation "s'explicite par la donnée d'un groupe ℰ (ou Π) (=Aut Ũ), ℰᵢ (ou Πᵢ) (=Aut D̃ᵢ\*) (i∈I), Γᵢ (i∈I)", together with ρᵢ: ℰᵢ → ℰ and σᵢ: ℰᵢ → Γᵢ, σᵢ surjective. The group names are settled: the diagram labels are ℰᵢ and ℰ written over Πᵢ and Π, matching the insertions on scan 162. The text does not prove the equivalence between the topos datum and this group datum, or its dependence on the choices.
*Reason:* the letters are settled, and ρ_! (not ρ_{i!}) is confirmed.

**R04 — scan 163 — unpursued implication — kept, with a correction.** Over a base field: e = Spec K, B_e = the étale topos e_ét of e = B_Γ with Γ = Gal(K̄/K). The diagram (\*) is put into a square over B_e "avec donnée de commutativité pour le carré". The first pass's insertion "fét" is "e_ét". The text does not say whether the later gluings and amalgamations are to be formed over B_e.
*Reason:* the insertion is corrected; the implication stands.

**R05 — scans 163–164 — unproved claim — kept.** Gluing B_U and B_S along σ_\*ρ^\* gives "un topos mixte, qui n'est plus en général multigaloisien". It was formerly B_{X,U} and is renamed B_{X;S} "[pour rappeler qu'il s'agit de faisceaux sur X, mais n'ayant de singularités que sur S]". The construction and the failure of the multigaloisian property are asserted, and no criterion is given.
*Reason:* the content is unaffected. Only the renaming clause changes, to "et que \[je préfère\] maintenant noter", which stays doubtful.

**R06 — scan 164 — unpursued implication — kept.** The comparison α_X: σ^\*ψ^\* → ρ^\*φ^\* is "un morphisme de foncteurs sans plus", "pas un iso", and the arrow orientation is confirmed. A universal property for the glued topos must therefore allow a non-invertible 2-cell.
*Reason:* the reading is confirmed.

**R07 — scan 164 — unproved claim — kept, with a correction.** In the geometric model, B_X corresponds to sheaves on X that are "\[ess.\] loc. constants sur U". That is, on U they "proviennent par l'image inverse par U → B_{Π₁U} d'un faisceau sur B_{Π₁U}". B_{D;S} corresponds to sheaves on D = ∐ Spec(𝒪ᵢ = hensélisé …) that are locally constant on D\* = D − S. Then "avec l'hyp. de dim faite — en fait B_{D;S} ≃ D_ét (Dᵢ n'a que 2 pts, Dᵢ\* = {ηᵢ})". These identifications are not proved.
*Reason:* the inserted "par" is added and the "on a" read by the first pass is not in the ink. See also S03 on the name B_X here.

**R08 — scan 165 — unproved claim — corrected.** The canonical morphism B_{D\*} → B_{D;S} is φ_D, "et non ψ_Dσ". Geometrically, φ_D corresponds to the inclusion D\* ⊃ D∖S → D and ψ_D to S → D, "alors que σ ni ψ_Dσ ne correspondent en général à des morphismes de schémas". The margin says that the three topoi of the triangle are étale and that φ_D and ψ_D "correspondent à des morph. … mais non … de topos)". The row order is doubtful, and CSG has "à des morphismes de topos, mais non σ". The first pass's "inclusions de topos" is not in the ink. None of this is proved here.
*Reason:* the margin and the display are corrected.

**R09 — scan 166 — conjecture (qualified) — kept; reading settled.** "Sauf erreur les deux carrés sont [non seulement ess^t. comm. mais aussi] 2-cartésiens (dans la 2-cat. des topos)." This is to be checked as a 2-pullback statement for each square of (\*\*). The neighbouring warning that the triangle is "pas ess. commutatif" must stay in that formulation.
*Reason:* "ess^t." is settled; the rest is unchanged.

**R10 — scan 166 — unproved claim — corrected (notation).** Passing to the B_{Π₁} of the topoi gives "un topos B_X (= B_{Π₁B_{X;S}})" as an amalgamated sum, and "ce carré est bel et bien essentiellement commutatif". The Π₁ of the lower vertex is hatched out. Grothendieck renames B_{Π₁X} as B_X, as announced on scan 162 (see S02). The universal property, and which locally constant objects are meant, are not established here.
*Reason:* the notation is corrected; the claim is unchanged.

**R11 — scan 166 — unproved claim — kept; reading settled.** "un B_D, qui est cependant (par B_S → B_D) isom. (plutôt: équiv.) à B_S". In the ink, Grothendieck himself corrects isomorphism to equivalence. The equivalence induced by B_S → B_D is asserted, not proved.
*Reason:* "cependant" is settled.

**R12 — scan 167 — conjecture — corrected.** The morphism (\*\*) → (\*\*\*) is described "pour les flèches qui (ne) sont pas ess. des (semi-)identités, B_{D;S} → B_D et B_{X;S} → B_X". These two components "ont une nette tendance d'être acycliques i.e. d'induire des iso. sur la cohomologie (il faudrait voir … ce point)". The expectation therefore concerns exactly the two components that are not identities, and "acyclic" is defined by the "i.e.". CSG and IUT read "qui sont par essence des identités … ou à induire", which reverses the selection and weakens the definition.
*Reason:* the selection clause and the "i.e." are fixed on the ink, against both witnesses.

**R13 — scan 168 — unproved claim — corrected.** "Ici (\*\*\*\*) s'envoie dans le diagramme homologue (\*\*)". This induces isomorphisms of topoi for D\*, D, S. For U_ét → B_U and X_ét → X it induces morphisms "qui ont moins tendance d'être acycliques, mais qui le sont quand même dans des cas importants, rappelés dans une section antérieure…". These pages do not identify the earlier section.
*Reason:* "moins tendance" (not "moins de chances"), the singular "le diagramme homologue" and "s'envoie" (CSG: "s'insère") are corrected.

**R14 — scan 168 — unproved claim — kept.** The constructions of (\*\*) and (\*\*\*) are "purement formelles, et indépendantes de tte hypothèse". The formal existence of the glued and amalgamated topoi must be kept apart from the geometric identifications and the acyclicity expectation.
*Reason:* the reading is unchanged.

**R15 — scan 169 — unproved claim — corrected.** In the computational setting, B_X is the classifying topos B_{π_X}. Here π_X = π₁(X; X̃) is computed "comme quotient de π par le ss-groupe invariant engendré par les ρᵢ(Lᵢ), où Lᵢ = Ker σᵢ ⊂ ℰᵢ": a van Kampen statement for filling the holes. The letters are corrected: ℰᵢ and π (not Ξᵢ and Π), "ss-groupe", and ⊂. The object described is B_X (CSG: "BU"). The statement is not proved, and the closure question of R19 applies.
*Reason:* the letters are corrected.

**R16 — scans 169–170 — unpursued implication — corrected.** A "sommande direct" B_{D₀\*} of B_{D\*} (first pass: a "sous-monde/sous-ensemble ouvert") corresponds to a part I₀ ⊂ I. It gives the partial amalgamation of B_U and B_{S₀} under B_{D₀\*}, written "B_{U∪S₁} ← B_U". The filling is along S₀, and on scan 170 the object is B_{(U∪S₀)} with a brace U₁, where U₁ = X∖S₁ = U∪S₀. The S₁ on scan 169 is therefore probably a slip, kept as written. The family of partial fillings indexed by the subsets of I, with its transition maps, is not pursued.
*Reason:* "sommande direct" (a union of components, open and closed) is stronger than the first pass's "ouvert", and the index discrepancy is recorded.

**R17 — scan 170 — unproved claim — kept, with a correction.** The diagrams are a "hom de diagrammes cocartésiens" (CSG and IUT: "cartésiens"). The second amalgamation uses B_{D₁\*} → B_U → B_{U₁} and B_{D₁\*} → B_{S₁}. "Il est évident que celle-ci est can. équivalente à B_X", the full amalgamation; this is asserted, not proved. The sentence continues beyond this package.
*Reason:* "cocartésiens" is confirmed, and the composite is spelled out.

**R18 — scans 163–165 — own idea (first pass) — kept.** Test the gluing with sets, identity maps and a non-bijective connecting map, to see the role of a non-invertible comparison.
*Reason:* still apt, since α_X and α_D are confirmed as non-invertible.

**R19 — scan 169 — own idea (first pass) — kept.** Ask whether "ss-groupe invariant engendré" means algebraic or closed normal generation. In a profinite setting the closed normal subgroup is needed.
*Reason:* it applies directly to R15.

**R20 — scans 169–170 — own idea (first pass) — kept.** For J ⊂ I, take the quotient by the normal subgroup generated by the ρᵢ(Lᵢ), i ∈ J. This models the partial fillings and their transition maps.
*Reason:* it fits the corrected R16.

**R21 — scan 170 — own idea (first pass) — corrected.** Take a discrete toy model with π = F(a,b), two groups ℰᵢ = ℤ (first pass: "Ξᵢ") and trivial Γᵢ, so that Lᵢ = ℰᵢ. Filling one component kills a or b, and filling both kills both, in either order.
*Reason:* the group letter is corrected; the calculation stands.

**R22 — scans 167–168 — own idea (first pass) — kept.** Test acyclicity with declared coefficients and degrees, not only constant coefficients.
*Reason:* it now targets the two components named in R12.

**R23 — scans 167–168 — own idea (first pass) — kept.** Keep a ledger of scheme morphisms, topos morphisms and inverse-image functors to diagnose two things:
- the bottom arrow of (\*\*\*\*), which points from X_ét to U_ét;
- the target "X" in "X_ét → X" on scan 168.

*Reason:* both readings are confirmed on the images; see also S06.

## Second-pass notes (own)

**S01 — scan 161 — unproved claim (second pass).** This is the end of the marginal note begun on scan 160 ("une telle situation toposique décrit 2-fidèlement les situations topologiques (X,S) … pourvu qu'aucune composante irréductible de U ne soit ≃ S²"). Because these situations stay "très proches du langage et de l'intuition topologique", Grothendieck rates the toposic description above the "groupes à lacets" point of view, "qui correspond à l'appr. du calculatoire plutôt". The 2-faithfulness and its S² exception are asserted, not proved.

**S02 — scans 162, 166–170 — own idea, notation (second pass).** The warning "on écrit B_S, non B_D, qui aura un autre sens" (scan 162) is carried out on scans 166–170. B_D and B_X arise by hatching out the Π₁ in B_{Π₁D}, B_{Π₁X}, B_{Π₁(U∪S₀)}, B_{Π₁(U∪S)} and B_{Π₁U₁}, while B_{Π₁S}, B_{Π₁D\*}, B_{Π₁U} and B_{Π₁U₁} (scan 170, l. 2) are left as written. A reading edition should not restore the Π₁ silently, and should not confuse B_D and B_X with the glued B_{D;S} and B_{X;S}.

**S03 — scan 164 — own idea, possible slip (second pass).** "B_X correspond aux faisceaux sur X qui sont \[ess.\] loc. constants sur U (et sur S …)" describes the glued topos of the previous paragraph. Its parallel "et de m̄ B_{D;S} correspond aux faisceaux sur D" suggests that B_{X;S} is meant. On scans 166–170, B_X is the Π₁-topos instead (S02). The ink (an over-inked B with subscript X) and both witnesses read "B_X". This is recorded, not emended.

**S04 — scan 167 — question (second pass).** The ink and both witnesses read "le triangle sup. est bien ess. surjectif (c'est bien comme ça qu'on a défini σ, dans le cas géométrique!)". It contrasts with (\*\*), where the triangle "n'est pas ess. commutatif", and with the margin of (\*\*\*\*), "triangle sup. pas ess. comm.". This suggests that essential commutativity of the upper triangle of (\*\*\*) may be meant. On the other hand, σ was defined on scan 162 as surjective on Hom, which fits "surjectif". The two readings should be compared before the sentence is used.

**S05 — scan 167 — unproved claim (second pass).** The margin of (\*\*\*\*) states that in the étale diagram the upper triangle, D\*_ét → S_ét → D_ét against D\*_ét → D_ét, is "pas ess. comm." This is the étale counterpart of the warning beside (\*\*). No proof or comparison 2-cell is given.

**S06 — scan 168 — question (second pass).** "Toutes les flèches sauf D\*_ét → S_ét sont induites par des morphismes de topos": the ink (and both witnesses) reads "topos". But every arrow of a diagram of topoi is a morphism of topoi, and scan 165 says that σ does not come from a morphism of schemes. The intended contrast is probably with morphisms of schemes. This is recorded, not emended.

**S07 — scan 168 — unproved claim (second pass).** "La construction d'un B_X multigaloisien, comme somme amalgamée, peut être interprété comme la traduction (au niveau des groupoïdes fondamentaux) d'une opération de 'bouchage de trous'." The precise content would be that B_{Π₁}X is a 2-pushout of B_U ← B_{D\*} → B_S among multigaloisian topoi. This is a van Kampen theorem for filling punctures, whose group form is the quotient of R15. It is stated as an interpretation, without proof.
