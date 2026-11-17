# Correct filled contact-source cohomology gate

Complete conversation proof relayed by CE in three parts, independently read by root and DE. This explicitly supersedes root's tentative claim that the relevant H1 map should be injective. All old source-byte bindings remain deferred during the execution outage; no formal promotion.

## 1. Exact FILLED quotient diagram and actual completions

Let Ggen=F11 semidirect S with ALL actual signed source operators. Let N be the full actual node kernel, the normal closure of all 40 ordinary node relators, equivalently their full signed source-orbit closure. Set Gamma0=Ggen/N with quotient p. The actual FILLED one-family map F_a:Gamma0->Gamma_a^0 kills the six family meridians deleted by B139's retained-a projection. Define q_a=F_a p and K_a^d=ker(q_a). Thus
K_a^d=normal_Ggen(N together with the six deleted meridians),
and N<=K_a^d.
This inclusion comes from the actual marked quotient presentation. The different PRE-node deletion used for the unfilled-double embedding does not establish it.

Historical locators, NOT fresh byte reads:
- Formal B139, complete marked one-family theorem.
- work_CE/one_family_graph_fixed_source28.txt, corrected final 7913056... edition retaining all 40 ordinary words/factors and all 20 whole orbifold node words.
- work_CE/one_family_kernel_reduction28.txt, final 052f63... exact-kernel reduction.
- work_CE/compact_one_family_fixed_source28.txt, final 4f2b2617....
- Formal B155 source work_CE/B155_single_fixed_coset_relative_kernel_proposed.tex, SHA687bd20fbac398eae3f962a3bbb486b893a6e5c40d6a3010610d7ab4345e1271.
- Formal B159 source work_CE/B159_pre_node_section_delta_defect_proposed.tex, SHA9151c7315f9407b6601bee9080c6e58ed98cf792c96a0fc624e54cbf472287c4.
The abbreviated historical hashes above are locators only, not new complete hash claims.

Inside the ACTUAL Ghat=hat(Ggen), write mathcalN=bar(N), Ka=bar(K_a^d). Right exactness of full profinite completion gives
Ghat/mathcalN=hat(Gamma0), Ghat/Ka=hat(Gamma_a^0),
so mathcalN<=Ka.
Let J=(Gamma_a^0)^delta=<A,m,v | [A,m]>, with generic section lambda and filled section sigma. B139/B154 identify the ACTUAL completed one-family fixed group with embedded Jhat and prove its section topology.

For P=q_a^(-1)(J), the actual identity is
bar(P)=Ka semidirect lambdahat(Jhat)=qahat^(-1)(Jhat).
The compact product contains P densely; its intersection is trivial by applying qahat to the embedded section. Conversely any element mapping into Jhat can be divided by its section value. No hat(P)=bar(P) or hat(K_a^d)=Ka is assumed.

## 2. Surviving pre-node classes

The generic fixed theorem gives Ghat^delta=Shat. Since q_a is injective on that source, Ka^delta=1 and bar(P)^delta=Shat.

For U=bar(R), the already proved finite-factor torsion/compactness argument gives
H1(delta,U)=Jhat/Shat,
represented by X_j=delta(lambda(j))lambda(j)^(-1).
Its map into H1(delta,Ka) is injective. To keep conjugation conventions explicit, if
k^(-1)(X_j tau)k=X_l tau,
then delta(lambda(l))^(-1) k^(-1) delta(lambda(j)) centralizes tau. It is even, so belongs to Shat; applying qahat gives l^(-1)j in Shat.

Its image is exactly ker[H1(delta,Ka)->H1(delta,bar(P))], by the complete split-closure argument already stored in the unfilled-cohomology proof. Since U<=mathcalN<=Ka, H1(delta,U)->H1(delta,mathcalN) is also injective. Its image meets ker[H1(delta,mathcalN)->H1(delta,Ka)] only at the basepoint. These surviving coset classes do not exhaust the nodal cohomology.

## 3. Actual fixed subgroup after filling

The section defects X_j lie in U<=mathcalN. Therefore
bar(P)/mathcalN=(Ka/mathcalN) semidirect sigmahat(Jhat),
and delta fixes the second factor. Its fixed subgroup is
(Ka/mathcalN)^delta semidirect sigmahat(Jhat).

Every fixed element of hat(Gamma0) maps to a fixed element of hat(Gamma_a^0), and the latter fixed group is precisely Jhat. Thus every fixed element belongs to this actual preimage. The formula describes the WHOLE fixed subgroup of this specified actual Gamma0.

For the exact sequence
1 -> mathcalN -> Ka -> Ka/mathcalN -> 1,
define partial(h)=[t^(-1)delta(t)] for h fixed and any lift t in Ka. The representative is a cocycle in mathcalN. Replacing t by t n changes it to n^(-1)c delta(n), so the class is well defined.

The map partial is injective because Ka^delta=1. If two classes agree, alter one lift by n in mathcalN so that their cocycles coincide. The ratio of the adjusted lifts is then delta-fixed in Ka and hence is 1. Its image is exactly
ker[H1(delta,mathcalN)->H1(delta,Ka)]:
a class trivial in Ka is represented by t^(-1)delta(t), and t mathcalN is fixed. Here kernel means the inverse image of the distinguished point; H1 is not assumed to be an abelian group.

## 4. Correct contact-source comparison and explicit nonzero class

Let H_src be the ACTUAL six-source subgroup and I_src=H_src intersect K_rem, where K_rem=ker(F_a). B150 gives
H_src=I_src semidirect sigma(J),
with I_src normally generated by the three discarded contact elements B_s,D_s,E_s. B154 gives the ACTUAL closure identity
bar(H_src)=bar(I_src) semidirect sigmahat(Jhat),
bar(I_src)=bar(H_src) intersect bar(K_rem),
where bar(K_rem)=Ka/mathcalN.
No abstract completion of I_src is substituted.

The remaining specified fixed-source comparison is EXACTLY
(Ka/mathcalN)^delta=bar(I_src),
equivalently
ker[H1(delta,mathcalN)->H1(delta,Ka)]=partial(bar(I_src)).
It is NOT injectivity of the H1 map. Root's earlier tentative injectivity gate is preserved explicitly as SUPERSEDED by this correction.

Indeed the left-hand kernel is already nontrivial. Let tilde(D_s) be the literal generic prelift of the actual contact D_s. B150 gives F_a(D_s)=1, so tilde(D_s) lies in K_a^d. Since D_s is fixed, the word
c_D=tilde(D_s)^(-1)delta(tilde(D_s))
lies in N and is a cocycle. It becomes a coboundary in Ka by this same lift. It is NONTRIVIAL in H1(delta,mathcalN), because partial is injective and B132 proves D_s remains nontrivial in the actual completion: <m,D_s> is F2 with full induced topology.

Historical locators: work_CE/even_sum_m_free_subgroup26.txt; work_A/actual_free_source_pair_full_topology26.md, final SHA9c0c11989ecaf61b79a45a113592c9035659c379c9c495c7a81bdd91185cc145; formal B150; work_DE/next_marginal_source/review_remaining_fixed_kernel_contact30.md/.json; retained one_family_sources28 JSON. These remain deferred bindings, not fresh file reads.

This known contact class lies outside the ENTIRE nonbase image of H1(delta,U), because its image in H1(delta,Ka) is trivial whereas that map is injective on H1(delta,U).

## 5. Ordered formulas for the actual contact-word classes

Choose generic lifts t_C in K_a^d for C in {B_s,D_s,E_s}, and put c_t=t^(-1)delta(t). Products obey
c_(tu)=u^(-1)c_t u c_u.

For T=lambda(j)t_C lambda(j)^(-1), put kappa_j=delta(lambda(j))lambda(j)^(-1) in R. The exact formula is
c_T=T^(-1)kappa_j T
    lambda(j)c_(t_C)lambda(j)^(-1)
    kappa_j^(-1).
It follows by substituting delta(lambda(j))=kappa_j lambda(j) and delta(t_C)=t_C c_(t_C). These corrections must be retained; the source classes are not an additive or normal span in H1 and are not the naive J-conjugation orbit of the three elementary classes.

The connecting injection is continuous. Its lift map on the compact preimage of fixed cosets is continuous and descends through that compact quotient. The H1 orbit space is Hausdorff because its equivalence relation is compact and closed. Consequently
partial(bar(I_src))=closure(partial(I_src)).
The exact remaining compact gate says that EVERY nodal cocycle which becomes a Ka-coboundary lies in this closed set of actual all-contact-word classes.

This is the precise annular/one-family fixed-source comparison in the specified Gamma0. It does not by itself prove the B75 uniform characteristic-neighborhood criterion or the broader original Main-B/icosahedral conclusion.
