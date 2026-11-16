# Formal and algebraic group proof supplement

The canonical notes G01–G21, exact Hua-ID reconciliation, APA references, and source/version qualifications are in [MPL_133_notes.md](../MPL_133_notes.md). This supplement preserves the full mathematical checks and the per-note context table. All assertions concern the explicit categories and hypotheses stated here; none changes the frozen transcription.

## Context search record

Both ps6.tex and ps7.tex were searched for the relevant subjects, including Chevalley, anti-affine, crossed, formal group, central extension, constructibility, commutators, and cohomology notation. No exact Chevalley, anti-affine, or crossed-module classification was found. The following are actual relevant passages or expressly different nearby discussions.

| Note | Supplied file and original PS locator | Adds / repeats / differs |
|---|---|---|
| G01 | ps6.tex, §117, pp. 494–496 | Differs in category; PS separates formal and schematic objects. |
| G02 | ps6.tex, §113, pp. 468–469; §117, pp. 494–496 | Adds specific formal centre/derived questions; not consequences of those passages. |
| G03 | ps6.tex, §117, pp. 494–496 | Adds algebraization problem; repeats completion distinction. |
| G04 | ps6.tex, §119, pp. 501–502; §117, p. 495 | Repeats coboundary mechanism; differs in allowed cochains. |
| G05 | ps6.tex, §117, pp. 494–496 | Different “affine/formal” issue; no matching classification found. |
| G06 | ps6.tex, §113, pp. 468–469; §117, pp. 494–496 | Adds algebraic-group reconstruction. |
| G07 | ps6.tex, §117, pp. 494–496 | Adds character/vector classification. |
| G08 | ps6.tex, §117, pp. 494–496 | Adds finite-intersection distinction. |
| G09 | ps6.tex, §115, pp. 482, 488; §117, pp. 494–496 | Repeats coefficient/category care; no general Cartier-dual theorem there. |
| G10 | ps7.tex, §137, p. 577 | Differs: constructibility hit concerns sheaf operations. |
| G11 | ps7.tex, §137, p. 577 | Adds arithmetic fibre invariant; no such family found. |
| G12 | ps6.tex, §119, pp. 501–502 | Repeats splitting issue; adds quotient distinction. |
| G13 | ps7.tex, §137, p. 577 | Differs: sheaf constructibility; adds a family counterexample. |
| G14 | ps6.tex, §115, pp. 482, 488 | Repeats obstruction direction; differs in coefficient category. |
| G15 | ps6.tex, §113, pp. 468–469 | Adds exact centre criterion. |
| G16 | ps6.tex, §113, p. 468; §119, p. 501 | Repeats convention/extension setting; adds nonabelian restriction. |
| G17 | ps6.tex, §113, pp. 468–469 | Adds counterexample to withdrawn reduction. |
| G18 | ps6.tex, §113, pp. 468–469 | Adds cokernel computation. |
| G19 | ps6.tex, §113, pp. 468–469 | Adds verified quotient/intersection equivalences. |
| G20 | ps6.tex, §113, pp. 468–469 | Adds residual-condition test. |
| G21 | ps6.tex, §119, pp. 501–502 | Repeats central-extension setting; adds undetected directions. |

In particular, §115 at PS p. 482 uses quasi-coherent sheaves \(W(\pi_{n+1})\), while p. 488 discusses cohomology/Ext and Postnikov comparisons. Section 117 at p. 495 contrasts additive polynomials with arbitrary additive formal series \(\sum c_i t^{p^i}\). These support category restraint; they do not prove the formal assertions here.

## Appendix A — What the primary sources actually supply

All algebraic-group comparisons here concern finite-type groups over a field. The manuscript explicitly assumes a Chevalley decomposition on scan 042 and gives perfectness as sufficient. The general field theorems used in G05–G08 must not be promoted to relative theorems for arbitrary bases, and the broad Cartier-dual formula remains outside the verified scope.

For universal vector extensions, Mazur and Messing (1974, I §1.9, Proposition 1.10; §2.6, Proposition 2.6.7) treat abelian schemes over an arbitrary base and explicitly justify arbitrary-base-change compatibility. Their vector-variable universal property uses morphisms of quasi-coherent modules; in positive characteristic this does not say every additive group homomorphism between vector groups is linear.

For crossed modules, Baez and Lauda (2004, Theorem 43) describe maps inducing fixed homomorphisms \(f_0,f_1\) on the two homotopy groups by normalized 2-cochains \(b\) satisfying
\[
\delta b=f_1(a)-f_0^*(a'),
\]
and 2-isomorphisms by 1-cochains with the corresponding coboundary. Thus the difference of the \(H^3\) classes must vanish, and, once it does, fixed-data maps modulo 2-isomorphism have an \(H^2\) torsor. This concerns ordinary groups; the manuscript's relative \(H^i(B_Q/X,C)\) needs its own topology and coefficients.

Aldrovandi and Noohi (2009) supply butterflies for crossed modules of sheaves and the reversible-butterfly criterion for equivalence. This is a modern structural comparison, not proof that every reconstructed sheaf is an algebraic or formal group with the desired smoothness and finiteness properties. Noohi (2008, Theorem 14.1; Remark 15.1 and Example 15.2) also checks the classical fixed-kernel/fixed-outer-action case; his broader Theorem 14.6 is worded as a transitive \(H^2\)-action, so freeness is not inferred from that statement alone.

## Appendix B — Two complete nonconstructibility arguments

### B.1. Mixed characteristic: infinitely many primes are necessary here

This is an own deduction from the cited primary-source premises.

Let
\[
S=\operatorname{Spec}\mathbb Z[1/2],
\qquad A:\ y^2=x^3-x.
\]
The projective Weierstrass curve with its point at infinity is an elliptic scheme: its discriminant is \(64\), a unit on \(S\). The invariant differential trivializes its rank-one differential module; using elliptic self-duality, the universal vector extension has the form
\[
0\longrightarrow\mathbb G_{a,S}\longrightarrow E
\longrightarrow A\longrightarrow0.
\]
Existence and fibre compatibility are the arbitrary-base results cited from Mazur–Messing. As a vector torsor over the elliptic scheme, \(E/S\) is smooth of finite presentation with connected geometric fibres.

At the generic point \(\eta\), its universal class has an isomorphism as classifying linear map. The characteristic-zero vector test gives
\[
\operatorname{Aff}(E_\eta)=1,\qquad
\dim\operatorname{Aff}(E_\eta)=0.
\]
Here \(\operatorname{Aff}\) always denotes the largest affine quotient, avoiding the ambiguous subscript.

At each closed point \(s=(p)\), \(p\ne2\), pullback along \([p]:A_s\to A_s\) splits, giving an isogeny \(\mathbb G_a\times A_s\to E_s\). Let \(B\) be the image of the abelian factor. Then \(B\) is an abelian subvariety of dimension one, \(E_s=B\cdot\mathbb G_a\), and their intersection is finite. Since an abelian variety has no nonconstant morphism to an affine scheme, \(B\) lies in the anti-affine kernel, while
\[
E_s/B\simeq\mathbb G_a/(\mathbb G_a\cap B)
\]
is affine. Hence \(B\) is exactly the anti-affine kernel. The quotient is a one-dimensional smooth connected quotient of \(\mathbb G_a\), thus isomorphic to \(\mathbb G_a\) over the finite, hence perfect, residue field. In particular its dimension is one.

The zero locus of the integer-valued invariant
\[
s\longmapsto \dim\operatorname{Aff}(E_s)
\]
is therefore precisely \(\{\eta\}\). A constructible subset of an irreducible noetherian space containing its generic point contains a nonempty open: one of its finitely many locally closed pieces contains that point, and its closed part must be the whole space. But every nonempty open of \(\operatorname{Spec}\mathbb Z[1/2]\) contains closed points, since only finitely many primes can be excluded. Thus \(\{\eta\}\) is not constructible.

This proves nonconstructibility of a specific fibre invariant and obstructs a finite constructible stratification carrying a well-behaved family of the fibrewise affine quotients with these dimensions. It does not assert that a relative spectrum of global functions cannot be formed, nor assume that its fibres equal the affinization of each fibre; that base-change issue must remain separate.

The special extensions themselves remain nonsplit: after any base change the universal class still corresponds to the nonzero identity of the one-dimensional vector kernel. Consequently the Hua summary's special-splitting clause is unnecessary and unsupported by the manuscript. By contrast, on a DVR spectrum the generic point is open and the closed point is closed, so a single such jump is constructible; the infinite-prime base is essential to this argument.

### B.2. Equal characteristic zero: the Poincaré family

This calculation was checked against the cited family and torus-extension results. It addresses the intended non-affine scope illustrated by scan 044, not its literally affine wording.

Fix a complex elliptic curve \(A\), and let \(S=A^\vee\). The identity of \(A^\vee\) defines the Poincaré biextension of \((A^\vee,A)\) by \(\mathbb G_m\). Viewed over the first factor, this is a family
\[
1\longrightarrow\mathbb G_{m,S}\longrightarrow\mathcal E
\longrightarrow A\times S\longrightarrow0.
\]
Bertolin (2010, Proposition 2.2.3) identifies precisely the biextension class corresponding to that identity, and Lemma 1.2.2 ensures that the underlying torus torsor is a scheme. Its description as the complement of the zero section of the Poincaré line bundle shows smoothness and finite presentation over \(A\times S\), hence smoothness and finite presentation over \(S\); each fibre is connected. All residual characteristics are zero.

For a complex point \(t\in S\), let \(L_t\) be the associated degree-zero line bundle on \(A\). The extension is the corresponding \(\mathbb G_m\)-torsor, so
\[
\Gamma(\mathcal E_t,\mathcal O)
\simeq\bigoplus_{n\in\mathbb Z}H^0(A,L_t^{\otimes n}).
\]
A degree-zero line bundle on an elliptic curve has a nonzero global section only when it is trivial: a section's effective zero divisor has degree zero and hence is empty.

If \(t\) is nontorsion, only \(n=0\) contributes and the function algebra is \(\mathbb C\). If \(t\) has exact finite order \(m\), the contributing degrees are \(m\mathbb Z\); a trivialization of \(L_t^m\) identifies the function algebra with \(\mathbb C[z,z^{-1}]\). Therefore
\[
\operatorname{Aff}(\mathcal E_t)\simeq
\begin{cases}
\mathbb G_m,&t\text{ torsion},\\
1,&t\text{ nontorsion}.
\end{cases}
\]
This also agrees with the character-lattice criterion: \(\mathbb Z\to A^\vee(\mathbb C)\), \(n\mapsto nt\), is injective exactly when \(t\) is nontorsion (Brion, 2016, §5.4, equations (5.4.2)–(5.4.4), and Proposition 5.5.2).

The torsion subgroup of a complex elliptic curve is infinite and countable: it is the union of the finite \(n\)-torsion groups. Its complement is infinite, since the curve has uncountably many complex points. Every infinite constructible subset of an irreducible algebraic curve contains a nonempty open subset and is therefore cofinite in its closed points. The torsion locus is not cofinite, so it is not constructible.

Thus even the dimension of the largest affine quotient need not be constructible in an equal-characteristic-zero smooth connected family. This is stronger than merely observing that scan 044 lacks a proof of its blanket equal-characteristic sentence. The argument does not rule out valid more restricted constructibility results, for example linear-rank strata in fixed vector-extension families.

## Appendix C — Ordinary-group proofs for scans 047–054

### C.1. Hypotheses and notation

Let \(N\triangleleft G\), \(N'\le Z(G)\), and put
\[
C=N\cap N',\quad Q=G/NN',\quad
M=G/N',\quad M'=G/N,\quad K=G/C.
\]
Conjugation on \(N\) factors through \(\theta:M\to\operatorname{Aut}(N)\). The natural map identifies
\[
K\simeq M\times_Q M':
\]
its kernel is \(C\), and compatible representatives can be adjusted by elements of \(N\) and \(N'\) to give a common lift. Thus \(K\) is determined by the quotient data. In C.4–C.6 also assume \(G'=[G,G]\subseteq N\); then \(M'\) and \(Q\) are abelian. Use \([g,h]=ghg^{-1}h^{-1}\).

### C.2. Centre injectivity

Define
\[
\zeta=\operatorname{im}(Z(K)\to M)\cap\ker\theta.
\]
Because \(N'/C\le Z(K)\), the first subgroup is exactly the source's \(Z(K)/(N'/C)\). For \(z\in\zeta\), a lift \(g\in G\) satisfies
\[
[g,G]\subseteq C,\qquad [g,N]=1.
\]
For \(q\in Q\) and a lift \(h\in G\), set \(\psi(z)(q)=[g,h]\). Changing \(g\) by an element of central \(N'\), or \(h\) by an element of \(NN'\), has no effect. Since the commutators lie in central \(C\), the commutator identities show that \(\psi:\zeta\to\operatorname{Hom}(Q,C)\) is a homomorphism.

It vanishes on \(z\) exactly when \(g\) is central in \(G\). Hence
\[
1\longrightarrow Z(G)/N'\longrightarrow\zeta
\xrightarrow{\psi}\operatorname{Hom}(Q,C)
\]
is exact at \(\zeta\); there is no claim that its last map is onto. This proves \(N'=Z(G)\) iff \(\psi\) is injective, without requiring \(Q\) abelian.

For the importance of the correction, take \(G=Q_8\), \(N=1\), \(N'=Z(G)\). Then \(C=1\), and the uncorrected \(Z(M)\cap\ker\theta=M\) is nontrivial, although its map to \(\operatorname{Hom}(Q,1)\) is zero and \(N'=Z(G)\). The corrected \(\zeta\) is trivial. If additionally \(G'\subseteq N\), centrality modulo \(N'\) already puts commutators in \(N\cap N'\), so the correction is redundant in that narrower setting.

### C.3. Twisting and cancellation

Let \(E\) be a central extension of \(Q\) by \(C\). Lifts of commuting elements of \(Q\) have commutator in \(C\), independent of the lifts. For abelian \(Q\) this gives an alternating bilinear map \(c_E:Q\times Q\to C\); for arbitrary \(Q\), restriction to \(Z(Q)\times Q\) suffices for the central image of \(\alpha:\zeta\to Q\).

Twisting uses \(G\times_Q E\), followed by quotient by the antidiagonal copy of \(C\). Commutators in the product add, giving, with the stated convention,
\[
\psi_{\mathrm{twist}}(z)(q)
=\psi_G(z)(q)+c_E(\alpha(z),q).
\]
Interchanging arguments or conventions changes the sign, exactly as flagged on scan 049.

The cancelled condition \(N'=Z(H)\), \(H=NN'\), is not necessary: for \(G=S_3\), \(N=A_3=G'\), and \(N'=1\), one has \(N'=Z(G)\) but \(Z(H)=A_3\ne1\). The live proof above never uses that condition.

### C.4. Derived surjectivity

Now assume \(G'\subseteq N\). Put
\[
N_0=[G,N],\qquad\eta=N/[G,N]=(N_{\mathrm{ab}})_M.
\]
The subgroup \([G,N]\) contains \([N,N]\), is normal in \(G\), and is contained in \(G'\). It is exactly the quotient required to make \(N\) abelian with trivial \(G\)-action. Thus
\[
1\longrightarrow\eta\longrightarrow G/[G,N]\longrightarrow M'
\longrightarrow1
\]
is central with abelian quotient. Commutators of lifts give an alternating bilinear pairing on \(M'\); centrality of \(N'\) makes it factor through
\[
\lambda:Q\otimes Q\longrightarrow\eta,
\]
indeed through \(\bigwedge^2 Q\). Its image is precisely \(G'/[G,N]\), since this subgroup is generated by those commutators. Consequently
\[
\operatorname{coker}\lambda
\simeq (N/[G,N])/(G'/[G,N])\simeq N/G'.
\]
This is the scan-053 criterion.

### C.5. The “Vérifier” equivalences

Let
\[
C_*=\operatorname{im}(C\to\eta),\qquad
\eta_0=\eta/C_*=N/(C[G,N]).
\]
The image of \(\lambda_0\) is \(G'C/(C[G,N])\). Thus
\[
\lambda_0\text{ onto}\iff N=G'C
\iff N/C=(G/C)'.
\]
For \(d:N\to M=G/N'\), the image is \(d(N)=NN'/N'\), while \(D(M)=G'N'/N'\). Therefore \(d(N)=D(M)\) iff \(NN'=G'N'\). Intersecting with \(N\), and using \(G'\subseteq N\), gives
\[
N\cap G'N'=G'(N\cap N')=G'C.
\]
This verifies all the displayed equivalences for ordinary groups with the stated hypotheses. Here \(M'\) denotes the source's second quotient \(G/N\), not the derived subgroup of \(M\).

### C.6. The remaining epimorphism

Suppose \(\lambda_0\) is onto and put \(P=\ker\lambda_0\). Then \(\lambda(P)\subseteq C_*\), every element of \(\eta\) differs from one in \(\operatorname{im}\lambda\) by an element of \(C_*\), and
\[
C_*\cap\operatorname{im}\lambda=\lambda(P).
\]
Hence \(\operatorname{coker}\lambda\simeq C_*/\lambda(P)\). Surjectivity of the residual map is necessary and sufficient, not automatic.

For \(G=C_p\times C_p\) and \(N=N'=C_p\times1\), one has \(C=N\), \([G,N]=1\), \(\eta=C\ne0\), \(Q=C_p\), and \(\eta_0=0\). Thus \(\lambda_0\) is onto zero while every commutator and the residual map are zero.

Twisting changes \(\lambda\) by \(\beta c_E\); restricting to \(P\) gives scan 054's residual formula. If \(E\) is commutative, \(c_E=0\), explaining why these tests do not detect every \(H^2\)-direction.

## Appendix D — Conditional Barsotti–Tate diagnostic

Work in abelian fppf sheaves over a characteristic-p field, not an unspecified narrower formal-group category. For the constant étale p-divisible group \(P=\mathbb Q_p/\mathbb Z_p\), push out
\[
0\longrightarrow\mathbb Z/p\longrightarrow P
\xrightarrow{p}P\longrightarrow0
\]
along the nonzero homomorphism \(\mathbb Z/p\to\mathbb G_a\), \(1\mapsto1\). Since \(p:P\to P\) is an epimorphism and \(\mathbb G_a\) is killed by p, \(\operatorname{Hom}(P,\mathbb G_a)=0\). The Hom/Ext exact sequence therefore gives an injection
\[
\operatorname{Hom}(\mathbb Z/p,\mathbb G_a)
\hookrightarrow\operatorname{Ext}^1(P,\mathbb G_a).
\]
The pushed-out extension is nonsplit although its kernel is smooth and unipotent. This tests the unrestricted modern reading of the first sentence on scan 036; it does not decide a connected-formal interpretation, the a-torique condition, or the second statement in an isogeny category.

