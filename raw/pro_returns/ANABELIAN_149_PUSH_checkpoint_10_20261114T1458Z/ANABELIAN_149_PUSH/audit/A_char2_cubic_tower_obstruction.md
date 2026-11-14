# Characteristic-two genus-two towers: two exact method obstructions

Status: independently approved by root and integrated as A.C2.9–A.C2.10; not a counterexample to A1.
Prepared by the Part A agent after checkpoint06. This note does not alter the
accepted A.C2.1–A.C2.8 results or their files.

## 1. The whole first cubic compositum can remain ordinary

Let Ω be an algebraic closure of F₂, choose α in F₄ with α²+α+1=0, and let

\[
C:\quad y^2+y=x+1/x+\alpha/(x+1).
\]

The accepted A.C2.2 proves that C is ordinary of genus two and that every
connected cyclic étale cubic cover of C is ordinary. Its proof is exhaustive:
all nonzero classes in J_C[3] are represented by reduced degree-two divisors,
and the elliptic reflection quotient is supersingular precisely when
(a+b+c)³+abc=0. Here that expression is 1+α, which is nonzero.

Fix a Weierstrass point W of C, and form the pullback U of [3]:J_C→J_C
along the Abel map a_W:C→J_C. The Abel map induces the maximal abelian
quotient on the geometric fundamental group, so U is connected and

\[
G=\operatorname{Gal}(U/C)=J_C[3]\simeq(\mathbf Z/3)^4,
\qquad \deg(U/C)=81,\qquad g(U)=82.
\]

For each of the 40 index-three subgroups K of G, put D_K=U/K. These are
exactly the 40 connected cyclic cubic covers, without choosing a generator.
Write P_K for the connected Prym of D_K→C. It has dimension two. A.C2.2
constructs an elliptic reflection quotient E_K and proves

\[
J_{D_K}\sim J_C\times P_K,
\qquad P_K\sim E_K^2.
\]

Here every E_K is ordinary.

We verify that these factors exhaust J_U, not merely its dimension. In Q[G]
let e_H=|H|⁻¹∑_{h∈H}h. The idempotents

\[
e_G,\qquad e_K-e_G\quad(K\text{ of index }3)
\]

are pairwise orthogonal and sum to one. To check the sum integrally, each
nonzero element of F₃⁴ lies in 13 hyperplanes and zero lies in all 40, so

\[
\sum_K\sum_{h\in K}h=27\,1+13\sum_{g\in G}g.
\]

Equivalently 1=e_G+∑_K(e_K-e_G). Orthogonality follows either from this
hyperplane geometry or from e_Ke_L=e_G for distinct K,L, since KL=G.
Pullback and norm identify the e_G factor with J_C and the e_K-e_G factor
with the pullback of P_K. Thus the sum of these pullback maps is an isogeny

\[
J_C\times\prod_K P_K\longrightarrow J_U,
\qquad
J_U\sim J_C\times\prod_{40}E_K^2.                 \tag{1}
\]

The idempotents have only powers of three in their denominators, so the
decomposition also splits the geometric two-adic Tate module integrally.
There is no lost two-primary component. The dimensions in (1) are
2+40·2=82, as required by Riemann–Hurwitz.

Consequently U is ordinary. Every intermediate cover U/H is ordinary:
its Jacobian is an isogeny factor of J_U, using pullback and norm and the
odd degree |H|. Every map from U, or from an intermediate curve, to an
abelian variety of two-rank zero is constant. Indeed its Albanese
homomorphism has image both an ordinary abelian quotient and an abelian
subvariety of two-rank zero; that image has dimension zero.

This cover also fails the sufficient deck-kernel test A.C2.7. On the
two-adic Tate module, every nontrivial character pair of G occurs in one
P_K, and has kernel K. The nonzero characters therefore have common kernel
∩_K K={0}. Thus G acts faithfully on J_U[2](Ω). The same conclusion holds
for every nontrivial intermediate Galois cover U/H→C: its nontrivial
character pairs all occur and their common kernel in G/H is trivial.

For completeness the hyperelliptic involution ι lifts on the [3] pullback
by τ(P,z)=(ιP,−z), because a_W(ιP)=−a_W(P). It inverts G. Over each of
the three hyperelliptic branch points its action is an affine inversion
on the 81-element G-torsor, hence has exactly one fixed point. The local
étale map U→C identifies its local different exponent with that on C,
namely two. The total different is six, and

\[
162=2(2g(U/\langle\tau\rangle)-2)+6.
\]

The reflection quotient therefore has genus 40; it too is ordinary.
Combining every first cubic cover and all their reflection maps does not
create a two-rank-zero target. This leaves open whether their ordinary
targets can jointly detect all hypothetical section collisions.

## 2. An inertia obstruction throughout every equivariant odd étale tower

Let C/Ω be any genus-two curve in characteristic two, let ι be its
hyperelliptic involution, and let V→C be a connected odd-degree étale
Galois cover with group N. Assume ι lifts so that V→P¹ is Galois, with
group Γ in an exact sequence 1→N→Γ→C₂→1.

This equivariance is no restriction on choosing a further odd Galois
refinement of a given odd Galois cover: intersect the corresponding
normal subgroup of π₁(C) with its ι-transform. The resulting quotient
still has odd order and is ι-stable. The resulting extension by C₂
splits by the finite Schur–Zassenhaus theorem. Alternatively normalize
the fibre product with the ι-conjugate cover; the factor-swapping
involution fixes a component because the number of components is odd.

Every inertia subgroup of V→P¹ has order two. This follows directly
from the multiplicativity of ramification indices and the étaleness of
V→C. For every subgroup H⊂Γ and every point R of V, the inertia of
V→V/H at R is H∩I_R, so its order is either one or two. More generally,
all maps between intermediate curves of this Γ-cover have ramification
indices one or two.

It follows that no elliptic quotient obtained as an intermediate curve
in this tower supplies the odd common ramification index required by
A.21. Moreover, an odd subgroup H⊂Γ is contained in N, hence acts
freely on V. The quotient V/H is an étale cover of C of degree [N:H],
and

\[
g(V/H)=1+[N:H](g(C)-1)\ge2.
\]

Thus an odd-order Galois elliptic quotient of V cannot arise from a
subgroup of the specified tower group Γ. This does not exclude an
additional automorphism or a map not arising from that group. It also
does not refute A1. It identifies exactly why the accepted tame
orbifold theorem A.29l cannot simply be applied to the usual elliptic
Prym maps: those maps have wild degree two, and further odd étale
refinements retain only the indices one and two.

## 3. What remains to be constructed

The accepted A.C2.7–A.C2.8 already give a stronger positive route than
requiring the whole Prym to have two-rank zero. For a cyclic cover of
odd prime-power degree, killing all primitive doubling orbits makes
the deck action on two-primary torsion nonfaithful even if lower
conductor factors stay ordinary. In particular a Raynaud-theta point
of exact 3ᵃ order would suffice at every a≥1.

**Supersession, 2026-11-14:** A.C2.11 now supplies an explicit point of
exact order nine on the Raynaud theta of the curve in §1 and proves A1
for that curve. The first cubic-compositum obstruction proved above
remains valid; it is overcome at a higher exponent. Existence of a
suitable prime-power point for every genus-two curve is still unproved.

For arbitrary genus-two curves, the exact next obligations are: construct such a cover with
nonfaithful deck action, prove joint detection by ordinary Prym images
without assuming their two-primary differences vanish, or find a map
outside the hyperelliptically equivariant tower group to a curve whose
point sections are already separated. The obstructions above address
the stated methods only.

## 4. Finite certificate

`code/A_char2_cubic_tower_certificate.py` independently enumerates all
81 group elements and all 40 hyperplanes, verifies their intersection
and incidence counts, the integer group-ring idempotent identities,
the partition into the 40 nonzero character pairs, their trivial common
kernel, and the unique fixed point of every affine inversion. It uses
only integer arithmetic. Its output is saved beside it as JSON.

The mathematical identification of the group-ring factors with actual
Jacobians is supplied in §1; the finite calculation alone is not used
as a substitute for that identification.
