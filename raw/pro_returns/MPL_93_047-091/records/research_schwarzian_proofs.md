# Supporting checks for the SC research notes (research only)

Date: 18 November 2026. Author: ChatGPT research agent, independent of the frozen transcription. All page references below mean cote 93 scan numbers. No scan image was inspected in this research phase, and no transcription file was edited. These are mathematical checks of the frozen text, not proposed silent corrections to it.

## C1. An integral three-jet identity

For Hasse jets put

\[
 Q(j_1,j_2,j_3)=-j_3/j_1+(j_2/j_1)^2,
 \qquad N(j)=j_2^2-j_1j_3.
\]

For the jets \(a_i\) of a function and \(b_i\) of a substituted coordinate, composition gives

\[
 c_1=a_1b_1,\quad c_2=a_1b_2+a_2b_1^2,
 \quad c_3=a_1b_3+2a_2b_1b_2+a_3b_1^3.
\]

Expansion over \(\mathbb Z[a_1,a_2,a_3,b_1,b_2,b_3]\) gives

\[
 N(c)=a_1^2N(b)+b_1^4N(a).
\]

The two mixed terms \(2a_1a_2b_1^2b_2\) cancel. After localizing at \(a_1b_1\), this becomes

\[
 Q(F\circ g)=Q(g)+(g')^2(Q(F)\circ g).
\]

Thus differences \((Q_t(g)-Q_t(f))dt^2\) are independent of the chosen étale coordinate and satisfy the additive cocycle identity by telescoping. These are identities of integral jet algebras, and therefore specialize to every commutative base ring. No division by 2, 3, or 12 occurs in this construction. An étale coordinate on a smooth relative curve supplies the Taylor/Hasse operators locally; the coordinate-change identity is exactly the compatibility needed to glue the quadratic differential. This verifies the formula-level existence and cocycle claim, not the full uniqueness theorem of scans 072–074 or a global surjectivity assertion in an algebraic topology.

For \(M(z)=(az+b)/(cz+d)\), let \(\Delta=ad-bc\) and \(u=cz+d\). Taylor expansion gives

\[
 D^{(1)}M=\Delta/u^2,\quad D^{(2)}M=-c\Delta/u^3,
 \quad D^{(3)}M=c^2\Delta/u^4.
\]

Hence \(N(M)=0\), integrally. With the chain law this proves invariance under constant/base-defined homographies where their denominators and first derivatives are units. The same calculation works when the coefficients are annihilated by the first three Hasse operators, with the usual corresponding truncated product rules.

## C2. The factor 12 and the two test values

The identities \(f''=2D^{(2)}f\) and \(f'''=6D^{(3)}f\) imply

\[
 -2f'''/f'+3(f''/f')^2=12Q(f).
\]

Accordingly \(G=12G_0\) is an integral identity; \(G_0=G/12\) is only a mnemonic when 12 is not invertible. In characteristic 2 or 3 the left side is identically zero, while \(G_0\) need not vanish. Direct calculation gives

\[
 G_0(t,t^2)=\frac{dt^2}{4t^2},\qquad
 G_0(t,t^3)=\frac{2\,dt^2}{3t^2}.
\]

The first is defined on the locus where \(2t\) is a unit and contradicts the final \(1/(2t)\) in scan 073. The second is defined where \(3t^2\) is a unit, and reduces to zero in characteristic 2; it does not by itself witness nonvanishing there. Such witnesses are \(s=t+t^2\) in characteristic 2, giving \(Q=1\), and \(s=t+t^3\) in characteristic 3, giving \(Q=-1\).

## C3. Classical local rigidity and surjectivity

The classical convention is \(S(f)=f'''/f'-(3/2)(f''/f')^2\); the manuscript uses \(G(t,f)=-2S(f)dt^2\). On a complex analytic coordinate disc, the equation \(G(t,g)=q(t)dt^2\) is obtained by taking the ratio of two independent solutions of

\[
 y''-\tfrac14q(t)y=0.
\]

Their nonzero Wronskian makes the ratio locally univalent. Two ratios for the same second-order equation differ by a constant Möbius transformation; prescribing the same value, first derivative and second derivative fixes that transformation. This proves the local analytic existence and rigidity used in scan 072 for the displayed invariant. The local solutions need not glue to a single globally defined coordinate on a non-simply-connected domain. Dumas, §§3.1–3.2, is the primary published reference for this classical framework: [source](https://arxiv.org/pdf/0902.1951). The explicit normalization above is our calculation, not a quotation or a claim about p-curvature.

## C4. Translation, logarithmic, and connection checks

For \(A(f,g)=dg-df\) and fixed étale \(f\), the target value \(-df\) would require \(dg=0\). Thus the map from étale coordinates to all one-forms in scan 075 fails to be locally surjective. Scan 076's replacement by the ratio of bases fixes this particular issue: \(dg/df\) is a unit, and locally integrating any nonzero analytic one-form supplies an étale \(g\).

If \(e\) is a frame and \(D_e e=0\), the standard connection satisfying this condition is \(D_e(h)=e\,d(h/e)\). Consequently

\[
 D_g-D_f=-d\log(g/f).
\]

The positive logarithmic differential in scans 076, 078 and 082 is valid as an invariant, but its identification with \(D_g-D_f\) has the opposite sign under this convention. Scan 082's \(\beta_n=D_{dt}-(1/n)d\log f\) is consistent with horizontality. One must state a different convention to keep the other sign; this does not authorize changing uncertain manuscript signs.

In scan 077, \((dg/g)/(df/f)=(dg/df)(f/g)\). The printed \((dg/df)(g/f)\) gives \(2t^2\) when \(f=t,g=t^2\), whereas the left side is 2. On the nonvanishing étale locus, \(d\log g\) is a basis and local logarithmic integration is possible. On all étale coordinates \(g/dg\) cannot be identically zero, so the author's rejection of surjectivity is justified.

## C5. The coefficients on scans 080 and 082

For \(\psi=f\,dt^n\), set \(\lambda=-(1/n)f'/f\), with \(n\ne0\) in the complex analytic setting. Then

\[
 2\lambda'+\lambda^2=-\frac2n\frac{f''}{f}
 +\frac{2n+1}{n^2}\left(\frac{f'}f\right)^2.
\]

This checks \(c_n\), the coefficient \(2n+1\), and \(5/4\) for \(n=2\). It also proves

\[
 c_{nr}(\psi^r)=c_n(\psi),\qquad
 \delta(fdt^2)=c_t+[f-f''/f+(5/4)(f'/f)^2]dt^2,
\]

and

\[
 \delta((fdt)^2)=c_t+[f^2-2f''/f+3(f'/f)^2]dt^2.
\]

The variation formula in scan 082 is consistent with the ordinary induced connection on \(\omega\): if \(D=D_{dt}+\lambda dt\) and \(\eta=hdt\), then \(D\eta=(h'+\lambda h)dt^2\), and

\[
 [2(\lambda+h)'+(\lambda+h)^2]-[2\lambda'+\lambda^2]
 =2(h'+\lambda h)+h^2.
\]

For scan 080's \(G_{m,n}\), take \(m=1,n=2,f=t,g=t^2\), away from zero. The two associated root differentials coincide, so the correct difference is zero. Keeping the printed \((g'/g)^2\) in the second term instead gives \(-9dt^2/t^2\); this is a concrete counterexample to that displayed equality, not an inference about its handwriting. The later \(G'_{m,n}\) reverses the order of the two terms and has the opposite sign from \((\delta^2/12)G_{m,n}\).

The exponential identity is also a direct consequence of the chain law: \(S(\exp z)=-1/2\), so \(G(t,e^u)-G(t,u)=(du)^2\). It explains the added \(\omega_2\) in \(\delta\). This repeats the earlier context note P02 and carries no p-curvature implication.

## C6. Kernel of the first three Hasse operators

Let \(A\) be any \(\mathbb F_p\)-algebra, with Hasse operators relative to \(A\) on \(A[t]\). The kernel of \(D^{(1)},D^{(2)},D^{(3)}\) is \(A[t^p]\) for \(p>3\), \(A[t^4]\) for \(p=2\), and \(A[t^9]\) for \(p=3\). Indeed \(D^{(1)}\) eliminates exponents not divisible by \(p\); in characteristic 2, \(\binom{2k}{2}=k\pmod2\), and in characteristic 3, \(\binom{3k}{3}=k\pmod3\), give exactly the extra factor. Conversely every surviving exponent has zero binomial coefficients for orders 1–3. Distinct monomials cannot cancel in any one Hasse derivative, and every nonzero element of \(\mathbb F_p\) is a unit in \(A\), so this proof permits nilpotents in \(A\).

The notation \(A[t^q]\) here is a relative Frobenius image, with arbitrary coefficients from \(A\), and need not equal the subring of literal q-th powers when \(A\) is imperfect. This distinction matters when reading Hua's \(\mathcal O_X^{p^e}\).

## C7. Arbitrary-ring rigidity in the nilpotent model

Let \(q=p\) for \(p>3\), \(q=4\) for \(p=2\), or \(q=9\) for \(p=3\). Put \(B=A[t]/(t^q)\) for an arbitrary \(\mathbb F_p\)-algebra \(A\). The first three Hasse operators descend because \((t+z)^q=t^q+z^q\) and \(q>3\). Suppose \(s=a_0+a_1t+a_2t^2+\cdots\), \(D^{(1)}s\in B^*\), and \(N(s)=0\). Then \(a_1\) is a unit. The homography

\[
 h(t)=a_0+\frac{a_1t}{1-rt},\qquad r=a_2/a_1,
\]

has the same two-jet as \(s\), determinant \(a_1\), unit denominator, and zero \(Q\). Its inverse is defined at \(s\), since its denominator there has constant term \(a_1\). Set \(u=h^{-1}(s)=t+\sum_{d\ge3}b_dt^d\). The integral chain law gives \(Q(u)=Q(s)=0\).

Inductively suppose the coefficients below degree \(d\) vanish. The coefficient of \(t^{d-3}\) in \((D^{(2)}u)^2-D^{(1)}uD^{(3)}u\) is \(-\binom d3b_d\): the square term starts in degree \(2d-4>d-3\), and the nonconstant part of \(D^{(1)}u\) only contributes higher degree. For \(3\le d<q\), \(\binom d3\) is a unit: for \(p>3\) its numerator has no factor \(p\), for \(p=2,q=4\) it is 1, and for \(p=3,q=9\) its residues are \(1,1,1,2,2,2\). Thus every \(b_d=0\), and \(s=h(t)\). This is an independent proof over arbitrary \(A\); the finite enumeration below is a separate diagnostic, not its justification.

## C8. Own repair of the arbitrary-α descent step

**Statement proved here and independently reviewed by the root agent on 18 November 2026 for exactly this monic model:** with \(p,q,A\) as in C7, let \(\alpha\in A\), \(B=A[t]/(t^q-\alpha)\), and let \(s\in B\) satisfy \(D^{(1)}s\in B^*\), \(N(s)=0\). If \(\operatorname{Pic}(A)=0\), there are \(a,b,c,d\in A\) with \(ad-bc\in A^*\), \(ct+d\in B^*\), and \(s=(at+b)/(ct+d)\). There is no asserted determinant-one normalization. This supplies an argument missing from Hua's reported reduction and concerns later, unsupplied manuscript pages; it is not a proof written in scans 072–074.

1. Set \(A'=A[u]/(u^q-\alpha)\). It is a free \(A\)-module of rank \(q\), hence faithfully flat. In \(B'=B\otimes_AA'\), put \(v=t-u\); Frobenius gives \(v^q=0\), so \(B'=A'[v]/(v^q)\). The first three Hasse operators are relative to \(A'\) after base change and obey \(D_t^{(i)}=D_v^{(i)}\), since \(u\) is constant for these operators. The truncated Taylor algebra construction descends modulo \(t^q-\alpha\) because \(q>3\).

2. Apply C7 to \(s\in B'\). It yields \(M'\in\operatorname{GL}_2(A')\) and a unit denominator such that \(M'\cdot t=s\); the change from \(v\) to \(t=v+u\) is itself an invertible affine matrix over \(A'\).

3. Define an \(A\)-linear map \(A^4\to B\) by

   \[
   (a,b,c,d)\longmapsto (ct+d)s-(at+b)
   \]

   and let \(K\) be its kernel. Flatness implies \(K\otimes_AA'\) is exactly the corresponding kernel over \(A'\). Every matrix \(N\) in this latter kernel is a scalar multiple of \(M'\), **including singular matrices**: write \(N=M'R\), where \(R=(r_{ij})\), and let \(w=(t,1)^T\). The kernel condition says \(Nw\wedge M'w=0\), since the second coordinate of \(M'w\) is a unit. Multiplication by \(M'^{-1}\) turns this into \(Rw\wedge w=0\), that is

   \[
   -r_{21}t^2+(r_{11}-r_{22})t+r_{12}=0.
   \]

   Because \(q\ge4\), the classes of \(1,t,t^2\) are linearly independent over \(A'\) in the monic quotient \(B'\). Therefore \(r_{21}=r_{12}=0\) and \(r_{11}=r_{22}\), proving \(K\otimes_AA'=A'M'\) freely. This argument does not divide by a coefficient of \(N\), so it handles zero divisors and noninvertible \(N\).

4. Faithfully flat descent of finite projective modules shows \(K\) is finite projective; its rank is one after the surjective base change, hence one everywhere. The exact external theorem used is Stacks Project, Proposition 10.83.3, [source](https://stacks.math.columbia.edu/tag/058Q). The hypothesis \(\operatorname{Pic}(A)=0\) now makes \(K\) free of rank one. Choose a generator \(M=(a,b;c,d)\); after base change it is \(\lambda M'\) for some \(\lambda\in A'^*\), since both are bases of the same rank-one module. Thus \(\det M\) becomes a unit in \(A'\), and \(ct+d\) becomes a unit in \(B'\). Both were already units in \(A\) and \(B\), respectively, because invertibility descends under faithful flatness: the cokernel of multiplication by either element becomes zero, so is zero. Finally \(M\in K\) gives the desired equality in \(B\).

The converse follows from C1. Without \(\operatorname{Pic}(A)=0\), the proof produces a line of matrix coefficients \(K\); it does not by itself provide four global scalar coefficients. This explains precisely where the Picard hypothesis enters. This is an ordinary written proof using one cited descent theorem, not a proof-assistant certificate.

## C9. Actual computation record

The reproducible script is `schwarzian_checks.py`; its raw result is `schwarzian_checks_output.json`. It was executed successfully on 18 November 2026 with exact SymPy arithmetic. It checked the universal rational jet identity, \(G-12G_0\), the two test values, Möbius vanishing, the \(c_n\) and power-compatibility formulas, the 077 ratio counterexample, and the 080 counterexample.

It also exhaustively enumerated all elements with unit first derivative in three rings:

| Ring | Unit-derivative elements checked | Elements with \(N=0\) | Möbius forms among those |
|---|---:|---:|---:|
| \(\mathbb F_2[t]/t^4\) | 8 | 4 | 4 |
| \(\mathbb F_3[t]/t^9\) | 13,122 | 18 | 18 |
| \(\mathbb F_5[t]/t^5\) | 2,500 | 100 | 100 |

The comparison form was \(a_0+a_1t/(1-rt)\), with \(r=a_2/a_1\). These finite checks do not establish arbitrary-base descent or uniqueness of all differential invariants. No Lean file from Hua's project was obtained or executed.

## C10. Scope and provenance

The actual scans 072–074 state the divided-derivative formula and its proposed universal properties. They contain no explicit \(p\)-versus-\(p^2\) homography theorem. The latter enters through **Hua, modernised reading of cote 93**, `context/hua_project/93.modern.tex`, IX, “L'injectivité en caractéristique p (pages 121 à 123)”, and **Hua, findings register, 93-integral-schwarzian-level-p2**, recorded as a candidate in `context/notes/RESULTS_STATE.md`. C6–C8 are checks and a further argument prompted by that lead. They establish a monic local algebra statement, not every global sheaf or projective-connection assertion in the later manuscript.

Prior notes P05 and P06 remain credited to `context/same_cote_93/MPL_93_002-046_notes.md`: their p-curvature warning was used as background and was not re-proved here. No p-curvature conclusion follows from the checks in this record alone.

## C11. Conditional interpretation of the genus counts

For a smooth projective connected complex curve of genus \(g\ge2\), let \(K\) be its canonical line bundle. Riemann–Roch and duality give

\[
 h^0(K^2)-h^0(K^{-1})=\deg(K^2)+1-g=3g-3.
\]

Since \(K^{-1}\) has negative degree, its space of sections is zero; also \(h^0(K)=g\) and \(h^0(\mathcal O)=1\). Thus the direct sum \(K^2\oplus K\oplus\mathcal O\) has \(4g-2\) sections. The cited input is [Stacks Project, Lemma 53.5.2](https://stacks.math.columbia.edu/tag/0B5B). This is only a conditional explanation of the numbers on scan 081, not a reconstruction of its unspecified bundles or of the cancelled numerical matrix.
