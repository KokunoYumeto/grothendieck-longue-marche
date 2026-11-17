# The uniform affine pentagon, all signed congruence heads, and the exact kernel gate

New checkpoint33 proof, saved after the observed checkpoint32 capture exit. Sections 1–4 retain the complete uniform affine argument from the unchanged checkpoint32 research source SHA 9bcb84e25041c47d7b0b97be37a56db0c654251a7c74cc585c10e364c87ae48c. Sections 5–7 supply the full integral cyclic calculation, the actual congruence automorphism, and a direct original-alpha descent and conjugacy argument. No source from checkpoint32 is altered. This is a symbolic proof, not a finite target search or an execution certificate.

## 1. Exact hypotheses and theorem

Let F be the free profinite group on x,y, and let u belong to its closed commutator subgroup. Assume the full word duality

\[
u(y,x)=u(x,y)^{-1}
\]

and the original marked sphere pentagon

\[
u(a,ce)u(bc,f)=u(c,f)u(ab,ef)u(a,c)                 \tag{1}
\]

in the completion of G=P4/<Delta4²>, with
(a,b,c,d,e,f)=(A12,A13,A23,A14,A24,A34). For an actual canonical u of a full-GT involution, the full profinite pentagon for this very word is the proved A37 theorem. No norm equation is required in the argument below. A general GT0 canonical word is not supplied with this extra pentagon.

In D=Zhat_T semidirect C2(s), use the original map x->s,y->sT, so xy->T. Define the unique k by u(s,sT)=T^k. The closed derived subgroup of D is 2Zhat_T, hence k is even. Put d=1+2k, z=(xy)^-1, and retain the ordered word

\[
H_d=u(x,y)x^k u(z,x)z^k u(y,z)y^k.                \tag{2}
\]

For every positive integer m, use the original signed matrices

\[
X_m=\begin{pmatrix}1&2\\0&1\end{pmatrix},\qquad
Y_m=\begin{pmatrix}1&0\\-2&1\end{pmatrix}
\]

over R=Z/m, and put U_m=u(X_m,Y_m). The uniform conclusion is

\[
d(U_m)_{11}=1\quad\text{in }R.                    \tag{3}
\]

Consequently d is a full profinite unit, and in the inverse-limit signed representation

\[
U=u(X,Y)=
\begin{pmatrix}d^{-1}&b\\b&d(1+b^2)\end{pmatrix}
\quad\text{for the actual }b=U_{12}\in\widehat{\mathbb Z}. \tag{4}
\]

In fact q(H_d)=I in the full original signed congruence representation to SL2(Zhat), and hence in every finite modulus. Section 5 proves this with a single integral order-three matrix. This remains a quotient value of the original word (2), not H_d=1 in F; no separately normalized CM character is identified by that quotient equality alone.

## 2. The exact original source presentation

The reversible A96 presentation is

\[
G=F(P,A,C)\rtimes F(d_0,f_0),
\]

where the subscript distinguishes the braid generators from the scalar d. Positive base actions are

\[
\begin{array}{c|ccc}
 &P&A&C\\\hline
d_0&C^{-1}PC&C^{-1}P^{-1}CPA&C\\
f_0&A^{-1}PA&A&CPA^{-1}P^{-1}A.
\end{array}                                                   \tag{5}
\]

The original words are

\[
a=Af_0,\quad c=Cd_0,\quad
b=a^{-1}P^{-1}c^{-1},\quad e=d_0^{-1}Pf_0^{-1}.       \tag{6}
\]

For clarity, (5) is reversibly equivalent to

\[
[A,f_0]=[C,d_0]=[Af_0,P]=[Cd_0,P]
=[PA,d_0]=[CP,f_0]=1.                               \tag{7}
\]

The first two relations fix A under f0 and C under d0. The next two give their P-actions. The last two then solve for d0(A) and f0(C) exactly as in (5). Thus checking (7) checks all six original relations. P is the original unrestricted generator; no root extension, boundary deletion, relative-pro-two quotient, or four-square filling is used here.

## 3. One uniform affine construction over every Z/m

Write v=e1,w=e2 in V=R² and use affine multiplication

\[
(t,M)(s,N)=(t+Ms,MN)
\]

in Q=V semidirect SL2(R). Assign

\[
P=(0,-I),\quad A=(-2v,I),\quad C=(-2w,I),\quad
f_0=(2v,X),\quad d_0=(2w,Y).                         \tag{8}
\]

All six relations hold over every R, including even and nonreduced rings. Indeed Xv=v and Yw=w give the first two. The images a=(0,X) and c=(0,Y) commute with P. The fifth relation holds because PA=(2v,-I) and

\[
(I-Y)(2v)=4w.
\]

The sixth holds because CP=(-2w,-I) and

\[
(I-X)(-2w)=4v.
\]

These are exact polynomial identities. There is no cancellation or division by two. The construction therefore gives a homomorphism from the entire actual G, continuously extending to its completion because Q is finite.

From (6), the images of a,c are as above, while

\[
b=(0,-X^{-1}Y^{-1}),\qquad
e=(2v+2w,-Y^{-1}X^{-1}).                             \tag{9}
\]

The five pairs of the original pentagon, in order, are

| Pair | First image | Second image |
|---|---|---|
| (a,ce) | (0,X) | (2(v-w),-X^-1) |
| (bc,f0) | (0,-X^-1) | (2v,X) |
| (c,f0) | (0,Y) | (2v,X) |
| (ab,ef0) | (0,-Y^-1) | (-2w,-Y^-1) |
| (a,c) | (0,X) | (0,Y) |

In particular the exact e-translation is 2v+2w and the exact ef0-translation is -2w; their signs control the conclusion.

## 4. Evaluate all five pairs, retaining their order

In each of the first two pair subgroups, the linear heads commute. A commutator word consequently has linear image I. Those heads preserve the direct summand Rv. On the affine quotient by Rv, the first generator of pair one is the identity, and the second generator of pair two is the identity. Therefore each u-value is a translation in Rv. This quotient is used only for those pair subgroups; Rv need not be invariant under the whole Q. The entire left side of (1) is thus (ell v,I), for some ell in R.

For pair three, put t=-w. The identities

\[
(I-Y)t=0,\qquad (I-X)t=2v
\]

show that it is the simultaneous conjugate of ((0,Y),(0,X)) by (t,I). Duality therefore gives

\[
u(c,f_0)=(t-U^{-1}t,U^{-1}).                         \tag{10}
\]

For pair four, the element h=(0,Y^-1) commutes with both

\[
j_0=(0,-I),\qquad j_1=(-2w,-I),
\]

since Yw=w. The pair is (j0h,j1h). Any profinite commutator word is unchanged by such central decorations: the two total exponent sums are zero. Both j0,j1 are involutions and their ordered product is (2w,I). The universal dihedral definition of k therefore gives

\[
u(ab,ef_0)=(2k w,I).                                \tag{11}
\]

This assertion also covers m=2 and other degenerations; it is a homomorphism from the universal dihedral group, not an assumption that the finite image has a particular exact order.

Finally u(a,c)=(0,U). Multiplying (10), (11), and this last value in their original order yields

\[
(\ell v,I)=(-w+(1+2k)U^{-1}w,I).                    \tag{12}
\]

For any determinant-one two-by-two matrix U over a commutative ring, the second coordinate of U^-1w is U11. The second coordinate of (12) proves (3). Since this holds for every m, d is a unit in every finite quotient and hence a unit of Zhat; the compatible U11 coordinates equal d^-1.

The integral matrix S=[[0,-1],[1,0]] conjugates X to Y and Y to X. Duality gives SUS^-1=U^-1. Comparing the inverse formulas gives U12=U21 over every ring, without division. The determinant condition and (3) then give (4).

The conclusion d unit overlaps the earlier A88/A100 result for actual canonical full-GT data; no novelty claim is made for that overlap. Formula (3) is an exact original congruence-matrix entry, proved directly from the full pentagon rather than by replacing the historical Alexander proof.


## 5. The full integral cycle and every congruence head

Put
\[
R_0=\begin{pmatrix}0&-1\\1&-1\end{pmatrix},\qquad
S_0=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad Z=(XY)^{-1}.
\]
These are integral matrices. Direct multiplication gives R_0^3=I and
Ad(R_0): X -> Y -> -Z -> X. The original cyclic automorphism
rho:(x,y)->(y,z) differs, after q, from Ad(R_0)q by the central sign
character that is +I on x and -I on y. That character is trivial on
F', and rho preserves F'. Therefore
\[
q(u(y,z))=\kappa(U),\qquad q(u(z,x))=\kappa^2(U),
\quad \kappa=\operatorname{Ad}(R_0).
\]
The actual k is even, so (-Z)^k=Z^k. The exact ordered word is
\[
q(H_d)=V\kappa^2(V)\kappa(V)=(UX^kR_0^{-1})^3,
\qquad V=UX^k.
\]
The integral R_0 reduces modulo three to the matrix previously also
written XYX^{-1} in that finite field. That equality is not used
integrally. Here
\[
X^kR_0^{-1}=\begin{pmatrix}-d&1\\-1&0\end{pmatrix}.
\]
The already proved symmetry of U and d U_11=1 give
tr(UX^kR_0^{-1})=-1 in Zhat. Its determinant is one.
Cayley--Hamilton over this commutative ring gives g^2+g+I=0,
hence g^3=I. Thus q(H_d)=I simultaneously at every modulus.
The argument involves neither division by two nor a field-only
cancellation. It includes all prime powers and mixed moduli.

## 6. The actual congruence automorphism and exact remaining kernel

Let C=q(F) be the actual closed image and N=ker(q). No assertion
that C is the entire SL2(Zhat) is required. Define the actual
endomorphism
\[
\psi_d(x)=x^d,\qquad \psi_d(y)=u^{-1}y^du,
\qquad
H=\begin{pmatrix}1&-b\\0&d^{-1}\end{pmatrix}.
\]
Its inverse matrix is H^{-1}=[[1,bd],[0,d]]. Exact multiplication gives
\[
HXH^{-1}=X^d,\qquad
HYH^{-1}=\begin{pmatrix}1+2b&2db^2\\-2d^{-1}&1-2b\end{pmatrix}
=U^{-1}Y^dU.
\]
Consequently q psi_d=Ad(H)q on the entire free profinite group.
For each m, this conjugation maps the actual finite image
C_m=<X_m,Y_m> into itself. It is injective, hence onto by finiteness.
The closed subgroups HCH^{-1} and C have equal projections to every
congruence head, hence are equal. Thus H normalizes C, with inverse
normalizer action Ad(H^{-1}). It is an external GL2 normalizer;
H is not asserted to belong to C.

The equality q psi_d=Ad(H)q gives psi_d^{-1}(N)=N exactly.
Let L=psi_d(F), a compact and therefore closed subgroup.
Because d is a unit,
\[
L=\overline{\langle x,u^{-1}yu\rangle},\qquad q(L)=C.
\]
For every f in F choose l in L with q(l)=q(f); then fl^{-1} is in N.
This proves F=NL. Moreover
\[
L\cap N=\psi_d(\psi_d^{-1}(N))=\psi_d(N).
\]
It follows, in both directions, that
\[
\psi_d(F)=F\quad\Longleftrightarrow\quad\psi_d(N)=N.
\]
There is no finite-generation assumption on N in this argument.
This is an exact reduction to the actual infinite congruence kernel,
not a proof of surjectivity on that kernel.

The normalized map is psi_d=psi_u p_d, where
psi_u(x)=x, psi_u(y)=u^{-1}yu and p_d sends both generators to their
d-th powers. The latter is a genuine automorphism, with inverse
p_(d^{-1}). Hence full surjectivity is exactly the original canonical
image question. Separately, the abelianization of psi_d is d I_2,
so each maximal free pro-p quotient map is an automorphism by the
Frattini criterion. This and the congruence result have DIFFERENT
quotient scopes; neither is asserted to follow logically from the
other. No automorphism of a relative pro-p layer over a nontrivial
congruence head has been proved here.

## 7. Direct descent and quotient conjugacy of the original alpha

Now specialize to actual canonical full-GT data with
alpha(x)=x^{-1}, alpha(y)=phi^{-1}y^{-1}phi and
u=phi alpha(u). Let c_0 invert both free generators and
J_0=diag(1,-1), so q c_0=Ad(J_0)q. The original GT0 two-cycle
for phi gives S_0 Phi S_0^{-1}=Phi^{-1}, where Phi=q(phi).
Thus Phi is symmetric, say [[a,t],[t,e]].

Do not assume alpha preserves N at this stage. Original third
peripheral inversion says that alpha(xy) is conjugate to (xy)^{-1}
in F. Apply q to that actual equality and take traces:
\[
2-4a^2=\operatorname{tr}(X^{-1}\Phi^{-1}Y^{-1}\Phi)
=\operatorname{tr}((XY)^{-1})=-2.
\]
Additive Zhat is torsion-free, hence a^2=1. Therefore a is a unit,
e=a(1+t^2), and
\[
K_\Phi=\begin{pmatrix}1&at\\0&-1\end{pmatrix}
\]
is an involution. Direct generator multiplication gives
\[
K_\Phi X K_\Phi^{-1}=X^{-1},\qquad
K_\Phi Y K_\Phi^{-1}
=\begin{pmatrix}1-2at&-2t^2\\2&1+2at\end{pmatrix}
=\Phi^{-1}Y^{-1}\Phi.
\]
This proves q alpha=Ad(K_Phi)q on all F and hence alpha(N)=N.
The descent itself has used only the original negative peripheral
input and original two-cycle; it has not cancelled psi_d.

Now evaluate the ACTUAL norm. It gives
\[
UK_\Phi=\Phi K_\Phi U,\qquad
\Phi K_\Phi=\begin{pmatrix}a&0\\t&-a\end{pmatrix}.
\]
The (1,1) entries and the established unit U_11=d^{-1} give a=1.
The (1,2) entries then give d^{-1}t-b=b, so t=2bd. Hence
\[
\Phi=Y^{-bd}X^{bd}
=\begin{pmatrix}1&2bd\\2bd&1+4b^2d^2\end{pmatrix},\qquad
K_\Phi=\begin{pmatrix}1&2bd\\0&-1\end{pmatrix}=HJ_0H^{-1}.
\]
Thus the actual alpha and standard inversion are conjugate on the
actual congruence quotient by Ad(H). The original intertwining
alpha psi_d=psi_d c_0 follows directly from the norm, but was NOT
cancelled to establish this quotient descent or conjugacy.

## 8. Exact limits, earlier proofs, and review provenance

The actual full-GT canonical specialization uses the complete A37
pentagon for u; fixed arrows alone are not substituted for it.
The d-unit conclusion overlaps A88/A100, whose original Alexander
proofs remain unchanged. The full-ring A101 cover-module conclusion
also remains unchanged. This new theorem gives q(H_d)=I for the
original signed congruence map, not H_d=1 in F and not Omega_alpha=1.
The remaining original H_d lies in N, and its value there is open.
The full-source image is all F precisely when the actual restriction
psi_d:N->N is onto. No arbitrary congruence-kernel automorphism is
substituted for that restriction.

The complete scaled affine checkpoint32 proof was independently read
by root, CE and DE at its genuine saved hash. The congruence-normalizer
and exact N-surjectivity argument was independently checked by CE in
conversation before release. The new integral-cycle extension and
direct alpha calculation are printed in full here and in proposed
A103/A104 for fresh entire-source review. Current source hashes and
review receipts will be recorded separately; no unreceived review
or mathematical execution is claimed in this paragraph.
