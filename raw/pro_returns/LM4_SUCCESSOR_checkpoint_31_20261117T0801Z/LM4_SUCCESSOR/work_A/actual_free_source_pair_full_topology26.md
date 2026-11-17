# Full induced topology of the actual free source pair

Late research proof, checkpoint26. This strengthens the discrete free-pair result in CE's `even_sum_m_free_subgroup26.txt`. It changes no frozen formal source. Independent complete review is required before acceptance; the finite construction below involves no target census or new producer.

## 1. The exact quotient already proved

CE constructs an actual epimorphism

    P=W2 semidirect <m> -> G=(<D0>*R) semidirect_alpha <m>,
    R=F(B)*T2,

where W2 is the actual index-two kernel of chi_sum modulo2 in W, T2 is the index-two subgroup of T=F(f,g,x), and alpha preserves R, fixes D0, and satisfies

    alpha(B)=kappa B kappa^-1, kappa=f^-1g.

The actual source Ds maps to d=B^-1D0B. The entire integer family is

    alpha^r(B)=B_r=kappa_r B kappa_r^-1,
    kappa_(2r)=q^-r f q^r f^-1, q=gf,
    kappa_(2r+1)=q^-r(f^-1g)(fg)^r.

CE's simultaneous Schreier-basis proof establishes that H=<m,d> is free on those two words, and hence the actual <m,Ds> in Gamma0 is free on the corresponding words. We use this exact quotient, not an assumed equivariant section of its free-seven fiber.

## 2. A finite orbit-divisibility lemma in the actual R

For every positive integer n there is a characteristic finite-index subgroup C of the finitely generated free group R such that the orbit of the image of B under the induced alpha automorphism of R/C has length divisible by n.

To prove this, first consider a finite quotient Q of T2 that is the product of two explicit finite images. The first is the f-exponent modulo2. Every odd kappa_(2r+1) has f-exponent-1, so its image in this factor is nonzero. The second is the restriction to T2 of the homomorphism

    F(f,g,x) -> UT3(Z/n),
    f -> (1,0,0), g -> (0,1,0), x -> 1,

using the multiplication (a,b,c)(a',b',c')=(a+a',b+b',c+c'+ab'). In this class-two group q=gf has abelian coordinates(1,1), so

    q^-r f q^r f^-1 -> (0,0,r).

Thus kappa_(2r) can be trivial in Q only when n divides r. The assertion is also valid for n=1. Both maps are defined on the entire T2; its displayed words kappa_r lie in that subgroup.

Map R=F(B)*T2 to the finite wreath product C2^Q semidirect Q by sending B to the nonzero lamp at the identity of Q and sending T2 to Q. Conjugation transports that single lamp, so equality of the images of B_r and B forces the image of kappa_r in Q to be one. This implies r is divisible by2n.

Let K be the kernel of this finite R map. Choose a characteristic finite-index subgroup C of R contained in K: the intersection of all subgroups of R of index at most [R:K] is such a subgroup. There are only finitely many subgroups of bounded index because R is finitely generated, so this is a finite-index characteristic subgroup. In particular alpha induces an automorphism a of the finite group Rbar=R/C. If a^r(Bbar)=Bbar, then B_r and B have equal images in the earlier finite target, so 2n divides r. The finite a-orbit of Bbar therefore has length divisible by n. No assertion is made that the original wreath quotient itself is alpha-invariant; the characteristic refinement supplies that point.

## 3. Extend an arbitrary finite quotient of the free pair

Let psi:H->A be any homomorphism to a finite group, and write

    u=psi(m), z=psi(d), n=order(u).

Choose Rbar and a from Section2. Let ell be the length of the a-orbit of Bbar; n divides ell. Put K_A=A^Rbar semidirect Rbar, using the left regular action

    (r.f)(s)=f(r^-1 s).

Define an automorphism theta of K_A by

    theta(f,r)=(f_theta,a(r)),
    f_theta(s)=u f(a^-1(s)) u^-1.

This is an automorphism because a intertwines the left regular actions. Choose a positive M divisible by both order(a) and order(u). Then theta^M is the identity, and u^M=1. We can form the finite group

    K_A semidirect_theta C_M,

with the cyclic generator denoted mstar.

Define a function F0:Rbar->A by

    F0(a^j(Bbar))=u^j z u^-j,

and set F0=1 off this orbit. It is well-defined because n divides ell. It satisfies F0(s)=u F0(a^-1(s))u^-1 for every s. Therefore theta fixes (F0,1).

Send D0 to(F0,1), send R to its quotient Rbar in K_A, and send m to mstar. The free-product universal property first gives a map <D0>*R->K_A. It is compatible with alpha: D0 is fixed, the R map is a-equivariant, and the whole action on R is exactly the already proved alpha. Consequently it extends to a homomorphism

    Phi:G -> K_A semidirect_theta C_M.

The images of m and d=B^-1D0B lie in the subgroup A^Rbar semidirect C_M, which has no Rbar component. On this subgroup the formula

    Ev(f,mstar^j)=f(1)u^j

is a well-defined homomorphism to A. Indeed a fixes the identity element of Rbar, so theta acts on the identity coordinate by conjugation by u; also u^M=1 makes the formula independent of the cyclic representative. The left-translation convention gives

    Ev(Phi(d))=(Bbar^-1.F0)(1)=F0(Bbar)=z,
    Ev(Phi(m))=u.

Thus Ev composed with Phi equals the prescribed psi on H. In particular ker(Phi) intersect H is contained in ker(psi). Every finite quotient kernel of H therefore contains the restriction of a finite quotient kernel of G. This is precisely the full induced profinite topology on H in G.

The proof extends an arbitrary finite target, not only a single commutator witness. It does not require the free-seven section in CE's quotient to be m-equivariant.

## 4. Transfer the topology through the actual quotient and ambient group

The actual map P=W2 semidirect <m> -> G restricts to the identified isomorphism from <m,Ds> onto H. Pulling back Phi therefore proves the full induced topology of the actual pair in P.

For completeness, P has its full induced topology in Gamma0. One can use the following direct finite-target argument with W, which is finitely generated. Put Pbig=W semidirect <m>. Given a finite quotient rho of Pbig, choose a characteristic finite-index subgroup W0 of W contained in ker(rho) intersect W. The full free source S=F(m,v) acts on the finite group W/W0. Let n be the order of rho(m). Map S to the product of that finite action group with C_n by giving m cyclic coordinate1 and v cyclic coordinate0. This is a homomorphism because S is free on the actual two source lifts. The resulting finite semidirect quotient of Gamma0 has, on Pbig, kernel contained in ker(rho): a kernel element w m^j has w in W0 and n dividing j. Thus Pbig has the full topology in Gamma0.

The subgroup P=W2 semidirect <m> has finite index two in Pbig, since m preserves chi_sum. Every finite-index subgroup has its full induced profinite topology, by taking finite-index cores. Hence P also has its full topology in Gamma0. Equivalently one can apply the same characteristic refinement directly to W2 and then core through the actual index-two subgroup of Gamma0.

Combining these comparisons proves that the actual subgroup

    <m,Ds> <= Gamma0

is a discrete free group of rank2 with full induced profinite topology. Its closure in the actual full completion is therefore isomorphic to the free profinite group of rank2, with the two specified actual source generators. This conclusion concerns this pair only, not all five or six source generators, and it does not decide the selected fixed-source equality.

## 5. Review and evidence scope

The finite construction here is symbolic and uniform in the arbitrary finite target A; no finite groups are enumerated and no new numerical producer is needed. It depends on the fully reviewed actual free-seven quotient and all-integer kappa formulas in

    work_CE/even_sum_m_free_subgroup26.txt,
    work_CE/code/compile_even_sum_m_quotient26.py/.out/.err.

The two critical conventions are retained explicitly: left regular translation gives (B^-1.F0)(1)=F0(B), and alpha_s=Ad(s) fixes the cocycle order. The proper topology is proved by finite kernel containment, not by confusing a subgroup completion with an ambient closure. This note remains late research pending complete independent review; proposed B131 is unchanged and has no PDF build before capture26.
