# The actual order-three factor transporter in the first central quotient

Checkpoint34, first saved proof of the complete read-only argument from checkpoint33. All checkpoint33 files remain unchanged. This is an existence theorem for a specified actual quotient frame. It does not select the original full-group frame or resolve the CM sign.

## 1. Retained objects and the exact claim

Use the actual full-GT data of A103–A104 and the two fully reviewed checkpoint33 central proofs. Thus
\[
F=\widehat F(x,y),\quad B=C_2(s)\amalg C_3(r),\quad
\delta=sr,\quad x=\delta^{-2},\ y=sxs,\ z=(xy)^{-1}.
\]
The actual canonical word is \(u\in F'\), \(u=\phi\alpha(u)\); its dihedral exponent is \(k\in2\widehat{\mathbb Z}\), and \(d=1+2k\) is a full unit. Write
\[
q(x)=X=\begin{pmatrix}1&2\\0&1\end{pmatrix},\quad
q(y)=Y=\begin{pmatrix}1&0\\-2&1\end{pmatrix},\quad
U=q(u)=\begin{pmatrix}d^{-1}&b\\b&d(1+b^2)\end{pmatrix},
\quad H=\begin{pmatrix}1&-b\\0&d^{-1}\end{pmatrix}.
\]
Let \(C=q(F)\), \(N=\ker q\), \(N_1=\overline{[N,F]}\),
\(E_1=F/N_1\), \(B_1=B/N_1\). The preceding proofs give the actual automorphism
\[
\Psi_1(s)=v=u^{-1}s,\qquad \Psi_1(\delta)=\delta^d,
\qquad \Psi_1(r)=u^{-1}y^{-k}r.                     \tag{1}
\]

Let \(e\in\{1,-1\}\) be the integer representing \(d\bmod3\), and set
\[
\epsilon=(1-e)/2,\quad R_e=y^\epsilon r,\quad
t=(k+\epsilon)/3\in\widehat{\mathbb Z}.
\]
For \(\epsilon=1\), \(R_e=sr^{-1}s\). Hence \(R_e^3=1\) and its \(S_3\)-image is \(r\) in either branch. The displayed \(t\) exists because \(d=1+2k\): if \(e=1\), \(k\equiv0\bmod3\), and if \(e=-1\), \(k\equiv2\bmod3\).

We prove that there exists an actual \(h\in E_1\) such that
\[
\boxed{\Psi_1(r)=hR_eh^{-1},\qquad h_{\rm ab}=(t,-t).} \tag{2}
\]
In the negative branch \(hs\) conjugates \(r^{-1}\) to \(\Psi_1(r)\); it has the required transposition image. A pure conjugator directly to \(r^{-1}\) would have the wrong \(S_3\)-image.

## 2. The actual central pro-two kernel

Write \(C_{(2)}\) for the actual closed two-adic image, \(\pi_2:F\to F^{(2)}\), and
\[
M_2=\ker(F^{(2)}\to C_{(2)}),\qquad
M_{2,1}=\overline{[M_2,F^{(2)}]}.
\]
The exact central-coordinate theorem says
\[
N_1=N\cap F'\cap\pi_2^{-1}(M_{2,1}).                \tag{3}
\]
It follows that
\[
1\longrightarrow K\longrightarrow E_1'
 \xrightarrow{q}C'\longrightarrow1,\qquad
K=(N\cap F')/N_1                                  \tag{4}
\]
is an actual central pro-two extension. Surjectivity uses the equality \(q(F')=C'\), valid for continuous surjections of compact groups. Centrality follows from the definition of \(N_1\). On \(K\), (3) makes the induced map into \(M_2/M_{2,1}\) injective. This latter compact group is pro-two; hence so is \(K\). No surjectivity of \(N\to M_2\) is assumed.

We shall use the elementary fact that a continuous action of \(C_3\) on any pro-two group has trivial nonabelian \(H^1\). For a finite two-group \(P\), induct on its order. The nonzero characteristic elementary abelian central subgroup \(\Omega_1(Z(P))\) is action-stable. Kill the projected cocycle by induction, leaving a cocycle \(z\) in this central subgroup. In additive notation its norm is zero. Since three is invertible, the identity
\[
(\rho-1)(\rho+2\rho^2)=3-(1+\rho+\rho^2)
\]
writes \(z\) as a coboundary. For a pro-two group, intersect the three translates of open normal subgroups to obtain cofinal action-stable finite quotients. The compact sets of possible correcting conjugators have the finite-intersection property. This proves the continuous assertion without finite-generation assumptions.

In particular, if a cocycle of \(E_1'\) projects to a coboundary in \(C'\), it is a coboundary in \(E_1'\): lift a correcting conjugator, leaving a cocycle in \(K\), then use the preceding fact. No \(H^2\) comparison is needed for this direction.

## 3. Abelian normalization and the signed residual matrix

Put \(\rho=\operatorname{Ad}(r)|_F\) and \(\rho_e=\operatorname{Ad}(R_e)|_{E_1}\). Write
\[
\Psi_1(r)=a_eR_e,\qquad a_e=u^{-1}y^{-(k+\epsilon)}.
\]
Since both sides of (1) and \(R_e\) have order dividing three, \(a_e\) is an actual \(C_3\)-cocycle for \(\rho_e\).

On the original abelianization,
\[
\rho=\begin{pmatrix}0&-1\\1&-1\end{pmatrix}.
\]
Choose \(h_0=x^t y^{-t}\in F\), viewed in \(E_1\). Its abelianization is \((t,-t)\), and
\[
(1-\rho)(t,-t)=(0,-3t)=(0,-k-\epsilon).
\]
Therefore
\[
z_e=h_0^{-1}a_e\rho_e(h_0)\in E_1'                 \tag{5}
\]
is a genuine cocycle.

Use the original integral cyclic matrix
\[
J=R_0=\begin{pmatrix}0&-1\\1&-1\end{pmatrix},
\quad J^3=I,\quad
q(\rho(g))=Jq(g)J^{-1}(-I)^{\operatorname{exp}_y(g)}. \tag{6}
\]
The signed representation is not being extended to all of \(B\). Instead put
\[
D_e=\operatorname{diag}(1,e),\qquad
J_e=(-1)^\epsilon Y^\epsilon J=D_eJD_e^{-1}.         \tag{7}
\]
Both cases are literal integral identities. In particular \((YJ)^3=-I\), while \(J_e^3=I\). On \(E_1'\) the sign character in (6) vanishes, so \(q\rho_e=\operatorname{Ad}(J_e)q\).

Let \(Q=q(h_0)\). Equation (6), with \(\operatorname{exp}_y(h_0)=-t\), yields the ordered identity
\[
q(z_e)J_e=(-1)^{\epsilon-t}Q^{-1}U^{-1}Y^{-k}JQ.    \tag{8}
\]
Here \(3t=k+\epsilon\) and \(k\) is even; hence \(t\equiv\epsilon\bmod2\), so the sign is one. Direct multiplication using the entire A103 matrix gives
\[
U^{-1}Y^{-k}J=
 \begin{pmatrix}-b&d(b-1-b^2)\\d^{-1}&b-1\end{pmatrix}
 =H JH^{-1}.                                      \tag{9}
\]
Combining (7)--(9), with
\[
B_e=Q^{-1}HD_e^{-1},
\]
gives
\[
q(z_e)J_e=B_eJ_eB_e^{-1},\qquad
\det B_e=e\,d^{-1}.                               \tag{10}
\]
In particular its determinant is one modulo three. The parity cancellation in (8) is essential.

## 4. Correcting the determinant at every odd prime

Fix an odd prime \(p\). We adjust \(B_{e,p}\) on the right by an element commuting with \(J_e\), whose determinant is \((\det B_{e,p})^{-1}\).

For \(p\ne3\), the algebra \(\mathbb Z_p[J_e]\) is the quadratic algebra defined by \(T^2+T+1\). Its discriminant is the unit \(-3\). If the polynomial splits modulo \(p\), its two distinct roots lift, and the algebra is \(\mathbb Z_p\times\mathbb Z_p\); its determinant norm is the product, which is onto units. If it is irreducible modulo \(p\), its residue field is \(\mathbb F_{p^2}\). That field's norm onto \(\mathbb F_p^\times\) is surjective, as follows from the cyclic multiplicative groups and the exponent \(p+1\). Lift a residue unit giving the desired determinant modulo \(p\). The remaining determinant ratio is in \(1+p\mathbb Z_p\), and is the square of a scalar unit. This follows by successive lifting of the square-root equation, since its derivative is a unit for odd \(p\). A scalar correction belongs to the same centralizer.

At \(p=3\), (10) makes the desired determinant ratio an element of \(1+3\mathbb Z_3\). A scalar square root alone corrects it. Thus no ramified norm theorem is invoked or needed.

We obtain \(G_p\in{\rm SL}_2(\mathbb Z_p)\) with
\[
q_p(z_e)J_e=G_pJ_eG_p^{-1}.                        \tag{11}
\]

## 5. Placing the conjugators in the actual derived image

The actual image decomposes as
\[
C=C_{(2)}\times\prod_{p\ {\rm odd}}{\rm SL}_2(\mathbb Z_p),
\]
and its closed derived subgroup is the product of the closed derived subgroups. Beyl's Proposition5.7(a) gives
\[
{\rm SL}_2(\mathbb Z_p)_{\rm ab}=1\ (p\ge5),
\qquad {\rm SL}_2(\mathbb Z_3)_{\rm ab}=C_3.
\]
These statements follow from its character computation by continuous character separation. Thus \(G_p\) already belongs to the derived subgroup for \(p\ge5\).

At three, the abelianization is the original character \(\chi\) obtained by reduction modulo three, with \(\chi(X)=\chi(Y)=1\). The original \(J\bmod3=XYX^{-1}\) has character one, and \(\chi(-I)=0\). Equation (7) gives
\[
\chi(J_e)=1+\epsilon=e\quad\text{in }\mathbb F_3.
\]
Multiplying \(G_3\) on the right by a suitable power of \(J_e\) makes its character zero, while preserving (11). Hence all odd-prime conjugators can be chosen in the actual derived factors.

At two, the genuine projected cocycle \(q_2(z_e)\) lies in the pro-two group \(C_{(2)}'\) with its actual order-three action. The elementary coprime result of §2 supplies a conjugator there. Taking the product gives \(G\in C'\) such that
\[
q(z_e)=G\,\rho_e(G)^{-1}.                          \tag{12}
\]
No assertion that the two-adic factor is all of \({\rm SL}_2(\mathbb Z_2)\) has been made.

Lift \(G\) to \(g\in E_1'\) in (4). Then \(g^{-1}z_e\rho_e(g)\) is a cocycle in the central pro-two \(K\), so is a coboundary. Consequently \(z_e=j\rho_e(j)^{-1}\) for some \(j\in E_1'\). Equation (5) now gives
\[
a_e=(h_0j)\rho_e(h_0j)^{-1}.
\]
Taking \(h=h_0j\) proves (2), including its exact abelianization.

## 6. Sources and remaining scope

The exact central model and actual \(\Psi_1\) are the unchanged checkpoint33 proofs at hashes dae57e05 and38151d4a. The original six marked maps and ordered cubic identity were bound there to A87.9–12. The signed matrix and normalizer are the complete A103–A104. The only additional external use here is part(a) of the same Beyl Proposition5.7 whose complete statement and proof were already freshly read: printed page41, GDZ OCR XML,
https://gdz.sub.uni-goettingen.de/fulltext/PPN266833020_0191/00000049?_format=xml .

The elementary determinant correction has been proved in §4; no target census or unrecorded finite execution is used. This is the first saved byte version of the complete conversation-level proof. Independent complete saved-source review is requested.

The transporter is not asserted unique. The actual quotient has extra order-three centralizers, so an unframed E65 character cannot simply be imported from the full free profinite group. No original full frame, actual CM sign, full automorphism of \(B\), full \(H_d=1\), or further relative lifting conclusion follows from this theorem.

