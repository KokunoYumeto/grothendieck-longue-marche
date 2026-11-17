# The actual elliptic joint kernel as an intersection of two retraction kernels

Checkpoint36 research, separate from the frozen formal statements. All subgroups, maps and completions below are the actual ones; closures are taken in the indicated profinite group. This note uses the complete A124–A125 fibration/topology proofs and the fully reviewed based table in `actual_elliptic_based_forgetting36.md`. It does not identify an abstract infinite-index completion or assert that a closed subgroup of a free profinite group is itself free profinite.

## 1. The actual three-generator fiber

Let G be the full completion of the reduced elliptic braid group B1,3 and P its pure subgroup. Retain the based deletion maps pi1, pi2, pi3 and the target E=Fhat(X,Y), with K=[Y,X]. Put

\[
 N_3=\ker(\pi_3:P\longrightarrow E),\qquad
 h=X_3,\quad k=Y_3,\quad m=A_{13}=\tau^{-1}\sigma^2\tau.
\tag{1}
\]

The actual forget-third-strand fibration has once-punctured-torus base and torus-minus-two-points fiber. The original third-strand handle paths X3,Y3, together with the original meridian A13 about one remaining puncture, are its three free generators: the surface presentation eliminates the other puncture meridian. Equivalently these are the fiber generators used in the complete based-table proof. A124 proves that this actual fiber has full induced profinite topology, using characteristic finite fiber targets and finite source-action quotients. Hence the kernel in(1) is its embedded full completion and

\[
 N_3=\widehat F(h,k,m).
\tag{2}
\]

In particular H=cl<h,k> is an actual free factor of N3. These are the finite-rank fiber and its topology, not a completion assigned to the joint kernel below.

## 2. Every original deletion image

The complete based table gives

\[
\begin{array}{c|ccc}
 &h&k&m\\\hline
 \pi_1&X^{-1}&Y^{-1}&1\\
 \pi_2&X^{-1}&Y^{-1}&K\\
 \pi_3&1&1&1.
\end{array}
\tag{3}
\]

For example X3=(X X2) inverse and Y3=(Y Y2) inverse give both handle rows. The marked meridian table gives pi1(A13)=1, pi2(A13)=K and pi3(A13)=1. Thus all three images retain their actual whiskers.

Let iota:H→E be the isomorphism h↦X inverse, k↦Y inverse, and set

\[
 w=[k^{-1},h^{-1}]\in H,\qquad \iota(w)=K.
\]

Define the two continuous retractions

\[
 r_0,r_1:N_3\longrightarrow H,
 \quad r_0|_H=r_1|_H=\mathrm{id},\quad
 r_0(m)=1,\quad r_1(m)=w.
\tag{4}
\]

Then pi1|N3=iota r0 and pi2|N3=iota r1 exactly. The inverse substitutions for the free basis give

\[
 U=\ker r_0=\langle\!\langle m\rangle\!\rangle_{N_3},\qquad
 V=\ker r_1=\langle\!\langle m w^{-1}\rangle\!\rangle_{N_3}.
\tag{5}
\]

Indeed quotienting by either displayed relator eliminates the third generator and leaves H, with the indicated retraction. The replacement m↦m w inverse is an invertible Nielsen substitution fixing h,k, so the second presentation is as literal as the first.

## 3. The full joint image and its exact kernel

Write Eab=E/E′ and form the actual compact fiber product

\[
 D=E\times_{E_{\mathrm{ab}}}E
   =\{(x,y)\in E\times E:xE'=yE'\}.
\tag{6}
\]

The joint image of(pi1,pi2) on N3 is exactly D. It is contained in D by(3), because K is a commutator. It contains the entire diagonal E from the actual H free factor and contains(1,K) from m. Conjugating(1,K) by the diagonal E gives every generator of(1,E′), since the closed normal closure of K in E is E′. The joint image is compact and hence closed, so it contains that whole subgroup. Every pair in D is a product of a diagonal element and an element of(1,E′). This proves surjectivity, without exchanging an abstract completion with a fiber product.

Let the whole derived Brunnian kernel be

\[
 \mathcal B=\ker\bigl((\pi_1,\pi_2,\pi_3):P'\longrightarrow(E')^3\bigr).
\]

There is no extra derived intersection to insert in the following exact model:

\[
 \boxed{\mathcal B=U\cap V,\qquad
 1\longrightarrow\mathcal B\longrightarrow\widehat F(h,k,m)
 \xrightarrow{(\pi_1,\pi_2)}E\times_{E_{\mathrm{ab}}}E
 \longrightarrow1.}
\tag{7}
\]

To check the point carefully, any element of B lies in N3 and is killed by r0,r1, hence lies in U intersect V. Conversely U is already contained in P′. The original meridian m belongs to P′ by A125's actual integral abelianization calculation; P′ is closed normal in P and therefore contains its entire N3-normal closure U. Thus an element of U intersect V is in P′ and is killed by all three original deletions. This is precisely B. Compactness also shows that the induced quotient in(7) is a topological isomorphism, not only an algebraic bijection.

## 4. Two further exact consequences, with their limits

The product UV is closed, since U,V are compact normal subgroups. Eliminating both m and m w inverse leaves H modulo the closed normal closure of w, which is Hab. Hence

\[
 N_3/(UV)\cong H_{\mathrm{ab}}.
\tag{8}
\]

The restrictions of the other retractions have exact images H′:

\[
 U/\mathcal B\xrightarrow[\ r_1\ ]{\ \cong\ }H',\qquad
 V/\mathcal B\xrightarrow[\ r_0\ ]{\ \cong\ }H'.
\tag{9}
\]

For r1(U), use r1(m)=w and all H conjugates. For r0(V), use r0(m w inverse)=w inverse. In both cases the image is closed and is the whole normal closure of that commutator in H. The kernels are exactly U intersect V. No section of either extension is asserted.

The kernel is concretely nontrivial. The original free word

\[
 b_*=[m,mw^{-1}]
\tag{10}
\]

belongs to U intersect V, because a commutator of two elements from normal subgroups U,V belongs to their intersection. In the abstract free product F(h,k)*<m>, it reduces to the nonempty alternating word

\[
 m^2 w^{-1}m^{-1}w m^{-1}.
\]

Here w is a nonidentity commutator in F(h,k). The abstract finite-rank free group embeds in its full profinite completion, so(10) remains nonidentity in the actual N3. This is a symbolic reduced-word argument, not a finite target enumeration or an execution claim.

The model(7) retains the entire kernel on which the exact C3 cohomology and corrected elliptic involution act. Those actions need not preserve the particular ambient fiber N3, since the cyclic braid permutes deletions. No further action on N3, freeness of B, equality B=[U,V], finite presentation of the fiber product, canonical value of a_u, boundary identity, original full hexagon or CM conclusion is inferred.
