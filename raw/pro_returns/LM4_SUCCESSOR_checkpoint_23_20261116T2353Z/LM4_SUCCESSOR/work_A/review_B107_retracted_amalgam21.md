# Independent review of B107.3: the retracted amalgam

Reviewed 2026-11-16, checkpoint21 cycle. Verdict: **PASS** at the stated discrete and full profinite scopes. The reviewed formal source is `sections/b_free_swap_quotient.tex`, including B107.2–4. This review does not assert the global fixed-source equality.

Let C be a discrete retract of R, with the inclusion understood and r:R→C extended to an idempotent endomorphism of R. Set E=(C×C2)*_C R and let τ generate the displayed C2.

1. Ordinary reduced normal form gives C_E(τ)=C×C2. In particular τ is outside the amalgamated subgroup, so a reduced word leaving the first vertex cannot conjugate τ into that vertex. Equivalently, E=(C2*ker r)⋊C, with C fixing τ, gives the same normal-form conclusion.

2. For each finite-index normal N0 of R, N=N0∩r^{-1}(N0) is finite-index normal, lies in N0, and satisfies r(N)⊂N. Intersections preserve this property. Hence the r-stable family is cofinal and directed; no finite generation or residual finiteness of R is used.

3. Writing Q_N=R/N=K_N⋊D_N, with D_N the actual image of C, the amalgam quotient is exactly E_N=(C2*K_N)⋊D_N. The finite group D_N acts trivially on τ. The normal subgroup C2*K_N has finite index and therefore carries its full induced profinite topology. Its completion is the full free profinite product C2 amalg K_N. The accepted full-category centralizer theorem of Herfort–Ribes, Theorem B′ (the primary proof was reopened by root at this dependency), gives centralizer C2 there. Consequently C_{hat E_N}(τ)=C2×D_N. The trivial K_N case causes no exception.

4. Given any finite quotient of E, restrict to R and refine its kernel by an r-stable N. The first vertex map also factors through D_N×C2, because its restriction to C kills C∩N. The universal property of the ordinary amalgam therefore factors that finite quotient through E_N. Thus the maps hat E→hat E_N jointly separate points. This is the exact separation required; it is not a claim that an unspecified infinite-index kernel carries its full topology.

5. If g∈hat E centralizes τ, its E_N images are uniquely τ^ε d_N. The parity coordinate is the fixed global quotient E→C2, and the d_N are compatible under refinement. For every finite-index normal L of C, N=r^{-1}(L) belongs to the r-stable family and gives D_N=C/L. Therefore lim D_N=hat C with its full topology. There is c∈hat C with these coordinates. The element τ^ε c has the same image as g in every hat E_N, so joint separation gives equality. The inclusion hat C×C2→hat E is injective because the discrete inclusion has the explicit retraction induced by r and the identity on the first vertex.

This proves C_{hat E}(τ)=hat C×C2 without residual finiteness of R. B107.4 then intersects with the actual index-two orientation kernel. Completion of that finite-index subgroup is its open closure, so this intersection is legitimate. The selected source over the inner region has trivial cover monodromy and is the explicitly chosen component through P; the one-directional cover transfer is therefore correct.

The geometric identification of the inner-region amalgam is independently reviewed by DE. The algebra above retains the entire actual outside vertex R, including its critical fibers, and does not replace it by a generic fiber or assert injection across the global q-boundary.
