# Independent audit of the rank-97 congruence-cover detector

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 16 November 2026.
This records the audit sent to the root agent; the integrated theorem is maintained there.

Let B=C2 amalgam C3, let q:B→Q=SL2(Z/12)/{±I} be the fixed quotient of order576, and let N=ker(q). Because q is injective on both finite factors, the Bass–Serre quotient graph gives N free profinite of rank97. Put M=N^ab and C1=Zhat[Q], C0=Zhat[Q/C2]⊕Zhat[Q/C3]. There is an exact Q-module sequence

0→M→C1→C0→Zhat→0.

Write L=ker(C0→Zhat). Its invariant elements are (a sum[Q/C2],b sum[Q/C3]) with 288a+192b=0, so L^Q=Zhat(2,−3). The image of the edge norm in C1^Q is precisely (2,−3). Since C1 is induced from the trivial subgroup, all its positive-degree cohomology vanishes. Thus H¹(Q,M)=0.

The same sequence gives a sharper finite bound than annihilation by |Q|: H²(Q,M)=H¹(Q,L). From 0→L→C0→Zhat→0, the vanishing H¹(Q,C0)=H¹(C2,Zhat)⊕H¹(C3,Zhat)=0 gives

H²(Q,M) ≅ Zhat/(288,192) ≅ Z/96.

The action Q→Aut(M) is faithful, and faithful already modulo576. For q≠1, its character on M is

tr(q|M)=1−fix(q;Q/C2)−fix(q;Q/C3).

An element different from1 cannot have fixed cosets in both terms: a fixed coset would make it conjugate to an element of that cyclic factor, so its order would have to divide both2 and3. Consequently 0<97−tr(q)≤384<576. Thus no q≠1 acts as the identity modulo576.

Suppose an actual multiplier-one gentle automorphism α acts as the identity on M/576. The covariance equation with the Q-action then forces α_Q=id. On Γ_576=B/(N'N^576), α fixes both kernel M/576 and quotient Q, so its discrepancy is an actual cocycle c∈Z¹(Q,M/576); this works without assuming the extension splits. Because H¹(Q,M)=0, its cohomology class is identified by the connecting map with an element of H²(Q,M)[576]. Under reduction M/576→M/6, the connecting class is multiplied by576/6=96. This annihilates H²(Q,M), so the induced automorphism on Γ_6=B/(N'N^6) is inner.

The SINGLE separating homomorphism θ:B→E0 of FP.23 factors through Γ_6: its N-image is contained in the abelian exponent-six permutation module. Therefore the cusp-centralizer argument of FP.29 implies δ(α)=0. This is sufficient; one must not assert that the all-Hom characteristic core Q* factors through B/N', since its component homomorphisms can have different maps to Q.

For the full integral action, α_M=id forces λ=1: the normalized action sends τ to τ^λ, and the nonzero primitive cusp class [τ^12]∈M is multiplied by λ. The multiplier-one result therefore shows ker(α_M)⊂ker(Δ) on full GT0. Hence Δ factors through the continuous image in GL97(Zhat), and through some finite coefficient reduction. The explicit modulus576 above has only been proved for the multiplier-one subgroup; the full-group finite modulus requires the extra multiplier-normalization argument or another theorem.
