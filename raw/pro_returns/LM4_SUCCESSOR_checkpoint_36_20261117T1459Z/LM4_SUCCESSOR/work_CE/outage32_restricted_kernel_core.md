# The exact restricted defect kernel and its actual compact closure

Conversation-stage proof and independent review during the execution-environment outage. No saved-file or execution claim was made at that stage.

## 1. Established marked inputs

Use G_gen=F11⋊S, S=F(m,v), delta=Ad(tau), and E_gen=G_gen⋊C2(tau). Let N be the complete actual node normal closure, with every signed source/deck translate, so E_actual=E_gen/N. Let q_a:G_gen→Gamma_a be the actual one-family quotient and J=Gamma_a^delta=<A,m,v|[A,m]>. Set P=q_a^-1(J), K_gen=ker(q_a), P_+=P⋊<tau>. The proved generic section lambda:J→P sends A to A0=aa*, a*=tau a tau, and fixes m,v. Its filled image is the actual marked section sigma:J→Gamma0. The induced full topology on sigma(J), and its embedded completion, are already proved. B159 gives c0=delta(A0)A0^-1=[a*,a] and N_lambda=normal_P(c0), which is delta-stable and contained in N. These facts are inputs; no new pre-node graph decomposition is assumed below.

Define the ACTUAL subgroups D_+=<A0,m,v,tau>≤P_+ and D0=D_+∩G_gen, and R=normal_D+(c0). The original orientation is zero on A0,m,v and one on tau, hence R≤D0.

## 2. Exact ordinary restricted kernel

The existing generic relations give [A0,m]=[tau,m]=[tau,v]=1 and tau²=1. Modulo c0, tau also commutes with A0. Therefore there is a surjection

J×C2(tau) → D_+/R,

induced by the four named generators. This uses only these valid relations; it does not assume a complete unfilled presentation for D_+.

The further map to E_actual sends the first factor to sigma(J) and tau to the actual selected cone. Sigma is injective, and the original orientation separates its ordinary image from tau, so sigma(J)×C2(tau) embeds. The composite of the displayed surjection with this final map is the canonical isomorphism J×C2→sigma(J)×C2 on all four generators. Consequently both maps are isomorphisms, and

ker(D_+→E_actual)=R.

As R≤N_lambda≤N, it follows exactly that

N_lambda∩D_+=N∩D_+=R.

The same argument with q_a and the already identified one-family image J×C2 gives K_gen∩D0=R. Thus D0/R=J and the induced involution is the identity.

## 3. Actual compact closure, without an abstract completion identification

Take all closures in the actual full completion of E_gen. Let R_D be the closed normal closure of c0 in bar(D_+). By density and continuity of conjugation, R_D equals the ambient closure of the ordinary subgroup R. The final image of bar(D_+) is sigmahat(Jahat)×C2, isomorphic to Jahat×C2 by the established full topology of the marked section and original orientation.

The compact quotient bar(D_+)/R_D receives a continuous surjection

Jahat×C2 → bar(D_+)/R_D:

the four generators satisfy the displayed J×C2 relations, their discrete image is dense, and full completion supplies the map. Its composite to the final image is the canonical isomorphism Jahat×C2→sigmahat(Jahat)×C2, checked on the same four generators. Hence both compact maps are isomorphisms. Therefore

closure(N_lambda)∩bar(D_+)=closure(N)∩bar(D_+)=R_D.

No assertion hat(D_+)≅bar(D_+) or hat(R)≅bar(R) is made or needed. The finite orientation character gives bar(D0)=bar(D_+)∩ker(orientation); consequently bar(D0)/R_D≅Jahat.

## 4. Fixed creation and scope

The established generic fixed-group equalities are G_gen^delta=S and G_genhat^delta=Shat. Since D0 contains S, they imply D0^delta=S and bar(D0)^delta=Shat. The quotients D0/R=J and bar(D0)/R_D=Jahat are wholly fixed. Also R^delta=1 and bar(R)^delta=1: R is in K_gen, its actual closure maps trivially under q_ahat, and the source subgroup S/Shat maps injectively under that same quotient.

Thus this particular complete source-orbit subgroup has an exactly known ordinary and closed defect kernel, and the full J is created as fixed across it. This does not identify N_lambda with N in P, does not assert an ambient free factor or retraction, and does not prove K_rem^delta=I_src in the whole final group or its completion. Every other actual node and signed orbit remains in that unresolved ambient comparison.

The explicit unfilled amalgam and free all-cocycle basis are separate results requiring the existing B139 literal pre-node quotient input. This core proof does not require that input.
