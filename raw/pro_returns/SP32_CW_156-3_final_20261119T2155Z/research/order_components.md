# Research draft: order, components, and subdivision algebras

Research by `/root/order_components`, after the root's transcription freeze. No scan was opened, no OCR was used, no frozen transcription or apparatus was altered, and no external literature was consulted. `RESULTS_STATE.md` was read first. All references to the definition on scan009 are to the **report** in `SP32_CW_156-3_sweep3/readings/156-3.md`, §1.2; scan009 is outside the supplied sixteen images and was not independently read here.

The conclusions below distinguish (i) the frozen text, (ii) a mathematically corrected interpretation, and (iii) the restricted theorem for a dense **total** order. In particular the sweep's claims about arbitrary tronçons do not receive a blanket endorsement.

## Concise research items

### ORD-01 — Absolute endpoints of rays

**Scan:** 026, absolute-boundary display. **Kind:** unproved claim / own counterexample. **Quote:** “bord absolu”; `∂L_{≥a}=∂L_{≤a}={a}`. **Confidence:** high, direct finite endpoint calculation. **Context:** sweep `readings/156-3.md`, §1.6, compresses the boundary definitions without checking this equation; Esquisse API transcription, `119/35`, uses a different tubular-boundary construction. **RESULTS_STATE:** no entry settles this elementary endpoint issue; the comparison does not alter INTAKE 20261114 §13.2.

With `L=[0,1]` and `a=1/2`, the absolute endpoints are `∂L_{≥a}={a,1}` and `∂L_{≤a}={0,a}`, so the displayed singleton equation needs exclusion of inherited ambient endpoints or a switch to relative frontier. This is a mathematical correction only and must not replace the frozen ink. The boxed **disjoint** union later on the page works for nondegenerate real intervals, but extending it to the pseudo-tronçon `{0}` would count `0` twice under the frontier definition of030; that is an exception to check, not an asserted error if its variable is restricted to nondegenerate tronçons.

### ORD-02 — The closed hull is not unique under the reported general axioms

**Scans:** 026 lower margin; 027 definition of `∂T′`; consequences for033(6). **Kind:** unproved claim / own counterexample. **Quote:** “Cette écriture est unique”; “le … plus petit fermé”; `∂T′=∂T`. **Confidence:** high under the sweep's stated definition of tronçon. **Context:** sweep §1.2 admits doubled lines and §1.5 reports their failure of T0; §1.6 leaves the non-total axioms unproved. **RESULTS_STATE:** adds an explicit obstruction to the axiomatic programme described by MPL_150_044-084 Q9 and WG2 B15 (§1.2), without changing either register status.

In the admissible doubled order `L=Q×{0,1}`, where `(q,i)<(r,j)` means `q<r`, the twins `a=(0,0)` and `b=(0,1)` give the same subset `T=L_{<a}=L_{<b}` but two incomparable closed hull candidates `L_{≤a}` and `L_{≤b}`. Thus the asserted unique presentation and the definition of the boundary through that presentation require additional hypotheses or decorated subsets. Moreover `T` has **no least closed moderate superset**, even among finite unions of closed pseudo-tronçons, so the later closure axiom is not justified for this reported general class. Appendix A proves this, while Appendix B strengthens the no-least-hull obstruction to an admissible T0 example whose ray presentation is unique.

### ORD-03 — Intersection with comparable endpoint data

**Scan:** 028 opening proposition. **Kind:** unproved claim, checked. **Quote:** “Immédiat”; `∂(T∩T′)⊂∂T∪∂T′`. **Context:** sweep §1.4 / SA21-R3-05 verifies the closed version at018; this page adds the open/half-open endpoint cases. **RESULTS_STATE:** none directly; no finite-poset realization result is needed.

For two interval presentations whose endpoint data lie in one chain, take the larger lower endpoint and the smaller upper endpoint, and exclude an endpoint whenever either factor excludes it. The intersection is empty, a singleton, or the corresponding pseudo-tronçon, and its endpoint set uses only endpoints already present. This proves the displayed claim for fixed compatible endpoint data; it does not cure ORD-02's ambiguity in assigning such data to a subset in an arbitrary tronçon.

### ORD-04 — Pointwise precedence does not force moderate position

**Scan:** 028 margin; also033(2). **Kind:** unproved claim / own counterexample. **Quote:** “Ça implique … en pos. rel. mod”; “pas l'inclusion!”. **Confidence:** high, explicit T0 example. **Context:** sweep §1.6 repeats the implication without checking it; this refines the sweep's statement that the general axioms remain open. **RESULTS_STATE:** bears on the generality of WG2 B15, not on its finite-poset theorem.

Use `R²` with the **strict-coordinate** order `p<q` iff both coordinates strictly increase, adding equality for `≤`; this is a T0 tronçon under the reported axioms. For `a=(0,0)`, `b=(0,1)`, every point of `T=L_{<a}` is below the sole point of `T′={b}`, but their boundaries `{a}` and `{b}` are incomparable. The same example gives `L_{<a}⊂L_{<b}` with incompatible boundaries, contradicting033(2) in this concrete model. Thus T0 alone cannot repair the model; Appendix B supplies the axiom checks.

### ORD-05 — Interstitial intervals require the stated actual suprema and infima

**Scan:** 029 proposition and description of `S`; relation to028. **Kind:** unproved claim, conditional proof / reading question. **Quote:** “si a=Sup T, b=Inf T′”; “ce … S est unique”; “S est formé des x”. **Confidence:** high, after root's independent hypothesis check. **Context:** sweep §1.6 / SA21-R3-09 proves only the total-order version and flags a doubled-point obstruction; the latter must not be mistaken for a refutation under actual-Sup/Inf hypotheses. **RESULTS_STATE:** no listed result settles this interval statement.

Under the explicitly stated hypothesis that `a=sup T` and `b=inf T′` really exist, a separator `x` must satisfy `a≤x≤b`, and conversely those interval points separate exactly after omitting an endpoint occupied by a neighbouring interval. This proves the corrected separator formula, nonempty interstice, and uniqueness in the partial-order setting too, with divisibility supplying an interior point when `a<b`; the frozen first lower-cone variable is instead a literal `a`, a separate reading question. The strong-coordinate rays `T=L_{<(0,0)}`, `T′=L_{>(1,1)}` have no actual supremum/infimum, although they have named boundary endpoints: their separator set is the ordinary closed square, larger than the proposed pseudo-tronçon. Thus that example refutes the **unchecked extension from boundedness to endpoint extrema**, not029's conditional theorem.

### ORD-06 — Uniqueness of separated interval components

**Scan:** 030, injectivity proposition. **Kind:** unproved claim, checked under totality. **Quote:** “est injective”; “NB réunion disjointe”. **Context:** sweep §1.4 / SA21-R3-06 discusses the closed version at019; §1.6 gives this extension. **RESULTS_STATE:** no entry directly; complements the meaning of components without importing STRATA A.4.

For a dense total order, a finite `≪`-separated family consists exactly of the maximal nonempty order-convex subsets of its union: a separator outside the union prevents any convex subset from meeting two members. Its union therefore determines the family, including open, half-open and singleton members, and the empty family gives the empty set. This is an intrinsic order-convex decomposition and does not assert connectedness in the ordinary topology.

### ORD-07 — “Connected” is explicitly relative to the moderate algebra

**Scans:** 030 lower margin; 038–039. **Kind:** unpursued implication / checked distinction. **Quote:** “mais pas pour la top canonique”; “adh … au sens modéré bien sûr!”. **Context:** sweep §1.4 / SA21-R3-06 already warns about `Q`, and §1.7 / SA21-R3-13 uses the combinatorial meaning. **RESULTS_STATE:** differs from STRATA A.4 / A.12 and BISITE G.10, whose strata are realized topological spaces; also does not identify the components in Esquisse API `119/33`'s isomorphism spaces.

For `L=Q`, the order interval `[0,1]∩Q` is one moderate component but is topologically disconnected, for example by an irrational cut in `(0,1)`. That cut is not a moderate subset with endpoints in `Q`, which explains why it does not split the component in the manuscript's algebra. The page's warning is therefore substantive and should accompany any use of `Π₀` in a topological or exit-category comparison.

### ORD-08 — Complement count, strict endpoint bounds, and the empty set

**Scans:** 031–032. **Kind:** unproved claim, checked / reading question. **Quote:** “les n−1 tronçons interstitiels”; `|Card Π₀(X)−Card Π₀(X′)|≤1`. **Context:** sweep §1.6 / SA21-R3-10, SA21-K3-03. **RESULTS_STATE:** no listed statement directly; this is a one-dimensional test relevant to WG2 B15.

In a dense total order and for `n≥1`, the exact formula is `n′=n−1+ℓ+r`, where `ℓ,r∈{0,1}` say whether the strict left and right exterior interstices are nonempty. Hence “minoré/majoré” must be understood as admitting the required **strict** exterior bound, and the frozen first “non majoré” has to be distinguished from the mathematically expected “non minoré”. The sweep's qualifier that the count “fails for n=0” is too strong: `X=∅` has `X′=L`, so `n′=1` and the displayed absolute-difference bound—and even membership in `{n−1,n,n+1}`—remain true. Only the case division involving nonexistent `T₁,T_n` is unavailable at `n=0`.

### ORD-09 — The proposed meet test fails for every incomparable pair of points

**Scan:** 032 margin. **Kind:** self-flagged conjecture / own refutation of the proposed test. **Quote:** “p.ex. {X,Y} mod ssi X∧Y existe ???”. **Confidence:** high. **Context:** sweep §1.6 / SA21-R3-11 and SA21-K3-07; the corrected proof is simpler and avoids its inadmissible ordinary-product example. **RESULTS_STATE:** no entry settles order-definability of this compatibility relation.

For incomparable points `a,b`, the moderate singleton subsets `X={a}`, `Y={b}` have the meet `∅` in the inclusion order, but their boundary union `{a,b}` is not a chain. The strong-coordinate model of Appendix B gives a concrete admissible T0 example with unambiguous singleton boundaries. This refutes only the suggested **meet-existence test**, not the larger question whether compatibility can be defined from the entire ordered structure by some subtler formula.

### ORD-10 — The sweep's ordinary product order is not an admissible test model

**Scan:** mathematical context for032. **Kind:** own check of supplied research context. **Confidence:** high, two-element cone obstruction. **Context:** sweep `readings/156-3.md`, §1.2 and §1.6 / SA21-R3-11; `STUDY.md`, §156-3, point1. **RESULTS_STATE:** no entry establishes this model claim.

For the ordinary coordinatewise product order on `R²`, both `(1,0)` and `(0,1)` lie strictly above `(0,0)`, yet any common lower bound still above `(0,0)` would have to be `(0,0)` itself, a contradiction. Its strict upper cone is therefore not downward directed, contrary to the tronçon axiom as the sweep reports it. The sweep's desired refutation of the meet test is preserved by ORD-09, but its example and any downstream use of that model require replacement by a genuinely admissible order.

### ORD-11 — The finite-clopen hypothesis is conditional

**Scan:** 038 opening continuation of037. **Kind:** unproved claim, conditional check. **Quote:** “de Boole en question est finie”; “X≠∅ minimaux”. **Context:** sweep §1.7; Esquisse API `119/32–34` gives a programme of axioms rather than this finite-algebra identification. **RESULTS_STATE:** no entry discharges037's preceding compatibility expectation.

If the clopen elements do form a finite Boolean algebra, its nonzero minimal elements are its atoms and every element is their unique disjoint join; this proves the finite statement. It does not prove that arbitrary clopens are compatible with all elements, which037 expressly leaves as “On s'attend”. The empty algebra case `0=1` has no nonzero atoms and must be kept separate.

### ORD-12 — Components of a moderate subset of a dense total order

**Scans:** 038–039. **Kind:** unproved claim, independently checked under totality. **Quote:** “Je dis”; “il suffit donc de prouver”; “C'est immédiat”; “OK”. **Context:** sweep §1.7 / SA21-R3-13. **RESULTS_STATE:** restates the elementary finite decomposition independently of STRATA's realization results; it does not establish a general exit interpretation.

For `A=⋃T_i` in separated normal form, `cl_mod(T_i)∩A=T_i`, because any omitted endpoint lying in another component would cause a forbidden raccordement. Thus each `T_i` is closed in `A`, and the finite union of the other closed components makes it open as well. A nontrivial moderate clopen partition of one `T_i` would have a transition endpoint inside that order interval and hence a nonempty relative frontier, impossible for a clopen partition. Therefore the `T_i` are exactly the atoms of the relative clopen algebra in the dense total-order setting; ORD-02/04 prevent exporting this proof to all reported tronçons without further hypotheses.

### ORD-13 — A finite generator family need not generate the whole subdivision algebra

**Scan:** 040. **Kind:** unproved claim / own counterexample. **Quote:** “l'Alg. de Boole engendrée par les Xα”; “composants”; “connue quand on connait S”. **Confidence:** high; exact finite certificate provided. **Context:** sweep §1.7 repeats the statement, replacing the live “composants” with “atoms”, and flags only the interval-index slip SA21-K3-04. **RESULTS_STATE:** limits a proposed connection to WG2 B15 and MPL_121_049-073+153+155 R121-08; those entries do not establish this claim.

For the single generator `X=(0,1)⊂R`, the generated ordinary Boolean algebra has only `∅,X,R\X,R`, whereas the five listed endpoint cells generate an algebra with 32 elements. Calling them “composants” does not fix the statement under038–039's notion: the components of `R\X` are the **closed** rays `(-∞,0]` and `[1,∞)`, not the endpoint singletons and open rays separately. Moreover `(0,1)` and `[0,1]` have the same frontier set `{0,1}` but generate different subalgebras, so that frontier set does not determine the generated subalgebra. This is separate from the literal interval `]t₁,t₃[` after `{t₂}`, whose corrected `]t₂,t₃[` still does not solve the algebra problem.

### ORD-14 — What the endpoint set does canonically determine

**Scan:** 040. **Kind:** own corrected formulation / unpursued implication. **Quote:** “décomposition … ou subdivision”. **Confidence:** high for dense total orders. **Context:** sweep `readings/156-7.md`, scans072–073 report support algebras relative to a chosen chain; Esquisse API `119/32–34` describes axiom tests on concrete models. **RESULTS_STATE:** bears on WG2 B15 (§1.2); it provides a finite algebraic test, not a proof of the programme for the real line.

For a finite cut set `S={t₁<…<t_n}`, let `B_S` be **all unions of the nonempty cells** consisting of the points, intervening open intervals, and the two exterior rays when present. Then every moderate set whose frontier lies in `S` belongs to `B_S`, so the algebra generated by the `Xα` is a subalgebra of `B_S`, possibly proper. For `n≥1` the number of atoms of `B_S` is `2n−1+ℓ+r`, and its size is `2^(2n−1+ℓ+r)`; for `S=∅`, it is `{∅,L}`. Closure alone need not generate `B_S` from the `Xα`: reflection symmetry already prevents `(0,1)` from distinguishing its two endpoints.

### ORD-15 — Closure and incidence are extra data beyond a finite Boolean algebra

**Scans:** 039–040. **Kind:** own idea / unpursued implication. **Confidence:** high for the finite interval construction, low for any global extension. **Context:** Esquisse API `119/58–59` retains junction maps and ordered/category objects; `RESULTS_STATE.md`, MPL_121_049-073+153+155 R121-08, STRATA 0.1, STRATA A.4, BISITE G.10, and WG2 B15. **Relation:** these pages add an elementary finite test; they do not restate or prove the cited geometric results.

On `B_S`, the moderate closure of an interval atom adds its incident endpoint atoms, thereby recovering the finite incidence relation that the abstract Boolean algebra alone forgets. Ordering interval cells below their incident point cells makes saturated open unions into downsets, matching the variance recorded in STRATA 0.1 before any geometric realization comparison is attempted. This suggests comparing the **Boolean algebra with closure and refinement maps**, rather than the bare generated algebra, with the finite-poset side of WG2 B15. It supplies neither links nor junction maps, the additional information explicitly retained in Esquisse `119/58–59` and stressed by R121-08.

## Appendix A — A doubled tronçon and failure of least closed hull

Let `L=Q×{0,1}` with `(q,i)≤(r,j)` precisely if the points are equal or `q<r`. It is a partial order; any two points have a common strict upper bound and a common strict lower bound by choosing a rational coordinate above or below both. If `u,v>a`, choose a rational coordinate strictly between that of `a` and the smaller coordinate of `u,v`; either point over it is a lower bound of `u,v` lying in `L_{>a}`. The dual verifies the strict lower-cone condition, and a rational midpoint proves divisibility. Thus it satisfies every axiom listed in the sweep's report of009.

Take `a=(0,0)`, `b=(0,1)`. Put `T={ (q,i):q<0 }`, `C_a=T∪{a}`, `C_b=T∪{b}`. Both `C_a=L_{≤a}` and `C_b=L_{≤b}` are closed sub-tronçons, and `T=C_a\{a}=C_b\{b}`. They are incomparable by inclusion; their intersection is exactly `T`.

Suppose a least closed moderate superset `Z` of `T` existed. It would lie in both `C_a,C_b`, hence `Z=T`. But every closed pseudo-tronçon contained in `T` has a greatest endpoint with rational coordinate strictly less than zero; a finite union of such pieces is bounded above by the largest of finitely many negative endpoint coordinates, whereas `T` is cofinal below zero. Thus `T` cannot itself be a closed moderate set, contradiction. This proof checks the failure of033(6) as a model claim without requiring a choice of boundary for arbitrary open sets.

The strict cones of the twins coincide, so the canonical basic opens contain both or neither; this also rechecks the sweep's non-T0 observation, but the new issue here is failure of the algebraic hull.

## Appendix B — An admissible T0 non-total order and two failures

On `L=R²`, define `p<q` iff `p₁<q₁` **and** `p₂<q₂`; define `p≤q` iff `p=q` or `p<q`. This is **not** the ordinary coordinatewise product order. Global directedness follows by choosing coordinatewise bounds with a positive margin. For `u,v>a`, choose `w_i` strictly between `a_i` and `min(u_i,v_i)`; then `a<w<u,v`, giving the strict-cone filteredness required in the report of009. The lower-cone condition is dual and midpoints prove density.

The open interval `]a,b[` is the ordinary open rectangle `(a₁,b₁)×(a₂,b₂)`, so these intervals give the Euclidean topology. In particular the canonical topology is T0 (indeed Hausdorff), and the counterexamples below are not failures of topological separation.

For `a=(0,0)`, `b=(0,1)`, the lower cones satisfy `L_{<a}⊂L_{<b}`, yet the endpoints are incomparable. Both rays have unique endpoint presentations, so the ambiguity in Appendix A is irrelevant. This refutes the concrete inclusion⇒moderateness claim033(2). Every `t∈L_{<a}` also satisfies `t<b`, giving the failure of the implication in028's margin.

The ray `T=L_{<a}` nevertheless has no least closed moderate hull. Both `C_a=L_{≤a}` and `C_b=L_{≤b}` contain it, but `C_a∩C_b=T`, since the point `a` is not below `b` in this strict-coordinate order. Every closed pseudo-tronçon contained in `T` has a finite greatest endpoint with both coordinates negative: an unbounded upper ray or all of `L` cannot lie in `T`. A finite union of such pieces misses points of `T` sufficiently close to `(0,0)`. Therefore `T` is not a finite union of closed pseudo-tronçons, so no least closed moderate superset exists. This strengthens the closure obstruction to a T0 model; **unique endpoint presentation does not imply least closed hull**.

For incomparable singleton sets `{a},{b}`, their intersection is empty and therefore is their meet in **any** subset family containing them and the empty set, including the manuscript's proposed `Mod(L)`. Their boundaries are the incomparable points themselves, refuting032's meet criterion independently of operations on any larger sets.

For the interstitial formula, put `c=(1,1)`, `T=L_{<a}`, `T′=L_{>c}`. A point `x` is above every `t∈T` exactly when its two coordinates are at least zero, and it is below every `t′∈T′` exactly when its two coordinates are at most one. Thus the separator set is the ordinary closed square. The pseudo-tronçon `[a,c]` in the defined order is `{a,c}∪((0,1)×(0,1))`, excluding all other edge points. **This is not a counterexample to029 under its actual-Sup/Inf hypothesis:** `T` has no supremum and `T′` has no infimum, since coordinate-edge bounds such as `(0,1)` prevent the named corner from being least or greatest among bounds. It shows why028 cannot assume that being bounded by another pseudo-tronçon supplies those extrema.

For completeness, under actual extrema the proof is direct in a partial order: if `T<T′`, every `t′` is an upper bound of `T`, whence `a≤t′` for every `t′`, and thus `a≤b`. The separator set is `[a,b]` minus `a` when `a∈T` and minus `b` when `b∈T′`; the forward inclusion follows from the extremal property, and the reverse inclusion from transitivity, with equality excluded precisely at occupied endpoints. When `a<b`, divisibility gives a point strictly between them; when `a=b`, non-raccordement means neither neighbour occupies it. The prescribed raccordements force these endpoints and their occupancy, hence uniqueness. This does not establish that every bounded open pseudo-tronçon in the reported general class has an actual extremum.

## Appendix C — Exact total-order component and complement arguments

Let `L` be a dense linearly ordered set with more than one point, permitting a minimum and/or maximum. A pseudo-tronçon is a nonempty interval whose finite endpoints belong to `L`, with either endpoint included or excluded as appropriate, or a singleton. Finite unions have a unique normal form obtained by merging overlapping intervals and raccording intervals, leaving components separated by at least one omitted point. Maximality among convex subsets proves uniqueness without ordinary topological connectedness.

For nonempty normal form `T₁≪…≪T_n`, the complement consists of the `n−1` nonempty interstices and whichever exterior interstices are nonempty. The interstice between `T_i,T_{i+1}` is the interval from the upper endpoint of the first to the lower endpoint of the second, with endpoint inclusion opposite to that of its neighbouring component. Density makes it nonempty when the endpoints differ; if they agree, both neighbours must omit the common point and the interstice is that singleton. Therefore `n′=n−1+ℓ+r` and `|n−n′|≤1`.

For `X=∅`, the complement is `L`, with one component; the inequality and the three-value range are still true. For a bounded ambient interval, merely being bounded below does not imply a left interstice: `X=L=[0,1]` has none. The correct condition is existence of a **strict lower bound of all its points inside L**, exactly the exterior condition emphasized by029's “minorants stricts”.

Moderate closure in a total order fills the omitted endpoints of each component and then merges any components that now raccord; it remains a finite interval union. For a component `T_i` of `A`, its newly added endpoints cannot already be in `A`, otherwise its original separation from its neighbour would fail. Hence the relative closure leaves `T_i` fixed; all other components are likewise relatively closed and their finite union proves relative openness. A nonempty proper clopen moderate subset of an interval would require at least one finite endpoint of change inside the interval; density puts that endpoint in both relative closures, contradicting clopenness. This proves038–039 in the stated total-order setting.

## Appendix D — Finite certificate for040

`research/check_subdivision_algebra.py` was run successfully. It represents the five cells of `R` cut at `0<1` as a five-element set and uses the exact usual closure rule (an interval cell adds its adjacent endpoint cells). Starting from `X=(0,1)` it finds:

| Operations admitted | Number of elements | Distinguishes `{0}` from `{1}`? |
|---|---:|---|
| Boolean operations | 4 | No |
| Boolean operations and closure | 8 | No |
| Boolean operations, closure, and taking moderate components | 32 | Yes |

The middle obstruction also follows without computation from reflection symmetry `x↦1−x`, which commutes with Boolean operations and closure. The final computation is a certificate for this example, not a claim that every proposed general partial algebra admits those operations. For a finite family of sets in a dense total order, the ordinary generated Boolean atoms are the nonempty **membership-vector classes**; each such atom can be a union of several endpoint cells, so the canonical cut subdivision is generally a refinement.

## Register-use limits

No open item in the supplied RESULTS_STATE is solved by these checks. STRATA 0.1, STRATA A.4/A.12, BISITE G.10, WG2 B15, MPL_121_049-073+153+155 R121-08, MPL_150_044-084 Q9, and INTAKE 20261114 §13.2 were used only at the level actually reproduced in RESULTS_STATE; their underlying return files are not supplied. The mathematical proofs above are local checks of the present pages and of explicit examples, not independent verification of those register statements. The Esquisse transcription is an unchecked API transcription, used as contextual wording only.
