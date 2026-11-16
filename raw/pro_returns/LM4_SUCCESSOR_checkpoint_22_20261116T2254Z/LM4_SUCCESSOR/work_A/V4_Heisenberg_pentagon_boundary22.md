# A bounded V4--Heisenberg pentagon attempt: exact failure to couple the two coefficients

Research, checkpoint22 cycle. **This attempt does not advance the full Fox-unit or third-cusp decision.** It identifies an exact limitation of a new nonmetabelian target family, then stops. No formal statement or register row is proposed.

## 1. The question tested

For the actual canonical word u, A45 defines a dihedral exponent k by u(x,y)=t^k when x=a, y=at in the full dihedral quotient. A necessary condition for a full peripheral conjugator is

\[
(2k+1)^2=1+24c_2(u).
\]

The earlier Heisenberg target with one C2 acting negatively on both degree-one directions collapsed to a metabelian image. This cycle tested the different target Heis ⋊ V4, with the two degree-one directions and the center carrying the three distinct nontrivial V4 characters. Its derived group can be the nonabelian Heisenberg group, so it does not have that earlier formal defect.

The result is nevertheless negative: the actual P4 representations in the tested nontrivial-character family never make the pentagon see the ordinary c2 coordinate. The explicit integrable word [x,y]^2 satisfies all their resulting equations while violating the displayed coefficient equality. It is not asserted to be a full pentagon word or a canonical involution word.

## 2. Exact group law and actual P4 relations

For odd coefficient characteristic use the class-two BCH law

\[
(a,b,z;\epsilon,\eta)(a',b',z';\epsilon',\eta')
=\left(a+\epsilon a',b+\eta b',z+\epsilon\eta z'
+\tfrac12(a\eta b'-b\epsilon a');\epsilon\epsilon',\eta\eta'\right).
\]

The calculation is over Q, with all relevant denominators powers of two. The constructed representations therefore also make sense in the corresponding compact class-two groups over Z_p for every odd p. The actual pure-braid relations are the same audited Artin action presentation used in `work_CE/code/check_heisenberg_parity.py`; no braid relation was replaced by an infinitesimal approximation. The six generator order is 12,13,23,14,24,34.

For each nontrivial rank-one sign character, its degree-one cocycle matrix is evaluated exactly. There are fifteen characters with a one-dimensional H1 after the one-dimensional coboundary direction is removed. For each unordered pair of distinct such characters, choose an actual non-coboundary representative in each coordinate and solve the exact linear central-coordinate equation. This is a 105-case character/cup calculation, not an enumeration of finite groups or their elements.

Fifteen pairs admit a lift; ninety are cup-obstructed. In every obstructed case, the computed left-nullspace obstructions have integral gcd one and the left-nullspace basis has only power-of-two denominators. Thus these obstructions do not disappear at an odd coefficient prime. The liftable pairs form five three-character packets. Four are the coordinate-triple packets and the fifth has characters 011110,101101,110011. The complete vectors and lift coordinates are in the JSON certificate.

Central lifts are not restricted to one chosen solution: the calculation evaluates a particular solution and every independent central cocycle variation. The pentagon expressions are linear in these variations. Scalar changes in the two nonzero H1 coordinates are accounted for by the Heisenberg automorphisms scaling the two degree-one directions and their central product. Coboundary changes are simultaneous target conjugations. This describes the tested family with two nontrivial H1 coordinates. Degenerate or other coefficient families are not silently substituted into it.

## 3. A universal thirteen-coordinate word evaluation

Let K0 be the index-four kernel of F(x,y)→V4. An actual free Schreier basis is

\[
x^2,\quad yxy^{-1}x^{-1},\quad y^2,\quad xyxy^{-1},\quad xy^2x^{-1}.
\]

The relative class-two Lie algebra has free degree-one basis A,B,C,D,E, with V4 weights 0,0,10,01,11 and its ten exterior-square central coordinates. Realize the source generators as

\[
x=\exp(A+D)s,\qquad y=\exp(B+C+E)t,
\]

where s,t are the two head generators. The first-coordinate matrix of the five actual Schreier words has determinant 128. It is invertible at every odd prime. The kernel is generated in degree one by those five words and in degree two by their ten brackets, so this is the actual relative class-two quotient, with no extra formal word coordinates introduced.

For u in the full commutator subgroup, its two trivial first coordinates vanish. Write the remaining coordinates as

\[
c=\ell_C,\quad d=\ell_D,\quad e=\ell_E,
\qquad z_{ij}\quad(0\le i<j\le4).
\]

The program obtains the induced Lie map for every argument pair from the five actual Schreier-word evaluations. It includes their central offsets before changing basis. Hence it does not treat a degree-one basis change as a complete class-two coordinate change.

Two direct calibrations give

\[
k=-e,\qquad c_2(u)=z_{01}.
\]

The proposed coefficient equality would therefore be

\[
e^2-e-6z_{01}=0.
\]

For an independent integrability check, five genuine commutator words were evaluated directly at all five argument pairs in every chosen representation/central variation. All 1125 direct group-word evaluations agree with the universal-coordinate substitution. In particular the subsequent negative witness is a literal word, not an arbitrary thirteen-coordinate assignment.

## 4. All equations obtained in this family

The retained pentagon convention is

\[
u(q_{12},q_{23}q_{24})u(q_{13}q_{23},q_{34})
=u(q_{23},q_{34})u(q_{12}q_{13},q_{24}q_{34})u(q_{12},q_{23}).
\]

Multiplication uses the full BCH cross term, in this exact order. There are seven distinct nonzero polynomial outputs. Over any ring in which two is invertible, their ideal is exactly

\[
\left(c+d,\; z_{34}-z_{24}-\tfrac12c\right).
\]

Indeed one output is -(c+d); after imposing it, every nonzero central output becomes the second displayed generator, and the remaining quadratic output is a multiple of c+d. Neither e nor z01 is constrained. In particular this is not a mere failure of a linearized test to find a nonlinear consequence: the complete displayed polynomial system leaves those two coordinates free.

Take the literal word u=[x,y]^2. Its relevant actual coordinates are

\[
(c,d,e)=(-4,4,-4),\quad z_{01}=2,\quad z_{24}=0,\quad z_{34}=-2.
\]

Every obtained pentagon polynomial is zero, while

\[
e^2-e-6z_{01}=8,
\qquad (2k+1)^2-1-24c_2(u)=32.
\]

Thus even integrability by an actual word does not repair the missing coefficient in this representation family. The word also has the elementary two-cycle u(y,x)=u(x,y)^{-1}; no canonical full negative involution with this u is claimed.

## 5. Artifacts and stopping decision

- Producer: `work_A/code/check_V4_Heisenberg_bridge22.py`.
- Final genuine stdout/stderr: `work_A/code/check_V4_Heisenberg_bridge22_final.out`, `.err`.
- Exact matrices, characters, central lifts, polynomials, and literal-word coordinates: `work_A/V4_Heisenberg_bridge22.json`.
- Initial and intermediate successful outputs are retained separately as the unsuffixed and `_verified` stdout/stderr files.

No finite-group census, quotient-depth iteration, new primary theorem, or formal claim was used. The bounded target has failed its stated coupling purpose and will not be enlarged merely to obtain another passing layer. The exact full Fox unit B and the canonical third-cusp equation remain Open.
