# E1: proved repair by boundary-tame moduli paths

Status: independently reviewed and accepted by root, 14 November 2026; E.10--E.12 are Proved. The literal full-path formulation and unrestricted specialization remain refuted by E.1 and E.2. This note constructs the precisely modified category and restricts the characteristic-zero covering arrows. Root expressly directed insertion of E_tame_extension.tex and removal of superseded E.U1 in E.tex, now completed.

## Statement

Fix an algebraically closed field k of characteristic p. For each hyperbolic type (g,n), let M be the moduli stack with unordered punctures, and let (Mbar,D) be its proper stable compactification with its normal-crossings boundary. Use logarithmic root stacks, so the construction treats self-intersections and permutations of local boundary branches correctly. Define

    R_m = root_m(Mbar,D),       (m,p)=1,
    Pi^bt(M) = lim_m Pi_1^et(R_m),

with geometric base points in M. The superscript bt means boundary tame; it does not mean the maximal prime-to-p quotient. Original p-torsion stack inertia and p-monodromy of finite étale interior covers are retained.

There is a compact-Hom category T_k^bt whose objects are all hyperbolic k-curves, whose markings are Pi^bt(M), and whose covering arrows are exactly finite étale maps with prime-to-p geometric Galois closure. It contains these actual maps faithfully. Every arrow factors as a marking and such a cover. Covers transport along markings, compatibly with composition. Algebraically closed field extension gives an equivalence.

After the choice of good-reduction base models and the usual paths between type base points, there is a specialization functor

    T_char0^{cov(p')} -> T_k^bt.

The source is the characteristic-zero category with ALL its moduli markings, but only covering arrows with prime-to-p Galois closure. It is not the entire T of the literal prompt. The functor preserves type; on automorphism groups it is the surjective specialization map from the full profinite mapping class group onto Pi^bt(M_k); on each Hom it is a finite disjoint union of the induced surjective closed-coset maps. There is no assertion that these automorphism maps are injective.

## 1. Proper DM stack finite-étale comparison, proved by descent

Let X be a proper finite-type DM stack over an algebraically closed field. Its diagonal is finite. EHKV Theorem 2.7 gives a finite surjective representable map Y -> X from a scheme. Then Y, Y x_X Y, and Y x_X Y x_X Y are proper schemes: the relevant fibre products are finite over products of schemes because the diagonal is finite. Finite-étale descent along Y -> X is effective, by applying SGA1 IX.4.12 after an étale atlas of X. It identifies FEt(X) with finite étale covers of Y equipped with a descent isomorphism and a cocycle on these next two Čech levels. SGA1 X.1.8 makes FEt of EACH proper scheme invariant under algebraically closed field extension. Full faithfulness carries the descent isomorphism and its cocycle uniquely. Hence FEt(X) is invariant.

The same proof over a complete noetherian local ring A, using SGA1 X.2.1 (or IX.1.10), gives FEt(X) equivalent to FEt(X_s). No tameness of the original stack inertia is needed. In particular the argument applies to Mbar and R_m in characteristic 2 or 3.

If A is a complete DVR with algebraically closed residue field and X is smooth proper with geometrically connected fibres, the map pi_1(X_geometric_generic) -> pi_1(X_s) is surjective. A connected finite étale cover of X_s extends uniquely. Its total space over A is connected by the finite-étale equivalence and regular because it is smooth over a regular DVR. A connected regular DM stack is irreducible (check on étale charts), so its generic fibre is connected. The same argument after every finite extension of the DVR proves geometric connectedness. Thus every connected special cover stays connected generically, which is exactly surjectivity. This avoids assuming a stacky Stein-factorization theorem.

## 2. Root stacks, boundary tameness, and faithful curve automorphisms

On an étale chart where D is x_1...x_r=0, R_m has the chart

    [Spec A[t_1,...,t_r]/(t_i^m-x_i) / mu_m^r].

It is proper over Mbar and smooth DM over the same ground base when m is invertible. The construction glues for the divisorial log structure, even when D is only normal crossings. Its finite representable étale covers restrict fully faithfully to M. SGA1 XIII.5.2 says that every finite cover of M tame at D extends uniquely to some R_m; uniqueness of normalization supplies the descent on overlaps. Conversely any cover of R_m is tame at D by this local chart. Consequently the displayed inverse limit is the full boundary-tame groupoid. This is a direct finite-root proof; Talpo–Vistoli Proposition 3.10 supplies the root chart, but their Kummer-flat Theorem 6.16 is NOT misquoted as an étale theorem.

Part 1 applied to every R_m proves base-field invariance of Pi^bt(M). Applied over W(k), it gives surjective geometric specialization at every finite root level. These compatible surjections give a surjection on inverse limits: a compact image which projects onto every directed finite level is the whole limit. Restriction from the generic open M to each normal R_m is also surjective on pi_1, so

    pi_1^et(M_geometric_generic) -> Pi^bt(M_k)

is surjective. The analogous path-torsor statement follows after any choice of a path and the group statement.

The natural map Aut(C) -> Pi^bt(M,C) is injective. First order all punctures; that cover extends as a finite étale cover of the quotient stack of the stable compactification, even if p divides n!. For genus zero this kills automorphisms. For positive genus choose a full Jacobi level ell >= 3 with ell != p, and in genus one use one ordered puncture as origin. This kills automorphisms: Deligne–Mumford Theorem 1.13 and Lemma 1.14 give the faithful Jacobian action in genus >=2; the genus-one statement is the corresponding faithful action of origin-preserving automorphisms. A finite-order matrix congruent to identity modulo ell is identity in GL(Z_ell), as follows from the first nonzero ell-adic term of its binomial expansion. The level cover is boundary tame. On a strict regular chart of the stable compactification the universal curve is split semistable. The prime-to-p monodromy theorem underlying B.5 and C.2 gives trivial wild inertia and boundary transvections I+N_e on H1 mod ell, with N_e squared zero. Hence (I+N_e)^ell=I. At an intersection, disjoint vanishing cycles give N_e N_f=0, so the boundary image is an elementary abelian ell-group. This also applies to marked genus one; in genus zero only the already-étale ordering cover is needed. The final proof uses this explicit monodromy argument, following root review, rather than the earlier proposed shortcut through Deligne–Mumford Lemma 5.10. Knudsen Theorem 2.7 supplies relative normal crossings for every pointed hyperbolic type. No assertion that the full finite monodromy group has prime-to-p order is made. Thus the faithful levels are among the covers defining Pi^bt, while finite interior p-monodromy remains allowed.

## 3. The exact Hurwitz path-lifting statement

For a finite étale u:V->Y with prime-to-p Galois-closure group G, mark every puncture of Y and every point over it, retaining labels/colours only as needed. Use the stable Hurwitz compactification with Galois closure retained, not the generally nonnormal naive admissible-cover space. Bertin–Romagny Definition 6.8, Theorem 6.9, Proposition 6.14, Theorem 6.20 and Definitions 6.21–6.22 apply. All ramification points are marked; hence nodal stabilizers are cyclic and do not exchange branches. Their Theorem 5.5 gives local parameters

    tau_i = t_i^{e_i},       e_i divides |G|,

for the discriminant map to the stable target moduli. The other parameters are unchanged. Quotients by intermediate subgroups remain stable because all preimages of target marks are retained; this is Proposition 5.3 and the discussion in Definition 6.21. It is not the unmarked quotient statement that BR explicitly warns may fail.

After base change to R_m with every e_i dividing m, NORMALIZE the Hurwitz pullback. Locally normalization splits t_i^{e_i}=r_i^m into the branches t_i=zeta_i r_i^{m/e_i}. Its deformation map is now an isomorphism. Automorphisms permuting these branches are handled by the stack normalization; the remaining relative automorphisms are the deck groups of the smooth covers. Thus the normalized morphism is a proper étale DM morphism with finite groupoid fibres. It is a finite étale gerbe over a representable finite étale cover of R_m. One must not call the original discriminant map representable; BR Proposition 6.14 explicitly warns about its centre gerbe.

As m ranges over multiples prime to p, these pulled-back roots are cofinal among all prime-to-p roots of the Hurwitz boundary: locally tau_i=t_i^{e_i} with e_i prime to p. Hence their fundamental groups compute Pi^bt of the Hurwitz open.

For a finite étale gerbe H->Q, the fibre deck group D has the exact sequence

    D -> pi_1(H,u) -> pi_1(Q,q) -> 1.

This is Noohi Proposition 10.4 and Corollary 10.5. The relative version over a stack base follows by the same finite-étale descent argument: a finite cover on which the relative fibre inertia acts trivially descends uniquely to Q; the image of that finite inertia is normal. Neutralize étale locally and check the assertion for BD; the descent cocycle gives the general case. Injectivity on the left is NOT automatic for an arbitrary gerbe. Pass first to the cofinal root system. Exactness survives: lift sets are compact and compatible finite sets of constraints have solutions, while a limit-kernel element is represented by a single d in the finite group D by the same finite-intersection argument. Here the left map in the limit is injective because the source map to Pi^bt(M_source) sends D to the canonical curve-automorphism subgroup, which is injective by Part 2. Injection at an arbitrary single finite root level is not assumed. This also explains exactly why ignoring deck gerbes would be an error.

Passing to the cofinal root system gives the path form needed here: a boundary-tame target path and a starting cover determine a unique endpoint isomorphism class of covers; they admit a lift in the Hurwitz boundary-tame path groupoid; two lifts with the same chosen endpoint differ by a deck element. The source map takes that lift to a boundary-tame source marking. The source map is defined on these groupoids because it extends to stable compactifications and pulls each source-boundary parameter to a monomial in Hurwitz boundary parameters times a unit. Thus a prime-to-p Kummer root pulls back to a prime-to-p Kummer root. There is no pullback of an unexplained wild boundary class.

## 4. Category and normal forms

An arrow X->Y is an equivalence class of pairs (u,alpha), with u:V->Y a prime-to-p-closure cover and alpha a Pi^bt marking X->V. An isomorphism h:V->V' over Y identifies (u,alpha) with (u',h alpha).

For (u,alpha):X->Y and (v,beta):Y->Z, transport u along beta to u':V'->W, where v:W->Z. If gamma:V->V' is a lifted source marking, define the composite by (v u', gamma alpha). Part 3 proves independence of the lifted path. Independence of the cover representative is functoriality of its Hurwitz stack. Associativity is checked on the stack of a chain of covers: the Galois closure of a composite embeds in the corresponding wreath product and therefore still has prime-to-p order; the common Galois closure and its intermediate subgroups construct all transports simultaneously. All punctures over the target are marked, so these common-closure quotient maps extend to the stable compactification. Both bracketings are the same composite-cover and path maps there. Identities are (id,id).

The category contains actual covers through (u,id). Faithfulness follows from the injectivity of Aut(V) into its marking group: if two actual covers become equal then an isomorphism of their sources has trivial canonical marking, hence is identity. Cover transport and the requested marking-cover factorization hold by construction.

Put c(X)=2g_X-2+n_X. Tame Riemann–Hurwitz gives d=c(X)/c(Y). If d is not a positive integer there are no arrows. Otherwise there are only finitely many isomorphism classes u:V_u->Y of the required degree and source type, because pi_1(Y)^{p'} is topologically finitely generated. Consequently

    Hom(X,Y) = disjoint union_u D_u \ Path_bt(M_type(X); X,V_u).

Each path torsor is profinite and each D_u is a finite closed subgroup. Thus Hom is compact Hausdorff. Composition is continuous: on a fixed component, target transport depends on a finite quotient, and after fixing the transported cover it is the continuous map of Hurwitz path torsors followed by multiplication. Degree-one covers show Aut(X)=Pi^bt(M_type(X),X).

For k subset K algebraically closed of the same characteristic, fixed-target prime-to-p covers correspond by E.3; source type and deck groups correspond. Part 2 gives isomorphisms on all path torsors, so the Hom formula gives full faithfulness. Every K-curve has a type represented by a k-curve, and the connected moduli path groupoid marks it to that base-changed curve. This proves essential surjectivity and therefore base-extension equivalence, despite the fact that the actual individual K-curve may not descend to k.

## 5. Restricted specialization, with all model choices exposed

Choose R=W(k). Smoothness of pointed stable moduli lifts a chosen k-curve of each type to a smooth marked R-curve; properness of the resulting family and formal existence algebraize it. Equivalently choose the curves in a nonempty smooth chart over R. Fix one such curve per type. The full subcategories on their geometric generic fibres and special fibres are skeletons up to marking equivalence. A characteristic-zero common algebraically closed overfield compares the generic-fibre category to the stated characteristic-zero T; no embedding of an arbitrarily large field into C is assumed.

For a prime-to-p-closure cover u:V->Y of a chosen generic target, E.3 gives the corresponding special cover. After a finite extension of R, it has a smooth marked model over the chosen model of Y. One can obtain this by lifting the corresponding special cover and identifying its generic fibre with u; the identification descends to a finite field extension. Stable-model uniqueness makes the marked model and its deck action compatible with further extensions. This is the place where the prime-to-p restriction on the covering arrows is indispensable.

An arrow has normal form (u,alpha), where alpha is now a FULL characteristic-zero étale marking from the chosen source-model curve to V. Both endpoints have models after the preceding finite extension. Specialize alpha by the root-stack proper comparison of Part 2, and send (u,alpha) to (u_s,sp(alpha)). The result is independent of the finite extension, the representative cover and the model isomorphism by proper separated stable-model uniqueness and finite-étale descent. It is functorial because source and target maps of the normalized root Hurwitz diagrams commute with specialization; the common-closure diagram gives the same assertion for composition of any finite chain.

The functor sends type (g,n) to type (g,n). On automorphisms it is the continuous surjection

    q_(g,n): pi_1^et(M_(g,n),char0) -> Pi^bt(M_(g,n),k).

The source group is the full profinite mapping class group under the characteristic-zero comparison. It first maps to the inverse limit of prime-to-p boundary-root generic groups, then specializes. Interior p-monodromy is retained on the target. It is not the maximal pro-prime-to-p quotient.

For each fixed-target cover component, E.3 matches u with u_s and identifies its finite deck group. The induced Hom map is

    D_u \ Path_et(X,V_u) -> D_us \ Path_bt(X_s,V_us).

It is surjective, since the corresponding path-torsor specialization is surjective. After choosing paths to identify the torsors and identifying the deck groups, it is the quotient map D\Gamma -> D\Gamma_t attached to q. Its fibres are precisely the equivalence classes D ker(q) gamma. The cover-component index set is preserved. Neither full faithfulness of specialization nor injectivity of q is claimed.

## Source check and limitations

- EHKV, *Brauer groups and quotient stacks*, Theorem 2.7, author's PDF p.5: https://www.math.brown.edu/bhassett/papers/brauer/brauer.amj.pdf. Opened actual primary PDF, including theorem and proof start.
- SGA1 supplied full source, IX.4.12 proper descent; X.1.8 proper algebraically closed field invariance; X.2.1 proper formal comparison; XIII.5.2–5.3 Kummer/Abhyankar charts. Exact statements read locally.
- Deligne–Mumford 1969 supplied PDF, Theorem 1.13, Lemma 1.14; Theorem 5.2; 5.5–5.14, especially 5.8–5.10 and 5.14. Knudsen (1983), Theorem 2.7, printed p.179: the supplied PDF has no text layer, so this page was rendered and actually inspected as tmp/F_pdf/knudsen_th27.png. It states proper smoothness and relative normal-crossings boundary for every hyperbolic pointed type. Publisher metadata: https://journals.msp.org/mscand/article/view/1622, DOI 10.7146/math.scand.a-12001.
- Bertin–Romagny supplied actual TeX: Proposition 5.3; Theorem 5.5; Definition 6.8; Theorem 6.9; Proposition 6.14 and its nonrepresentability footnote; Theorem 6.20; Definitions 6.21–6.22. Exact passages read locally.
- Noohi, *Fundamental groups of algebraic stacks*, arXiv:math/0201021v1, Proposition 10.4 and Corollary 10.5, pp.23–24. Actual primary PDF opened: https://arxiv.org/pdf/math/0201021. Appendix A.4 checks the stack formulation; the relative gerbe descent argument is given above rather than attributed word-for-word to a base-space-only theorem.
- Talpo–Vistoli, *Infinite root stacks and quasi-coherent sheaves on logarithmic schemes*, arXiv:1410.1164v2, Propositions 3.4 and 3.10, actual PDF opened. Finite-root local construction only; no false identification of Kummer-flat and étale sites.
- Landesman 2024 Theorem 1.1, arXiv:2005.09690v3, proves the scheme tame-invariance theorem. It was opened as a cross-check but is not needed for the stronger proper-DM-root proof above, and it is not silently cited for a stack extension.

The original E1 request still has two false literal clauses: full moduli étale paths are not base invariant in characteristic p (E.1), and the entire characteristic-zero category cannot specialize to one with only prime-to-p Galois-closure arrows (E.2). The proposed theorem answers the mathematically repaired construction, with both necessary changes named.
