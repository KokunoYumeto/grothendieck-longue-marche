# Exact change of cohomology after a stabilized abelian layer

Status: abstract formula reviewed by the parent, explicit independent next cocycle certified, and incorporated as formal A.54. This identifies the new-base limitation of A53; it is not a negative norm obstruction.

## General formula

Let R=R_nil(K0), C=Pi/R, W and V=R/W be as in A53, and let W_m be its stabilized scalar kernel. Put

    P=R/W_m, C'=Pi/W_m.

Then P is finite nilpotent of class at most2 and P^ab=V. Let T be a finite C-module such that, for each prime p dividing its order, the actual normal pro-p' subgroup N_(p') of N=K0/R has no invariants on T_p. Equivalently, the relevant odd-to-p action is sensitive in the exact sense used in A53. Then

    H^j(C,T)=0 for every j>=0,
    H1(C',T) = Hom_C(V,T),

with the second isomorphism given by restriction to P. Here T is inflated to C', so P acts trivially.

Proof: continuous cohomology of N_(p') with finite p-primary coefficients vanishes in positive degree by finite averaging, and degree0 vanishes by the stated invariant condition. The profinite Hochschild–Serre spectral sequence therefore gives H^j(C,T_p)=0 in every degree. The inflation–restriction sequence for 1->P->C'->C->1 then identifies H1(C',T) with H1(P,T)^C=Hom_C(P^ab,T)=Hom_C(V,T). No splitting of C' over C is assumed.

Primary exact source: Poonen, B. (2017), Rational points on varieties, Graduate Studies in Mathematics186, AMS, Theorem6.7.3 and Corollary6.7.4, printed p194, author's PDF https://math.mit.edu/~poonen/papers/Qpoints.pdf . Opened directly and inspected at PDFpage207 (zero-based), webref turn502view0; exact statements found as turn503view0/1. Metadata independently checked on author's errata/CV and AMS DOI10.1090/gsm/186. The original-source input here is only the standard continuous spectral/five-term sequence; all applications and module checks are proved above and in A53.

For T=V, the no-invariant hypothesis follows from A53's actual N_(p') coinvariant argument and finite averaging. Hence

    H1(C',V) = End_C(V).

It is nonzero whenever V is nonzero. Thus automatic vanishing on the initial pronilpotent base does not persist for every coefficient module after adjoining a stabilized layer.

## The failure can occur for a legitimate next residual layer

Use the single-head A51 construction. Write U=V there (the42-dimensional simple), so the first residual abelianization is

    V0=U direct-sum U^vee.

The two modules are distinct, each has endomorphism fieldF2, and H1(Pi,U) and H1(Pi,U^vee) each have dimension7. The formula above gives

    dim_F2 H1(C',U)=dim_F2 H1(C',U^vee)=1.

Choose the normalized cocycle with s-value0 and r-value zeta² e1 in U^vee. The original class has r-value e1. The exact certificate gives normalized coboundary rank21, rank22 after the original class, and rank23 after both, so the new class lies outside the one-dimensional inflation subspace in H1(Pi,U^vee). Its restriction to R'=W2 is nonzero. Since R' acts trivially on U^vee (the coefficient action factors the old C), that restriction is a continuous homomorphism. It is Pi-equivariant; irreducibility makes its image all of U^vee. Its kernel W' is closed normal in Pi and

    R'/W' = U^vee.

But the coefficient group required for the conditional A53 theorem on this next base is (U^vee)^vee=U, and H1(C',U) has dimension1. Thus the automatic cohomology hypothesis genuinely fails for an actual next elementary residual layer, even though R'=[R',Pi] is stabilized.

This does not show that the next scalar refinement or negative lift is impossible. One may instead return to the initial base and include both independent affine cocycles at once; the joint residual abelianization is still finite abelian, so A53 applies there. The result locates the exact obstruction to a naive step-by-step application of its automatic-H1 clause.
