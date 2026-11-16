## 4. Explicit editorial tests and links not made on these leaves

### NCTX-01 — A point tests the unrestricted finite-rank quotient sentence

**Source:** 90.pdf, scan 016, assertion 4; compare 010–012. **Kind:** own idea. **Confidence:** high for this counterexample to the literal unrestricted sentence, because it is a finite-dimensional image calculation. **Quote:** “tt O_X-G-module … quotient d'un loc. libre de t.f.” **Context search:** `90-equivariant|resolution|finite.rank|finite type`. **Comparison:** adds a scope test to RS H90-E, without deciding the full unseen finding.

Set S=X=Spec(k), take the trivial group and E=⊕_{n≥0}k. All hypotheses about finite-type modules on X hold, but every map k^r→E has image of dimension at most r and cannot be surjective. Thus the sentence on 016 needs a restriction such as finite type on E, or a different conclusion, in any mathematical restatement; the example does not contradict the finite-type claims on 010–012 and is not a novelty claim.

### NCTX-02 — A diagonal representation tests the withdrawn faithful-flatness claim

**Source:** 90.pdf, scans 006 and 014. **Kind:** own idea. **Confidence:** high for the explicit example; both the representation and its proper image are visible algebraically. **Quote:** “fidèle” versus cancelled “fidèlement plat”. **Context search:** `90-saturated|90-equivariant|faithful|Aut`. **Comparison:** explains the distinction between the live and withdrawn statements, adding to RS H90-S/H90-E.

Over a field, let G=G_m and N=span(1,t,t^{-1}) inside k[t,t^{-1}], with the left regular action. This finite saturated stable module generates the coordinate algebra, but G→GL(N) is z↦diag(1,z^{-1},z), which is faithful and has image in a proper diagonal subgroup. A nonzero off-diagonal coordinate function on GL_3 maps to zero, so the coordinate-ring map is not injective and hence cannot be faithfully flat. This tests the cancelled claim only and leaves the live faithful-representation argument intact.

### NCTX-03 — One disappearing component links the two cotes

**Source:** 90.pdf, scans 002,010; 91.pdf, scans 008–009. **Kind:** own idea. **Confidence:** high for the displayed example, because the group law, special fibre and saturation are explicit; no general equivalence between the two criteria is claimed. **Quote:** “toutes ses fibres sont non vides”; “U=G_T”. **Context search:** `90-components|91-centraliser|special fibre|saturation|component`. **Comparison:** adds a concrete bridge between RS H90-C/H90-S and H91-R.

Let R=k[t]_(t), K=k(t), and take the open subgroup G=Spec(R)⊔Spec(K) of the constant two-element group over Spec(R), retaining the whole identity component and only the generic point of the other component. It is flat, affine and of finite presentation, but the identity subgroup U contains the entire special fibre and is not G, so condition R fails. Its algebra B=R×K has a finite R-submodule N=0×R whose saturation is 0×K, which is not finite over R; the nonidentity irreducible component also misses the closed fibre. The example demonstrates both obstructions in the same object, is consistent with the finite-type criterion on 90/010, and supplies no counterexample to that criterion.

### NCTX-04 — A presentation matrix realizes the open surjectivity locus

**Source:** 91.pdf, scans 016–017. **Kind:** own idea. **Confidence:** high for the conditional calculation, because it uses a finite presentation of the cokernel; the existence of the manuscript's coherent modules is a separate input. **Quote:** “M_v … M_u”; “par Nakayama”. **Context search:** `91-hom-unramified|Nakayama|cokernel|coherent`. **Comparison:** makes one intermediate step in RS H91-H explicit without claiming a proof of its theorem.

On an affine base, suppose q:M_v→M_u is available and choose a finite presentation A^n→A^m→C→0 of C=coker(q), with matrix P. The locus where q is surjective is the union of the principal opens defined by the m×m minors of P, because C_p=0 exactly when that presentation matrix is surjective over A_p. Cokernels commute with base extension, so this description also supplies the expected universal open condition. It proves only the local finite-presentation step after the corepresenting modules have been constructed.

### NCTX-05 — The Hom square has a conditional cartesian calculation

**Source:** 91.pdf, scan 018, diagram (2). **Kind:** own idea. **Confidence:** high for the following algebraic identity under its explicit hypotheses; medium for its exact role in the unfinished manuscript proof because the torsor existence argument is absent. **Quote:** “princ. homogènes sous les groupes”. **Context search:** `91-hom-unramified|torsor|obstruction|RN142-01|Hom`. **Comparison:** adds a possible proof component to RS H91-H and a precise comparison with S91 RN142-01 (91/142).

For a surjection q:V→U and an injection J→J_t, restriction and localization give
\[
\operatorname{Hom}(U,J)\simeq
\operatorname{Hom}(V,J)\times_{\operatorname{Hom}(V,J_t)}\operatorname{Hom}(U,J_t).
\]
Indeed, if a:V→J and b:U→J_t agree after composition/localization, then a vanishes on ker(q), since its image there vanishes in J_t and J→J_t is injective, so a factors uniquely through U. The one-associated-point hypothesis suggested by the margin on 012 is relevant to choosing a non-zero-divisor parameter, but must be established for the actual base and J. Even a cartesian square of acting groups does not prove the missing extension space nonempty; the obstruction class and compatibility of the two specified corners remain essential.

### NCTX-06 — A modern comparison for the ambient Hom functors

**Source:** 91.pdf, scans 016–017. **Kind:** own idea; unpursued implication. **Confidence:** medium for using this as a route to the manuscript's relative theorem, because a comparison of categories and the unramified condition is still required. **Quote:** “Hom_S(X,Y;φ)”. **Context search:** `91-hom-unramified|MPL_131|Hom|non-projective`. **Comparison:** adds a checked benchmark to RS H91-H, not a verdict that the manuscript formulation is new or completely matched.

SP-0D1C represents the ambient morphism functor by an algebraic space when the source is flat, proper and finitely presented and the target is separated and finitely presented, and SP-0DPL records its separatedness. These match the principal finite-presentation/properness hypotheses in the manuscript sufficiently to provide a concrete comparison target for the composition map. One must still identify the manuscript's open condition with the relative unramified locus and account for its claim of representation by preschemes; the marginal proposal to drop a separatedness hypothesis lies outside this immediate comparison.

### NCTX-07 — Compare the two Hom constructions by their actual functors

**Source:** 91.pdf, scans 016–018; S91's locators 114,120,136. **Kind:** own idea. **Confidence:** medium for the value of the comparison, low for any identification until the categories and transition maps are supplied. **Quote:** “Énoncer plutôt en termes de”; S91's reported “foncteur pleinement fidèle”. **Context search:** `RN114-01|RN120-01|RN136-01|RN136-02|Hom`. **Comparison:** adds a bridge to S91 RN114-01, RN120-01 and RN136-01/02; those remain unreviewed leads.

The present leaves concern relative representability and infinitesimal rigidity of a composition map, whereas S91 reports Hom comparisons for constructible models and inverse-system objects. A useful comparison would explicitly send each finite-presentation stage map to a map of limit objects and then ask whether the same test base changes compute both relative-product functors. Shared Hom notation alone does not supply that functor or transfer either representability theorem.

### NPLAN-01 — What the pages confirm and what they do not establish

**Source:** 90.pdf, scans 002–025; 91.pdf, scans 002–018. **Kind:** unpursued implication; bounded planning comparison. **Quote:** “Représentabilité relative”; “Flattening functor”; “Passage au quotient”. **Context search:** `K_G|K.theory|S19|Greenberg|Néron|intersections|residues|WG`. **Comparison:** refines P90/P91 and RS MPL_91_099-143 §68 rather than adopting the catalogue predictions as mathematical evidence.

Cote 90 supplies equivariant generation and resolution material relevant to a future K_G(X) construction, but these leaves do not define that group or give a Chern-class or Riemann–Roch formula. Cote 91 directly confirms non-projective representability, flattening and quotient work, with Greenberg named on the cover but no Greenberg point construction in this supplied range; S91 locates such work at 126,128,131–132. Neither the reused EGA sheets nor these Hom arguments gives the numerical cycle-pairing or residue-duality constructions named in the wider plan. Thirty-nine retained scans cannot determine S19's proposed size of the remaining Book I material.

