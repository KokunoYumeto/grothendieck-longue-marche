# Independent review of the large-conductor theta certificate

**Reviewer:** degeneration. **Outcome:** PASS in the stated finite-field/form scope.
This is an independent mathematical and executable review of the proposed
positive certificate for the previously remaining Frobenius-conjugate
ordinary genus-two classes 203 and 302. It does not prove universal A1.

## 1. Files and independently repeated checks

Reviewed in full:

- `code/A_F4_large_theta_search.py` and its saved JSON;
- `code/A_F4_large_theta.c`, the Python ctypes wrapper, and the general
  coefficient-list Cantor implementation;
- `code/A_F4_large_theta_canonical.py` and its saved JSON;
- the fixed file `code/A_F4_large_theta_witness.json`, SHA256
  `edcf6ed3d425eb72837ae72f521f7221ee91c8a53c1b005885a4c1280d530ae6`;
- the exact statements and proofs of A.C2.5 and A.C2.20.

I independently reran the canonical field/divisor calculation from a
separate command, without writing or changing finite_field's output.
It verified all **1296** saved point-multiple relations, the exact
generator order, and an independent order-seven point in **60773**
canonical divisor operations. The run passed.

My additional executable is
`code/A_F4_large_theta_degeneration.py`, with its JSON output.
It uses neither the tailored search normalization nor Hermite normal
form. It proves the quotient order and checks every saved coset by
local logarithms and the elementary generalized CRT. It also independently
computes the Jacobian order by Newton sums, rather than the search's
matrix determinant. It passed.

The divisor arithmetic in that rerun is the separate canonical
coefficient-list implementation, not a third newly written group law.
The new independence supplied here is the mathematical origin/group
analysis and the different complete quotient classification.

## 2. The curve and its correct theta origin

Write \(a^2+a+1=0\), and consider
\[
 C:\quad v^2+v=z+\frac{a^2(z+1)}{z^2+z+a}.
\]
Set
\[
 h=z^2+z+a,\qquad g=z^3+z^2+z+a^2,\qquad Y=hv.
\]
Then \(h(z+\frac{a^2(z+1)}h)=g\), because \(a+a^2=1\).
Thus the polynomial model is exactly
\[
                         Y^2+hY=hg.
\]
Its two finite poles and its pole at infinity are all simple. The
numerators do not cancel either finite pole: \(h\) is separable and
has no root at one. Consequently the smooth compactification is an
ordinary genus-two curve, with the three geometric ramification
points denoted \(W_1,W_2,W_\infty\).

The canonical exact differential has
\[
                    \operatorname{div}(dz)
                   =2W_1+2W_2-2W_\infty.
\]
Indeed the pullback of the base divisor of \(dz\) is \(-4W_\infty\),
and the three simple Artin--Schreier poles each have different
exponent two. The line bundle of locally exact differentials with
the Frobenius module structure is therefore
\[
                    \mathcal B_C\simeq\mathcal O_C(B_\theta),
 \qquad B_\theta=W_1+W_2-W_\infty.
\]
This verifies the required Raynaud origin, not merely an arbitrary
translate of the Abel curve.

The reduced Mumford pair \(T=(h,0)\) represents
\[
                    [W_1+W_2-2W_\infty].
\]
It is two-torsion: \(\operatorname{div}(h)=2W_1+2W_2-4W_\infty\).
For an affine nonbranch point \(R=(z,v)\), the code forms
\([R-W_\infty]+T\). This equals
\[
                       [R-B_\theta],
\]
since \(-T=T\). Thus every saved point is on the **correct** theta
curve. The sign convention is also correct: \(v\mapsto v+1\)
changes this class to its negative. The canonical checker verifies
the polynomial curve equation for every saved point.

The polynomial \(X^{18}+X^7+1\) and the binary field representation
are checked by the independent field constructor. The constructor
enumerates all \(2^{18}-1\) nonzero powers of the supplied generator,
so every nonzero residue is a unit; this also certifies that this
quotient really is the field of \(2^{18}\) elements. The saved
\(\alpha=114587\) satisfies \(\alpha^2+\alpha=1\).

## 3. Exact group order and exponent

The previously independently checked actual \(\mathbf F_4\)
Weil polynomial is
\[
                   P(X)=X^4+2X^3+X^2+8X+16.
\]
The Newton sums in my executable give
\[
       s_9=-26,\qquad s_{18}=621026,\qquad q=4^9=262144.
\]
Therefore
\[
 \#J_C(\mathbf F_q)
 =q^2+1-(q+1)s_9+\frac{s_9^2-s_{18}}2
 =68725982332
 =4\cdot7^2\cdot31\cdot2503\cdot4519.
\]
The corresponding point count is \(q+1-s_9=262171\).
This is an independent recurrence calculation of the same group
order obtained by the search's determinant.

Put
\[
                     M=7\cdot31\cdot2503\cdot4519
                      =2454499369.
\]
Trial division verifies all four factors prime. The canonical
checker proves \([M]G=0\) and
\([M/p]G\ne0\) for each of the four prime factors, so the final
theta generator has **exact order \(M\)**.

It also constructs \(H\) of order seven, not in the cyclic subgroup
generated by \(A=[M/7]G\). Thus the seven-primary subgroup contains
\(C_7^2\). Its order is exactly \(49\), from the group order, so it
is \(C_7^2\), not \(C_{49}\). Every other odd primary part has prime
order. It follows rigorously that the **entire odd exponent** is
\(M\). The group order alone would not establish this fact; the
independent seven-point calculation is essential and is present.

## 4. The search's eight directions and CRT indices are correct

This paragraph audits the discovery code, although the fixed
certificate does not depend on its completeness.

Let \(G_0\) be its initial exact-order-\(M\) generator,
\(A_0=[M/7]G_0\), and choose \(c=(M/7)^{-1}\pmod7\).
Its first seven generators are
\[
                         G_r=G_0+[cr]H,\qquad 0\le r<7;
\]
their seven-primary projections are \(A_0+rH\). Its eighth
generator
\[
                         G_\infty=G_0-[c]A_0+[c]H
\]
has projection \(H\). Their other prime projections all equal
the corresponding projections of \(G_0\). These are exactly
the eight lines of \(\mathbf F_7^2\), with the common other
primary factors.

For a retained theta point \(D\), the test \([M]D=0\) removes
its two-primary component. If
\([M/7]D=uA_0+vH\), then for \(u\ne0\) its direction is \(v/u\)
and its scalar on that direction is \(u\); for \(u=0\), its
direction is infinity and its scalar is \(v\). The other scalars
are computed against the matching \([M/p]G_0\). The CRT
therefore gives the correct index relative to \(G_r\) or
\(G_\infty\).

Equality of these projections implies equality of the classes:
all classes involved are killed by squarefree \(M\), and on the
\(p\)-part the multiplier \(M/p\) is a unit. The nonzero
projection test also verifies that these theta classes have
exact order \(M\).

The selected direction is 1. Replacing its generator by the saved
theta point multiplies every index by the inverse of one unit
modulo \(M\). This permutes the doubling cosets. My executable
checks every one of the 1296 reindexings against the discovery
packet, including its prime-coordinate CRT values.

## 5. Complete primitive doubling-orbit coverage, independently

For each \(p\in\{7,31,2503,4519\}\), choose a primitive root
\(g_p\), and let \(a_p\) be the discrete logarithm of a unit
\(i\bmod p\). Let
\[
 v_p=\log_{g_p}2,\quad c_p=\gcd(v_p,p-1),\quad
 m_p=(p-1)/c_p.
\]
My executable chooses different primitive roots from the search,
namely \(5,24,2501,4510\). It obtains
\[
                  (c_p)=(2,6,2,6),\qquad
                  (m_p)=(3,5,1251,753).
\]
Write
\[
 r_p=a_p\bmod c_p,\qquad
 t_p=\frac{a_p-r_p}{c_p}(v_p/c_p)^{-1}\pmod {m_p}.
\]
Multiplication of \(i\) by two leaves every \(r_p\) unchanged
and adds one to every \(t_p\). Two units belong to the same
doubling orbit exactly when their four residues agree and
the four required time differences admit a common solution.
The pairwise gcds of the time moduli are one except that
the three moduli \(3,1251,753\) have pairwise gcd three.
Thus a complete orbit signature is
\[
 (r_7,r_{31},r_{2503},r_{4519},
                       t_{2503}-t_7\bmod3,\,
                       t_{4519}-t_7\bmod3).
\]
The generalized CRT proves both necessity and sufficiency.
There are exactly
\[
                    2\cdot6\cdot2\cdot6\cdot3\cdot3
                    =1296
\]
such signatures. Equivalently,
\[
 \operatorname{ord}_M(2)=\operatorname{lcm}(3,5,1251,753)=1570005,
 \qquad \frac{\varphi(M)}{\operatorname{ord}_M(2)}=1296.
\]

All saved indices are units. My executable verifies that the
1296 saved indices produce each of these signatures exactly
once, and that multiplying each index by two preserves its
signature. This proves exhaustion of **all primitive doubling
orbits**, independently of both the original normalization
and the canonical checker's integer HNF. The canonical
checker separately verifies
\[
                     [R_i-B_\theta]=[i]G
\]
for all 1296 points.

The search's triangular normalization is also valid: at each
step it normalizes one coordinate by a multiple of the already
stabilizing period, and increases that period by exactly the
remaining coordinate-orbit length. Its final period fixes
all coordinates. No traversal of the billion-element cyclic
subgroup is required.

## 6. Exact mathematical implication and scope

Let \(L\) be the degree-zero line bundle represented by the final
theta generator. It has exact odd order \(M\); after a finite
extension of the field of definition it gives a connected
cyclic étale cover \(D\to C\) of degree \(M\).

A.C2.5 gives one-dimensional nonzero character cohomology
spaces in genus two. A theta hit makes the corresponding
Frobenius arrow zero. Since every primitive doubling orbit has
a saved hit, **all primitive character blocks are nilpotent**.
Duality may invert character indices, but preserves both
primitivity and the orbit-exhaustion conclusion.

Consequently the actual primitive factor
\[
 P_M=\operatorname{im}\left(
     \prod_{p\mid M}(1-\sigma^{M/p}):J_D\to J_D\right)
\]
has two-rank zero. This is precisely the hypothesis of
A.C2.20 (or its genus-two version A.C2.19).
There are four prime factors, so the sparse divisor in that
proof has degree \(16\); the required numerical inequality
\(M>(16-1)^2\) is more than satisfied.

The conclusion is geometrically prime-to-two point-section
injectivity for this curve over finitely generated
characteristic-two fields, for its finite-extension forms,
and for its hyperbolic open subcurves. Coefficient Frobenius
conjugation proves the same for the paired class 302.
Together with the previously verified 46 classes and the
already proved exhaustive finite-field classification, this
settles all 48 classes in that enumeration.

No vanishing of the entire new part of \(J_D\) is asserted.
Proper-conductor character blocks may survive; A.C2.20 was
proved expressly to handle that situation. No extrapolation
to every ordinary genus-two curve or to universal A1 is
made.

## 7. Review conclusion

The fixed certificate has the correct theta origin, an exact
connected cyclic conductor, exact point-multiple relations,
and exhaustive primitive-orbit coverage. The seven-primary
rank and generator rescaling have no hidden group-structure
assumption. The implication to the existing primitive-Prym
theorem is direct and satisfies its hypotheses.

**Approved in this exact scope.**

## 8. Later full written-proof check

I subsequently read the entire integrated proof candidate
`audit/A_F4_all_48_candidate.md`. Its explicit ideal-class
derivation of the two extended-gcd composition formula and norm
reduction is correct, including coincident points and ramification
fibres. In particular the common factor removes a pair of
hyperelliptic conjugate points (twice the ramification point
when these coincide), and norm reduction replaces the
complementary divisor by its hyperelliptic conjugate. The source
uses the general \(h\)-polynomial characteristic-two formula,
rather than an odd-characteristic-only version.

The identification of the omitted class is also exact:
after \(x=z+r\), \(r^2+r=\alpha\), the normalized coefficients
are \(1,\alpha^2(r+1),\alpha^2r\), with elementary symmetric
functions \(\alpha,0,\alpha^2\). Its coefficientwise-square
conjugate supplies the other class. The finite-extension
trivialization of the exact-order-\(M\) line bundle gives a
connected cyclic étale cover, and the final form/open-curve
scope is precisely that of A.C2.19--20. No further wording or
mathematical correction was needed.


