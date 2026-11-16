# Independent DE audit of A.70

Status: **PASS**, complete written proof, fresh primary dual-isogeny verification, and independent complete certificate replay. The final arithmetic-comparison wording correction has been read: no rationality over a finite extension is asserted for an arbitrary profinite geometric path.

## Files and exact execution

- Entire `notes/fgh_A70_draft.tex`, final SHA256 `f2d08a2d643dd99378f354ed798361fefd91f06e5c4413e9f69d8314d4b88f3d`.
- Entire `notes/fgh_A70_certificate.py`, executed independently with only its final output-writing lines removed. The complete result JSON is identical. Exact hashes and results are in `notes/de_A70_certificate_rerun.json`.

## Primary source

Freshly reopened Silverman, *The Arithmetic of Elliptic Curves*, second edition, III.6.1–6.2, printed pp.81–83: https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf . Refs `turn1160view0`, `turn1161view1`, `turn1162view0`. The actual identities dual(phi) composed with phi=[degree] and the reverse composition are exactly those used to identify the dual-kernel point. The explicit isogeny formulas themselves are verified by polynomial identities in the certificate.

## Full mathematical checks

1. The rotation quotient is the actual elliptic curve u²=t³+a t²+b t. Its degree is m, the displayed rotation fixes both coordinates, and the four source cusps have ramification m/2. The reflection has square one, conjugates the rotation to its inverse, and induces translation by the actual nonzero kernel point on this quotient. Hence the composed degree2m map is a genuine dihedral Galois cover of the fixed E.
2. The two nonkernel two-torsion points map to (t',u')=(0,0). The three target-coordinate changes send this dual kernel to the three distinct nonzero E[2] points. This distinguishes covers over the identity of the fixed base, even though two source curves become isomorphic after a field extension and a nonidentity base automorphism.
3. For every two-power m≥4, the rotation subgroup is characteristic. The stated complete automorphism formula has exactly the three orbits of generating ordered pairs: rotation/reflection, reflection/rotation and two reflections with odd exponent difference. Their quotient binary vectors distinguish them. Thus the three actual models exhaust all geometric normal covering kernels; finite samples are not used to extrapolate the orbit classification.
4. V4 is correctly separated, since its rotation subgroup is not characteristic. Its six ordered bases form one automorphism orbit, and its cover/intermediates are actual elliptic isogenies.
5. Every stable-family intermediate has at least two cusps from the actual inertia=Frattini subgroup. Norm maps give the proper Jacobian isogeny quotient, preserve potential good/rank-zero reduction, and push geometric points with coefficient one. The source 4m-torsion cusp divisors therefore give the required target torsion divisors. The compact genus is at least one because of the finite map to E. A.41/A.42 and A.59 apply at their established scopes.
6. The nonstable cases use the independently audited A.69 intrinsic marked-curve statements; they do not depend on source-curve isomorphisms preserving the identity of the base.
7. After finite extension, only covering isomorphisms, finite subgroup data and marked points need a field of definition. An arbitrary geometric path supplies the usual arithmetic fundamental-group comparison up to inner conjugacy; the fixed-inertia/packet assertions are invariant under that conjugacy. Intersecting the permitted open subgroup and arithmetic normalizer image with the finite-index field subgroup gives descent. This corrects the earlier unnecessary assertion that chosen profinite paths themselves have finite field of definition.

## Scope

This proves all two-power dihedral geometric closures and their actual intermediates, at every coefficient prime. It does not classify arbitrary nilpotent closures or products of two nonabelian Sylow factors. The finite exact certificate supports the actual algebra and orbit formulas through m128; the unbounded proof is in the text.
