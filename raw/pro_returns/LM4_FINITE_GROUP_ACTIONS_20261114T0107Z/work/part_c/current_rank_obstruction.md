# Exact cubic torus rank obstruction after D.54–D.55

This note records the established groups, maps and remaining equation. It makes no existence claim for a scalar cubic action and no identification of the sibling group with a full free profinite group.

## 1. Actual groups and characters

Let \(F=\widehat F(x,y)\), \(c=[x,y]\), and let \(a\) be an order-three element of the full punctured-torus loop-outer group. D.27 supplies an actual order-three representative \(\alpha\), so its centre-free extension has the exact presentation

\[
E=F\rtimes_\alpha\langle s\rangle
 =\langle x,y,s\mid s^3=1,\ sxs^{-1}=\alpha(x),\
 sys^{-1}=\alpha(y)\rangle.
\]

The displayed right-hand sides are the actual profinite words of \(\alpha\). Let \(u:E\to\mathbb F_3\) send \(F\) to zero and \(s\) to one. D.48 gives two \(F\)-conjugacy classes of labelled order-three sections, \(S_0=\langle s\rangle\) and \(S_1\), with

\[
H^1(C_F(S_i),\mathbb F_3)=0,\qquad
N_E(S_i)=C_F(S_i)\times S_i .
\]

Choose the invariant character \(\chi:F\to\mathbb F_3\) of D.51, extend it by \(\chi(s)=0\), and rescale it so that the generator of \(S_1\) labelled by \(u=1\) has \(\chi=1\). Rescaling means replacing that character by \(b_1^{-1}\chi\), not changing any group. Then

\[
E^{\mathrm{ab},(3)}=\mathbb F_3^2,\quad
(u,\chi)(S_0)=\langle(1,0)\rangle,\quad
(u,\chi)(S_1)=\langle(1,1)\rangle.
\]

For \(L=\langle c\rangle\cong\widehat{\mathbb Z}\), write
\(N=N_E(L)\). The exact normalizer sequence is

\[
1\longrightarrow L\longrightarrow N\xrightarrow{u}C_3
\longrightarrow1.
\]

Choose \(v\in N\) with \(u(v)=1\). Its actual relations are

\[
vcv^{-1}=c^\lambda,\qquad
v^3=c^\kappa,\qquad
\lambda^3=1,\qquad
(\lambda-1)\kappa=0,\qquad \kappa_3\in\mathbb Z_3^\times .
\]

D.51's Heisenberg cube calculation gives \(\chi(v)=-1\). Thus

\[
U=\ker(\chi+u),\qquad
V=\ker u\cap\ker\chi=F\cap U,
\]

and the inclusions and quotients are exactly

\[
[E:F]=[E:U]=3,\quad [F:V]=[U:V]=3,\quad
E/V=C_3^2,\quad E=U\rtimes S_0 .
\]

The two normal index-three subgroups \(F,U\) are precisely the torsion-free ones. The other two contain the two section classes. In particular \(N\subset U\). The inclusion \(V\hookrightarrow F\) is the completion of the actual degree-three unramified punctured-torus cover associated to \(\chi\).

## 2. The full cover and the three normalizers

The cover has three degree-one boundary lifts, Euler characteristic \(-3\), and type \((1,3)\). Hence

\[
V\cong\widehat{\pi_1(S_{1,3})}\cong\widehat F_4.
\]

Choose a word \(f\) in the original dense discrete group with \(\chi(f)=1\). Set

\[
c_i=f^icf^{-i},\quad L_i=\langle c_i\rangle,\quad
v_i=f^ivf^{-i},\quad N_i=f^iNf^{-i}\quad(0\leq i<3).
\]

These are actual subgroups of \(E\), and \(N_i=N_E(L_i)=N_U(L_i)\). The exact maps are

\[
1\longrightarrow L_i\longrightarrow N_i
\xrightarrow{u}U/V\cong C_3\longrightarrow1,
\quad
N_i\cap V=L_i,
\]

with \(u(v_i)=1\),
\(v_i c_i v_i^{-1}=c_i^\lambda\), and \(v_i^3=c_i^\kappa\).
The three \(L_i\), and therefore the three \(N_i\), are pairwise nonconjugate under \(U\). The quotient \(E/U\) cyclically permutes their classes. This follows from the three cosets of \(U/V\) in the exact quotient \(E/V\); it does not rely on a proposed graph decomposition of \(U\).

For an optional explicit discrete Schreier basis, first choose an orientation-preserving discrete Nielsen change with \(\chi(x)=1,\chi(y)=0\), carrying the cusp and its chosen normalizer by that same isomorphism. Then

\[
A=x^3,\quad B_0=y,\quad B_1=xyx^{-1},\quad
B_2=x^2yx^{-2}
\]

freely generate \(V\). The three representatives are

\[
c_0=B_1B_0^{-1},\quad
c_1=B_2B_1^{-1},\quad
c_2=AB_0A^{-1}B_2^{-1}.
\]

Their three homology classes have the sole relation
\([c_0]+[c_1]+[c_2]=0\). No product relation among the three roots \(v_i\) follows from this homology relation.

The full group \(U\) is projective: it is torsion-free and has the open full free subgroup \(V\). An exact presentation is obtained by adjoining \(v\) to a free basis \(z_1,\ldots,z_4\) of \(V\):

\[
U=\langle z_1,\ldots,z_4,v\mid
v z_j v^{-1}=\beta(z_j)\ (1\leq j\leq4),\
v^3=c^\kappa\rangle,
\qquad \beta=\operatorname{Inn}(v)|_V .
\]

Here \(\beta^3=\operatorname{Inn}(c^\kappa)\) and
\(\beta(c^\kappa)=c^\kappa\), as follows inside the given \(U\). The natural map of this presentation to \(U\) is an isomorphism: its relations reduce each coset to \(Vv^i\), \(0\leq i<3\), and the inverse is the twisted extension multiplication on these three copies of \(V\). This is a presentation with five generators and five profinite-word relations; no minimal full generating number is established. In particular it is not a presentation of a two-generator free group.

## 3. Established primary and cross-prime maps

The pro-three topology on \(V\) is the one induced from \(U\): intersect the three \(U/V\)-conjugates of each open normal subgroup of three-power index in \(V\). Consequently

\[
V^{(3)}\hookrightarrow U^{(3)},\quad
[U^{(3)}:V^{(3)}]=3,\quad
V^{(3)}=\widehat F^{(3)}_4,\quad
U^{(3)}=\widehat F^{(3)}_2.
\]

The last equality follows from projectivity and pro-three Schreier rank. This argument proves an embedding at the prime three only.

Now let \(q\ne3\) with \(\lambda_q\ne1\). Necessarily \(q\equiv1\pmod3\). D.54 excludes the eigenvalue pattern \(\{1,\lambda_q\}\), leaving

\[
A_q=\lambda_q^2 I,\qquad
H_1(V,\mathbb Q_q)
 =\lambda_q^{\oplus2}\oplus(\lambda_q^2)^{\oplus2}
\quad\text{as a labelled }U/V\text{-module}.
\]

The first summand is the actual boundary augmentation module; the second is the compact-cover homology, identified with base homology by the degree-three covering map. At \(q\ne3\), averaging and the unit differences of the cube roots give the same splitting integrally. Thus

\[
H^1(U,\mathbb F_q)=0,\qquad U^{(q)}=1.
\]

In contrast \(V^{(q)}\) is free pro-\(q\) of rank four. The induced map \(V^{(q)}\to U^{(q)}\) is therefore the zero map. No embedding or pro-\(q\) Schreier comparison is available here. The earlier rank-one alternative in D.51 is removed by D.54.

At a prime \(\ell\ne3\) with \(\lambda_\ell=1\), D.54 and finite-order semisimplicity give the eigenvalues \(\zeta_3,\zeta_3^{-1}\) over a splitting field on base homology and two trivial boundary characters. Hence \(H^1(U,\mathbb F_\ell)\) has dimension two and \(U^{(\ell)}\) is free pro-\(\ell\) of rank two. This does not supply a full free presentation.

Each \(N_i\) is torsion-free. At a bad prime \(q\), its maximal pro-\(q\) quotient is trivial. In such a quotient \(c_i^\kappa=1\), since \(\kappa_q=0\); hence \(v_i^3=1\) forces \(v_i=1\), and \(c_i^{\lambda_q-1}=1\) then forces \(c_i=1\). Its maximal pro-three quotient is \(\mathbb Z_3\), with \(L_i^{(3)}\) mapping as its index-three subgroup; the unit \(\kappa_3\) proves this. Thus ordinary mod-\(q\) first cohomology does not distinguish the three bad normalizers.

## 4. The precise missing incidence equation

Use the three representatives obtained by conjugating \(N\) with \(s\), rather than \(f\); these give the same three classes because \(s\) generates \(E/U\). Put

\[
\widetilde v_i=s^ivs^{-i}\quad(0\leq i<3).
\]

The exact group identity is

\[
\widetilde v_0\widetilde v_1\widetilde v_2=(vs)^3.
\]

The element \(vs\) has abelian coordinates \((2,-1)=(2,2)\), on the second section line. It is not established that \(vs\) has order three, nor that some permitted \(v\in N\), after a full change of section representative, makes it have order three. Equivalently, the required full section class has not been shown to meet the specified coset \(Ns\) with its label. Passing to the abelian quotient gives only the line, not the incidence. Even an incidence solution would still require an explicit generation proof for the resulting proposed presentation.

The structural question under examination is whether the actual free rank-four cover \(V\), together with these three pairwise nonconjugate virtually procyclic normalizers and their shared label, forces this incidence or excludes the bad-prime homology pattern. No full-profinite tree action or free-product decomposition has been proved from these data.

## 5. Correct section count in the scalar Heisenberg cover

Let \(Q=H_q\) be the characteristic class-two exponent-\(q\) quotient of \(F\), of order \(q^3\), and \(K=\ker(F\to Q)\). The induced order-three action is

\[
\theta(r,z)=(\lambda_q^2r,\lambda_qz+\ell(r)).
\]

It has no nonidentity fixed element. Let
\(\rho:E\to Q\rtimes_\theta\langle\bar s\rangle\) be the actual quotient map, and let
\(E_K=\rho^{-1}(\langle\bar s\rangle)=K\rtimes\langle s\rangle\).

Every section image is \(Q\)-conjugate to \(\langle\bar s\rangle\). One can see this directly: \(a\mapsto a^{-1}\theta(a)\) is injective because equality makes the corresponding quotient of two inputs \(\theta\)-fixed; it is surjective by finiteness. Its images are precisely the corrections of the complement generator. Thus both global section classes have representatives \(T_i\) in \(E_K\) mapping onto the specified complement.

For \(g\in F\), the conjugate \(gT_i g^{-1}\) lies in \(E_K\) exactly when
\(\rho(g)\) normalizes \(\langle\bar s\rangle\). In the \(Q\)-part that normalizer is

\[
N_Q(\langle\bar s\rangle)=C_Q(\theta)=1,
\]

since conjugation by a \(Q\)-element preserves the quotient generator label. Therefore this condition is exactly \(g\in K\). There is one \(K\)-class above each global \(F\)-class, not \(q^3\) classes. Also
\(C_F(T_i)\subset K\), by the same fixed-point calculation, so the two centralizers retain their zero mod-three first cohomology. Passing from \(F\)- to \(E\)-conjugacy introduces no further fusion because the section itself supplies the required quotient label.

The original two full section classes therefore remain exactly two in \(E_K\). The independent characteristic-zero homology trace is \(-1\): all nontrivial deck isotypic summands lie in three-cycles under the scalar action, while the deck-invariant summand is the two-dimensional base torus module. The \(q^2\) cusp labels have one fixed point and free triples, so their boundary augmentation has trace zero; filling the cusps retains trace \(-1\). These counts are consistent and do not yield a scalar-branch contradiction.

Further details of the character calculations are retained in work/part_c/d51_incidence_audit.txt; the established finite identities were executed in work/part_c/code/torus_order3_sibling_d51.py.
