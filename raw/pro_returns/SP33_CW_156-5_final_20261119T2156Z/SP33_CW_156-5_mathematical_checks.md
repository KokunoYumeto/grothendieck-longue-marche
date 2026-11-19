# Mathematical checks after the transcription freeze

These checks were made after the freeze recorded in `progress.log`. They do not amend the transcription. They distinguish a mathematically specified statement from the literal wording, including slips, unresolved readings, and uncompleted arguments. The proofs below are this run's deductions, with no claim of novelty. References to the supplied sweep are comparisons with its claims, not transfers of its check events to this run.

## P00. Model and the necessary interpretation of scan 002

For a family \(F\subseteq\mathcal P(L)\), put \(S=\bigcup F\) and
\[
 A^\circ=A\setminus\bigcup_{B\in F,\,B\subsetneq A}B.
\]
In the mathematical checks, “préadmissible” means that every \(x\in S\) has a **least** member \(A_F(x)\) of \(F\) containing it; “admissible” adds \(A^\circ\ne\varnothing\) for every \(A\in F\). The empty family is admissible, but a family containing the empty-set member is not admissible.

This is an explicit interpretation for the checks. The frozen scan 002 has a plain \(\subset\) both in the boundary and in union formulas, has \(x\in L\) in condition 1, and has \(x\in\mathscr L\) in the first formulation of beta. A single globally strict reading of every inclusion is impossible: alpha with \(A=B\) needs to admit \(C=A\), whereas the boundary must omit \(B=A\). A globally weak boundary would make every open stratum empty. Also, with \(L=\{a,b\}\), \(F=\{\{a\}\}\), the support-based conditions hold but the literal condition 1 fails at \(b\). These are mathematical qualifications and reading questions, not new ink readings.

## P01. Proposition 1 on its support

Assume the least-member condition. For \(x\in A\cap B\), the member \(A_F(x)\) lies in \(A\cap B\), proving alpha with weak inclusion in its union. The least member has no proper submember through \(x\), proving beta. Conversely, choose a minimal member \(A\) through \(x\) using beta; for any other member \(B\) through \(x\), alpha provides \(C\) through \(x\) with \(C\subseteq A\cap B\), so minimality forces \(C=A\), hence \(A\subseteq B\). Thus minimality becomes leastness by alpha, not merely by uniqueness of a minimal member.

The nonempty strata are consequently exactly the fibres of \(x\mapsto A_F(x)\), proving gamma. Every member is a union of these fibres, proving delta. If \(A^\circ\ne\varnothing\) and \(A^\circ\subseteq B\), pick a point in that stratum: its least member is \(A\), hence \(A\subseteq B\), proving eta. Conversely, gamma chooses the unique stratum through \(x\); delta puts that entire stratum inside each \(B\) through \(x\), and eta then puts its closed member inside \(B\). The final implication in scan 003 therefore genuinely uses eta, even though its opening says only gamma and delta.

The margin's alternative, gamma together with
\[
 A=\bigcup_{B\in F,\,B\subseteq A}B^\circ,
\]
also implies leastness: if \(x\in A^\circ\cap D\), the displayed decomposition of \(D\) supplies \(C\subseteq D\) with \(x\in C^\circ\); gamma forces \(C=A\). This rechecks the support-based theorem underlying the sweep's SA21-R5-01, without pretending that its normalized statement is the literal transcription.

## P02. Artinian eta, and an explicit infinite counterexample

For an artinian family, beta follows by taking a minimal member in each nonempty family of members through a fixed point. Here “artinian” is used in its usual well-founded/minimal-element sense (equivalent to the sequence formulation in the usual choice setting). If gamma holds and \(p\in A^\circ\subseteq B\), choose \(E\) minimal among members containing \(p\) and contained in \(B\). No proper submember of \(E\) contains \(p\), hence \(p\in E^\circ\); gamma gives \(E=A\), so eta follows. This confirms the sweep's reason why the cancelled finite example of scan 004 cannot work.

An explicit infinite example shows that the general nonredundancy claim is nevertheless correct. Take distinct points \(p,a,b_0,b_1,\ldots\), and set
\[
 A=\{p,a\},\qquad B_n=\{p\}\cup\{b_m:m\ge n\},\qquad
 F=\{A,\{a\}\}\cup\{B_n:n\ge0\}\cup\{\{b_n\}:n\ge0\}.
\]
The strata are \(A^\circ=\{p\}\), \(\{a\}^\circ=\{a\}\), \(\{b_n\}^\circ=\{b_n\}\), and \(B_n^\circ=\varnothing\), since \(B_{n+1}\cup\{b_n\}=B_n\). Thus gamma and delta hold: the nonempty strata are all singletons and every member is saturated. Eta fails because \(A^\circ=\{p\}\subseteq B_0\) but \(a\notin B_0\). The infinite descending chain of the \(B_n\) explains exactly where the artinian argument fails. This is our test-family; no identity with the unavailable GF VIII example is asserted.

## P03. Ordered-set description, redundant members, and irreducibility

For an admissible family, take \(I=F\) ordered by inclusion and \(p:S\to I\), \(p(x)=A_F(x)\). Then \(p\) is onto because every stratum is nonempty, and
\[
 A=p^{-1}(I_{\le A}),\qquad A^\circ=p^{-1}(A).
\]
Conversely, given a poset \(I\) and a surjection \(p:S\to I\), the family \(\{p^{-1}(\downarrow i):i\in I\}\) is admissible: the least member through \(x\) is indexed by \(p(x)\), and its stratum is the nonempty fibre. Surjectivity also makes the indexing faithful. Closed sets are inverse images of downsets; open sets are inverse images of upsets. This orientation is opposite to the **downset-open** convention in RESULTS_STATE's STRATA 0.1; applying that register convention uses \(I^{op}\).

For a preadmissible family, the active members \(F'=\{A:A^\circ\ne\varnothing\}\) still give such an admissible family. Every other member is the union of active members below it, hence corresponds to a downset of \(I=F'\) that is not principal. Conversely, one may adjoin **any collection** of nonprincipal downsets, pulled back along \(p\): every point still has its old least member, old strata remain nonempty, and the added members have empty stratum. There is no general finiteness restriction on this collection. For example, all singletons of \(\mathbb N\), together with the sets \(\{0,\ldots,n\}\) for \(n\ge1\), form a preadmissible family with infinitely many redundant members; this is a test of the uncertain “fini/fin.” in scan 005's margin.

A nonempty downset is **completely join-irreducible** in the lattice of downsets iff it is principal: write it as the union of all its principal downsets and apply complete irreducibility; the converse follows by looking at the greatest point. Ordinary topological irreducibility only tests finite unions and is weaker. The whole ordered set \(\mathbb N\), with closed downsets, is irreducible but has no greatest point and is not a principal downset. Thus the unqualified irreducible-closed-set sentence on scan 005 needs a finite/strong qualification; scan 012 explicitly supplies “au sens fort”. The sweep's abbreviated unqualified statement must be read with this distinction too.

## P04. Locally closed and Boolean-constructible sets

In a poset with closed downsets, a subset \(J\) is locally closed iff it is order-convex. Indeed, if \(i\le j\le k\) and \(i,k\in J\), an open-upset/closed-downset presentation forces \(j\in J\). Conversely, for convex \(J\), one has \(J=(\uparrow J)\cap(\downarrow J)\): a point in the intersection lies between two points of \(J\), so belongs to \(J\). This proves the statement of scan 006 with the manuscript's orientation.

When \(I\) is finite, each fibre \(A_i^\circ\) is a finite Boolean combination of principal closed sets. Consequently the Boolean algebra generated by the members of the figure consists exactly of all unions of fibres. For infinite \(I\), that last statement need not hold for the **ordinary**, finitely generated-under-operations Boolean algebra: take the discrete order on \(\mathbb N\), whose figure consists of singletons. Its generated Boolean algebra contains exactly the finite and cofinite subsets, whereas all subsets are saturated. Scan006's inserted finiteness condition is therefore essential; no general all-subsets assertion is inferred outside that scope.

## P05. Subfigures, compatibility, and bounded unions

If \(F\le G\), meaning a down-closed subfamily, all proper submembers of each \(A\in F\) are already in \(F\). Its boundary and stratum are unchanged, so \(F\) is admissible. Its support is exactly the union of those unchanged strata. Conversely, the scan 007–008 condition that a subfamily is admissible and has the induced partition forces it to be down-closed: for \(B\in G\) lying inside \(A\in F\), pick \(x\in B^\circ_G\); the \(F\)-stratum through \(x\) equals that \(G\)-stratum, and the associated least members are equal. Hence \(B\in F\). The scan 008 parenthesis “Psi adm.” is not the hypothesis justifying nonemptiness of \(B^\circ_G\); that uses the ambient family's admissibility.

For clarity in that converse, support saturation is already automatic from the raw subfamily inclusion: each ambient member is a union of ambient strata. If the smaller stratum indexed by \(C\in F\) equals the ambient stratum indexed by \(B\in G\), then \(C_G^\circ\subseteq C_F^\circ=B_G^\circ\), because every proper smaller-family member is an ambient member. The nonempty \(C_G^\circ\) and disjointness of ambient strata force \(C=B\). This supplies the equality-of-members step in the preceding paragraph rather than assuming it from equality of partitions alone.

The four compatibility criteria on scans 008–012 can be checked explicitly. Put \(D=F\cap G\) and \(T=|F|\cap|G|\). If \(D\) is down-closed in both and \(|D|=T\) (condition b), a point in the overlap has the same least member in both: choose a common member through it, and use down-closure to see that both least members belong to \(D\), then compare them in both directions. If \(B\in G\) lies inside \(A\in F\), choose \(x\in B_G^\circ\); some member of \(D\) contains \(x\), and leastness plus down-closure puts \(B\) in \(D\). Thus both families are down-closed in their union, their strata are unchanged, and that union is admissible, proving a. The reverse implication follows by working in the common upper figure; a-prime is equivalent to a by the same downset-union argument.

Condition c says that \(T\) is closed for both and that the members contained in it coincide. Such closed sets are unions of the corresponding lower members, so c is equivalent to b. Condition d gives this locally on every \(A\cap B\): their union \(T\) is closed for both, and if \(C\in F\) is contained in \(T\), take \(x\in C_F^\circ\) and \(B\in G\) through \(x\). The \(F\)-closed intersection \(C\cap B\) contains \(x\), hence contains \(C\); local agreement then puts \(C\) in \(G\). The symmetric argument proves c, while a implies d by restriction inside the common upper figure. This proves a, a-prime, b, c, d equivalent without importing the sweep's finite computation.

For compatible families \(F,G\), both are down-closed in their union. Their common support equals the support of their common subfamily: the least member through a point of the overlap is the same in both. Thus support inclusion for compatible figures implies subfigure inclusion, and equal support implies equality. Equality of support and of the stratum equivalence relation alone does not imply compatibility: on \(\{a,b\}\), take
\[
 F=\{\{a\},\{a,b\}\},\qquad G=\{\{a\},\{b\}\}.
\]
Both partitions are the singleton partition, but their union has an empty top stratum.

For any pairwise compatible collection \((F_i)\), its union is admissible and each \(F_i\) is down-closed in it. To see this, each member's lower members are unchanged by compatibility, and a point appearing in two families has the same least member in both. This proves the bounded-union assertion C1 and gives its pairwise-compatible version. Every figure is the union of its principal subfigures \(F_A\), proving C2 with the corrected indexing; compatibility can therefore be checked on these principal multistrates, as in C3. These are checks in the set-theoretic model, not claims about all abstract axiom systems in the sweep.

## P06. The component obstruction and its finite classification

The node \(\{L\}\) is **isolated** in the comparability graph of nonempty multistrates, for every nonempty \(L\). A nonempty subfigure of it must equal it; if it is a subfigure of a multistrate \(H\), down-closure at its member \(L\) forces every member of \(H\) to be \(L\). If \(|L|\ge2\), the node \(\{\{x\}\}\) is different and is incompatible with \(\{L\}\): their union contains \(\{x\}\subsetneq L\), so \(\{L\}\) is not down-closed there. This directly disproves both connectedness and the cross-component compatibility claim C4 for every \(|L|\ge2\), including infinite ground sets.

For finite \(n=|L|\ge3\), the components are exactly:

1. The isolated node \(\{L\}\).
2. For every \((n-1)\)-element subset \(A\), the two nodes \(\{A\}\) and \(\{A,L\}\).
3. One component containing all remaining multistrates.

Here is a proof of the nontrivial last assertion and of completeness. Any finite multistrate has a minimal member \(A\), so \(\{A\}\) is a subfigure. If \(|A|=n-1\), any further minimal member must be disjoint from \(A\), hence must be the singleton complement; the greatest member would then have empty stratum. Thus only the two displayed nodes occur in that component. If \(|A|\le n-2\), choose distinct \(x,y\notin A\); the admissible family
\[
 \{A,\{x\},A\cup\{x,y\}\}
\]
has top stratum \(\{y\}\), and joins the nodes \(\{A\}\) and \(\{\{x\}\}\) by comparability. Any two distinct point-singleton nodes are similarly joined using a third point. Every remaining multistrate therefore belongs to that one component. There are exactly \(n+2\) components for \(n\ge3\); the cases \(n=1,2\) give one and three components respectively.

The ancillary independent computation used only the definitions specified by root, not scans, witnesses, context or the supplied sweep implementation. Its results are fully reproducible in `scripts/finite_figures_check.py` and `scripts/finite_figures_n4_components.py`:

| Ground-set size | Admissible families, including empty | Multistrates | Component sizes | Incompatible ordered pairs across components |
|---:|---:|---:|---|---:|
| 1 | 2 | 1 | 1 | 0 |
| 2 | 7 | 5 | 2, 2, 1 | 14 |
| 3 | 45 | 28 | 21, 2, 2, 2, 1 | 324 |
| 4 | 500 | 231 | 222, 2, 2, 2, 2, 1 | Not computed |

The n=4 check was limited to the exact predicted component partition. It did not test additional refinement pairs. The two computation JSON files retain memberships and the n≤3 relation tables.

## P07. The two readings of the scan 015 construction must be distinguished

The frozen display literally takes \(A\in F\), \(B\in G\), with an inserted exclusion of both being empty. Since admissible families contain no empty-set member, that insertion is redundant under the literal ranges. For \(F=\{\{a\}\}\), \(G=\{\{b\}\}\), the literal construction is \(F\boxtimes G=\{\{a,b\}\}\), which **is admissible**, but contains neither \(F\) nor \(G\) as a subfigure. Its actual boundary is empty; the displayed manuscript boundary formula gives \(\{a,b\}\), so that formula is false in this example.

The stratum formula also fails for the literal construction in general. Let \(F=\{\{a\},\{a,a'\}\}\), \(G=\{\{b\}\}\). The product family is \(\{\{a,b\},\{a,a',b\}\}\); the top stratum is \(\{a'\}\), whereas the proposed union of the two factor strata is \(\{a',b\}\).

If instead one **adjoins empty choices to both ranges**, as suggested by the later claimed inclusion of \(F\amalg G\), then a mixed member \(A\cup B\) with both parts nonempty has the proper members \(A\) and \(B\) below it. Its stratum is empty, so the intended bounding family is not admissible. The sweep's SA21-K5-01 is right about the failed bounding argument and C4; its blanket assertion that the displayed product is always inadmissible conflates this enlarged interpretation with the literal ranges. No resolution of that mismatch has been put into the frozen TeX.

The scan 013 and scan 014 displays also have extra nested braces in the ink. They are not silently flattened in the transcription. Even the natural typed version \(\{A,\{x\},A\cup\{x\}\}\) of the scan 013 proposal fails: its top stratum is empty. The valid three-member bridge in P06 needs the genuinely additional point \(y\).

## P08. Supports, atoms, and the regular-open alternative

Two figures are disjoint in the manuscript sense (compatible, with empty common subfigure) iff their supports are disjoint. Disjoint supports make the union admissible and both families down-closed; the converse follows from the common-support statement of P05. For a collection of figures \(\mathcal C\), its orthogonal class is
\[
 \mathcal C^\perp=\{F:|F|\subseteq L\setminus\textstyle\bigcup_{G\in\mathcal C}|G|\}.
\]
Taking the orthogonal twice gives all figures supported on that union. The reverse containment is detected by the point figures \(\{\{x\}\}\). Thus the support lattice is exactly \(\mathcal P(L)\), with set complement.

The marginal reconstruction from \(M\) on scan 017 also follows. Send \(F\) to all multistrates below it; this is down-closed in \(M\) and pairwise compatible. Conversely, for a down-closed pairwise compatible subset \(D\subseteq M\), form \(F=\bigcup D\) by P05. If \(A\in F\), some \(X\in D\) contains it and its principal lower subfamily is unchanged in \(F\), so \(F_A=X_A\le X\) lies in \(D\). Hence the multistrates of \(F\) are exactly \(D\), even though \(M\) is disconnected.

This complete atomic Boolean algebra already recovers \(L\) as its set of atoms. In its Stone-space interpretation, those atoms correspond to isolated principal ultrafilters; the Boolean-algebra-to-Stone-space construction is not a reason to conclude that the original discrete point set is irretrievably lost. The manuscript itself adds the isolated-point recovery in scan 017. We carry the usual Stone representation as background; the elementary atom identification just given is checked here.

For the proposed compact zero-dimensional Hausdorff variant with clopen strata, arbitrary unions of clopen supports are open sets \(U\). The union of clopen sets disjoint from \(U\) is \(U^*=\operatorname{int}(X\setminus U)\); double orthogonality gives \(U^{**}=\operatorname{int}\overline U\). Thus biorthogonally closed supports are regular open sets. With \(U=\operatorname{int}\overline U\) and \(V=X\setminus\overline U\), one has \(V=X\setminus\overline U\), \(U=X\setminus\overline V\), and
\[
 \overline U\cap\overline V=X\setminus(U\cup V).
\]
This derives the intended regular-open identities under the stated hypotheses; it does not decide the irregular final symbols of scan 017, or assert that the manuscript has specified all those topological hypotheses.

## P09. Density, locality of restrictions, and finiteness

In an admissible family of closed subsets of a topological space, the density condition \(B=\overline{B^\circ}\) for every member is equivalent to the incidence condition \(A\subseteq B\Rightarrow A^\circ\subseteq\overline{B^\circ}\). One implication is immediate; conversely, decompose \(B\) into all strata \(A^\circ\) with \(A\subseteq B\), to obtain \(B\subseteq\overline{B^\circ}\), while closedness gives the reverse inclusion. This checks the mathematical content of the legible density part of scan 018's margin, separately from its cancelled draft.

Properties depending only on each member and its unchanged principal subfigure survive subfigures and compatible unions: they can be checked member by member. Global local-finiteness needs a separate restriction. On \(\mathbb R\), each singleton figure supported at \(1/n\) is locally finite, but their compatible union is not locally finite at 0. This confirms why scan 019 allows finite sups while warning about arbitrary ones.

A finite poset of strata is a finite union of principal ideals, and each principal ideal is finite. Conversely, a finite union of finite principal ideals is finite. Thus “finite type and finite strata” gives finiteness if “strates finies” means finite principal **multistrates**. It is false if it means finite cardinality of each underlying subset: a one-member figure \(\{L\}\) is a finite figure even when \(L\) is infinite. The ambiguous level of “strates” is kept as an explanatory question rather than corrected in the transcription.

## P10. What a finite-poset realization supplies

For a finite poset \(I\), use its order complex \(|NI|\) and let \(X_i=|N(\downarrow i)|\). A point lies in the unique open piece indexed by the largest vertex of its barycentric support; hence the \(X_i\) form an admissible family, with the same order as \(I\), and downsets correspond bijectively to unions of the \(X_i\). This supplies an elementary finite realization of the kind contemplated on scan 019.

It does not make the \(X_i\) ordinary closed balls. If a top element lies above three incomparable elements, its principal order complex is a tripod, not a ball. The quoted “cellules” therefore needs its intended geometric meaning specified before a regular-cell or manifold conclusion is drawn. We do not reprove the register's STRATA A.4/A.12 or BISITE G.10 exit statements; their variance and hypotheses must be transported separately. Nor does this construction retain the link and attachment data in Esquisse 119/58–59.

## P11. Refinement and the marginal lemma

Write \(p_F(x)=A_F(x)\). Suppose each \(A^\circ_F\) lies in one \(\varphi(A)^\circ_G\), with \(\varphi\) increasing. Every \(x\in A\) belongs to \(A'^\circ_F\) for \(A'\subseteq A\); hence \(x\in\varphi(A')\subseteq\varphi(A)\), proving \(A\subseteq\varphi(A)\). If also \(A\subseteq B\in G\), the nonempty stratum \(\varphi(A)^\circ_G\) meets \(B\), so leastness in \(G\) gives \(\varphi(A)\subseteq B\). Thus \(\varphi(A)\) is the least container.

For \(x\in A\cap B\), put \(A'=p_F(x)\). Its image stratum meets \(B\), so \(\varphi(A')\subseteq B\) and therefore \(A'\subseteq A\cap B\). This proves that the intersection is a union of \(F\)-members. Conversely, suppose the least-container and closed-intersection conditions hold. For \(x\in A^\circ_F\) and \(B\) the least \(G\)-container of \(A\), let \(C=p_G(x)\subseteq B\); the \(F\)-closed set \(A\cap C\) contains \(x\), so it contains \(A\), forcing \(B=C\). Thus all of \(A^\circ_F\) lands in \(B^\circ_G\), and leastness makes \(A\mapsto B\) increasing.

The same reasoning proves the marginal lemma: under b, \(A^\circ_F\subseteq B\in G\Rightarrow A\subseteq B\). Conversely, that lemma plus the stratum landing condition implies monotonicity, because \(A'\subseteq A\) gives \(A'^\circ_F\subseteq A\subseteq\varphi(A)\), so \(\varphi(A')\subseteq\varphi(A)\). This closes the corollary's temporary proof obligation on scans 022–023.

Equivalently, the identity on the included supports preserves the preorders \(x\le_F y\iff p_F(x)\subseteq p_F(y)\). Preservation forces one \(G\)-equivalence class on every \(F\)-class and gives the increasing quotient map; the converse is immediate. Refinement is therefore reflexive and transitive; antisymmetry follows from equality of supports and both preorders, which reconstruct the same admissible family by P03. The literal top line of scan 021 says \(A\cap F\); this proof checks the intended \(A\cap B\), as the continuation itself does, not that ill-typed literal expression.

The continuity NB on scan 021 follows as well. If support inclusion holds and every \(A\cap B\) is \(F\)-closed, then \(B\cap|F|=\bigcup_{A\in F}(A\cap B)\) is \(F\)-closed for every \(B\in G\). The inverse image of any union of \(G\)-members is therefore closed, and the support inclusion is continuous. Conversely, continuity makes those inverse images closed and hence their intersections with \(A\) closed. For these preorder topologies this is exactly preorder preservation: a least closed neighbourhood of a point maps into the least closed neighbourhood of its image, and conversely order preservation pulls downsets back to downsets. This verifies the marginal assertion rather than imposing it as an additional axiom.

The independent finite computation verifies the two principal formulations on all 4+49+2025 admissible ordered pairs for n=1,2,3, and order laws on all composable chains. Its finite scope is separate from the proof above.

## P12. Subdivision as maximal refinement

Compatible refinements of \(G\) have a union refining \(G\): each member and its stratum is unchanged, so the least-container/stratum criterion is unchanged. The same argument works for arbitrary compatible sups, as the scan 024 insertion says.

If \(F\ll G\) has full support and \(F\le H\ll G\), then \(|F|\subseteq|H|\subseteq|G|=|F|\). Compatible figures of equal support are equal by P05, so \(H=F\). Conversely, if \(x\in|G|\setminus|F|\), the singleton figure \(H=\{\{x\}\}\) refines \(G\), is disjoint from \(F\), and \(F\cup H\) is a strictly larger refinement. Thus the **maximal**, not minimal, refinements under the subfigure order are exactly those with full support. The finite enumeration confirms this for all 54 target figures on n≤3.

The literal “minimal|maximal” uncertainty on scan 023 and the reversed initial “F-prime sous figure de F” on scan 024 remain frozen. Taken as a minimality statement, the criterion is false already for the empty refinement of a nonempty figure; the preceding no-proper-extension clause and the proof demand maximality. With the intended refinement hypothesis, the marginal condition that every \(G\)-member is a union of \(F\)-members is equivalent to full support, using the closed-intersection property. Without that hypothesis, adding least containers as in margin d recovers the same proof.

## P13. The square, raw inclusion, and image operations

Given the square of scan 025 with \(p,q\) surjective, \(S\subseteq T\), and increasing \(\varphi:I\to J\), the families \(F_i=p^{-1}(\downarrow i)\) and \(G_j=q^{-1}(\downarrow j)\) satisfy the refinement criterion of P11. Conversely, every refinement gives precisely this square on its stratum quotients. However, that does **not** imply raw family inclusion \(F\subseteq G\): take \(F=\{\{a\},\{b\}\}\) and \(G=\{\{a,b\}\}\), with the surjection from a two-point antichain to a one-point poset. Thus the initial written “couple F subset G” needs clarification; the square describes general refinements, and the frozen symbol has not been replaced.

The inverse image of a \(G\)-saturated subset is \(F\)-saturated, because \(q i=\varphi p\); it is simply inverse image along \(\varphi\) on quotient subsets. This checks the inverse-image sentence on scan 025 with “modérée” interpreted as saturated, or with the finite-figure qualification of scan 006. By contrast a continuous identity/refinement need not carry closed subsets to closed subsets. On \(\{a,b\}\), let \(F\) be the discrete singleton figure and \(G=\{\{a\},\{a,b\}\}\); \(\{b\}\) is \(F\)-closed but not \(G\)-closed. The final direct-image sentence is unfinished, so this is a test for a future continuation, not a claim that the author asserts a false direct-image theorem here.

The Boolean qualification has an explicit infinite counterexample. Let \(F=\{\{n\}:n\in\mathbb N\}\), and let \(G\) consist of the even and odd subsets of \(\mathbb N\). Both are admissible and \(F\ll G\): the map from the discrete singleton index set to the two-point discrete index set is parity. The even set is a member of \(G\), hence is \(G\)-constructible in the ordinary Boolean sense, but it is not in the finite–cofinite Boolean algebra generated by \(F\). Thus preservation of saturated subsets must not silently be promoted to preservation of finite-Boolean constructibility for arbitrary infinite figures. This is a counterexample to that strengthened interpretation, not an alteration of the text's terminology.
