# Bounded actual scalar refinements for every finite abelian residual layer

Status: independently reviewed and accepted by the parent and CE; incorporated as formal A.53. This extends A53_general_scalar_working.md to all primes and arbitrary finite primary exponents. No negative-action or norm equation is solved by this theorem.

## The conditional theorem

Let Pi=C2 amalg C3, let R be closed normal with R=[R,Pi], and put C=Pi/R. Let W be closed normal in Pi, contained in R, such that V=R/W is finite abelian. Regard V as a continuous C-module. Assume

    H1_cont(C,V^vee)=0,

where V^vee=Hom(V,Q/Z) is the finite Pontryagin dual. Put W0=W and W_(i+1)=[W_i,Pi], with closed commutators. Let exp(V_2)=2^e2 and exp(V_3)=3^e3, taking e2 or e3 to be0 when the corresponding summand is absent. Set

    m=max(1,e2+1,2e3+1).

Then W_(m+1)=W_m. More precisely, for every i>=1:

* M_i=R/W_i has abelianization V and is nilpotent of class at most2;
* Z_i=W/W_i=M_i' is a finite quotient of wedge^2_Z V and is central in M_i;
* the Pi-action on its p-primary part Z_(i,p) factors through the maximal pro-p quotient of Pi, namely C2 for p=2, C3 for p=3, and1 otherwise.

Consequently, writing T_p for the relevant cyclic generator and I_p=T_p-1, the actual intermediate relative commutators satisfy, for j<=i,

    (W_j/W_i)_p=I_p^j Z_(i,p).

These are descriptions of actual quotients, not merely possible module extensions. The theorem does not identify Z_i with the entire exterior-square quotient.

For a finite elementary-abelian ell-group V the bounds specialize to

    W3=W2 for ell=2,
    W4=W3 for ell=3,
    W2=W1 for ell>=5.

If the finite action head has trivial maximal ell-group quotient, the corresponding primary center stabilizes at the first scalar step even for ell=2 or3.

## 1. Finite action heads and coinvariants

Let H be the finite action image of Pi on V. For each prime p let K_p=O^p(H), the kernel of the maximal p-group quotient. Since H is an actual quotient of Pi, H/K_p is generated only by s when p=2, only by r when p=3, and is trivial otherwise. In particular it is1 or C_p.

Relative perfectness implies (V_p)_H=0 for every primary summand. Taking K_p-coinvariants leaves a finite abelian p-group with an action of the finite p-group H/K_p and with zero coinvariants. The finite p-group Nakayama argument gives

    (V_p)_(K_p)=0.

One may avoid a group-ring citation: if U=[U,P] for a finite p-group P acting on a finite abelian p-group U, then U lies in every lower-central term of the finite p-group U semidirect P, hence U=0.

## 2. The exact finite-quotient abelianization induction

Put E_i=Pi/W_i and A_i=W_(i-1)/W_i, so the NEW A_i is globally central in E_i. Relative perfectness gives M_i=[M_i,E_i]. We prove M_i^ab=V by induction.

Take finite quotients of E_i retaining the given V quotient of M_i. They are cofinal: V is finite, and compactness/separation supplies an open normal subgroup whose intersection with M_i lies in ker(M_i->V); intersect it with any chosen open normal subgroup. The induced quotient of E_(i-1) also retains V, since an element projecting into M_(i-1) already lies in M_i.

In any such finite quotient, let B be the new R-preimage abelianization. By the induction hypothesis the preceding one is V. Thus the kernel A' of B->V is the image of the NEW globally central A_i and is a trivial C-module. The dual exact sequence is

    0 -> V^vee -> B^vee -> (A')^vee -> 0.

Relative perfectness gives (B^vee)^C=0. The invariants exact sequence and the stated H1(C,V^vee)=0 give (A')^vee=0. Hence B=V. Cofinality proves M_i^ab=V globally. This argument uses cohomology of the infinite retained C, not cohomology only of H.

Consequently the kernel Z_i=W/W_i is the closed derived subgroup M_i'.

## 3. Class two and finite derived centers by induction

For i=1, Z1 is globally central. Thus M1 has class at most2. Its commutator pairing is alternating and bilinear on the finite abelianization V, so Z1 is a quotient of wedge^2_Z V. It is finite and abelian. The Pi-action on it is trivial.

Suppose the conclusion holds at stage i-1. The preimage Z_i of Z_(i-1) satisfies [Z_i,M_i] subset A_i, which is globally central. Thus gamma4(M_i)=1 and [Z_i,Z_i]=1. The commutator therefore descends to a C-equivariant pairing

    Z_(i-1) tensor_Z V -> A_i.

The tensor product splits into its same-prime parts; mixed-primary tensor factors vanish. On the p-part the old center Z_(i-1,p) has p-group action through H/K_p by induction, while A_i is globally trivial. Since (V_p)_(K_p)=0, every such pairing vanishes. Therefore Z_i centralizes M_i.

Now Z_i=M_i' is a quotient of wedge^2_Z V, hence finite, with exponent on each p-part dividing exp(V_p). Its action factors through H by functoriality of the commutator pairing. The exact sequence

    0 -> A_i -> Z_i -> Z_(i-1) -> 0

has globally trivial new kernel and, on each primary part, an old action image that is a p-group. The kernel of the automorphism map fixing both subquotients embeds in Hom(Z_(i-1,p),A_(i,p)), a p-group. Therefore the entire finite action image on Z_(i,p) is a p-group and factors through H/K_p. This completes the induction for every i.

No assumption that the old center remains globally central is made. It is only central in M_(i-1), and its p-primary action through H/K_p is the exact input used to kill the next pairing.

## 4. Exact augmentation formulas and the bound

Inside the actual abelian group Z_i, relative commutators are augmentation images. Induction on j gives

    (W_j/W_i)_p=I_p^j Z_(i,p),  0<=j<=i.

For p>=5 the action is trivial, so I_p=0. For p=2, T^2=1 gives

    I^2=-2I,
    I^(e2+1)=(-2)^e2 I=0

on every group of exponent dividing2^e2. For p=3,

    I^3=-3I(1+I),
    I^(2e3+1)=(-3)^e3 I(1+I)^e3=0

on exponent dividing3^e3. When a primary summand is absent it contributes no constraint. With the displayed m, all I_p^m vanish. Apply the exact formula at i=m+1 and j=m: W_m/W_(m+1)=0.

An equality at one scalar step persists at every subsequent step because the next subgroup is defined by the same closed commutator operation. The derived centers thus remain finite and the final residual is relatively perfect with Pi.

## 5. Automatic cohomology over every relative-pronilpotent base

Let K0 be any closed normal subgroup of Pi, let R=R_nil(K0), and set C=Pi/R. A34 gives R=[R,K0], while N=K0/R is an actual closed normal pronilpotent subgroup of C. The conditional theorem applies to EVERY finite abelian quotient V=R/W of the stated kind, because its H1 hypothesis is automatic.

Fix p. Decompose N=N_p times N_(p'), using its characteristic Sylow factors. Since R=[R,K0], one has (V_p)_N=0. The finite group U=(V_p)_(N_(p')) has an action of a finite p-group image of N_p and has zero N_p-coinvariants. The finite p-group argument in Section1 gives U=0. Therefore

    (V_p^vee)^(N_(p'))=0.

Any continuous1-cocycle C->V_p^vee restricts to a coboundary on the normal pro-p' subgroup N_(p'), by finite averaging. More explicitly, its restriction factors through a finite p'-quotient after taking the core of an open subgroup on which both the action and cocycle vanish. Subtract a coboundary so the cocycle vanishes on N_(p'). Normality and the cocycle identity force every remaining value into the zero invariant space. Thus H1(C,V_p^vee)=0; summing the primary components gives H1(C,V^vee)=0.

This proof uses the ACTUAL closed normal N_(p') inside C. It does not infer cohomology of C from a finite quotient that happens to have an odd or p'-normal subgroup.

## Scope

The theorem settles the scalar-refinement depth for every finite abelian residual layer over an initial relative-pronilpotent base. It also applies to an enlarged base whenever its displayed H1 hypothesis is independently proved. It does not establish that this hypothesis persists through arbitrary nonabelian layers. It does not construct the required peripheral automorphism, retain its particular frames automatically, make its negative companion involutory, solve a nonabelian norm equation, or prove cofinality. Those are separate tasks.
