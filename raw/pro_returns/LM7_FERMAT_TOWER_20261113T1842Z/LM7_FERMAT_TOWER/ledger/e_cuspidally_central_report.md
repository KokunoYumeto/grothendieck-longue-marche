# Cuspidally central cubic section fibers: E.36

The complete proof is in sections/E_cuspidally_central.tex. It evaluates an intrinsic class-two quotient that retains every one of the cubic's ten abelian coordinates and the elliptic commutator. With I the kernel of N -> T3E, the exact based arithmetic isomorphism is N/[N,I] -> C times over T3E V, induced by the open immersion into E minus O and by abelianization. The map on cusp lattices is (t_O,t_i) -> (t_O,t_i-t_O), with explicit integral inverse. The quotient from N/gamma3N has central kernel rank44, precisely the kernel of the exterior-square projection.

The proof applies the directly opened primary Borne-Emsalem-Stix Theorem5.10 to the proper elliptic curve over Q and the singleton boundary O. A singleton satisfies their torsion-subpacket definition because every point difference is zero. A pro3 elliptic section is first made into an actual full proper-curve section by setting its other prime components to zero. The theorem's full lift is then projected back to the pro3 once-punctured class-two quotient. Pairing with an arbitrary prescribed rank-ten abelian section proves existence for every such class, including all ramified classes.

Every fiber is evaluated as the group of restricted Z3 sequences over rational primes: central twisting is Kummer theory, and H0(Q,V)=0 is proved directly from finiteness of rational torsion in the generalized Jacobian. Consequently no extra conjugation quotient is suppressed. The same tangent s=z/x of value one at O is used throughout, so there is no unidentified affine origin shift.

The exact integral lattice program e_cuspidally_central.py verifies determinant1, the inverse cusp matrix, and the exterior-square Smith map of rank45 to rank1 with kernel44. Existence of infinite sections is established by the theorem and proof, not by finite computations.

The result computes the entire section map to this specified intermediate quotient. It does not lift through the additional rank44 kernel automatically: the nonempty abelian fibers obstructed by E31 still have the cuspidally central lifts just proved. This makes the remaining intrinsic obstruction concrete.
