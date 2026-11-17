# The next actual modular central refinement and a full peripheral lift

Checkpoint34 research only. All A106–A108 proposed sources remain frozen. This proof uses the original full-GT canonical u and the same d,k,H_d throughout. It is not a claim that the canonical endomorphism itself is an automorphism of the full free group, or that the original CM parity vanishes.

## 1. Objects and conclusions

Retain F=hat F(x,y), B=C2(s) amalg C3(r), the original pure kernel F of B→S3, the full signed q:F→C, and
\[
N=\ker q,\quad N_1=\overline{[N,F]},\quad
E_1=F/N_1,\quad B_1=B/N_1.
\]
All closed commutators and quotients below are actual ambient ones. Put
\[
P=F^{(2)},\quad O=\ker(F\to P),\quad
M_2=\ker(P\to C_{(2)}),\quad M_{21}=\overline{[M_2,P]},
\]
\[
\overline B=B/O,\qquad B_2^*=\overline B/M_{21},\qquad
M_B=\overline{[N_1,B]}.
\]
The use of \(\overline B\), whose pure subgroup is the full free pro-two P, is essential. It is not B with a different kernel silently substituted.

We prove:
\[
H^2_{\rm cont}(B_1,\mathbb Q_\ell/\mathbb Z_\ell)=0
\quad(\ell\text{ odd}),                                      \tag{1}
\]
\[
N_1/M_B\text{ is pro-two},\qquad
M_B=N_1\cap\pi_2^{-1}\bigl(\overline{[M_{21},\overline B]}\bigr),
\qquad H_d\in M_B.                                            \tag{2}
\]
Here \(\pi_2\) on \(N_1\) is the restriction of the actual map B→\(\overline B\); it agrees with the maximal pro-two map on F.

Consequently the original assignments
\[
s\mapsto v=u^{-1}s,\qquad \delta=sr\mapsto\delta^d
\]
give a genuine automorphism of B/M_B, with positive or negative r-factor frame as in A108 and with those frames lifting the actual ones on B1. The closed-normal central lifting criterion of A3/A34 then yields a full peripheral automorphism of B inducing the specified \(\Psi_1\) on B1. Its cusp can be normalized literally to \(\delta^d\).

This is a lift of the quotient automorphism. It is not an identification of that lift's full pure substitution with the actual canonical \(\psi_d\), nor a full conjugacy between the original \(\alpha\) and \(c_B\).

## 2. The actual pure product and the two-primary comparison

Write \(C_o=\prod_{p\ {\rm odd}}\operatorname{SL}_2(\mathbb Z_p)\).
Beyl's Proposition5.7(a) gives \((C_o)_{\rm ab}=C_3\), supported at3, with the original character \(\chi(X)=\chi(Y)=1\). Thus \(C_o\) has no nontrivial pro-two quotient: any nontrivial finite two-group quotient has a nontrivial C2 character, which would contradict this abelianization.

The maximal pro-two quotient of the actual \(C=C_{(2)}\times C_o\) is therefore \(C_{(2)}\). Right exactness of the maximal pro-two quotient gives
\[
\pi_2(N)=M_2,\qquad \pi_2(N_1)=M_{21}.                         \tag{3}
\]
For clarity, \(P/\pi_2(N)\) is pro-two and has exactly the universal property of the maximal pro-two quotient of F/N. This proves the first equality; continuous commutator functoriality and compactness give the second.

Define
\[
P^*=P/M_{21},\qquad
D_o=(F_{\rm ab})_o\times_{(C_o)_{\rm ab}}C_o.                   \tag{4}
\]
The map from F to \(D_o\) is onto. First match the odd abelian vector. Its discrepancy from the requested \(C_o\)-coordinate lies in \(C_o'\), and is corrected by an F' lift, because \(q_o(F')=C_o'\). The map to \(P^*\) is onto and kills N1 by (3). A106's exact coordinate equality proves that the combined map induces an injection
\[
E_1\hookrightarrow P^*\times D_o.                             \tag{5}
\]
Indeed, a zero \(P^*\)-coordinate gives zero signed dyadic coordinate and zero dyadic abelian vector; the zero \(D_o\)-coordinate gives zero odd signed and abelian coordinates. The A106 criterion then gives membership in N1.

The kernel of \(D_o\to C_o\) is pro-odd abelian. Hence any map from \(D_o\) to a finite two-group kills that kernel and factors through \(C_o\), and is trivial. Profinite Goursat applied to the subdirect image in (5) now yields the exact product
\[
E_1=P^*\times D_o.                                            \tag{6}
\]
Any common quotient would be pro-two because \(P^*\) is; the preceding argument excludes a nontrivial such quotient of \(D_o\).

The factor \(D_o\) is normal in B1. More intrinsically it is the kernel of
\[
B_1\longrightarrow B/(ON_1)=B_2^*.
\]
Both O and N1 are normal in B: O is characteristic in the actual F, and A107 proves the required full signed geometric stability of N1. The image of N1 under B→\(\overline B\) is exactly M21 by (3). Thus this quotient identification, including its S3 action, is literal.

Let \(\mathcal A_2=\mathbb Q_2/\mathbb Z_2\), always with trivial action. The pro-odd central kernel in \(D_o\to C_o\) has no positive continuous cohomology with two-primary coefficients, by finite-quotient averaging. Beyl5.7(b), the complete product argument of A106, and the odd abelianizations give
\[
H^1(D_o,\mathcal A_2)=H^2(D_o,\mathcal A_2)=0.                 \tag{7}
\]
The low-degree Lyndon–Hochschild–Serre spectral sequence for \(D_o\to B_1\to B_2^*\) therefore gives
\[
H^2(B_2^*,\mathcal A_2)\ \xrightarrow{\ \mathrm{inf}\ }\ 
H^2(B_1,\mathcal A_2)
\quad\text{is an isomorphism}.                               \tag{8}
\]
No assertion that either side is zero is used.

## 3. The odd cohomology calculation, including the prime3 lattice

Set A=N/N1. It is central in E1. Its map to \(F_{\rm ab}\) has kernel
\[
K=(N\cap F')/N_1,
\]
which is pro-two by A106, and image
\[
L=\ker(F_{\rm ab}\to C_{\rm ab}).                              \tag{9}
\]
The image assertion follows from right exactness of abelianization: the image of compact N is closed. Since A is profinite abelian, its odd primary components are canonically those of L. Consequently
\[
A_\ell\simeq\mathbb Z_\ell^2\quad(\ell\ge5),\qquad
A_3\simeq L_3=\{(a,b)\in\mathbb Z_3^2:a+b\equiv0\bmod3\}.     \tag{10}
\]
Their actual S3 actions are the restrictions of the original swap \(\iota\) and cyclic matrix \(\rho\) on \(F_{\rm ab}\).

Fix an odd prime \(\ell\), and put \(\mathcal A_\ell=\mathbb Q_\ell/\mathbb Z_\ell\). A106's actual product/Beyl argument gives
\[
H^2(C,\mathcal A_\ell)=0.
\]
Apply LHS to the central extension \(A\to E_1\to C\). The action of C on
\[
M_\ell=H^1(A,\mathcal A_\ell)
\]
is trivial. In total degree2 its possible associated graded terms are:
- the quotient of \(H^2(C,\mathcal A_\ell)=0\);
- a **submodule** of \(H^1(C,M_\ell)\);
- a **submodule** of \(H^2(A,\mathcal A_\ell)\).

The submodule qualification is essential: for the positions (1,1) and (0,2) there are no incoming differentials in this first-quadrant spectral sequence. Thus it is legitimate to use the vanishing of their S3 invariants. The canonical filtration and differentials are equivariant under conjugation by B1; inner E1 actions act trivially on these cohomology groups, so the action factors through the actual S3.

For \(\ell\ne3\), \(H^1(C,M_\ell)=0\). For \(\ell=3\), it is
\[
\operatorname{Hom}(C_{\rm ab},M_3)=M_3[3].
\]
The actual S3 action on the C3 abelian quotient of C is trivial: the swap preserves the character sum, and the cyclic substitution sends each of x,y,z to a generator with that same character modulo3. The central cyclic sign has character zero. Hence the invariants here are the invariants of the dual root lattice. They vanish. Explicitly, with
\[
a=(1,-1),\qquad b=(0,3)
\]
as a basis of L3,
\[
(\iota-1)a=-2a,\qquad(\rho-1)a=b.
\]
Since2 is a unit in \(\mathbb Z_3\), these relations kill both basis vectors in the coinvariants. Thus \(L_{3,S_3}=0\) and \(M_3[3]^{S_3}=0\).

Finally \(H^2(A,\mathcal A_\ell)\) is the continuous alternating-form module on \(\Lambda^2 A_\ell\). This follows from the two procyclic factors of the rank-two lattice: each has cohomological dimension one, and the product cross term is the alternating bicharacter. Other primary factors have zero positive \(\ell\)-cohomology. The swap has determinant−1 on this lattice, so acts by−1 on its second cohomology. Since \(\ell\) is odd, its invariant subgroup is zero.

Each associated graded term therefore has zero S3 invariants. The finite filtration implies
\[
H^2(E_1,\mathcal A_\ell)^{S_3}=0.                             \tag{11}
\]

Now use \(E_1\to B_1\to S_3\). We have
\[
H^1(E_1,\mathcal A_\ell)=
\operatorname{Hom}(F_{\rm ab},\mathcal A_\ell)
=\mathcal A_\ell^2
\]
with the actual standard dual action. The remaining total-degree2 terms vanish:
\[
H^2(S_3,\mathcal A_\ell)=0,\qquad
H^1(S_3,\mathcal A_\ell^2)=0.                                 \tag{12}
\]
For \(\ell\ge5\) this is finite-group averaging. At3 use the normal C3 and the quotient C2. On the standard dual, the norm \(1+\rho+\rho^2\) is zero, while \(\rho-1\) is onto the divisible module: its determinant is3, and the adjugate formula plus divisibility supplies preimages. Thus its C3 first cohomology is zero; C2 has invertible order. For the trivial coefficient module, \(H^2(C_3,\mathcal A_3)=\mathcal A_3/3\mathcal A_3=0\), and positive C2 cohomology vanishes. These prove (12). Equations (11)--(12) prove (1).

## 4. The actual free-pro-two modular comparison

The quotient \(\overline B=B/O\) has pure subgroup P, a full free pro-two group of rank2, and quotient S3 with the actual standard action on the pure abelianization.

Its continuous two-primary H2 is zero. Indeed \(H^2(P,\mathcal A_2)=0\). For \(H^1(P,\mathcal A_2)=\mathcal A_2^2\), the C3 invariants vanish because \(\rho-1\) has determinant3, a two-adic unit; higher C3 cohomology vanishes by averaging. Therefore
\[
H^1(S_3,\mathcal A_2^2)=0.
\]
For the trivial coefficients, normal-C3 averaging reduces
\[
H^2(S_3,\mathcal A_2)=H^2(C_2,\mathcal A_2)
=\mathcal A_2/2\mathcal A_2=0.
\]
The same LHS total-degree2 calculation gives
\[
H^2(\overline B,\mathcal A_2)=0.                              \tag{13}
\]
This direct proof avoids any unverified comparison of extension classes.

There is the actual commutative extension diagram
\[
\begin{array}{ccccccccc}
1&\to&N_1&\to&B&\to&B_1&\to&1\\
 &&\downarrow&&\downarrow&&\downarrow\\
1&\to&M_{21}&\to&\overline B&\to&B_2^*&\to&1 .
\end{array}                                                  \tag{14}
\]
Use the same transgression convention in both five-term sequences. Equations (8),(13) imply that every B-invariant continuous character \(\chi:N_1\to\mathcal A_2\) has the form
\[
\chi=\chi_2\circ\pi_2|_{N_1}+\lambda|_{N_1},                  \tag{15}
\]
where \(\chi_2:M_{21}\to\mathcal A_2\) is \(\overline B\)-invariant and \(\lambda:B\to\mathcal A_2\) is a character. To obtain this, lift the transgression of \(\chi\) through (8), choose a character with that lower transgression using (13), and use naturality and exactness on the difference. No surjectivity of a false full-kernel map is assumed; the required actual map was proved in (3).

For odd-primary characters, (1) makes the transgression zero, so every B-invariant \(\chi:N_1\to\mathcal A_\ell\) extends to a character of B. But \(N_1\subset F'\subset B'\), so all such characters are zero. Character separation of the compact abelian group \(N_1/M_B\) proves it is pro-two.

Commutator functoriality gives the forward inclusion in the coordinate formula (2). Conversely, for an element of its right side, every character in (15) vanishes: the first term kills \([M_{21},\overline B]\), and the second kills \(N_1\subset B'\). The odd-primary characters already vanish. Invariant-character separation proves the reverse inclusion.

The actual full canonical hexagon belongs to N1 by A106, and its whole pro-two image is1 by A89.3 with A42/A45 for this same u,d. Therefore the exact criterion gives \(H_d\in M_B\). This is stronger than a dyadic coefficient equality. In fact (3) and (2) also give the actual compact isomorphism
\[
N_1/M_B\ \simeq\ 
M_{21}/\overline{[M_{21},\overline B]}.
\]
No claim that N1 itself is pro-two is made; A110 proves the contrary.

## 5. The genuine next modular map and its factor frames

The ordered identity
\[
H_d=u((v\delta^d)^3)^{-1}u^{-1}
\]
now kills the cubic in B/M_B. Since v²=1, the free profinite product defines a homomorphism B→B/M_B with s→v and r→vδ^d. Its pure restriction is the original \(\psi_d\).

This map kills M_B. Indeed \(\psi_d(N_1)\subset N_1\) by A107, while N1/M_B is central in B/M_B; the images of all commutators [N1,B] are therefore1. It descends to an endomorphism \(\Psi_M\) of B/M_B. Its pure map is onto because
\[
N_2=\overline{[N_1,F]}\subset M_B
\]
and A107 already proves \(\psi_d\) is an automorphism of F/N2. The finitely generated profinite pure quotient is Hopfian, hence this induced pure map is an automorphism. The S3 map is the identity, so \(\Psi_M\) is an automorphism of B/M_B. The same generator calculation gives \(\alpha\Psi_M=\Psi_M c_B\).

Lift the actual A108 frame h to \(\widetilde h\in F/M_B\). The two elements
\[
\Psi_M(r),\qquad \widetilde hR_e\widetilde h^{-1}
\]
have the same image in B1, so differ by an element of the central pro-two group N1/M_B. Both have order dividing3. Their central difference consequently has cube1 and is1. Thus every such lift is the required r-factor frame. The s-factor has its genuine full frame already: v is an involution in B with S3 image s, so the full finite-factor torsion theorem and the S3 normalization give v=gs g^-1 for a pure g. The cusp is mapped literally to δ^d. These are actual peripheral-power data at the next central refinement, not a use of a conjugacy-only theorem on powers.

## 6. Exact multiplier reduction and the full lift it permits

Choose an actual Galois element with cyclotomic multiplier d and its original normalized action \(\gamma\) on B. The original LM7_PUSH E65.8 gives \(\gamma(\delta)=\delta^d\); its original E65.15 proves, over every \(\mathbb Z_\ell\), signed covariance for the actual B3 representation. Restriction to the based pure generators \(x=u_{\rm braid}^2\), \(y=v_{\rm braid}^2\) gives
\[
q\gamma=\operatorname{Ad}(\mathcal V_\gamma)q.
\]
Hence \(\gamma(N)=N\), and functoriality gives preservation of N1 and M_B. This is a use of that explicit original theorem, not an assumption that an arbitrary peripheral automorphism preserves the signed kernel.

Compose \(\Psi_M\) with \(\gamma^{-1}\). The common multiplier cancels, including its r-exponent e. The resulting map on B/M_B fixes δ and preserves each positive peripheral conjugacy class, with specified literal conjugators. It descends to the corresponding automorphism \(\eta_1\) on B/N1.

The closed-normal modular central criterion in the final paragraph of A34, proved by the complete A3 finite-count argument, now applies with relative kernel **N1**:
\[
M_B=[N_1,B].
\]
It gives a full positive-peripheral automorphism \(\widetilde\eta\) inducing \(\eta_1\), with the specified conjugators modulo N1. Its cusp conjugator can be taken in N1, and the usual inner correction by that element fixes δ literally without changing the quotient data. Then
\[
\widetilde\Psi=\gamma\widetilde\eta
\]
is a full peripheral automorphism of B inducing \(\Psi_1\) on B1 and sending δ literally to δ^d.

The central criterion has been used at exactly the required level. Before the new \(H_d\in[N_1,B]\) argument, it yielded only a lift of the coarser action on B/N. It did not directly lift \(\Psi_1\).

## 7. Sources, status and remaining scope

The external cohomological input is only the already fully read original Beyl1986 Proposition5.7(a,b), printedp41, with the A106 product argument. All finite-group cohomology and lattice calculations needed at2 and3 are printed above. The LHS and five-term sequences are used for their actual continuous profinite extensions.

At this use I freshly read the complete A3 and A34 proofs and the entire original LM7_PUSH E65 source, including the precise all-multiplier covariance E65.15. The closed-normal criterion retains its already refereed original D50 dependency; no fresh whole D50 reread is claimed.

This is a new research proof, sent for complete independent review. No finite census, mathematical producer, private build, render, or central source edit was used. The frozen A106–A108 sources are unchanged.

The full lift has not been identified with the canonical \(\psi_d\) on F, and its conjugate of \(c_B\) is only known to agree with the original \(\alpha\) modulo N1. The original full involution norm, the coherent C2 class of A111, full Main A, and the actual CM parity are not decided.

