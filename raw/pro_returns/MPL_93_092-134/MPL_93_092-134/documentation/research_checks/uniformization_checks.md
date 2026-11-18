# Post-freeze research checks: uniformization, algebraicity and formal jets

Run `/root/uniformization_context`; model GPT-6 Astra Pro, inherited; numerical effort setting not exposed. All work occurred after the transcription freeze of 2026-11-18 01:07:16 UTC. This report reads frozen TEX and supplied textual context only; it neither rereads scan images nor changes transcription/inventory. Proposed note IDs E01–E15 are for root to adopt or renumber. The accompanying `uniformization_context_map.md` gives the full Michel Hua section/line map and confirms reading all 2,524 source lines.

## E01 — Mere homogeneity does not give the three uniformization domains

**Location:** scan126, definition and Theorem1(a),(b). **Actual check:** direct counterexample.

Take P=P¹(C) and D=P\{0,∞}=C*. The subgroup of projectivities z↦az, a∈C*, acts transitively on D: a=v/u sends any u to any v. Thus D satisfies the printed definition. But π₁(D)=Z, so it is not simply connected and is not projectively equivalent to P¹, C or a disk. The theorem as written is false; the counterexample is connected, so merely adding connectedness does not repair it.

**Context:** Michel Hua, modernised reading of cote93, §X “Domaines homogènes et revêtement universel,” lines1563–1572, repeats the same implication. This check contradicts that part of Hua's modernization rather than relying on it. `RESULTS_STATE`13–19 has no prior settled result on this classification. Context query: `homog|simplement connexe|uniformisation`.

## E02 — The intended simply connected statement has a separate scope

**Location:** scan126(c), and127–128 use of universal covers. **Actual check:** hypothesis analysis with classical uniformization carried as background.

For the intended category, require D to be connected and simply connected. Uniformization then supplies the abstract models P¹, C and the unit disk; the manuscript's subsequent construction needs these models and their Möbius extension property. This report does **not** claim to have proved a full classification of every homogeneous domain in P¹ or to have proved the general uniformization theorem. The C* counterexample to E01 does not invalidate the later construction, whose fibers are independently assumed universal covers and hence simply connected.

**Context:** Hua §X1567–1572 combines the invalid implication and the intended conclusion. Separate them. The explicit “pour iso” on frozen126(c) is material to the next check. Context query: `homog|pour iso|revêtement universel`.

## E03 — The real projective group has two components

**Location:** scan126 corollary, continued127. **Actual check:** algebraic calculation and explicit witness; recheck of Hua's correction.

For a real matrix g=(a b;c d) with nonzero determinant,

\[
\operatorname{Im}\frac{az+b}{cz+d}
=\frac{(ad-bc)\operatorname{Im}z}{|cz+d|^2}.
\]

Consequently the upper half-plane stabilizer is PGL₂(R)⁺, the positive-determinant component, which is isomorphic to PSL₂(R)=SL₂(R)/{±I}. The full GL₂(R)/R* has another component. Scaling a representative changes its determinant by a positive square, so determinant sign survives the quotient. For example diag(−1,1) induces z↦−z and exchanges the two half-planes. Thus the displayed equality of full PGL₂(R) with SL₂(R)/μ₂(R) is false on real points, even though the associated algebraic quotient relationship does not imply surjectivity on real points.

**Context:** Hua §X1574–1581 already makes this correction and explains the two components. The present calculation confirms his mathematical correction; it does not justify altering the frozen reading. Context query: `PGL|PSL|GL.*mathbb.*R|composantes`.

## E04 — Real descent must be split to produce a boundary circle

**Location:** scan127, equivalences α),β),γ),δ). **Actual check:** explicit nonsplit real structure and fixed-point calculation.

On P¹(C), the antiholomorphic involution j(z)=−1/\bar z exchanges0 and∞ and has no fixed point: a finite fixed point would satisfy |z|²=−1. This is a real descent of the projective line with empty real locus. One algebraic model is the conic x²+y²+z²=0 over R, whose complexification is a projective line but which has no real point. It cannot give a circle separating the sphere into two disks. Its automorphism real form is the compact one; by contrast, the usual conjugation has real locus RP¹ and gives the split form. Thus the unqualified correspondence between arbitrary real group/Lie-algebra forms and disks modulo polarity requires a split/real-point restriction. The fixed-point-free example alone suffices to refute the unrestricted circle claim, without a classification of all real forms.

**Context:** Hua §X1582–1590 adds the appropriate split/real-point restriction. His phrase identifying split forms with real structures of P itself should still be read with the real-point qualification: the displayed j is also a real structure of P. Context query: `forme réelle|descente|split|compact|cercle`.

## E05 — Functoriality here is on a groupoid of isomorphisms

**Location:** scan126(c), Scholie127. **Actual check:** category scope comparison and a counterexample to an overbroad interpretation.

Frozen126(c) explicitly inserts “pour iso” twice. This supplies the natural category for the Scholie127: biholomorphisms of simply connected curves extend to the relevant projective lines. The Scholie need not be read as making a new assertion about all holomorphic maps. Such an enlarged assertion would fail: exp:C→C is holomorphic and locally biholomorphic, but it does not extend to a holomorphic map P¹→P¹, since such a map is rational and exp has an essential singularity at∞. If projective-line morphisms mean only projective linear isomorphisms, even z↦z² would already be a counterexample. Thus this is a clarification, not a demonstrated new error in the manuscript after its explicit category qualification is taken into account.

**Context:** Hua §X1592–1596 leaves the morphism category implicit. This report supplies the qualification from frozen126(c). Context query: `foncteur|pour iso|simplement connexes`.

## E06 — An explicit model confirms the canonical universal-cover bundle

**Location:** scans127–128. **Actual check:** construction and descent argument under uniformization background.

Write X=D/Γ with D one of the simply connected uniformization models, and let ρ:Γ→PGL₂(C) be the extended deck action. Then

\[
P_X=(\mathbf P^1\times D)/\Gamma,\quad
\widetilde X=(D\times D)/\Gamma,\quad
\sigma(q(z))=[z,z],
\]

with diagonal action γ·(u,z)=(ρ(γ)u,γz). The map p([u,z])=(q(u),q(z)) has the required universal-cover fibers. The product horizontal distribution with u constant descends because ρ(γ) is independent of z. The diagonal section is transverse to that distribution. Isomorphism functoriality, not functoriality for arbitrary maps, is sufficient for this construction. Changing the chosen uniformization conjugates all data and gives the same object up to the corresponding canonical isomorphism.

The five-data uniqueness statement uses the universal-cover and transversality requirements, not arbitrary flat P¹ bundles with sections. It does not imply a unique projective connection on a fixed hyperbolic curve once the universal-cover condition is removed; the later ω² torsor parametrizes many projective connections.

**Context:** Hua §X1598–1610 restates this construction. This check supplies an explicit descent model and preserves the distinction between a marked and a horizontal section. Context query: `groupoïde|système local|revêtement universel|marquée`.

## E07 — The C-covered list and affine-versus-linear distinction

**Location:** scans129–130. **Actual check:** elementary deck-group argument; no new proof of uniformization.

A nonidentity affine automorphism z↦az+b with a≠1 has a fixed point. Deck transformations of a covering act freely, so all nontrivial deck transformations of C are translations. A discrete subgroup of the real two-dimensional additive group C is a lattice of rank0,1 or2; its quotients are C, C* and an elliptic curve. In the tangent-bundle model, the marked section is the zero section and the missing point in each projective fiber defines a horizontal infinity section. The horizontal distribution generally moves the zero section, so the connection preserves the affine structure, not the tangent bundle's vector-bundle origin. The distinction in frozen129 is mathematically necessary.

**Context:** Hua §X1612–1619 already presents this classification and affine description. The proof here is a limited elementary recheck. Context query: `translations|rang|elliptique|affines|vectorielle`.

## E08 — Explicit algebraic connections for A¹, G_m and an elliptic curve

**Location:** scans130 and132. **Actual check:** explicit algebraic construction and differentiation.

Choose a nonzero invariant differential η on the relevant one-dimensional algebraic group and use the invariant tangent-fiber coordinate w=η(v). On the tangent bundle define the horizontal distribution by

\[
dw+\eta=0.
\]

This is algebraic. Its vertical vector fields are translations, so it extends to the fiberwise projective completion, with infinity horizontal. The zero section is transverse. Rescaling η and w by the same nonzero constant leaves the distribution unchanged. The same construction applies to a torsor, since invariant differentials and translations do not require choosing an origin on the torsor.

| X | η and covering map p | Consequence |
|---|---|---|
| A¹, coordinate x | η=dx; p(x,w)=(x+w,x) | All displayed data, including p, are algebraic; the horizontal equation is dw+dx=0. |
| G_m, coordinate x | η=dx/x; p(x,w)=(x exp(w),x) | The projective bundle, connection, zero and infinity sections are algebraic; p is an analytic covering, not an algebraic map. Here w=v/x if v is the usual tangent coordinate. |
| Elliptic E | invariant η identifies Lie(E) with C; p(x,w)=(x+exp_E(w),x) | The same algebraic horizontal equation constructs the canonical affine connection. The exponential covering map is analytic. |

For G_m, d log(x exp w)=dx/x+dw, directly checking compatibility with the trivial connection on X×X. The local projective coordinate s=log x has

\[
G_x(s)=-2\frac{2/x^3}{1/x}+3\left(\frac{-1/x^2}{1/x}\right)^2=-\frac1{x^2}.
\]

Thus the corresponding quadratic differential is −(dx/x)² in the manuscript's normalization. This resolves the affine algebraicity question raised at130 for these explicit cases; it does not settle the general nonproper hyperbolic case.

**Context:** Hua §X1612–1619 leaves the G_m case at the same unfinished transition. The formula is an independent computation extending that account, not a claim read from the manuscript. Context query: `algébrique|mathbb.*C.*ast|mathbb.*G.*m|elliptique|affines`.

## E09 — Algebraic formal data do not make the covering map algebraic

**Location:** scans131–132. **Actual check:** explicit formal expansion and nonalgebraicity test.

For G_m the formal expansion x exp(w)=xΣwⁿ/n! belongs to C[x,x⁻¹][[w]], and its linear coefficient x is invertible. It therefore gives an isomorphism of the relevant formal completions over G_m, even though its analytic realization is transcendental. If the covering map were algebraic, its restriction to a fiber A¹→G_m would be algebraic; an algebraic map A¹→G_m is an invertible polynomial and hence constant, whereas exp is not. Likewise the elliptic exponential cannot be algebraic A¹→E: it would extend to P¹ by properness of E and then be constant, since no nonconstant map P¹→E exists. This check distinguishes algebraic formal series, algebraic bundles/connections, and algebraic maps of finite-type varieties.

**Context:** Hua §X1624–1634 retains the formal datum but does not spell out this distinction. Frozen132 itself only asserts algebraicity of p in the A¹ case. Context query: `formel|algébrique|prolonger|revêtement`.

## E10 — Deligne's theorem preserves the scan's qualification about σ

**Location:** scan131, enumerated a), b), c) and final insertion. **Actual check:** frozen-text comparison plus primary-source theorem verification.

Here c) is the section σ. The inserted “mais pas l’algéb. de c !” therefore denies that the cited result proves algebraicity of σ; it does not deny algebraicity of the connection, which is b). The page asserts existence and uniqueness of algebraic a), b), with regularity at infinity, and explicitly leaves the extra section out.

Deligne, *Équations différentielles à points singuliers réguliers*, LNM163(1970), **II, Theorem5.9, printed p97**, gives the equivalence between regular algebraic flat vector bundles and analytic flat vector bundles. A faithful algebraic representation with invariant tensors transfers the conclusion to the projective-group situation; the theorem is not stated as an algebraicity theorem for arbitrary nonhorizontal sections.

**Context:** Hua §X1628–1631 compresses this to “uniqueness / not existence of σ.” That is not a substitute for the exact frozen distinction: σ already exists analytically, and the question is its compatible algebraicity. Context query: `Deligne|algéb|section|régulière`.

## E11 — A transverse analytic section need not be algebraic in the regular model

**Location:** illustrates the gap explicitly recognized at131, not a counterexample to the canonical uniformizing construction. **Actual check:** countermodel.

Take the trivial algebraic P¹ bundle over A¹ with the trivial flat connection. The analytic section σ(x)=[1:eˣ] is everywhere transverse because d(eˣ)/dx=eˣ is nonzero, but is not algebraic: it takes values in the affine fiber chart and eˣ is not a polynomial/rational function. The flat bundle itself is regular and algebraic. Thus neither transversality nor algebraicity of the regular flat bundle forces the chosen section to be algebraic in that model.

This is deliberately **not** the canonical uniformizing section of A¹. It also does not show that every algebraic realization of the associated projective connection is impossible: G_x(eˣ)=1 is algebraic. A transcendental analytic gauge may relate different algebraic realizations, with different behavior at infinity. The counterexample isolates precisely why the section must be checked in the same algebraic regular model.

**Context:** reinforces the warning on131 and Hua §X1628–1631. Same-cote P05 already used eˣ for a different p-curvature countermodel; no p-curvature is recomputed or claimed here. Context query: `Deligne|exp|section|P05|algébrique`.

## E12 — The second-jet extension is an algebraic construction

**Location:** scan133. **Actual check:** exact-sequence calculation.

For a smooth relative curve, the diagonal ideal J satisfies J/J²≅ω and J²/J³≅ω². Tensoring the exact sequence

\[
0\to J^2/J^3\to J/J^3\to J/J^2\to0
\]

by ω⁻¹ gives exactly 0→ω→E→O_X→0 with E=(J/J³)⊗ω⁻¹. This checks the displayed extension without needing a square root of ω. The associated projective bundle is determined by second infinitesimal data; its normalization and section must be carried along rather than treating an arbitrary rank-two vector bundle as canonical.

**Context:** Hua §X1636–1655 gives the same construction. Direct published parallel: Deligne I§5.2–5.4, printed pp29–30, constructs the osculating projective line from second-order infinitesimal data. This is a published parallel with analytic scope, not a manuscript dating claim. Context query: `augmentation|J|oscul|extension|jets`.

## E13 — Third-jet torsor: correct once the global-connection constraint is retained

**Location:** scans133–134. **Actual check:** local jet calculation and scope check.

In a normalized local coordinate let q(z)=z+a z²+b z³+O(z⁴). The unique Möbius map fixing0, with first derivative1 and second coefficient a, is z/(1−az)=z+a z²+a²z³+O(z⁴). The free third coefficient is therefore b−a². Intrinsically, two third-order extensions of a fixed second-order isomorphism differ by a derivation with values in ω³, namely Hom(ω,ω³)≅ω². In this normalization G₀(0)=−b+a² and G(0)=−12(b−a²).

A single arbitrary formal isomorphism is not determined by its third jet: z and z+z⁴ have the same third jet. Frozen133 explicitly restricts to formal identifications for which transport of the tautological connection comes from a connection on the whole projective bundle. That restriction is essential in134's bijection. In characteristic zero, the Schwarzian differential equation with given coefficient and initial second-order data gives the formal prolongation recursively; this explains why the allowed third-jet datum determines the rest. The check here is local and characteristic zero, not an assertion over arbitrary positive-characteristic bases.

**Context:** Hua §X1636–1655 preserves the restriction. Deligne I§5.6bis, Proposition5.8 and §5.10, printed pp31–35, give the corresponding third-jet characterization and Ω² torsor. His formula5.9.2 is −G₀ in the current convention. At134, ω² lives on X; the literal phrase “torseur ... sur S” needs a relative interpretation or a separate pushforward. A global set of connections is a torsor under H⁰(X,ω²) only when it is nonempty. Context query: `ordre 3|torseur|Hom|jets|Schwarz`.

## E14 — The uniformizing choice is not holomorphic in arbitrary varying families

**Location:** question at114–115; relevant limitation on interpreting131–134 relatively. **Actual check:** verification against primary published research; not a new proof of the underlying theorem.

For closed marked curves of genus g≥2, the Fuchsian uniformizing projective structure defines a section of the affine bundle of projective structures over Teichmüller space. That section is real analytic and is not holomorphic. Zograf–Takhtadzhyan's1987 original /1988 English article identifies its antiholomorphic variation with the Weil–Petersson form. Loustau's2015 paper gives a direct geometric explanation: the Fuchsian slice is maximal totally real, as the image of the diagonal in T(S)×\overline{T(S)} under simultaneous uniformization. A holomorphic section of positive-dimensional T(S) could not have its image in a totally real submanifold while retaining p∘σ=id.

Thus fiberwise GAGA for a fixed compact curve must not be promoted into a holomorphic, and hence algebraic, canonical uniformizing section for every family. This does not say that every special or constant family fails, nor that projective connections in general lack holomorphic local sections.

**Context:** Hua §VIII “Le dictionnaire,”1374–1388 already states this obstruction, citing Zograf–Takhtadzhyan. This check verifies his substantive claim in the stated genus range and supplies exact primary locators. Context query: `famille|holomorphe|Zograf|Takht|Weil|uniformisation`.

## E15 — Context outside the supplied range cannot settle the arithmetic bridge

**Location:** overall interpretation, and continuation after134. **Actual check:** full-context scope comparison, not a new theorem.

All of Hua's source, including XI–XXI, was read. Those later interpretative sections discuss Gauss–Manin, stratifications, Cartier and p-curvature. They do not, solely by sharing the folder, identify the uniformizing projective connection of126–134 with a specified Gauss–Manin or Picard–Fuchs realization, and they do not establish its vanishing or nilpotent p-curvature. This agrees with same-cote P04–P09 and the explicit caution in `RESULTS_STATE`13–19.

Hua's discussion after our endpoint also requires care: for punctured curves, simple poles in the **difference** of projective connections require fixing the leading double-pole terms. “Regular singular” alone allows double poles. In particular, the ordinary projective connection restricted from P¹ is not the cuspidal uniformizing connection on P¹\{0,1,∞}: its projective monodromy is trivial, whereas the latter has nontrivial deck monodromy. This observation limits an apparent overstatement at Hua1692–1700; it is not a reading of unsupplied scan images and is not offered as a comprehensive review of the continuation.

**Context:** Hua VII–X supplies the projective strand; XI–XXI is context beyond our images. Same-cote P01,P03–P09 already insist on normalization, equivariance, an identified algebraic family, and zero-versus-nilpotent distinctions. Context query: `Picard|Gauss|Cartier|courbure|réguli|P04|P09`.

## Primary sources actually checked

1. **Pierre Deligne**, *Équations différentielles à points singuliers réguliers*, Lecture Notes in Mathematics163, Springer1970. [Author archive PDF](https://publications.ias.edu/sites/default/files/Number9.pdf). Read relevant extracted text at I§5.2–5.10, printed pp29–35, and II Theorem5.9, printed p97. Source refs: `turn890672764view0`, `turn196128359view0`, `turn505336028view0`, `turn505336028view1`. No external claim of arbitrary-base or positive-characteristic generality is drawn from these passages.
2. **P. G. Zograf and L. A. Takhtadzhyan**, “On uniformization of Riemann surfaces and the Weil-Petersson metric on Teichmüller and Schottky spaces,” Russian original1987; English *Math. USSR-Sbornik*60(2)(1988),297–313, DOI10.1070/SM1988v060n02ABEH003170. [Journal's primary abstract and bibliographic record](https://www.mathnet.ru/eng/sm1856). Abstract directly states the antiholomorphic-variation result. Full English PDF link redirected to the landing page; no claim to have read the full original proof. Ref `turn458554327view0`.
3. **Brice Loustau**, “The complex symplectic geometry of the deformation space of complex projective structures,” *Geometry & Topology*19(2015),1737–1775, DOI10.2140/gt.2015.19.1737. [Publisher PDF](https://msp.org/gt/2015/19-3/gt-v19-n3-p16-s.pdf). Read introduction p1738 and §6, especially Proposition6.4 and following paragraph on p1766, plus Theorem6.9 p1768. Ref `turn458554327view1`, `turn661828065view1`, `turn661828065view2`. Only the nonholomorphic conclusion and its geometric explanation are used; normalization constants are not imported.

## Reading questions retained for root

The invariant-metric parenthesis in126 needs its intended group specified. There is no positive Riemannian metric on P¹ invariant under all PGL₂(C): a stabilizing dilation rescales a nonzero tangent vector. A chosen compact rotation group admits a round metric up to scalar; these are distinct assertions. This is a mathematical reading question, not grounds to replace any frozen word. The torsor's base issue in134 is noted in E13. Root may keep these as separate notes.
