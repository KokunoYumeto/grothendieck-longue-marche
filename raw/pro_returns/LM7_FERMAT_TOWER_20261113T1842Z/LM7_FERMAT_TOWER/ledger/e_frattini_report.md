# E.59 — Actual inert Frobenius, its Frattini orbit, and exact rank densities

Status: Proved. Independent full-proof and fresh-execution audit PASS, retained in ledger/a_independent_audits.md. The auditor rebuilt the certified field and reran both finite-field and fixed-module certificates with identical JSON.

## Exact arithmetic outcome

The arithmetic group is the actual free pro-three group P=G_(Q(zeta3),{3})^(3), with the c-equivariant basis from E.55. Its Frattini field is Q(zeta9,cuberoot3). Every inert rational prime ell congruent to8 modulo9 has its arithmetic Frobenius in D3(P). The entire image in D3/D4 is

    x^(3 alpha_ell) [y,[x,y]]^beta_ell,

where alpha_ell=(ell^2-1)/9 modulo3, and beta_ell is the cubic residue of the explicit cross ratio

    h=(r-u)(omega^2 r-u1)/((omega^2 r-u)(r-u1)),
    u=-z^2(1-z)^2, u1=-z^8(1-z^4)^2,
    z=zeta9, omega=z^3, r^3=3.

The proof supplies the actual Kummer morphism and its sign. The exact equality ((3-u^3)/(3-u1^3))*gamma=9q^3 gives (Y^-1 h)/h=gamma times an explicit cube. The eigenspace argument proves gamma is a noncube before the associated Heisenberg extension is used. That extension pairs gamma with [x,y] as1. At the prime over two, h reduces to omega^2 in F64 and has trivial cubic residue, so h is precisely the second dual coordinate. The other dual coordinate is zeta9. This evaluates the word without presuming a presentation of a larger arithmetic group.

At17 the formula gives x^6[y,[x,y]]^2. The Frobenius has exact first Frattini depth and exact Zassenhaus degree three. Its nine conjugates have rank five in the ten-dimensional Frattini quotient. Each is nonzero, but their exact span prevents their being included simultaneously in a free generating set.

## Full finite module and density calculation

Continuous Fox derivatives give the actual module

    Phi(P)/Phi(Phi(P)) = ker(R^2 -> R), R=F3[s,t]/(s^3,t^3),
    boundary(A,B)=sA+tB.

Complex conjugation acts by substitution Y->Y^-1 and the derivative factor -Y^-1 on the second coordinate. Its fixed space has basis a=(s^2,0), b=(-t^2,st-st^2), sb,s^2b. The cyclic submodules of all81 fixed vectors have ranks0,1,3,5 with counts1,2,24,54. Every case, including zero coordinates, is proved by explicit independent generators and annihilating polynomials.

The finite arithmetic quotient P/Phi(Phi(P)) is the full Fox group of pairs(q,D) with boundaryD=q-1, of order3^12. The exact chi9=-1 subset in its c-extension consists of q=Y^b. Squaring and then multiplying byY^b gives the surjection (1+c)Y^b from the ten-dimensional cycle space to its four-dimensional fixed subspace. Its kernel has dimension six. Consequently every fixed vector has3^7 preimages across the three values ofb. Chebotarev applied to these actual conjugacy-stable subsets gives relative Dirichlet densities1/81,2/81,8/27,2/3 among primes ell=8 mod9, and absolute densities1/486,1/243,4/81,1/9.

This density proof uses the entire finite Galois quotient. It is independent of the finite sample of prime residues.

## Certificates and scope

The official PARI source reconstructs K1 and unconditionally certifies class number one, discriminant-3^39, the complete fundamental-unit basis, roots mu18 and the unique three-prime. The exact primitive element is theta=cuberoot3-zeta9; its polynomial, all units, the integral basis, and each prime ideal are retained in code/e_frattini17_certificate.json.

The independent Python certificate verifies120 cubic residues with actual prime-ideal Hermite-lattice matching. It evaluates the uniform formula at all50 primes ell=8 mod9 through2000, checks all450 prolongations, and evaluates270 additional full Kummer residues at the three primes with both first coefficients zero. Their actual ranks are269:3,809:1,1187:3. Thus the rank-one case at809 is evaluated from the full Frattini quotient.

The root-owned code/e_frattini_fixed_module.py/.out/.json independently verifies all81 fixed vectors, eighteen involution identities,162 semilinear identities, a ten-generator Schreier basis, the three rank-four square maps, and the exact finite arithmetic counts. It is part of this theorem's certificate.

Run the final arithmetic source from its code directory with gp -q e_frattini17.gp, then run python e_frattini17.py. The GP source truncates its output certificate before rewriting it, so the computation is repeatable. The Python verification uses only the standard library.

All exploratory programs and outputs, including ordinary implementation failures and the incomplete higher radical-field call, are retained under code/research_prime17/. The final self-contained scripts do not depend on the temporary staged binary files. The attempted short complete Kummer basis had dimension eight; the full certified unit basis is therefore retained with its exact coordinate map.

The theorem evaluates the actual maps to P/D4 and Phi/Phi2. The correction words from E.39 remain in the full arithmetic inertia presentation. No replacement of a nonprimitive local Frobenius by the image of a projective section, and no full intrinsic section lift, is inferred.
