# Complete independent audit: all signed congruence quotients

Saved after the explicit checkpoint32 writer release on 2026-11-17. This
materializes DE's complete conversation-only audit. No earlier saved
file or numerical execution is claimed, and all32 bytes are retained.

## Inputs and scope

Use the actual full-GT negative involution, its canonical word
\(u\in\widehat F(x,y)'\), duality \(u(y,x)=u(x,y)^{-1}\), and the
actual even dihedral exponent \(k\in2\widehat{\mathbb Z}\). Put
\[
 d=1+2k,\qquad
 H_d=u(x,y)x^k u(z,x)z^k u(y,z)y^k,\quad z=(xy)^{-1}.
\]
The entire actual affine-pentagon argument, independently reviewed in
work_DE/review_actual_affine_pentagon_recovered32.md, proves that for
every \(m\ge1\), with the ORIGINAL signed matrices
\[
 X=\begin{pmatrix}1&2\\0&1\end{pmatrix},\quad
 Y=\begin{pmatrix}1&0\\-2&1\end{pmatrix},\quad U=u(X,Y),
\]
one has \(dU_{11}=1\) over \(\mathbb Z/m\). This input was proved
from the whole marked pentagon, not from the desired hexagon.

We prove that the actual \(H_d\) lies in the kernel of the marked
map \(\widehat F(x,y)\to\mathrm{SL}_2(\widehat{\mathbb Z})\).
Neither this kernel nor the word is asserted to be trivial.

## 1. Integral cyclic matrix and signs

Write
\[
 J=\begin{pmatrix}0&-1\\1&-1\end{pmatrix},\qquad
 J^{-1}=J^2=\begin{pmatrix}-1&1\\-1&0\end{pmatrix}.
\]
Then \(J^3=I\), and for
\[
 Z=(XY)^{-1}=\begin{pmatrix}1&-2\\2&-3\end{pmatrix}
\]
direct integral multiplication gives
\[
 JXJ^{-1}=Y,\qquad JYJ^{-1}=-Z,\qquad J(-Z)J^{-1}=X.
\]
These hold over EVERY \(\mathbb Z/m\). The notation is deliberate:
\(J\) is integral, whereas only modulo three do we have
\[
 C=J\bmod3=XYX^{-1}\bmod3.
\]
The integral word \(XYX^{-1}\) is not \(J\).

Let \(q_m\) be the actual marked representation. Multiplying either
argument by a central sign twists it by a character of the free
abelianization, which vanishes on \(u\in\widehat F'\). Thus
\[
 u(Y,Z)=JUJ^{-1},\qquad u(Z,X)=J^{-1}UJ.
\]
Actual evenness gives \((-Z)^k=Z^k\), hence
\[
 Y^k=JX^kJ^{-1},\qquad Z^k=J^{-1}X^kJ.
\]
These are continuous profinite powers. No integer representative
of \(k\), or membership of \(J\) in the source image, is needed.

## 2. The printed factor order gives a cube

Put \(B=UX^k\). In the ORIGINAL order,
\[
\begin{aligned}
 q_m(H_d)&=B(J^{-1}BJ)(JBJ^{-1})\\
 &=BJ^{-1}BJ^2BJ^{-1}=(BJ^{-1})^3,
\end{aligned}
\]
because \(J^2=J^{-1}\). This is exactly
\((UX^kJ^{-1})^3\), not a reordered or merely conjugate product.

## 3. Trace over every coefficient ring

Let \(S=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\).
It interchanges \(X,Y\), so duality gives \(SUS^{-1}=U^{-1}\).
The determinant-one inverse formula over any commutative ring gives
\[
 U=\begin{pmatrix}a&b\\b&e\end{pmatrix},\qquad da=1.
\]
The integer identity \(X^n=I+2nE_{12}\) extends continuously to
the actual \(k\). Therefore
\[
 X^kJ^{-1}=\begin{pmatrix}-d&1\\-1&0\end{pmatrix},\quad
 G:=UX^kJ^{-1}=
 \begin{pmatrix}-da-b&a\\-db-e&b\end{pmatrix}.
\]
Thus \({\rm tr}(G)=-1\) and \(\det(G)=1\). Cayley--Hamilton gives
\[
 G^2+G+I=0,\qquad G^3=I
\]
over EVERY \(\mathbb Z/m\). No division by two or three, field
hypothesis, or reduced-ring hypothesis occurs. All even moduli and
all prime powers are included. Consequently \(q_m(H_d)=I\) for
every \(m\ge1\).

## 4. Exact conclusion and limits

Compatibility of the original integral representations gives
\[
 H_d\in\bigcap_{m\ge1}\ker q_m
 =\ker\bigl(\widehat F(x,y)\longrightarrow
                    \mathrm{SL}_2(\widehat{\mathbb Z})\bigr).
\]
This is the full SIGNED congruence kernel of the specified map,
even though its image need not be the whole matrix group. It
strengthens the modulus-twelve result. It proves neither
\(H_d=1\) in the original free profinite group nor vanishing of
the original CM frame character.

DE independently checked every integral matrix identity, the exact
cyclic product order, central-character cancellation, and profinite
power step. Root and A independently obtained the same calculation.
No execution or finite group census is claimed.
