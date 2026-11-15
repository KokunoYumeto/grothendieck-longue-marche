# Independent check: a Cartesian square of scalar gauges

This is a concrete check of the abstract conditions posed in frozen cote 11, scan 031, within the gauge/bivariant category defined on scans 027 and 034. It also uses the non-normalized-isomorphism example explicitly written on scan 042. No source image was opened and no frozen fragment was changed.

## Four objects and their arrows

For λ∈Q×, write Q_λ for the degree-zero algebra Q with d=0 and trace κ_λ(a)=λa. The pairing (a,b)↦λab is perfect. Between Q_λ and Q_μ, use the bivariant morphism r_{λ,μ} with

\[
r_{\lambda,\mu}^{*}=\operatorname{id}_{\mathbf Q},
\qquad
r_{\lambda,\mu*}=(\lambda/\mu)\operatorname{id}_{\mathbf Q}.
\]

Its pullback is a unital Q-algebra map, both projection formulas are scalar identities, and κ_μr_*=κ_λ. Composition is r_{μ,ν}r_{λ,μ}=r_{λ,ν}; its inverse is r_{μ,λ}. Thus these are actual isomorphisms in the category on scan 034, and their pushforwards are the adjoints specified on scan 027.

Use X′=Q₂ and X=Y′=Y=Q₁, with square

\[
\begin{array}{ccc}
X'&\xrightarrow{q=r_{2,1}}&X\\
{\scriptstyle f'=r_{2,1}}\downarrow&&\downarrow{\scriptstyle f=r_{1,1}}\\
Y'&\xrightarrow{p=r_{1,1}}&Y.
\end{array}
\]

Every pullback is the identity; q_* and f′_* are twice the identity, and f_* and p_* are the identity. The composites fq and pf′ both have pullback id and pushforward 2id, so the square commutes as bivariant morphisms, including their trace data. All four formal dimensions are zero and satisfy d(X′)+d(Y)=d(X)+d(Y′).

## Universal property in the whole bivariant category

For an arbitrary object T and bivariant maps u:T→X and v:T→Y′ with fu=pv, take h=q^{-1}u:T→X′. Then qh=u and

\[
f'h=(p^{-1}fq)q^{-1}u=p^{-1}fu=p^{-1}pv=v.
\]

The equation qh=u determines h uniquely because q is an isomorphism. This verifies the pullback universal property for arbitrary T in the entire category, not merely in the four-object subcategory.

## Exchange calculation

Both maps in the first exchange formula of scan 031 have source A(X)=Q and target A(Y′)=Q. Their exact values are

\[
p^*f_*=\operatorname{id}_{\mathbf Q},
\qquad
f'_*q^*=2\operatorname{id}_{\mathbf Q}.
\]

Their values on 1 are 1 and 2, so the proposed exchange identity fails in this particular Cartesian square with the stated dimensions. The other displayed exchange identity similarly gives f^*p_*=id and q_*f′^*=2id.

The factor 2 is precisely the scalar σ in scan 042's example `f^*=id`, `f_*(y)=yσ`, `k_B(y)=k_A(yσ^{-1})`: here κ_A=2id, κ_B=id and σ=2. Thus the morphism-level obstruction is already expressed by the source's warning about isomorphisms with f_*(1)≠1. The square's upper/left maps belong to that explicitly allowed class, whereas the identity-valued right/lower maps have f_*(1)=1.

## Scope and verdict

The example verifies an obstruction to using Cartesian universal properties and dimension equalities alone inside this written abstract category. It makes no assertion about a geometric cohomology theory whose pullbacks, traces and pushforwards come with additional specified normalizations; none of those additional data are part of this four-object construction. In particular, it does not assert failure of a proper-base-change theorem.

**Verdict:** orientation, trace compatibility, both projection formulas, Poincaré condition, bivariant commutativity, inverses, the whole-category universal property and both failed exchange identities check exactly. **Confidence: high**, because the maps are the explicit scalars 1, 2 and 1/2, and the universal lift is written above for an arbitrary test object. The example is unconditional and uses the source's explicit non-normalized-isomorphism mechanism; no novelty claim is made.
