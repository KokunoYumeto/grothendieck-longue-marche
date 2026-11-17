# The actual hexagon defect in the full Alexander module

Checkpoint29 research. All checkpoint28 sources and the proposed A87/A88 sources remain unchanged. This is a new exact marked relation and a consequence under the additional full-GT hypothesis. It does not settle the full coefficient or nonlinear cusp gate.

## 1. Actual data and the existing coefficient test

Use A87/A88's actual negative GT0 involution alpha, canonical u in F', canonical duality u(y,x)=u(x,y)^{-1}, and d=d_alpha=2k+1. Put

\[
z=(xy)^{-1},\qquad m=(d-1)/2\in2\widehat{\mathbb Z},
\quad u_0=u(x,y),\quad u_1=u(y,z),\quad u_2=u(z,x).
\]

The evenness of m is A45's established k in 2Zhat; it is not an assumption on a conjectural positive multiplier. The actual positive hexagon defect is

\[
\mathcal H_d=u_0x^m u_2z^m u_1y^m\in F'.                 \tag{1}
\]

It is the entire actual word, whether or not it equals one. A87 identified it with u0 Xi_d^{-1} u0^{-1}. No vanishing is assumed here.

Let K=closed normal closure of x in F and let

\[
\Lambda=\mathbb F_2[[\widehat{\mathbb Z}]],\qquad
K/\overline{K^2[K,K]}=\Lambda[x],\qquad T=\text{image of }y.
\]

Identify [x] with 1. The coefficient bar sends T to T^{-1}. Write

\[
U=[u_0],\qquad W=[u_1],\qquad R_d=[\mathcal H_d],\qquad
\Theta_u=1+(T-1)(U+\overline U),
\quad (T-1)D_b=T^b-1.                                  \tag{2}
\]

Every u_i lies in F' and hence in K. The module retains the full procyclic head, not only its pro-two quotient. A88 proves

\[
\Theta_uD_{a_{\rm reg}}=1,
\qquad a_{\rm reg}=d\iff\Theta_uD_d=1.                 \tag{3}
\]

The new exact relation is

\[
\boxed{\quad\overline{R_d}+T^dR_d=\Theta_uD_d+1.\quad} \tag{4}
\]

In particular the full coefficient equality is equivalent to the specified weighted symmetry of the actual hexagon class:

\[
\boxed{\quad a_{\rm reg}=d
\iff\overline{R_d}=T^dR_d.\quad}                       \tag{5}
\]

This gives a necessary linear condition on the nonlinear defect, not a proof that the condition holds or that the defect vanishes.

## 2. Two actual basis transformations determine the coefficient orders

The free basis (y,z) has x=(yz)^{-1}. Let beta be its swap:

\[
\beta(y)=z,\quad\beta(z)=y,\quad
\beta(x)=(zy)^{-1}=y^{-1}xy.
\]

Thus beta preserves K, sends the retained head T to T^{-1}, and sends [x] to T^{-1}[x]. Its action on the entire compact module is

\[
[P(T)]\longmapsto T^{-1}P(T^{-1}).
\]

Canonical duality applied in the actual basis (y,z) gives beta(u1)=u(z,y)=u1^{-1}. Passing to characteristic two therefore gives

\[
T^{-1}\overline W=W,\qquad\overline W=TW.              \tag{6}
\]

There is no missing conjugator: the factor T^{-1} is exactly the displayed image y^{-1}xy of the original meridian.

Next let nu be the actual basis transformation x to x, y to z. It preserves K, fixes [x], and inverts the retained head, so it acts by coefficient bar. Consequently [u(x,z)]=bar U. Canonical duality again gives u(z,x)=u(x,z)^{-1}, and hence

\[
[u_2]=\overline U.                                    \tag{7}
\]

These identities use genuine continuous substitutions of the same full canonical word. They are not relations imposed on independently chosen Alexander data.

## 3. Ordered evaluation of the entire hexagon word

In the quotient by the mod-two commutator subgroup of K, write elements as a module part followed by a retained head. The product law is

\[
(P,T^r)(Q,T^s)=(P+T^rQ,T^{r+s}).
\]

The original z=y^{-1}x^{-1} therefore has module coordinate T^{-1} and head T^{-1}. For every m in Zhat,

\[
[z^m]_{\rm module}=T^{-m}D_m,
\qquad\text{head}(z^m)=T^{-m}.                         \tag{8}
\]

This follows first from the finite geometric sum on integer powers and then by continuity. Since m is even, the x^m module coordinate is zero. Reading (1) in its actual order and using (7)–(8) gives

\[
R_d=U+\overline U+T^{-m}D_m+T^{-m}W.                    \tag{9}
\]

Only u1 is conjugated by the accumulated retained head T^{-m}; no factors have been commuted in the group.

Write F_u=U+bar U, so bar(F_u)=F_u. The geometric-sum identities in the full ring are

\[
\overline{D_m}=T^{1-m}D_m,\quad
1+T^m=(T-1)D_m,\quad
D_{2m+1}=1+T(1+T^m)D_m.                               \tag{10}
\]

These follow by continuity from integer powers and the already proved continuous D-function, rather than division in a finite group algebra. Using d=2m+1, equations (6), (9) and (10) give

\[
\begin{aligned}
\overline{R_d}+T^dR_d
 &= (1+T^d)F_u+T(1+T^m)D_m
      +T^m\overline W+T^{m+1}W\\
 &= (T-1)D_dF_u+T(1+T^m)D_m\\
 &= (T-1)D_dF_u+D_d+1\\
 &=\Theta_uD_d+1.
\end{aligned}
\]

This proves (4). Combining it with the actual full-head test (3) proves (5). The cancellation of W uses the exact weighted involution (6); replacing it by unweighted bar-invariance would give the wrong relation.

## 4. A full dyadic coefficient consequence for actual full-GT involutions

Now add the hypothesis alpha in full GT, so the pentagon input of A42 is available. This is an extra hypothesis; no assertion in this section is made for a general GT0 involution.

The complete formal A42 proof supplies the actual prescribed pair (mu_2,u_2) in the pro-two GT group for either local square root of 1+24c2(u)_2. The complete formal A45 proof identifies those roots with plus or minus d_2 and already proves d_2 congruent1 modulo4. Thus the prescribed pair (d_2,u_2) satisfies its actual pro-two positive hexagon. In particular the image of the specific word (1) in F_2^(2) is one.

There is a natural compatible map from the full cyclic-cover module to

\[
\Lambda_2=\mathbb F_2[[\mathbb Z_2]],
\]

sending the original x,y and retained head to their pro-two images. Hence R_d has image zero there. Equations (3)–(4) imply

\[
\Theta_{u,2}D_{d_2}=1=\Theta_{u,2}D_{a_{{\rm reg},2}}.
\]

The first identity already makes Theta a unit, so D_{d2}=D_{a2}. Multiplication by T-1 gives T^{d2}=T^{a2}. Distinct elements of Z2 are separated by its finite cyclic heads, whose group elements are a basis in the finite F2 group algebra. Therefore

\[
\boxed{\quad a_{{\rm reg},2}=d_{\alpha,2}
\quad\text{for every actual full-GT involution.}\quad}  \tag{11}
\]

Equivalently the two canonical frame coordinates satisfy t_2=rho_{D,2}, and the dyadic component of (Omega_alpha)_ab is zero. This is stronger than the mod-eight congruence, but it uses the full-GT pentagon through A42. It neither identifies the odd components nor proves nonlinear Omega=1. No transport of an unproved pro-two fixed-subgroup theorem or uniqueness of a projected norm frame is required: the proof uses the actual pro-two hexagon and the explicit module maps only.

## 5. Exact remaining scope

For GT0 data, equations (4)–(5) are unconditional. The missing full coefficient comparison is precisely the weighted symmetry of the actual full-head hexagon class. For full-GT data, its pro-two projection is proved, while mixed and odd cyclic heads remain part of the full test.

Even if (5) is proved, a class in this one Alexander quotient need not determine the whole group word. The nonlinear obstruction remains the entire Xi_d or Omega_alpha from A87/A86. The prospective modular map sending s to v and delta to delta^d is still not an actual map before its cubic relation is proved, so the relative LM7/R2 lifting theorem is not applied circularly.

No finite quotient or period enumeration is used. The dependencies are the complete A42/A45 proofs, reread at this use, and the fully reviewed A87/A88 marked identities and cyclic-cover argument. All newly used basis transformations and module calculations are printed above.
