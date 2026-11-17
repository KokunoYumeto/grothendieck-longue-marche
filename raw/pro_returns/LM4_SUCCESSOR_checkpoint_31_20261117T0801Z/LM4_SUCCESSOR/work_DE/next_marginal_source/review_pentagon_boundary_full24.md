# Independent complete review of the pentagon boundary-subgroup proof

DE, checkpoint24. Full source read and algebraic audit: PASS, including the full induced topology and final DISCRETE neck intersection. No correction requested. This review does not assert a completed intersection or a post-cross-quotient injection.

## 1. Actual quotient and character

Killing regional a,b,d leaves exactly R_e=<C,k,z,e | C²,[C,z],[k,z],[k,e],[e,CeC]>. The selected c maps to C and full boundary T maps to z e k^{-1}. The five-cycle group is the kernel of the auxiliary delta(C)=1, delta(z,k,e)=0, not the original ordinary character. Its generators K=CkC and E=CeC and all five edge commutators follow by the complete two-coset rewrite.

## 2. Discrete embedding

With r=e^{-1}E, the P4 base is F(k,K,r) semidirect Z(e): e fixes k,r and sends K to r^{-1}Kr. Both the automorphism and its inverse are literal Nielsen substitutions. Setting s=ze produces the two relations [s,k]=1 and s(rKr^{-1})s^{-1}=K. The two edge subgroups <k,rKr^{-1}> and <k,K> are embedded free rank two subgroups of the base free group, and alpha identifies them. Thus the HNN group J has its base L embedded. The remaining e extension is precisely J amalgam_L (L semidirect Z(e)), so J embeds in the entire pentagon group by ordinary amalgam normal form.

Replacing r by s^{-1}q changes J exactly to Z²(k,s)*Z²(K,q). Here s=ze and q=zE. C swaps these two factors and has order two, so adjoining C yields C2(C)*Z²(k,ze). The actual marked <c,k,T> therefore embeds in R, because its map to this quotient is the isomorphism C2(c)*Z²(k,T), with ze=Tk. This is an injection proof by a genuine quotient detector, not a rank argument.

## 3. Full induced topology

The finite-target argument passes in full. Given a finite quotient psi of J, a characteristic finite-index N in the finitely generated free L can be chosen inside ker psi|L. Alpha preserves N, and hence maps the images of H0,H1 isomorphically in Q=L/N. The resulting finite-base HNN J_N is proper, and psi factors through it. The finite-order alpha quotient Q semidirect C_m is compatible with the same Q, so G maps to J_N amalgam_Q (Q semidirect C_m).

A finite quotient of J_N injecting Q can be combined with psi into a finite image F' which still injects Q and retains psi. A finite quotient of the proper finite-group amalgam F' amalgam_Q (Q semidirect C_m) can then be chosen injective on F'. The resulting finite G quotient has restriction kernel on J contained in ker psi. This proves precisely the required full induced topology; no virtual retract is assumed.

The supplied elementary finite-permutation construction is sufficient: choose free regular-multiple vertex actions of equal size, align edge restrictions, and for an HNN edge choose an intertwining permutation. All vertex groups inject. The kernel acts freely on the ordinary Bass-Serre tree and is finitely generated free. Characteristic finite-index refinements of that kernel give the stated residual finiteness. In fact the finite vertex-injective quotients already suffice at the two places used in the argument.

Intersecting the chosen finite-index normal subgroup of G with its C-conjugate gives a C-stable subgroup. Keeping the C2 coordinate in the finite semidirect quotient proves full induced topology of J semidirect C2 in G semidirect C2. Pullback through the actual regional quotient gives the full induced topology of <c,k,T> in R. All directions of containment are correct.

## 4. Corner retract

The map from the embedded j-even path graph product D--k--u--k'--c to the actual corner subgroup <c,k,T> given by D,k' to1, u to T, and c,k fixed respects each graph edge. It fixes T=uD and is a genuine retraction. Finite index then gives full induced topology in the entire auxiliary corner. This does not by itself prove properness of a profinite R/corner amalgam or survival under the four remaining mirror relations, as the source explicitly states.

## 5. Final discrete K/H intersection

The second HNN description is also exact. In H=C2(C)*Z²(k,s), its s-height kernel is the free product of <k> and all involutions C_n=s^{-n}Cs^n. Thus D0=<k,C,C'=s^{-1}Cs> is the indicated full free factor and is embedded. The displayed beta fixes k and r=C'C, sends C to CC'C and C' to C, and has the stated inverse.

For the Tietze comparison, [C,z]=1 with z=s e^{-1} is exactly e^{-1}Ce=C'. The node equation [e,CeC]=1 becomes [e,r]=1: using Ce=eC', its two sides are e²r and e r e. Together these give eCe^{-1}=Cr=r^{-1}C and eC'e^{-1}=C, precisely beta. Conversely those equations recover the original two relations. All other generators/relations are retained.

The height of p=C s k^{-1} is one, so every nonzero power p^n avoids both associated subgroups D0. A reduced word in e,p containing an e letter is therefore HNN-reduced after grouping its nonzero p powers; it cannot lie in H. Hence <e,p> is free2 and meets H exactly in <p>. The actual neck maps onto <e,f>=<e,p>, since p=f e using [k,e]=1, while the actual boundary subgroup maps injectively to H. This proves K intersect <c,k,T>=<P5> discretely. No completed intersection is inferred from induced topology or density.

The complete proof remains research-only at this checkpoint. MainA and MainB are Open.
