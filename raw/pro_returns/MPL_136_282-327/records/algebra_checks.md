# Algebra checks made after the transcription freeze

These are the reader's calculations, not manuscript text and not claims of novelty. They use the frozen coefficient relation on cote 136, scan 299, and the explicit convolution question on scan 324. The current page files are not changed by any calculation below. The two main arguments were independently checked by the research subagent after the context was opened.

## A. Negative-degree reconstruction from scan 299

### Statement and scope

Let \(h\) be any commutative ring, let \(M\) be any \(h\)-module, and put
\[
S=\Gamma_h(T)=\bigoplus_{i\geq0}hT^{[i]},\qquad
T^{[i]}T^{[j]}=\binom{i+j}{i}T^{[i+j]}.
\]
Interpret the right-adjoint calculation on scan 299 in the category of all \(\mathbb Z\)-graded \(S\)-modules. For every integer \(d>0\), its degree \(-d\) term is naturally
\[
\operatorname{Hom}^{-d}_S(\tau_dS,M\otimes_hS)
\cong \operatorname{Hom}_{\mathbb Z}(\mathbb Q,M).
\]
The \(h\)-action on the right is on the target. This is **not** \(M\otimes\mathbb Q\), and it is not just the subgroup of \(M\) obtained by evaluating at 1.

### Reduction to a presented abelian group

A homogeneous map has the form
\[
u(T^{[i]})=\xi_iT^{[i-d]},\qquad i\geq d.
\]
Its \(S\)-linearity is exactly the boxed recurrence on scan 299:
\[
\binom ji\xi_j=\binom{j-d}{i-d}\xi_i\qquad(j\geq i\geq d).
\]
Let \(R_d\) be the abelian group with generators \(e_i\), \(i\geq d\), and these relations:
\[
\binom ji e_j=\binom{j-d}{i-d}e_i.
\]
Then the desired compatible families are
\(\operatorname{Hom}_h(h\otimes_{\mathbb Z}R_d,M)\).

Define \(v:R_d\to\mathbb Q\) by
\[
v(e_i)=\binom id^{-1}.
\]
This respects the relations, since
\(\binom ji/\binom jd=\binom{j-d}{i-d}/\binom id\).

### Prime-local proof that \(v\) is an isomorphism

Fix an integer prime \(p\) and a finite set of generator indices. Choose \(r\) large enough that \(j=p^r+d-1\) exceeds them all. For every such \(i\),
\[
\binom{j-d}{i-d}=\binom{p^r-1}{i-d}
\]
is a unit in \(\mathbb Z_{(p)}\). One elementary proof is to expand
\((1+X)^{p^r-1}\equiv(1+X^{p^r})/(1+X)\pmod p\), whose coefficients below degree \(p^r\) alternate between \(1\) and \(-1\).
Consequently every finite linear combination of the \(e_i\) in \(R_d\otimes\mathbb Z_{(p)}\) is a scalar multiple of \(e_j\). If its image in \(\mathbb Q\) is zero, that scalar is zero, because \(v(e_j)\ne0\); this proves injectivity.

For \(p^r>d-1\),
\[
v_p\binom{p^r+d-1}{d}=r-v_p(d).
\]
Indeed the numerator is \(p^r(p^r+1)\cdots(p^r+d-1)\), and the nonzero terms have the same \(p\)-adic valuations as \(1,\ldots,d-1\). These valuations are unbounded with \(r\), so the image contains arbitrary \(p\)-power denominators over \(\mathbb Z_{(p)}\), and is all of \(\mathbb Q\). Thus \(v\) is an isomorphism after localization at every prime; its kernel and cokernel are therefore zero.

Finally,
\[
\operatorname{Hom}_h(h\otimes\mathbb Q,M)
\cong\operatorname{Hom}_{\mathbb Z}(\mathbb Q,M)
\]
by the tensor–Hom adjunction. No flatness of \(M\), \(h\), or \(h\otimes R_d\) was used.

### Consequences and relation to prior work

For \(M=\mathbb Z\), the negative terms vanish; for a rational vector space \(M\), they equal \(M\); for \(M\) of bounded torsion exponent, they vanish. For \(M=\mathbb Q/\mathbb Z\), they need not vanish, and evaluation at 1 is not injective: the quotient map \(\mathbb Q\to\mathbb Q/\mathbb Z\) is nonzero but has value zero at 1.

The earlier unreviewed `same_cote_136/MPL_136_235-281_notes.md`, N21–N22 (scans 275, 277, 279), already claims degree-zero rigidity and finite-tail recovery **in nonnegative degrees**, and gives the rational Laurent example as a warning about the all-graded category. The present calculation adds the precise negative-degree functor suggested by scan 299; it does not re-prove the earlier degree-zero result or settle the monoidal derived reconstruction in **gap g1048**. It also does not resolve the ambiguous exponent in two unboxed lines of the frozen transcription.

## B. A nonflat coalgebra for which the convolution ideal has no divided powers

### The question and the affirmative finite-projective case

Scan 324 asks whether \(\operatorname{Hom}_h(A,J)\) has divided powers, where \(A\) is a counital cocommutative coalgebra and \((B,J,\gamma)\) is a divided-power algebra. If \(A\) is finite projective over \(h\), the answer is affirmative: convolution identifies \(\operatorname{Hom}_h(A,B)\) with \(A^\vee\otimes_hB\), and \(\operatorname{Hom}_h(A,J)\) with the extended ideal \(A^\vee\otimes_hJ\). The map \(B\to A^\vee\otimes_hB\) is flat, so the divided powers extend uniquely (The Stacks Project Authors, n.d., Lemma 23.4.2, [Tag 07H1](https://stacks.math.columbia.edu/tag/07H1)).

The following example shows that an unrestricted affirmative answer is false if “coalgebra” permits nonflat underlying modules. It is a mathematical test of that interpretation, not evidence that Grothendieck intended to omit a standing flatness convention.

### The coalgebra

Over \(\mathbb Z\), set
\[
A=\mathbb Z\,1\oplus(\mathbb Z/2)\,e,
\quad
\Delta(1)=1\otimes1,
\quad
\Delta(e)=e\otimes1+1\otimes e+e\otimes e,
\quad
\epsilon(1)=1,\quad\epsilon(e)=0.
\]
This is coassociative, counital, and cocommutative. To check coassociativity without an expansion, take the free coalgebra on the two group-like elements \(1,g\), quotient by the coideal generated by \(2(g-1)\), and put \(e=g-1\). The coideal assertion follows from
\[
\Delta(2(g-1))=2(g-1)\otimes g+1\otimes2(g-1).
\]

### The divided-power algebra

Let
\[
B=\mathbb Z\oplus(\mathbb Z/2)t\oplus(\mathbb Z/4)u,
\quad t^2=2u,\quad tu=u^2=0,
\quad J=(t,u).
\]
The given additive group and multiplication define a commutative unital ring: in particular \(2t=0\) is compatible with \(t^2=2u\), since \(4u=0\). Define
\[
\gamma_1(x)=x,\qquad
\gamma_2(at+bu)=a^2u,\qquad
\gamma_n(x)=0\ (n\geq3),\qquad \gamma_0(x)=1.
\]
Here \(a\) is taken modulo 2 and \(b\) modulo 4. The square \(a^2u\) is independent of the chosen lift of \(a\), since replacing \(a\) by \(a+2k\) changes its square by a multiple of 4.

For \(x=at+bu\) and \(y=a't+b'u\), one has \(xy=2aa'u\). Hence
\(\gamma_2(x+y)=\gamma_2(x)+xy+\gamma_2(y)\), and \(x^2=2\gamma_2(x)\). If \(c=n+rt+su\in B\), then
\(\gamma_2(cx)=n^2a^2u=c^2\gamma_2(x)\). All other nontrivial-looking divided-power product, addition, and composition identities vanish because \(uJ=0\), \(u^2=0\), and the higher \(\gamma_n\) vanish. In particular \(\gamma_2(\gamma_2(x))=0=3\gamma_4(x)\). Thus \(J\) is genuinely a divided-power ideal, using the axioms of The Stacks Project Authors (n.d.), Definition 23.2.1, [Tag 07GL](https://stacks.math.columbia.edu/tag/07GL).

### The obstruction in convolution

Let \(f:A\to J\) be given by \(f(1)=0\), \(f(e)=t\); this is well defined because \(2t=0\). In the convolution ring,
\[
(f*f)(e)
=m_B(f\otimes f)\Delta(e)
=t^2=2u\ne0.
\]
But every group homomorphism \(v:A\to B\) satisfies \(2v(e)=v(2e)=0\). Consequently \(f*f\ne 2v\) for **every** \(v\in\operatorname{Hom}_{\mathbb Z}(A,B)\). The necessary divided-power identity \(f^2=2\gamma_2(f)\) cannot hold, so \(\operatorname{Hom}_{\mathbb Z}(A,J)\) admits **no** divided-power ideal structure at all.

### What this does and does not settle

This refutes the unrestricted version of the first question on scan 324 while preserving the finite-projective case explicitly suggested there. It supplies a flatness/finiteness diagnostic for the universal elements on 320–325 and for the classification programme in **claims #243**; it does not refute a theory restricted to free or flat representing coalgebras, and it does not decide the weighted cochain comparison in **follow-ups @305**. No assertion of historical or mathematical novelty is made.

## C. A finite-cutoff warning for tensor compatibility

In the ordinary category of \(\mathbb Z\)-graded \(k\)-vector spaces (the special case \(S=k\)), let \(K\) be \(k\) in degree \(-1\) and \(L\) be \(k\) in degree \(1\). Then \(\tau_0K=0\), but \(\tau_0(K\otimes L)=k\) in degree zero. Therefore the finite-cutoff functor of scans 287–293 is not strong monoidal for the ordinary graded tensor on the entire all-graded category, and its kernel is not a tensor ideal there. This elementary example adds a constraint to **gap g1048** without prejudging a suitably restricted or repaired stable quotient, which is a different construction.
