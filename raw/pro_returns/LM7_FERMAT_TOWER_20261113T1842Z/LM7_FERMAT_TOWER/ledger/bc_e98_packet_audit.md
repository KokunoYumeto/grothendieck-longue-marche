# Independent E98 source and packet audit

Status: **PASS for the proposed arithmetic source, normalized packet
classification, and exact full-to-metabelian comparison.** The complete E98
theorem text had not yet been supplied for this audit. No new assertion about
sections ramified outside the specified set is inferred.

## Scope and material read

I read both owned program sources,
research_e98/code/e_global_split7_explore.py and
research_e98/code/e_global_split7_residues.py, and their exact certificate
structure. I read the complete relevant arguments of E.56, E.61, E.66, E.71,
and E.73, with the actual unramified action comparison of E.34 and inertia
comparison of E.39. The E.56 source presentation specializes literally to
seven; no new free-product assumption is needed.

I freshly opened Wingberg, *Riemann's existence theorem and the
K(pi,1)-property of rings of integers*, original preliminary version dated
December 6, 2007:

<https://www.mathi.uni-heidelberg.de/~wingberg/agwingberg/paperwingberg/Riemann-kpi1.pdf>

The checked passages are the continuous bundle and Lemma 1.1 on printed
pages 4–5; the remark after Proposition 2.1 on printed page 11; and
Theorem 2.4, including its infinite-set clause and full proof, on printed
pages 13–15. Retrieval references: turn813view0, turn814view0,
turn815view0.

## The actual arithmetic source

Put \(K=\mathbb Q(\zeta_3)\), let \(S_0\) be its prime over three, and let
\(S=S_0\cup\{\mathfrak p,\bar{\mathfrak p}\}\), where the latter primes lie
over seven. The E.34/E.49 group
\(P=G_{K,S_0}^{(3)}=\langle\tau,\tau'\rangle\) is free pro-three.
The E.56.11–13 normalization chooses actual Frobenii at these two
prolongations, related by the original complex conjugation, with
\(\chi(\tau)=\chi(\tau')=7\) and
\(\kappa_3(3)(\tau)=1,\ \kappa_3(3)(\tau')=-1\).
Their two Frattini characters have determinant
\(-2((7-1)/3)\), a three-adic unit. They therefore give this free basis.
Choosing positive inertia \(t\) at the first prolongation and
\(t'=ct^{-1}c\) gives the two literal tame relations
\[
 \tau t\tau^{-1}=t^7,\qquad
 \tau't'(\tau')^{-1}=(t')^7.
\]

Wingberg supplies the kernel as the continuous free product of the actual
inertia groups over \(P/\langle\tau\rangle\) and
\(P/\langle\tau'\rangle\). The hypotheses hold: \(S_0\) contains every
three-adic place, and the cyclotomic tower gives nontrivial unramified
completion at both primes, with Frobenius seven. Inertia injects by this
comparison; the unramified cyclic subgroup injects because its cyclotomic
character has infinite order.

Use the section of \(P\) specified by these actual two Frobenii.
The induced inertia bundle has exactly the identifications
\[
 (p\tau^z,t^u)=(p,t^{7^z u}),
\]
and the corresponding primed identifications. Its semidirect product
with \(P\) maps to and from
\[
 D_7 *_3D_7',\qquad
 D_7=\langle t,\tau\mid\tau t\tau^{-1}=t^7\rangle_3.
\]
Both maps fix all four displayed generators, so are inverse. Wingberg's
map on the kernel is induced by the same actual inertia inclusions,
and the quotient map is the identity on \(P\). This proves the arithmetic
isomorphism, not merely a generator-count comparison.

The same four generators already lie in \(G_K^{(3)}\); their inclusions
define a reverse map from \(D_7*_3D_7'\) whose composite with projection
is the identity. It commutes with \(c\), which exchanges the Frobenii and
sends \(t\) to \((t')^{-1}\). This is an actual splitting of the
finite-ramification arithmetic quotient. It does not remove the E.39
Frobenius correction words at omitted primes for sections having further
ramification.

## The exact normalized section space

Let \(V\) be \(N\) or \(M=N/N''\), with the genuine action \(T\) of
\(\tau\) and \(J\) of \(c\). The action is unramified outside three and
has pro-three image over \(K\), by E.34. A continuous cocycle unramified
outside \(S\), paired with its action, is a homomorphism into a pro-three
semidirect product. It therefore factors through the actual maximal
pro-three quotient above. Conversely a cocycle on that quotient inflates
to the original arithmetic group. These maps preserve geometric
conjugacy and are inverse on the stated subspace.

If the cocycle value at \(c\) is \(z\), then \(J(z)=z^{-1}\).
Conjugation by \(z^{-1/2}\) makes that value one. The square roots here
are the unique square roots in the relevant pro-three group; their
existence, uniqueness and continuity follow on every finite three-group
quotient and then on the inverse limit. Residual conjugations are exactly
\(V^J\).

After this normalization, set \(u=a(\tau)\), \(a=a(t)\).
The other values are forced:
\[
 a(\tau')=J(u),\qquad a(t')=J(a)^{-1}.
\]
Since arithmetic inertia acts trivially on \(V\), the first tame relation
becomes exactly
\[
             uT(a)u^{-1}=a^7.
\]
The second is its \(J\)-image. The free-product universal property proves
sufficiency and continuity of the resulting section. Residual conjugation
by \(h\in V^J\) sends this pair to
\[
 (h uT(h)^{-1},\ h a h^{-1}).
\]
Thus the proposed pair quotient is exact in both directions.

The zero-inertia part \(a=1\) is precisely the unramified-outside-three
space already computed in E.41. Its normalized pair quotient is
\(u/(u\mapsto h uT(h)^{-1}),\ h\in V^J\).

## Every ramified packet and all its redundancies

Fix for each cusp \(D\) the actual positive inertia \(\delta_D\) and the
actual tangential Frobenius \(z_D\tau\), so that
\(z_DT(\delta_D)z_D^{-1}=\delta_D^7\).
E.61 applies to the full group. E.66 applies to every nontrivial
metabelian inertia: its proof first excludes inertia with zero abelian
image and then treats all nonunit exponents. Its final Magnus calculation
proves
\[
 C_M(\delta_D^r)=\langle\delta_D\rangle
 \quad(r\ne0);
\]
the full centralizer has the same equality by the actual free-factor
comparison.

Consequently every ramified pair has the form
\[
 a=g\delta_D^r g^{-1},\qquad
 u=g\delta_D^b z_DT(g)^{-1},\qquad r\ne0.
\]
The cusp and \(r\) are determined by abelian inertia. Equality of two
such representatives at fixed \(D,r\) implies
\(g'=g\delta_D^k\). Direct substitution gives equality precisely when
\(b'=b+6k\). The quotient \( \mathbb Z_3/6\mathbb Z_3\) has the unique
representatives \(0,1,2\). Choosing this representative determines \(k\)
uniquely, and once \(b\) is fixed there is no remaining right-cusp
ambiguity. The remaining geometric conjugation is exactly left
multiplication by \(V^J\).

The ramified global subspace therefore has the exact coordinates
\[
 \coprod_{D}
 (\mathbb Z_3\setminus\{0\})\times\{0,1,2\}\times V^J\backslash V.
\]
This is a homeomorphism. On each fixed-valuation annulus for \(r\), the
parameter space is compact and its continuous bijection to the Hausdorff
geometric orbit space is a homeomorphism. These annuli are clopen in the
ramified subspace, as detected by its actual abelian inertia.

The final quotient has explicit, choice-free coordinates:
\[
 V^J\backslash V\longrightarrow
 \{x\in V:J(x)=x^{-1}\},\qquad
 [g]\longmapsto g^{-1}J(g).
\]
Its inverse sends \(x\) to \([x^{-1/2}]\). Left \(V^J\)-invariance is
immediate; equality of two coordinates implies that \(g'g^{-1}\) is
\(J\)-fixed. This proves both directions and continuity.

## Exact full-to-metabelian global fibers

Let \(R=N''\). With the same projected paths and tangents, the ramified
map is literally
\[
 (D,r,b,[g])\longmapsto(D,r,b,[\bar g]).
\]
It is onto. Fixed elements also lift explicitly: given
\(\bar h\in M^J\), choose \(h_0\in N\), put
\(k=h_0^{-1}J(h_0)\in R\), and set \(h=h_0k^{1/2}\).
Then \(J(k)=k^{-1}\), \(J(h)=h\), and \(h\) maps to \(\bar h\).

Choose a lift \(g_0\) of a representative \(\bar g\) of a target coset.
Every source coset mapping to it has a representative \(kg_0\), \(k\in R\):
lift and remove the needed left \(M^J\)-factor by the preceding formula.
Two such representatives are equivalent exactly when their \(k\)'s
are left equivalent under \(R^J\). Hence the entire global fiber is
homeomorphic to \(R^J\backslash R\), via the actual map
\([k]\mapsto[kg_0]\). This states precisely the additional global
conjugator information beyond E.66's unique local full class.

## Program-source checks and independent small certificate

The two supplied programs correctly use the primitive determinant line,
the quotient map \(Q\), the integral differential
\(\bigwedge^2 T/7-1\), and its exact left/right Smith transformations.
The nonzero local cokernel factors are \(C_3^{18}\oplus C_9^{12}\).
The horizontal representatives have three order-three coordinates and
six free coordinates. The two-digit algorithm retains its divided
constant and divided-kernel carry terms. The high-row left-kernel test
is the exact solvability condition for the second digit, and every
retained solution is substituted back into all original congruences.
No additional global ramification or full/metabelian lift follows from
these finite class-two calculations alone.

The owned independent program bc_split7_packets.py verifies all 73
retained inverse witnesses against 2190 original congruences and proves
that the resulting relative residue set is exactly the union of the
nine cusp lines modulo nine. It also checks the explicit coset,
anti-fixed, inverse-square-root, and central-fiber maps on all 729
elements of a nonabelian finite three-group. This finite model is
only a verification of the algebraic formulas; the arithmetic transfer
is the proof above. Its actual stdout and full JSON are retained.

No full copied rerun of the two root-owned exploration programs is
claimed in this peer audit. The complete program sources and their
mathematical reduction were checked, and the independent smaller
certificate was executed successfully.
