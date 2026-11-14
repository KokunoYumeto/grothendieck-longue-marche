# Independent review of the prime-seventeen and elliptic calculations

The root agent read the complete proof of E.57, including the positional
finite-etale norm map, the certified ideal-class coordinates, the supported
principal-divisor lattice, the full S-unit basis and the restricted global
divisor splitting. The norm-one and root-of-unity coordinates agree with
the displayed relative multiplication determinants. The actual element
of norm zeta3 has the stated nonzero divisor of relative norm zero. The
calculation evaluates this specific first complex transition; higher
radical transitions remain explicit further maps in the original task.
The separate independent program rerun is recorded by agent A.

For E.58, the root agent checked the exact module ideals, their intersection,
the fiber-product map and the free-rank comparison kernels. The eleven-element
ring basis gives the asserted class-three quotient. The surface-coordinate
map, tangent coefficient, discriminant roots, Tate-kernel inner action and
integral path transport were checked through the displayed comparison
maps. The Frobenius formulas on the two handles and the full commutator
module agree with their projections to both constituent quotients.
Agent B independently read the complete proof and reran both programs;
its exact certificate comparison is retained in bc_e58_audit.md.

The root agent independently derived the tame defect in E.60 from the
actual Frobenius action over K_v=Q2(zeta3), whose residue cardinality is
four. The two torsion-free handle equations force zero inertia handles.
The unique Frobenius-handle normalization leaves precisely the displayed
eleven-dimensional integral coboundary matrix. Its two unit columns give
the actual finite coordinate maps and their inverse, not just an abstract
Smith-factor count. All nine systems have factors C3^7 plus C27^2.

The lower central image follows from changing the inertia lift by9U and9V;
the correction coefficient is-108, so the exact image test is divisibility
of the two displayed parentheses by27. The central framed fiber is C9^2.
The full lower stabilizer is exactly C9^2: its handle coordinates vanish
by3s=3t=0, and its nine free module coordinates vanish by-3l_ij=0.
Its action adds9rU+9sV to a Frobenius lift and is simply transitive on
the framed fiber. Consequently the full geometric-conjugacy fiber is
one point whenever it is nonempty. The explicit excluded lower class
and the zero class have identical abelian data under the proved map.

The root also wrote and executed e_frattini_fixed_module.py as an independent
finite audit for the forthcoming uniform inert-prime calculation. The
actual Fox module has dimension ten over F3, and its fixed subspace has
dimension four with the displayed basis. All81 vectors were enumerated:
one has cyclic rank zero, two rank one,24 rank three and54 rank five.
Each case includes checked independent generators and annihilating
relations. Its mathematical transfer to Frobenius conjugates is supplied
in the corresponding prime calculation rather than presumed from the
finite rank table.

## E.59 full arithmetic and density review

The root agent read the complete final proof of E.59. The actual local
involution can be conjugated to the fixed complex conjugation while
retaining the specified Kummer coordinate. Its signs on the first
Zassenhaus grades leave exactly the two stated Frobenius coefficients.
The explicit cross-ratio norm identities give a Kummer character killed
by the required square of the augmentation ideal. The exact dimension
comparison identifies D4/Phi2 with that ideal times the Fox module.
The noncube proof for gamma and the explicit Heisenberg lifts fix the
triple-bracket sign; the residue calculation at two gives the other
dual-basis value. These establish the uniform arithmetic formula.

The finite Magnus/Fox group has exactly3^12 elements and is the actual
quotient P/Phi2. Its semidirect product with complex conjugation is an
actual Galois quotient over Q. The cyclotomic-minus-one subset has
3^11 elements. Each of its three square maps is, after the displayed
invertible deck change, the surjection (1+c)Y^b onto the four-dimensional
fixed space, with six-dimensional kernel. Each fixed vector therefore
has3^7 preimages in that subset. The computed counts1,2,24,54 give the
stated Dirichlet densities by the cited conjugacy-stable version of
Chebotarev. Agent B checked this derivation independently; agent A then
rebuilt the PARI field certificate, reran both Python programs, checked
the complete proof, and reopened the stated original density theorem.
