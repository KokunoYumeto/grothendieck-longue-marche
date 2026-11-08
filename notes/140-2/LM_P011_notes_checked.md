# LM_P011 (scans 101–110): research notes, checked against the corrected transcription

Each first-pass note (R01–R21) is checked against `LM_P011_checked.tex` and kept, corrected or dropped, with the
reason. Notes added in the second pass are labelled S01–S07 ("second pass, own"). Kinds: conjecture/question, claim
without proof, implication not pursued, own idea. Literature mentioned below is a lead for later reading; it was
not checked against the corpus in this pass.

## First-pass notes

**R01 — scan 101 — claim without proof — KEEP, quote corrected.**
The author expects that full faithfulness of the functor "ne fasse pas de difficultés essentielles" (not "ne fera
pas"), using the case Γ = 1. The margin note beside these lines, misread in the first pass, says "Ça vaudrait
drôlement le coup de le faire très soigneusement…": the author himself marks this proof as worth writing out with
care. No proof is given here.

**R02 — scan 101 — implication not pursued — KEEP, reading corrected.**
The margin reads "Attention au cas S = ∅ dans la définition des structures : … (donnée de H²(π,Z) ≃^κ T); il faut
bien sûr tenir compte lors de l'action de Σ sur H²(π,Z) (via son action ext. sur π) et sur T (via χ) et exiger la
compatibilité", with some words still doubtful. With the corrected source category ("X surface compacte T
orientée"), the orientation datum lives in T, so the required compatibility is between the action on H²(π,Z) and
the χ-twisted action on T. The precise equivariance condition is not written out.

**R03 — scans 101–102 — conjecture/question — KEEP.**
Essential surjectivity is called "un problème ouvert sur lequel les gens sèchent": whether every finite subgroup of
the extended Teichmüller group is realized on (X₀,S₀), "de façon essentiellement unique". The question has an
existence part (lifting to A) and a uniqueness part (conjugacy by A⁰, "isotopie au sens strict"). See S02 for the
later literature.

**R04 — scan 102 — claim without proof — KEEP, quote corrected.**
"A⁰ est contractile, dans les cas anabéliens" (plural in the ink). The topology on the homeomorphism or
diffeomorphism group and the treatment of the marked points are not specified, and no proof is given. See S02.

**R05 — scan 102 — own idea (first pass) — KEEP.**
Separating the lifting problem (a splitting problem for the preimage extension) from the conjugacy problem
(simultaneous conjugacy of homomorphisms) is sound and matches the two clauses of the text.

**R06 — scan 103 — implication not pursued — KEEP.**
The aside distinguishes T^{(⊗−1)} ≃ H²(π,Z) from the "iso. canonique T^{⊗−1} ≃ T i.e. T^{⊗2} ≃ Z"; which data make
this identification canonical is not said, and its compatibility with the later T(K̄) is not discussed.

**R07 — scan 103 — conjecture/reconstruction question — KEEP.**
The programme is to recover the diagram Π_{D*,Γ} → Π_{U,Γ} → Π_{e,Γ} "à équivalence définie à isom unique près"
from the lacet data. The pages that follow carry it out for Π_{U,Γ} and Π_{D*}, and stop at the equivariant step
(R17).

**R08 — scan 104 — own idea (first pass) — KEEP, context corrected.**
Checking i_{u'',u'}∘i_{u',u} = i_{u'',u} by multiplying the unique conjugating elements is the right verification
of the "syst. transitif d'iso". In the corrected text the restriction functor u* "définit donc, avec u_* =
(u⁻¹)*, une équivalence des Topos B_{π'} → B_π" (labelled u_•), so the coherence has to be stated for these
equivalences.

**R09 — scan 105 — claim without proof (with a proposed route) — KEEP.**
"Comme Centr(π) = 1, l'opération de Σ sur π définit une ext. ℰ de Σ par π": the pull-back of Aut(π) → Out(π)
along Σ → Out(π) gives it, using Inn(π) ≅ π. In the profinite case continuity must be checked.

**R10 — scans 105–106 — question / incompletely checked claim — KEEP, notation corrected.**
The subscripts are Γ in the ink: B_{π,Γ} = B_ℰ, B_{π,Γ} → B_Γ, Θ_Γ : B_{π',Γ} → B_{π,Γ}, u_Γ, u'_Γ = int_ℰ(g)∘u_Γ.
The extension map ℰ' → ℰ is said to lie "au-dessus(?) de u" (the word is still doubtful). Compatibility with
composition of exterior homomorphisms is not written out.

**R11 — scan 105 — own idea (first pass) — KEEP, scope corrected.**
The corrected margin restricts the remark to anabelian loop groups: "marche pour les [groupes à] lacets
anabéliens, et les hom. de tels dont l'image soit d'indice fini… (car le centralisateur dans un tel groupe π d'un
sous-groupe d'indice fini est encore réduit à e)". The infinite dihedral group (centre trivial, but ⟨r⟩ of index 2
centralizes itself) shows why that restriction is needed; it is not a counterexample to the stated remark.

**R12 — scan 106 — own idea (first pass) — CORRECT.**
The margin says only "L'injectivité dans le cas qui nous intéresse résulte de l'hyp. anabélienne"; the
"(infinité des lacets)" read by the first pass is "(initiale des "lacets")", written under Λ and explaining the
letter. The substantive point stands: Aut(κ) = Centr_π(κ) = κ(T) uses self-centralization, and the identification
with T uses injectivity.

**R13 — scan 107 — own idea (first pass) — KEEP.**
With f_π = id, T = Z and κ injective and self-centralizing, Im(κ∘d) is centralized by κ(Z), so the hypothesis
"κ ∈ Λ ⇒ Centr_π κ = Im κ" forces d = ±1. The hypothesis is therefore a real restriction on d. See S05 for what this
suggests about the formula.

**R14 — scans 107–108 — own idea (first pass) — KEEP, ink confirmed.**
The ink confirms the readings the first pass left open: on scan 107 "u∘κ∘(d.id_T)" with an unprimed κ (the object
is κ'); on scan 108 the prose "u_Λ : Π_Λ → Π_{Λ'}" against the square Π_{Λ'} → Π_Λ, and "Λ_i = Λ_{i'}∘Θ∘(d_{i'}.id)"
with the prime on the index only. As written the last composition does not type-check (Θ : π' → π after a map into
π'); these are slips to be read, not silently repaired.

**R15 — scans 108–109 — claim without proof — KEEP, quote corrected.**
"si I → Homext(T,π) injectif, ces conditions montrent (not "impliquent") que τ est déterminé par Θ, et si de plus Z
opère fidèlement dans T, p.ex. si T ≃ Z, alors (d_{i'}) est également unique". Uniqueness has to be checked on
exterior classes, i.e. modulo conjugation (R16, S06).

**R16 — scans 108–109 — own idea (first pass) — KEEP.**
In the infinite dihedral group, conjugation by s identifies κ with κ∘(−id), so d = 1 and d = −1 give the same exterior
class although Z acts faithfully on T: faithfulness alone does not give uniqueness of d. S06 explains why this does
not happen for anabelian surface groups.

**R17 — scan 109 — claim without proof — KEEP, quote corrected.**
"Supposons maintenant (ouf !) que Σ opère sur groupes extérieurs à lacets… Je déclare forfait — il est évident que
tout marche bien !": the equivariant version of the whole construction is asserted without proof.

**R18 — scan 109 — conjecture/expectation — CORRECT.**
Over a field of finite type over F_p one should restrict to fundamental groups "premiers à p", "à cel' près nos
développements pourraient se faire quand même": the author expects the developments to carry over unchanged to
the prime-to-p quotients (the first pass left this clause unread). Which quotient, and whether injectivity and
the centralizer conditions survive in it, is not discussed.

**R19 — scan 110 — implication not pursued — KEEP.**
Σ is "remplacé par un conjugué, quand on change Ū₀"; the compatible change of the exterior action, of the lacet
data and of the topos diagram is not checked.

**R20 — scan 110 — claim without proof — CORRECT.**
The vertical sign under S(K̄) is ≃ turned through 90°, so the text asserts S(K̄) ≃ S₀(K̄) ∧_Σ Γ, with I = S₀(K̄) ⊂
S(K̄) "vide ssi(?) S = ∅". The claim follows from the transitivity of Γ on the components of X̄ (X connected) and
the disjointness of the components, but no argument is given. The IUT witness prints "S ≠ ∅", which is wrong; the
ink and CSG have "=".

**R21 — scan 110 — own idea (first pass) — KEEP.**
The "T(K̄)-structure à lacets, avec(?) comme ens d'indices I" carries a Σ-action on T(K̄) through the cyclotomic
character as well as a permutation of I; both have to enter the equivariance condition on each lacet map.

## Second-pass notes (own)

**S01 — scan 101 — own idea (gap in a stated condition).**
The source condition "si X₀ ≃ S², on ait card S₀ ≥ 3" does not exclude a torus component with S₀ = ∅, whose π = Z²
is commutative, while the target requires "π non commutatif"; the gloss "(i.e. π ≠ 0, Z)" also omits Z². The
anabelian condition 2g − 2 + ν > 0 excludes exactly the sphere with at most two points and the unpunctured torus.
Unless the torus is excluded on an earlier page, the stated source condition is incomplete. Confidence: high
(elementary).

**S02 — scans 101–102 — status lead for R03/R04.**
The existence part of R03 is the Nielsen realization problem, solved for finite subgroups of the mapping class
group by Kerckhoff (Ann. of Math. 117, 1983), after this text; whether that covers the extended group with marked
points and the uniqueness up to A⁰ still has to be checked. For R04, contractibility of the identity component is
classically due to Earle–Eells (1969, diffeomorphisms) and Hamstrom (1966, homeomorphisms); read the exact
hypotheses before citing either.

**S03 — scans 103 and 105 — implication not pursued.**
The corrected scan 103 makes the functoriality of B_π explicit: "de façon "fonctorielle" (pour Iso)", i.e. for
conjugacy classes of isomorphisms. The NB on scan 105 then extends the construction to every exterior homomorphism
with trivial centralizer, and the margin to finite-index homomorphisms between anabelian loop groups. The text
does not check that these extensions compose.

**S04 — scan 105 — own check of a claim without proof.**
With the corrected "(ce qui pour un épi se réduit à l'hyp Centr(π) = 1)" the parenthesis is immediate: if u is
surjective, the centralizer of u(π') is the centre of π. The first-pass "iso" would have stated a special case only.

**S05 — scans 107–108 — own idea.**
For a finite-index inclusion f_π : π' → π of surface groups (a covering ramified with index e at a puncture), one
has f_π∘κ' ~ κ∘(e·id_T) with κ self-centralizing. Under the stated hypothesis "κ ∈ Λ ⇒ Centr_π κ = Im κ", the
formula Λ = f_π∘Λ'∘(d.id_T) then forces e·d = ±1, which excludes ramification. The geometric situation suggests the
intended relation is f_π∘Λ' = Λ∘(d.id_T) (and on scan 108, Θ∘Λ'_{i'} = Λ_i∘(d_{i'}.id)). This is a proposed reading
of the intended mathematics, not a correction of the ink. Confidence: medium.

**S06 — scans 108–109 — own idea.**
In a torsion-free hyperbolic group, and so in a discrete anabelian surface group, no nontrivial element is
conjugate to its inverse: if hgh⁻¹ = g⁻¹, then h lies in the maximal elementary subgroup of g, which is infinite
cyclic, so h commutes with g and g² = 1. So d = ±1 are distinguished there, unlike in the dihedral test of R16. The
profinite case needs the corresponding statement for the normalizers of cuspidal inertia subgroups, which should
be looked up rather than assumed.

**S07 — scan 110 — claim without proof.**
"Alors Σ opère sur le schéma Ū₀ (or X̄₀), donc opère extérieurement sur son π₁": the passage from an action on the
scheme to an exterior action on the (profinite) fundamental group is stated without argument. The package ends
here; according to the CSG draft, the next page asserts the compatibility of this action with the T(K̄)-lacet
structure and with χ|Σ, which should be checked on that page's scan.
