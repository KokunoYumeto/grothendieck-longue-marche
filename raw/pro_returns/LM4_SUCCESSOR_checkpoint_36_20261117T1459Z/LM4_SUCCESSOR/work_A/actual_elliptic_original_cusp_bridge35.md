# The actual elliptic boundary equation and the original third cusp

Checkpoint35 research continuation, separate from the frozen formal sources and from `actual_elliptic_pentagon_cubic35.md` (SHA ab9ccffba8f12ce224aab9fd3c812bfdf8b24d8117b61bf28c77490b291b196d). The purpose is an exact based comparison, not an inference of the missing boundary equation from the proved elliptic cubic.

## 1. Original data and the fully embedded pair

Let the original negative involution alpha belong to full GT. Retain its original parameter phi, canonical commutator word u, norm equation u=phi alpha(u), and duality for both phi and u. Write d=2k+1 for the actual canonical unit, with the same even k as in the preceding work. All evaluations below use these actual words.

In the free profinite group E=Fhat(X,Y), put

\[
 p=K=[Y,X],\qquad q=X,\qquad z=(pq)^{-1}=YX^{-1}Y^{-1}.
 \tag{1}
\]

This is an actual embedded free profinite pair. Indeed, the open kernel of the character E to C2 sending Y to the nontrivial element and X to one is free profinite on X, YXY^{-1}, Y^2, by the explicit index-two Schreier basis. The first two basis elements generate a retract/free factor. Replacing YXY^{-1} by (YXY^{-1})X^{-1}=p and retaining q=X is an inverse Nielsen basis change. Thus Fhat(p,q) embeds with its intrinsic full profinite topology in E. This argument does not identify the completion of an infinite-index kernel.

Set

\[
 u_0=u(p,q),\quad u_2=u(z,p),\quad
 U=u(q,p)=u_0^{-1},\quad V=u(z,p)=u_2,
 \quad \Phi=\phi(q,p),\quad Q=\phi(z,p).
 \tag{2}
\]

Enriquez's full profinite section, Proposition2.20 at lambda=-1, gives an actual involution Theta of E with

\[
 \Theta(X)=\Phi X^{-1}\Phi^{-1},\qquad
 \Theta(Y)=p^{-1}QY\Phi^{-1},\qquad
 \Theta(p)=p^{-1}.
 \tag{3}
\]

The last identity is the boundary-commutator identity in that same section proof. The completion and convention are bound in the predecessor note, which contains the complete primary-read record. No section is being applied to the still unproved pair (d,u).

## 2. Exact canonical equivariance of the candidate pair

Define the always meaningful endomorphism eta of E by its generator images

\[
 \xi=\eta(X)=U X^dU^{-1}=u_0^{-1}q^du_0,
 \qquad
 \omega=\eta(Y)=p^k VY U^{-1}=p^ku_2Yu_0.
 \tag{4}
\]

These are the two displayed section formulas evaluated at (d,u). Their use as words does not assert membership in GTell or automorphy of eta.

The original norm and duality imply

\[
 \Theta(U)=U\Phi^{-1},\qquad
 \Theta(V)=p^{-1}VQ^{-1}p.                         \tag{5}
\]

For the first equality, restrict (3) to the marked pair (p,q). It is precisely the original negative action with parameter phi(p,q)=Phi^{-1}; applying the original norm to u(p,q)=U^{-1} and inverting gives the first formula. For the second, direct substitution in (3) gives

\[
 \Theta(z)=p^{-1}Qz^{-1}Q^{-1}p.
\]

Consequently Ad(p)Theta restricts to the pair (p,z) as the original negative action with parameter phi(p,z)=Q^{-1}. Apply the same norm and duality argument to u(p,z)=V^{-1}. This proves the second equality without choosing a new canonical word or conjugator.

Substituting (3) and (5) in their actual order gives

\[
 \boxed{\Theta(\xi)=\xi^{-1},\qquad
        \Theta(\omega)=p^{-d}\omega.}             \tag{6}
\]

In particular the second calculation is

\[
 \Theta(p^kVYU^{-1})
 =p^{-k-1}VQ^{-1}p\,p^{-1}QY\Phi^{-1}
                       \Phi U^{-1}
 =p^{-k-1}VYU^{-1}=p^{-d}\omega.
\]

Thus the candidate pair has exactly the required equivariance apart from its own boundary image.

Let c_ell denote the section of the standard conjugation pair (-1,1):

\[
 c_{\rm ell}(X)=X^{-1},\qquad
 c_{\rm ell}(Y)=p^{-1}Y=XYX^{-1}.
\]

It is an involution. Since eta(p)=[omega,xi], equations (6) prove the exact equivalence

\[
 \boxed{\Theta\eta=\eta c_{\rm ell}
        \quad\Longleftrightarrow\quad
        [\omega,\xi]=p^d.}                       \tag{7}
\]

Both directions follow on the two free generators. In particular no cancellation through eta, and no prior surjectivity of eta, is used.

## 3. Literal comparison with the original third-cusp equation

On the embedded original pair (p,q), let

\[
 \psi_d(p)=p^d,\qquad
 \psi_d(q)=u_0^{-1}q^du_0=\xi.
 \tag{8}
\]

The defining relation YqY^{-1}=pq=z^{-1} gives a complete collection of the candidate commutator:

\[
\begin{aligned}
 [\omega,\xi]
 &=p^ku_2Y u_0(u_0^{-1}q^du_0)u_0^{-1}Y^{-1}
                       u_2^{-1}p^{-k}\xi^{-1}\\
 &=p^ku_2 z^{-d}u_2^{-1}p^{-k}\xi^{-1}.
\end{aligned}                                                    \tag{9}
\]

All profinite powers in (9) are preserved by conjugation and inversion. Therefore

\[
\begin{aligned}
 [\omega,\xi]=p^d
 &\Longleftrightarrow
 p^ku_2z^{-d}u_2^{-1}p^{-k}=p^d\xi=\psi_d(z^{-1})\\
 &\Longleftrightarrow
 \boxed{\psi_d(z)=\operatorname{Ad}(p^ku_2)(z^d).}
\end{aligned}                                                    \tag{10}
\]

The last line is a specified conjugacy at the ORIGINAL third cusp of the embedded free pair, with its entire conjugator p^ku(z,p) retained. It is not an arbitrary elliptic peripheral identification, an unspecified conjugacy, or an equality only after a finite quotient. Equations (7) and (10) give the promised exact based bridge.

For completeness, if D=[omega,xi]p^{-d}, the closed normal subgroup generated by D in E is Theta-stable. Modulo that subgroup, (6) and [omega,xi]=p^d imply

\[
 \Theta(D)
 =[p^{-d}\omega,\xi^{-1}]p^d
 =[[\omega,\xi]^{-1}\omega,\xi^{-1}]p^d
 =[\omega,\xi]^{-1}p^d=1.
\]

The displayed commutator identity is a literal group identity. Inclusion of normal subgroups becomes equality because Theta is an involution. This defines the obstruction quotient; it supplies no reason for D itself to vanish.

## 4. Exact remaining gate and provenance

The already proved negative elliptic cubic for u is independent of asserting the boundary equation (7). The present calculation locates the missing boundary equation precisely in the actual third-cusp problem. It does not derive that equation, an automorphism of the full free group from eta, the other elliptic relations for (d,u), the original full H_d=1, or the CM sign.

The direct use of full GT here is the existence of the actual section automorphism Theta in (3) and the predecessor's canonical-u pentagon. The displayed norm manipulations themselves retain the original parameter and canonical word; no arbitrary residual word is substituted. The A118 transported expression can be substituted pair by pair into (4), as in the predecessor's equation(13), but Gamma is still only GT0 and is not given an elliptic action.

Primary reference: Enriquez, B. (2014). Elliptic associators. *Selecta Mathematica, 20*(2), 491–584. https://doi.org/10.1007/s00029-013-0137-3. Full proof used: author version https://arxiv.org/pdf/1003.1012, Proposition2.20, printed pp.14–18, especially formula and boundary identity in proof part4. The exact complete prior reading, source conventions, B1,3 presentation, and marked pentagon are recorded in the frozen predecessor ab9ccffb. This note adds the literal calculations (5)–(10); it claims no new primary theorem or additional source reread. Mathematical verification is symbolic, with no finite census or numerical producer.
