# Independent application review: C04, C05, C10

**Reviewer:** /root/bisite_mapping; GPT-6 Astra Pro; reasoning effort inherited and not exposed.  
**Scope:** Three targeted mathematical checks against the frozen text only. No manuscript images were read, no frozen file was changed, and no broader claim from the contextual registers was re-audited.  
**Prior-work credit:** The root's supplied-context audit identifies these points as already settled in Hua/context. This record independently checks their application to the cited manuscript passages; it claims no new result or priority.

| ID | Frozen location | Application verdict |
|---|---|---|
| C04 | scan 036; condition (ii) from scans 033–035 | The groupoid observation is correct for ordinary weak homotopy equivalences. A nontrivial BG disproves the adjacent proposed repair using only connectedness. |
| C05 | scan 035 | The comma-category isomorphism and its forward product-comparison argument are correct. Binary products alone do not include the terminal-object condition; the empty category is a counterexample to the unqualified binary/finite equivalence. |
| C10 | scans 034 and 040 | Strong saturation of W formally implies strong saturation of W_A for every A, without assuming A aspherical. This does not check the independent theorem that W is strongly saturated. |

## C04 — A connected groupoid separates product stability from asphericity

**Exact frozen evidence.** Scan 036 first proposes that an A satisfying (ii) and 0-connectedness is W-aspherical, then says:

> `alors dans $\widehat A$ $\underline W_A$ est formé des seuls iso`

Its explicit scope is the usual weak equivalence class. Write this class as W∞ in the review, without changing the manuscript's notation.

Take A=BG for a nontrivial group G, for example C₂. A presheaf on BG is a G-set, with the choice of left or right action affecting only notation. Its category of elements is the corresponding action groupoid. For an equivariant map u:X→Y, the induced functor of action groupoids is a weak homotopy equivalence precisely when it induces a bijection on orbits and, for each x, an isomorphism on the automorphism groups at x and u(x).

For this particular functor the automorphism map is the inclusion of stabilizers G_x⊆G_{u(x)}. Being an isomorphism therefore says that the stabilizers are equal. The map from the orbit of x onto the orbit of u(x) is then bijective, and the orbit bijection gives a bijection of the whole underlying sets. Thus u is an isomorphism of G-sets. Conversely, an isomorphism of G-sets gives an isomorphism of their categories of elements. This verifies the manuscript application W_A=Iso for A=BG.

Isomorphisms are stable under all products, so condition (ii) holds. But BG is connected and has fundamental group G; when G is nontrivial, BG→e is not in W∞. Hence product stability plus 0-connectedness does not imply asphericity, and the connected repair in scan 036 fails in the precise way indicated by its own following groupoid observation.

This does **not** say that the functor from G-sets to the absolute homotopy category preserves binary products. For G=C₂, the category of elements of the regular G-set is contractible, whereas that of the diagonal action on G×G has two components. Its product comparison therefore fails to be a weak equivalence. The distinction is between product stability of arrows in W_A (and the ordinary local category Hot_A) and product preservation by the absolute category-of-elements realization.

## C05 — The comma calculation is correct; the empty product is separate

**Exact frozen evidence.** Scan 035 writes the comparison

> `A_{/X\times Y}\longrightarrow A_{/X}\times A_{/Y}`

and the formula

> `(A_{/X\times Y})_{/\alpha}\simeq A_{/a\times b}`

for α=(a/x,b/y). Its final diagram also equates preservation of `produits binaires` and `produits finis`.

Let h_a=A(−,a) and h_b=A(−,b), and let P denote the displayed comparison. An object of P/((a,x),(b,y)) is a triple consisting of c∈A, an element (u,v)∈X(c)×Y(c), and arrows r:c→a, s:c→b with u=X(r)(x) and v=Y(s)(y). The element (u,v) is uniquely determined by c,r,s. A morphism from (c,r,s) to (c′,r′,s′) is exactly an arrow t:c→c′ satisfying r=r′t and s=s′t. These are precisely the objects and arrows of the category of elements A/(h_a×h_b), and the identification preserves identities and compositions. Thus the displayed comma isomorphism is correct, with a×b interpreted as the product of representable presheaves, not an assumed product object of A.

Consequently, if every A/(h_a×h_b) is W-aspherical, P is W-aspherical and belongs to W by the relevant Theorem A axiom. This checks the forward application actually made on the page. Conversely, applying the comparisons to representables has the expected target (A/a)×(A/b), which has a terminal object. Reading a comparison that is invertible in Hot(W) as membership in W uses strong saturation when W is not already the usual W∞; the comma calculation itself does not prove that separate input.

For the nullary issue, take A=∅ and W=W∞. The presheaf category on A is the terminal category, and the category-of-elements functor sends its sole object to ∅. Every binary comparison is the isomorphism ∅→∅×∅=∅, so binary products are preserved. But the terminal presheaf is sent to ∅, whereas the terminal object of Hot is the point, and ∅→e is not a weak equivalence. Thus finite products are not preserved when “finite” includes the empty product.

The application should therefore retain a separate terminal-object condition: A=i_A(1) must have the terminal homotopy type, supplied in the usual formulation by A→e∈W. If the author's intended convention excludes the empty product, that convention removes this particular objection but must be stated; the standard all-finite-products reading has the gap just exhibited. None of this invalidates the objectwise comma isomorphism.

## C10 — Strong saturation passes to the inverse-image class

**Exact frozen evidence.** Scan 040 gives

> `\uline{Cor} Pour $\forall A$, $\underline W_A$ est saturé.`

Scan 034 explicitly invokes `fortement saturé` for W_A and attributes this to strong saturation of W, with the connecting reading retained as uncertain in the transcription.

Let i_A:Â→Cat be the category-of-elements functor and W_A=i_A⁻¹(W). Let Q:Cat→Hot(W) and Q_A:Â→Hot_A=Â[W_A⁻¹] be the localization functors. Since Q i_A sends every arrow of W_A to an isomorphism, the universal property gives a functor F:Hot_A→Hot(W) with FQ_A naturally isomorphic to Qi_A.

If Q_A(u) is invertible, then Q(i_A(u)) is invertible. Strong saturation of W implies i_A(u)∈W, and therefore u∈W_A. The converse follows directly from the definition of localization. Hence W_A is strongly saturated.

This argument requires no asphericity of A, no equivalence Hot_A≃Hot(W), and no full faithfulness or conservativity of F. In particular, it remains valid for A=BG and A=∅. Its only saturation input is strong saturation of W; weak saturation or closure under retracts alone is not being substituted for that hypothesis. The proof of that input elsewhere in the manuscript was outside this targeted check.

## Event accounting

Four mathematical application-check events are recorded separately: C04's groupoid counterexample, C05's comma calculation, C05's empty-category counterexample, and C10's formal localization argument. These events do not alter the BISITE matrix's textual-only check scope and are not new checks of the full contextual source theorems.

**Recorded:** 2026-11-18T03:12:41+00:00.  
**Frozen combined SHA-256, unchanged:** `63b5213a6f4b8790fefa6a9d7d8ce3fdc50723ef67fad682348b36a48845b149`.
