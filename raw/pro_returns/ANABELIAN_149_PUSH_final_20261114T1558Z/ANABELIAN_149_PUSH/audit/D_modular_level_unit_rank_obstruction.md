# Full Legendre levels do not force growth of the rational unit rank

Status: proved route limitation, retained as an audit. This note does not prove finite ramification for an arbitrary section, construct a nongeometric section, or settle the mixed-label case in D.31. It proves that a proposed source of unit-rich neighbourhoods can fail completely: maximal torsion image gives exactly three rational cusp orbits at every full odd level. An explicit rational point supplies an infinite such tower.

After root's complete review, the proof was integrated as D.32 in sections/D_modular_unit_obstruction.tex, immediately after D.31. This full audit is retained as the source and review history; the stated limitations are unchanged.

The original question is 149; manuscript pp.27–31,62v–63; scans56,59–63,126–127. The comparison is with the separately proved D.30–D.31, and is not attributed to the manuscript.

## 1. The neighbourhoods actually attached to a section

Put
\[
 U=\mathbf P^1_{\mathbf Q}\setminus\{0,1,\infty\},\qquad
 \mathcal E_\lambda:\ y^2=x(x-1)(x-\lambda).
\]
For a continuous section \(s\) and an odd integer \(N\ge3\), let
\(W_N=s^*\mathcal E[N]\). It is a finite étale rank-two
\(\mathbf Z/N\)-module over \(\mathbf Q\), with its alternating Weil pairing
to \(\mu_N\). Define the finite étale cover
\[
 Y_{s,N}
   =\operatorname{Isom}_{\rm sympl}(W_N,\mathcal E[N])\longrightarrow U.
 \tag{1}
\]
Representability and étaleness can also be seen directly by étale locally
trivializing the two finite étale modules: (1) becomes the constant finite
set \(\operatorname{SL}_2(\mathbf Z/N)\). Pulling it back along \(s\), the
identity of \(W_N\) is fixed by \(G_{\mathbf Q}\), so \(s\) lifts to this
cover. This uses the actual integral torsion module. A rational
Tate-module comparison in D.30 is not silently promoted to an isomorphism
of all integral lattices.

The two usual geometric Legendre monodromies, in a symplectic basis, are
\[
 A=\begin{pmatrix}1&2\\0&1\end{pmatrix},\qquad
 B=\begin{pmatrix}1&0\\-2&1\end{pmatrix}.
 \tag{2}
\]
Their direct Picard–Lefschetz computation is given by Carlson,
Müller-Stach, and Peters (2017, §1.1, pp.20–21). Since \(2\) is invertible
modulo \(N\), their powers contain every upper and lower elementary
unipotent. These generate \(\operatorname{SL}_2(\mathbf Z/N)\): over each
local factor of \(\mathbf Z/N\), elementary row operations reduce a
unimodular column, and the Chinese remainder theorem combines these
operations. Thus (1) is geometrically connected, with geometric deck
group
\[
                         G_N=\operatorname{SL}_2(\mathbf Z/N).
 \tag{3}
\]

There is a distinction between this full torsion cover and its quotient
by the central sign. The latter is geometrically the usual congruence
cover \(X(2N)\to X(2)\); the full torsion cover has twice its degree.
We retain the full cover in the calculation rather than identifying
these two objects.

## 2. Geometric cusp fibres

Let \(C_{s,N}\) be the smooth completion of \(Y_{s,N}\). The third
horizontal monodromy is
\[
 C=(AB)^{-1}=\begin{pmatrix}1&-2\\2&-3\end{pmatrix}.
 \tag{4}
\]
The elements \(A\) and \(B\) have order \(N\), while \(C\) has order
\(2N\). Indeed \(C=-I+M\), with \(M^2=0\) and at least one entry of \(M\)
invertible modulo \(N\); since \(N\) is odd, its scalar and unipotent
parts have respective orders \(2\) and \(N\).

For each rational label \(c=0,1,\infty\), choose the horizontal inertia
subgroup \(I_c\subset G_N\). In a suitable basis the first two are the
upper unipotent subgroup \(U_N\), and the third is
\(\{\pm1\}U_N\). The geometric cusp fibre is the left coset set
\(I_c\backslash G_N\). Consequently the three geometric counts are
\[
 \frac{|G_N|}{N},\qquad \frac{|G_N|}{N},\qquad
 \frac{|G_N|}{2N},\qquad
 |G_N|=N^3\prod_{\ell\mid N}(1-\ell^{-2}).
 \tag{5}
\]
The projectivized cover has \(|G_N|/(2N)\) cusps over each label.
These are geometric counts, not counts of closed points over
\(\mathbf Q\). The standard cusp classification by primitive vectors
modulo \(N\), and the determinant/cyclotomic arithmetic action, are
also recorded in Sutherland and Zywina (2017, Lemma 2.1 and Proposition
2.2, pp.1206–1207).

For example, at \(N=5\) the full cover has degree \(120\), with
\(24,24,12\) geometric cusps and genus \(31\). Its projectivization has
degree \(60\), \(12\) cusps over each label, and genus \(13\).

## 3. Maximal image leaves one closed cusp over each label

Assume
\[
       \rho_{s,N}(G_{\mathbf Q})
          =\operatorname{GL}_2(\mathbf Z/N).
 \tag{6}
\]
Then each of the three geometric cusp fibres is a single
\(G_{\mathbf Q}\)-orbit.

Here are the action conventions and the proof. Fix a tangential
splitting at \(c\), a local Tate basis, and a basis of \(W_N\).
A symplectic level isomorphism is a matrix \(h\in G_N\), and
\(\sigma\in G_{\mathbf Q}\) acts by
\[
                 h\longmapsto
          \rho_c(\sigma)h\rho_{s,N}(\sigma)^{-1}.
 \tag{7}
\]
The local Legendre degeneration is potentially multiplicative. Tate
uniformization, after its quadratic splitting twist, gives the
filtration with characters \(\chi_N\) and \(1\). Restricting the
quadratic splitting character to the chosen tangential splitting
gives a character \(\delta_c:G_{\mathbf Q}\to\{\pm1\}\).
On \(G_{\mathbf Q(\mu_N)}=\ker\chi_N\), therefore,
\[
                    \rho_c(\sigma)=\delta_c(\sigma)u_\sigma,
                         \qquad u_\sigma\in I_c.
 \tag{8}
\]
At infinity the additional horizontal sign is already in \(I_\infty\);
it causes no change to this assertion on inertia cosets. The relevant
Tate uniformization and its Galois equivariance are recalled in
Conrad's Math 248B notes, §19, p.44; the formula here is the resulting
two-dimensional torsion representation.

Passing (7) to left cosets and using the centrality of \(\delta_c\)
gives
\[
 I_ch\longmapsto
       I_ch\bigl(\delta_c(\sigma)\rho_{s,N}(\sigma)\bigr)^{-1}.
 \tag{9}
\]
Because \(\det\rho_{s,N}=\chi_N\), hypothesis (6) implies that
\(\rho_{s,N}\) maps \(G_{\mathbf Q(\mu_N)}\) onto \(G_N\).
The image \(H_c\) of its quadratic twist in (9) has the same image in
\(G_N/\{\pm I\}\). Hence
\[
                  H_c\{\pm I\}=G_N,\qquad [G_N:H_c]\le2.
 \tag{10}
\]
There is no quotient of \(G_N\) of order two: the elementary
unipotents generate it and each has odd order dividing \(N\).
If the index in (10) were two it would give just such a quotient.
Thus \(H_c=G_N\), proving transitivity in (9).

The original three labels are rational and distinct, so no Galois
element interchanges them. It follows that \(C_{s,N}\setminus Y_{s,N}\)
has exactly three closed points over \(\mathbf Q\), one over each
label. The same conclusion holds for the projectivization, either by
passing to its quotient or directly by killing the scalar signs in
(9).

This argument allows nonsplit multiplicative tangential models; it
does not assume their quadratic splitting characters are trivial.

## 4. All rational units come from the two original directions, up to powers

Let \(D_0,D_1,D_\infty\) be the three closed boundary divisors just
obtained, with coefficient one on each geometric point in its Galois
orbit. Since \(Y_{s,N}\) is geometrically connected, the divisor map
injects
\[
 \mathcal O(Y_{s,N})^\times/\mathbf Q^\times
     \hookrightarrow
 \operatorname{Div}^0_{\partial C_{s,N}}(C_{s,N})(\mathbf Q).
 \tag{11}
\]
The right side is the kernel of the nonzero degree map from the free
rank-three group on \(D_0,D_1,D_\infty\), and therefore has rank two.
The pullbacks of \(\lambda\) and \(1-\lambda\) are independent units,
so
\[
              \operatorname{rank}
        \bigl(\mathcal O(Y_{s,N})^\times/\mathbf Q^\times\bigr)=2.
 \tag{12}
\]

More precisely, if \(v\) is any rational unit, there exist
\(m>0\), \(a,b\in\mathbf Z\), and \(q\in\mathbf Q^\times\) such that
\[
                     v^m=q\,\lambda^a(1-\lambda)^b.
 \tag{13}
\]
To see this, let \(e_c\) denote the ramification index over \(c\).
Then
\[
 \operatorname{div}(\lambda)=e_0D_0-e_\infty D_\infty,\qquad
 \operatorname{div}(1-\lambda)=e_1D_1-e_\infty D_\infty.
 \tag{14}
\]
These are independent and span the rational vector space underlying
the degree-zero lattice in (11). Clear denominators for
\(\operatorname{div}(v)\), and then take the constant quotient of
the functions with equal divisors. Its constant belongs to
\(\mathbf Q\), since \(\mathbf Q\) is algebraically closed in the
function field of a geometrically connected curve.

If a unit is regular and nonzero at closed cusps above two different
original labels, the two corresponding coefficients in (14) vanish.
For labels \(0,1\) this says \(a=b=0\); for \(0,\infty\) it says
\(a=0,a+b=0\); and for \(1,\infty\) it says \(b=0,a+b=0\).
Thus such a unit is constant.

Consequently, under (6), these full level neighbourhoods cannot
supply D.31's nonconstant unit if the lifted local cusps use two
different original labels. Their rank also never exceeds a number
of exceptional places that is at least two. This does not show that
every other finite étale neighbourhood fails; D.31 permits much more
than congruence level covers.

## 5. The exact role of Manin–Drinfeld

The distinction between geometric cusps and rational cusp orbits
persists even when every geometric cusp difference is torsion.
Drinfeld's original Theorem 1 states this torsion property for
congruence modular curves (1973, Russian original, p.83).

In particular, for a \(\mathbf Q\)-form of a congruence modular curve
with its cuspidal boundary
with \(c\) closed boundary points, the rational unit rank is \(c-1\).
Indeed any rational degree-zero boundary divisor becomes torsion in
the geometric Picard group by the theorem, so some multiple is
principal over a finite extension \(L/\mathbf Q\).
Enlarge \(L\) to be Galois and take the norm of the function; the
result is a rational function whose divisor is a positive multiple
of the original divisor. Thus rational principal boundary divisors
have finite index in the degree-zero boundary lattice.

This applies in particular to the projectivized congruence covers
above, giving rank two again. The stronger full-cover conclusions
(12)–(13) did not need Manin–Drinfeld: their lower bound already
comes from the two base units. The theorem cannot turn a single
large Galois orbit of cusps into many rationally independent units.

## 6. An explicit infinite maximal-image tower

Take the actual rational point section at \(\lambda=3\), and write
\[
                    E_3:\ y^2=x(x-1)(x-3).
 \tag{15}
\]
Its full \(5\)-adic image is
\(\operatorname{GL}_2(\mathbf Z_5)\). The following short proof avoids
an uncomputed open-image assertion.

First,
\[
                    \Delta(E_3)=576,\qquad c_4(E_3)=112.
 \tag{16}
\]
At the local prime \(3\), the model is minimal and has multiplicative
reduction of Kodaira type \(I_2\), since \(v_3(c_4)=0\) and
\(v_3(\Delta)=2\). Its Tate parameter after at most an unramified
quadratic extension has valuation \(2\). The \(5\)-adic inertia image
therefore contains a full unipotent subgroup
\[
                       U(\mathbf Z_5)
        =\left\{\begin{pmatrix}1&z\\0&1\end{pmatrix}:z\in\mathbf Z_5\right\}.
 \tag{17}
\]
Explicitly, the Kummer parameter on inertia is \(2t_5\), which is
surjective because \(2\) is a \(5\)-adic unit. A nonsplit
multiplicative twist is unramified, so does not alter (17).

At the good prime \(7\), the only affine points are
\((0,0),(1,0),(3,0)\); including infinity gives
\(\#E_3(\mathbf F_7)=4\). Its Frobenius \(g\) has characteristic
polynomial
\[
                            T^2-4T+7.
 \tag{18}
\]
Modulo five its discriminant is \(3\), a nonsquare. If \(e_1\) spans
the fixed line of (17), then \(e_1,e_2=ge_1\) form a
\(\mathbf Z_5\)-basis. In that basis,
\[
              g=\begin{pmatrix}0&-7\\1&4\end{pmatrix},\qquad
                   gE_{12}g^{-1}=-\frac17 E_{21}.
 \tag{19}
\]
The original unipotent subgroup remains the entire upper root
subgroup in this basis, and (19) supplies the entire lower one.
These generate \(\operatorname{SL}_2(\mathbf Z_5)\).
Finally the determinant is the surjective \(5\)-adic cyclotomic
character, so the image is all of
\(\operatorname{GL}_2(\mathbf Z_5)\).

It follows that every \(N=5^a\) satisfies (6) for this section.
These connected neighbourhoods have unbounded degree, genus and
number of geometric cusps, but each has exactly three closed
boundary points over \(\mathbf Q\) and rational unit rank exactly
two. The section in this example is already geometric; its role
is to disprove the proposed automatic growth of the rational unit
rank in this class of neighbourhoods.

## 7. A bounded-image-index variant

There is also a useful conditional boundedness statement. Fix an
odd prime \(\ell\), and suppose the image of
\(G_{\mathbf Q(\mu_{\ell^\infty})}\) under \(\rho_{s,\ell}\) has
finite index \(m\) in \(\operatorname{SL}_2(\mathbf Z_\ell)\).
At every projective level \(\ell^a\), (9) loses the scalar character.
The image acting on each cusp fibre has index at most \(m\) in the
ambient transitive group. An index-\(m\) subgroup has at most \(m\)
orbits on any transitive ambient group set. Hence there are at most
\(3m\) rational cusp orbits, and the rational unit rank is at most
\(3m-1\), uniformly in \(a\).

For the full covers, restrict further to the kernel of
\(\delta_c\) for each of the three labels. This increases the
image index by at most two, so there are at most \(6m\) closed
cusps and the rank is at most \(6m-1\). This bound is only an upper
bound; (6) yields the sharper rank two already proved.
The argument assumes the displayed finite index. It does not
deduce it for arbitrary section systems.

## 8. Reproducible checks and source scope

The standard-library script
`code/D_modular_cusp_orbits.py` writes
`code/D_modular_cusp_orbits.json`. It checks exactly:

- the \(120\)-element \(\operatorname{SL}_2(\mathbf F_5)\) generated
  by (2), and the inertia orders \(5,5,10\);
- the left-coset counts \(24,24,12\), and transitivity of the right
  action on each fibre;
- the corresponding three projective fibres of size \(12\);
- the point count in (18), the nonsquare discriminant, and the
  \(480\)-element \(\operatorname{GL}_2(\mathbf F_5)\) generated by
  the displayed Frobenius and one unipotent;
- the rational matrix identity (19), and the numerical cusp/genus
  formulas at levels \(5,25,125,625\).

The all-level and Galois conclusions are proved above, not inferred
from these finite checks. The script returned PASS on
14 November 2026. The action convention, the scalar-twist argument
and the explicit \(E_3\) calculation were independently reviewed by
the topos agent.

The following primary texts were opened directly:

| Source | Exact opened passage | Use and scope |
|---|---|---|
| Carlson, Müller-Stach, and Peters (2017) | §1.1, printed pp.20–21; publisher preview PDF pp.36–37 | The two explicit monodromy matrices (2). We do not use the subsequent literal identification with \(\Gamma(2)\) in Theorem 1.1.7, which obscures its central sign; the required finite odd-level image is proved directly. |
| Sutherland and Zywina (2017) | Lemma 2.1 and Proposition 2.2, printed pp.1206–1207; publisher PDF pp.10–11 | Primitive-vector cusp description and the determinant/cyclotomic modular-function-field action. The twist action (7)–(9) is separately derived here. |
| Conrad, Math 248B notes | §17, Proposition 17.6, pp.38–39; §19, p.44 | Finite étale level-isomorphism spaces and Galois-equivariant Tate uniformization. The point count and matrix generation in §6 are our explicit computations. |
| Drinfeld (1973) | Theorem 1 and its proof, original Russian pp.83–84 | Torsion of differences of congruence cusps. The original Russian PDF, not an English translation, was opened. The rational norm descent in §5 is supplied here. |
| Zywina (undated author copy opened 14 November 2026) | §§2.3–2.4, Lemma 2.3, author p.4 | Corroborating double-coset cusp description and cyclotomic fields of definition; not needed for the maximal-image proof. |

### References

Carlson, J., Müller-Stach, S., & Peters, C. (2017).
*Period mappings and period domains* (2nd ed.). Cambridge University
Press. https://doi.org/10.1017/9781316995846
Opened publisher preview:
https://api.pageplace.de/preview/DT0400.9781108118989_A30888647/preview-9781108118989_A30888647.pdf

Conrad, B. (n.d.). *Math 248B: Modular curves* [Course notes].
Stanford University.
https://virtualmath1.stanford.edu/~conrad/248BPage/handouts/modularcurves.pdf
The pagination above is that of this 47-page course-notes copy.

Drinfeld, V. G. (1973). Two theorems on modular curves.
*Functional Analysis and Its Applications, 7*(2), 155–156.
Original Russian: *Funktsional'nyi Analiz i ego Prilozheniya, 7*(2),
83–84. Metadata:
https://www.mathnet.ru/php/archive.phtml?jrnid=faa&option_lang=eng&paperid=2422&wshow=paper
Opened original:
https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=eng&paperid=2422&what=fullt

Sutherland, A. V., & Zywina, D. (2017). Modular curves of prime-power
level with infinitely many rational points.
*Algebra & Number Theory, 11*(5), 1199–1229.
https://doi.org/10.2140/ant.2017.11.1199
Opened publisher PDF:
https://msp.org/ant/2017/11-5/ant-v11-n5-p05-p.pdf

Zywina, D. (n.d.). *Improved bounds for integral points
on modular curves using Runge's method* [Author manuscript].
https://pi.math.cornell.edu/~zywina/papers/Runge.pdf
The source is used only for the exact corroborating cusp passage
listed above.
