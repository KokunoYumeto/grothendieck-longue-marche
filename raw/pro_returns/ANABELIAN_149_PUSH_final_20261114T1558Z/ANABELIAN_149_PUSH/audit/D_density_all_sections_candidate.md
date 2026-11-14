# Candidate: density-one integrality for every noncuspidal section of P1−3

## Scope

Let U=P1_Q−{0,1,∞}. Using the checked D.6 local theorem, every continuous full arithmetic section s:G_Q→π1(U) is Selmer. The claim below removes **birational liftability** from the density-one integrality conclusion for this specific U. It does not prove cofinite integrality or the section conjecture.

## Lemma A: a completed rational Kummer class trivial at almost all places at every level is trivial

Let A∈widehat(Q^×). Suppose that for every n≥1, the image of A in Q_p^×/Q_p^{×n} is zero for all but finitely many primes p (the finite exceptional set may depend on n). Then A=1.

Proof. Represent A modulo n by b_n∈Q^× and set F_n=Q(μ_n,b_n^{1/n}). If Gal(F_n/Q(μ_n)) had a nonidentity element τ, that element would act on the n roots of X^n−b_n by a nontrivial translation, so fix none. Chebotarev would give infinitely many primes, unramified in F_n and away from the numerator/denominator of b_n, whose Frobenius conjugacy class has this property. At those primes X^n−b_n has no Q_p-root, contradicting the assumption. Thus F_n=Q(μ_n).

After multiplication by a suitable 2n-th root of unity, the positive real root r=|b_n|^{1/n} lies in Qab. The extension Q(r)/Q is therefore abelian, hence Galois. It is a subfield of R, so every conjugate of r is real. All those conjugates are roots of X^n−|b_n|, which has at most two real roots. Thus r²∈Q, and b_n²=(r²)^n∈Q^{×n}. Every finite-level component of A consequently has order dividing2, and A²=1.

The only torsion of widehat(Q^×) is {±1}. Indeed Q^×={±1}×⊕_q q^Z, and its power completion embeds, by all valuations, into {±1}×∏_q Zhat; the second factor is torsion-free. Finally A=−1 violates the assumption at n=2 at every prime p≡3 mod4. Hence A=1.

The argument deliberately avoids the false assertion that a **single** nth-power class which is locally trivial almost everywhere must vanish: the classical 2-primary exception can occur. For example16 is an eighth power in every Q_p for odd p but is not an eighth power in Q. Here is the complete local check. If p≡3,5,7 modulo8, gcd(8,p−1) equals2,4,2 respectively; in the cyclic group F_p^×, the eighth powers are the corresponding squares, fourth powers and squares, and16 belongs to each. If p≡1 modulo8, quadratic reciprocity gives (2/p)=1; choosing r²=2 in F_p gives r⁸=16. Every root is nonzero and the derivative8r⁷ is nonzero modulo odd p, so Hensel lifts it to Q_p. A rational eighth root of16 would have2-adic valuation1/2, impossible. Compatibility across all n is essential above. Exact Legendre matrix checks and representatives of these four residue cases are in `code/D_legendre_density_certificate.py` and its JSON output.

## Lemma B: the triangular Legendre alternative fixes one cusp modulo2

Suppose a Selmer section s of U is in the second case of Stix's Theorem10. Thus all but finitely many places are cuspidal or degenerate, and the Legendre representation at2 has the form

\[
 \rho_{s,2}\sim
 \begin{pmatrix}\delta\chi_2&*\\0&\delta\end{pmatrix}.
\]

At every sufficiently good odd prime p, let c_p∈{0,1,∞} be the cusp approached by x_p, including exact cusp points. The local specialization calculation (equation(5.1) in Stix's proof of Theorem20) says that rho_s(G_Qp) cyclotomically normalizes the maximal unipotent group containing the image of the **geometric cusp inertia** at c_p (use the square at∞). This calculation concerns a specified local point/cusp and specialization of the geometric pro-2 group. It does not require a birational lift. If desired one first passes to a finite étale neighbourhood on which the entire representation has pro-2 image; such a neighbourhood exists because the image of s already lies in a pro-2 group. In the Legendre family the rational full2-torsion already makes its full arithmetic image congruent to1 modulo2.

The two local situations must be distinguished. At an ordinary degenerate point the local elliptic curve is potentially multiplicative, and after its at-most-quadratic splitting twist the inertia cocycle is m_p times the tame2-adic character with m_p a strictly positive ordinary integer. This is nonzero in Z_2, so the resulting transvection itself determines the Tate cyclotomic line. At an exact cusp the tangent cocycle may be a unit or zero, and its arithmetic inertia image can be trivial. No nonzero-transvection assertion about the section is made in that case. Instead the section lies in the cusp decomposition group, which normalizes the nontrivial **geometric** inertia group through χ_2. The image of this geometric inertia (or its square at∞) is still a nontrivial unipotent group U_c, independently of the chosen tangent cocycle. Hence U_c is cyclotomically normalized even when the local section representation splits.

The displayed triangular representation has a unique maximal unipotent group on which conjugation by G_Qp acts as χ_2. Its fixed line is the δχ_2 line; the quadratic δ cancels in the conjugation character. In the locally split case the other eigenspace gives conjugation character χ_2^{-1}, and these characters are distinct because χ_2(Frob_p)=p and p²≠1 in Z_2. In the locally nonsplit case the invariant line is unique. Consequently its cyclotomically normalized line is the fixed global line L of the upper triangular representation, independent of p. This identifies the χ-normalized line, not merely an arbitrary stable line.

Stix's explicit Legendre monodromy (Lemma17) is

\[
 T_0=\begin{pmatrix}1&2\\0&1\end{pmatrix},\quad
 T_1=\begin{pmatrix}1&0\\-2&1\end{pmatrix},\quad
 T_\infty=\begin{pmatrix}1&-2\\2&-3\end{pmatrix}.
\]

The fixed lines of T0,T1 and T∞² reduce respectively to(1:0),(0:1),(1:1) in P1(F2). Geometric conjugacy preserves these distinct reductions because the monodromy is congruent to1 modulo2. This is exactly Lemma19. Hence c_p is the same cusp c for all sufficiently good p.

This is only the part of Stix's proof of Theorem20 ending with constancy of β(y_v). We use β=id_U and introduce no extra punctures. The later Riemann–Roch step in that proof, which requires lifting to smaller opens to separate arbitrary boundary points, is unnecessary for the three rational cusps of U.

## Consequence

Let s be any continuous section of U. D.6 plus the real theorem makes s Selmer. Apply Stix Theorem10 to the Legendre family, which has bad, not potentially good, reduction at all three boundary points. Its first alternative is the desired density-one integrality; asymptotic integrality is also part of that theorem.

In the second alternative, LemmaB gives one cusp c approached at almost all primes. Choose a nonconstant global unit

\[
 f=1-t\ (c=0),\qquad f=t\ (c=1),\qquad
 f=t/(t-1)\ (c=\infty).
\]

It is regular and has value1 at c. Let A=s^*κ(f)∈widehat(Q^×). For an ordinary local point approaching c at a good prime p, f(x_p)∈1+pZ_p. For an actual cusp section at c, the pullback of f is exactly its residue value1, irrespective of the tangent cocycle, because f is regular and nonzero at c. Therefore for any fixed n, A is an nth power in Q_p at almost all p: exclude p|n and use Hensel on1+pZ_p. LemmaA gives A=1.

At any prime where s_p were an interior point section, full local Kummer injectivity would give f(x_p)=1. None of the three listed functions takes the value1 at an interior point of U: the unique solution on P1 is the corresponding cusp. Thus every finite-local section is cuspidal, and the local support lies in the fixed finite set{0,1,∞}. Stix's finite-support argument, Corollary5 with its proof and Stoll8.2, then makes s globally cuspidal. The real-place formulation is the usual component convention; the finite-place support condition alone suffices in the Stoll step.

Accordingly every **noncuspidal** continuous section of U is asymptotically integral and integral on a set of primes of Dirichlet density one. No cofinite conclusion is obtained. The exceptional triangular alternative is characterized here as cuspidal without a birational-liftability assumption.

## Sources actually opened

- Stix, primary arXiv:1203.3236v3, <https://arxiv.org/pdf/1203.3236>, Theorem10 pp.9–11, Lemmas17–19 pp.13–15, proof of Theorem20 pp.15–16, particularly equation(5.1), and Corollary5 p.5. The complete corresponding supplied TeX passages were also read.
- D.6 and D.19 for finite-local sections, D_Mochizuki2003Real Corollary3.13 for the real place.
- LemmaA is proved here from Chebotarev and the elementary structure of Q^×; no unproved local-global nth-power assertion is invoked.

Status: independently reviewed and approved by root; promoted as D.25 in `sections/D_density_extension.tex` on 2026-11-14. The integrated statement also includes the reviewed finite étale cover extension. The intrinsic cofinite-integrality and neighbourhood-compatibility problems remain unresolved.
