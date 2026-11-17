# Independent full nonlinear comb/transport review

16 November 2026, checkpoint20. **PASS.** I read the complete current
`work_CE/research_nonlinear_comb_and_cones_20h.txt` and both its exact
rewrite producer and its universal transport checker.

The comb tree consists of the B tree at A=1 and every A tree above
a B vertex. Contracting the A trees leaves a tree, so it is indeed
a spanning tree. The non-tree B edges give the actual free basis
`c(a,b,x)=b[a,x]b^-1`. Both signed prefix formulas preserve the exact
nonlinear invariant `prefix=n*b*a*t`; the negative step uses the
following B vertex. The complete independent129-word replay and all
128 short expansions are in `nonlinear_comb_independent_review20.json`.

The uniform coefficient formula was independently derived from the
actual section before reading CE's implementation. For g=(u,v,t),
`q_g=v*u*t` and h=(a,b,s), direct multiplication gives

    omega(g,h)=v[u,tau_beta(t)(b)]v^-1,
    q_g q_h=omega(g,h)q_gh.

The nonabelian cocycle identity follows by associating the three
actual section words in both orders. The resulting maps are a
crossed action, with inner omega correction. Their abelianized
action is strict; the nonlinear correction is not discarded.

The displayed uniform comb formula follows from the literal identities
`[u*a,x][u,x]^-1=u[a,x]u^-1` and
`P_g(b)*(v*b'*u)=v*u*b'`. The correction P is itself the finite comb
path along the whole B word. The retained shifts really permute the
positive Schreier generators; this property is not attributed to
general old/source automorphisms. The formula therefore applies to
the actual retained coefficient action uniformly, not only to the
printed finite node inputs.

The involution formula is also literal:
`[b,a][b*x,a]^-1=b[a,x]b^-1`, with the factor roles exchanged.
The section defect is `eta(g)=[v_A,u_B]`, which gives both the
F/rho intertwining equation and `F(eta(g))*eta(F(g))=1`. All seven
printed complete free-word identities are separately replayed in
`verify_nonlinear_transport_independent20.py/.out/.err` and its JSON.
This independent checker imports no producer. The general
three-variable cocycle is proved algebraically; it is not labeled
as an additional executed test.

The selected-cone decomposition is valid with the stated single
maximal-tree transversal. Its C2 factors are indexed by the actual
fixed quotient group diag(R); the other cone class remains distinct
in the retained orbifold quotient. Arbitrary independent lifts
preserve conjugacy classes but are correctly not claimed to form a
simultaneous free-product generating family. The orientation-kernel
Schreier basis and the left-versus-right defect distinction follow.

After the whole actual nodal normal closure is imposed, conjugacy of
the two cone images by M is precisely the fixed-lifting condition.
The source gives a map on the sets rI (left cosets); injectivity of
that map is not inferred. The local filling annuli kill their base
lassos, so they are correctly excluded from an injective-edge
Bass–Serre argument.

No simultaneous primitive basis, quotient freeness, full nonabelian
normal-closure decision, fixed lift, or kappa value follows from
these exact uniform formulas.
