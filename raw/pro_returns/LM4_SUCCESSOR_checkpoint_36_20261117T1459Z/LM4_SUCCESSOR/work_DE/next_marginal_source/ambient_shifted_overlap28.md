# One exact translated overlap of the two actual unfilled edge groups

Status: complete ordinary proof; independent review requested. The previously frozen B136/B137 sources are unchanged.

## 1. Actual marking and claim

Use the whole marking of B134, B136 and B137:

\[
V=R^0*_Kp(R^0),\quad p|_K=\eta,\quad \theta(R^0)=p(R^0),
\quad E_1=C\langle K,k\rangle C,
\]
\[
H_i=\langle E_1,a^{-1}p(k)a\rangle,
\quad H_j=\langle p(E_1),\eta(a)^{-1}k\eta(a)\rangle,
\]
\[
B_i=\langle f,a^{-1}p(k)a\rangle,
\quad B_j=\langle\eta(f),\eta(a)^{-1}k\eta(a)\rangle.
\]
Their actual embedded ordinary subamalgams are
\[
H_i=E_1*_{\langle f\rangle}B_i,
\qquad H_j=B_j*_{\langle\eta(f)\rangle}p(E_1).
\]
Set \(\zeta=\eta(a)\). Then the following **whole translated intersection**, not only a vertex intersection, is exact:

\[
\boxed{H_i\cap\zeta H_j\zeta^{-1}=\langle k\rangle.}
\tag{1}
\]
All statements about trees and intersections in this note are ordinary. No corresponding completed subgroup intersection is claimed.

## 2. The entire regional tree input

Put \(L=\langle K,k\rangle\). The actual B117 color retraction gives
\[
E_1\cap L=H,\qquad
L=H*_{T}P,\quad T=\langle k\rangle,
\]
\[
H=\langle h,k\mid[h^2,k]\rangle,
\quad P=\langle k\rangle\times F(a,d,e,V_4),
\quad f=hk^{-1},\quad V_4=f^{-1}Bf.
\]
The actual retraction \(r:L\to K\) fixes \(K\), kills \(k\), and sends \(H\) onto \(\langle f\rangle\subset H\).

Use the exact B137 words
\[
\ell=afa^{-1},\quad q=\eta(\ell),\quad U=\langle k,q\rangle,
\]
\[
\gamma=afV_4f^{-1}a^{-1}f,\quad D=ded^{-1},\quad
w=\gamma Df^{-1}d^{-1}.
\]
The complete marked reflection dictionary gives literal free-word equalities
\[
q=wf^{-1}w^{-1},\quad
\zeta=\gamma V_4^{-1}f^{-1}a^{-1},\quad
\zeta B_j\zeta^{-1}=U.
\tag{2}
\]
The B137 all-power endpoint proof embeds the subdivided tree of
\(\langle k\rangle*\langle q\rangle\) into the tree \(X\) of \(H*_TP\).
Write \(Y\) for its image. The fundamental segment joins \(aH\) to \(wH\).
Its first edge at \(aH\) is \(afT\). The incident edges of \(Y\) at \(aH\) are exactly
\[
k^n afT\quad(n\in\mathbb Z).
\tag{3}
\]
The stabilizer of \(aH\) in \(U\) is exactly \(\langle k\rangle\); every interior subdivision vertex has trivial \(U\)-stabilizer. These follow from the injective equivariant tree map, not a finite edge sample.

## 3. Two further vertex intersections

The path from \(H\) to \(aH\) ends through \(aT\). None of the edges (3) equals \(aT\): such equality would require
\[
a^{-1}k^na f=k^nf\in T,
\]
which is impossible by the \(h\)-exponent character of \(H\).
Since \(Y\) is a subtree and hence convex, the nearest point in \(Y\) to \(H\) is therefore \(aH\). An element of \(U\) fixing \(H\) fixes this projection and so belongs to \(\langle k\rangle\). Conversely every power of \(k\) fixes \(H\). Consequently
\[
U\cap H=\langle k\rangle,
\qquad E_1\cap U=\langle k\rangle.
\tag{4}
\]
The second equality uses \(U\subset L\) and \(E_1\cap L=H\).

At the interior vertex \(\gamma P\), the two directions in \(Y\) are represented by \(1,D\) in \(P/T\). The free-leaf coordinate \(V_4^{-1}\) is different from both. Thus the adjacent vertex \(\gamma V_4^{-1}H\) lies on the third, private branch and projects to \(\gamma P\). It has trivial \(U\)-stabilizer. Equation (2) gives
\[
\zeta aH=\gamma V_4^{-1}H,
\]
because \(f^{-1}\in H\). Hence
\[
B_j\cap aHa^{-1}=1.
\]
Since \(a\in L\),
\[
aE_1a^{-1}\cap L=aHa^{-1},
\qquad B_j\cap aE_1a^{-1}=1.
\tag{5}
\]
Applying \(\theta\), including its actual restriction \(\eta\) on \(K\), gives
\[
B_i\cap\zeta p(E_1)\zeta^{-1}=1.
\tag{6}
\]
This preserves the entire conjugating word; no peripheral-conjugacy replacement is used.

## 4. All shared incident directions

The first vertex groups of \(H_i\) and \(\zeta H_j\zeta^{-1}\) are \(E_1\) and \(U\). Their incident directions at the standard left vertex of the tree of \(V\) are \(E_1K/K\) and \(UK/K\).

Take \(u\in U\cap E_1K\), so \(u=e k_0\), \(e\in E_1\), \(k_0\in K\). As \(u,k_0\in L\), we have \(e\in H\). Also \(r(U)=\langle q\rangle\subset U\), and \(r(H)\subset H\). Therefore
\[
u r(u)^{-1}=e r(e)^{-1}\in U\cap H=\langle k\rangle.
\]
Since \(r(u)\in\langle q\rangle\), this proves the exact set identity
\[
U\cap E_1K=\{k^nq^j:n,j\in\mathbb Z\}.
\tag{7}
\]
The reverse inclusion follows from \(k\in E_1\) and \(q\in K\). Thus the shared incident edges at the left vertex are precisely
\[
k^nK\quad(n\in\mathbb Z).
\tag{8}
\]
They are distinct by the actual base-winding homomorphism.

At the standard right vertex, apply \(\theta\). The two groups become \(B_j\) and \(aE_1a^{-1}\). If
\(b\in B_j\cap aE_1a^{-1}K\), then \(b=h_0k_0\) with \(h_0\in aHa^{-1}\). The actual retraction preserves both \(B_j\) and \(aHa^{-1}\). Hence
\[
b r(b)^{-1}=h_0r(h_0)^{-1}
 \in B_j\cap aHa^{-1}=1.
\]
Thus \(b\in K\). Conversely elements of \(B_j\cap K\) plainly occur, so the two direction sets have only the common standard edge. By \(\theta\), the same is true of \(B_i\) and \(\zeta p(E_1)\zeta^{-1}\) at the right endpoint.

## 5. The whole intersection is the cyclic star stabilizer

Let \(\mathcal T_i,\mathcal T_j\) be the actual embedded invariant trees from B137, each containing the standard edge \(e_0=K\). Since \(\zeta\in K\), \(\zeta\mathcal T_j\) also contains \(e_0\) with the same endpoints. Equations (4) and (6) are its vertex comparisons with \(\mathcal T_i\).

The subgroup \(\langle k\rangle\) belongs to both groups, so the common subtree contains every edge \(k^ne_0\). These edges form an infinite star with one left vertex. Equation (8) lists **every** shared incident edge there. At the standard right endpoint only the incoming edge is shared, by Section 4; translation by the common \(k^n\) proves the same at every other right endpoint of this star.

The intersection of two subtrees of a tree is convex. Any further common edge would have a first departure from the star; all possible departures have just been excluded. Consequently
\[
\mathcal T_i\cap\zeta\mathcal T_j
   =\bigcup_{n\in\mathbb Z}k^ne_0.
\tag{9}
\]
An element of the whole subgroup intersection preserves this star. Its only left vertex is the standard one, so the element fixes that vertex and belongs to \(E_1\cap U=\langle k\rangle\). Conversely \(\langle k\rangle\) lies in both groups. This proves (1).

## 6. What this says about the two actual fillings

There is an actual winding homomorphism \(V\to\mathbb Z^2\), giving the two regional base windings and killing the common fiber subgroup \(K\). It sends \(k\) to \((1,0)\). Every one of B134's five initial target relators and every theta-mate is a commutator, hence maps to zero. Therefore the **entire two-family** initial normal subgroup \(N_*\) satisfies
\[
N_*\cap\langle k\rangle=1.
\]
The same continuous winding map proves that the closed initial normal subgroup in \(\widehat V\) meets the actual embedded \(\widehat{\mathbb Z}(k)\) trivially. This cyclic survival statement does not assert a completed analogue of (1).

Thus this specified nontrivial translated overlap is cyclic and is not itself collapsed by either complete initial filling. It does **not** identify the subgroup generated by the two translated groups with their amalgam, prove any quotient embedding, classify all other translates, or establish kappa-invariance of the actual local kernel. Those would require further control of ambient relations and of the full family of translated overlaps. In particular an unshifted or single-shift intersection calculation cannot replace that normal-closure analysis.

## Provenance

The only literal word input is the complete actual reflection dictionary and the previously executed whole-input fork certificate:

- `work_DE/next_marginal_source/annular_neck_reflection23.json`;
- `work_DE/next_marginal_source/check_ambient_vertex_fork28.py`, genuine `.out`, `.err`, and `ambient_vertex_fork28.json`;
- the frozen B136 and B137 sources and their complete proof reviews.

No new finite subgroup, double-coset, word-depth or period census was used. Every exponent in the proof is unrestricted.
