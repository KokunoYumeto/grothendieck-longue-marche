# Independent E96 algebra and integral-lattice audit

Result: PASS for the proposed reduction on the actual b=0 slice, using
the transported marking and framed-point representatives specified in
E95's path derivation.

Read in full: the integrated E37 statement and proof, the complete
E95 path_derivation.md, and the executed E95 coefficient program and JSON.
This is an algebra/lattice audit of the E96 comparison. The theorem and
its final source wording remain owned by root.

Full-text supplement: the complete E96 statement and proof at
research_e96/sections/E_zero_free_elliptic_obstruction.tex were subsequently
read. The exact transported marking, both global directions, finite
carry, fixed-support simplification and rational-prime equivariance
all pass. The modulo-three image is exactly the three displayed cusp
rays: the mixed rows, together with9X_p integral, give the stated
equations; all of their global finite-support solutions are attained
by actual rational tangent sections with rational Kummer twists.
Two missing TeX backslashes before quad in E96.9 were reported to root.
No mathematical correction was requested.

## Actual quotient map

Use the E37 wedge basis of M=exterior-square V. Let p be the wedge
e_A0 wedge e_A2, and let w=exterior-square(j)(t1 wedge t2).
The coefficient w_p is exactly1. The quotient Q is the following
integral map, not just coordinate deletion:

    Q(m) = non-pivot coordinates of (m - m_p w).

Its section inserts zero in the pivot coordinate. Consequently QS=I,
SQ=I-w e_p^t, and Qw=0. The first row has pivot coefficient -9.
This is the full domain M/Z3w used in E37, including the determinant
index-nine feature of M0 inside that quotient.

## Exact inverse formula

For arithmetic Frobenius at a K-prime, write k=q-1 and
d=q^-1 exterior-square(A)-1. Its action on a mixed wedge satisfies

    d(h wedge e_d) = (A-I)h wedge e_d,

because A e_d=q e_d. On exterior-square W it is multiplication by k.
The retained numerator therefore satisfies dX=D, with

    alpha(F)=(A-I)(epsilon h*/3)+u,
    u=kappa(beta)(F)+epsilon(cT3 kappa3(F)+cTz k/3)/3.

Substitution of each actual cusp formula

    k_d=(A-I)b_d+r_d kappa3(F)+s_d k/3

gives the proposed X with precisely the minus signs in E37.10.
As d factors through Q and is rationally injective there, the unique
E37 correction is c=-QX.

Multiplication by3k gives exactly the root-proposed numerator

    N=Q[epsilon k h* wedge v
        -3k sum v_d b_d wedge e_d
        +3 kappa(beta)(F) wedge v
        +epsilon kappa3(F)cT3 wedge v
        +epsilon(k/3)cTz wedge v
        -3 kappa3(F)sum v_d r_d wedge e_d
        -k sum v_d s_d wedge e_d].

Every coefficient is in Z3. Indeed h*,cT3,cTz and
3b_d,3r_d,3s_d are integral in the retained literal V basis,
and k is divisible by3 at every prime of K away from3.
Denominators prime to3 are retained exactly in the certificate.
No additional factor9 is necessary.

The exact local condition is

    N in 3^(v3(k)+1) Z3^44.

The actual correction is -N/(3k), so convergence of the corrections
is equivalent to this condition with exponent v3(k)+1+m outside
a finite set for every fixed m. The increasing local valuation is
retained; it is not replaced by a constant modulus.

## Arithmetic marking and scope

The proof uses E95's actual scalar Tate-basis change and its lift
Psi on the full free pro-three group. The arithmetic action is
transported by Psi^-1 rho Psi and every curve/quotient map by F Psi.
This is essential when using the phase-zero framed constants.
The first-degree matrices stay the same because the displayed
integral P_u commutes with T and J; this fact alone would not identify
the higher actions. E95 explicitly supplies their transport.

The input is the inverse image of the zero free coefficient under
the actual compact projection

    H1(Q,V) -> H1(Q,T3E)=Z3 t1 plus C3 t2.

Use epsilon in {0,1,2}, with the E92 toric carry when changing an
integer representative. This fixes the input coordinates and does
not assign Frobenius values to the separate free proper-elliptic
cocycle.

## Executed independent certificate

bc_class2_reduction.py verifies eighty universal mixed-wedge
identities, all eight universal numerator identities,352 exact
coefficient-integrality checks, and all eight actual q=7 quotient
inverse identities. It retains the complete Q and w, the fixed
coefficient columns, and the hashes of both source inputs.
The first execution stopped at an insufficient symbolic
simplification: expand had left a rational identity in q-1
uncancelled. Its exact source/stdout are retained under the
simplification_attempt names. Replacing that equality check by
exact cancellation made the complete run pass. No arithmetic or
theorem formula was changed.
