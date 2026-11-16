# The actual eta source fiber and its removed zero component

Research record after checkpoint15. Here **eta** denotes the new rational
function `(vw-1)/(w-1)^2`. It is distinct from the older product-pencil
coordinate `q=vw`. This note is an exact explanation of the boundary gate,
not a relative Lefschetz theorem or a new kernel-surjectivity claim.

On the actual surface Y,

\[
\eta+1=\frac{w(v+w-2)}{(w-1)^2},\qquad
\frac{\partial\eta}{\partial v}=\frac{w}{(w-1)^2}.
\]

Because w and w−1 are units on Y, the actual source v+w=2 is exactly the
eta=−1 fiber, and eta:Y→G_m is smooth at every point of Y. Nevertheless the
fiber is atypical at the removed boundary: in a compactification the divisor
eta+1 also contains the entire w=0 component. That component meets the
source at (v,w)=(2,0). It is not an interior critical point of eta.

For one constant component v=u, u in mu5 except1, its two generic eta-fiber
punctures solve

\[
\eta w^2+(-2\eta-u)w+(\eta+1)=0.
\]

At eta=−1 this is

\[
w(2-u-w)=0.
\]

One puncture remains at the actual source point w=2−u; the other escapes to
w=0. The discriminant is u²+4eta(u−1), and its value at−1 is (u−2)²≠0.
Thus this loss is not a collision of those two constant punctures in Y: it
is disappearance into the removed old zero component. All four added
constant components have this same feature.

The B85 chart near the resolved (1,1) source point is correct and gives the
literal product-one tangential inertia. It does not make the actual source
a generic fiber globally. Replacing that source by a generic eta-fiber
would insert precisely these additional branch punctures near the removed
w=0 component. Their transport and conjugating operators must be retained.
In particular, the old zero source direction is not absorbed by the current
controlled b-normality argument merely by resolving the product-one
source tangency.

DE confirmed that this exact degeneration had not been used as a theorem
in the earlier w-pencil proof. It is consistent with the already audited
failure of the generic-fiber shortcut and with the outstanding old-zero
operator. The exact identities and discrimination are verified by
`code/check_eta_source_degeneration.py` and its genuinely executed stdout.
No new formal theorem ID is allocated.

Implementation note: an initial structural-expression equality assertion rejected two algebraically identical factorizations. Its genuine trace is retained in `check_eta_source_degeneration_structural_assertion.out`; the final checker correctly tests the expanded polynomial difference, which is zero. No mathematical condition was weakened.
