# Independent verification: a characteristic-two counterexample to unrestricted Lie-side vanishing

## Result and scope

**The proposed example is correct.** For every field \(k\) of characteristic \(2\), the semisimple adjoint algebraic group \(G=\mathrm{PGL}_{2,k}\) has Lie algebra \(\mathfrak g=\mathfrak{gl}_2(k)/kI\), and

\[
\dim_k\operatorname{Der}_k(\mathfrak g)=6,\qquad
\dim_k\operatorname{ad}(\mathfrak g)=3,\qquad
\dim_k H^1(\mathfrak g,\mathfrak g)=3.
\]

Here \(H^1\) means ordinary Lie algebra cohomology with the adjoint module. In particular, the unrestricted Lie-side vanishing question at **C45:040, final display** has a negative answer. This calculation makes no assertion about \(H^*(G,\mathfrak g)\), whose intended definition is itself part of the question on that page. It does not settle any uncertain reading in C45:042, and it does not contradict the explicitly conditional claims in C45:038.

Confidence: **high**, from a symbolic proof over arbitrary characteristic-two fields, an independent finite enumeration based on actual matrix commutators, and primary-source confirmation of the group and Lie-algebra identifications.

## Group and Lie algebra

The quotient \(\mathrm{GL}_2\to\mathrm{PGL}_2\) has smooth scalar kernel \(\mathbb G_m\), hence its differential gives \(\mathfrak g=\mathfrak{gl}_2/kI\). This uses the \(\mathrm{GL}_2\) quotient; it must not be replaced by an asserted characteristic-two isomorphism \(\mathfrak{sl}_2\simeq\mathfrak{pgl}_2\).

For primary-source confirmation, Garibaldi–Guralnick, *Essential dimension of algebraic groups, including bad characteristic*, arXiv:1512.09158v2, Example 4.2, identifies \(\mathrm{PGL}_n\) as adjoint of type \(A_{n-1}\); Example 9.3 explicitly identifies \(\mathfrak{pgl}_2\) with matrices modulo scalars and discusses characteristic two. See [the authors' paper](https://arxiv.org/html/1512.09158v2). Milne's *Reductive Groups*, version 2.00, §15.16 defines adjoint as semisimple with trivial centre, and §17.60 explicitly states that \(\mathrm{PGL}_2\) is adjoint; its conventions allow an arbitrary field. See [Milne's notes](https://www.jmilne.org/math/CourseNotes/RG.pdf), printed pp.65 and80. These sources are used only for the group/Lie identification, not as sources for the cohomology calculation below.

Let

\[
h=\begin{pmatrix}1&0\\0&0\end{pmatrix}\bmod kI,
\quad x=E_{12}\bmod kI,
\quad y=E_{21}\bmod kI.
\]

These form a basis. Matrix commutators give

\[
[h,x]=x,\qquad [h,y]=-y=y,\qquad
[x,y]=\operatorname{diag}(1,-1)\bmod kI=0,
\]

because \(-1=1\). Thus \(V=kx\oplus ky\) is an abelian ideal, \(\mathfrak g=kh\ltimes V\), and \(\operatorname{ad}h\) acts as the identity on \(V\). In particular, semisimplicity of the algebraic group does not imply semisimplicity of this Lie algebra in characteristic two.

## An explicit outer derivation

Define \(D(h)=0\), \(D(x)=x\), \(D(y)=0\). The derivation identity on the three distinct basis pairs is

\[
\begin{aligned}
D([h,x])&=x=[D(h),x]+[h,D(x)],\\
D([h,y])&=0=[D(h),y]+[h,D(y)],\\
D([x,y])&=0=[D(x),y]+[x,D(y)].
\end{aligned}
\]

Diagonal pairs also satisfy the identity, and bilinearity then proves it for every pair of elements. For \(z=ah+bx+cy\),

\[
\operatorname{ad}(z)(h)=bx+cy,\quad
\operatorname{ad}(z)(x)=ax,\quad
\operatorname{ad}(z)(y)=ay.
\]

Every inner derivation therefore has scalar restriction to \(V\). Our \(D|_V=\operatorname{diag}(1,0)\) is not scalar over any field, so \(D\) is not inner. Since degree-one cocycles are derivations and degree-one coboundaries are inner derivations, \([D]\ne0\) in \(H^1(\mathfrak g,\mathfrak g)\).

## Complete dimension calculation

Write an arbitrary linear map as

\[
\begin{aligned}
D(h)&=ah+bx+cy,\\
D(x)&=dh+ex+fy,\\
D(y)&=rh+sx+ty.
\end{aligned}
\]

Applying the derivation identity to \([h,x]=x\) forces \(d=0\) and \(a=0\). Applying it to \([h,y]=y\) forces \(r=0\); the identity for \([x,y]=0\) then holds automatically. Thus \(b,c,e,f,s,t\) are arbitrary: a derivation consists of an arbitrary value \(D(h)\in V\) and an arbitrary endomorphism \(D|_V\in\operatorname{End}(V)\). This gives dimension \(2+4=6\).

The displayed formula for \(\operatorname{ad}(z)\) has three independent parameters. Equivalently, \(Z(\mathfrak g)=0\): commuting with \(x\) forces the coefficient of \(h\) to vanish, and then commuting with \(h\) forces the coefficients of \(x,y\) to vanish. Therefore

\[
H^0(\mathfrak g,\mathfrak g)=0,\qquad
H^1(\mathfrak g,\mathfrak g)\simeq
\operatorname{End}_k(V)/(k\operatorname{Id}_V)
\]

as vector spaces. The latter has dimension three. The quotient statement is obtained by restricting derivations to \(V\): its two-dimensional kernel is exactly \(\operatorname{ad}(V)\), and the remaining inner derivations restrict to scalars.

## Independent finite check

`check_pgl2_char2.py` represents each element of \(\mathfrak g(\mathbb F_2)\) by a genuine two-by-two matrix with lower-right entry zero. It computes commutators by matrix multiplication and reduces modulo scalar matrices, rather than using the simplified bracket formula in the proof. It checks alternation on all eight elements and Jacobi on all 512 triples, enumerates all 512 linear endomorphisms, checks the derivation identity on all 64 ordered pairs for each endomorphism, and enumerates all eight possible inner derivations.

The saved result is `check_pgl2_char2_result.json`:

| Quantity | Result |
|---|---:|
| Linear endomorphisms examined | 512 |
| Derivations over \(\mathbb F_2\) | 64 |
| Dimension of derivation space | 6 |
| Distinct inner derivations | 8 |
| Dimension of inner-derivation space | 3 |
| Dimension of \(H^1\) | 3 |
| Proposed \(D\) a derivation | true |
| Proposed \(D\) inner | false |

The finite computation checks the example over \(\mathbb F_2\); the symbolic argument, not the finite enumeration alone, establishes the result over every characteristic-two field.

## Exact relation to the frozen scans

All locators refer to the unmodified page files under `MPL_45_033-080/pages/`.

- **C45:040 final paragraph/display**, `MPL_45_033-080_45_scan040.tex`: the written question assumes semisimple adjoint \(G\) and asks whether both \(H^*(G,\mathfrak g)\) and \(H^*(\mathfrak g,\mathfrak g)\) vanish, with no characteristic restriction written there. The example disproves the unrestricted Lie-side assertion already in degree one; this is an answer to the mathematical question under that unrestricted reading, not a correction of its text.
- **C45:042 final bracket display**, `MPL_45_033-080_45_scan042.tex`: the frozen reading is \([H',X]=X\), \([H',Y]=-Y\), \([X,Y]=0\), below an uncertain `SPL(2,k)|PGL(2,k)` heading. In characteristic two these are exactly the brackets used here. This mathematical agreement is relevant context, but is not independent paleographic evidence and must not be used to resolve the uncertain group name or alter the frozen transcription.
- **C45:038 numbered conditions**, `MPL_45_033-080_45_scan038.tex`: the claims successively assume \(H^0=0\), then \(H^1=0\), and then \(H^2=0\). Here \(H^0=0\) holds but \(H^1\ne0\), so the joint hypotheses fail. The example therefore does not contradict the conditional reconstruction/smoothness statements; no claim about the value of \(H^2\) is needed or made.

## Four-sentence candidate note

**C45:040, final question — counterexample to unrestricted Lie-side vanishing (own calculation; confidence high).** Over a field of characteristic two, the semisimple adjoint group \(G=\mathrm{PGL}_2\) has Lie algebra with basis \(h,x,y\) and brackets \([h,x]=x,[h,y]=y,[x,y]=0\). The map \(D(h)=0,D(x)=x,D(y)=0\) is a derivation but not inner, since every inner derivation scales both \(x\) and \(y\) by the same scalar; indeed \(\dim H^1(\mathfrak g,\mathfrak g)=6-3=3\). This answers the unrestricted Lie-side question negatively without deciding the group-cohomology side or resolving the uncertain heading in the matching final bracket display on C45:042. It does not contradict C45:038, whose hypothesis \(H^1(\mathfrak g,\mathfrak g)=0\) fails here.

## Verification boundary

No manuscript images were inspected. No frozen transcription or combined TeX was modified. The cited public sources were opened and searched only to confirm the standard PGL identification; all derivation/cohomology claims in this memo were independently calculated.
