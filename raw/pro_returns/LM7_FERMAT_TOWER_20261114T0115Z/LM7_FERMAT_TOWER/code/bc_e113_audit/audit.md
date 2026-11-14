# E113 focused independent proof audit

**PASS.** Reviewer: bc_fermat. Scope: complete draft proof read, with the requested focused check of E113.8–9 and E113.16–19, plus the finite/real/inverse-limit Weil-cup argument. This report does not claim a fresh author-certificate execution or independent retrieval of every new source cited by E113.

Multiplying `(m,w)(a,z)g(m,w)^(-1)` in the actual BCH group gives the abelian coordinate `a+m-gm` and central increment `(1-g)w-D_g m+(m+gm) wedge a/2-m wedge gm/2`. Thus the gauge and obstruction signs in E113.16 are correct. The action cross term D is retained throughout this multiplication.

Expanding the two abelian cocycle identities gives `d(b wedge e)=-b wedge g e+e wedge g b`. Together with the actual compact primitive `d nu=e wedge g e/2`, this gives `Omega_a=Omega_rem+d(nu+b wedge e/2)`. Hence the forward central change is `tilde z=z+P` and its inverse is `z=tilde z-P`, exactly as written.

For the filling map `(x,z) -> (p x,p_B z+J x)`, equality with the actual arithmetic actions gives `D_C p=p_B D+J rho_A-rho_Z J`. Applying it to the abelian cocycle gives `Omega_C=p_B Omega-d(Ja)`. The last formula for the action cocycle follows by composing with `rho_A^(-1) j`; the equivariance of the established coefficient section j makes the last term precisely `g(Jj)`. This is an actual coefficient and cochain comparison with the surviving compact action, including its inner-coordinate change.

The determinant and mixed compact columns in E113.5 have the stated factor two. In a common rank-two cocycle, the cross-factor exterior coordinate is `h_g tensor h_t-h_t tensor h_g`, so its symmetric-square coordinate vanishes already as a cochain. This is compatible with the full tensor-cup class argument when two is invertible.

The local point argument at two is exact: odd x makes x(x^2+1) have odd valuation, so no rational point reduces to the singular point. The nonsingular reduction group has order at most two and the formal kernel has no odd torsion. Local finite self-duality and the prime-to-residue Euler identity therefore give H1(Q2,E[ell^n])=0 for odd ell.

At good q distinct from ell, the actual inertia vector satisfies `(F_q-q)v=0`; its determinant is `q #E(F_q)`, nonzero, so every integral cocycle is unramified. At the real place the continuous H2 with Z2(1) is zero, since the invariants of the sign lattice are zero. More explicitly the square maps on the finite H2 classes represented by ±1 kill both representatives. Hence a compatible cup has zero finite component there as well. After this actual real comparison, global Brauer reciprocity leaves only the ell place and forces that invariant to vanish.

Finally the Kummer H1 transition for the global coefficient tower is the onto quotient map represented by the same rational number. The displayed correction of successive finite primitives aligns them exactly; its uniform inverse limit is continuous. This supplies the continuous primitive and removes the derived-limit ambiguity. Rationalizing is justified by bounded denominators on compact cochain domains. No mathematical correction was found.

## Added E113.20–22 refinement

The subsequently added nine Tate-line projections also pass this focused proof read. The actual CM automorphism gives the perfect symmetric pairing `B_I(x,y)=<Ix,y>` with target `R(1) chi_-1`; its equivariance identifies Hom(V,L) with the same actual V. The unique E103 cohomology coordinates therefore decompose each retained action cocycle as `s_i B(h,-)+delta m_i`. Evaluating the Hom coboundary on `g h_t` gives exactly `d(m_i(h))`, with the written positive sign. For the symmetric pairing, `d[-B_I(h,h)/2]=B_I(h_g,g h_t)` follows by direct expansion, while the alternating pairing uses the already constructed Weil primitive.

The toric action is sent into Lambda2 W after restriction to the specified four-coset field, so each of these compact coefficient rows kills its restricted defect. The stated abelian-kernel pushout and actual four-coset formula give its global primitive with the sign specified. The mixed cup is killed by the coefficient projection itself. Adding the three primitives and the previous exact central shift yields E113.22. The coefficient complement has rank55+66+6=127, and the argument retains the actual remaining mixed and CM operators. No new mathematical correction was found.
