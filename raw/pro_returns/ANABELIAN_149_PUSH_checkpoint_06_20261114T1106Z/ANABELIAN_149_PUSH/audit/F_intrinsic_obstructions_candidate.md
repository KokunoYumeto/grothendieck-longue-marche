# Intrinsic necessary conditions and negative field families

Status: independently reviewed and approved by root and the finite-field agent; integrated as F.38–F.41 in sections/F.tex, with result/source ledgers synchronized. The finite-extension proof uses discreteness specifically for the finite étale slice. The intrinsic converse in F.9 remains unresolved.

Throughout, reconstruction means the actual Carlson–Haine–Wolf closed-point-preserving relative small-étale-topos property, with the specified structural isomorphism over BG_k included in the object and retained under isomorphism. Characteristic is zero.

## A. Finite-extension invariance

If E/k is finite, k satisfies reconstruction if and only if E does. The implication from E to k is F.32. For the other implication, regard finite-type E-schemes X,Y as finite-type k-schemes. A pinned morphism phi:X_et→Y_et over BG_E is also a pinned morphism over BG_k. Reconstruction over k gives a unique k-map f:X^awn→Y and a relative isomorphism to phi_et.

The two algebraic maps X^awn→Spec(E), namely the given structure and the composite with f, induce isomorphic relative topos maps over BG_k, since phi is over BG_E. Faithfulness over k makes the algebraic maps equal. Thus f is E-linear. The comparison isomorphism is also over BG_E: the finite étale object Spec(E) over BG_k, and its distinguished sections on X and Y, present BG_E as the corresponding slice. Naturality of the BG_k-relative comparison preserves these sections. Equivalently, CHW's rigidity of pinned relative morphisms makes the structural comparison with Spec(E) unique, so the required compatibility cannot differ by another 2-cell. Absolute weak normalization is intrinsic to the scheme and does not depend on regarding it as a k-scheme or an E-scheme.

This proves both fullness and faithfulness over E. It does not assert ascent through infinite algebraic extensions; Q→Qbar already shows why that stronger assertion would be false.

## B. Central structural twists force slimness

Fix a separable closure kbar and z in the centre of G_k. Let X=Gm_k and p:X_et→BG_k. On any continuous discrete G_k-set S, the rule s↦z s is G_k-equivariant because z is central. It is natural in S and gives a natural automorphism of the identity functor of BG_k, hence of the structural pullback p*. Use it (or its inverse, according to the convention for the structural 2-cell) to equip the underlying identity geometric morphism of X_et with a new relative structure theta_z. The underlying map of topological spaces is the identity, so theta_z preserves every closed point.

The relative geometric point function of theta_z is

    X(kbar) → X(kbar),  a ↦ z(a),

after choosing the inverse convention just indicated. This is an actual statement about the relative 2-isomorphism classes, not merely an informal action on stalks. To check it, put a in a finite Galois extension E/k. The finite constant object is the G_k-set Hom_k(E,kbar). The structural twist acts on its embeddings by iota↦z∘iota. Slicing the relative point at this object changes precisely the residue embedding by z. CHW Proposition 3.6 identifies relative pinned point-source morphisms Spec(kbar)_et→X_et with X(kbar), so the changed embedding is the point z(a). In particular the two relative point morphisms can be isomorphic only when z(a)=a.

Every k-point is fixed. If theta_z were induced by an algebraic k-map X→X, that map would be t↦c t^m with c∈k*, m∈Z. Its values at 1 and 2 force c=1 and m=1. It would therefore fix every geometric point. If z≠1, choose a∈kbar* with z(a)≠a, a contradiction.

A global natural automorphism cannot erase this obstruction in the relative 2-isomorphism quotient: its pullback to the chosen geometric point would identify the two distinct relative point-source morphisms just distinguished by Proposition 3.6. No computation of the automorphism group of the entire étale topos is assumed.

Thus reconstruction implies Z(G_k)=1. By A, it also implies Z(G_E)=1 for every finite E/k; equivalently, G_k is slim (every open subgroup is centre-free).

## C. Kernel of the action of field automorphisms

There is a natural homomorphism Aut(k)→Out(G_k). Extend a field automorphism sigma to kbar; conjugation gives the continuous automorphism of G_k. Another extension differs by an element of G_k, so the outer class is well defined.

Suppose sigma≠1 has trivial outer action. The corresponding geometric automorphism of BG_k is naturally isomorphic to the identity: if the chosen group automorphism is conjugation by g, the standard natural equivalence of the restriction functors is given by g on continuous G_k-sets. Hence the absolute scheme automorphism f_sigma of Gm_k defined by

    f_sigma^#: k[t,t^-1]→k[t,t^-1],  c↦sigma(c), t↦t,

becomes a geometric morphism of the full small étale topoi relative to BG_k after composing its structural map with this natural isomorphism. It is closed-point preserving because f_sigma is an isomorphism of schemes.

On rational points its map is a↦sigma^(-1)(a): pull back the maximal ideal (t-b) and compare with (t-a). This rational point function is independent of the chosen inner conjugator, because the rational closed point has a unique relative point-source structure over k up to the prescribed relative isomorphism. Any algebraic k-map inducing this relative geometric morphism is a monomial c t^m. Its values at 1 and 2 force c=1, m=1, contradicting any a moved by sigma.

Consequently reconstruction implies injectivity of Aut(k)→Out(G_k), and by A the same for every finite E/k. Combining this with B gives the equivalent stronger-looking necessary formulation

    C_{Aut(kbar)}(G_E) = {1}  for every finite E/k.

Indeed a commuting field automorphism of kbar preserves the fixed field E, its restriction acts trivially in Out(G_E), and injectivity forces that restriction to be the identity; it then lies in Z(G_E), which is trivial. Conversely the centralizer formulation separately rules out the centre and any inner-trivial automorphism by adjusting an extension by the inner conjugator. These conditions are not asserted sufficient.

## D. Algebraically closed, real-closed and finite-Galois-group exclusions

Every algebraically closed characteristic-zero field K has a nonidentity automorphism. Choose Qbar inside K, extend the nontrivial automorphism of Q(sqrt(2)) to Qbar, fix a transcendence basis of K/Qbar, and extend to the algebraic closure K. Since G_K is trivial, C excludes K.

If G_k is finite, its separable closure is a finite algebraically closed extension in characteristic zero. A would force that extension to reconstruct, contrary to the preceding paragraph. Hence a reconstruction field has infinite absolute Galois group. In particular every real-closed field fails: its algebraic closure k(i) has degree two. This includes real-closed fields whose own automorphism group is trivial. Alternatively their nontrivial central complex conjugation is already detected by B.

## E. Every characteristic-zero Laurent-series field fails

Let F be any characteristic-zero field, K=F((u)), and choose a separable closure Fbar. The precise algebraic closure used is

    Omega = union_{F'/F finite, n≥1} F'((u^(1/n))),

with compatible roots. This is an algebraic closure of K by the Proposition on p.314 of van den Dries–Ribenboim (1984). It is essential to restrict the coefficient field to one finite F'/F for each series: arbitrary Fbar-coefficient Laurent series need not be algebraic over K.

The substitution sigma(u)=u+u², fixing F, is an automorphism of K. Its inverse is the unique series v∈u Q[[u]] satisfying v+v²=u, explicitly (-1+sqrt(1+4u))/2. Define an extension tau of sigma to Omega by fixing every element of Fbar and by

    tau(u^(1/n)) = u^(1/n) (1+u)^(1/n),

where the factor is the binomial series with rational coefficients and constant term one. On each F'((u^(1/n))) this is substitution of a uniformizer with leading coefficient one, so it is a field automorphism. The formulas are compatible when n divides m and when F' grows, because the constant-term-one roots are unique. The inverse substitution is compatible as well.

For g∈G_K, write g(u^(1/n))=zeta_n u^(1/n), with zeta_n∈Fbar. Since g fixes u and tau fixes Fbar,

    g tau(u^(1/n)) = zeta_n u^(1/n)(1+u)^(1/n)
                  = tau g(u^(1/n)).

They also commute on Fbar and on K. Each F'((u^(1/n))) equals the finite field extension K(F',u^(1/n)), so these checks on generators prove g tau=tau g on all of Omega; no continuity assumption on arbitrary automorphisms of the series field is being used. Thus sigma induces the identity in Out(G_K), while sigma is nonidentity. C gives a nonalgebraic, genuinely nonconstant, closed-point-preserving relative endomorphism of (Gm_K)_et. Its nonalgebraicity is already detected on K-points by 1, 2 and u.

## Opened primary sources

- CHW supplied source: Section3 Proposition3.6 (field-source reconstruction), Section2 rigidity of pinned relative morphisms, and the full reconstruction Hom-set condition. The source statements retain the structural 2-cell and its compatibility under relative isomorphism.
- L. van den Dries and P. Ribenboim (1984), “The Absolute Galois Group of a Rational Function Field in Characteristic Zero is a Semi-Direct Product,” Canadian Mathematical Bulletin 27(3),313–315, Proposition p.314. DOI: https://doi.org/10.4153/CMB-1984-047-4. The publisher's three-page primary PDF and journal metadata were opened. Only its exact bounded-coefficient Puiseux-closure proposition is needed; the commutation calculation above is proved directly.
- Stacks, Lemma15.116.7, Tag0EXW, and Definition15.113.7, Tag09E9, were opened as an independent check: residue characteristic zero is tame, and a finite tame extension lies in an unramified extension after adjoining a root of the uniformizer. These support the closure description but are not a substitute for the directly opened proposition.

The positive sufficient class in F.37 and these negative/necessary statements leave the converse classification in F.9 unresolved. They do not assert that slimness and automorphism faithfulness imply reconstruction.
