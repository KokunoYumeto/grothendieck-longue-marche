# Residue-characteristic-zero topos counterexample: draft under independent audit

17 November 2026. This is an attempted proof, **not yet promoted to a numbered Proved statement**. The main exact source input has been opened. Parent should adversarially inspect the clustered log-model lemma and passage to the entire small étale site.

## Candidate theorem

For any henselian discretely valued field (K,v) with residue characteristic zero, closed-point-preserving reconstruction fails, already for the normal finite-type scheme A1_K. In particular it fails for the explicitly unresolved field K_*=Q(t,sum t^(n!))^h from AS-FF.18. This would not decide B7, since centralizers of K_* are not established trivial.

Choose uniformizer t and λ=1+t. Extend the unique valuation to bar K. Define

f(a)=λa if v(a)>0, and f(a)=a if v(a)≤0; f(∞)=∞.

This is a G_K-equivariant bijection, preserves K(a) for every algebraic a, fixes 0,1,∞ and every nonzero rational number, and moves t. It is not an affine linear function. For every a≠b finite,

(f(a)-f(b))/(a-b) belongs to 1+m_(bar K).

Indeed it equals λ or 1 on the two same-region cases; in the crossing case v(a)>0≥v(b), the difference is changed by ta, of strictly larger valuation. All cross-ratios and 1 minus cross-ratios therefore have the same valuation and leading unit before and after f.

## Exact opened source input

Emmanuel Lepage, *Covers in p-adic analytic geometry and log covers I: Cospecialization of the (p')-tempered fundamental group for a family of curves*, Ann.Inst.Fourier63(2013),1427–1467, URL https://www.numdam.org/article/AIF_2013__63_4_1427_0.pdf . Local `sources/Lepage2013_log.pdf/.txt`.

- Theorem1.6, p1437: X log-regular fs; all primes in L invertible on X; restriction KCov(X)^L → Cov_alg(X^tr)^L is an equivalence.
- Theorem1.8, pp1438–1439: S noetherian henselian scheme with closed point s; connected fs log X with underlying X proper over S; restriction KCov(X) → KCov(X_s) is an equivalence.
- Corollary1.9 gives their combined application for proper log-smooth models over complete DVRs. We can use Thms1.6+1.8 directly over any henselian DVR, so completion is not needed.
- Take L=all primes, permissible since the entire valuation ring contains Q (residue characteristic zero). The equivalence therefore sees all finite covers, not only an l-primary or prime-to-p quotient.
- The same equivalence for X=Spec R, with its standard divisorial log structure, identifies KCov(s^log) with finite étale K-algebras. Thus an isomorphism over the fixed log point gives an equivalence over the entire BG_K, retaining arithmetic data.

## Clustered log-model lemma to prove carefully

Let S be a finite G_K-stable subset of P1(bar K) containing 0,1,∞. Choose finite Galois L/K splitting S. Let X_S/R_L be the stable marked genus-zero model; it exists by successive blowups of the coincident section closures followed by contraction of unstable components. Its total log structure is defined by the special fibre and all marks. Node equations have shape xy=u π^n. This is log regular (toric node), and it is proper over the henselian DVR R_L.

Claim: f supplies a canonical isomorphism of the log special fibres

(X_S)_s^log ≅ (X_f(S))_s^log

over s_L^log, respecting the labelled marks; these commute with forgetting marks and with finite extension of L, and are Gal(L/K)-equivariant.

Proposed proof: The marked special fibre is the tree of clusters, i.e. the rooted finite subtree of closed balls spanned by S. The vertices carry P1 over the residue field, with the marked/node locations determined by residues of normalized differences; edge thicknesses are differences of valuations. Because every difference changes by a principal unit, f induces the same cluster tree, edge lengths and residue configurations. The unique isomorphism on each stable component (at least three special points) respects all marks/nodes. At a node, the log structure over s_L is fixed by its thickness n and the leading unit bar u in xy=uπ^n. Such a u can be computed from an adjacent quadruple of marked points, through its cross-ratio. The transformed cross-ratio has ratio in 1+m_L, so the leading unit is unchanged, with tangent vectors transported by the component isomorphisms. Hence the component maps glue to a log isomorphism over the unchanged log point. A log lift is unique: at a node, a possible change of the two generators by units u1,u2 must fix x,y and satisfy u1u2=1; in κ[x,y]/(xy) this forces u1=u2=1. On the smooth locus the vertical generator is fixed by the log base, and any horizontal generator is determined by its non-zero-divisor local parameter. Thus uniqueness gives Galois equivariance and compatibility with all contractions and base changes, or these can be checked directly on the same cluster charts.

Potential concern to audit: in proving uniqueness of node log lift, more general log-automorphisms whose characteristic map is fixed might have units with nontrivial components killed by x or y; the base-product relation seems to eliminate them because (x)∩(y)=0 in the reduced nodal local ring. Need verify global chart and thickness n as well. Compatibility with contractions may involve non-isomorphism log maps; use explicit cluster charts rather than only the uniqueness assertion if needed.

## From log fibres to compatible punctured-cover categories

For each S, Thms1.6+1.8 and the preceding log isomorphism give an equivalence

FEt(P1_L−S) ≅ FEt(P1_L−f(S)),

compatible with inclusions S⊂T, finite constant extensions and Gal(L/K). Effective finite étale descent gives the equivalence over K, over FEt(K). Log mark compatibility preserves the full cusp decomposition and inertia groups, with the same residue field K(a). In particular it preserves which branches of a finite cover are unramified over a marked point.

## From those categories to the whole étale site

It is insufficient merely to assert that finite étale categories for individual opens are equivalent. Here the directed compatibility and cusp pairs supply the missing information.

Any quasi-compact separated étale V→P1_K is an open subscheme of its finite normal compactification Vbar→P1_K, by Zariski Main and normalization. The finite compactification is generically étale and is a finite étale cover over P1−S for some finite S. Transport that cover, then normalize P1 in the transported finite separable generic algebra. The cusp decomposition/inertia data identify the points over each a∈S and preserve their residue fields and ramification. Consequently the deleted finite set Vbar−V can be transported, and the resulting open is again étale. The construction is independent of enlarging S by the restriction compatibility above. Maps between these étale objects are maps of their generic finite algebras extending to normal compactifications, with the condition on the retained point sets; all of this is preserved. Covering families are characterized by surjectivity on geometric points, also preserved. Thus the construction is an equivalence of a generating small étale site, yielding a pinned K-relative autoequivalence of (P1_K)_et with point function f. Since ∞ is fixed it restricts to (A1_K)_et.

If that equivalence were induced by a K-morphism A1→A1, it would be a scheme automorphism by full faithfulness on scheme morphisms (or by the point bijection and a polynomial degree argument in characteristic zero). Such an automorphism has shape aT+b. It fixes 0 and1, hence is the identity, contradicting f(t)=(1+t)t≠t. More directly, any polynomial agreeing with f on the infinitely many nonzero rational units is the identity, with the same contradiction. Universal-homeomorphism localization changes nothing because A1 is normal in characteristic zero.

## Remaining B7 obstacle

The argument, if correct, proves a counterexample to reconstruction for K_* but does not establish its centralizer condition. A possible B7 route is to choose a rational-coefficient formal series u(t) whose formal arc has no nontrivial algebraic self-correspondence tangent to identity, simultaneously after finite Puiseux extension. Then K=Q(t,u)^h would have trivial centralizers for every finite E/K (number-field residue rigidity and G_K=Zhat(1)⋊G_Q reduce a centralizer to such an infinitesimal formal self-correspondence). Establishing existence rigorously requires a separate generic-arc lemma; not proved here. The specific factorial series has t→−t,u→u−2t symmetry, whose leading coefficient −1 acts nontrivially on Galois groups, so it does not itself violate the proposed centralizer condition.
