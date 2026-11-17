# Independent mathematical assessment: frozen scans 050–058

Research support for the root agent, 2026-11-17. Only frozen page `.tex` files and supplied context were read; no images were inspected and no transcription was edited. This is an assessment of exact hypotheses and possible repairs, not a replacement note catalogue or a novelty claim.

## Source boundaries and credit

The controlling witnesses are the frozen files `pages/MPL_91_019-058_91_scan050.tex` through `...scan058.tex`. The context comparison is **Hua, modernised reading of cote 91**, §VI, **“Lissité, étalitude, dimension (pages 49 à 53)”**, lines 935–984, and **“Torseurs, et les composantes connexes relatives (pages 54 à 58)”**, lines 986–1027, in `work/context/hua_project/91.modern.tex`. Its opening comments explicitly describe an interpretation, supply some hypotheses, and identify its literature as recalled rather than checked. Hua's manuscript page numbers are one lower than our scan numbers. In particular, its discussion of manuscript page 58 reaches beyond frozen scan 058, whose last sentence stops at “on tire|on trouve”. Its completed canonical-map statement and converse must not be attributed to the retained endpoint.

**Hua, findings register, `91-weil-restriction-finite-etale-criterion`**, supplied through `notes/RESULTS_STATE.md:18,465`, remains a candidate/search-status claim. The assessment below proves a precise finite locally free version by a modern argument; it does not validate a novelty claim or silently replace the register's status. `RESULTS_STATE.md:22` specifically requests the full four-condition equivalence with proof.

## EC01 — The lifting argument and the missing separation in the bound

**Frozen source:** 050–052. **Confidence: high**, because the counterexamples and repaired lifting argument are elementary and all hypotheses are displayed.

Scan 050 assumes the restrictions exist and are locally of finite type over a locally noetherian base. It inserts affineness of `T/S` in the smooth case, and replaces finiteness by finite type in the étale case. Scan 051 says the lifting argument first gives smoothness and then tries to prove finite fibres. Hua instead describes non-ramification followed by flatness, and works with zero-dimensional Artinian sources in the explanation. That is a modernised argument under the surrounding finite-source setting, not the same written proof.

A clean modern repair for the étale assertion is to use **unique** lifting across nilpotent closed immersions. After base change to `T`, an étale morphism gives unique local lifts, which glue uniquely. Thus the restriction morphism is formally étale; if it is represented and locally of finite presentation, it is étale. The frozen locally noetherian/locally finite type assumptions provide the finite-presentation condition. This proof does not require a section to be determined by one point.

The latter sentence on 051 needs separation. Two sections of a **separated étale** morphism have an equalizer both open and closed, so agreement at a point of a connected source implies agreement everywhere. For a nonseparated étale map the equalizer need only be open.

**Own counterexample to the numerical bound, not merely the proof step.** Let `k` be algebraically closed, `T=A¹_k`, and let `X` be two copies of `A¹_k` glued along `A¹_k\{0,1}`. The map `g:X→Y=T` is étale, of finite type, and has at most two geometric points in any fibre. The source `T` has one geometric connected component. Nevertheless there are four sections, choosing either lift of 0 and either lift of 1 independently. For every test scheme `U`, a section over `A¹_U` amounts to a clopen choice of lift along each of the two disjoint divisors `{0}×U` and `{1}×U`; these choices extend and glue uniquely away from the divisors. Hence `Res_{T/k}(X)` is the constant four-point scheme, while `Res_{T/k}(Y)=Spec(k)`. The existence assumptions are satisfied, but `4>2^1`. A single doubled point already refutes determination by the image of one point away from the doubled point. Two doubled points refute Corollary 1's stated `n^ν` bound under the visible hypotheses without separation.

This does not contradict preservation of étaleness: the four-point restriction is étale. Nor does it affect the finite étale case of EC04, where separation is automatic.

## EC02 — Dimension sets require more than reversing the formula

**Frozen source:** 052–053. **Confidence: high** for the examples and pointwise formula; the manuscript's ambiguous labels stay untouched.

The source writes `D(s)=nD'(s)` but concludes pure relative dimension `nd`. Hua explicitly reverses the formula and restricts its equality of dimension sets to local `T_s`; that repair must be credited to Hua. It also correctly warns about sums of dimensions when `T_s` has several points.

There is an additional issue even for local `T_s`: not every geometric point of `Y_s` need occur in a section of `Y` over `T_s`.

**Own nonvacuous counterexample to Hua's local-source dimension-set equality.** Let `S=Spec(k)`, `T=Spec(k[ε]/ε²)`, `Y=T ⊔ Spec(k)`, and `X=A¹_T ⊔ A²_k`, with `g` the two projections. This is smooth, `T/S` is finite free of rank 2, and the source fibre-dimension set is `{1,2}`. No nonempty `T_U` admits a `T`-map to the `Spec(k)` summand: it would have to kill the nonzero element `ε` of `O_U[ε]/ε²`. Therefore `Res(Y)=S` and `Res(X)=A²_k`. The restriction's dimension set is `{2}`, not `{2,4}`. All schemes involved are of finite type and the restrictions exist.

The robust repair is pointwise. Over an algebraically closed field write the finite source as `T=⊔ T_i`, with Artinian local lengths `n_i`. At a section `x:T→X` over a section of `Y`, let `d_i` be the smooth relative dimension of `g` at the image of the unique point of `T_i`. The relative dimension of the restriction at `x` is `Σ_i n_i d_i`. One may verify this through étale coordinates or the tangent space `Γ(T,x* T_{X/Y})`. In particular, constant relative dimension `d` gives `nd`. Any equality of global dimension sets must quantify over dimensions actually realised by such sections. This is a modern repair, not a transcription correction.

## EC03 — The degree formula needs the finite-source hypothesis

**Frozen source:** 054, Corollary 1 bis. **Confidence: high**, by direct calculation.

For finite locally free `T/S`, a finite étale `g:X→Y` of constant degree `λ` has restriction with geometric fibre degree `λ^{ν(s)}`, where `ν(s)` is the number of geometric points of `T_s`. Over an algebraically closed field, the finite source is a disjoint union of Artinian local schemes; each finite étale cover of such a local scheme is a disjoint union of copies, so each component supplies exactly `λ` choices. This proves the geometric-fibre statement; it does not prove that the entire restriction morphism is finite when `ν` jumps.

On 054, however, `T/S fini` is explicitly deleted and replaced by the conditions of Corollary 1. The following example satisfies that broader visible setting and defeats the exact degree formula.

**Own example, independently also suggested by the root agent.** Take `S=Spec(k)`, with `k` algebraically closed of characteristic different from 2, `T=Y=G_m,k`, and `g:G_m,k→G_m,k`, `z↦z²`. It is finite étale of degree 2. Here `ν=1`, `Res(Y)=S`, and `Res(X)=∅`: a section over any nonempty test scheme would give, after passage to a geometric point, a Laurent-polynomial square root of `t`, which cannot exist because its valuation at `t=0` would have to be `1/2`. Thus the restriction has degree 0, not `2^1`. Connectedness alone supplies uniqueness for separated étale lifts, not existence of all choices. This example does not by itself disprove the four-condition equivalence in an appropriately restricted nonfinite-source class.

## EC04 — A complete finite locally free four-condition repair

**Frozen source:** 054, Corollary 3 and implication diagram; 055, “homogène”. **Context:** Hua, findings register, `91-weil-restriction-finite-etale-criterion`. **Confidence: high**, with the proof below and primary references R1–R5. The full argument is ours; the frozen page supplies the statements and arrows, not these details.

Let `f:T→S` be a **finite locally free morphism of schemes**, with no additional noetherian hypothesis needed. Interpret restriction initially as an fppf sheaf. The following are equivalent:

1. `ν(s)=#T_{̄s}` is locally constant on `S`.
2. For every finite étale morphism `X→Y` of `T`-schemes, the induced morphism of restriction sheaves is representable and finite étale.
3. For every finite étale `T'→T`, `Res_{T/S}(T')` is a finite étale `S`-scheme.
4. `Res_{T/S}(T⊔T)` is finite over `S`.

For arbitrary finite locally free `f`, restriction of an étale morphism is already étale as an algebraic-space morphism [R1]. In (3) and (4), existence as an affine scheme can also be seen directly: on a finite-free affine chart, write the finitely many coordinates of a map of finite algebras and impose their algebra relations. In (4) this is simply the scheme of idempotents in the finite locally free algebra `f_*O_T`. Consequently “finite” in (4) already implies finite étale. Scheme representability of arbitrary `Res(X)` or `Res(Y)` is a different question; the general existence theorem gives algebraic spaces [R2]. The original theorem's scheme-existence qualification must not be silently dropped when discussing arbitrary `X,Y`.

**Local structure from (1).** Fix a geometric point `s`, and put `m=ν(s)`. Over the strict henselisation at `s`, the finite algebra of `T` splits into `m` local henselian factors [R3]. The finite set of orthogonal idempotents defining that decomposition descends to an étale neighbourhood `V→S`. Shrink `V` so that `ν=m` and each factor `T_i→V` has positive constant finite locally free rank. Every geometric fibre of each factor has at least one point. There are `m` factors and the total fibre has `m` points; hence every factor has exactly one geometric point in every fibre. Each `T_i→V` is therefore finite, surjective and universally injective, hence a universal homeomorphism. If `m=0`, the same discussion is the empty decomposition.

**(1)⇒(3).** Finite étale schemes over `T_i` descend uniquely to finite étale schemes `E_i` over `V`, by topological invariance [R4]. That equivalence is stable under arbitrary base change. For every `V`-scheme `U`, a section of `T_i×_V E_i` over `T_i×_V U` corresponds to a section of `E_i` over `U`. Thus restriction from `T_i` is `E_i`, and restriction from the disjoint union `T_V` is `∏_i E_i`, finite étale over `V`. Descent proves (3) over `S`.

**(1)⇒(2).** For any scheme `U→Res(Y)`, use the universal map `T_U→Y` and set `W=T_U×_Y X`. Then `W→T_U` is finite étale, and

`U×_{Res(Y)}Res(X) = Res_{T_U/U}(W)`.

Condition (1) survives every base change, so the preceding proof shows that this fibre product is finite étale over `U`. This simultaneously establishes relative representability and finiteness, and handles finite étale maps whose degree is only locally constant rather than one global `λ`.

**(2)⇒(3)⇒(4).** Set `Y=T`, so `Res(T)=S`; then take `T'=T⊔T`.

**(4)⇒(1).** The scheme of idempotents is étale by [R1] (or unique lifting of idempotents). If finite, it is finite étale and has locally constant rank. Its geometric fibre has one point for every subset of the `ν(s)` geometric points of `T_s`, hence exactly `2^{ν(s)}` points. Since the function `m↦2^m` is injective, `ν` is locally constant.

This proves all written arrows under the explicit finite locally free hypothesis. It does not establish the more general version suggested by the deletion of finiteness in the source.

## EC05 — Homogeneous maps, the relative component object, and compatibility

**Frozen source:** 055–058. **Confidence: high** under the finite locally free hypothesis of EC04; no claim is made for all flat morphisms bearing the manuscript's name “homogène”.

The local factors in EC04 glue to a finite étale scheme `A=A(T)` and a finite locally free universal homeomorphism `q:T→A`. Locally on the étale base `A` is the disjoint union of one copy of the base for each factor. The overlap identifications are the unique identifications matching those components, so the cocycle holds. This produces `A` independently of a base point or connectedness assumption.

Topological invariance gives, for every base change `U→S` and every étale `S`-scheme `E`, a natural bijection

`Hom_U(A_U,E_U) ≅ Hom_U(T_U,E_U)`.

It therefore gives the **internal** Hom identity on 058, not merely equality of global sections. The pair `(A,q)` is unique by this universal property, and its formation commutes with arbitrary base change. On this class of sources it is legitimate to identify `A` with the finite étale scheme of geometric connected components. One should not apply a general relative-π₀ theorem with geometrically reduced fibres to the present possibly nonreduced finite sources without checking its hypotheses.

After choosing `a` on a connected `S`, write `G=π₁(S,a)`. The internal Hom has fibre

`Map(A_a,E_a)`, with `(γ·h)(x)=γ·h(γ⁻¹·x)`.

The `G`-action comes from the base-change-compatible geometric construction. It is not furnished by left exactness alone (EC06). Classification by finite `G`-sets and change of geometric point are verified in [R5]; the group isomorphism for two base points is only canonical up to inner conjugation. The underlying scheme `A` is nevertheless intrinsic. The formula also proves the covariance of `A(T)` in `T` and `A(T⊔T')=A(T)⊔A(T')`; at the level of exponential functors, products correspond to coproducts of exponents.

Base change preserves homogeneity directly. For composition of two finite locally free homogeneous maps `U→T→S`, étale-locally write `T=⊔T_i` with each `T_i→S` a universal homeomorphism. The locally constant fibre counts of `U→T` then descend along each underlying homeomorphism, and the composite count is their sum. This proves the finite-case composition assertion on 055, rather than merely invoking it.

## EC06 — The unrestricted left-exact endofunctor assertion is false

**Frozen source:** 057–058, especially “un tel foncteur est nécessairement”; compare Hua, modernised reading of cote 91, “Torseurs, et les composantes connexes relatives”, lines 1002–1005. **Confidence: high**, because the following is a direct finite-set calculation.

Take `G=C₂` and define an endofunctor of finite `G`-sets by letting `F(E)` be the underlying set of `E` equipped with the **trivial** action; apply the same underlying functions to maps. Forgetting an action and assigning the trivial action both preserve finite limits. Indeed this example also preserves finite colimits and surjections.

Suppose `F(E) ≅ underline Hom_G(A,E)=E^A` naturally, with the usual internal Hom action. Evaluate on a trivial two-point set. The underlying cardinality is `2^{|A|}`, whereas `|F(2)|=2`, so `|A|=1`. A singleton `G`-set is trivial and exponentiation by it is the identity functor. But `F(G)` is a trivial two-point set, while `G` with its regular action has no fixed points; these are not isomorphic. Contradiction.

An alternative is `F(E)=E^G` with trivial action. It is left exact and also contradicts internal-Hom representability (evaluate on the trivial two-point set, then on the regular orbit). The first example is stronger because preservation of surjections or ordinary exactness does not rescue the assertion.

Ordinary equivariant `Hom_G(A,E)` and the underlined internal Hom must be kept separate. The former is a set of equivariant maps, and it is not the underlying set of `E^A`. Reading the notation as ordinary Hom would also leave unspecified how it becomes an endofunctor of `G`-sets. The geometric repair is EC05: establish the finite étale component object and its universal property after **every base change**, then derive the exponential description. Do not cite the broad category-theoretic sentence as a theorem of Galois categories. Hua repeats the inference, so its modernisation does not repair this gap.

## EC07 — Global Hom representability is weaker than the required compatibility

**Frozen source:** the compatibility margin and the passage from internal Hom to global sections on 058. **Confidence: high**, by the explicit example and the classification of finite étale covers of a strictly henselian local base.

Let `S=Spec(C[[t]])` and `T=Spec(C[[t]][x]/(x²−t))`. The source is connected and finite free of rank 2, but `ν` is 1 at the closed geometric point and 2 at the geometric generic point. Every finite étale scheme over the strictly henselian local scheme `S` is constant. Consequently, on finite étale targets, the ordinary global functor `E↦Hom_S(T,E)` is represented by `A=S`: a map from connected `T` to a constant finite scheme picks exactly one summand.

After geometric generic base change, however, `T` has two points and `A` one. Maps to a constant two-point target number four and two respectively. The internal identity `(*)` therefore fails. In particular, ordinary global Hom representability does not imply a relative component quotient with geometrically connected fibres or compatibility with base change. This is a concrete reason to preserve the source's unfinished compatibility warning. Hua's statement that the finite étale `A(T)` does not exist without local constancy is accurate for the **base-change-compatible relative component object**, but not if reduced merely to the displayed ordinary global universal property.

## EC08 — The μ₂ example and the limit of its link to LM1 D.11

**Own illustrative calculation, requested by the root agent. Confidence: high**, by an explicit affine presentation. **Context:** `RESULTS_STATE.md:15,356`, `LM1 D.11`; its supplied status remains **Open (the return's claim)**.

Let `R=Z₂`, `S=Spec(R)` and `T=μ₂,S=Spec(R[x]/(x²−1))`. This is finite free of rank 2. Its geometric generic fibre has two points; its characteristic-2 geometric special fibre has one. Thus `T/S` is not homogeneous in the sense of 055.

`Res_{T/S}(T⊔T)` is the scheme of idempotents `a+bx` in `R[x]/(x²−1)`, with equations

`a²+b²=a`, `b(2a−1)=0`.

These imply `b(4b²−1)=0`. The branches `b=0` give `a=0,1`, two copies of `S`; on the other branch 2 is invertible and `a=1/2`, `b=±1/2`, giving two copies of `Spec(Q₂)`. Accordingly

`Res_{T/S}(T⊔T) ≅ S ⊔ S ⊔ Spec(Q₂) ⊔ Spec(Q₂)`.

It is affine and étale, with four generic and two special geometric points, but is not finite. The two generic idempotents `(1±x)/2` explain the failure to extend integrally. This is an exact obstruction to applying the finite-étale-preservation criterion to this source; it is not an integral μ₂-extension classification or a solution of the missing arithmetic descent data in `LM1 D.11`.

## EC09 — What the torsor assertion needs

**Frozen source:** 055–056; Hua, modernised reading of cote 91, “Torseurs, et les composantes connexes relatives”, opening paragraph. **Confidence: high** for the finite-limit statement; high for the finite étale situation using [R1] and EC04.

Restriction preserves finite limits, so the action identity `P×_Y G ≅ P×_Y P` transports whenever the objects are represented. This accounts for the manuscript's weak/principal assertion. A torsor also needs the appropriate covering/surjectivity condition. For finite locally free `T/S`, an étale surjection remains an étale surjection under restriction [R1], so finite-group étale torsors do give torsors under the restricted group. Homogeneity is what additionally makes that restricted group **finite** étale; without it, even the restriction of a constant finite group can have varying finite geometric fibre cardinalities and fail to be finite, as in EC08. Keep this finiteness condition distinct from the action identity and the covering condition.

## Keyword/context search log

All queries were run against the six supplied context files: `work/context/README.md`, `work/context/notes/RESULTS_STATE.md`, `work/context/hua_project/README.md`, `work/context/hua_project/91.modern.tex`, and the two files in `work/context/same_cote_91/`. The raw regexes and complete matches are recorded in `research/etale_criterion_context_searches.jsonl`. “No matching example” below is limited to those supplied materials.

| Assessment item | Search themes / log ID | Material comparison |
|---|---|---|
| EC01, lifting/separation | `Lissité, étalitude`, `non-ramification`, `point par point`, `doubled`, `séparé`; `EC01_lifting_separation` | Hua VI lines 935–949 gives the differing proof summary; neighboring notes discuss other separation corrections, not this doubled-point bound. No matching doubled-point example found. |
| EC02, dimensions | `D(s)`, `D'(s)`, `dimensions des composantes`, `set of sums`; `EC02_dimension` | Hua VI lines 952–967 and header lines 76–78 already reverse the formula and impose local fibres. The inaccessible-summand example adds a separate hypothesis test. |
| EC03, degree | `Corollaire 1 bis`, `degré séparable`, `lambda`, `G_m`, `Laurent`; `EC03_degree` | Hua VI lines 969–974 records the finite-source argument. Laurent-series discussions elsewhere in the context are unrelated; no matching squaring-cover example found. |
| EC04, equivalence | finding ID, `Corollaire 3`, `nu(s)`, `finite locally free`, `localement constant`; `EC04_criterion` | Direct match to Hua VI lines 976–981 and findings-register ID at RS18/465. The four-arrow proof above is additional assessment. |
| EC05, homogeneous maps | `homogène`, `homogeneous`, `composition des morphismes`, `universal homeomorphism`; `EC05_homogeneous` | Hua's later “Weil et Greenberg” section also discusses universal homeomorphisms, but does not supply the missing proof of this criterion. Earlier “principal homogeneous” notes concern a different use of the word. |
| EC05–EC07, components/functors | `exact à gauche`, `pi_1`, `G-sets`, `internal Hom`; `EC06_functor`; `pi_0`, `compatibilité`, `adjoint ... gauche`; `EC07_components_compatibility` | Hua VI lines 996–1027 directly matches the claimed inference and modern relative-component interpretation. No matching finite-group counterexample or strict-henselian compatibility example found. |
| EC08, μ₂ | `mu.?2`, `μ.?2`, `D.11`, `dyadic`; `EC08_mu2` | RS15/356 and neighboring notes' status tables all retain the unresolved arithmetic extension problem. They do not supply the idempotent calculation or a comparison that would settle D.11. |
| EC09, torsors | `fibrés principaux`, `torseurs`, `principal homogène`, `torsor`; `EC09_torsors` | Hua VI opening “Torseurs...” and neighboring notes on torsors in the Hom obstruction problem; these are distinct uses requiring different covering hypotheses. |
| Primary-source verification | `Romagny`, `EGA IV 6.8`, `18.1.2`, checked Stacks tags; `EC10_primary_references` | Only Hua's remembered EGA/Romagny footnote appears. No supplied text of those cited works was treated as verified; the primary sources below were retrieved independently. |

## Primary-source log and checked scope

Searches used the web tool, first routine Stacks queries, then the stronger engine for the exact restriction-of-scalars page. Only the Stacks Project's own theorem pages were relied on. Broad search hits and third-party expositions were not used as evidence. Retrieved 2026-11-17.

| Key | Primary source / exact locator | Verified use and limit |
|---|---|---|
| R1 | The Stacks Project, Lemma 97.11.3, [Tag 05YD](https://stacks.math.columbia.edu/tag/05YD), web ref `turn15view1` | Finite locally free source; restriction of an étale morphism is representable by algebraic spaces and étale, and preserves surjectivity. Does not say finite étale maps remain finite without another condition. |
| R2 | The Stacks Project, §97.11, [Tag 05Y8](https://stacks.math.columbia.edu/tag/05Y8), Proposition 97.11.5, web refs `turn10search0`, `turn14view2` | General algebraic-space representability for finite locally free source; base change is Lemma 97.11.2. Does not give unrestricted scheme representability. |
| R3 | The Stacks Project, Lemma 10.153.4, [Tag 04GH](https://stacks.math.columbia.edu/tag/04GH), web ref `turn14view0` | Finite algebras over a henselian local ring are products of henselian local rings. The descent and constant-count argument in EC04 are our application. |
| R4 | The Stacks Project, Theorem 59.45.2, [Tag 04DZ](https://stacks.math.columbia.edu/tag/04DZ), web ref `turn15view2`; Proposition 58.8.4, [Tag 0BQN](https://stacks.math.columbia.edu/tag/0BQN), web ref `turn15view3` | Topological invariance for étale schemes, and specifically for finite étale covers, under a universal homeomorphism. The theorem's page cites EGA IV, Theorem 18.1.2; the original EGA text was not independently opened, so do not describe it as checked directly. |
| R5 | The Stacks Project, Theorem 58.6.2, [Tag 0BND](https://stacks.math.columbia.edu/tag/0BND), web ref `turn15view0` | Connected-scheme finite-étale/finite-π₁-set equivalence; comparison of geometric base points only up to inner conjugacy. It does not assert the false endofunctor representation in EC06. |

The root agent should open these primary URLs itself before reusing their web citation references in a user-facing response. These references support modern repairs only; they neither resolve the manuscript's uncertain words nor justify novelty language.
