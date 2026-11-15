# A fully explicit split calculation for bridge B12

## B12.1 — The conic, projective line, and rank-four algebra in the actual example

**72/075–077; kind: unpursued implication, proved explicit construction; quote (077): “d'une hyperquadrique \(Q_C\) de \(C\)” and “\((C,Q_C,\varphi_G^C)\).”** For the concrete reflection realization in the modular-comparison appendix, the infinity equation is \(q(x,y,z)=x^2+yz=0\), and the even Clifford algebra of this displayed polynomial maps isomorphically to \(M_2(R)\) by the matrices below over every commutative base ring \(R\). The maps \([a:c]\mapsto[ac:-a^2:c^2]\) and \(L\mapsto\operatorname{Hom}(R^2,L)\) give the actual identifications of its conic with \(\mathbf P^1_R\) and the rank-two right-ideal scheme of that algebra, while matrix units prove the Azumaya condition directly. **Context:** README bridge B12 — this verifies its three objects and the maps among them for the displayed split form; its request for all twisted forms and their descent requires the further descent data absent from these pages.
<!-- context-query: B12;conic;Azumaya;rank 4;quadratic forms -->

## Explicit algebra map

The integral polynomial \(q_{\mathbf Z}=x^2+yz\) base-changes along \(\mathbf Z\to\mathbf Z[1/2]\) to the form in the centred reflection example. Its base changes along \(\mathbf Z\to R\) are the all-ring objects computed below. The identification with the manuscript-shaped centred coordinates uses the bridge appendix's change of basis of determinant \(-2\), hence is made over \(\mathbf Z[1/2]\).

Let \(e_x,e_y,e_z\) be the Clifford generators with
\[
e_x^2=1,\qquad e_y^2=e_z^2=0,\qquad
e_xe_y+e_ye_x=e_xe_z+e_ze_x=0,\qquad
e_ye_z+e_ze_y=1.
\]
These are obtained by expanding \(v^2=q(v)\) with the convention \(q=x^2+yz\). Set
\[
D=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
Y=E_{12},\qquad Z=E_{21}.
\]
The assignment \(e_x\mapsto D,\ e_y\mapsto Y,\ e_z\mapsto Z\) respects every relation: in particular
\[
(xD+yY+zZ)^2=(x^2+yz)I.
\]
This identity is integral, including after reduction modulo \(2\).

The relations move \(e_x\) before \(e_y\) before \(e_z\), eliminate repeated generators, and express every even word in the span of
\[
1,\qquad i=e_xe_y,\qquad j=e_xe_z,\qquad k=e_ye_z.
\]
Their four images are \(I,E_{12},-E_{21},E_{11}\). They form an \(R\)-basis of \(M_2(R)\): the inverse coefficient map sends
\[
\begin{pmatrix}a&b\\c&d\end{pmatrix}
\longmapsto d\cdot1+b\,i-c\,j+(a-d)k.
\]
The spanning statement gives surjectivity from these four generators to the even algebra, and the displayed independent images show that their only linear relation has all coefficients zero. Thus the induced homomorphism
\[
C^0(x^2+yz)\ \longrightarrow\ M_2(R)
\]
is an algebra isomorphism, with the written inverse.

The algebra \(M_2(R)\) is free of rank \(4\), its centre consists exactly of scalar matrices (commutation with \(E_{11},E_{12},E_{21}\) gives this entrywise), and its canonical action map is
\[
M_2(R)\otimes_R M_2(R)^{\mathrm{op}}
\longrightarrow \operatorname{End}_R(M_2(R)),\qquad
A\otimes B\longmapsto(T\mapsto ATB).
\]
For the matrix units this sends
\[
E_{ij}\otimes E_{kl}\ :\ E_{mn}\longmapsto
\delta_{jm}\delta_{nk}E_{il}.
\]
These are precisely the sixteen elementary endomorphisms, each occurring once, so the action map is an isomorphism. This proves the split rank-four Azumaya assertion by the defining map.

## The conic and the right-ideal scheme

The morphism
\[
\nu:\mathbf P^1_R\longrightarrow Q,\qquad
[a:c]\longmapsto[ac:-a^2:c^2]
\]
has inverse \([-y:x]\) on \(D(y)\) and \([x:z]\) on \(D(z)\). The equation \(x^2+yz=0\) proves agreement on the overlap and both inverse identities; these opens cover \(Q\), since a homogeneous prime containing \(y,z\) would also contain \(x\). Hence this is an isomorphism of schemes over \(R\).

For a line subbundle \(L\subset\mathcal O_T^2\) on any \(R\)-scheme \(T\), define
\[
I_L=\{A\in M_2(\mathcal O_T):\operatorname{im}A\subset L\}
=\operatorname{Hom}(\mathcal O_T^2,L).
\]
It is a rank-two locally direct-summand right ideal: right multiplication \(A\mapsto AB=A\circ B\) precomposes with an endomorphism of the domain and preserves the image, and a local basis for \(L\) gives the two columns independently. Conversely, for such a right ideal \(I\), define \(M\) to consist of the columns \(v\) for which \((v,0)\in I\). Right multiplication by the four matrix units extracts each column and moves it to either position, proving \(I=M\oplus M\) and \(M_2(\mathcal O_T)/I=(\mathcal O_T^2/M)^{\oplus2}\). Thus \(M\) and \(\mathcal O_T^2/M\) are direct summands of locally projective rank-two modules; their fibre ranks are one, because twice each fibre rank is two as an equality of integers. Consequently \(M\) is a line subbundle.

The two assignments \(L\mapsto I_L\) and \(I\mapsto M\) are inverse and commute with arbitrary base change: the first is \(L\otimes(\mathcal O_T^2)^\vee\), and the second is the image of the idempotent \(I\to I\), \(A\mapsto AE_{11}\), identified with its first column. The inclusions are locally split, so these pullbacks require no flatness assumption. Together with \(\nu\), they supply the promised scheme isomorphisms
\[
Q\ \simeq\ \mathbf P^1_R\
\simeq\ \{\text{rank-two locally direct-summand right ideals of }M_2(R)\}.
\]
Under \(g\in\operatorname{GL}_2(R)\), conjugation sends \(I_L\) to \(I_{gL}\), while the trace-zero matrix map of the bridge appendix satisfies \(M(gv)=\det(g)\,gM(v)g^{-1}\). The projective scalar factor disappears through the explicit quotient to \(Q\), proving compatibility with the projective conic action used there.

## Literature and reproduction

John Voight, *Quaternion Algebras* (2021), chapter 22, develops the even Clifford construction for ternary quadratic forms; its split example 22.3.12 uses a directly comparable ternary equation. The actual change of coordinates from the displayed equation here to \(XY-Z^2\) is \(X=y,\ Y=-z,\ Z=x\), giving \(XY-Z^2=-q\); the proof above computes our sign convention independently, so no unproved identification by a name or a sign convention is needed. [Primary chapter](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_22).

The companion split_clifford.py verifies the integral generator relations, the generic square identity, the four-element coefficient inverse, the complete sixteen-entry multiplication table in the displayed matrix basis, and the sixteen matrix-unit actions. It writes split_clifford_results.json, including the unit determinants of both basis maps; the algebra and functor proofs above supply the conclusions over arbitrary base rings.
