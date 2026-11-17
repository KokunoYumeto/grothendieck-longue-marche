# Actual special source: relative Lefschetz and van Kampen applicability audit

Research record, 2026-11-16, checkpoint 15. This records a bounded primary-source
audit; it proves no new marginal-kernel equality and adds no formal statement.

## 1. The question and its actual source

Put

\[
Y=\{(v,w)\in(\mathbb C^*)^2:v,w\notin\mu _5,
v\ne w,\ vw\notin\mu _5\}.
\]

Let \(Y'\) fill the four components \(v=u\),
\(u\in\mu _5\setminus\{1\}\), retaining every other deleted component.
The prescribed curve is \(v+w=2\). Its complements \(L\subset Y\) and
\(L'\subset Y'\) have nineteen and fifteen finite excluded parameters,
respectively. The question is whether

\[
\operatorname{im}\bigl(\ker[\pi _1(L)\to\pi _1(L')]\to\pi _1(Y)\bigr)
=\ker[\pi _1(Y)\to\pi _1(Y')].
\]

The same question is posed for the actual compact images after full profinite
completion. Replacing this source by a generic member of a pencil would change
the question.

At each newly filled component the source meets transversely away from all other
components. Its finite old-boundary exception is \((1,1)\), where four retained
branches meet and the source is tangent to \(vw=1\). The failure of transversality
is therefore already present for \(Y'\), not introduced by the four filled
components.

## 2. Exact primary theorem checks

### Tibăr: a nongeneric pencil still uses a general fiber

Tibăr's 2005 version permits isolated stratified singularities of the pencil,
including singularities in its axis. In Theorem 1.1 the reference slice is still
\(X_c\) for a general parameter outside the critical-value set. The variation
description concerns higher homotopy; its stated range does not supply the
required fundamental-group comparison from this chosen exceptional slice.
Thus “nongeneric pencil” does not authorize replacing the reference general
fiber by the actual sum fiber at parameter 1. We checked the setup, Theorem 1.1,
and the definition of the critical parameters in the author's primary preprint.

Verified source: Tibăr, M. (2005). *The Zariski-Lefschetz principle for higher
homotopy groups of nongeneric pencils* (arXiv:math/0207108v4, April 8, 2005),
especially pp. 1–3 and §§2–3.
<https://arxiv.org/pdf/math/0207108>.

### Eyral–Petrov: “relative” means relative to the pencil axis

Section 2 first fixes a Whitney stratification with the deleted locus a union
of strata, then requires the selected hyperplane and the pencil axis to be
transverse to that stratification. Theorems 3.5–3.6 compute the fundamental
group from that general hyperplane, with relative variation operators based on
paths whose initial point lies in the axis. This is not a relative theorem for
two divisor complements \(Y\subset Y'\). The proof of Theorem 3.6 preserves the
general reference hyperplane when refining the stratification. The actual
source fails its reference-hyperplane hypothesis at \((1,1)\).

Verified source: Eyral, C., & Petrov, P. (2019). Zariski-van Kampen theorems for
singular varieties—an approach via the relative monodromy variation.
*Kodai Mathematical Journal, 42*(1), 75–98.
<https://doi.org/10.2996/kmj/1552982507>.
Primary full PDF, especially §2, pp. 78–79, and Theorems 3.5–3.6, pp. 83–84:
<https://www.jstage.jst.go.jp/article/kodaimath/42/1/42_75/_pdf/-char/en>.

### Shimada: a section controls generic-fiber monodromy, not this special source image

Shimada fixes a locally trivial open base \(Y^\circ\), a point
\(b\in Y^\circ\), and the reference fiber \(F_b\). Theorem 3.20 imposes the
conditions (C1), (C2), and (Z). The section-curve version, Theorem 3.33, further
requires surjectivity from the punctured section curve onto the fundamental
group of the regular base, a corresponding \(\pi _2\) condition, and transverse
section intersections with the discriminant. Its conclusion describes the
kernel from \(\pi _1(F_b)\), not the image of the kernel of an arbitrary
punctured section after filling selected crossings. Proposition 3.1 likewise
keeps the general reference fiber. These statements justify generic-fiber
presentations but do not remove the present normalization problem.

Verified source: Shimada, I. (2010). Generalized Zariski-van Kampen theorem and
its application to Grassmannian dual varieties. *International Journal of
Mathematics, 21*(5), 591–637.
<https://doi.org/10.1142/S0129167X10006252>.
Primary author manuscript, especially Proposition 3.1, Theorem 3.20, and
Theorem 3.33 with its proof (manuscript pp. 31–33):
<https://home.hiroshima-u.ac.jp/ichiro-shimada/preprints/newZvK/pioneU.pdf>.

## 3. What the actual w projection does and does not add

The coordinate \(z=wv\) is legitimate on the actual surface. Over
\(w\in\mathbb C^*\setminus\mu _5\), the generic fiber punctures are

\[
0,\quad w\mu _5,\quad w^2,\quad\mu _5,
\]

and the actual moving source point is \(z=w(2-w)\). The five additional
finite collision fibers occur at \(w\in-\mu _5\). Each is an old-only node:
the diagonal point meets a product point. The four added constant components
avoid these collisions. This observation alone is not a kernel-surjectivity
theorem.

DE's existing calculation already includes all five node relations in a single
source-compatible marking. Its transported product-one relation is

\[
[d,(ba)^{-1}(zc_3c_4)b(zc_3c_4)^{-1}(ba)]=1,
\]

not the untransported relation \([d,b]=1\). Discarding the conjugating word
would discard precisely the source information under investigation.

Let \(H\) be the actual source image, \(J_c\) its constant-family kernel
image, and \(R_c\) the ambient filling kernel. The common-marked presentation
has the exact statements

\[
J_c\triangleleft H,\qquad J_c\subset R_c,
\qquad G=\langle H,a,d,b\rangle,
\]

and hence

\[
J_c=R_c\quad\Longleftrightarrow\quad
a,d,b\text{ normalize the entire }J_c.
\]

The forward implication is normality of the ambient kernel. For the reverse,
the proposed normalizations make \(J_c\) normal in \(G\); it already contains
the four actual meridians normally generating \(R_c\). This is an exact
remaining condition, not a finite list of meridian-membership tests.

Existing actual-source evidence:
`work_DE/next_marginal_source/w_projection_common_transport.md`,
`w_positive_negative_transport.json`, and the independent common-path CE audit.
No replacement marking or new numerical braid extraction was made in this audit.

## 4. Two essential boundaries from existing results

**New-only transversality is insufficient in general.** B80 is already an
actual finite-cover counterexample with a single old source tangency and a
transverse source intersection with the added divisor. Its eight-sheet cover
has source-kernel image \(C_2\) but ambient filling-kernel image \(C_2^2\).
This rules out the broad relative shortcut. It does not decide the present
surface: B80's added and retained divisors also have a tangency elsewhere,
whereas the present added verticals meet retained multiple points with distinct
branch tangents. The latter global incidence is additional data that a more
specialized argument would have to use.

**Filling product one changes the status.** The accepted root note
`records/product_one_filling_reduction_13h.md` proves the desired comparison
after additionally filling \(vw=1\), because the same source then becomes a
generic ratio-pencil fiber. The original quotient defect is localized in the
kernel of that extra filling. This does not permit filling product one in the
original task.

## 5. Outcome

The three primary theorem families checked here do not establish the requested
equality for the prescribed source. This is an applicability conclusion about
those exact statements, not a claim that no suitable theorem exists.

A successful new argument must control the globally transported interaction of
the four filled verticals with the old boundary, equivalently the actual
\(a,d,b\) normalizations above. Neither generic-fiber surjectivity, ordinary
normal generation of meridians in the ambient group, nor transversality only at
the four source crossings supplies that control. No formal status is changed.
